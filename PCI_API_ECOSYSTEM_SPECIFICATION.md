# PCI API Ecosystem
## Implemented API Contract (Repository Snapshot)

**Status:** Prototype interfaces documented from the current source code. This is not a specification for a production or enterprise API.

This document describes the two HTTP APIs present in this repository. It does not imply that other services, engines, integrations, or production controls are implemented.

## 1. DeFi Analysis API

**Application:** `pci_defi_analysis_suite/api.py`

**Local startup:** `uvicorn pci_defi_analysis_suite.api:app --host 127.0.0.1 --port 8000`

### `GET /analysis`

Runs the deterministic sample analysis in `run_defi_analysis()` and returns a JSON object with these top-level fields:

| Field | Description |
|---|---|
| `amm` | AMM analysis using fixed sample reserves and fee |
| `lp` | LP risk estimate using fixed sample volatility |
| `yield` | Yield decomposition using fixed sample values |
| `lending` | Lending analysis using fixed sample borrowed/supplied amounts |
| `bridge` | Bridge analysis using fixed sample finality and trust model |
| `routing` | Routing summary for fixed sample routes |
| `scenarios` | Heuristic results for five fixed stress scenarios |
| `resilience_score` | Score derived from the sample structural indicators |

The endpoint accepts no request parameters. It does not query live protocols, chains, prices, or market feeds. Values are illustrative outputs from the checked-in logic, not investment advice or live risk measurements.

## 2. Hydra Simulation API

**Application:** `ppci_sws_proof/api/main.py`

**Local startup:** `uvicorn ppci_sws_proof.api.main:app --host 127.0.0.1 --port 8000`

### `POST /hydra/simulate`

Accepts a JSON request:

```json
{
  "capital": 250000,
  "risk_tolerance": 0.55,
  "signal_intensity": 0.35
}
```

| Property | Type | Validation |
|---|---|---|
| `capital` | number | Greater than 0 |
| `risk_tolerance` | number | Between 0 and 1, inclusive |
| `signal_intensity` | number | Between -1 and 1, inclusive |

Returns `capital`, `risk_tolerance`, and `signal_intensity`; a `yield_corridor` object (`min_pct`, `max_pct`, `spread_bps`); `risk_band` (`capital_preservation`, `balanced`, or `growth`); and `engine_decision` (`defend`, `balance`, or `accelerate`). The deterministic calculation is implemented in `ppci_sws_proof/hydra.py`; the reported yield corridor is simulated, not a promised or realized financial yield.

Invalid request bodies are rejected by FastAPI/Pydantic validation (HTTP 422).

## Shared limitations

- Neither API currently implements authentication, authorization, rate limiting, API versioning, or a documented compatibility guarantee.
- The services are local prototypes; no deployment or availability SLA is specified here.
- HTTPS, secrets management, persistence, monitoring, and production data integrations are not implemented by these API modules.
- These contracts describe current routes only. They do not claim that the nine-engine architecture or other integrations described elsewhere are available through these APIs.
