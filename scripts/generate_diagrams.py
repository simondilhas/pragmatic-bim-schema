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
    "pillars-overview": "pillars-overview",
    "entity-detail": "entity-detail",
    "requirements-overview": "requirements-overview",
    "changes-overview": "changes-overview",
}
PREAMBLE_MARKER = "<!-- schema-diagrams-preamble -->"
ENTITY_ROOT = "Entity"
PERFORMANCE_ROOT = "PerformanceProperty"
REQUIREMENT_ROOT = "Requirement"
CHANGE_ROOT = "Change"
CHANGES_SCHEMA = "changes_schema"


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


def render_pillars_overview() -> str:
    lines = [
        "flowchart TB",
        '  Root["Pragmatic BIM Data Contract"]',
        '  Root --> Entity["Entities"]',
        '  Root --> Requirement["Requirements"]',
        '  Root --> Change["Changes"]',
    ]
    return "\n".join(lines) + "\n"


def render_module_map(modules_in_root: list[dict], *, interactive: bool = False) -> str:
    lines = ["flowchart TB", "  Root[\"Pragmatic BIM Data Contract\"]"]
    for module in modules_in_root:
        slug = module["slug"]
        node_id = slug.replace("/", "_").replace("-", "_")
        title = str(module.get("title") or slug)
        short = title.split(" - ")[-1] if " - " in title else title
        lines.append(f"  Root --> {node_id}{mermaid_label(short)}")
        if interactive:
            lines.append(f'  click {node_id} href "./{slug}/" _blank')
    return "\n".join(lines) + "\n"


def order_edges_depth_first(edges: set[tuple[str, str]]) -> list[tuple[str, str]]:
    """Order (child, parent) edges depth-first from roots for clearer Mermaid layout."""
    if not edges:
        return []

    children: dict[str, list[str]] = {}
    child_nodes: set[str] = set()
    parent_nodes: set[str] = set()
    for child, parent in edges:
        children.setdefault(parent, []).append(child)
        child_nodes.add(child)
        parent_nodes.add(parent)

    for parent in children:
        children[parent].sort()

    roots = sorted(parent_nodes - child_nodes)
    if not roots:
        roots = sorted(parent_nodes)

    ordered: list[tuple[str, str]] = []

    def visit(parent: str) -> None:
        for child in children.get(parent, []):
            ordered.append((child, parent))
            visit(child)

    for root in roots:
        visit(root)

    seen = set(ordered)
    for edge in sorted(edges):
        if edge not in seen:
            ordered.append(edge)
    return ordered


def render_class_diagram(edges: set[tuple[str, str]]) -> str:
    lines = ["classDiagram", "  direction TB"]
    for child, parent in order_edges_depth_first(edges):
        lines.append(f"  {parent} <|-- {child}")
    return "\n".join(lines) + "\n"


def render_class_diagram_mixed(
    inheritance: set[tuple[str, str]],
    composition: set[tuple[str, str]],
) -> str:
    lines = ["classDiagram", "  direction TB"]
    for child, parent in order_edges_depth_first(inheritance):
        lines.append(f"  {parent} <|-- {child}")
    for contained, container in sorted(composition):
        lines.append(f"  {container} *-- {contained}")
    return "\n".join(lines) + "\n"


def load_schema_doc(schema_dir: Path, import_name: str) -> dict:
    schema_file = schema_dir / f"{import_name}.yaml"
    return yaml.safe_load(schema_file.read_text(encoding="utf-8")) or {}


def module_class_names(schema_dir: Path, import_name: str) -> set[str]:
    doc = load_schema_doc(schema_dir, import_name)
    classes = doc.get("classes", {})
    if not isinstance(classes, dict):
        return set()
    return set(classes.keys())


def composition_edges_from_slots(
    schema_dir: Path,
    import_name: str,
    *,
    allowed_containers: set[str] | None = None,
) -> set[tuple[str, str]]:
    """Return (contained, container) pairs for inlined slot ranges declared on module classes."""
    doc = load_schema_doc(schema_dir, import_name)
    classes = doc.get("classes", {})
    slots_global = doc.get("slots", {})
    if not isinstance(classes, dict) or not isinstance(slots_global, dict):
        return set()

    module_classes = set(classes.keys())
    edges: set[tuple[str, str]] = set()

    for class_name, class_body in classes.items():
        if not isinstance(class_body, dict):
            continue
        if allowed_containers is not None and class_name not in allowed_containers:
            continue
        slot_names = class_body.get("slots", [])
        if not isinstance(slot_names, list):
            continue
        for slot_name in slot_names:
            if not isinstance(slot_name, str):
                continue
            slot_def = slots_global.get(slot_name, {})
            if not isinstance(slot_def, dict):
                continue
            if not slot_def.get("inlined", False):
                continue
            range_name = slot_def.get("range")
            if not isinstance(range_name, str) or range_name not in module_classes:
                continue
            edges.add((range_name, class_name))
    return edges


def subtree_edges(parents: dict[str, str], root: str) -> set[tuple[str, str]]:
    """Collect all (child, parent) edges in the inheritance subtree under root."""
    edges: set[tuple[str, str]] = set()

    def visit(parent_name: str) -> None:
        for child, parent in parents.items():
            if parent == parent_name:
                edges.add((child, parent))
                visit(child)

    visit(root)
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


def mermaid_pre(body: str) -> str:
    return f'<pre class="mermaid">\n{body.strip()}\n</pre>'


def render_pillars_accordion(
    pillars_overview: str,
    entity_detail: str,
    requirements_branch: str,
    changes_branch: str,
) -> str:
    return (
        f"{PREAMBLE_MARKER}\n\n"
        "## Schema diagrams\n\n"
        "Generated from `schema/*.yaml`. "
        "Click a pillar in the overview or use the buttons below to explore each branch.\n\n"
        '<div id="pillars-acc" class="pillars-acc">\n\n'
        '<div class="pillars-overview">\n'
        f"{mermaid_pre(pillars_overview)}\n"
        "</div>\n\n"
        '<div class="pillar-controls">\n'
        '  <button type="button" class="pillar-btn" data-pillar="entity">Entities</button>\n'
        '  <button type="button" class="pillar-btn" data-pillar="requirement">Requirements</button>\n'
        '  <button type="button" class="pillar-btn" data-pillar="change">Changes</button>\n'
        "</div>\n\n"
        '<div class="pillar-panels">\n'
        '  <div id="pillar-entity" class="pillar-panel" hidden>\n'
        f"{mermaid_pre(entity_detail)}\n"
        "  </div>\n"
        '  <div id="pillar-requirement" class="pillar-panel" hidden>\n'
        f"{mermaid_pre(requirements_branch)}\n"
        "  </div>\n"
        '  <div id="pillar-change" class="pillar-panel" hidden>\n'
        f"{mermaid_pre(changes_branch)}\n"
        "  </div>\n"
        "</div>\n\n"
        "</div>\n"
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
    pillars_overview = render_pillars_overview()
    entity_inheritance = subtree_edges(parents, ENTITY_ROOT)
    performance_inheritance = subtree_edges(parents, PERFORMANCE_ROOT)
    entity_composition = {
        (PERFORMANCE_ROOT, ENTITY_ROOT),
    }
    entity_detail = render_class_diagram_mixed(
        entity_inheritance | performance_inheritance,
        entity_composition,
    )
    performance_branch = render_class_diagram(subtree_edges(parents, PERFORMANCE_ROOT))
    requirements_branch = render_class_diagram(subtree_edges(parents, REQUIREMENT_ROOT))
    change_inheritance = subtree_edges(parents, CHANGE_ROOT)
    change_composition = composition_edges_from_slots(schema_dir, CHANGES_SCHEMA)
    changes_branch = render_class_diagram_mixed(change_inheritance, change_composition)

    outputs: dict[str, str] = {
        "module-map.mmd": module_map,
        "module-map-interactive.mmd": module_map_interactive,
        "pillars-overview.mmd": pillars_overview,
        "entity-detail.mmd": entity_detail,
        "entity-overview-performance.mmd": performance_branch,
        "entity-overview-requirements.mmd": requirements_branch,
        "entity-overview-changes.mmd": changes_branch,
        "pillars-accordion.md": render_pillars_accordion(
            pillars_overview,
            entity_detail,
            requirements_branch,
            changes_branch,
        ),
    }

    for module in modules:
        import_name = import_name_for_slug(schema_dir, module["slug"])
        if not import_name:
            continue
        edges = module_class_edges(schema_dir, import_name, parents)
        if import_name == CHANGES_SCHEMA:
            comp = composition_edges_from_slots(schema_dir, import_name)
            if edges or comp:
                outputs[f"modules/{module['slug']}.mmd"] = render_class_diagram_mixed(edges, comp)
            continue
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
                        "pillars-overview": outputs["pillars-overview.mmd"],
                        "entity-detail": outputs["entity-detail.mmd"],
                        "requirements-overview": outputs["entity-overview-requirements.mmd"],
                        "changes-overview": outputs["entity-overview-changes.mmd"],
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
                "pillars-overview": outputs["pillars-overview.mmd"],
                "entity-detail": outputs["entity-detail.mmd"],
                "requirements-overview": outputs["entity-overview-requirements.mmd"],
                "changes-overview": outputs["entity-overview-changes.mmd"],
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
