from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field

from ppci_sws_proof.hydra import simulate_hydra


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
