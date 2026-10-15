# Copilot Walkthrough — APO

1. Compare the supplied “APO DAG Constellation” snippet with the checked-in `APO.py`; do not overwrite the existing file or imply the snippet is already committed.
2. Before calling a future design a DAG, require explicit node/edge schemas, stable identifiers, acyclicity validation, traversal behavior, and tests. The supplied snippet has none of these.
3. Treat metrics and security statements as unverified content unless independently measured and linked to reproducible evidence.
4. Keep local development bound to loopback. Do not expose the unauthenticated prototype or traceback responses publicly.
5. If exposing catalog products, use exact catalog names such as **Investor Dashboard**, validate the schema, and add a tested read-only adapter; do not infer a connection from matching names.
6. Add tests for every route, unknown paths, content types, malformed/error cases, and safe HTML handling before changing the HTTP interface.
7. Document current and proposed capabilities separately. No production oracle, validator mesh, satellite infrastructure, or DAG network is configured here.
