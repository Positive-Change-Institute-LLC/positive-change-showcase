# Shopify and Whop CSV Preparation

## Status

This is a documentation-only workflow. The repository contains a Shopify-format sample at `TURNKEYS_SHOPIFY.csv`, but no CSV rows were included with the supplied “upgraded final prompt,” and no bulk transformation or Whop/Shopify API integration is implemented.

## Preserve source data

- Keep the exported header names, column order, row count, handles, populated prices, and existing Whop URLs unchanged.
- Treat Whop URLs as opaque values; preserve the complete string, including query parameters.
- Do not fill every blank automatically. Shopify exports can use blank cells to represent variant continuation rows or absent optional values. Adding invented values or `N/A` to those cells can change import behavior.
- Do not infer a real price, shipping/tax status, fulfillment method, variant option, availability, legal statement, or product capability from a title alone. Use an approved source or leave the field for owner review.
- Product descriptions, tags, SEO copy, product type, and alt text can be generated as reviewable suggestions, but must not introduce unsupported product or financial claims.

## Review before import

Write and review a diff rather than overwriting the source export. Validate CSV quoting and parseability, unchanged headers and row count, unique unchanged handles, unchanged populated prices and Whop links, and every generated field. Check HTML-escaped descriptions, tag count, and the SEO character limits from the prompt. Review Shopify's import preview and keep a backup before selecting “Overwrite existing products.”

The existing catalogs are independent inputs; see the [Turnkey Catalog guide](../turnkey-catalog/README.md) before mapping names or categories. The supplied prompt contains `[PASTE YOUR CSV ROWS HERE]`, not CSV data, so it is not enough to generate an import file.
