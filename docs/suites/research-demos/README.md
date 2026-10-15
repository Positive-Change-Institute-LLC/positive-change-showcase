# Research and Demo APIs

This group contains three distinct, executable prototypes. Their limits describe the specific behavior and integrations present in the source; they do not mean the programs are nonfunctional. The prototypes do not share a validated authority layer or production registry.

| Source | What source implements | Important limitation |
|---|---|---|
| `APO.py` | Local HTTP handler with metadata/document endpoints and a generated UI | Many reported validator/integrity/performance figures are hard-coded narrative, not measured service guarantees |
| `OMEGA_QUANT.py` | FastAPI program registry, deterministic scoring/routing endpoints, and health response | Program list and Whop URLs are inline data; API has no authentication, bounded scoring, persistence, verified progression tracking, or provider integration |
| `AAA_PROMETHEUS_SUPER_DEMO.py` | Randomized terminal simulation with a stub that returns success for a named verification action | Its `execute_payment` function only prints; this is not payment processing or security verification |

The **AI Business Builder**, **IncomeOS**, and **Omega Quant Authority** names appear in catalog or code data, but name overlap does not establish interoperability.

## Safe review

Read the source before running it. The demo calls randomized simulation logic and prints a false impression of payment success. The APIs expose services and should be run only in a controlled local environment, bound to loopback by the operator. Do not use real account credentials, wallets, funds, or API keys.

`APO.py`'s metrics and text are not evidence of a deployed oracle, satellite network, validators, quantum-resistant implementation, or measured integrity. `OMEGA_QUANT.py` returns code-defined scores and recommendations, not financial advice or verified Whop actions.

The supplied “Sovereign Stack – Full Runtime” code corresponds to the checked-in `OMEGA_QUANT.py` prototype; it is not a separate production runtime. Its score uses simple averages with a default of 50, does not validate score ranges, and treats a supplied zero as missing. Unknown role/region values can fall back to the full static program list. The Whop URLs and prices are hard-coded; no request is made to Whop, and the “progression is now tracked” response is not backed by persistence. The health route's uptime/doctrine strings are constants, not measurements.

The direct Uvicorn entrypoint binds to `0.0.0.0` with reload enabled, and the API has no authentication or authorization. Do not expose it to untrusted networks or send real credit, income, or protection data; use a loopback bind for local evaluation.

## Interoperability

Before connecting either API to the command dashboard or a product catalog, define an authenticated/versioned contract and verify sources of truth. Current routes are not consumed by the static dashboard or the SQL/CSV catalogs.
