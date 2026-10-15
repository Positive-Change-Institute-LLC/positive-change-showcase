# Prometheus Deployment Orchestrator

## Purpose

`PROMETHEUS_SOVEREIGN_DEPLOYMENT_SUITE.py` validates a local JSON plan and, only when explicitly requested, runs its configured commands. It is not a hard-coded deployment implementation for every product or provider.

## Current behavior

- Supported target labels are `homepage`, `shopify`, `whop`, `cloudflare_workers`, and `api_layer`.
- A local `deployment-targets.json` is required for selected targets. It is ignored by Git and must be reviewed locally.
- Default execution is a dry run. `--execute` is required to run commands; `--env prod` additionally requires `--confirm-production`.
- Commands use argument arrays, run sequentially, and stop on the first failure. No automatic rollback is provided.
- Deployment metadata and the PCI copyright notice are written only when execution is enabled.
- The separate Pages workflow builds and deploys the checked-in static site; this orchestrator does not configure Pages credentials.

## Validate a configured plan

From the repository root, after a local manifest has been reviewed:

```bash
python PROMETHEUS_SOVEREIGN_DEPLOYMENT_SUITE.py --version 1.0.0 --target homepage
```

That command is a plan validation/dry run. Add `--execute` only after reviewing the exact command and target. Production execution requires both `--execute` and `--confirm-production`. Do not copy secrets into the manifest or command arguments.

## Interoperability

The suite accepts operator-supplied commands and gives them deployment metadata through `PCI_DEPLOY_ENV`, `PCI_DEPLOY_VERSION`, `PCI_DEPLOY_COMMIT`, and `PCI_ARTIFACTS_DIR`. It does not read the product catalog and does not infer that **Prometheus Sovereign Intelligence** or **Investor Dashboard** is ready to publish.

## Validation

```bash
python -m unittest tests.test_deployment_suite
```

No provider deployment command, external credential, or production manifest is committed.
