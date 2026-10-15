# PCI Enterprise QR Package

A local Flask demonstration containing a product metadata endpoint, QR-code generation, an interactive dashboard, and transaction simulation.

## Run locally

Requires Python 3.10 or newer.

```sh
cd PCI_Enterprise_QR_Package
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python backend/app.py
```

Open <http://127.0.0.1:5000>. On Windows, activate the environment with `.venv\Scripts\activate`.

## API

- `GET /api/product_metadata?wallet=Base&product_id=PCI-DEMO-001`
- `GET /api/qr?product_id=PCI-DEMO-001` — SVG QR encodes the `pci-product:` product identifier
- `POST /api/transaction` — validates and returns `simulation_only`; never submits a transaction
- `POST /api/analytics` — validates an event and returns `retained: false`

Supported wallet values name providers only. The app does not connect wallets, store wallet credentials, resolve account names, or communicate with a blockchain. Product metadata is demonstration data. Analytics events are not logged or persisted. Use only local development data; this sample is not hardened for public deployment.

## Package archive

From the repository root, run:

```sh
python PCI_Enterprise_QR_Package/build_zip.py
```

This creates `PCI_Enterprise_QR_Package.zip` in the repository root. The archive excludes caches and local virtual environments.
