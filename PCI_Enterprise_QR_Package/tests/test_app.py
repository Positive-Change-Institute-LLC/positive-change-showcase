import unittest

from backend.app import app


class EnterpriseQRApiTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_dashboard_and_svg_assets_are_served(self):
        self.assertEqual(self.client.get("/").status_code, 200)
        response = self.client.get("/api/qr?product_id=PCI-DEMO-001")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "image/svg+xml")
        self.assertIn(b"<svg", response.data)

    def test_product_metadata_validates_provider_and_identifier(self):
        response = self.client.get("/api/product_metadata?wallet=Base&product_id=PCI-DEMO-001")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "demo_metadata")
        self.assertEqual(response.json["wallet_provider"], "Base")
        self.assertEqual(
            self.client.get("/api/product_metadata?wallet=Unknown&product_id=ok").status_code,
            400,
        )
        self.assertEqual(
            self.client.get("/api/product_metadata?wallet=Base&product_id=../bad").status_code,
            400,
        )

    def test_transaction_never_claims_chain_execution(self):
        response = self.client.post(
            "/api/transaction",
            json={"wallet": "Coinbase", "product_id": "PCI-DEMO-001", "action": "purchase"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "simulation_only")
        self.assertFalse(response.json["submitted"])
        self.assertIsNone(response.json["tx_hash"])

    def test_malformed_transaction_json_types_return_bad_request(self):
        response = self.client.post(
            "/api/transaction",
            json={"wallet": [], "product_id": "valid", "action": "purchase"},
        )
        self.assertEqual(response.status_code, 400)

    def test_analytics_is_not_retained(self):
        response = self.client.post(
            "/api/analytics",
            json={"event": "metadata_viewed", "product_id": "PCI-DEMO-001"},
        )
        self.assertEqual(response.json, {"status": "received", "retained": False})


if __name__ == "__main__":
    unittest.main()
