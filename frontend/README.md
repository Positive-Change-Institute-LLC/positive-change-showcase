# Arcana Product Concept Showcase

## What this page is

`index.html` is a static bilingual English/Spanish browser for three illustrative product concepts: Forge (`FORGE001`), Relics (`RELICS001`), and Ascendants (`ASCEND001`). It filters the fixed sample records and shows motif references and disconnected wallet ecosystem labels.

## Run and validate

Open `index.html` directly or serve the repository root on loopback:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

```text
http://127.0.0.1:8000/frontend/
```

Focused checks:

```bash
python -m unittest tests.test_arcana_showcase
```

## Interoperability and limitations

The page uses its own static product concept list. The names **Forge**, **Relics**, and **Ascendants** are concept examples; they are not claims of issued tokens, purchasable products, or records in the turnkey SQL catalog. It does not connect wallets, generate QR codes, call APIs, authenticate, mint, trade, or retrieve market data.

When a future product catalog adapter is approved, map stable IDs and validated fields explicitly; do not equate these sample IDs with IDs in `PCI_MASTER_TURNKEYS_150_COMPLETE.json` or `TURNKEYS_DATABASE.sql`.

The separately supplied “Arcana Enterprise NFT Dashboard” is not this implementation and must not replace this safe showcase as-is. Its `admin/admin` defaults, client-generated JWT variable, and `/api/login` and `/api/transaction` calls have no matching backend in this repository; the sample does not establish real authentication or minting.

The separate Arcana Enterprise NFT product list is also proposal data. Its hyphenated IDs (`FORGE-001`, `RELICS-001`, `ASCEND-001`) and unverified prices/links are distinct from this page's static IDs and do not add wallet, QR, payment, or NFT behavior.
