# AFI Canonical Evidence Persistence — Implementation Authorization v0.1 (MONGO-IMPL)

**Slot:** `AFI-GOV-PERSISTENCE-IMPL-v0.1` (MONGO-IMPL)
**Status:** **Proposed** for owner approval. This is a **staged implementation-authorization** decision. **Merging it contains and merges no implementation code**; on owner merge it opens the gate for **Slot 1 only**, and establishes the owner-merge **gate chain** for the remaining wave-1 slots. It becomes authoritative **only** when the owner merges it. Until merged, it authorizes nothing.
**Date:** 2026-07-14
**Type:** Staged implementation-authorization decision (persistence). Docs/governance-ledger only.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md`, its `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md`, and `decisions/authority-districts-v0.1.md`. **Implements the merged `decisions/persistence-v0.1.md` (MONGO-GOV);** it does **not** re-decide it. Consumes `decisions/object-identity-v0.1.md` (OBJ-GOV) and `decisions/lifecycle-v0.1.md` (LIFE-GOV) **exactly**. Uses the staged **RC-12** authorization pattern of `decisions/uwr-runtime-consumption-v0.1.md`. Where this decision conflicts with the Charter, the Charter wins.
**Evidence basis:** the merged MONGO-GOV / LIFE-GOV / OBJ-GOV decisions and the preserved audit (F-PERSIST-01…08, LIFE-02/06, BG-10), all on current `origin/main` (`afi-governance` @ `98a401b`).
**Ledger slot:** Operationalizes `persistence-v0.1.md` (MONGO-GOV) — which authorized no implementation and deferred all conforming work to "separately authorized" slots (its §12). This decision **is** that separate authorization, staged and gated.

---

## 0. Purpose & authorization model

MONGO-GOV designated the canonical scored-signal evidence store, its shape/owner, the single write boundary, idempotency, append/finality, failure behavior, and the store treatment (Option A), but **authorized no code** (`persistence-v0.1.md` §12). This decision authorizes a **bounded, sequenced** set of implementation slots to realize exactly that — and nothing more.

**Authorization model (RC-12, gated).**
- **Owner merge of this decision** authorizes **Slot 1 (`MONGO-CONTRACT`)** to proceed — *and only Slot 1*.
- Each later wave-1 slot is authorized **if and only if** the owner has **merged the prior slot's PR** (its **gate**). No slot's PR may begin before its gate is open. A slot's executing PR is itself owner-reviewed and owner-merged; that merge opens the next gate.
- **Slot 5 (`MONGO-MIGRATION`) is NOT authorized by this decision.** It is deferred behind a **separate future authorization**; it must not begin in wave 1.
- Merging this decision **merges no implementation**; each slot's code lands only in that slot's own gated, owner-merged PR.

**Scope fence (binding).** This authorizes **only** the persistence implementation for the canonical scored-signal evidence store per MONGO-GOV. It authorizes **no** ATLAS-GOV surface (HTTP/API/endpoint/read surface), **no** CHAIN-GOV work (blockchain, mint, rewards, settlement, receipts), **no** production scoring-law change, and **no** unrelated cleanup or refactor. Every slot stays inside its named repo and consumes OBJ-GOV/LIFE-GOV/MONGO-GOV **as written** — no slot may re-decide a governed matter (a scope-ambiguous change is escalated to the owner per `authority-districts-v0.1.md` Part E.3).

---

## 1. Authorized slots (implementation ledger)

Proposed execution order: top to bottom. "Authorized?" states what **this decision** authorizes on its own merge; later slots open per §2.

| Slot | Owner repo | Gate — opens when | Wave-1 authorized? |
|---|---|---|---|
| **`MONGO-CONTRACT`** | `afi-config` | owner merge of **this** decision | **Yes — on merge of this decision** |
| **`MONGO-STORE`** | `afi-infra` | owner merge of the `MONGO-CONTRACT` PR | Yes — when its gate opens |
| **`MONGO-REACTOR-SUBMIT`** | `afi-reactor` | owner merge of the `MONGO-STORE` PR | Yes — when its gate opens |
| **`MONGO-GATEWAY-BOUNDARY`** | `afi-gateway` | owner merge of the `MONGO-REACTOR-SUBMIT` PR | Yes — when its gate opens |
| **`MONGO-MIGRATION`** | `afi-infra` (+ legacy stores) | a **separate future** owner authorization (not this decision) | **No — deferred** |

### Slot 1 — `MONGO-CONTRACT` (afi-config)
- **Define the canonical `afi.scored-signal-evidence.v1` schema** (MONGO-GOV D-MONGO-1/D-MONGO-2 — afi-config-governed contract, building on the District-2 `schemas/provenance/v1/` family).
- **Consume OBJ-GOV and LIFE-GOV exactly** — the governed `signalId` (D-OBJ-1), the `afi.scored-signal.v1` projection (D-OBJ-5), two-axis versioning (D-OBJ-6), identity continuity (LIFE-GOV D-LIFE-5), and the lifecycle/finality semantics (D-LIFE-4/D-LIFE-6). It introduces **no** new object-identity or lifecycle semantics.
- **Include:** `signalId` uniqueness/key requirements (MONGO-GOV D-MONGO-6); the canonical scored-signal projection; **provenance linkage** (`afi.provenance-record.v1` present per D-LIFE-6; its full shape a deferred afi-config schema); schema **version** fields (D-OBJ-6); and the **lifecycle/finality** fields (the LIFE-GOV state + the immutable-after-`FINALIZED` marker per D-MONGO-5).
- **Boundary:** schema/contract only — **no storage engine and no API implementation**.

### Slot 2 — `MONGO-STORE` (afi-infra)
- **Implement the fresh canonical MongoDB evidence store behind one internal persistence interface** (MONGO-GOV D-MONGO-1 fresh store + D-MONGO-7 Option A; D-MONGO-3 sole persistence interface / storage mutation path owned by afi-infra).
- **Enforce unique-`signalId` idempotency** at the store layer (D-MONGO-6 — unique index / insert-if-absent; therefore **not** a time-series collection).
- **Preserve append-once and immutable-after-`FINALIZED`** behavior (D-MONGO-5 — one current record per `signalId`; corrections supersede, never in-place).
- **Provide read-by-`signalId` and minimum replay-data retrieval** (D-MONGO-9 data guarantees).
- **Boundary:** an **internal** interface only — **no external HTTP API** (D-MONGO-9 / ATLAS-GOV).

### Slot 3 — `MONGO-REACTOR-SUBMIT` (afi-reactor)
- **Submit complete governed evidence records through the afi-infra interface** (D-MONGO-3 — reactor is a *submitter, not a writer*).
- **Treat canonical persistence failure as a first-class scoring-run failure — no silent HTTP `200`** (D-MONGO-8; retires the swallow/`@ts-nocheck` path, fixing LIFE-06).
- **Do not retain Reactor's existing collection as canonical** (D-MONGO-7 — `reactor_scored_signals_v1` is demoted/non-canonical; no parallel canonical store).

### Slot 4 — `MONGO-GATEWAY-BOUNDARY` (afi-gateway)
- **Prevent raw/unscored ingestion from entering canonical evidence** (D-MONGO-3 / D-MONGO-4 — raw/unscored MUST NOT enter the canonical store).
- **Gateway may use operational storage** (its `afi_eliza`/operational plane) **and may submit only complete governed evidence records through the same afi-infra interface** (D-MONGO-3).
- **No independent canonical writer** (D-MONGO-3 — submitter, not writer).

### Slot 5 — `MONGO-MIGRATION` (deferred; separately gated)
- Inventory and reconcile **eligible** records from the two legacy stores (`reactor_scored_signals_v1`, `tssd_signals`) into the canonical store (MONGO-GOV D-MONGO-7).
- **NOT authorized here.** It requires a **separate future owner authorization** and must **not** begin or be implemented in the first wave.

---

## 2. Dependencies & owner-merge gates

The gate chain is strictly sequential; each arrow is an **owner merge**:

```
merge(this decision) ─▶ Slot 1 MONGO-CONTRACT
   merge(Slot 1 PR)  ─▶ Slot 2 MONGO-STORE
   merge(Slot 2 PR)  ─▶ Slot 3 MONGO-REACTOR-SUBMIT
   merge(Slot 3 PR)  ─▶ Slot 4 MONGO-GATEWAY-BOUNDARY
   (wave 1 complete) ─▶ [separate future authorization] ─▶ Slot 5 MONGO-MIGRATION
```

- **Data dependencies:** Slot 2 needs the Slot 1 schema; Slots 3 and 4 both consume the Slot 2 interface (they are ordered 3→4 here for a single-writer cutover, so the reactor path proves the interface before the gateway boundary lands). A slot's PR **must not** open before its gate.
- **Each gate is an owner act.** The owner opens a gate by merging the prior slot's PR (or, equivalently, an owner-authored approval recorded on the executing PR no later than merge — the RC-12 form). Absent that, the next slot is **not** authorized.
- **No auto-progression, no skipping, no reordering** without a new governance edit to this ledger.

---

## 3. Requirements binding on every authorized slot

Every wave-1 slot PR MUST:
1. **Consume, not re-decide,** OBJ-GOV / LIFE-GOV / MONGO-GOV — it references the governed clauses and changes none of them.
2. **Stay within its named repo** and within the slot's stated scope; it introduces no second canonical store and no parallel canonical writer.
3. **Cross into no out-of-scope domain** — no ATLAS-GOV (HTTP/API/endpoint/read surface), no CHAIN-GOV (chain/mint/rewards/settlement), no scoring-law change, no unrelated cleanup.
4. **State, in its PR body, which slot it executes and that its gate is open** (the prior owner merge), in the RC-12 form.
5. Be **independently owner-reviewed and owner-merged**; its merge is what opens the next gate.

A change whose slot or scope is unclear **must be escalated to the owner** (`authority-districts-v0.1.md` Part E.3); an implementer may not resolve it by proceeding.

---

## 4. Explicit non-authorizations

This decision does **not** authorize:
- **`MONGO-MIGRATION`** (Slot 5) or any migration/backfill of legacy records — deferred to a separate future authorization (§1, §2).
- **ATLAS-GOV** — any HTTP/API/endpoint, gateway route, replay/read/verify **surface**, or query API over the store.
- **CHAIN-GOV** — blockchain, minting, rewards, claims, settlement, receipts, epoch settlement.
- **Production scoring law** — no change to score values, decay, thresholds, or UWR.
- **Unrelated cleanup/refactor**, and any re-decision of MONGO-GOV / LIFE-GOV / OBJ-GOV.
- **More than one slot at a time** beyond what §2's gate chain has opened; and **no code at all** by the mere merge of this decision.

---

## 5. Relationship to existing decisions

- **`persistence-v0.1.md` (MONGO-GOV)** — unchanged and **implemented** by this staged authorization; every slot maps to its D-MONGO-* clauses. No MONGO-GOV decision is altered.
- **`lifecycle-v0.1.md` (LIFE-GOV)** and **`object-identity-v0.1.md` (OBJ-GOV)** — unchanged and **consumed exactly** (identity, continuity, lifecycle/finality). No OBJ/LIFE question is re-opened.
- **`uwr-runtime-consumption-v0.1.md`** — unchanged; its **RC-12** staged-authorization pattern is the model for the gate chain here.

---

**Proposed for owner approval. Authoritative only upon owner merge. On merge it authorizes only Slot 1 (`MONGO-CONTRACT`) to proceed and establishes the owner-merge gate chain for Slots 2–4; it authorizes no migration (Slot 5), no ATLAS/CHAIN work, and no code by its own merge — each slot lands only in its own gated, owner-merged PR.**
