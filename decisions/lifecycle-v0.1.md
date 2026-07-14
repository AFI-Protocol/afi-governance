# AFI Canonical Signal Lifecycle & Finality v0.1 (LIFE-GOV)

**Slot:** `AFI-GOV-LIFECYCLE-v0.1` (LIFE-GOV)
**Status:** **Proposed** for owner approval. **This decision authorizes no implementation and no code, schema, package, contract, persistence, API, scoring, or economic change.** It designates the canonical signal **lifecycle state machine**, the **separation and ownership** of each lifecycle phase, the **finality writer**, the **identifier continuity** rule, and the **pre-persistence handoff** as protocol-development law; it makes every conforming code change a **separately authorized** implementation act. It becomes authoritative **only** when the owner merges it. Until merged, it is a draft with no force.
**Date:** 2026-07-14
**Type:** Scoped protocol-development governance decision (signal lifecycle + finality). Docs/governance-ledger only.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` (canonical home `afi-config/codex/governance/droids/`), its `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md`, and `decisions/authority-districts-v0.1.md`. **Builds on `decisions/object-identity-v0.1.md` (OBJ-GOV):** every lifecycle record uses OBJ-GOV's governed identities. Coordinates with (does **not** override) `decisions/uwr-profile-pin-v0.1.md` / `decisions/uwr-runtime-consumption-v0.1.md` / `decisions/math-authority-v0.1.md`. Where this decision conflicts with the Charter, the Charter wins.
**Evidence basis:** the preserved read-only Districts/API-Atlas audit (`afi-docs/specs/audit/districts-api-atlas/`, findings LIFE-01…10, OBJ-04, OBJ-05, F-PERSIST-01…08 — **input, not authority**), re-verified against current `origin/main` at these pinned commits (working tree == `origin/main`, clean): `afi-governance` @ `4f490a5`, `afi-reactor` @ `9b56fb1`, `afi-mint` @ `d98a622`, `afi-infra` @ `e136a9c`, `afi-core` @ `806db49`, `afi-config` @ `ce8c1de`. Every claim is cited by current `path:line`.
**Ledger slot:** Fills the item `authority-districts-v0.1.md` Part H reserved to a later decision — "**lifecycle states or the finality writer**" (`:160`) — and the lifecycle/finality matters Part E.1 classes as governance-required (`:126`). It consumes the identities governed by `object-identity-v0.1.md` and is the `LIFE-GOV` decision the `object-identity` non-decisions (`:109`) and `district-2-m2-ratification` reserved.

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these):**
1. **One canonical lifecycle state machine** (reconciling today's three incompatible vocabularies).
2. **Clean separation** of seven phases: schema validation · scoring · certification · qualification · challenge · finalization · epoch eligibility.
3. **Ownership of each transition.**
4. **Designation of the finality writer.**
5. **Identifier continuity** using the OBJ-GOV-governed identities.
6. **The handoff required before persistence.**

**Does NOT decide (reserved to their own scoped decisions; see §8):** canonical MongoDB store / write ownership / dedup-index / the two-store reconciliation (MONGO-GOV); API Atlas / Gateway authority / replay/read/verify endpoints (ATLAS-GOV); mint execution, on-chain settlement, epoch **settlement**/receipts, rewards, claims, vault or challenge **economics** (stake/slash/reward), Snapshot voting, on-chain finality (CHAIN-GOV); and **production scoring law** (score computation, decay half-life, the qualifying **threshold value** — governed by `uwr-profile-pin` / `uwr-runtime-consumption` / `math-authority`).

**Nature of the act.** Per `authority-districts-v0.1.md` Part E.1 (`:126`), lifecycle/finality semantics are protocol-development-governance matters. This decision sets them as **tier-1 law** (Part B) but authorizes **no** implementation PR. Making the code conform is a **separately authorized** act (owner decision or owner-recorded PR authorization, the `uwr-runtime-consumption-v0.1.md` RC-12 pattern). Shipped code (the three vocabularies, the unwired gates) remains **tier-4 reality** until it conforms; nothing here is retroactively blessed.

---

## 1. The lifecycle landscape (evidence, cited)

Verified against current `origin/main`. Today the lifecycle is **fragmented, conflated, and partly unwired**:

- **Three incompatible state vocabularies (LIFE-01).** afi-mint `SignalValidatorStateKind` (`afi-mint/src/orchestrator/types.ts:33-42`): `pending → qualified/rejected → challenge_window → contested → dispute_resolved → finalized → minted/rejected_final`. afi-infra `SignalLifecycleStage` (`afi-infra/src/tssd/types.ts:10-16`): `RAW → ENRICHED → ANALYZED → SCORED → MINTED → REPLAYED`. afi-infra `ValidatorStateKind` (`tssd/types.ts:277-283`): `pending → decay_pass → challenge_open → voting_complete → minted → rejected`. The three disagree on names and granularity for overlapping concepts.
- **"Validation" is overloaded (OBJ-04).** Five schema `*ValidationResult` types are conflated with the validator's certification decision (`afi-reactor/src/uss/ussValidator.ts:24`; `afi-reactor/src/types/pipeline.ts:233`; `afi-mint/src/orchestrator/types.ts:47,115`). Schema validation, scoring, certification, and qualification are not cleanly distinguished.
- **The qualification gate is unwired (OBJ-05).** afi-mint's validator makes an **automatic combined** decision — `decayedScore >= minDecayScoreThreshold ? 'qualified' : 'rejected'` (`afi-mint/src/orchestrator/ValidatorDaemon.ts:305-313`) — via `IAnalystScoreFetcher.getAnalystScore(signalId)` (`ValidatorDaemon.ts:50-51`), an interface **with no concrete implementation**; nothing joins a persisted scored signal to the validator.
- **Canonicalization-without-persistence vs persistence-without-canonicalization (LIFE-03).** The reference harness produces the canonical D2 artifacts but never persists (`afi-reactor/src/pipeheads/harness.ts:145-202`); the live path `runFroggyTrendPullback…` persists a heavy `ReactorScoredSignalDocument` (`afi-reactor/src/services/froggyDemoService.ts:5,13,126` "ingest → enrich → score → persist") that is **not** the canonical projection — and the whole live path is `@ts-nocheck` (`froggyDemoService.ts:1`; LIFE-09).
- **No live finality marker; finality only in unwired surfaces (LIFE-08); mint mis-treated as finality (LIFE-07).** The `finalized` concept exists only in the unwired orchestrator/vault types; the live path has no finality stamp, and `MintExecutor` treats mint as terminal finality against a revert-today/stubbed contract.
- **Epoch assignment has zero implemented owner (LIFE-05).** No component owns assigning a signal to an epoch.
- **`VaultedSignalRecord` self-labels "the CANONICAL record of a signal's full lifecycle"** (`afi-infra/src/tssd/types.ts:321,331`) — a tier-4 self-label that confers nothing (authority-districts Part B.1).

---

## 2. D-LIFE-1 — one canonical lifecycle state machine

**Decision.** The canonical signal lifecycle is a **single ordered state machine** with these states (each is the *completed-state* of one phase; every gate has an explicit reject/terminal branch):

`INGESTED → VALIDATED → SCORED → CERTIFIED → QUALIFIED → CHALLENGE_OPEN → [CONTESTED →] FINALIZED → EPOCH_ELIGIBLE`

with terminal/reject branches `SCHEMA_REJECTED` (validation fail), `DECERTIFIED` (certification fail), `UNQUALIFIED` (qualification fail), and `FINAL_REJECTED` (rejected at/after the challenge window). **`EPOCH_ELIGIBLE` is the terminal LIFE-GOV state, and `FINALIZED`/`EPOCH_ELIGIBLE` together form the LIFE-GOV↔CHAIN-GOV boundary.** Everything downstream — mint execution, on-chain settlement, reward/claim — is a **CHAIN-GOV** concern **beyond** this machine's boundary and is **not** a LIFE-GOV state (the shipped `minted`/`MINTED` states are recorded as tier-4 reality to be re-homed under CHAIN-GOV, not adopted here).

The three shipped vocabularies (§1) are **tier-4 reality reconciled to — not adopted as — this canonical machine**: each existing state maps to a canonical state (e.g. afi-infra `decay_pass` and afi-mint `qualified` both collapse the distinct **certification** and **qualification** phases, which this machine separates; afi-mint `finalized` = canonical `FINALIZED`; `challenge_window`/`challenge_open` = `CHALLENGE_OPEN`). No shipped enum is declared canonical by self-label.

**Scope-guard.** This fixes the canonical **state set + ordering + boundary** only. It does **not** set timing/threshold **values** (scoring law / config), does **not** define the mint or settlement states (CHAIN-GOV), and does **not** choose where state is stored (MONGO-GOV).

---

## 3. D-LIFE-2 — clean separation of the seven phases

**Decision.** The seven phases are **distinct**, each answering a different question; none may be conflated with another (directly correcting OBJ-04 and OBJ-05):

1. **Schema validation** — *is the signal structurally valid?* Canonical USS v1.1 (`afi.usignal.v1.1`, OBJ-GOV D-OBJ-2) validation only. Produces `VALIDATED`/`SCHEMA_REJECTED`. **Not** a scoring or eligibility judgment.
2. **Scoring** — *what is the analyst score?* Produces the canonical `afi.scored-signal.v1` projection (OBJ-GOV D-OBJ-5) + Analyst Score identity (D-OBJ-4). Produces `SCORED`. Score **values/law** stay UWR-governed.
3. **Certification** — *is this a legitimate, well-formed scored signal?* An authenticity/correctness attestation (schema-valid input, a **recognized scorer identity** per `uwr-profile-pin` UP-10, canonical projection + ProvenanceRecord present). Produces `CERTIFIED`/`DECERTIFIED`. **Not** an eligibility/threshold judgment.
4. **Qualification** — *does the certified score clear the eligibility bar?* Applies the governed qualifying gate (e.g. decay-score ≥ threshold). Produces `QUALIFIED`/`UNQUALIFIED`. The **threshold value** is scoring-law (UWR); the **phase, its position, and its owner** are LIFE-GOV.
5. **Challenge** — *can the certification/qualification be appealed?* An appeal window (`CHALLENGE_OPEN`), optionally `CONTESTED`. The challenge **process/state** is LIFE-GOV; challenge **economics** (stake/slash/reward, Snapshot voting) are **CHAIN-GOV**.
6. **Finalization** — *is the decision now immutable?* The challenge window closed → the decision is sealed. Produces `FINALIZED`/`FINAL_REJECTED`. Written **only** by the finality writer (D-LIFE-4).
7. **Epoch eligibility** — *which epoch is this finalized signal eligible for?* Assigns the finalized signal to an epoch **as a lifecycle attribute** (`EPOCH_ELIGIBLE`). Epoch **settlement/receipts/emissions** are **CHAIN-GOV**, not decided here.

---

## 4. D-LIFE-3 — ownership of each transition

**Decision.** Each transition has exactly **one** owning authority (designated as a **role**; the concrete component and its wiring are a separate implementation slot — §9). No transition may be performed by more than one authority, and no authority may perform a transition it does not own:

| Transition | Owning authority |
|---|---|
| `INGESTED → VALIDATED` / `SCHEMA_REJECTED` | **Ingest validator** (USS v1.1 validation at the ingest boundary) |
| `VALIDATED → SCORED` | **Scorer** (the afi-core scorer invoked at the scoring seam) |
| `SCORED → CERTIFIED` / `DECERTIFIED` | **Certifier** (correctness/authenticity attestation) |
| `CERTIFIED → QUALIFIED` / `UNQUALIFIED` | **Qualifier** (applies the governed eligibility gate) |
| `QUALIFIED → CHALLENGE_OPEN → [CONTESTED]` | **Challenge authority** (challenge-window + dispute process) |
| `→ FINALIZED` / `FINAL_REJECTED` | **Finality writer** (D-LIFE-4) — **sole** owner |
| `FINALIZED → EPOCH_ELIGIBLE` | **Epoch-eligibility authority** |

The **Certifier** and **Qualifier** are **separate** authorities (today conflated in one automatic ValidatorDaemon decision — `ValidatorDaemon.ts:305-313`). The Epoch-eligibility authority is a **named** owner where none exists today (LIFE-05). This decision designates the roles; it does **not** wire them, nor bless the current owners.

---

## 5. D-LIFE-4 — designation of the finality writer

**Decision.** There is **exactly one finality writer**: the **Finality-writer authority** is the sole component permitted to transition a signal into `FINALIZED`/`FINAL_REJECTED`. It is **distinct** from the scorer, the certifier, the qualifier, the challenge authority, and any mint/settlement component. Finalization is a **lifecycle-finality** event — "the challenge window has closed and the decision is now immutable" — and is **not** on-chain settlement finality: **mint is downstream of finalization, never the finality event itself** (correcting LIFE-07, where `MintExecutor` conflates mint with terminal finality). Once written, the **lifecycle decision** `FINALIZED`/`FINAL_REJECTED` is **immutable as a lifecycle state** (distinct from any storage-layer immutability, which is MONGO-GOV); no phase may re-open a finalized signal except through a governed superseding process (out of scope here).

**Scope-guard.** Designates the finality **role and its exclusivity/immutability** only. It does **not** name a specific existing service as the writer, does **not** decide where the finality marker is stored (MONGO-GOV), and does **not** decide on-chain settlement finality (CHAIN-GOV).

---

## 6. D-LIFE-5 — identifier continuity using the governed identities

**Decision.** Every lifecycle record and state transition, in every surface (reactor state, validator state, any persistence record, epoch record), MUST be keyed on the **single canonical `signalId`** governed by OBJ-GOV D-OBJ-1 (assigned once at ingest, threaded verbatim, immutable), and MUST carry the governed **strategy triple** (`analystId`/`strategyId`/`strategyVersion`, D-OBJ-3) and **Analyst Score identity** (D-OBJ-4), referencing the canonical **`afi.scored-signal.v1`** representation (D-OBJ-5). No lifecycle surface may introduce a divergent id space or re-key by anything other than the governed `signalId`. This closes LIFE-02 (two stores with **no identifier join**) and the mint side's separate `AnalystScoreInput.signalId` re-declaration by mandating the one governed join key end-to-end.

**Scope-guard.** Fixes the **join key + identity carriage** only. It does **not** decide the stores themselves, their indexes, or write ownership (MONGO-GOV).

---

## 7. D-LIFE-6 — the handoff required before canonical scored-signal evidence persistence

**Decision.** A signal MUST NOT be persisted into the **canonical scored-signal evidence store** until the **pre-persistence handoff** is complete:
1. **Schema validation passed** (`VALIDATED`, USS v1.1); and
2. **Scoring produced the canonical artifacts** — the `afi.scored-signal.v1` projection (the canonical representation **selected by the merged OBJ-GOV D-OBJ-5**) **and** its `ProvenanceRecord`, i.e. a **canonicalized, self-identifying** object, not raw runtime baggage (`rawUss`/`lenses`/volatile timestamps) and not an un-canonicalized heavy document; and
3. **Identifier continuity is established** (D-LIFE-5: governed `signalId` + triple + score identity).

The canonical scored-signal evidence store receives the **canonical, self-identifying, certifiable** object; the current live path — which persists a `@ts-nocheck` heavy non-canonical document and **swallows persistence failure** (`afi-reactor/src/services/froggyDemoService.ts:1,330` discards the write status; `server.ts:237` returns 200; LIFE-06, LIFE-03) — is **non-conforming reality** to be corrected under a separate implementation authorization.

**Scope-guard (critical).** This defines the **precondition for entry into the canonical scored-signal evidence store** — the object shape and identity that store must receive — **only**. It governs **only** that evidence store; it does **not** govern or forbid operational storage of **raw ingestion, intermediate/DAG state, retry/dead-letter data, or replay inputs** (all **MONGO-GOV**). It does **not** decide **which** concrete store holds the canonical scored signal, the write/dedup/index mechanism, the two-store reconciliation (**F-PERSIST-01**, a blocker-severity finding), or store immutability/finality — **all of that is MONGO-GOV** (§8). LIFE-GOV defines *what must be true before* canonical scored-signal evidence persistence; MONGO-GOV decides *where and how* it persists.

---

## 8. Explicit non-decisions

This decision does **not** decide, authorize, ratify, or pre-empt any of the following; each remains for its own scoped decision:

- **MONGO-GOV** — canonical MongoDB store; write/dedup/index ownership; the two divergent "canonical" stores reconciliation (**F-PERSIST-01/02**, DIST-H-04, LIFE-02 store-choice, BG-10); store immutability/finality (F-PERSIST-03). *(LIFE-GOV defines only the pre-persistence handoff and the join key — §6, §5.)*
- **ATLAS-GOV** — API Atlas / Gateway authority; replay/read/verify endpoints.
- **CHAIN-GOV** — mint execution, on-chain settlement finality, epoch **settlement**/receipts/emissions, rewards, claims, vault economics, **challenge economics** (stake/slash/reward), Snapshot dispute voting, on-chain anchoring (LIFE-04/05/07/10, CHAIN-03/04, BG-7). The canonical machine **stops at `EPOCH_ELIGIBLE`**.
- **Production scoring law** — score computation, decay half-life, and the qualifying **threshold value** (`minDecayScoreThreshold`) — governed by `uwr-profile-pin` / `uwr-runtime-consumption` / `math-authority`. LIFE-GOV separates the qualification **phase/owner**, not its values.

It amends no prior decision, the Charter, or the Addendum; it creates **no** implementation slot; and it authorizes **no** repository code, schema, package, contract, persistence, API, or economic change.

---

## 9. What still requires a new authorization

Any code change conforming to §§2–7 is a **separately authorized** implementation act (owner decision or owner-recorded PR authorization), not licensed here — in particular: adopting the one canonical state vocabulary across afi-reactor/afi-mint/afi-infra (retiring the three divergent enums); separating the Certifier and Qualifier and wiring the qualification gate (OBJ-05); implementing the `IAnalystScoreFetcher` join by governed `signalId`; naming and wiring the finality writer and the epoch-eligibility owner; enforcing the pre-persistence handoff and removing the `@ts-nocheck` / failure-swallowing live path (LIFE-06/09). Each such slot must also respect the out-of-scope boundaries in §8.

---

## 10. Relationship to existing decisions

- **`authority-districts-v0.1.md`** — unchanged. Fills its Part H reserved item "lifecycle states or the finality writer" (`:160`) and exercises the lifecycle authority Part E.1 (`:126`) classes as governance. Respects the 7-tier model: the three shipped vocabularies and the `VaultedSignalRecord` "CANONICAL" self-label are tier-4 reality, not law.
- **`object-identity-v0.1.md` (OBJ-GOV)** — unchanged and **depended upon**. This decision consumes its governed identities (`signalId` join key, USS v1.1 Signal, strategy triple, Analyst Score identity, `afi.scored-signal.v1` representation) as the identity substrate for every lifecycle record (§5, §7). It does not re-open any OBJ-GOV question.
- **`district-2-m2-ratification-v0.1.md`** — unchanged. The canonical `afi.scored-signal.v1` projection + `ProvenanceRecord` referenced in the pre-persistence handoff are the OBJ-GOV-selected shapes; their non-production status and the unshipped production-wiring remainder are untouched here.
- **`uwr-profile-pin-v0.1.md` / `uwr-runtime-consumption-v0.1.md` / `math-authority-v0.1.md`** — unchanged and **not** overridden. The certification "recognized scorer identity" references UP-10; all scoring values, decay, and the qualifying threshold remain UWR/scoring-governed. No scoring law is touched.

---

**Proposed for owner approval. Authoritative only upon owner merge. This decision designates the canonical signal lifecycle, phase separation and ownership, the finality writer, identifier continuity, and the pre-persistence handoff as protocol-development law; it authorizes no implementation, decides no persistence/API/economic/settlement/scoring-law question, and blesses no shipped code — conforming changes remain separately authorized.**
