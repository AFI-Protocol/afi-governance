# CFG-GOV D-CFG-3 "Proof Schema" Scope-Guard Reading v0.1 (CPSR-GOV)

**Slot:** `AFI-GOV-CFG-PROOF-SCHEMA-SCOPE-GUARD-READING-v0.1` (CPSR-GOV)

**Status:** **Accepted** owner decision — accepted by merge of afi-governance PR #44 on 2026-08-06 (merge commit `e04ba9d`, merged unedited).

**Date:** 2026-08-06

**Type:** Scoped **Tier S** clarification record (GPR-GOV D-GPR-2 short form). It fixes the authoritative reading of one accepted clause; it authorizes no schema, score, hash, golden, registry, or deployment act, and decides nothing beyond its single clause.

**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` and `decisions/authority-districts-v0.1.md`. **Consumes (does not re-decide)** CFG-GOV (`analyst-configuration-freedom-v0.1.md`, accepted 2026-08-06, merge `414f2cc`). Where this reading conflicts with CFG-GOV's operative clauses, CFG-GOV wins.

**Relevance (GPR-GOV D-GPR-4):** Outside the building, this removes an ambiguity that could otherwise be used to challenge the provenance record's proof-count law after the fact — the sealed record's meaning stays exactly what the accepted decision says it is.

---

## 0. Scope

**Decides (only this):** the authoritative reading of the words "no proof schema" in the CFG-GOV D-CFG-3 scope-guard (`analyst-configuration-freedom-v0.1.md:74`).

**Does not decide:** any change to any schema, proof law, hash law, scored value, or fixture; any new authorization beyond what CFG-GOV §8 already grants.

## 1. D-CPSR-1 — the reading

**Decision.** CFG-GOV D-CFG-3's scope-guard states the clause "changes no category identity, no proof schema, no hash law, no graph geometry, no join semantics, and no scored value" (`analyst-configuration-freedom-v0.1.md:74`). Meanwhile D-CFG-3(2) (`:69`) mandates that the evidence record carry "exactly as many category proofs as its composition declares lanes … **replacing the fixed count of five**" — which necessarily amends the `providerInvocations` array-cardinality constraint in the evidence **record** schema (`afi-config/schemas/scored-signal-evidence/v3/scored-signal-evidence.schema.json`).

The authoritative reading: **"proof schema" in the D-CFG-3 scope-guard means the individual proof *document* schemas** — `afi-config/schemas/provider-invocation-proof/v1/provider-invocation-proof.schema.json` and `afi-config/schemas/aiml-invocation-proof/v1/aiml-invocation-proof.schema.json` — **which are untouched** (verified: neither file is modified by the CFG-PROOF-SCOPE implementation, afi-config `d789646`). The evidence record's proof-**array cardinality** is not a "proof schema" in that sense; it is exactly the constraint D-CFG-3(2) replaces. There is no conflict between the scope-guard and the clause it guards: the guard protects what a proof *is*; the clause changes how many the record carries.

**Scope-guard.** This is a reading, not a program. It amends nothing, authorizes nothing D-CFG-3 did not already authorize, and cannot be cited to touch either proof document schema, the five-category namespace (FCP-GOV D-FCP-1), or any hash law.

## Explicit non-authorizations

- No change to any governed schema, proof document, hash preimage, golden/KAT byte, or scored value.
- No new implementation slot; CFG-GOV §8 remains the sole authorization surface, with CFG-WEIGHTS and CFG-FIXTURES still inert.
- No self-acceptance; Status remains Proposed until owner merge.

## Supersessions and interactions (touch-scoped, GPR-GOV D-GPR-1)

- **CFG-GOV** (`analyst-configuration-freedom-v0.1.md`) — **consumed and clarified, not amended**: D-CFG-3's operative text and gates stand as written; only the scope-guard's "proof schema" phrase is given its authoritative reading.
- **Every other accepted decision on `decisions/INDEX.md` — untouched.**
