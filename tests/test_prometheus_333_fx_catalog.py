import unittest
from collections import Counter
from pathlib import Path

from prometheus_333_fx_catalog import FAMILIES, build_catalog, validate_catalog


class Prometheus333FxCatalogTests(unittest.TestCase):
    def test_catalog_has_333_unique_specification_only_effects(self):
        catalog = build_catalog()
        effects = catalog["effects"]
        self.assertEqual(len(effects), 333)
        self.assertEqual(len({effect["id"] for effect in effects}), 333)
        self.assertEqual(len({effect["name"] for effect in effects}), 333)
        self.assertEqual(len({effect["motif_id"] for effect in effects}), 333)
        self.assertTrue(all(effect["render_status"] == "SPECIFICATION_ONLY" for effect in effects))
        self.assertEqual(
            Counter(effect["family"] for effect in effects),
            {family: count for family, count, _ in FAMILIES},
        )

    def test_every_effect_has_consistent_slow_spin_specification(self):
        for effect in build_catalog()["effects"]:
            insignia = effect["insignia"]
            self.assertEqual(insignia["rotation_deg_per_frame"], 1.5)
            self.assertEqual(insignia["render_fps"], 1)
            self.assertEqual(insignia["rotation_deg_per_second"], 1.5)
            self.assertEqual(insignia["seconds_per_rotation"], 240)

    def test_validator_rejects_deployed_render_claim(self):
        catalog = build_catalog()
        catalog["effects"][0]["render_status"] = "DEPLOYED"
        with self.assertRaisesRegex(ValueError, "must not claim rendered assets"):
            validate_catalog(catalog)

    def test_dashboard_exposes_family_selector_and_slow_spin_preview(self):
        dashboard = Path(__file__).parents[1].joinpath(
            "PROMETHEUS_COMMAND_DASHBOARD.html"
        ).read_text(encoding="utf-8")
        self.assertIn('id="fx-family"', dashboard)
        self.assertIn('id="fx-effect"', dashboard)
        self.assertIn("fxCatalogFallback", dashboard)
        self.assertIn("animation: fx-spin var(--fx-spin-duration, 240s)", dashboard)
        self.assertIn("fxPreviewAria", dashboard)


if __name__ == "__main__":
    unittest.main()
