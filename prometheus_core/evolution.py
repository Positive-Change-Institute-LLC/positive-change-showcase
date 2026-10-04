"""Prometheus Evolution Engine: review performance and recommend improvements."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Review:
    metric: str
    value: float
    target: float
    status: str  # "ok" | "weak"
    recommendation: str


class EvolutionEngine:
    """Compare metrics to targets (higher is better) and flag weaknesses."""

    def __init__(self, targets: dict[str, float], tolerance: float = 0.0) -> None:
        if not targets:
            raise ValueError("at least one target is required")
        self.targets = dict(targets)
        self.tolerance = tolerance

    def review(self, metrics: dict[str, float]) -> list[Review]:
        results = []
        for name, target in self.targets.items():
            if name not in metrics:
                raise KeyError(f"missing metric: {name}")
            value = metrics[name]
            weak = value < target * (1 - self.tolerance)
            gap = target - value
            results.append(Review(
                name, value, target, "weak" if weak else "ok",
                f"Raise '{name}' by {gap:g} to reach target {target:g}." if weak
                else f"Maintain '{name}'.",
            ))
        return sorted(results, key=lambda r: (r.status != "weak", r.metric))

    def level(self, metrics: dict[str, float]) -> int:
        """Evolution level = number of metrics meeting target."""
        return sum(r.status == "ok" for r in self.review(metrics))
