"""Prometheus Synthesizer: fuse multiple sources into ranked conclusions."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class Finding:
    claim: str
    sources: tuple[str, ...]
    confidence: float  # 0..1, combined


class Synthesizer:
    """Combine (source, claim, confidence) observations.

    Claims are normalised (case/whitespace). Independent sources agreeing on a
    claim raise its confidence via noisy-OR: 1 - prod(1 - c_i).
    """

    def __init__(self) -> None:
        self._obs: dict[str, list[tuple[str, float]]] = defaultdict(list)
        self._display: dict[str, str] = {}

    def observe(self, source: str, claim: str, confidence: float) -> None:
        if not 0.0 <= confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        key = " ".join(claim.lower().split())
        if not key:
            raise ValueError("claim must be non-empty")
        self._display.setdefault(key, " ".join(claim.split()))
        if all(s != source for s, _ in self._obs[key]):
            self._obs[key].append((source, confidence))

    def synthesize(self, min_confidence: float = 0.0) -> list[Finding]:
        findings = []
        for key, obs in self._obs.items():
            miss = 1.0
            for _, c in obs:
                miss *= 1.0 - c
            conf = round(1.0 - miss, 6)
            if conf >= min_confidence:
                findings.append(Finding(self._display[key],
                                        tuple(sorted(s for s, _ in obs)), conf))
        return sorted(findings, key=lambda f: (-f.confidence, f.claim))
