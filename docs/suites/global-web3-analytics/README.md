# Prometheus Global Web3 Liquid Analytics — Supplied Snippet

## Status and execution warning

The supplied Stellar campaign script is not part of the repository and has not been run. Do not copy it into a normal test or startup path: module import creates random Stellar keypairs, performs network-capable setup, generates files, and its bottom-level reward distribution can submit public-network XLM payments. It also starts a Flask server bound to `0.0.0.0`.

## Why it is not production-ready

- The fallback assumes an example XLM price when a rate request fails.
- Campaign amounts and metrics are hard-coded; the data is not a verified market or campaign feed.
- Random in-process wallets are not durable, recoverable, or suitable for custody.
- Reward distribution lacks an approval workflow, reliable idempotency, recipient validation, and a reviewed spending limit.
- The code uses an external price endpoint and public Stellar Horizon endpoint without a documented provider contract or operational safeguards.
- The VR/AR hook is only a print/return stub, and the described dashboard template is not supplied.

## Interoperability boundary

The current repository's **Investor Dashboard**, **Prometheus Sovereign Intelligence**, and **Phantom Wallet System** are catalog labels, not connections to this script. No QuickNode, Stellar, XLM, QR, wallet, or campaign analytics integration is configured in the repository.

Any future implementation must be a separately authorized, testnet-first project with explicit user approvals, externally managed signing authority, rate/data provenance, bounded spend, recipient validation, idempotency, logs without secrets, failure tests, and a production release gate. Never place private keys or API credentials in source or browser assets.
