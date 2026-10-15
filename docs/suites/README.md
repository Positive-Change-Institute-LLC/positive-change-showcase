# Suite Documentation Index

This index maps maintained suite documentation to the source files and identifies the current implementation boundary. Each suite directory contains a `README.md` and a `COPILOT_WALKTHROUGH.md`. Product examples use names from the repository catalogs, such as **Investor Dashboard**, **AI Business Builder**, **Prometheus Sovereign Intelligence**, and **DeltaFlow**.

| Suite | README | Copilot walkthrough | Main sources | Current boundary |
|---|---|---|---|---|
| PCI DeFi Analysis | [README](../../pci_defi_analysis_suite/README.md) | [Walkthrough](../../pci_defi_analysis_suite/COPILOT_WALKTHROUGH.md) | `pci_defi_analysis_suite/` | Deterministic sample inputs; not connected to live chains or markets |
| Hydra / SWS Proof | [README](../../ppci_sws_proof/README.md) | [Walkthrough](../../ppci_sws_proof/COPILOT_WALKTHROUGH.md) | `ppci_sws_proof/` | Local validated simulation API; not financial advice or live yield |
| Deployment Orchestrator | [README](deployment/README.md) | [Walkthrough](deployment/COPILOT_WALKTHROUGH.md) | `PROMETHEUS_SOVEREIGN_DEPLOYMENT_SUITE.py`, `.github/workflows/deploy.yml` | Manifest-driven; dry-run default; production gated |
| 333 FX Catalog | [README](fx-catalog/README.md) | [Walkthrough](fx-catalog/COPILOT_WALKTHROUGH.md) | `prometheus_333_fx_catalog.py`, `PROMETHEUS_333_FX_CATALOG.json` | Generated specifications; rendered/deployed assets not verified |
| Command Dashboard | [README](command-dashboard/README.md) | [Walkthrough](command-dashboard/COPILOT_WALKTHROUGH.md) | `PROMETHEUS_COMMAND_DASHBOARD.html` | Local browser prototype; FX catalog is same-site static JSON |
| Arcana Showcase | [README](../../frontend/README.md) | [Walkthrough](../../frontend/COPILOT_WALKTHROUGH.md) | `frontend/index.html` | Static concept cards; no wallet, QR, login, or transaction behavior |
| Investor Portfolio | [README](investor-portfolio/README.md) | [Walkthrough](investor-portfolio/COPILOT_WALKTHROUGH.md) | `pci_portfolio_master_builder_v2.py`, `pci_investor_suite_portal.py`, `PCI_INVESTOR_SUITE_PORTAL.html` | Dry-run-first file inventory and loopback-only read-only browser |
| Turnkey Catalog Data | [README](turnkey-catalog/README.md) | [Walkthrough](turnkey-catalog/COPILOT_WALKTHROUGH.md) | `TURNKEYS_DATABASE.sql`, `PCI_MASTER_TURNKEYS_150_COMPLETE.json`, catalog CSVs | Static/local catalog inputs; never implies a production database update |
| Product Generators | [README](product-generators/README.md) | [Walkthrough](product-generators/COPILOT_WALKTHROUGH.md) | `PCI_TURNKEY_GENERATOR_MAIN.py`, `PCI_SOVEREIGN_PORTFOLIO_GENERATOR.py`, `PCI_ENTERPRISE_PDF_SPEC_GENERATOR.py` | Local generation scripts; generated links, prices, and output names require review |
| PCI Automation Suite | [README](automation-suite/README.md) | [Walkthrough](automation-suite/COPILOT_WALKTHROUGH.md) | User-supplied inline registry/generator snippet | Supplied concept only; no checked-in implementation or live Whop integration |
| Motion Engine | [README](motion-engine/README.md) | [Walkthrough](motion-engine/COPILOT_WALKTHROUGH.md) | `PROMETHEUS_MOTION_ENGINE__SOVEREIGN_DYNAMICS.py` | Profile selection and print stubs; no browser animation integration |
| Bootstrap Utilities | [README](bootstrap-utilities/README.md) | [Walkthrough](bootstrap-utilities/COPILOT_WALKTHROUGH.md) | `bootstrap_ppci_sws.py`, `bootstrap_pswe_repo.py`, `bootstrap_signal_layers.py` | Scaffolding only; dry-run before writing to a repository |
| APO / DAG Constellation | [README](apo/README.md) | [Walkthrough](apo/COPILOT_WALKTHROUGH.md) | `APO.py` and user-supplied “APO DAG Constellation” proposal | Static metadata/HTTP prototype; no DAG implementation; metrics are unverified |
| Research / Demo APIs | [README](research-demos/README.md) | [Walkthrough](research-demos/COPILOT_WALKTHROUGH.md) | `OMEGA_QUANT.py`, `AAA_PROMETHEUS_SUPER_DEMO.py` | Prototypes and simulations; reported security, payment, market, and performance claims are not verified |
| Public Homepage | [README](homepage/README.md) | [Walkthrough](homepage/COPILOT_WALKTHROUGH.md) | root `index.html` | Static marketing page; outbound product links do not prove checkout integration |

## Shared doctrine for contributors

- Treat source behavior as authoritative; use proposal/specification language for anything not implemented and tested.
- Keep catalogue names intact. Examples in these guides are real catalog entries, not replacement keys or fabricated offerings.
- Preserve data boundaries: DeFi results and Hydra simulations are not production financial signals; portfolio files are not verified products; static dashboards do not authenticate or transact.
- Keep external integrations disabled unless their provider, credentials, environment, review, and tests are explicitly configured.
- Never commit API keys, private keys, tokens, or local deployment manifests. Store credentials in an approved secret manager or environment at runtime.
- Preserve the deployment suite's dry-run default and explicit production confirmation.
- Run focused tests first, then the repository suite; keep generated outputs and temporary files out of source control.

## Suggested review order

Read the root [README](../../README.md), then the suite README and Copilot walkthrough for the area being changed, then the [integration guide](../INTEGRATION_GUIDE.md). Validate the data contract at the producer and consumer before changing either side.
