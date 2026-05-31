#!/usr/bin/env python3
"""Generate Mermaid diagrams from LinkML schema YAML for README and docs."""

from __future__ import annotations

import argparse
import difflib
import re
import shutil
import sys
import tempfile
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_module_pages import load_modules, slug_from_id  # noqa: E402

ROOT_SCHEMA = "00_pragmatic_bim_data_contract.yaml"
BASE_URL = "https://schema.pragmaticbim.ch"
README_MARKERS = {
    "module-map": "module-map",
    "entity-overview": "entity-overview",
}
PREAMBLE_MARKER = "<!-- schema-diagrams-preamble -->"


def load_root_imports(schema_dir: Path) -> list[str]:
    root_path = schema_dir / ROOT_SCHEMA
    root = yaml.safe_load(root_path.read_text(encoding="utf-8")) or {}
    imports = root.get("imports", [])
    result: list[str] = []
    for item in imports:
        if isinstance(item, str) and not item.startswith("linkml:"):
            result.append(item)
    return result


def load_class_graph(schema_dir: Path) -> tuple[dict[str, str], dict[str, str]]:
    """Return (parents, module_by_class) for all classes across imported modules."""
    parents: dict[str, str] = {}
    module_by_class: dict[str, str] = {}
    for import_name in load_root_imports(schema_dir):
        schema_file = schema_dir / f"{import_name}.yaml"
        if not schema_file.exists():
            continue
        doc = yaml.safe_load(schema_file.read_text(encoding="utf-8")) or {}
        module_id = doc.get("id")
        slug = slug_from_id(str(module_id).strip(), BASE_URL) if isinstance(module_id, str) else import_name
        classes = doc.get("classes", {})
        if not isinstance(classes, dict):
            continue
        for class_name, class_body in classes.items():
            module_by_class[class_name] = slug or import_name
            if isinstance(class_body, dict):
                parent = class_body.get("is_a")
                if isinstance(parent, str) and parent.strip():
                    parents[class_name] = parent.strip()
    return parents, module_by_class


def module_for_import(schema_dir: Path, import_name: str, modules: list[dict]) -> dict | None:
    schema_file = schema_dir / f"{import_name}.yaml"
    if not schema_file.exists():
        return None
    doc = yaml.safe_load(schema_file.read_text(encoding="utf-8")) or {}
    module_id = doc.get("id")
    if not isinstance(module_id, str):
        return None
    slug = slug_from_id(module_id.strip(), BASE_URL)
    for module in modules:
        if module["slug"] == slug:
            return module
    return {
        "slug": slug or import_name.replace("_schema", "").replace("_", "-"),
        "title": doc.get("title") or import_name,
        "source_file": schema_file.name,
    }


def mermaid_label(text: str) -> str:
    escaped = text.replace('"', "'")
    return f'["{escaped}"]'


def render_module_map(modules_in_root: list[dict], *, interactive: bool = False) -> str:
    lines = ["flowchart TB", "  Root[\"Pragmatic BIM Data Contract\"]"]
    for module in modules_in_root:
        slug = module["slug"]
        node_id = slug.replace("-", "_")
        title = str(module.get("title") or slug)
        short = title.split(" - ")[-1] if " - " in title else title
        lines.append(f"  Root --> {node_id}{mermaid_label(short)}")
        if interactive:
            lines.append(f'  click {node_id} href "./{slug}.html" _blank')
    return "\n".join(lines) + "\n"


def render_class_diagram(edges: set[tuple[str, str]]) -> str:
    lines = ["classDiagram"]
    for child, parent in sorted(edges):
        lines.append(f"  {parent} <|-- {child}")
    return "\n".join(lines) + "\n"


def all_is_a_edges(parents: dict[str, str]) -> set[tuple[str, str]]:
    known = set(parents.keys())
    for parent in parents.values():
        known.add(parent)
    edges: set[tuple[str, str]] = set()
    for child, parent in parents.items():
        if parent in known or parent in parents.values():
            edges.add((child, parent))
    return edges


def shallow_is_a_edges(parents: dict[str, str], max_depth: int = 2) -> set[tuple[str, str]]:
    known = set(parents.keys())
    for parent in parents.values():
        known.add(parent)

    children: dict[str, list[str]] = {}
    for child, parent in parents.items():
        children.setdefault(parent, []).append(child)

    roots = sorted(
        name
        for name in known
        if parents.get(name) not in known
    )

    included: set[str] = set()
    depth_by_node: dict[str, int] = {}

    def visit(name: str, depth: int) -> None:
        if name in depth_by_node and depth_by_node[name] <= depth:
            return
        depth_by_node[name] = depth
        included.add(name)
        if depth >= max_depth:
            return
        for child in sorted(children.get(name, [])):
            visit(child, depth + 1)

    for root in roots:
        visit(root, 0)

    edges: set[tuple[str, str]] = set()
    for child, parent in parents.items():
        if child in included and parent in included:
            edges.add((child, parent))
    return edges


def module_class_edges(schema_dir: Path, import_name: str, parents: dict[str, str]) -> set[tuple[str, str]]:
    schema_file = schema_dir / f"{import_name}.yaml"
    if not schema_file.exists():
        return set()
    doc = yaml.safe_load(schema_file.read_text(encoding="utf-8")) or {}
    classes = doc.get("classes", {})
    if not isinstance(classes, dict):
        return set()
    module_classes = set(classes.keys())
    edges: set[tuple[str, str]] = set()
    for class_name in sorted(module_classes):
        parent = parents.get(class_name)
        if parent:
            edges.add((class_name, parent))
        elif class_name in parents.values():
            continue
    return edges


def import_name_for_slug(schema_dir: Path, slug: str) -> str | None:
    for schema_file in sorted(schema_dir.glob("*_schema.yaml")):
        doc = yaml.safe_load(schema_file.read_text(encoding="utf-8")) or {}
        module_id = doc.get("id")
        if not isinstance(module_id, str):
            continue
        if slug_from_id(module_id.strip(), BASE_URL) == slug:
            return schema_file.stem
    return None


def render_docs_preamble(module_map: str, entity_overview: str) -> str:
    return (
        f"{PREAMBLE_MARKER}\n\n"
        "## Schema diagrams\n\n"
        "Generated from `schema/*.yaml`. "
        "See the [schema documentation](https://schema.pragmaticbim.ch/schema/pragmatic-bim.docs.html) "
        "for interactive class pages.\n\n"
        "### Module map\n\n"
        f"```mermaid\n{module_map.strip()}\n```\n\n"
        "### Entity hierarchy\n\n"
        f"```mermaid\n{entity_overview.strip()}\n```\n\n"
    )


def fenced_mermaid(body: str) -> str:
    return f"```mermaid\n{body.strip()}\n```\n"


def patch_readme(readme_path: Path, sections: dict[str, str]) -> None:
    text = readme_path.read_text(encoding="utf-8")
    for key, body in sections.items():
        marker = README_MARKERS[key]
        begin = f"<!-- diagram:{marker} begin -->"
        end = f"<!-- diagram:{marker} end -->"
        replacement = f"{begin}\n{fenced_mermaid(body)}{end}"
        pattern = re.compile(
            rf"{re.escape(begin)}.*?{re.escape(end)}",
            re.DOTALL,
        )
        if pattern.search(text):
            text = pattern.sub(replacement, text)
        else:
            raise SystemExit(f"README marker not found: {marker}")
    readme_path.write_text(text, encoding="utf-8")


def write_outputs(diagrams_dir: Path, outputs: dict[str, str]) -> None:
    modules_dir = diagrams_dir / "modules"
    modules_dir.mkdir(parents=True, exist_ok=True)
    for rel_path, content in outputs.items():
        path = diagrams_dir / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def collect_outputs(schema_dir: Path) -> dict[str, str]:
    modules = load_modules(schema_dir, BASE_URL)
    parents, _ = load_class_graph(schema_dir)

    modules_in_root: list[dict] = []
    for import_name in load_root_imports(schema_dir):
        module = module_for_import(schema_dir, import_name, modules)
        if module:
            modules_in_root.append(module)

    module_map = render_module_map(modules_in_root, interactive=False)
    module_map_interactive = render_module_map(modules_in_root, interactive=True)
    entity_full = render_class_diagram(all_is_a_edges(parents))
    entity_readme = render_class_diagram(shallow_is_a_edges(parents, max_depth=2))

    outputs: dict[str, str] = {
        "module-map.mmd": module_map,
        "module-map-interactive.mmd": module_map_interactive,
        "entity-overview-full.mmd": entity_full,
        "entity-overview-readme.mmd": entity_readme,
        "docs-preamble.md": render_docs_preamble(module_map, entity_full),
    }

    for module in modules:
        import_name = import_name_for_slug(schema_dir, module["slug"])
        if not import_name:
            continue
        edges = module_class_edges(schema_dir, import_name, parents)
        if not edges:
            continue
        outputs[f"modules/{module['slug']}.mmd"] = render_class_diagram(edges)

    return outputs


def compare_trees(expected_dir: Path, actual_dir: Path) -> list[str]:
    errors: list[str] = []
    expected_files = sorted(p.relative_to(expected_dir) for p in expected_dir.rglob("*") if p.is_file())
    actual_files = sorted(p.relative_to(actual_dir) for p in actual_dir.rglob("*") if p.is_file())
    if expected_files != actual_files:
        errors.append(
            "Diagram file set mismatch:\n"
            f"  expected: {[str(p) for p in expected_files]}\n"
            f"  actual:   {[str(p) for p in actual_files]}"
        )
    for rel_path in expected_files:
        expected = (expected_dir / rel_path).read_text(encoding="utf-8")
        actual = (actual_dir / rel_path).read_text(encoding="utf-8")
        if expected != actual:
            diff = difflib.unified_diff(
                expected.splitlines(keepends=True),
                actual.splitlines(keepends=True),
                fromfile=str(rel_path),
                tofile=f"{rel_path} (generated)",
            )
            errors.append("".join(diff))
    return errors


def generate(
    schema_dir: Path,
    diagrams_dir: Path,
    readme_path: Path | None,
    *,
    check: bool = False,
) -> None:
    outputs = collect_outputs(schema_dir)

    if check:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_root = Path(tmp)
            tmp_dir = tmp_root / "diagrams"
            write_outputs(tmp_dir, outputs)
            if readme_path is not None:
                tmp_readme = tmp_root / "README.md"
                shutil.copy2(readme_path, tmp_readme)
                patch_readme(
                    tmp_readme,
                    {
                        "module-map": outputs["module-map.mmd"],
                        "entity-overview": outputs["entity-overview-readme.mmd"],
                    },
                )
            errors = compare_trees(diagrams_dir, tmp_dir)
            if readme_path is not None and readme_path.exists():
                expected_readme = readme_path.read_text(encoding="utf-8")
                actual_readme = tmp_readme.read_text(encoding="utf-8")
                if expected_readme != actual_readme:
                    diff = difflib.unified_diff(
                        expected_readme.splitlines(keepends=True),
                        actual_readme.splitlines(keepends=True),
                        fromfile=str(readme_path),
                        tofile=f"{readme_path} (generated)",
                    )
                    errors.append("".join(diff))
            if errors:
                print(
                    "Generated diagrams are out of date. "
                    "Run: python scripts/generate_diagrams.py",
                    file=sys.stderr,
                )
                for error in errors:
                    print(error, file=sys.stderr)
                raise SystemExit(1)
        print("Diagram artifacts are up to date.")
        return

    write_outputs(diagrams_dir, outputs)
    if readme_path is not None:
        patch_readme(
            readme_path,
            {
                "module-map": outputs["module-map.mmd"],
                "entity-overview": outputs["entity-overview-readme.mmd"],
            },
        )
    print(f"Generated {len(outputs)} diagram artifacts in {diagrams_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema-dir", type=Path, default=Path("schema"))
    parser.add_argument("--diagrams-dir", type=Path, default=Path("docs/diagrams"))
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify committed diagram artifacts match schema (for CI).",
    )
    parser.add_argument(
        "--skip-readme",
        action="store_true",
        help="Do not patch README.md (used internally by --check).",
    )
    args = parser.parse_args()

    readme_path = None if args.skip_readme else args.readme
    generate(
        args.schema_dir,
        args.diagrams_dir,
        readme_path,
        check=args.check,
    )


if __name__ == "__main__":
    main()
