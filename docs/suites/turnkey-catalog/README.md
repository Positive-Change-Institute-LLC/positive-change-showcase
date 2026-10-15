# Turnkey Catalog Data

## Files and roles

- `PCI_MASTER_TURNKEYS_150_COMPLETE.json` groups named product collections, including **DeltaFlow**, **Chrono Relics**, and **Resilience OS Toolkit**.
- `PCI-Master-Catalogue-Complete.csv` is a separate product catalogue export.
- `TURNKEYS_SHOPIFY.csv` is a Shopify-format import/export sample.
- `TURNKEYS_DATABASE.sql` defines the `turnkeys`, `categories`, and `pricing_tiers` schema and contains SQL seed data.
- `PCI_REVENUE_MATRIX_COMPLETE.json` currently contains metadata only; it is not a populated revenue matrix.
- `PCI_COMPETITION_ENTRY_MANIFEST.json` records a submission description and claims; it is not runtime deployment configuration.

These files are not currently proven to be generated from one shared source of truth. Their naming, row counts, prices, statuses, categories, IDs, and claims can differ. Do not merge or import them as if they were synchronized.

## Safe review

```bash
python -m json.tool PCI_MASTER_TURNKEYS_150_COMPLETE.json >/dev/null
python -m json.tool PCI_REVENUE_MATRIX_COMPLETE.json >/dev/null
python -m json.tool PCI_COMPETITION_ENTRY_MANIFEST.json >/dev/null
```

Review CSV headers and quote handling before any commerce import. Execute `TURNKEYS_DATABASE.sql` only against an explicitly selected local/test database first. It does not write to production on its own.

For prompted bulk edits, follow the [Shopify and Whop CSV preparation guide](../shopify-whop-csv/README.md): preserve handles, populated values, row structure, and existing URLs, and review every generated suggestion before import.

## Interoperability rules

The SQL schema requires unique non-null `handle` values and non-null `name` and `category` values. The SQL categories are their own canonical set for that SQL seed; do not silently substitute names from the separate 150-turnkey JSON or either CSV. A future catalog unification needs a reviewed product ID/handle crosswalk, explicit provenance, and collision tests.

Prices, "LIVE" labels, patent assertions, and product descriptions in data files are supplied catalog values, not independently verified commerce state or legal claims. No QuickNode, payment, wallet, or external catalog API is configured here.
