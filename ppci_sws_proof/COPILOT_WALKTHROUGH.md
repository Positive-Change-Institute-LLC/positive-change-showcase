# Copilot Walkthrough — PPCI SWS Proof / Hydra

1. Read this README, `hydra.py`, `api/main.py`, `tests/test_hydra.py`, and the benchmark before editing the model.
2. Preserve request validation: capital greater than zero, risk tolerance in `[0, 1]`, signal intensity in `[-1, 1]`.
3. Preserve the response fields and enumerated risk/decision labels documented in `PCI_API_ECOSYSTEM_SPECIFICATION.md`; test both API and pure simulation behavior when changing the contract.
4. Keep all claims clear that the yield corridor is modeled. Do not connect capital inputs to transfers, trading, the portfolio builder, or catalog products without an explicit and tested integration design.
5. Run the API on `127.0.0.1` during local work. Avoid the module's `0.0.0.0` direct-run default for untrusted networks.
6. Run `python -m unittest ppci_sws_proof.tests.test_hydra` and `python -m ppci_sws_proof.benchmarks.hydra_benchmark`.
7. Use product names such as **Investor Dashboard** only as documentation examples; no investor catalog connection is implemented.
