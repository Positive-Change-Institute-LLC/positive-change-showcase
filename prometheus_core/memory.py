"""Prometheus Memory System: persistent, searchable knowledge with continuity."""
from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable, Optional


@dataclass
class MemoryRecord:
    id: int
    kind: str  # e.g. "project", "lesson", "preference", "decision"
    text: str
    tags: list[str] = field(default_factory=list)
    created_at: float = field(default_factory=time.time)


class MemorySystem:
    """JSON-file backed store. Pass ``path=None`` for an in-memory store."""

    def __init__(self, path: Optional[str | Path] = None) -> None:
        self.path = Path(path) if path else None
        self._records: list[MemoryRecord] = []
        if self.path and self.path.exists():
            data = json.loads(self.path.read_text(encoding="utf-8"))
            self._records = [MemoryRecord(**r) for r in data]

    def add(self, kind: str, text: str, tags: Iterable[str] = ()) -> MemoryRecord:
        if not kind.strip() or not text.strip():
            raise ValueError("kind and text must be non-empty")
        rec = MemoryRecord(
            id=max((r.id for r in self._records), default=0) + 1,
            kind=kind.strip(),
            text=text.strip(),
            tags=sorted({t.strip().lower() for t in tags if t.strip()}),
        )
        self._records.append(rec)
        self._save()
        return rec

    def search(self, query: str = "", kind: Optional[str] = None,
               tag: Optional[str] = None) -> list[MemoryRecord]:
        q = query.lower()
        out = [
            r for r in self._records
            if (not kind or r.kind == kind)
            and (not tag or tag.lower() in r.tags)
            and (not q or q in r.text.lower())
        ]
        return sorted(out, key=lambda r: r.created_at, reverse=True)

    def delete(self, record_id: int) -> bool:
        before = len(self._records)
        self._records = [r for r in self._records if r.id != record_id]
        changed = len(self._records) != before
        if changed:
            self._save()
        return changed

    def __len__(self) -> int:
        return len(self._records)

    def _save(self) -> None:
        if self.path:
            self.path.write_text(
                json.dumps([asdict(r) for r in self._records], indent=2),
                encoding="utf-8",
            )
