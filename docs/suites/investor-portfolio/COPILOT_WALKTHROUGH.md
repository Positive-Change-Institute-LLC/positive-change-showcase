# Copilot Walkthrough — Investor Portfolio

1. Read the builder, portal server, portal HTML, and `tests/test_portfolio_builder.py` / `tests/test_investor_portal.py`.
2. Preserve dry-run defaults, source/output separation, no symlink traversal, safe file allowlists, no-overwrite defaults, and loopback binding.
3. Keep `portfolio_index.json` as the explicit boundary between the builder and UI. Validate its schema and treat names, categories, filenames, and suggestion strings as untrusted input.
4. Never add `innerHTML`, `os.system`, hard-coded credentials, remote media/CDN scripts, login/mint endpoints, or claims of TTS/payment support.
5. Use exact catalog names like **Investor Dashboard** only for examples; do not synthesize product records when no corresponding local source folder exists.
6. Run `python -m unittest tests.test_portfolio_builder tests.test_investor_portal` and `python -m py_compile pci_portfolio_master_builder_v2.py pci_investor_suite_portal.py`.
7. Check HTTP binding/security headers and report that this tool inventories files—it does not prove their function or commercial readiness.
