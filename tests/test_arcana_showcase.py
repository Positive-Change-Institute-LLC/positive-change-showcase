import unittest
from html.parser import HTMLParser
from pathlib import Path


class ScriptSourceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.external_scripts = []
        self.ids = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "script" and attributes.get("src"):
            self.external_scripts.append(attributes["src"])
        if "id" in attributes:
            self.ids.append(attributes["id"])


class ArcanaShowcaseTests(unittest.TestCase):
    def test_static_showcase_does_not_claim_live_wallet_or_transaction_features(self):
        html = Path(__file__).parents[1].joinpath("frontend", "index.html").read_text(
            encoding="utf-8"
        )
        normalized = html.lower()
        self.assertNotIn("admin/admin", normalized)
        self.assertNotIn("/api/login", normalized)
        self.assertNotIn("/api/transaction", normalized)
        self.assertNotIn("innerhtml", normalized)
        self.assertIn("not live nfts or offers", normalized)
        self.assertIn("no wallet is connected", normalized)
        self.assertIn("not implemented", normalized)

    def test_static_showcase_uses_no_external_scripts_and_unique_dom_ids(self):
        parser = ScriptSourceParser()
        parser.feed(
            Path(__file__).parents[1].joinpath("frontend", "index.html").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(parser.external_scripts, [])
        self.assertEqual(len(parser.ids), len(set(parser.ids)))


if __name__ == "__main__":
    unittest.main()
