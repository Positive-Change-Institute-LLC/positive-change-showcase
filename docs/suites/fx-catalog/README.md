# Prometheus 333 FX Catalog

## Purpose

`prometheus_333_fx_catalog.py` deterministically generates and validates `PROMETHEUS_333_FX_CATALOG.json`. The seven family counts are Pulse 60, Arc 48, Sigil 48, Forge 48, Veil 45, Fracture 42, and Core 42, totaling 333.

## Generate or check

```bash
python prometheus_333_fx_catalog.py --check
python prometheus_333_fx_catalog.py --output /tmp/PROMETHEUS_333_FX_CATALOG.json
python -m unittest tests.test_prometheus_333_fx_catalog
```

Use the committed catalog as the dashboard input. Regenerate the checked-in JSON only when the specification changes intentionally; review the diff and uniqueness/count validation before merging.

## Interoperability

The browser dashboard reads the JSON from its own origin and falls back to a family preview when the JSON is unavailable. Each catalog entry is `SPECIFICATION_ONLY`; this does not create rendered FX, NFT assets, animation files, or deployed capabilities. The FX catalog is independent of product entries such as **Chrono Relics** and **Investor Dashboard** unless an explicit integration is implemented and tested.

## Supplied deployment and render declarations

The supplied `PROMETHEUS_333_FX_TURNKEY` and `PROMETHEUS_333_RENDER_TURNKEY` blocks match the checked-in family counts, doctrine labels, palettes, camera values, and render-specification fields. They do not change implementation status: the catalog says `CATALOG_GENERATED_RENDER_ASSETS_NOT_DEPLOYED`, and its effects remain `SPECIFICATION_ONLY`. `DEPLOYED`, `ACTIVE`, and `ready_for` claims are not verified by those metadata declarations. No renderer or rendered assets are included.

The catalog validates unique effect IDs, names, and `motif_id` values, but the motif-form names themselves are drawn from a repeating list. Therefore the metadata label `motif_reuse: ZERO` does not currently mean that every motif form is unique. Likewise, `CANON_LOCKED`, `ZERO` drift, and `Render_Ready_Specification` are declared metadata, not cryptographic immutability, measured drift guarantees, or proof of a render pipeline.

## Data and IP caution

The catalog records authored metadata and a stated copyright notice. Trademark and patent status is not independently verified by the generator. Do not convert that metadata into legal advice or deployment claims.
