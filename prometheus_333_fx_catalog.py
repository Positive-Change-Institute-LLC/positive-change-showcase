#!/usr/bin/env python3
"""Generate and validate the deterministic Prometheus 333 FX catalog."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

FAMILIES = (
    ("Pulse", 60, "Electric_Blue_White"),
    ("Arc", 48, "Solar_Gold_Ember"),
    ("Sigil", 48, "Runic_Violet_Cyan"),
    ("Forge", 48, "Alloy_Steel_Molten"),
    ("Veil", 45, "Mist_Silver_Teal"),
    ("Fracture", 42, "Obsidian_Void"),
    ("Core", 42, "Reactor_Green_White"),
)
CAMERAS_MM = (35, 50, 85, 120)
MOTIF_FORMS = (
    "Aegis", "Aperture", "Beacon", "Crest", "Halo", "Lattice",
    "Monolith", "Prism", "Sigil", "Spiral",
)
MOTION_FORMS = (
    "Afterglow", "Bloom", "Cascade", "Convergence", "Drift",
    "Echo", "Eclipse", "Pulse", "Resonance", "Wake",
)


def build_catalog() -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    for family, count, palette in FAMILIES:
        for sequence in range(1, count + 1):
            motif = MOTIF_FORMS[(sequence - 1) % len(MOTIF_FORMS)]
            motion = MOTION_FORMS[((sequence - 1) // len(MOTIF_FORMS)) % len(MOTION_FORMS)]
            effect_id = f"PCI-FX-{family.upper()}-{sequence:03d}"
            entries.append(
                {
                    "id": effect_id,
                    "name": f"{family}::{sequence:03d} | {motif}_{motion}",
                    "family": family,
                    "sequence": sequence,
                    "motif_id": f"MOTIF::{effect_id}",
                    "palette": palette,
                    "camera_mm": CAMERAS_MM[(sequence - 1) % len(CAMERAS_MM)],
                    "lighting": "Single_Key_Rim_Glow",
                    "style": "Cinematic_Obsidian",
                    "background": "Pure_Black",
                    "layer_count": 7,
                    "insignia": {
                        "material": "Metallic_Glass_Hybrid",
                        "motion": "SLOW_SPIN_DIGITAL_EFFECT",
                        "rotation_deg_per_frame": 1.5,
                        "render_fps": 1,
                        "rotation_deg_per_second": 1.5,
                        "seconds_per_rotation": 240,
                    },
                    "render_status": "SPECIFICATION_ONLY",
                }
            )

    catalog: dict[str, Any] = {
        "catalog_id": "PROMETHEUS_333_FX_TURNKEY",
        "catalog_version": "1.0.0",
        "schema_version": 1,
        "authorship": "Positive Change Institute LLC",
        "doctrine": "PROMETHEUS_STANDARD_V1",
        "integrity": "CANON_LOCKED",
        "classification": "7_FAMILY_MACRO_TAXONOMY",
        "naming": "HYBRID_FORMAT",
        "rules": {
            "redundancy": "ZERO",
            "drift": "ZERO",
            "motif_reuse": "ZERO",
            "expansion": "ON_DEMAND",
        },
        "family_counts": {family: count for family, count, _ in FAMILIES},
        "fx_total": len(entries),
        "render_specification": {
            "style": "Cinematic_Obsidian",
            "lighting": "Single_Key_Rim_Glow",
            "camera_mm": list(CAMERAS_MM),
            "insignia_layers": 7,
            "insignia_material": "Metallic_Glass_Hybrid",
            "background": "Pure_Black",
            "spin": {
                "requested_rotation_deg_per_frame": 1.5,
                "preview_render_fps": 1,
                "preview_rotation_deg_per_second": 1.5,
                "preview_seconds_per_rotation": 240,
                "note": "Frame rate is explicit so the requested 1.5 degrees per frame renders as a slow spin.",
            },
            "family_palettes": {family: palette for family, _, palette in FAMILIES},
            "output": "Render_Ready_Specification",
        },
        "deployment_status": "CATALOG_GENERATED_RENDER_ASSETS_NOT_DEPLOYED",
        "activation_phrase": "Prometheus 333 — Execute Sovereign FX Expansion",
        "activation_note": "Reference phrase only; generating this catalog does not deploy or activate external systems.",
        "legal_notice": (
            "© 2026 Positive Change Institute LLC — FX, motifs, insignias, and "
            "doctrines are asserted as PCI intellectual property by the author. "
            "Trademark and patent status has not been independently verified."
        ),
        "effects": entries,
    }
    validate_catalog(catalog)
    return catalog


def validate_catalog(catalog: dict[str, Any]) -> None:
    effects = catalog.get("effects")
    if not isinstance(effects, list) or len(effects) != 333:
        raise ValueError("Catalog must contain exactly 333 effect records.")
    if len({effect.get("id") for effect in effects}) != 333:
        raise ValueError("Effect IDs must be unique.")
    if len({effect.get("name") for effect in effects}) != 333:
        raise ValueError("Effect names must be unique.")
    if len({effect.get("motif_id") for effect in effects}) != 333:
        raise ValueError("Motif IDs must be unique.")

    actual_counts: dict[str, int] = {}
    for effect in effects:
        actual_counts[effect.get("family")] = actual_counts.get(effect.get("family"), 0) + 1
    expected_counts = {family: count for family, count, _ in FAMILIES}
    if actual_counts != expected_counts or catalog.get("family_counts") != expected_counts:
        raise ValueError("Catalog family counts do not match the 333-FX specification.")

    for effect in effects:
        if effect.get("render_status") != "SPECIFICATION_ONLY":
            raise ValueError("Generated catalog entries must not claim rendered assets.")
        spin = effect.get("insignia", {})
        if spin.get("rotation_deg_per_frame") != 1.5 or spin.get("render_fps") != 1:
            raise ValueError("Insignia rotation must use the declared slow-spin preview rate.")


def write_catalog(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    catalog = build_catalog()
    path.write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("PROMETHEUS_333_FX_CATALOG.json"),
        help="Output JSON file path.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate the generated catalog without writing a file.",
    )
    args = parser.parse_args(argv)
    try:
        catalog = build_catalog()
        if args.check:
            print(f"Catalog valid: {catalog['fx_total']} unique FX across {len(FAMILIES)} families.")
        else:
            write_catalog(args.output)
            print(f"Wrote {catalog['fx_total']} FX specifications to {args.output}.")
    except (OSError, ValueError) as exc:
        print(f"Catalog generation failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
