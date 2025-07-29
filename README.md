# **AFI Governance – Agentic Financial Intelligence** ⚡

> **Mission:** Scalable, transparent, and intelligent governance for the agentic financial future.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![TypeScript](https://img.shields.io/badge/TypeScript-100%25-blue)
[![arXiv](https://img.shields.io/badge/arXiv-paper--v1-<COLOR>.svg)](https://arxiv.org/abs/XXXX.XXXXX)

---

## 🌐 Overview

AFI Governance is the agentic decision-making layer of the **AFI Protocol**.  
It empowers both **human and agent participants** to submit, evaluate, and validate governance proposals using a hybrid system of **off-chain deliberation** and **on-chain enforcement**.  

The goal is to create **scalable, transparent, and intelligent governance** powered by:

- ✅ **Autonomous Agents**  
- ✅ **Validators & Mentors**  
- ✅ **Multi-chain Interoperability**

---

## ⚡ Deferred Staking Notice

Staking features and vote-weighted governance are **currently deferred**.  
They will activate automatically **after 1,000,000,000 AFI tokens have been minted**:

```typescript
const THRESHOLD = 1_000_000_000; // MIN_SUPPLY_FOR_STAKING
```

- Until then, validators, proposals, and SAFE REALITY execution **operate without staking**  
- This bootstraps governance quickly while allowing the network to grow agent-first  

---

## 🧠 Universal Proposal Signal

All governance proposals (human or agent-generated) follow a **standardized schema** and are routed through **scoring agents** for:

- Clarity  
- Feasibility  
- Risk  
- Alignment with AFI’s mission

The canonical schema is maintained at:

- `schemas/UniversalProposalSignal.schema.json`  
- Mirrors `specs/universal_proposal_schema.json` for **Zenodo lineage**

---

## 📂 Directory Structure

```
afi-governance/
│
├── agents/                   # Proposal executors and governance agents
├── cli/                      # Submit and validate proposals
├── codex/                    # Proposal receipt schemas and metadata
├── config/                   # Staking and governance configs
├── docs/                     # Governance docs and archives
│   └── sprint_archive/       # Historical Sprint README
├── schemas/                  # Universal Proposal Signal schema
├── validator/                # Proposal scoring and validator logic
└── schema_tests/             # Schema validation harness
```

---

## 🏗️ Agent Validator Role

Validators are responsible for:

1. **Scoring** governance proposals using the Universal Proposal Signal schema  
2. **Simulating** proposal impact and validating AOS compatibility  
3. **Contributing** to the AFI Codex memory system for auditability  

This layer is **ready for Factory.ai and Augmentcode** to populate with intelligent agent behaviors.

---

## 📚 Quick Links

- [AFI Governance Docs](./docs)  
- [Universal Proposal Schema](./schemas/UniversalProposalSignal.schema.json)  
- [Zenodo Release (paper-v1)](https://doi.org/xx.xxxx/zenodo.xxxxxxx)  
- [AFI Protocol Organization](https://github.com/AFI-Protocol)

---

## 🤝 Contributing

We welcome contributions from both **developers and agents**:  
- Submit PRs for validators, proposal schemas, and Codex integrations  
- Join the **Agentic AI** revolution by improving the governance layer

---

### ⚡ Agentic Financial Intelligence

> _“Finance that thinks, votes, and evolves with you.”_
