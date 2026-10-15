import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from PROMETHEUS_SOVEREIGN_DEPLOYMENT_SUITE import (
    DeployContext,
    PrometheusDeploymentEngine,
)


class DeploymentSuiteTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "surface").mkdir()
        self.manifest = self.root / "deployment-targets.json"
        self.manifest.write_text(
            json.dumps(
                {
                    "targets": {
                        "homepage": [
                            {"command": ["printf", "deploy"], "cwd": "surface"}
                        ]
                    }
                }
            ),
            encoding="utf-8",
        )
        self.artifacts = self.root / "artifacts"
        self.context = DeployContext(
            env="staging",
            version="1.2.3",
            commit_hash="a" * 40,
            artifacts_dir=self.artifacts,
            metadata={},
        )
        self.engine = PrometheusDeploymentEngine(
            self.context, self.root, self.manifest, ["homepage"]
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_dry_run_does_not_execute_commands_or_write_artifacts(self):
        self.engine.load_plan()
        output = io.StringIO()
        with patch(
            "PROMETHEUS_SOVEREIGN_DEPLOYMENT_SUITE.subprocess.run"
        ) as run, contextlib.redirect_stdout(output):
            self.engine.deploy_all()

        run.assert_not_called()
        self.assertFalse(self.artifacts.exists())
        self.assertIn("Dry run", output.getvalue())

    def test_execution_writes_copyright_then_runs_commands(self):
        self.engine.load_plan()
        with patch(
            "PROMETHEUS_SOVEREIGN_DEPLOYMENT_SUITE.subprocess.run"
        ) as run:
            run.return_value.returncode = 0
            self.engine.deploy_all(execute=True)

        self.assertTrue((self.artifacts / "PCI_COPYRIGHT.txt").is_file())
        metadata = json.loads((self.artifacts / "deployment.json").read_text(encoding="utf-8"))
        self.assertEqual(metadata["environment"], "staging")
        self.assertEqual(metadata["version"], "1.2.3")
        run.assert_called_once()
        args, kwargs = run.call_args
        self.assertEqual(args, (["printf", "deploy"],))
        self.assertEqual(kwargs["cwd"], self.root / "surface")
        self.assertEqual(kwargs["env"]["PCI_DEPLOY_VERSION"], "1.2.3")
        self.assertEqual(kwargs["env"]["PCI_DEPLOY_COMMIT"], "a" * 40)

    def test_rejects_working_directory_outside_repository(self):
        self.manifest.write_text(
            json.dumps(
                {
                    "targets": {
                        "homepage": [
                            {"command": ["printf", "deploy"], "cwd": "../"}
                        ]
                    }
                }
            ),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ValueError, "inside the repository"):
            self.engine.load_plan()

    def test_rejects_unconfigured_target_before_execution(self):
        self.engine.targets = ("shopify",)
        with self.assertRaisesRegex(ValueError, "No deployment steps configured"):
            self.engine.load_plan()

    def test_command_failure_stops_deployment(self):
        self.engine.load_plan()
        with patch(
            "PROMETHEUS_SOVEREIGN_DEPLOYMENT_SUITE.subprocess.run"
        ) as run:
            run.return_value.returncode = 1
            with self.assertRaisesRegex(RuntimeError, "exit code 1"):
                self.engine.deploy_all(execute=True)


if __name__ == "__main__":
    unittest.main()
