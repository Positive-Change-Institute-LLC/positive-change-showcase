# Copilot Walkthrough — Explorer Gateway API Proposal

1. Treat the pasted OpenAPI document as unverified input, not as proof that the named endpoint or services exist.
2. Do not generate a live client or make external requests until the service owner and contract are verified.
3. Validate the OpenAPI 3.1 document, including its `nullable` usage, optional API-key security, network/address constraints, units, and error responses.
4. Note that the WebSocket server URL has no corresponding WebSocket operations in the document.
5. Keep any API key out of source, documentation, and browser code; use an approved runtime secret store.
6. If implementation is approved, build a read-only adapter with bounded requests and fixture-based tests before considering live data.
