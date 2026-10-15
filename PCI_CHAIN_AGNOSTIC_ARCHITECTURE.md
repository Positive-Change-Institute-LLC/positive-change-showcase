# PCI Chain-Agnostic Architecture

## Purpose

PCI's chain-agnostic direction is to keep business intent, identity policy, and risk rules separate from network-specific transaction behavior. A shared orchestration layer should select a compatible network adapter rather than assume that every chain has the same account model, transaction format, finality, asset standard, or smart-contract capabilities.

> **Status:** This document describes an architectural direction, not a claim of production multi-chain support. The current APIs in this repository use deterministic sample inputs and do not connect to live chains, wallets, bridges, exchanges, or market feeds. See the [implemented API contract](./PCI_API_ECOSYSTEM_SPECIFICATION.md).

## Ecosystems in scope

The architecture is intended to evaluate networks individually, including:

- **XRP Ledger (XRPL):** XRP payments and ledger-specific transaction and account behavior.
- **EVM networks:** Ethereum and compatible networks, subject to network-specific configuration.
- **Solana:** Solana accounts, programs, transaction handling, and finality characteristics.
- **Other networks:** additional chains only after their capabilities, risks, and operational requirements are reviewed.

Listing an ecosystem means it is in scope for design consideration; it does not mean an adapter, deployment, or production integration exists.

## Adapter-oriented design

A future implementation should define explicit network adapters behind a shared orchestration interface. Each adapter would be responsible for:

1. Declaring supported operations and assets.
2. Validating network identifiers, addresses, amounts, and transaction parameters.
3. Building and submitting transactions through a configured provider.
4. Reporting confirmation and finality according to that network's semantics.
5. Returning normalized results while preserving the original network response for audit.
6. Failing closed when an operation, asset, provider, or network is unsupported.

The shared layer should not hide material differences between networks. Route selection must consider user authorization, asset availability, transaction costs, expected finality, provider health, and operational policy. Cross-chain movement must use an explicitly selected and reviewed mechanism; it must not be inferred from a shared interface.

## XRP Ledger considerations

XRPL is a first-class design target, not an EVM alias. Any XRPL adapter would need XRPL-specific address and transaction validation, account sequence and reserve handling where applicable, signing boundaries, and confirmation rules. XRP and issued assets on XRPL are distinct assets with distinct trust, liquidity, and custody considerations.

No private keys, seed phrases, or signing secrets belong in this repository or in application logs. A production design should keep signing under explicit user or approved custody control and separate transaction construction from authorization and signing.

## Circle and USDC relationship

Circle-related workflows should be treated as optional integrations that can be enabled only for the specific product, network, and asset combinations that are actually supported and validated. Chain-agnostic design does not imply that USDC is available on every network, that Circle issues or supports an asset on XRPL, or that Circle provides a bridge between any particular chains. Verify current issuer and network documentation before implementing or advertising a route.

Where an asset or Circle service is not supported on a selected network, the system should reject the requested route or present a clearly disclosed alternative requiring explicit approval. It must not silently substitute a token, bridge, or network.

## Validation and rollout gates

Before calling any chain integration active, document and test:

- The exact network, provider, asset, and operations supported.
- Address, amount, and transaction validation, including malformed and boundary inputs.
- Signing authority, key custody assumptions, and secret handling.
- Confirmation, reorganization, timeout, retry, and duplicate-submission behavior.
- Failure handling, monitoring, and a way to stop or limit submissions.
- Testnet results and an independently reviewed production rollout plan.

Until these gates are met, describe the work as design or prototype scope rather than deployed chain support.

© 2026 Positive Change Institute LLC
