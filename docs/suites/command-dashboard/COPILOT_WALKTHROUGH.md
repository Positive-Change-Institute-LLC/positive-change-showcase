# Copilot Walkthrough — Command Dashboard

1. Read this README, `PROMETHEUS_COMMAND_DASHBOARD.html`, `PROMETHEUS_333_FX_CATALOG.json`, and `.github/workflows/deploy.yml`.
2. Keep English/Spanish text in sync and preserve accessible labels, keyboard focus, responsive layout, and reduced-motion behavior.
3. Do not add remote scripts, external AI calls, wallet actions, live market values, or credential fields to a static page.
4. Validate any new catalog dependency against missing JSON, malformed records, and the embedded fallback.
5. Do not imply that the browser-side Hydra approximation is the API. If they are deliberately connected, test against the API contract in `PCI_API_ECOSYSTEM_SPECIFICATION.md`.
6. Extract inline scripts and run `node --check`; run `python -m unittest tests.test_prometheus_333_fx_catalog`; verify Pages copies the dashboard and catalog.
7. Use truthful labels: the FX catalog is specification-only, Circle is proposed, and the helper is local/rules-based.
