#!/usr/bin/env python3
"""Generate module resolver landing pages and JSON descriptors for schema module URIs."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from urllib.parse import urlparse

import yaml

ARTIFACTS = (
    ("json_schema", "JSON Schema", "pragmatic-bim.schema.json", "application/json"),
    ("shacl", "SHACL", "pragmatic-bim.shacl.ttl", "text/turtle"),
    ("csv", "CSV", "pragmatic-bim.csv", "text/csv"),
    ("pydantic", "Pydantic", "pragmatic-bim.pydantic.py", "text/x-python"),
    ("docs_md", "Docs (Markdown)", "pragmatic-bim.docs.md", "text/markdown"),
)

STYLE = """
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; margin: 2rem auto; max-width: 980px; padding: 0 1rem; line-height: 1.55; color: #1f2328; }
.top-nav { border-bottom: 1px solid #d0d7de; padding: 0.6rem 0; margin-bottom: 1rem; }
.top-nav a { margin-right: 0.9rem; font-weight: 600; }
a { color: #0969da; text-decoration: none; }
a:hover { text-decoration: underline; }
code { background: #f6f8fa; padding: 0.15rem 0.35rem; border-radius: 4px; }
ul { padding-left: 1.2rem; }
.mermaid { border: 1px solid #d0d7de; border-radius: 8px; padding: 0.6rem; background: #fff; margin: 1rem 0; overflow: auto; }
"""

MERMAID_SCRIPT_PATH = "assets/mermaid-init.js"


def mermaid_script(schema_prefix: str) -> str:
    src = f"{schema_prefix.rstrip('/')}/{MERMAID_SCRIPT_PATH}"
    return f'<script type="module" src="{html.escape(src)}"></script>\n'


def mermaid_tail(has_diagram: bool, schema_prefix: str) -> str:
    if not has_diagram:
        return ""
    return mermaid_script(schema_prefix)


def read_mermaid_diagram(diagrams_dir: Path, filename: str) -> str | None:
    path = diagrams_dir / filename
    if not path.is_file():
        return None
    body = path.read_text(encoding="utf-8").strip()
    return body or None


def render_mermaid_section(title: str, body: str) -> str:
    return f"""
    <h2>{html.escape(title)}</h2>
    <div class="mermaid">{body.strip()}</div>
"""


def normalize_description(value: object) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(value.split()).strip()


def slug_from_id(module_id: str, base_url: str) -> str | None:
    base = base_url.rstrip("/")
    if module_id.rstrip("/") == base:
        return None
    parsed = urlparse(module_id)
    path = parsed.path.strip("/")
    if not path:
        return None
    return path


def pick_primary_doc(doc: dict) -> str | None:
    classes = doc.get("classes")
    if isinstance(classes, dict) and classes:
        for name, body in classes.items():
            if isinstance(body, dict) and body.get("abstract"):
                return name
        for name, body in classes.items():
            if isinstance(body, dict) and body.get("tree_root"):
                return name
        for name, body in classes.items():
            if isinstance(body, dict):
                slots = body.get("slots", [])
                if isinstance(slots, list) and "id" in slots:
                    return name
        for name, body in classes.items():
            if isinstance(body, dict) and not body.get("abstract"):
                return name
        return next(iter(classes.keys()))
    enums = doc.get("enums")
    if isinstance(enums, dict) and enums:
        return next(iter(enums.keys()))
    return None


def load_modules(schema_dir: Path, base_url: str) -> list[dict]:
    modules: list[dict] = []
    for schema_file in sorted(schema_dir.glob("*_schema.yaml")):
        doc = yaml.safe_load(schema_file.read_text(encoding="utf-8")) or {}
        module_id = doc.get("id")
        if not isinstance(module_id, str) or not module_id.strip():
            continue
        slug = slug_from_id(module_id.strip(), base_url)
        if slug is None:
            continue
        primary = pick_primary_doc(doc)
        modules.append(
            {
                "slug": slug,
                "id": module_id.strip(),
                "title": doc.get("title") or slug,
                "description": normalize_description(doc.get("description")),
                "source_file": schema_file.name,
                "primary_doc": primary,
            }
        )
    return modules


def artifact_urls(base_url: str) -> dict[str, str]:
    schema_base = f"{base_url.rstrip('/')}/schema"
    urls = {"docs_index": f"{schema_base}/pragmatic-bim.docs.html"}
    for key, _, filename, _ in ARTIFACTS:
        urls[key] = f"{schema_base}/{filename}"
    return urls


def build_descriptor(module: dict, base_url: str) -> dict:
    urls = artifact_urls(base_url)
    descriptor = {
        "id": module["id"],
        "title": module["title"],
        "description": module["description"],
        "source_file": module["source_file"],
        "docs_index": urls["docs_index"],
        "json_schema": urls["json_schema"],
        "shacl": urls["shacl"],
        "csv": urls["csv"],
        "pydantic": urls["pydantic"],
        "docs_md": urls["docs_md"],
        "landing_page": f"{base_url.rstrip('/')}/{module['slug']}",
    }
    primary = module.get("primary_doc")
    if primary:
        descriptor["html"] = f"{urls['docs_index'].rsplit('/', 1)[0]}/{primary}.html"
        descriptor["primary_doc"] = primary
    return descriptor


def render_landing_html(
    module: dict,
    descriptor: dict,
    *,
    base_url: str,
    descriptor_href: str,
    schema_prefix: str,
    home_href: str,
    diagrams_dir: Path,
) -> str:
    title = html.escape(str(module["title"]))
    module_id = html.escape(str(module["id"]))
    description = html.escape(str(module.get("description") or ""))
    docs_index = html.escape(descriptor["docs_index"])
    json_schema = html.escape(descriptor["json_schema"])

    primary_block = ""
    primary = module.get("primary_doc")
    if primary and "html" in descriptor:
        primary_name = html.escape(primary)
        primary_href = html.escape(descriptor["html"])
        primary_block = f"""
      <h2>Primary entry</h2>
      <ul>
        <li><a href="{primary_href}">{primary_name}</a></li>
      </ul>
"""

    artifact_items = "\n".join(
        f'        <li><a href="{html.escape(descriptor[key])}">{label}</a></li>'
        for key, label, _, _ in ARTIFACTS
    )

    diagram_block = ""
    has_module_diagram = False
    module_diagram = read_mermaid_diagram(diagrams_dir, f"modules/{module['slug']}.mmd")
    if module_diagram:
        has_module_diagram = True
        diagram_block = render_mermaid_section("Class hierarchy", module_diagram)

    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title} - Pragmatic BIM Schema</title>
    <link rel="describedby" href="{html.escape(descriptor_href)}">
    <link rel="alternate" type="application/json" href="{json_schema}">
    <style>{STYLE}</style>
  </head>
  <body>
    <nav class="top-nav">
      <a href="{html.escape(home_href)}">Home</a>
      <a href="{docs_index}">Schema Index</a>
    </nav>
    <h1>{title}</h1>
    <p><strong>Module URI:</strong> <code>{module_id}</code></p>
    <p>{description}</p>
{diagram_block}
{primary_block}
    <h2>Documentation</h2>
    <ul>
      <li><a href="{docs_index}">Full schema index</a></li>
      <li><a href="{html.escape(descriptor_href)}">Module descriptor (JSON)</a></li>
    </ul>
    <h2>Machine artifacts (merged schema)</h2>
    <ul>
{artifact_items}
    </ul>
{mermaid_tail(has_module_diagram, schema_prefix)}
  </body>
</html>
"""


def render_root_index(
    base_url: str,
    modules: list[dict],
    release_label: str = "Stable",
    *,
    diagrams_dir: Path,
) -> str:
    docs_index = f"{base_url.rstrip('/')}/schema/pragmatic-bim.docs.html"
    module_items = "\n".join(
        f'      <li><a href="./{html.escape(module["slug"])}/">{html.escape(str(module["title"]))}</a> '
        f'(<code>{html.escape(module["id"])}</code>)</li>'
        for module in modules
    )
    artifact_items = "\n".join(
        f'      <li><a href="./schema/{filename}">{label}</a></li>'
        for _, label, filename, _ in ARTIFACTS
    )
    latest_item = ""
    if release_label == "Stable":
        latest_item = '      <li><a href="./latest/index.html">Latest stable alias</a></li>\n'

    overview_block = ""
    has_overview = False
    pillars_overview = read_mermaid_diagram(diagrams_dir, "pillars-overview.mmd")
    if pillars_overview:
        has_overview = True
        overview_block = render_mermaid_section("Three pillars", pillars_overview)

    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Pragmatic BIM Schema ({release_label})</title>
    <style>{STYLE}</style>
  </head>
  <body>
    <nav class="top-nav">
      <a href="{html.escape(docs_index)}">Schema Index</a>
    </nav>
    <h1>Pragmatic BIM Schema ({release_label})</h1>
    <p>Schema URI: <code>{html.escape(base_url.rstrip("/"))}</code></p>
    <p>Latest stable release artifacts are available here.</p>
    <h2>Schema modules</h2>
    <ul>
{module_items}
    </ul>
{overview_block}
    <h2>Artifacts</h2>
    <ul>
{artifact_items}
      <li><a href="./schema/pragmatic-bim.docs.html">Docs (HTML)</a></li>
{latest_item}    </ul>
{mermaid_tail(has_overview, "./schema")}
  </body>
</html>
"""


def upward_prefix(slug: str) -> str:
    """Relative prefix from a module directory page back to the site root."""
    return "../" * (slug.count("/") + 1)


def write_module_pages(
    site_dir: Path,
    modules: list[dict],
    base_url: str,
    *,
    diagrams_dir: Path,
) -> None:
    site_dir.mkdir(parents=True, exist_ok=True)
    for module in modules:
        slug = module["slug"]
        descriptor = build_descriptor(module, base_url)
        slug_dir = site_dir / slug
        slug_dir.mkdir(parents=True, exist_ok=True)
        (slug_dir / "descriptor.json").write_text(
            json.dumps(descriptor, indent=2) + "\n",
            encoding="utf-8",
        )

        html_dir_page = render_landing_html(
            module,
            descriptor,
            base_url=base_url,
            descriptor_href="./descriptor.json",
            schema_prefix=f"{upward_prefix(slug)}schema",
            home_href=f"{upward_prefix(slug)}index.html",
            diagrams_dir=diagrams_dir,
        )
        html_root_page = render_landing_html(
            module,
            descriptor,
            base_url=base_url,
            descriptor_href=f"./{slug}/descriptor.json",
            schema_prefix="./schema",
            home_href="./index.html",
            diagrams_dir=diagrams_dir,
        )
        (slug_dir / "index.html").write_text(html_dir_page, encoding="utf-8")
        html_alias = site_dir / f"{slug}.html"
        html_alias.parent.mkdir(parents=True, exist_ok=True)
        html_alias.write_text(html_root_page, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    parser.add_argument("--schema-dir", type=Path, default=Path("schema"))
    parser.add_argument("--base-url", default="https://schema.pragmaticbim.ch")
    parser.add_argument(
        "--write-root-index",
        action="store_true",
        help="Write site/index.html with module links.",
    )
    parser.add_argument(
        "--release-label",
        default="Stable",
        help="Label used in generated root index.html title.",
    )
    parser.add_argument(
        "--diagrams-dir",
        type=Path,
        default=Path("docs/diagrams"),
        help="Directory containing generated Mermaid diagram files.",
    )
    args = parser.parse_args()

    modules = load_modules(args.schema_dir, args.base_url)
    if not modules:
        raise SystemExit(f"No modules found in {args.schema_dir}")

    write_module_pages(
        args.site_dir,
        modules,
        args.base_url.rstrip("/"),
        diagrams_dir=args.diagrams_dir,
    )
    manifest = {
        "base_url": args.base_url.rstrip("/"),
        "modules": [
            {
                "slug": module["slug"],
                "id": module["id"],
                "title": module["title"],
                "landing_page": f"{args.base_url.rstrip('/')}/{module['slug']}",
            }
            for module in modules
        ],
    }
    args.site_dir.mkdir(parents=True, exist_ok=True)
    (args.site_dir / "modules.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )

    if args.write_root_index:
        (args.site_dir / "index.html").write_text(
            render_root_index(
                args.base_url.rstrip("/"),
                modules,
                args.release_label,
                diagrams_dir=args.diagrams_dir,
            ),
            encoding="utf-8",
        )

    print(f"Generated resolver pages for {len(modules)} modules in {args.site_dir}")


if __name__ == "__main__":
    main()
