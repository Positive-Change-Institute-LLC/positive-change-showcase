# Copilot Walkthrough — Global Web3 Analytics

1. Do not execute the submitted script, import it in tests, or move it into an application entry point; it has import-time file, network, key-generation, and payment side effects.
2. If the feature is revisited, first separate pure analytics from network clients, key management, server startup, and transaction submission.
3. Use only testnet fixtures for integration tests. A mocked XLM price or random wallet is not a production data source or custody design.
4. Require explicit human authorization and policy checks before any value-bearing action; add idempotency and conservative amount/recipient validation.
5. Bind local servers to loopback by default. Do not expose Flask debug servers or unauthenticated routes on `0.0.0.0`.
6. Use catalog names such as **Investor Dashboard** only as labels, not as proof of an existing service connection.
7. Keep API keys and signing material in approved runtime secret storage, and rotate any credential exposed outside that boundary.
8. Document testnet/mainnet status precisely; never report sample metrics or fallback prices as live/verified results.
