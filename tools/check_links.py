#!/usr/bin/env python3
"""Verify that relative links in top-level Markdown files point to existing files."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote

root = Path(__file__).resolve().parent.parent
bad = []
for md in sorted(root.glob("*.md")):
    in_fence = False
    for n, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if in_fence:
            continue
        for target in re.findall(r"\]\((\.{0,2}/[^)#\s]*|[A-Za-z0-9_.\-]+\.\w+)(?:#[^)]*)?\)", line):
            if not (root / unquote(target)).resolve().exists():
                bad.append(f"{md.name}:{n}: {target}")
print("\n".join(bad) or "All relative links OK")
sys.exit(1 if bad else 0)
