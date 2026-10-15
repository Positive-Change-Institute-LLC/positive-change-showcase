# Copilot Walkthrough — PCI DeFi Analysis

1. Read this README, `main.py`, the `core/`, `utils/`, `scenarios/`, `api.py`, `cli.py`, and existing tests before changing a calculation.
2. Distinguish fixed sample inputs from protocol or market data; never describe a sample result as live pricing, yield, risk, or investment advice.
3. Keep module input/output keys consistent because `main.py`, the API, CLI, and terminal dashboard consume those shapes.
4. Add focused tests for valid calculations, boundary values, zero/invalid reserves or supplies, and malformed inputs before extending formulas.
5. Bind local API examples to `127.0.0.1`. Any live-chain adapter needs a separately reviewed contract, secrets boundary, timeout/failure behavior, and tests.
6. Run `python -m unittest discover -s tests -b` from the repository root and test any changed CLI/API command locally.
7. Use exact catalog product names such as **Prometheus Sovereign Intelligence** only for references; this suite does not consume the product catalog.
8. Treat the supplied `PCI_DEFI_ANALYSIS_SUITE_ALL_IN_ONE` as a proposal; do not describe its chain support, solver network, access/pricing policy, or multi-language services as implemented here.
9. Before adapting any proposed formula, validate its units and assumptions and add boundary tests, including zero/invalid reserves and zero supplied lending balances. Scores and scenario labels are not financial risk assessments.
