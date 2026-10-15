# Prometheus Command Dashboard

## Purpose

`PROMETHEUS_COMMAND_DASHBOARD.html` is a static bilingual English/Spanish prototype. It combines a deterministic in-browser Hydra preview, a local rules-based helper, staged Circle recommendations, and a selector for the 333 FX specification catalog.

## Run locally

Serve the repository root so same-origin catalog loading works:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/PROMETHEUS_COMMAND_DASHBOARD.html`. The FX section reports when it is using the embedded fallback. The Hydra panel is a browser-side preview, not an API client.

## Interoperability and limits

- The dashboard fetches `PROMETHEUS_333_FX_CATALOG.json` from the same site.
- `ppci_sws_proof/hydra.py` is a separate validated API implementation; the dashboard does not call it.
- The helper uses deterministic text rules. It is not a connected AI system.
- Circle material is a proposal. There are no wallet, USDC, payment, or Circle API actions.
- Product names such as **Prometheus Sovereign Intelligence** may be referenced from catalogs, but this page does not provide product checkout.

The Pages workflow publishes the dashboard and catalog separately. Keep both paths in the workflow when changing their names.
