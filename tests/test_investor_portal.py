import tempfile
import unittest
from pathlib import Path

from pci_investor_suite_portal import serve


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
