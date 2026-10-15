# Copilot Walkthrough — 333 FX Catalog

1. Read `prometheus_333_fx_catalog.py`, the checked-in JSON, the command dashboard, and `tests/test_prometheus_333_fx_catalog.py`.
2. Keep family counts summing to 333 and preserve uniqueness for effect IDs, names, and motif IDs.
3. Treat specification metadata as data—not evidence that rendering, animation export, patent status, or deployment exists.
4. If adjusting spin semantics, keep per-frame rate, preview FPS, degrees/second, and seconds/rotation mathematically consistent; honor reduced-motion preferences in the UI.
5. Regenerate into `/tmp` first, run `python prometheus_333_fx_catalog.py --check` and `python -m unittest tests.test_prometheus_333_fx_catalog`, then review whether the committed JSON should change.
6. Use real product names from the catalog only when describing a product connection. Do not fabricate an FX-to-product mapping.
