# PCI Suite Integration Guide

This guide records current repository handoffs—not a promise that every design document or product is deployed. Product labels below are drawn from the checked-in catalogs; a label alone does not establish product readiness, a sale, or an external integration.

## Implemented local handoffs

| Producer | Output / contract | Consumer | Boundary |
|---|---|---|---|
| `prometheus_333_fx_catalog.py` | `PROMETHEUS_333_FX_CATALOG.json`, 333 validated `SPECIFICATION_ONLY` entries | Command dashboard selector | Dashboard fetches the static JSON from the same site and has an embedded family fallback |
| `pci_portfolio_master_builder_v2.py --build` | Per-project copied files, `metadata.json`, `portfolio_index.json` | `pci_investor_suite_portal.py` serves `investor_dashboard.html` and the index | Local file inventory only; copy does not validate product function or readiness |
| `ppci_sws_proof/hydra.py` | Validated deterministic `POST /hydra/simulate` result | Local clients or tests | Modeled corridor and decision only; not connected to portfolio allocations |
| `pci_defi_analysis_suite/main.py` | Deterministic sample analysis object | DeFi CLI, API, terminal dashboard | Fixed sample input; not live market/chain data |
| `TURNKEYS_DATABASE.sql` | Local schema and seed rows with unique handles/categories | Local SQLite/D1-compatible testing and review | Running SQL changes only the database explicitly selected by the operator |
| `.github/workflows/deploy.yml` | `_site` static Pages artifact | GitHub Pages deployment job | Publishes only paths copied by the workflow; it does not deploy Shopify, Whop, QuickNode, or API services |

Examples from product catalogs include **AI Business Builder**, **Investor Dashboard**, **Prometheus Sovereign Intelligence**, and **DeltaFlow**. They are identifiers for catalog documentation, not inputs to a live model, payment, or blockchain transaction.

## Designed but not wired together

- The command dashboard's Hydra preview mirrors a deterministic calculation in browser code. It does not call the Hydra API.
- The turnkey generators, catalog data, product list pages, and investor portfolio browser are not connected to a shared live product database.
- The deployment orchestrator reads `deployment-targets.json`, which is local and ignored. It is separate from the Pages workflow and fails closed when selected targets lack configured commands.
- Circle, QuickNode, wallets, QR generation, payments, Whop actions, external AI/TTS, and live-chain data remain unconfigured unless separately implemented and reviewed.
- `APO.py` and `OMEGA_QUANT.py` expose prototypes whose claims and API behavior must not be treated as validated authority or production service. The supplied Hypergraph/PSL/SDE APO specification is not implemented by its static metadata routes.
- The supplied Hydra Genius investor-email/PDF and Prometheus game-economy/ERC materials are proposals. They do not provide a verified investor package, generated PDFs, minted NFTs, token rewards, wallet flows, or standards integrations.
- ViralForge™ Pro appears in the product catalog, but the supplied browser UI is not a checked-in implementation. Its Claude API-key flow is client-side and unsafe for public deployment; no publishing, analytics, or revenue integration is verified.
- The supplied HackEntry dashboard uses randomized wallet/product placeholders and an unverified QR destination; it does not integrate the catalog, wallet networks, or NFT contracts. The separate Arcana enterprise login/minting page has no backend in this repository and is not the checked-in showcase.
- The supplied Arcana NFT list and enterprise dossier are static proposals: product IDs/prices/links and payment claims are unverified, and the dossier embeds contact information. Neither is connected to the checked-in Arcana showcase or product catalogs.
- **Genesis Relics** appears as a name in the master catalog, but its supplied pricing/hash/queue script does not implement a valuation, media assets, wallet, Grok, or evolution service. The Arcanex BlueChip records and requested rendering/signature package are also proposals; no such assets or integrations are checked in.
- The supplied BlueChip narration/motif/publishing scripts are not an implementation: they can delete destination trees, upload assets, and push Git commits/tags without a dry-run gate; the Whop/Linktree steps only construct or print links. Do not execute them or imitate the named performers.
- The supplied Explorer Gateway OpenAPI document is not a verified service contract or client. Its external endpoints, optional authentication, schemas, and undeclared WebSocket behavior require validation before integration.
- `PCI_DEFI_ANALYSIS_SUITE_ALL_IN_ONE` is design material, not live chain analysis. The checked-in DeFi API uses fixed sample inputs.
- The supplied PCI Automation Suite has an inline sample registry and text-file generator only. Its “120+” wording does not match the shown two-product registry, and its Whop IDs are not provider integrations.
- Shopify/Whop CSV preparation is manual and review-only; no rows were supplied with the prompt, and no exporter, importer, or commerce API is wired to the catalogs.

## Safe integration sequence

1. Choose a specific source of truth and record the exact field names, formats, ownership, and versioning.
2. Keep generated data deterministic where possible and validate schema, unique identifiers, and allowed categories before consuming it.
3. Add an adapter with explicit timeouts, failure behavior, and input validation; do not let a static page or data catalog silently initiate value-bearing actions.
4. Add consumer tests for valid data, missing records, malformed data, duplicates, and rejected external requests.
5. Keep credentials outside source, examples, docs, frontend assets, and Git history. For any key already pasted into chat or otherwise exposed, revoke it and issue a replacement before use.
6. Verify local behavior first. External deployment must remain disabled until the target is explicitly configured, reviewed, and separately confirmed.

## QuickNode note

No QuickNode client is wired to a suite in the checked-in implementation. If a future adapter is approved, read its credential at runtime from a secret manager or an environment variable such as `QUICKNODE_API_KEY`; do not add the value to a file or browser bundle. The exact endpoint/network and read/write permissions must be decided and documented before implementation.
