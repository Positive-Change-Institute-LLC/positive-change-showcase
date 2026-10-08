import json
import tempfile
import unittest
from pathlib import Path

from GENESIS_RELICS_NFT_EVOLUTION_HUB import (
    GENESIS_RELICS,
    build_metadata_fingerprints,
    build_portfolio_queue,
    write_package,
)


class GenesisRelicsTests(unittest.TestCase):
    def test_prices_are_identified_as_user_supplied_asking_prices(self):
        pricing = GENESIS_RELICS["pricing_usd"]
        self.assertEqual(pricing["one_time_asking_price"], 250000)
        self.assertIn("not a market valuation", pricing["basis"])
        self.assertEqual(GENESIS_RELICS["status"], "concept_only")

    def test_fingerprints_are_stable_and_cover_planned_media_names(self):
        first = build_metadata_fingerprints()
        self.assertEqual(first, build_metadata_fingerprints())
        self.assertEqual(
            set(first),
            {
                "concept1.png", "concept2.png", "render1.gif", "render2.gif",
                "dashboard_main.png", "dashboard_evolution.png",
                "cinematic_intro.mp4", "evolution_demo.mp4",
            },
        )
        self.assertIn("not media or ownership proofs", build_metadata_fingerprints.__doc__)

    def test_queue_remains_inert_and_package_writes_only_when_requested(self):
        queue = build_portfolio_queue()
        self.assertTrue(queue["simulation_only"])
        self.assertEqual(queue["orchestration_status"], "not_connected")
        self.assertFalse(next(iter(queue["gate_status"].values())))

        with tempfile.TemporaryDirectory() as temp_dir:
            paths = write_package(Path(temp_dir) / "package")
            self.assertEqual(len(paths), 3)
            manifest = json.loads(paths[0].read_text())
            self.assertEqual(manifest["wallet"]["status"], GENESIS_RELICS["wallet"]["status"])
            self.assertTrue(all(path.is_file() for path in paths))


if __name__ == "__main__":
    unittest.main()
