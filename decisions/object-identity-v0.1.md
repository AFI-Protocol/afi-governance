# AFI Canonical Object Identity & Identifier Continuity v0.1 (OBJ-GOV)

**Slot:** `AFI-GOV-OBJ-IDENTITY-v0.1` (OBJ-GOV)
**Status:** **Proposed** for owner approval. **This decision authorizes no implementation and no code, schema, package, contract, persistence, API, scoring, or economic change.** It designates canonical object *identities* and *identifier-continuity* rules as protocol-development law; it makes every conforming code change a **separately authorized** implementation act. It becomes authoritative **only** when the owner merges it. Until merged, it is a draft with no force.
**Date:** 2026-07-14
**Type:** Scoped protocol-development governance decision (canonical object identity + identifier continuity). Docs/governance-ledger only.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` (canonical home `afi-config/codex/governance/droids/`), its `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md`, and `decisions/authority-districts-v0.1.md`. Coordinates with (does **not** override) `decisions/uwr-profile-pin-v0.1.md`, `decisions/uwr-runtime-consumption-v0.1.md`, and `decisions/math-authority-v0.1.md`. Where this decision conflicts with the Charter, the Charter wins.
**Evidence basis:** a read-only primary-source pass verified against current `origin/main`, at these pinned commits (working tree == `origin/main`, clean, for every repo at draft time):
- `afi-governance` @ `65997fb` (base; Part E.1 makes object identity a governance matter; Part H reserved these questions)
- `afi-reactor` @ `9b56fb1` · `afi-core` @ `806db49` · `afi-mint` @ `d98a622` · `afi-infra` @ `e136a9c` · `afi-config` @ `ce8c1de`
- `afi-docs` @ `1f3f959` (Districts/API-Atlas audit — **input, not authority**; OBJ-* findings re-verified against current code main and cited by current `path:line`)

**Ledger slot:** Fills the two object-identity items `authority-districts-v0.1.md` Part H expressly reserved to a later decision — "**canonical scored-signal shape**" (`:158`) and "**canonical strategy identifier**" (`:159`) — and the object-identity/identifier-continuity matters Part E.1 classes as governance-required (`:126`). It is the `OBJ-GOV` decision that `district-2-m2-ratification-v0.1.md` §7 (`:141`) named, and it evaluates the District-2 M2 artifacts strictly as **admissible candidate evidence** (`district-2-m2-ratification-v0.1.md:102`), never as canonical by default.

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these):**
1. `signalId` as the canonical **end-to-end join key** (name + id-space discipline).
2. Canonical **Signal** identity (the inbound signal object).
3. **One Strategy identifier** name + value format.
4. **Analyst Score** identity (the score object + its self-identification requirement).
5. Selection of the canonical **Scored Signal representation**.
6. **Versioning, provenance, and identifier continuity** for the object family.

**Does NOT decide (reserved to their own scoped decisions; see §8):** lifecycle / qualification / finality / transition ownership (LIFE-GOV); canonical MongoDB store or write ownership (MONGO-GOV); API Atlas / Gateway authority / replay/read/verify endpoints (ATLAS-GOV); epoch / receipt / reputation / reward / claim / settlement / vault / mint / on-chain semantics (CHAIN-GOV); and **production scoring law** (UWR values, axis registry, weights, risk taxonomy, score ranges — governed by `uwr-profile-pin-v0.1.md` / `uwr-runtime-consumption-v0.1.md` / `math-authority-v0.1.md`).

**Nature of the act.** Per `authority-districts-v0.1.md` Part E.1 (`:126`), object identity and identifier continuity are protocol-development-governance matters. This decision therefore sets them as **tier-1 law** (Part B) — but it authorizes **no** implementation PR. Making the code conform (e.g. normalizing a strategy string, adding an id field to a score) is a **separately authorized** act (owner decision or owner-recorded PR authorization, the `uwr-runtime-consumption-v0.1.md` RC-12 pattern). Shipped code remains tier-4 reality until it conforms; nothing here is retroactively blessed.

---

## 1. The object-identity landscape (evidence, cited)

Verified against current `origin/main`. The identity problem is **fragmentation, not absence**: the same logical objects exist under several names/shapes/formats, and the join key breaks at three seams.

- **`signalId` is one field name over disjoint id-spaces.** Both live ingest adapters write `provenance.signalId` (`afi-reactor/src/uss/ussValidator.ts:40`), but derive it incompatibly: TradingView `{symbol}-{timeframe}-{strategy}-{direction}-{cleanTimestamp}` (`tradingViewMapper.ts:35-45`), **non-deterministic** from wall-clock when not supplied (`:90-93`); CPJ `cpj-{providerType}-{providerId}-{messageId}` (`cpjMapper.ts:136-142`). A separate content hash `ingestHash` is the dedupe key (`ingestDedupeService.ts:63`). `afi-infra` requires `z.string().uuid()` — a **format collision** with the reactor's slug ids (`afi-infra/schemas/signal_scoring_schema.ts:6`).
- **Seven objects wear "Signal."** The convergent **inbound** signal is the **USS / Universal Signal Schema v1.1** (`const "afi.usignal.v1.1"`, `afi-config/schemas/usignal/v1_1/index.schema.json:14`; validated at `afi-reactor/src/uss/ussValidator.ts:36,83-87`) — the shape both adapters normalize into on the live server, and the first to make `provenance.signalId`+`providerId` mandatory. CPJ v0.1 is a pre-USS chat-source adapter; `SignalEnvelope`/`AnalystInputEnvelope v1` are wrappers; `afi-governance`'s `UniversalProposalSignal`/`SignalChallengeProposal` are **governance-proposal** objects (a pure naming collision, `signal_type: "governance_proposal"`).
- **Strategy identity is self-conflicting (OBJ-01).** The same Froggy strategy appears in ≥4 value formats under ≥5 field names: `trend_pullback_v1` (afi-core + governance-pinned), `froggy_trend_pullback_v1` (USS `facts.strategy` example, `provenance.providerRef`, persisted `strategy.name`), `trend-pullback` + `strategyVersion "v1.2.0"` (D2 examples), `froggy-trend-pullback-v1` (folded into `signalId`). One persisted `ReactorScoredSignalDocument` simultaneously holds `pipeline.analystScore.strategyId="trend_pullback_v1"`, `pipeline.analystScore.analystId="froggy"`, `strategy.name="froggy_trend_pullback_v1"`, and `rawUss.facts.strategy="froggy_trend_pullback_v1"` (`afi-reactor/src/types/ReactorScoredSignalV1.ts:151-153,175`; `ussValidator.ts:55`). No JSON-Schema `pattern` constrains any strategy field; the sole hard commitment is `uwr-profile-pin-v0.1.md` UP-10 (`:53,:146`), which pins `strategyId "trend_pullback_v1"` for scorer recognition.
- **The Analyst Score is not self-identifying (OBJ-09).** `afi-core/src/analyst/AnalystScoreTemplate.ts` (the single authored score shape; TS + Zod) has identity `analystId`+`strategyId`+`strategyVersion?` (`:31-38`) but **no `signalId` and no score-object version**; the signal↔score binding lives only in wrappers, and the froggy scorer never copies the enriched input's `signalId` onto the emitted score. There is no canonical JSON-Schema contract for the full template (the D-3 gap).
- **"Scored signal" has multiple candidates (OBJ-02 + DIST-H-08).** The heavy runtime `ReactorScoredSignalV1` / `ReactorScoredSignalDocument` (self-labeled "Canonical output contract", `afi-reactor/src/types/ReactorScoredSignalV1.ts:1-11,75-114,122-187`) is what actually persists; the thin, self-identifying D2 `ScoredSignal v1` projection (`afi.scored-signal.v1`, `src/pipeheads/provenance/types.ts:145-162`) is produced only by the reference harness and never persisted; the `afi-config` M1 draft (`schemas/provenance/v1/scored-signal.schema.json`) is its schema contract; the `afi-infra` `SignalScoringSchema` (`signal_scoring_schema.ts:5-14`, uuid id + 0–100 score) is **orphaned — imported only by a smoke test**; `InternalScoringResult` (`src/pipeheads/types.ts:107-115`) is `@internal`, never emitted.
- **Continuity is meant to run on one key.** In the D2 family, `signalId` is minted once upstream (USS) and threaded verbatim (envelope→ScoredSignal→ProvenanceRecord, "same id space as USS `provenance.signalId`"); the ScoredSignal→ProvenanceRecord link is acyclic via an **id-derived** `provenanceRecordRef` (`builders.ts:151-162`) plus optional `provenanceRecordHash`, and identity carries a two-axis version (per-object schema-id const `afi.<obj>.v1` + a separate `canonicalizationVersion` `afi.hash.vN`).

---

## 2. D-OBJ-1 — `signalId` is the canonical end-to-end join key

**Decision.** `signalId` (as carried in the USS `provenance.signalId` field) is the **single canonical join key** for one signal across ingest → score → scored-signal → provenance. Every object that represents, wraps, scores, or records a signal MUST carry the **same** `signalId` value, threaded **verbatim** from the USS boundary and **never re-derived** downstream. The canonical id-space discipline is: `signalId` is a **stable, opaque string minted once at ingest** and is **not** re-computed from mutable content thereafter. A per-adapter derivation format MAY differ across sources, but each adapter MUST mint a **deterministic** id (no wall-clock entropy) so that re-ingest of the same logical signal is stable; the id, once minted, is immutable for that signal.

**Scope-guard (what D-OBJ-1 does NOT decide).** It does **not** decide the `ingestHash` dedupe scheme (a separate content-address concern), does **not** require or design a MongoDB unique index / persistence key (MONGO-GOV), does **not** define the mint keyspace or `IAnalystScoreFetcher` wiring (CHAIN-GOV / LIFE-GOV), and does **not** by itself authorize changing the shipped TradingView non-deterministic derivation — it *records the requirement* that the id be deterministic and immutable, to be realized under a separate implementation authorization.

---

## 3. D-OBJ-2 — canonical Signal identity = USS v1.1

**Decision.** The canonical **inbound Signal** object is the **Universal Signal Schema v1.1** (`const "afi.usignal.v1.1"`, `afi-config/schemas/usignal/v1_1/`), validated by `afi-reactor/src/uss/ussValidator.ts`. It is the convergence point every source adapter (TradingView, CPJ, future) MUST normalize into; `provenance.signalId` + `provenance.providerId` are its mandatory identity fields. Prior/source shapes are classified, not elevated: **CPJ v0.1** is a pre-USS source adapter (chat only); `SignalEnvelope` / `AnalystInputEnvelope v1` are processing **wrappers** that carry — not redefine — a `signalId`; `afi-governance`'s `UniversalProposalSignal` / `SignalChallengeProposal` are **governance-proposal** objects in a different domain and are **not** market-signal identities (their `signalId`, where present, is a foreign-key reference). USS `v1` (`afi.usignal.v1`) is the superseded predecessor of v1.1.

**Scope-guard.** This designates the inbound-signal **identity shape** only. It does **not** adopt the USS field descriptions' "reward attribution" language as binding (economics = CHAIN-GOV), does **not** fix the `signalId` value **format** here (that discipline is D-OBJ-1, to be kept consistent), and does **not** decide persistence of USS documents (MONGO-GOV).

---

## 4. D-OBJ-3 — one Strategy identifier name + format

**Decision.** The canonical strategy identity is the **orthogonal triple** `analystId` + `strategyId` + `strategyVersion`, carried under exactly those three field names:
- **`strategyId`** — the strategy identifier. Canonical value format: a **bare `snake_case` slug with an embedded major-version token** (illustrative, non-binding shape `^[a-z0-9]+(_[a-z0-9]+)*_v[0-9]+$`), matching the afi-core reference and the only governance-pinned value (`trend_pullback_v1`). It MUST NOT embed the analyst name and MUST NOT be an analyst-prefixed compound (`froggy_trend_pullback_v1` is **non-canonical**).
- **`analystId`** — the analyst, kept **orthogonal** (e.g. `froggy`); never folded into `strategyId`.
- **`strategyVersion`** — optional finer version, **semver without a `v` prefix** (e.g. `1.0.0`, matching the afi-core reference emission), separate from the id; the D2 examples' `v`-prefixed form (`v1.2.0`) is a **non-canonical alias** (and part of the `O-CHOICE-STRAT` bundle). When both are present, the major-version token embedded in `strategyId` MUST equal the major of `strategyVersion`.

All other strategy carriers are **non-canonical aliases** to be derived from / validated against this triple: `strategy`, `strategy.name`, `meta.strategy`, `facts.strategy`, `providerRef` (as a strategy proxy), and the strategy segment folded into `signalId`.

**Why this value format (and the visible alternative).** The bare-`snake_case` form is the **only** choice consistent with merged governance: `uwr-profile-pin-v0.1.md` UP-10 (`:53,:146`) pins `strategyId "trend_pullback_v1"` for scorer recognition; any reformat (e.g. the D2 examples' kebab `trend-pullback` + split `strategyVersion`) would **collide** with that pin. **⚠ OWNER-CHOICE `O-CHOICE-STRAT`:** the owner MAY instead adopt the kebab-case + fully-split-version form (the D2 `ScoredSignal v1` convention) as canonical — but only by **coordinating matching amendments** in the same or paired decisions, because the value cannot silently disagree across domains. Changing it would (i) re-open UP-10's `strategyId "trend_pullback_v1"` pin, (ii) alter the settlement `receiptId = hash(strategyId, epochId)` preimage (CHAIN-GOV), and (iii) change the `NoveltyScorer` `cohortId` key composition (production scoring law) — each a separate coordination/authorization, not effected here (these are the same downstream consumers the D-OBJ-3 scope-guard fences below). This decision proposes the snake_case form as default precisely to avoid re-opening the merged UWR pin and those consumers.

**Scope-guard.** Fixes the identifier **name + format** only. It does **not** decide provider reward-attribution semantics (`providerRef`/`providerId` economics = CHAIN-GOV), does **not** change the afi-core scorer's cohort partitioning or `NoveltyScorer` `cohortId` behavior (production scoring law), does **not** decide the epoch-settlement `receiptId = hash(strategyId, epochId)` encoding (settlement doctrine / CHAIN-GOV), and does **not** decide which service owns/migrates the persisted documents where the conflict is worst (MONGO-GOV).

---

## 5. D-OBJ-4 — Analyst Score identity

**Decision.** The canonical **Analyst Score** object is the afi-core `AnalystScoreTemplate` (`afi-core/src/analyst/AnalystScoreTemplate.ts`). To be a *self-identifying per-signal score* (closing OBJ-09), the canonical Analyst Score identity MUST comprise: the strategy triple `analystId` + `strategyId` + `strategyVersion` (D-OBJ-3); the join key **`signalId`** (D-OBJ-1), which the score MUST carry (not only its wrappers); and a **score-object version** distinguishing the score/template shape from its content. A detached Analyst Score MUST be attributable to its signal and template version without an external wrapper.

**Scope-guard (critical).** This governs the score object's **identity only**. It does **not** change any UWR value, axis, weight, `uwrScore`, `riskBucket` taxonomy, or scoring computation — those are governed by `uwr-profile-pin-v0.1.md` / `uwr-runtime-consumption-v0.1.md` / `math-authority-v0.1.md` and are untouched. Because adding identity bytes (`signalId`, version) to an emitted score feeds District-2 canonical hashing (`outputHash`, `provenanceRecordHash`) and the byte-stable goldens (`uwrScore == 0.1875`), any conforming implementation MUST be scoped so identity fields are added **without** altering canonical serialization law or scoring math — that reconciliation is a **separately authorized** implementation act, not performed here. The divergent `afi-mint` `AnalystScoreInput` is **noted** as a downstream identity re-declaration; any reconciliation to this identity is a **separately authorized** act (§9) that must not touch mint/validator semantics (CHAIN-GOV / LIFE-GOV).

---

## 6. D-OBJ-5 — selection of the canonical Scored Signal representation

**Decision.** The canonical **Scored Signal representation** — the identity/interchange shape of a scored signal — is the **thin `afi.scored-signal.v1` projection** (schema contract: `afi-config/schemas/provenance/v1/scored-signal.schema.json`; reference realization: `afi-reactor/src/pipeheads/provenance/types.ts:145-162`, the authorized non-production reference surface per `district-2-m2-ratification-v0.1.md`). It is selected as canonical because it is purpose-built to be **self-identifying** (carries `signalId` + `analystId` + `strategyId` + optional `strategyVersion`), **provenance-linked** (`provenanceRecordRef`/`provenanceRecordHash`), and **storage-free** (structurally excludes `rawUss`/`lenses`/`_priceFeedMetadata`/volatile timestamps). This is an **active selection on the merits**, not automatic adoption of an M2 artifact.

**Explicit demotions/classifications.** `ReactorScoredSignalV1` / `ReactorScoredSignalDocument` remain **tier-4 runtime carriers** (the objects that actually carry/persist the score in the live pipeline today) — recorded as reality, **not** elevated to the canonical representation and **not** amended here. The `afi-infra` `SignalScoringSchema` is a **non-canonical orphan** (DIST-H-08) — consumed by no production path — and is not part of the object family. `InternalScoringResult` is an internal-only carrier.

**⚠ OWNER-CHOICE `O-CHOICE-SCORED`.** The owner MAY instead designate the heavy `ReactorScoredSignalV1` as the canonical representation (it is what production actually returns/persists today). This decision proposes the thin projection because it is the self-identifying, storage-free identity shape; the alternative is surfaced, not foreclosed.

**Scope-guard (critical).** Selecting the canonical **shape** does **not**: wire it into the production scored seam or replace `ReactorScoredSignalV1` in `server.ts` (that seam-swap is unshipped and **explicitly unratified** — `district-2-m2-ratification-v0.1.md:88,157` — and is LIFE-GOV/production); decide where a canonical scored signal is **persisted** (MONGO-GOV); expose any replay/read/verify **endpoint** (ATLAS-GOV); or resolve the schema's **scoring-law open items** — `riskBucket` taxonomy (SS-O1), `uwrScore` range/normalization (SS-O2), and the org-wide `uwrAxes` axis-name registry (SS-O3), which **remains OPEN under District-2 / UWR authority**; this decision neither closes it nor ratifies any axis set as canonical, and takes **no position** on the recorded gateway axis drift. OBJ-GOV freezes the **field set/identity** of the representation, not those scoring values.

---

## 7. D-OBJ-6 — versioning, provenance, and identifier continuity

**Decision.** The object family adopts a **two-axis versioning** discipline: (a) a per-object **schema-id constant** `afi.<object>.v<major>` (e.g. `afi.usignal.v1.1`, `afi.scored-signal.v1`, `afi.provenance-record.v1`) that versions the object **shape** — a convention adopted on the merits because it is already shared across governed artifacts **beyond** the M2 surface (the USS `afi.usignal.v1.1` designated in D-OBJ-2 and the afi-config M1 schema-id consts), not an M2-exclusive import; and (b) a separate **version-identifier field** (`canonicalizationVersion`, valued `afi.hash.vN`) held **distinct from** the schema-id. OBJ-GOV mandates only the **presence** of this distinct field; the hash/serialization rules it labels remain **District-2 / CHAIN-GOV** hash doctrine and are **not** set here. **Identifier continuity** is: `signalId` minted once at the USS boundary (D-OBJ-1) and threaded verbatim through Signal → Analyst Score → Scored Signal → ProvenanceRecord; the Scored-Signal ↔ ProvenanceRecord binding is by **id-derived reference** (`provenance-record:{signalId}`) plus optional content **hash**, kept acyclic. This fixes the ProvenanceRecord's **versioning / continuity-linkage role only** — it does **not** adopt ProvenanceRecord as the canonical provenance object, nor decide its full shape, its finality writer (LIFE-GOV), or its store (MONGO-GOV). Every object in the family MUST bear its schema-id version; the currently unversioned sub-artifacts (`EvidenceRef`/`SourceDisclosureProfile`/`EnrichmentProvenance`) and the open stage→schema-id registry (PR-O2) are identified as continuity gaps to be closed under implementation authorization.

**Scope-guard.** Defines the versioning + provenance-linkage + continuity **shape** only. It does **not** decide the finality/hash **writer** (LIFE-GOV), the `storageProfileRef` **store** (MONGO-GOV; the field's identity role is kept, its store is not chosen), on-chain digest domains or the `legacyHashRef`→`ingestHash` migration (CHAIN-GOV / District-2 hash doctrine), or any replay **endpoint** (ATLAS-GOV).

---

## 8. Explicit non-decisions

This decision does **not** decide, authorize, ratify, or pre-empt any of the following; each remains for its own scoped decision:

- **LIFE-GOV** — lifecycle states, qualification, finality, transition ownership, the finality writer.
- **MONGO-GOV** — canonical MongoDB store, write ownership, unique-index/persistence-key design, document migration.
- **ATLAS-GOV** — API Atlas / Gateway authority; replay / read / verify endpoints.
- **CHAIN-GOV** — epoch, receipt, reputation, reward, claim, settlement, vault, mint, emissions, on-chain anchoring/commitments.
- **Production scoring law** — UWR values, `uwrAxes` axis names, weights, `riskBucket` taxonomy, `uwrScore` range/normalization, cohort partitioning, decay — all remain governed by `uwr-profile-pin-v0.1.md` / `uwr-runtime-consumption-v0.1.md` / `math-authority-v0.1.md`.
- **District-2 M2 status** — this decision uses the M2 artifacts as admissible candidate evidence and selects one as canonical *shape*; it does **not** alter their non-production status or authorize any production wiring (`district-2-m2-ratification-v0.1.md`).

It amends no prior decision, the Charter, or the Addendum; it creates **no** implementation slot; and it authorizes **no** repository code, schema, package, contract, persistence, API, or economic change.

---

## 9. What still requires a new authorization

Any code change conforming to §§2–7 is a **separately authorized** implementation act (owner decision or owner-recorded PR authorization), not licensed here — in particular: adding `signalId`+version to `AnalystScoreTemplate` **and populating `signalId` at the afi-core scorer emission site**; normalizing the strategy triple across the reactor surfaces; **reconciling the divergent `afi-mint` `AnalystScoreInput` to this identity** (identity only, respecting §8 CHAIN-GOV); making the shipped `signalId` derivation deterministic; producing/persisting the canonical scored-signal projection at any live seam; and versioning the sub-artifacts. Each such slot must also respect the out-of-scope boundaries in §8.

---

## 10. Relationship to existing decisions

- **`authority-districts-v0.1.md`** — unchanged. This decision fills its Part H reserved items "canonical scored-signal shape" (`:158`) and "canonical strategy identifier" (`:159`) and exercises the object-identity authority Part E.1 (`:126`) classes as governance. It respects the 7-tier model: shipped shapes are tier-4 reality; self-labeling "canonical" confers nothing.
- **`district-2-m2-ratification-v0.1.md`** — unchanged. This is the `OBJ-GOV` decision its §7 (`:141`) named; it treats the M2 `ScoredSignal v1` projection as the admissible candidate that §4.3/§7 made available for evaluation, and selects it as the canonical *shape* (§6) **without** changing its non-production status or wiring.
- **`uwr-profile-pin-v0.1.md` / `uwr-runtime-consumption-v0.1.md` / `math-authority-v0.1.md`** — unchanged and **not** overridden. UP-10's `strategyId "trend_pullback_v1"` pin constrains D-OBJ-3 (which coordinates with, never overrides, it); all UWR/scoring values and the afi-math authority remain in force. No scoring law is touched.

---

**Proposed for owner approval. Authoritative only upon owner merge. This decision designates canonical object identities and identifier-continuity rules as protocol-development law; it authorizes no implementation, decides no lifecycle/persistence/API/economic/scoring-law question, and blesses no shipped code — conforming changes remain separately authorized.**
