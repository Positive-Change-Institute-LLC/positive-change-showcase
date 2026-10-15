# Copilot Walkthrough — Arcana Showcase

1. Read `index.html`, this README, and `tests/test_arcana_showcase.py`.
2. Preserve semantic HTML, responsive layout, keyboard focus, bilingual labels, and safe text-node rendering.
3. Do not reintroduce the supplied `admin/admin` form, fake JWT, external QR CDN, inline event handlers, `innerHTML`, wallet connection, minting, or mock transaction success.
4. Keep the page's three concept records distinct from the real-name turnkey catalog unless a tested, documented mapping is added.
5. Add tests for any new input behavior or mapping. Run `python -m unittest tests.test_arcana_showcase` and check inline JavaScript with `node --check`.
6. If the public site changes, update the Pages copy step and test the published relative path.
