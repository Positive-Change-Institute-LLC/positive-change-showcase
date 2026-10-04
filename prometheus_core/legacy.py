"""Prometheus Digital Legacy System: verifiable inventory of knowledge assets.

Builds a manifest (path, size, SHA-256) of a directory so assets can be
preserved, handed over, and later verified for tampering or loss.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Verification:
    ok: bool
    missing: tuple[str, ...]
    modified: tuple[str, ...]
    added: tuple[str, ...]


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def build_manifest(root: str | Path, exclude: tuple[str, ...] = (".git", "__pycache__")) -> dict:
    root = Path(root).resolve()
    if not root.is_dir():
        raise NotADirectoryError(str(root))
    files = {}
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root)
        if p.is_file() and not any(part in exclude for part in rel.parts):
            files[rel.as_posix()] = {"size": p.stat().st_size, "sha256": _sha256(p)}
    return {"version": 1, "file_count": len(files), "files": files}


def write_manifest(root: str | Path, out: str | Path) -> dict:
    manifest = build_manifest(root)
    Path(out).write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    return manifest


def verify_manifest(root: str | Path, manifest: dict) -> Verification:
    current = build_manifest(root)["files"]
    expected = manifest["files"]
    missing = tuple(sorted(set(expected) - set(current)))
    added = tuple(sorted(set(current) - set(expected)))
    modified = tuple(sorted(
        f for f in set(expected) & set(current)
        if expected[f]["sha256"] != current[f]["sha256"]
    ))
    return Verification(not (missing or modified or added), missing, modified, added)
