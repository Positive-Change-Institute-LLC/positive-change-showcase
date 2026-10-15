# Copilot Walkthrough — Turnkey Catalogs

1. Inspect each file independently before editing: SQL schema/seeds, master JSON, product CSV, Shopify CSV, revenue matrix, and competition manifest.
2. Preserve source provenance. Do not "fix" an inconsistency by copying a product row across catalogs without a documented mapping decision.
3. When examples need a name, use the exact spelling from the source being documented—for example, **DeltaFlow** in the master JSON or **Resilience OS Toolkit** in the applicable product inventory.
4. Preserve unique SQL handles and ensure each seed category matches the category table used by that SQL database.
5. Validate JSON syntax, CSV parsing, duplicate IDs/handles, and category references. Test SQL against a temporary SQLite database before considering D1.
6. Do not claim that an import, sale, subscription, deployment, product status, price, or IP claim has been verified by parsing a local file.
7. Do not include API keys or credentials in catalog data, CSV exports, examples, or generated storefront content.
