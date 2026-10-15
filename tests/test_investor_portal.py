import functools
import http.server
import threading
import tempfile
import unittest
import urllib.request
from pathlib import Path

from pci_investor_suite_portal import LocalPortfolioHandler, serve


class InvestorPortalTests(unittest.TestCase):
    def test_requires_generated_inventory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with self.assertRaisesRegex(ValueError, "portfolio_index.json"):
                serve(Path(temp_dir), port=8765)

    def test_rejects_symlinked_portfolio_path(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            actual = root / "actual"
            actual.mkdir()
            alias = root / "alias"
            alias.symlink_to(actual, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "symbolic link"):
                serve(alias, port=8765)

    def test_http_server_is_loopback_only_and_sets_security_headers(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "portfolio_index.json").write_text("[]", encoding="utf-8")
            (root / "investor_dashboard.html").write_text("local-only", encoding="utf-8")
            handler = functools.partial(LocalPortfolioHandler, directory=str(root))
            server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                self.assertEqual(server.server_address[0], "127.0.0.1")
                with urllib.request.urlopen(
                    f"http://127.0.0.1:{server.server_address[1]}/investor_dashboard.html"
                ) as response:
                    self.assertEqual(response.read(), b"local-only")
                    self.assertIn("default-src 'self'", response.headers["Content-Security-Policy"])
                    self.assertEqual(response.headers["X-Content-Type-Options"], "nosniff")
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=2)

    def test_portal_has_no_fake_auth_or_external_dependencies(self):
        html = Path(__file__).parents[1].joinpath(
            "PCI_INVESTOR_SUITE_PORTAL.html"
        ).read_text(encoding="utf-8")
        self.assertNotIn("admin/admin", html)
        self.assertNotIn("innerHTML", html)
        self.assertNotIn("<script src=", html)
        self.assertIn("Payments, authentication, trading, minting", html)


if __name__ == "__main__":
    unittest.main()
