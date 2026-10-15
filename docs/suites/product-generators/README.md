# Product and Portfolio Generators

## Included scripts

- `PCI_TURNKEY_GENERATOR_MAIN.py` defines a hard-coded list of 25 game concepts and generates randomized rarity, elements, story, and placeholder storefront URLs into `PCI_Eternal_Architect_Ultimate_Master_Package.json`.
- `PCI_ENTERPRISE_PDF_SPEC_GENERATOR.py` builds a JSON specification package for a separate list of 25 named game concepts. Despite its filename, it does not generate PDF files.
- `PCI_SOVEREIGN_PORTFOLIO_GENERATOR.py` serializes 11 hard-coded product entries and arithmetic valuations into `PCI_Sovereign_Portfolio_Pricing.json`.

These are generation prototypes with independent hard-coded lists. They do not consume `PCI_MASTER_TURNKEYS_150_COMPLETE.json` as a shared source, and the output values, URLs, pricing, valuation, marketplace, and legal statements are not verified by generating JSON.

Names in the scripts include **BATTLEHAVEN : LORDS OF THE ARENA**, **AUTO-LIMITER™**, **INCINERATION ENGINE™**, and **ECONOMIC PHYSICS ENGINE™**. Retain exact names from their catalog source when documenting or testing; do not invent a generic product in place of a catalog entry.

The separately supplied ReportLab proposal for 25 NFT turnkeys and per-product PDFs is not checked-in code and differs from `PCI_TURNKEY_GENERATOR_MAIN.py`, which emits randomized JSON metadata. Neither implementation issues NFTs, creates playable games, or verifies the generated storefront URLs. The supplied FPDF investor-email snippet is also incomplete and is documented separately in the [Hydra Genius package guide](../hydra-genius-investor-package/README.md).

## Safe execution guidance

The scripts write files relative to the current working directory. Do not run them from the repository root unless intentionally generating and reviewing their outputs. Use a clean temporary working directory and inspect output before use. The turnkey generator uses randomness, so repeated output is not deterministic.

## Interoperability

Unification requires an explicit product ID/name mapping and provenance. Do not treat generated storefront URLs as working storefronts, QR links as active checkout, or narrative/rarity output as issued NFTs. Neither generator performs external payments or chain transactions.
