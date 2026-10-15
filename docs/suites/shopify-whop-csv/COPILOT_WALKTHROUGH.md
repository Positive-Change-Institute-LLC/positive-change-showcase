# Copilot Walkthrough — Shopify and Whop CSV Preparation

1. Ask for the actual CSV export before transforming rows; a prompt placeholder is not product data.
2. Read the header and sample rows, then preserve the exact header order, row count, handles, populated prices, and every Whop URL.
3. Do not fill structural blanks or guess business-critical values such as price, tax, fulfillment, variant options, shipping, or product capabilities. Collect those values from an approved source and flag generated copy for review.
4. Generate descriptions and metadata only from supported product information. Escape HTML content and validate the specified sentence and character limits.
5. Parse and re-serialize with a CSV-aware tool so commas, quotes, HTML, and newlines remain correctly encoded.
6. Compare source and output, checking unchanged handles/links/prices, unique handles, valid row counts, tags, and every flagged field.
7. Back up the original export and review Shopify's import preview before using “Overwrite existing products.” Do not automate a production import from this documentation prompt.
8. Keep credentials and private/signed links out of source control, public docs, and test fixtures.
