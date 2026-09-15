#!/usr/bin/env python3
"""Bootstrap sovereign signal layer definitions for a Prometheus × PCI repo."""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


DEFAULT_X_ADDRESS = "https://x.com/your-sovereign-handle"
DEFAULT_TIKTOK_ADDRESS = "https://www.tiktok.com/@your-sovereign-handle"


def build_signals_module(x_address: str, tiktok_address: str) -> str:
    return dedent(
        f'''\
        """PROMETHEUS × PCI SOVEREIGN SIGNAL LAYERS™
        External narrative and telemetry surfaces (X, TikTok).
        © 2026 Positive Change Institute LLC
        """

        SOVEREIGN_SIGNAL_LAYERS = {{
            "description": "External sovereign signal surfaces for Prometheus × PCI Operator.",
            "layers": [
                {{
                    "name": "X Sovereign Signal Layer™",
                    "role": "High-velocity narrative, macro sentiment, and operator presence.",
                    "channel_type": "X",
                    "address": "{x_address}",
                    "canonical": True,
                    "priority": "primary",
                    "functions": [
                        "narrative propagation",
                        "macro sentiment relay",
                        "operator presence anchoring",
                    ],
                }},
                {{
                    "name": "TikTok Sovereign Signal Layer™",
                    "role": "Short-form attention capture, cultural imprinting, and audience expansion.",
                    "channel_type": "TikTok",
                    "address": "{tiktok_address}",
                    "canonical": True,
                    "priority": "secondary",
                    "functions": [
                        "short-form signal amplification",
                        "audience expansion",
                        "visual doctrine propagation",
                    ],
                }},
            ],
        }}
        '''
    )


def write_file(path: Path, content: str, *, force: bool, dry_run: bool) -> str:
    if path.exists() and not force:
        return "exists"
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return "updated" if path.exists() and force else "created"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create core/signals.py for a Prometheus × PCI repository."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root where core/signals.py should be written.",
    )
    parser.add_argument(
        "--x-address",
        default=DEFAULT_X_ADDRESS,
        help="Canonical X address for the sovereign signal layer.",
    )
    parser.add_argument(
        "--tiktok-address",
        default=DEFAULT_TIKTOK_ADDRESS,
        help="Canonical TikTok address for the sovereign signal layer.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite core/signals.py if it already exists.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report the target file without writing it.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    signals_path = repo_root / "core" / "signals.py"
    content = build_signals_module(args.x_address, args.tiktok_address)
    status = write_file(signals_path, content, force=args.force, dry_run=args.dry_run)

    print(f"[{status}] {signals_path}")
    if args.dry_run:
        print("Next steps:")
        print("- Import SOVEREIGN_SIGNAL_LAYERS into core/telemetry.py and api/main.py")
        print("- Expose GET /api/v1/ppci/signals")
        print("- Use the configured addresses as canonical identity anchors")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
