# Explorer Gateway API Proposal

## Status

The supplied OpenAPI document is a user-provided contract proposal. No matching OpenAPI file, Explorer Gateway server, or client integration is checked in, and the external server URLs and route behavior have not been verified. Do not treat its sample responses, authentication description, or blockchain coverage as operational guarantees.

The document describes POST routes for Solana, Bitcoin, Bitcoin Cash, and Ethereum data. Its server list also includes a WebSocket URL, but it defines no WebSocket paths or messages. The global security declaration permits either API-key authentication or an empty security requirement, so anonymous access is explicitly allowed by the proposed contract. The consequences for rate limits, privacy, and abuse need review before adoption.

## Contract review required

- Verify service ownership, deployment, DNS/TLS, supported networks, request methods, response examples, and error behavior with the API operator before generating clients or making requests.
- Validate the document with an OpenAPI 3.1 validator. In particular, review its use of `nullable`, authentication alternatives, required fields, and the consistency of request and response schemas.
- Define allowed network values, address/transaction identifier formats, pagination limits, numeric units and precision, and stable error codes. Exercise these rules against representative fixtures without querying live wallets.
- Specify rate limits, retention, logging, CORS, key rotation, and whether requests may be anonymous. Never embed an Explorer API key in documentation, source examples, or a browser bundle.
- Add WebSocket routes and event schemas only if a real WebSocket service is part of the intended contract.

## Integration boundary

The proposal is not connected to the existing dashboards, catalogs, wallets, or deployment workflow. No blockchain requests should be made based only on this pasted specification. If implementation is approved, start with a schema-validated, read-only adapter, explicit timeouts and bounded pagination, fixture-based tests, and credentials supplied at runtime.
