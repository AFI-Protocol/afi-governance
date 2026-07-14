# AFI Canonical Scored-Signal Evidence Persistence v0.1 (MONGO-GOV)

**Slot:** `AFI-GOV-PERSISTENCE-v0.1` (MONGO-GOV)
**Status:** **Proposed** for owner approval. **This decision authorizes no implementation and no code, schema, package, contract, persistence, API, scoring, or economic change.** It designates the **canonical scored-signal evidence store**, its **persisted shape and contract owner**, the **write-ownership boundary**, the **operational-vs-canonical** separation, the **append/mutation/retention/finality** expectations, the **idempotency/dedup** rule, the **treatment of the two existing stores**, the **persistence-failure** behavior, and the **minimum replay/read** guarantees as protocol-development law; it makes every conforming code change a **separately authorized** implementation act. It becomes authoritative **only** when the owner merges it. Until merged, it is a draft with no force.
**Date:** 2026-07-14
**Type:** Scoped protocol-development governance decision (canonical persistence / evidence store). Docs/governance-ledger only.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` (canonical home `afi-config/codex/governance/droids/`), its `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md`, and `decisions/authority-districts-v0.1.md`. **Builds on `decisions/object-identity-v0.1.md` (OBJ-GOV) and `decisions/lifecycle-v0.1.md` (LIFE-GOV):** it decides *where and how* the object LIFE-GOV hands off is persisted. Coordinates with (does **not** override) `uwr-profile-pin` / `uwr-runtime-consumption` / `math-authority`. Where this decision conflicts with the Charter, the Charter wins.
**Evidence basis:** the preserved read-only Districts/API-Atlas audit (`afi-docs/specs/audit/districts-api-atlas/`, findings F-PERSIST-01…08, DIST-H-04, BG-10, LIFE-02, LIFE-06 — **input, not authority**), re-verified against current `origin/main` at these pinned commits (working tree == `origin/main`, clean): `afi-governance` @ `a9fc673`, `afi-reactor` @ `9b56fb1`, `afi-infra` @ `e136a9c`, `afi-gateway` @ `262fa30`, `afi-config` @ `ce8c1de`, `afi-docs` @ `1f3f959`. Every claim is cited by current `path:line`.
**Ledger slot:** Fills the item `authority-districts-v0.1.md` Part H reserved to a later decision — "**canonical MongoDB store**" (`:161`) — and the "**canonical persistence owner**" Part E.1 classes as governance (`:126`). It **evaluates and supersedes** the ungoverned `afi-docs/specs/audit/AFI_EVIDENCE_STORE_DECISION.md` ("Status: DECIDED" but never governed — F-PERSIST-02; tier-6 documentation, not law).

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these nine):**
1. the **single canonical scored-signal evidence store** and its **canonical persisted shape**;
2. **which repository owns** that store and its **contract**;
3. the **Gateway/Reactor write-ownership boundary**;
4. how **operational stores** differ from **canonical evidence persistence**;
5. **append-only / mutation / retention / finality** expectations for the canonical record;
6. **idempotency and deduplication** requirements using `signalId`;
7. **treatment or migration status** of the two existing MongoDB stores;
8. **behavior when scoring succeeds but canonical persistence fails**;
9. the **minimum replay/read guarantees** for the canonical evidence record.

**Does NOT decide (reserved to their own scoped decisions; see §11):** API Atlas / Gateway authority / replay-read-verify **endpoints** (ATLAS-GOV); blockchain / mint / rewards / claims / on-chain settlement / receipts / **settlement finality** (CHAIN-GOV); production **scoring law**; and **unrelated Gateway hygiene** (the gateway's operational `afi_eliza` chat/session/health store).

**Nature of the act.** Per `authority-districts-v0.1.md` Part E.1 (`:126`), the canonical persistence owner is a protocol-development-governance matter, and Part C records that `afi-infra` "holds **no** unilateral canonical-object or finality authority … Which persisted store/shape is canonical is **not** decided here" (`:79`) — this decision is where it is decided. It sets these as **tier-1 law** (Part B) but authorizes **no** implementation PR. Making the code conform (migration, index creation, reshaping, failure handling) is a **separately authorized** act (the `uwr-runtime-consumption-v0.1.md` RC-12 pattern). Shipped stores remain **tier-4 reality** until they conform; self-labels like `VaultedSignalRecord`'s "CANONICAL" confer nothing (Part B.1).

---

## 1. The persistence landscape (evidence, cited)

Verified against current `origin/main`. Two divergent Mongo stores each carry "canonical" intent; neither is governed, and neither can satisfy the requirements below as-is:

- **Store A — afi-reactor** `afi_reactor.reactor_scored_signals_v1` (`afi-reactor/src/services/tssdVaultService.ts:56-59`): persists the **heavy** `ReactorScoredSignalDocument` (`ReactorScoredSignalV1.ts:122-187` — carries `rawUss`/`lenses`/`_priceFeedMetadata`/`rawPayload` baggage) via `insertOne` — a **non-idempotent append, no unique index, no durable dedup** (`tssdVaultService.ts:112`; F-PERSIST-04); on failure it returns `"failed"` (`:120`), which the caller swallows into a `200` (LIFE-06). Header: "**ISOLATION** … Reactor-owned collections, **isolated from afi-infra TSSD vault**" (`:6`).
- **Store B — afi-infra** `afi_tssd.tssd_signals` (`afi-infra/src/tssd/MongoTSSDVaultClient.ts:2,232`): a MongoDB **time-series** collection (timeField `createdAt`) holding `VaultedSignalRecord`, self-labeled "**The CANONICAL record of a signal's full lifecycle … single source of truth**" (`afi-infra/src/tssd/types.ts:321,323,331`). Its `upsert` is a **non-atomic** `findOne` + `deleteOne` + `insertOne` (`MongoTSSDVaultClient.ts:120-160`; F-PERSIST-05), and — decisively — a **unique index on `identity.signalId` is not supported on a time-series collection, so the code falls back to a non-unique index** (`:241-252`; BG-10). Written by **afi-gateway** (multi-tenant) via `vaultFactory` (`afi-gateway/src/http/app.ts:133-134`, importing `afi-infra` `VaultedSignalRecord` at `:8`).
- **The "canonical" claim is ungoverned.** `afi-docs/specs/audit/AFI_EVIDENCE_STORE_DECISION.md` (tier-6) states "MongoDB TSSD is the canonical reference evidence store" and names the **two-store spine** (reactor→`afi_reactor.reactor_scored_signals_v1`; gateway→`afi_tssd.tssd_signals`) — but afi-governance has **zero** persistence decisions (F-PERSIST-02). Two documents "canonical," no join key, and neither reachable by the mint (F-PERSIST-01 **blocker**, F-PERSIST-06, DIST-H-04, LIFE-02).
- **The gateway's own store is operational, not evidence.** `afi-gateway/src/lib/db/mongo.ts` is "for gateway-specific data **ONLY** … chat/session history … demo/dev … **NOT for TSSD vault data**" (`afi_eliza`). It is a different plane.

---

## 2. D-MONGO-1 — the single canonical scored-signal evidence store & its persisted shape

**Decision.** There is **exactly one** canonical scored-signal evidence store: **`afi.scored-signal-evidence` (v1)** — the store LIFE-GOV D-LIFE-6 hands off into. Its **canonical persisted record** is a **self-identifying evidence record keyed by the governed `signalId`** (OBJ-GOV D-OBJ-1) that carries the canonical **`afi.scored-signal.v1`** projection (**OBJ-GOV D-OBJ-5**) **and** its provenance record (`afi.provenance-record.v1`, required *present* by **LIFE-GOV D-LIFE-6**'s handoff; its full shape is a **deferred afi-config schema**, not fixed by OBJ-GOV) — and **excludes** runtime/storage baggage (`rawUss`/`lenses`/`_priceFeedMetadata`/`rawPayload`/volatile timestamps). It is **not** the heavy `ReactorScoredSignalDocument`, and **not** the full `VaultedSignalRecord` lifecycle "brain" (whose `validator`/`minted`/`replayed` stages and `training`/`proprietary` views are LIFE-GOV / CHAIN-GOV / out-of-scope concerns, not canonical scored-signal evidence). The exact JSON contract is an **afi-config-governed schema** (see D-MONGO-2), specified under a separate implementation authorization; this decision fixes its **identity, composition, and constraints**, not its byte-level fields.

**Scope-guard.** Fixes the **canonical evidence store and record composition** only. It does **not** re-decide the scored-signal representation (that is OBJ-GOV D-OBJ-5, consumed here), does **not** define the on-chain receipt (CHAIN-GOV), and does **not** define read/verify **endpoints** (ATLAS-GOV).

---

## 3. D-MONGO-2 — repository ownership of the store and its contract

**Decision.** Ownership is **split by layer**, consistent with `authority-districts-v0.1.md` Part C:
- The **canonical persisted-record schema contract** (`afi.scored-signal-evidence.v1`) is a **governed `afi-config` schema** (Part C makes `afi-config` the canonical schema/registry home **where expressly delegated** (`:73`); this decision so delegates), building on the existing District-2 `afi-config/schemas/provenance/v1/` family.
- The **store implementation** (connection, collection, indexes, write client) is **owned by `afi-infra`** (Part C: `afi-infra` is the infrastructure/persistence implementation repo). `afi-infra` holds **no** authority to change the canonical shape or finality — those live in the contract and in LIFE-GOV.
- **`afi-reactor` does not own a canonical evidence store.** Its `reactor_scored_signals_v1` isolated collection is demoted (§8).

**Scope-guard.** Designates the **contract-vs-implementation owners** only; it does **not** grant `afi-infra` object-identity, lifecycle-finality, or economic authority (those remain OBJ-GOV / LIFE-GOV / CHAIN-GOV).

---

## 4. D-MONGO-3 — the Gateway/Reactor write-ownership boundary

**Decision.** Both **afi-reactor** (single-tenant ingest spine) and **afi-gateway** (multi-tenant ingest) are **writers** into the *one* canonical evidence store, and both MUST write **the same canonical record shape** (D-MONGO-1) **through the afi-infra-owned store contract** (D-MONGO-2). Neither may own or write a **parallel, isolated, differently-shaped canonical store** (ending today's split: reactor→heavy `reactor_scored_signals_v1`; gateway→time-series `tssd_signals`). Tenant-scoping is a **feature of the one store** (the existing `TenantScopedTSSDVaultClient` pattern), not a second canonical store. The **gateway's operational `afi_eliza` store** (chat/session/health) is **not** an evidence writer and is untouched (§5).

**Scope-guard.** Fixes **who may write the canonical evidence record and through what contract** only; it does **not** decide request/API surfaces or gateway auth (ATLAS-GOV), nor any gateway operational-store hygiene.

---

## 5. D-MONGO-4 — operational stores vs canonical evidence persistence

**Decision.** The **canonical evidence store** holds **only** the canonical scored-signal evidence record, admitted **only** after the LIFE-GOV pre-persistence handoff (`decisions/lifecycle-v0.1.md` D-LIFE-6). **Operational stores are distinct and are NOT governed as canonical evidence** — including raw-ingestion buffers, intermediate/DAG state, retry/dead-letter queues, replay **input** fixtures, ingest-dedupe caches, time-series **telemetry**, and the gateway's `afi_eliza` chat/session/health store. Operational stores MAY be append, mutable, ephemeral, or time-series as their function requires; they carry **no** canonical-evidence status and are outside this decision's finality/immutability/idempotency rules (their policy is ordinary implementation, not governance).

**Scope-guard.** Draws the **evidence-vs-operational boundary** only; it does **not** dictate operational-store schemas, retention, or engines (those are implementation).

---

## 6. D-MONGO-5 — append-only, mutation, retention, finality

**Decision.** The canonical evidence record is **write-once / append-only per `signalId`**: once written it is **not mutated in place**. The store holds **exactly one *current* canonical record per `signalId`** (this single-current-record invariant is the basis of the D-MONGO-6 uniqueness/idempotency rule); a governed correction **supersedes** the current record with a **new schema-versioned** record (schema-id/version per OBJ-GOV D-OBJ-6), and the superseded version is **retained immutably as history** — versioning is by **supersession**, never by an in-place edit nor by relaxing the one-current-record-per-`signalId` invariant. Once its signal reaches the LIFE-GOV **`FINALIZED`** state (`decisions/lifecycle-v0.1.md` D-LIFE-4), its canonical evidence record is **immutable** — resolving the "unimplemented, self-contradictory finality" of F-PERSIST-03. Pre-finalization status updates (lifecycle state advancing) are expressed as governed transitions (LIFE-GOV), not as destructive rewrites of the evidence record. **Retention:** the canonical evidence record is retained **durably** as the evidence plane. This is **storage-layer** immutability/custody **only** — per BG-10 it MUST NOT be conflated with **settlement finality**, which is CHAIN-GOV.

**Scope-guard.** Sets **storage immutability/append/retention** only; it does **not** set on-chain settlement finality, receipts, or emissions (CHAIN-GOV), nor lifecycle-state semantics (LIFE-GOV, consumed here).

---

## 7. D-MONGO-6 — idempotency & deduplication by `signalId`

**Decision.** Writes to the canonical evidence store MUST be **idempotent, keyed by the governed `signalId`** (OBJ-GOV D-OBJ-1): the store MUST enforce **`signalId` uniqueness at the store layer** (a **unique index** / insert-if-absent semantics) on the **single current canonical record per `signalId`** (D-MONGO-5 — governed corrections supersede, they do not duplicate), so re-ingesting the same `signalId` **cannot** create a duplicate canonical record. Because a MongoDB **time-series** collection **cannot enforce a unique index** (`MongoTSSDVaultClient.ts:241-252`; BG-10), the canonical evidence store **MUST be a store type that supports a unique `signalId` constraint** (i.e. a standard collection) — the current time-series `tssd_signals` form **cannot** be the canonical evidence store as-is. Store-layer uniqueness is **required**; in-memory app-level dedup (the non-durable `ingestDedupeService`, F-PERSIST-04) is **not** sufficient.

**Scope-guard.** Fixes the **idempotency key and store-layer uniqueness requirement** only; it does **not** mandate a specific index/driver API or dedup implementation (that is a conforming implementation act — §12).

---

## 8. D-MONGO-7 — treatment/migration of the two existing stores (⚠ owner choice)

**Decision.** Neither existing store is canonical as-is. Both are recorded as **tier-4 reality** to be reconciled to the canonical store (D-MONGO-1): afi-reactor's `reactor_scored_signals_v1` (heavy, non-idempotent) and afi-infra's `tssd_signals` (time-series, no unique index) are **non-conforming**. The concrete reconciliation is an owner choice, surfaced — **not** silently decided:

**⚠ OWNER-CHOICE `O-CHOICE-STORE`.**
- **(A) — DEFAULT (recommended):** Stand up the canonical evidence store as a **new, standard (non-time-series), unique-`signalId`-indexed** collection under the afi-config contract + afi-infra implementation; **migrate** conforming historical records from both existing stores into it; then **demote** `reactor_scored_signals_v1` (retire) and **repurpose** `tssd_signals` as an **operational time-series telemetry** store (§5) — never as canonical evidence. *(Cleanest: satisfies §6/§7 and aligns with OBJ-GOV shapes.)*
- **(B):** **Promote afi-infra `tssd_signals` to canonical** by **converting it from a time-series to a standard collection** (to gain the unique `signalId` index) and reshaping to the canonical record; retire the reactor collection.
- **(C):** **Promote afi-reactor `reactor_scored_signals_v1` to canonical** by reshaping it to the canonical record + adding the unique index; retire the afi-infra store as canonical.

This decision proposes **(A)**; it makes none of (A)/(B)/(C) a fait accompli. Whichever is chosen, the canonical store MUST satisfy §2/§6/§7, and the migration itself is a **separately authorized** implementation act (§12).

**Scope-guard.** Decides the **status (non-canonical) + reconciliation options** only; the migration code/DDL is not authorized here.

---

## 9. D-MONGO-8 — behavior when scoring succeeds but canonical persistence fails

**Decision.** A scoring success followed by a **canonical-persistence failure MUST NOT be reported as success** and MUST NOT silently advance the signal's lifecycle. The signal does **not** attain its post-persistence lifecycle status; the failure is **surfaced and durable** — routed to a retry/dead-letter **operational** path (§5) for re-attempt — never swallowed. This overrides the current live behavior, which discards the vault write status and returns `200` (`afi-reactor/src/services/froggyDemoService.ts:330`; `server.ts:237`; LIFE-06). The precise transport (status code, retry policy) is implementation; the **governed expectation** is: canonical persistence is a **required, acknowledged** step, and its failure is a **first-class failure**, not a masked success.

**Scope-guard.** Sets the **success/failure contract** only; it does **not** specify the HTTP code, retry cadence, or dead-letter schema (implementation), nor any API surface (ATLAS-GOV).

---

## 10. D-MONGO-9 — minimum replay/read guarantees for the canonical evidence record

**Decision.** The canonical evidence record MUST provide, at minimum: **(a) read-by-`signalId`** — a record is retrievable by its governed `signalId` (the `getBySignalId` access already exists, `MongoTSSDVaultClient.ts:163-167`); and **(b) replay/verify sufficiency** — the stored record contains everything needed to **deterministically replay/verify** the scored signal off-line: the `afi.scored-signal.v1` projection plus its `afi.provenance-record.v1` (input/enrichment/output CanonicalHash digests) and the District-2 replay pins, so a recompute can be checked against the stored digests without external state. These are **data guarantees on the record**, not endpoints.

**Scope-guard (critical).** Defines **what the record must contain and that it is readable by `signalId`** only. It does **not** define, expose, or authorize any **replay/read/verify API endpoint, gateway route, or query surface** — **all of that is ATLAS-GOV** (§11).

---

## 11. Explicit non-decisions

This decision does **not** decide, authorize, ratify, or pre-empt any of the following; each remains for its own scoped decision:

- **ATLAS-GOV** — API Atlas / Gateway authority; replay/read/verify **endpoints**, routes, or query surfaces over the evidence store.
- **CHAIN-GOV** — mint, rewards, claims, on-chain settlement, receipts, epoch settlement/emissions, and **settlement finality** (which storage custody MUST NOT be conflated with — BG-10).
- **Production scoring law** — score computation, decay, thresholds, UWR values (governed by `uwr-profile-pin` / `uwr-runtime-consumption` / `math-authority`).
- **Unrelated Gateway hygiene** — the gateway's operational `afi_eliza` chat/session/health store, and gateway auth/transport, are out of scope (noted as operational only, §4–§5).

It amends no prior decision, the Charter, or the Addendum; it creates **no** implementation slot; and it authorizes **no** repository code, schema, package, contract, persistence, API, or economic change.

---

## 12. What still requires a new authorization

Any code change conforming to §§2–10 is a **separately authorized** implementation act (owner decision or owner-recorded PR authorization), not licensed here — in particular: authoring the `afi.scored-signal-evidence.v1` afi-config schema; standing up / migrating the canonical store per the chosen `O-CHOICE-STORE` option; creating the unique `signalId` index and idempotent write path; converging the reactor + gateway writers onto the one contract; enforcing the pre-persistence handoff and first-class persistence-failure handling (retiring the `@ts-nocheck`/swallow path); and un-jest-ignoring the persistence tests (F-PERSIST-07). Each such slot must also respect the out-of-scope boundaries in §11.

---

## 13. Relationship to existing decisions

- **`authority-districts-v0.1.md`** — unchanged. Fills its Part H reserved item "canonical MongoDB store" (`:161`), exercises the Part E.1 "canonical persistence owner" authority (`:126`), and resolves the question Part C (`:79`) explicitly deferred. Respects the 7-tier model: the two stores and the `VaultedSignalRecord` "CANONICAL" self-label are tier-4 reality; the ungoverned `AFI_EVIDENCE_STORE_DECISION.md` is tier-6 documentation, evaluated and **superseded** here.
- **`lifecycle-v0.1.md` (LIFE-GOV)** — unchanged and **depended upon**. This decides *where/how* the LIFE-GOV D-LIFE-6 handoff persists and gives the D-LIFE-4 finality its storage-layer expression (immutability-after-`FINALIZED`); it consumes, and does not re-open, the lifecycle machine.
- **`object-identity-v0.1.md` (OBJ-GOV)** — unchanged and **depended upon**. The canonical persisted record is built on the governed `signalId` (D-OBJ-1) and the `afi.scored-signal.v1` + `afi.provenance-record.v1` shapes (D-OBJ-5); no OBJ-GOV question is re-opened.
- **`uwr-profile-pin` / `uwr-runtime-consumption` / `math-authority`** — unchanged and **not** overridden. No scoring value or law is touched.

---

**Proposed for owner approval. Authoritative only upon owner merge. This decision designates the canonical scored-signal evidence store, its shape/owner/contract, the write boundary, the operational separation, the append/mutation/retention/finality and idempotency rules, the treatment of the two existing stores, the persistence-failure contract, and the minimum replay/read guarantees as protocol-development law; it authorizes no implementation, decides no API/chain/settlement/scoring-law question, and blesses no shipped store — conforming changes remain separately authorized.**
