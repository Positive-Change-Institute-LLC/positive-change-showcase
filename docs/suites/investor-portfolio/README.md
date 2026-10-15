# Local Investor Portfolio Suite

## Components and flow

1. `pci_portfolio_master_builder_v2.py` discovers existing folders under `preexisting_turnkeys/`.
2. With `--build`, it copies supported Python/image/video/audio/PDF files, writes inventory metadata and text narration, and creates `portfolio_index.json`.
3. `pci_investor_suite_portal.py` serves the generated folder on loopback only; `PCI_INVESTOR_SUITE_PORTAL.html` renders that index safely.

The default builder mode is dry-run. Files are not replaced unless `--overwrite` is supplied. The portal is read-only and includes a local content security policy. It does not authenticate users or process payments or transactions.

## Commands

```bash
python pci_portfolio_master_builder_v2.py
python pci_portfolio_master_builder_v2.py --build
python pci_investor_suite_portal.py --portfolio-dir PCI_Python_Portfolio_Full --open
python -m unittest tests.test_portfolio_builder tests.test_investor_portal
```

The input directory is not guaranteed to exist in a fresh checkout. The builder reports this clearly and does not invent product files. The generated narration describes inventoried files only; no TTS provider is called.

## Interoperability

The shared contract is `portfolio_index.json`. A metadata record names a project, optional category, artifact paths, and suggestion basis. The portal treats record text as untrusted display data and creates DOM nodes using text APIs. Catalog products such as **Investor Dashboard** and **Resilience OS Toolkit** are not included unless matching source folders and files actually exist.

This is a local preview, not an investor offering, deployment certificate, or verification of legal status, performance, readiness, or sales.
