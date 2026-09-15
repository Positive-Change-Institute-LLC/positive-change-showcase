import math
from typing import Literal, TypedDict


class YieldCorridorData(TypedDict):
    min_pct: float
    max_pct: float
    spread_bps: int


class HydraSimulationData(TypedDict):
    capital: float
    risk_tolerance: float
    signal_intensity: float
    yield_corridor: YieldCorridorData
    risk_band: Literal["capital_preservation", "balanced", "growth"]
    engine_decision: Literal["defend", "balance", "accelerate"]


def simulate_hydra(capital: float, risk_tolerance: float, signal_intensity: float) -> HydraSimulationData:
    capital_scale = min(math.log10(max(capital, 1.0)) / 6.0, 1.0)
    base_center = 0.035 + (risk_tolerance * 0.055) + (capital_scale * 0.01)
    base_width = 0.012 + (risk_tolerance * 0.04)

    signal_shift = signal_intensity * (0.012 + (risk_tolerance * 0.008))
    signal_width = max(signal_intensity, 0.0) * 0.012 - max(-signal_intensity, 0.0) * 0.014
    corridor_width = max(0.006, base_width + signal_width)

    corridor_center = max(0.01, base_center + signal_shift)
    corridor_min = max(0.0, corridor_center - (corridor_width / 2))
    corridor_max = min(0.25, corridor_center + (corridor_width / 2))

    risk_score = (risk_tolerance * 0.75) + (abs(signal_intensity) * 0.15) + (capital_scale * 0.10)
    if risk_score >= 0.72:
        risk_band: Literal["capital_preservation", "balanced", "growth"] = "growth"
    elif risk_score >= 0.35:
        risk_band = "balanced"
    else:
        risk_band = "capital_preservation"

    if signal_intensity <= -0.35:
        engine_decision: Literal["defend", "balance", "accelerate"] = "defend"
    elif signal_intensity >= 0.45 and risk_tolerance >= 0.5:
        engine_decision = "accelerate"
    else:
        engine_decision = "balance"

    return {
        "capital": round(capital, 2),
        "risk_tolerance": round(risk_tolerance, 4),
        "signal_intensity": round(signal_intensity, 4),
        "yield_corridor": {
            "min_pct": round(corridor_min * 100, 2),
            "max_pct": round(corridor_max * 100, 2),
            "spread_bps": int(round((corridor_max - corridor_min) * 10000)),
        },
        "risk_band": risk_band,
        "engine_decision": engine_decision,
    }
