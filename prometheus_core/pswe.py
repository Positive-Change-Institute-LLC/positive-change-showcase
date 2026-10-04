"""Prometheus Sovereign Wealth Engine (PSWE): dollar-cost-averaging simulator.

Educational simulation over a caller-supplied price series. It does not trade,
connect to exchanges, or handle keys, and it is not financial advice.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class DCAResult:
    periods: int
    total_invested: float
    units: float
    average_cost: float
    final_value: float
    return_pct: float


def simulate_dca(prices: Sequence[float], contribution: float) -> DCAResult:
    """Invest a fixed ``contribution`` at each price and report the outcome."""
    if contribution <= 0:
        raise ValueError("contribution must be positive")
    if not prices:
        raise ValueError("prices must be non-empty")
    if any(p <= 0 for p in prices):
        raise ValueError("prices must be positive")
    units = sum(contribution / p for p in prices)
    invested = contribution * len(prices)
    final_value = units * prices[-1]
    return DCAResult(
        periods=len(prices),
        total_invested=invested,
        units=units,
        average_cost=invested / units,
        final_value=final_value,
        return_pct=(final_value / invested - 1) * 100,
    )
