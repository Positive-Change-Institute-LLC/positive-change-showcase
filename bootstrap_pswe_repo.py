#!/usr/bin/env python3
"""Bootstrap a lightweight showcase repository scaffold.

The script is safe to run multiple times:
- directories are created if missing
- files are created only when absent unless --force is provided
- a dry-run mode reports planned changes without mutating the filesystem
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from string import Template
from typing import Iterable


@dataclass(frozen=True)
class BootstrapContext:
    project_name: str
    organization: str
    tagline: str


@dataclass(frozen=True)
class Change:
    kind: str
    path: str
    status: str


DIRECTORIES = (
    "assets",
    "assets/css",
    "assets/js",
    "docs",
    "scripts",
)

FILE_TEMPLATES = {
    ".gitignore": Template(
        "__pycache__/\n"
        "*.py[cod]\n"
        ".pytest_cache/\n"
        ".venv/\n"
        "venv/\n"
        ".DS_Store\n"
    ),
    "README.md": Template(
        "# $project_name\n\n"
        "> $tagline\n\n"
        "## Overview\n\n"
        "This repository contains the source, content, and assets for $project_name.\n\n"
        "## Structure\n\n"
        "- `index.html` - landing page\n"
        "- `assets/` - static assets\n"
        "- `docs/` - supporting documentation\n"
        "- `scripts/` - utility scripts\n"
    ),
    "index.html": Template(
        "<!DOCTYPE html>\n"
        "<html lang=\"en\">\n"
        "<head>\n"
        "  <meta charset=\"UTF-8\">\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        "  <title>$project_name</title>\n"
        "  <link rel=\"stylesheet\" href=\"assets/css/styles.css\">\n"
        "</head>\n"
        "<body>\n"
        "  <main class=\"container\">\n"
        "    <h1>$project_name</h1>\n"
        "    <p>$tagline</p>\n"
        "    <p>Maintained by $organization.</p>\n"
        "  </main>\n"
        "</body>\n"
        "</html>\n"
    ),
    "assets/css/styles.css": Template(
        ":root {\n"
        "  color-scheme: dark;\n"
        "  --bg: #101728;\n"
        "  --fg: #edf2f7;\n"
        "  --accent: #ff6b35;\n"
        "}\n\n"
        "* { box-sizing: border-box; }\n\n"
        "body {\n"
        "  margin: 0;\n"
        "  min-height: 100vh;\n"
        "  display: grid;\n"
        "  place-items: center;\n"
        "  background: linear-gradient(135deg, #101728, #1b2a41);\n"
        "  color: var(--fg);\n"
        "  font-family: Arial, sans-serif;\n"
        "}\n\n"
        ".container {\n"
        "  max-width: 720px;\n"
        "  padding: 3rem 1.5rem;\n"
        "  text-align: center;\n"
        "}\n\n"
        "h1 { color: var(--accent); }\n"
    ),
    "assets/js/main.js": Template(
        "document.addEventListener('DOMContentLoaded', () => {\n"
        "  console.log('$project_name ready');\n"
        "});\n"
    ),
    "docs/ARCHITECTURE.md": Template(
        "# $project_name Architecture\n\n"
        "## Purpose\n\n"
        "$tagline\n\n"
        "## Ownership\n\n"
        "- Organization: $organization\n"
    ),
    "scripts/serve.py": Template(
        "#!/usr/bin/env python3\n"
        "\"\"\"Serve the repository root over HTTP for local preview.\"\"\"\n\n"
        "from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler\n\n"
        "\n"
        "def main() -> None:\n"
        "    server = ThreadingHTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)\n"
        "    print('Serving $project_name at http://127.0.0.1:8000')\n"
        "    server.serve_forever()\n\n"
        "\n"
        "if __name__ == '__main__':\n"
        "    main()\n"
    ),
}


def render_template(template: Template, context: BootstrapContext) -> str:
    return template.substitute(asdict(context))


def ensure_directory(path: Path, dry_run: bool) -> Change:
    if path.exists():
        return Change("directory", str(path), "exists")
    if not dry_run:
        path.mkdir(parents=True, exist_ok=True)
    return Change("directory", str(path), "created")


def ensure_file(path: Path, content: str, dry_run: bool, force: bool) -> Change:
    existed = path.exists()
    if existed and not force:
        return Change("file", str(path), "exists")
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return Change("file", str(path), "updated" if existed and force else "created")


def bootstrap_repo(
    repo_root: Path,
    context: BootstrapContext,
    *,
    dry_run: bool = False,
    force: bool = False,
) -> list[Change]:
    changes: list[Change] = []

    for directory in DIRECTORIES:
        changes.append(ensure_directory(repo_root / directory, dry_run))

    for relative_path, template in FILE_TEMPLATES.items():
        changes.append(
            ensure_file(
                repo_root / relative_path,
                render_template(template, context),
                dry_run,
                force,
            )
        )

    return changes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bootstrap a lightweight showcase repository.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Path to the repository root to bootstrap.",
    )
    parser.add_argument(
        "--project-name",
        default="Positive Change Showcase",
        help="Project name used in generated templates.",
    )
    parser.add_argument(
        "--organization",
        default="Positive Change Institute LLC",
        help="Organization name used in generated templates.",
    )
    parser.add_argument(
        "--tagline",
        default="Sovereign showcase repository scaffold.",
        help="Short tagline used in generated templates.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned changes without writing files.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite managed files even when they already exist.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit the change summary as JSON.",
    )
    return parser.parse_args()


def summarize(changes: Iterable[Change], *, emit_json: bool) -> None:
    if emit_json:
        print(json.dumps([asdict(change) for change in changes], indent=2))
        return

    for change in changes:
        print(f"[{change.status}] {change.kind}: {change.path}")


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    context = BootstrapContext(
        project_name=args.project_name,
        organization=args.organization,
        tagline=args.tagline,
    )
    changes = bootstrap_repo(
        repo_root,
        context,
        dry_run=args.dry_run,
        force=args.force,
    )
    summarize(changes, emit_json=args.json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
