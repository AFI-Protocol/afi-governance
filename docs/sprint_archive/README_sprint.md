
# AFI Governance Layer

> **DEPRECATED / SUPERSEDED:** This document predates AFI Settlement v1 doctrine. It may describe v0 per-signal minting, ERC-1155 receipts, direct beneficiary payouts, stale ENS/Snapshot references, or missing vault architecture. See `afi-docs/specs/AFI_SETTLEMENT_V1_DOCTRINE.md` for canonical architecture.

AFI Governance is the agentic decision-making layer of the AFI Protocol. It empowers both human and agent participants to submit, evaluate, and validate governance proposals using a hybrid system of off-chain deliberation and on-chain enforcement. The goal is to create scalable, transparent, and intelligent governance powered by agents, validators, and multi-chain interoperability.

## Overview

## ⚠️ Deferred Staking Notice

Staking features and vote-weighted governance are **currently deferred**.  
These features will activate **only after 1,000,000,000 AFI tokens have been minted**,  
as defined in `config/config_staking.ts` (`MIN_SUPPLY_FOR_STAKING`).  

Until that threshold is reached:
- Proposal submission, validation, and SAFE REALITY execution **operate without staking**.
- Validators and scoring agents process proposals **freely** to bootstrap governance.


AFI Governance introduces a new standard for proposal creation and validation through its **Universal Proposal Signal Schema**, allowing proposals to be treated like any other signal in the AFI Protocol. This allows them to be:
- Scored by agent validators
- Enriched via DAG-based insight analysis
- Simulated or executed via Safe + Reality module pipelines

## Key Concepts

### 🧠 Proposal as Signal
All governance proposals (human or agent-generated) follow a standardized schema and are routed through scoring agents for analysis. These validators assess clarity, feasibility, risk, and alignment with AFI's mission.

### 📜 Universal Proposal Signal Schema
Located in `schemas/UniversalProposalSignal.schema.json`, this schema defines all the necessary metadata for proposals to be processed as standardized governance signals.

### 🔐 Hybrid Execution (Snapshot + Safe + Reality)
AFI Governance leverages:
- **Snapshot** for gasless off-chain signaling
- **Safe** for treasury control and proposal execution
- **Zodiac Reality module** for enforcement via verified off-chain voting outcomes

This hybrid architecture balances ease of use with secure, enforceable governance workflows.

## Directory Structure

```
afi-governance/
├── README.md
├── schemas/
│   └── UniversalProposalSignal.schema.json
├── validator/
│   ├── proposal_validator.ts
├── safe-reality/
│   ├── governance_contracts/        # Optional modules or stubs (Safe, Reality)
│   └── config/                      # DAO config logic or templates
```

## Agent Validator Role

Agent validators operating in this layer are responsible for:
- Scoring governance proposals using learned models
- Flagging potential risks or conflicts
- Acting as insight producers in the proposal lifecycle

Each agent’s scoring activity is logged and auditable, forming part of the `afi-codex` memory system.

## Future Enhancements

- Replayable DAG of proposal analysis
- Challenge-resolve logic for flagged proposals
- Indexed explorer of historical proposals and validator assessments

## Status

🧱 The scaffolding is complete. Logic for proposal validation and codex integration is underway. This layer is ready for Factory.ai and augmentcode workflows to populate intelligent behavior.

---

Built for composability. Powered by cognition. Guided by insight.
