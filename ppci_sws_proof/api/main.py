import math
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="PPCI SWS Proof API", version="0.1.0")


class HydraSimulationRequest(BaseModel):
    capital: float = Field(..., gt=0, description="Capital allocated to the Hydra engine.")
    risk_tolerance: float = Field(
        ..., ge=0.0, le=1.0, description="Normalized risk tolerance between 0 and 1."
    )
    signal_intensity: float = Field(
        ...,
        ge=-1.0,
        le=1.0,
        description="Normalized market signal intensity between -1 and 1.",
    )


class YieldCorridor(BaseModel):
    min_pct: float
    max_pct: float
    spread_bps: int


class HydraSimulationResponse(BaseModel):
    capital: float
    risk_tolerance: float
    signal_intensity: float
    yield_corridor: YieldCorridor
    risk_band: Literal["capital_preservation", "balanced", "growth"]
    engine_decision: Literal["defend", "balance", "accelerate"]


def simulate_hydra(capital: float, risk_tolerance: float, signal_intensity: float) -> dict:
    capital_scale = min(math.log10(max(capital, 1.0)) / 6.0, 1.0)
    base_center = 0.035 + (risk_tolerance * 0.055) + (capital_scale * 0.01)
    base_width = 0.012 + (risk_tolerance * 0.04)

    signal_shift = signal_intensity * (0.012 + (risk_tolerance * 0.008))
    signal_width = max(signal_intensity, 0.0) * 0.012 - max(-signal_intensity, 0.0) * 0.014
    corridor_width = max(0.006, base_width + signal_width)

    corridor_center = max(0.01, base_center + signal_shift)
    corridor_min = max(0.0, corridor_center - (corridor_width / 2))
    corridor_max = min(0.25, corridor_center + (corridor_width / 2))

    stress_score = (risk_tolerance * 0.65) + (max(-signal_intensity, 0.0) * 0.35)
    if stress_score >= 0.72:
        risk_band = "growth"
    elif stress_score >= 0.36:
        risk_band = "balanced"
    else:
        risk_band = "capital_preservation"

    if signal_intensity <= -0.35:
        engine_decision = "defend"
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


@app.post("/hydra/simulate", response_model=HydraSimulationResponse)
def hydra_simulate(payload: HydraSimulationRequest) -> HydraSimulationResponse:
    return HydraSimulationResponse(
        **simulate_hydra(
            capital=payload.capital,
            risk_tolerance=payload.risk_tolerance,
            signal_intensity=payload.signal_intensity,
        )
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("ppci_sws_proof.api.main:app", host="0.0.0.0", port=8000, reload=False)
