# Copilot Walkthrough — Research and Demo APIs

1. Read each script independently and inspect route binding, imports, side effects, and hard-coded data before changing it.
2. Treat advertised numbers and phrases as unverified source text unless a reproducible test/benchmark supports them.
3. Never convert the AAA demo's print-only `execute_payment` into a real payment assumption; do not execute a wallet or funds flow.
4. Keep APIs local-only during development. Add explicit validation, authentication requirements, versioning, and tests before proposing external exposure.
5. Use catalog names such as **IncomeOS** or **Omega Quant Authority** only when the source lists them; do not infer that similarly named APIs or products share records.
6. Test scoring boundaries, unknown product routing, malformed requests, and exception paths before changing recommendation behavior.
7. Report prototype capabilities and unimplemented provider integrations separately.
