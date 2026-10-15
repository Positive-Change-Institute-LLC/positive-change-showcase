# Copilot Walkthrough — Product Generators

1. Read all three generator scripts and record their actual writes, product lists, random behavior, and external URLs before changing them.
2. Preserve exact catalog product names. Examples include **BATTLEHAVEN : LORDS OF THE ARENA** and **AUTO-LIMITER™**; avoid generic placeholder entries.
3. Do not label JSON "PDF output"; the PDF-named script currently writes one JSON file and no PDF.
4. Do not describe static URLs, prices, valuations, rarity, or IP statements as live, audited, or legally verified.
5. Run scripts only from a disposable temporary directory; keep generated outputs out of source control unless explicitly requested.
6. If connecting to the product catalog, introduce a reviewed stable-ID mapping, schema validation, deterministic behavior where needed, and tests for missing/duplicate entries.
7. Verify with Python compilation and tests for any newly extracted logic; do not run side-effectful generation as an import or test setup step.
8. Keep the user-supplied ReportLab PDF/NFT generator distinct from the checked-in JSON generator; do not claim PDFs, minted assets, game behavior, or working storefronts unless separately implemented and verified.
9. Do not execute the supplied dossier script at import time or include its embedded contact details in output; verify the actual product count and every URL/legal claim before generating a distributable PDF.
