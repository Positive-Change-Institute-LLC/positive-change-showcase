"""Concept manifest and asking-price summary for Genesis Relics.

This module does not connect to AI services, wallets, marketplaces, or blockchains.
Prices are supplied asking-price inputs, not an appraisal or market valuation.
"""

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


GENESIS_RELICS = {
    "name": "GENESIS_RELICS:NFT_EVOLUTION_HUB:ENTERPRISE_ADAPTIVE",
    "purpose": (
        "Proposed dynamic NFT evolution concept with cinematic guides, "
        "dashboards, and collector insights"
    ),
    "status": "concept_only",
    "planned_capabilities": [
        "Interactive dashboards",
        "NFT evolution sequences",
        "KPI metrics",
        "Cinematic guides",
    ],
    "integrations": {
        "prometheus_orchestration": "Proposed; not connected",
        "grok": "Proposed; not connected",
    },
    "pricing_usd": {
        "one_time_asking_price": 250000,
        "monthly_asking_price": 1999,
        "yearly_asking_price": 21999,
        "vip_extras_asking_price": 4999,
        "basis": "User-provided proposed prices; not a market valuation",
    },
    "links": {
        "whop": "https://whop.com/@positivechangeinstitute/GENESIS_RELICS",
        "linktree": "https://linktr.ee/critter2881/GENESIS_RELICS",
        "github": "https://github.com/positivechangeinstitute/GENESIS_RELICS",
        "status": "User-provided links; availability and ownership not verified",
    },
    "media_assets": {
        "status": "Planned filenames only; no media files are included or generated",
        "images": ["concept1.png", "concept2.png", "render1.gif", "render2.gif"],
        "dashboards": ["dashboard_main.png", "dashboard_evolution.png"],
        "videos": ["cinematic_intro.mp4", "evolution_demo.mp4"],
    },
    "wallet": {
        "status": "Not configured; no wallet address or donation integration",
    },
    "copyright_notice": "Copyright notice supplied by user; ownership is not verified",
    "trademarks": [
        "Arcanex AutoForge™",
        "Prometheus Superintelligence™",
        "BlueChip Master™",
    ],
}


def build_metadata_fingerprints(manifest=GENESIS_RELICS):
    """Return stable identifiers for planned media names, not media or ownership proofs."""
    fingerprints = {}
    for category, files in manifest["media_assets"].items():
        if category == "status":
            continue
        for filename in files:
            material = f"{manifest['name']}:{category}:{filename}"
            fingerprints[filename] = hashlib.sha256(material.encode("utf-8")).hexdigest()
    return fingerprints


def build_portfolio_queue(now=None):
    """Build an inert queue record; no modules are executed or gates changed."""
    checkpoint = now or datetime.now(timezone.utc)
    return {
        "modules": [GENESIS_RELICS["name"]],
        "gate_status": {GENESIS_RELICS["name"]: False},
        "last_checkpoint": checkpoint.isoformat(),
        "orchestration_status": "not_connected",
        "simulation_only": True,
    }


def write_package(output_dir):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    files = {
        "genesis_manifest.json": GENESIS_RELICS,
        "genesis_metadata_fingerprints.json": build_metadata_fingerprints(),
        "portfolio_queue.json": build_portfolio_queue(),
    }
    for filename, content in files.items():
        (output / filename).write_text(json.dumps(content, indent=2) + "\n", encoding="utf-8")
    return [output / filename for filename in files]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        help="Optional directory for concept manifest JSON files; no files are written by default.",
    )
    args = parser.parse_args()
    if args.output_dir:
        written = write_package(args.output_dir)
        print("Concept-only package written:")
        for path in written:
            print(path)
    else:
        print(json.dumps({
            "name": GENESIS_RELICS["name"],
            "status": GENESIS_RELICS["status"],
            "pricing_usd": GENESIS_RELICS["pricing_usd"],
            "media_status": GENESIS_RELICS["media_assets"]["status"],
            "wallet_status": GENESIS_RELICS["wallet"]["status"],
        }, indent=2))


if __name__ == "__main__":
    main()
