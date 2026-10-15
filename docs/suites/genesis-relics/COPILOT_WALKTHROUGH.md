# Copilot Walkthrough — Genesis Relics

1. Treat **Genesis Relics** as a cataloged name only; the supplied hub script and pricing are not checked-in implementation data.
2. Separate prices from valuation. Do not imply an investment value, expected return, or market price without a reviewed valuation method and evidence.
3. Confirm that referenced media files exist before building a manifest; the names in `media_assets` are not generated assets.
4. Hash actual file bytes and include stable filenames/version data if file-integrity checks are later required. The submitted timestamp-based string hashes do not authenticate files.
5. Replace the wallet placeholder and test every generated destination before publication; do not imply wallet, payment, or Grok integration.
6. Keep script output out of the repository root; its checkpoint function writes/overwrites JSON files in the current directory.
7. Add a reviewed product-ID mapping and tests before connecting the catalog, investor portal, or any asset service.
