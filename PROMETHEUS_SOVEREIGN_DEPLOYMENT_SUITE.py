#!/usr/bin/env python3
"""Safely orchestrate explicitly configured deployment commands.

Deployment commands are supplied in a local JSON manifest because this
repository does not contain Shopify, Whop, Workers, or API deployment projects.
The default mode validates and prints a plan; commands run only with --execute.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

PCI_COPYRIGHT = (
    "© 2026 Positive Change Institute LLC — All Systems, Divisions, Engines, "
    "Motifs, Insignias, and Products Are the Exclusive Property of Positive "
    "Change Institute LLC."
)

DEPLOY_TARGETS = (
    "homepage",
    "shopify",
    "whop",
    "cloudflare_workers",
    "api_layer",
)


@dataclass(frozen=True)
class DeployContext:
    env: str
    version: str
    commit_hash: str
    artifacts_dir: Path
    metadata: dict[str, Any]


@dataclass(frozen=True)
class DeployStep:
    target: str
    command: tuple[str, ...]
    cwd: Path


def run_cmd(command: Sequence[str], cwd: Path, ctx: DeployContext) -> None:
    """Run an argument-vector command without invoking a shell."""
    environment = os.environ.copy()
    environment.update(
        {
            "PCI_DEPLOY_ENV": ctx.env,
            "PCI_DEPLOY_VERSION": ctx.version,
            "PCI_DEPLOY_COMMIT": ctx.commit_hash,
            "PCI_ARTIFACTS_DIR": str(ctx.artifacts_dir.resolve()),
        }
    )
    result = subprocess.run(list(command), cwd=cwd, env=environment, check=False)
    if result.returncode:
        raise RuntimeError(
            f"Deployment command for a configured target failed "
            f"(exit code {result.returncode})."
        )


class PrometheusDeploymentEngine:
    """Validate configured deployment steps and execute them on request."""

    def __init__(
        self,
        ctx: DeployContext,
        repo_root: Path,
        manifest_path: Path,
        targets: Sequence[str],
    ) -> None:
        self.ctx = ctx
        self.repo_root = repo_root.resolve()
        self.manifest_path = manifest_path.resolve()
        self.targets = tuple(targets)
        self.steps: list[DeployStep] = []

    def load_plan(self) -> list[DeployStep]:
        if not self.targets:
            raise ValueError("Select at least one deployment target.")
        unsupported = sorted(set(self.targets) - set(DEPLOY_TARGETS))
        if unsupported:
            raise ValueError(f"Unsupported deployment targets: {', '.join(unsupported)}")

        try:
            self.manifest_path.relative_to(self.repo_root)
        except ValueError as exc:
            raise ValueError("Deployment manifest must be inside the repository.") from exc

        try:
            manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError(f"Cannot read deployment manifest: {exc}") from exc

        configured = manifest.get("targets") if isinstance(manifest, dict) else None
        if not isinstance(configured, dict):
            raise ValueError("Manifest must contain a 'targets' object.")

        steps: list[DeployStep] = []
        for target in self.targets:
            target_steps = configured.get(target)
            if not isinstance(target_steps, list) or not target_steps:
                raise ValueError(f"No deployment steps configured for target '{target}'.")
            for item in target_steps:
                if not isinstance(item, dict):
                    raise ValueError(f"Each step for '{target}' must be an object.")
                command = item.get("command")
                cwd_value = item.get("cwd")
                if (
                    not isinstance(command, list)
                    or not command
                    or any(not isinstance(arg, str) or not arg for arg in command)
                    or not isinstance(cwd_value, str)
                    or not cwd_value
                ):
                    raise ValueError(
                        f"Each step for '{target}' needs a non-empty command array "
                        "and working directory."
                    )
                cwd = (self.repo_root / cwd_value).resolve()
                try:
                    cwd.relative_to(self.repo_root)
                except ValueError as exc:
                    raise ValueError(
                        f"Working directory for '{target}' must be inside the repository."
                    ) from exc
                if not cwd.is_dir():
                    raise ValueError(
                        f"Working directory for '{target}' does not exist: {cwd_value}"
                    )
                steps.append(DeployStep(target, tuple(command), cwd))

        self.steps = steps
        return steps

    def deploy_all(self, execute: bool = False) -> None:
        if not self.steps:
            self.load_plan()

        mode = "Executing" if execute else "Dry run"
        self._log(f"{mode}: {len(self.steps)} configured deployment step(s).")
        for step in self.steps:
            self._log(
                f"{mode} target '{step.target}' in "
                f"{step.cwd.relative_to(self.repo_root)}."
            )

        if not execute:
            self._log("No files or external services were changed.")
            return

        self._embed_copyright()
        for step in self.steps:
            run_cmd(step.command, step.cwd, self.ctx)
        self._log("All configured deployment steps completed.")

    def _embed_copyright(self) -> None:
        artifacts_dir = self.ctx.artifacts_dir.resolve()
        try:
            artifacts_dir.relative_to(self.repo_root)
        except ValueError as exc:
            raise ValueError("Artifacts directory must be inside the repository.") from exc
        artifacts_dir.mkdir(parents=True, exist_ok=True)
        (artifacts_dir / "PCI_COPYRIGHT.txt").write_text(
            PCI_COPYRIGHT + "\n", encoding="utf-8"
        )
        (artifacts_dir / "deployment.json").write_text(
            json.dumps(
                {
                    "environment": self.ctx.env,
                    "version": self.ctx.version,
                    "commit": self.ctx.commit_hash,
                    **self.ctx.metadata,
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    def _log(self, message: str) -> None:
        print(f"[PROMETHEUS_DEPLOY][{self.ctx.env}] {message}")


def _commit_hash(repo_root: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo_root,
        check=False,
        capture_output=True,
        text=True,
    )
    commit = result.stdout.strip()
    if result.returncode or not re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", commit):
        raise ValueError("Could not determine a valid Git commit hash.")
    return commit


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--env", choices=("dev", "staging", "prod"), default="staging")
    parser.add_argument("--version", required=True)
    parser.add_argument("--commit", help="Full Git commit hash; defaults to HEAD.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("deployment-targets.json"),
        help="JSON deployment manifest path relative to --repo-root.",
    )
    parser.add_argument("--artifacts-dir", type=Path, default=Path("artifacts"))
    parser.add_argument(
        "--target",
        action="append",
        choices=DEPLOY_TARGETS,
        dest="targets",
        help="Target to deploy; repeat to select multiple. Defaults to all targets.",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Execute configured commands. Without this flag, only validate and show the plan.",
    )
    parser.add_argument(
        "--confirm-production",
        action="store_true",
        help="Required together with --execute when --env=prod.",
    )
    args = parser.parse_args(argv)
    if args.env == "prod" and args.execute and not args.confirm_production:
        parser.error("production execution requires --confirm-production.")
    return args


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    repo_root = args.repo_root.resolve()
    if not repo_root.is_dir():
        print("Repository root does not exist.", file=sys.stderr)
        return 2

    try:
        commit = args.commit or _commit_hash(repo_root)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    if not re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", commit):
        print("Commit must be a full 40- or 64-character hexadecimal hash.", file=sys.stderr)
        return 2

    manifest = args.manifest
    if not manifest.is_absolute():
        manifest = repo_root / manifest
    artifacts_dir = args.artifacts_dir
    if not artifacts_dir.is_absolute():
        artifacts_dir = repo_root / artifacts_dir

    ctx = DeployContext(
        env=args.env,
        version=args.version,
        commit_hash=commit,
        artifacts_dir=artifacts_dir,
        metadata={"prometheus": True},
    )
    targets = args.targets or DEPLOY_TARGETS
    engine = PrometheusDeploymentEngine(ctx, repo_root, manifest, targets)
    try:
        engine.load_plan()
        engine.deploy_all(execute=args.execute)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"Deployment stopped: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
