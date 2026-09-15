# PPCI SWS Proof

`ppci_sws_proof` is a concrete proof subsystem for a sovereign wealth stack workflow. It exposes a real FastAPI microservice that simulates how capital, risk tolerance, and signal intensity change a Hydra engine yield corridor, risk band, and deployment decision.

## What this subsystem does

- Accepts portfolio control inputs for capital, normalized risk tolerance, and normalized signal intensity
- Produces a yield corridor with minimum yield, maximum yield, and spread in basis points
- Assigns a risk band and an engine decision of `defend`, `balance`, or `accelerate`
- Provides a repeatable benchmark and notebook demo for investor-facing proof

## How to run it

### Start the API

```bash
python -m ppci_sws_proof.api.main
```

Or with Uvicorn:

```bash
uvicorn ppci_sws_proof.api.main:app --host 0.0.0.0 --port 8000
```

### Call the endpoint

```bash
curl -X POST http://127.0.0.1:8000/hydra/simulate \
  -H "Content-Type: application/json" \
  -d '{"capital": 250000, "risk_tolerance": 0.55, "signal_intensity": 0.35}'
```

### Run the tests

```bash
python -m unittest ppci_sws_proof.tests.test_hydra
```

### Run the benchmark

```bash
python -m ppci_sws_proof.benchmarks.hydra_benchmark
```

### Open the demo notebook

```bash
jupyter notebook ppci_sws_proof/demo/hydra_demo.ipynb
```

## Why it matters

This subsystem converts broad claims into an inspectable artifact:

- Real request validation through FastAPI and Pydantic
- Real deterministic simulation logic instead of static narrative output
- Real tests for corridor behavior and signal response
- Real benchmark evidence for latency and throughput
- Real demo material that can be shown live

## Benchmarks

Run `python -m ppci_sws_proof.benchmarks.hydra_benchmark` to produce current local latency and throughput measurements. Record the latest output here as validation evidence.

## Test coverage

The automated suite currently covers:

- Corridor expansion under higher risk and favorable signal conditions
- Corridor compression under adverse signals
- Signal-driven changes to corridor ceilings and engine decisions
