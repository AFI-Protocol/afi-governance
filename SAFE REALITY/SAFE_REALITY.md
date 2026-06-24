# 🛡️ Safe Reality Governance Model

> **AFI Settlement v1 note:** Parts of this document reference the **v0** per-signal mint / ERC-1155 receipt / direct-beneficiary path, which is **superseded as mainnet architecture** by AFI Settlement v1 — rewards settle **by epoch** through a RewardsVault / Merkle-claim layer funded from an EpochSettlementManifest, strategy/epoch receipts use **ERC-6909** (not ERC-1155), provenance is separated from payout, and ENS names are aliases (concrete addresses + chainId are the source of truth). See `afi-docs/specs/AFI_SETTLEMENT_V1_DOCTRINE.md` for the canonical architecture.

This document outlines the hybrid governance model used by the AFI Protocol.

## What is Safe Reality?

**Safe Reality** is the integration of:
- 🗳️ Snapshot — for off-chain voting and agent-involved proposal scoring.
- 🔗 Zodiac Reality Module — to enforce off-chain decisions on-chain.
- 🧠 Agent Participation — for scoring, simulation, and proposal auto-generation.
- 🔐 Safe Multisig — for secure execution of governance proposals.

## Key Features

- **UniversalProposalSignal** — Proposals are standardized and scored like AFI signals.
- **Proposal Executors** — Validators or agents act as authorized execution endpoints.
- **Chain-Agnostic Commit Layer** — Using Safe + cross-chain messaging optional broadcast.
- **Enforced Delays & Challenge Windows** — Reality module integration.
