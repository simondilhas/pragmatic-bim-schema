#!/usr/bin/env python3
"""Build schema HTML documentation with MkDocs Material."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from postprocess_schema_docs import postprocess_md_dir  # noqa: E402

DEFAULT_SCHEMA_ROOT = REPO_ROOT / "schema" / "00_pragmatic_bim_data_contract.yaml"
DEFAULT_MD_SRC = REPO_ROOT / "site" / "schema" / ".md-src"
DEFAULT_SITE_DIR = REPO_ROOT / "site" / "schema"
DEFAULT_HTML_BUILD = DEFAULT_SITE_DIR / ".html-build"
DEFAULT_ASSETS_SRC = REPO_ROOT / "docs" / "assets"
DEFAULT_ACCORDION = REPO_ROOT / "docs" / "diagrams" / "pillars-accordion.md"
INDEX_NAME = "pragmatic-bim.docs.md"


def find_gen_doc() -> str:
    for cmd in ("gen-doc", "gen-docs", "gen-markdown"):
        if shutil.which(cmd):
            return cmd
    raise SystemExit("No gen-doc command found; install linkml from requirements-docs.txt")


def run_gen_doc(md_src: Path, schema_root: Path) -> None:
    md_src.mkdir(parents=True, exist_ok=True)
    cmd = find_gen_doc()
    args = [
        cmd,
        "--index-name",
        "pragmatic-bim.docs",
        "--hierarchical-class-view",
        "--truncate-descriptions",
        "false",
        "--diagram-type",
        "mermaid_class_diagram",
        "-d",
        str(md_src),
        str(schema_root),
    ]
    subprocess.run(args, check=True, cwd=REPO_ROOT)


def copy_assets(md_src: Path, assets_src: Path) -> None:
    if not assets_src.is_dir():
        raise SystemExit(f"Assets directory not found: {assets_src}")
    target = md_src / "assets"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(assets_src, target)


def merge_html_build(html_build: Path, site_dir: Path) -> None:
    if not html_build.is_dir():
        raise SystemExit(f"MkDocs output directory not found: {html_build}")
    site_dir.mkdir(parents=True, exist_ok=True)
    for item in html_build.iterdir():
        dest = site_dir / item.name
        if item.is_dir():
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)


def publish_markdown_artifacts(md_src: Path, site_dir: Path) -> None:
    index_src = md_src / INDEX_NAME
    if not index_src.is_file():
        raise SystemExit(f"Expected index markdown not found: {index_src}")
    shutil.copy2(index_src, site_dir / INDEX_NAME)
    for md_file in md_src.glob("*.md"):
        if md_file.name == INDEX_NAME:
            continue
        shutil.copy2(md_file, site_dir / md_file.name)


def build_schema_docs(
    *,
    md_src: Path,
    site_dir: Path,
    html_build: Path,
    schema_root: Path,
    accordion_path: Path,
    assets_src: Path,
    skip_mkdocs: bool = False,
) -> None:
    postprocess_md_dir(
        md_src,
        schema_root=schema_root,
        accordion_path=accordion_path,
    )
    copy_assets(md_src, assets_src)

    if skip_mkdocs:
        return

    if html_build.exists():
        shutil.rmtree(html_build)

    subprocess.run(
        ["mkdocs", "build", "-f", str(REPO_ROOT / "mkdocs.yml")],
        check=True,
        cwd=REPO_ROOT,
    )

    merge_html_build(html_build, site_dir)
    publish_markdown_artifacts(md_src, site_dir)

    if html_build.exists():
        shutil.rmtree(html_build)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--md-src", type=Path, default=DEFAULT_MD_SRC)
    parser.add_argument("--site-dir", type=Path, default=DEFAULT_SITE_DIR)
    parser.add_argument("--html-build", type=Path, default=DEFAULT_HTML_BUILD)
    parser.add_argument(
        "--schema-root",
        type=Path,
        default=Path(os.environ.get("SCHEMA_ROOT", DEFAULT_SCHEMA_ROOT)),
    )
    parser.add_argument("--accordion-path", type=Path, default=DEFAULT_ACCORDION)
    parser.add_argument("--assets-src", type=Path, default=DEFAULT_ASSETS_SRC)
    parser.add_argument(
        "--dev",
        action="store_true",
        help="Run gen-doc and generate_diagrams.py before building docs.",
    )
    parser.add_argument(
        "--skip-mkdocs",
        action="store_true",
        help="Only post-process markdown (for tests).",
    )
    args = parser.parse_args()

    if args.dev:
        run_gen_doc(args.md_src, args.schema_root)
        subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "generate_diagrams.py"), "--skip-readme"],
            check=True,
            cwd=REPO_ROOT,
        )

    build_schema_docs(
        md_src=args.md_src,
        site_dir=args.site_dir,
        html_build=args.html_build,
        schema_root=args.schema_root,
        accordion_path=args.accordion_path,
        assets_src=args.assets_src,
        skip_mkdocs=args.skip_mkdocs,
    )
    print(f"Built schema docs in {args.site_dir}")


if __name__ == "__main__":
    main()
