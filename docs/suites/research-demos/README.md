# Research and Demo APIs

This group contains three distinct prototypes. They do not share a validated authority layer or production registry.

| Source | What source implements | Important limitation |
|---|---|---|
| `APO.py` | Local HTTP handler with metadata/document endpoints and a generated UI | Many reported validator/integrity/performance figures are hard-coded narrative, not measured service guarantees |
| `OMEGA_QUANT.py` | FastAPI program registry, deterministic scoring/routing endpoints, and health response | Program list and Whop URLs are inline data; API has no demonstrated auth or verified progression tracking |
| `AAA_PROMETHEUS_SUPER_DEMO.py` | Randomized terminal simulation with a stub that returns success for a named verification action | Its `execute_payment` function only prints; this is not payment processing or security verification |

The **AI Business Builder**, **IncomeOS**, and **Omega Quant Authority** names appear in catalog or code data, but name overlap does not establish interoperability.

## Safe review

Read the source before running it. The demo calls randomized simulation logic and prints a false impression of payment success. The APIs expose services and should be run only in a controlled local environment, bound to loopback by the operator. Do not use real account credentials, wallets, funds, or API keys.

`APO.py`'s metrics and text are not evidence of a deployed oracle, satellite network, validators, quantum-resistant implementation, or measured integrity. `OMEGA_QUANT.py` returns code-defined scores and recommendations, not financial advice or verified Whop actions.

## Interoperability

Before connecting either API to the command dashboard or a product catalog, define an authenticated/versioned contract and verify sources of truth. Current routes are not consumed by the static dashboard or the SQL/CSV catalogs.
