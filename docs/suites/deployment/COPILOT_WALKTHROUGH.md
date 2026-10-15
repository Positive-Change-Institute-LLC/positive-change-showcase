# Copilot Walkthrough — Deployment Orchestrator

1. Read `PROMETHEUS_SOVEREIGN_DEPLOYMENT_SUITE.py`, `tests/test_deployment_suite.py`, `.gitignore`, and this suite README before changing behavior.
2. Preserve the default dry run, supported-target validation, repository-contained working directories, argument-array execution, and fail-closed behavior.
3. Keep production behind both `--execute` and `--confirm-production`. Do not create live commands based only on a product name such as **AI Business Builder**.
4. Keep `deployment-targets.json` local/ignored. Never ask for or copy credentials into the manifest, source, logs, test fixtures, or pull request.
5. Add tests for each behavior change, including no side effects in dry-run and no execution after invalid or missing target configuration.
6. Verify with `python -m unittest tests.test_deployment_suite` and `git diff --check`.
7. Describe which behavior is tested and which provider setup remains external; do not claim deployment without deployment evidence.
