import json
import tempfile
import unittest
from pathlib import Path

from pci_portfolio_master_builder_v2 import PortfolioBuilderV2


class PortfolioBuilderTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.sources = self.root / "turnkeys"
        self.outputs = self.root / "portfolio"
        self.renders = self.root / "renders"
        self.cinematics = self.root / "cinematics"
        self.pdfs = self.root / "pdfs"
        self.sources.mkdir()
        self.renders.mkdir()
        self.cinematics.mkdir()
        self.pdfs.mkdir()
        self._make_project("Alpha", "education")
        self._make_project("Beta", "education")
        self._make_project("Other", "analytics")
        self.builder = PortfolioBuilderV2(
            self.sources, self.outputs, self.pdfs, self.renders, self.cinematics
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def _make_project(self, name, category):
        project = self.sources / name
        project.mkdir()
        (project / "turnkey.json").write_text(
            json.dumps({"category": category}), encoding="utf-8"
        )
        (project / f"{name}.py").write_text("print('present')\n", encoding="utf-8")
        (project / "notes.txt").write_text("not a supported artifact", encoding="utf-8")
        render_dir = self.renders / name
        render_dir.mkdir()
        (render_dir / "preview.png").write_bytes(b"image-placeholder")
        (render_dir / "source.psd").write_bytes(b"unsupported")

    def test_dry_run_does_not_create_output(self):
        result = self.builder.build_portfolio()
        self.assertEqual(result["project_count"], 3)
        self.assertFalse(self.outputs.exists())

    def test_build_copies_only_supported_artifacts_and_labels_inventory(self):
        result = self.builder.build_portfolio(execute=True)
        alpha = next(item for item in result["projects"] if item["turnkey_name"] == "Alpha")
        self.assertEqual(alpha["category"], "education")
        self.assertFalse(alpha["artifacts_verified"])
        self.assertEqual(alpha["python_scripts"], ["Alpha.py"])
        self.assertEqual(alpha["renders"], ["preview.png"])
        self.assertIn("Beta", alpha["cross_packaging"])
        self.assertNotIn("Other", alpha["cross_packaging"])
        self.assertFalse((self.outputs / "Alpha" / "notes.txt").exists())
        self.assertFalse((self.outputs / "Alpha" / "renders" / "source.psd").exists())
        narration = (self.outputs / "Alpha" / "Alpha_narration.txt").read_text(
            encoding="utf-8"
        )
        self.assertIn("does not verify functionality", narration)
        self.assertIn("No external AI or voice service was used", narration)
        self.assertTrue((self.outputs / "investor_dashboard.html").is_file())
        self.assertEqual(
            json.loads((self.outputs / "portfolio_index.json").read_text())[0]["turnkey_name"],
            "Alpha",
        )

    def test_existing_files_are_preserved_without_overwrite_and_remain_listed(self):
        self.builder.build_portfolio(execute=True)
        copied_script = self.outputs / "Alpha" / "Alpha.py"
        copied_script.write_text("keep this version\n", encoding="utf-8")
        record = next(
            item for item in self.builder.build_portfolio(execute=True)["projects"]
            if item["turnkey_name"] == "Alpha"
        )
        self.assertEqual(copied_script.read_text(encoding="utf-8"), "keep this version\n")
        self.assertEqual(record["python_scripts"], ["Alpha.py"])

    def test_rejects_output_path_through_symlink(self):
        alias = self.root / "portfolio-alias"
        alias.symlink_to(self.outputs, target_is_directory=True)
        builder = PortfolioBuilderV2(
            self.sources, alias, self.pdfs, self.renders, self.cinematics
        )
        with self.assertRaisesRegex(ValueError, "symbolic link"):
            builder.build_portfolio(execute=True)

    def test_does_not_follow_symlink_in_output_asset_tree(self):
        self.builder.build_portfolio(execute=True)
        outside = self.root / "outside"
        outside.mkdir()
        protected = outside / "protected.png"
        protected.write_bytes(b"protected")
        render_target = self.outputs / "Alpha" / "renders"
        (render_target / "preview.png").unlink()
        render_target.rmdir()
        render_target.symlink_to(outside, target_is_directory=True)
        self.builder.build_portfolio(execute=True, overwrite=True)
        self.assertEqual(protected.read_bytes(), b"protected")


if __name__ == "__main__":
    unittest.main()
