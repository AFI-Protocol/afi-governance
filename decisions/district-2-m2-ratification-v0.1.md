# AFI District 2 — Prospective Bounded Ratification of the Shipped "M2" D2-Native Artifact Surface v0.1

**Slot:** `AFI-GOV-DISTRICT-2-M2-RATIFY-v0.1`
**Status:** **Accepted** owner decision — accepted by merge of afi-governance PR #15 on 2026-07-14 (merge commit `65997fb`, merged unedited; acceptance recorded under DSC-GOV D-DSC-8). **This decision authorizes no new implementation and no code, schema, package, contract, persistence, API, scoring, or economic change.** It ratifies — *prospectively and within an exactly enumerated, commit-pinned, non-production scope* — a surface that **already exists**; it writes no bytes in any implementation repository. It became authoritative on that owner merge.
**Date:** 2026-07-14
**Type:** Scoped District-2 ratification decision (protocol-development governance). Docs/governance-ledger only. **Resolves the open owner choice `D-CHOICE-1`** recorded in `decisions/authority-districts-v0.1.md` §D.1.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` (canonical home `afi-config/codex/governance/droids/`), its `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md`, and `decisions/authority-districts-v0.1.md`. Where this decision conflicts with the Charter, the Charter wins.
**Evidence basis:** a read-only primary-source pass verified against current `origin/main`, at these pinned commits (working tree == `origin/main` for every repo at draft time):
- `afi-governance` @ `1b15fd217e4b326a00f541d3b258382e4434f3aa` (base; holds `D-CHOICE-1`)
- `afi-reactor` @ `9b56fb107cb9f54f50f5761d6f674046eb8b976c` (the shipped "M2" runtime surface)
- `afi-config` @ `ce8c1deab12fc00412b1cfcf08ac5599349235ce` (District-2 **M1** schema drafts)
- `afi-docs` @ `1f3f95988a3dfbe474fb50b60a912f69d01ac92e` (D-17 authorization; M0 plan; the Districts/API-Atlas audit)

The Districts/API-Atlas reconciliation audit (`afi-docs/specs/audit/districts-api-atlas/`, 96 findings) is **input, not authority**; every claim below was re-verified against primary sources and is cited by `path:line`.

**Ledger slot:** Fills `D-CHOICE-1` (`decisions/authority-districts-v0.1.md:109-114`). That clause recorded **Option (b) — shipped-but-non-normative** as the *registry's current default* and surfaced **(a)** prospective ratification and **(c)** rollback as owner options. This decision selects **(a)**, bounded exactly as specified there ("expressly preserving the record of its historical authorization gap"), and — on owner merge — moves the operative disposition of the District-2 "M2" surface from (b) to (a) as a governance-ledger fact. It does **not** rewrite `authority-districts-v0.1.md`; that record's account of the gap stands unaltered and is the historical baseline this decision preserves.

---

## 0. Why this decision exists

`decisions/authority-districts-v0.1.md` §D.1 established, and this decision re-verified, an authorization gap: the **only** District-2 authorization instrument authorizes **M1 only**, yet a District-2 **"M2"** runtime artifact surface shipped in `afi-reactor` with **no M2 authorization instrument in existence** (audit finding DIST-01). The topology/registry decision deliberately did **not** dispose of that surface — it recorded that **prospectively ratifying it** "is a **material District-scope authorization act**" that it excluded from its own scope (`authority-districts-v0.1.md:107`) and reserved to "a **separate** District-2 ratification decision" (`:109`). **This is that separate decision.**

It does one thing: it **prospectively ratifies the exact existing, reviewed, non-production "M2" surface** as a bounded set of shipped architecture and admissible candidate artifacts (§4.3 defines "admissible candidate") — **without** retroactively declaring the earlier work authorized, **without** blessing the broader milestone claims that documentation grouped under the "M2" label, and **without** deciding any object-identity, lifecycle, persistence, API, or economic question. Everything substantive remains for the later scoped decisions named in §7.

---

## 1. Historical authorization record (preserved, not laundered)

The following facts are recorded **as found** and are **not** softened, re-dated, or retroactively cured by this decision:

1. **The only District-2 authorization instrument authorizes M1 only.** `afi-docs/reports/district-2-d17-implementation-authorization.md` authorizes "**District 2 M1 — afi-config schema drafts and tests only** … **No runtime wiring**" (`:23`), states "It authorizes nothing beyond M1 … it does **not authorize M2–M6 or any other District work**" (`:19`), and mandates that "**Every implementation phase after M1 (M2–M6, and any successor) requires its own scoped PR/mission authorization** … Completion and review of M1 do not by themselves authorize M2" (`:84`).

2. **The M0 report is a plan, not an authorization.** `afi-docs/reports/district-2-m0-canonical-data-boundary-and-hash-doctrine.md` is "a **planning artifact, not an implementation authorization**" (`:543`, `:589`); "**No milestone here is authorized or begun by this M0 report**" (`:551`).

3. **The "M2" runtime surface shipped without an authorizing instrument.** The D2-native artifact surface exists at `afi-reactor@9b56fb1` under `src/pipeheads/provenance/` (see §2), yet **no M2 (nor M3/M4/M5) authorization instrument exists** in `afi-docs/reports/` or `afi-governance/decisions/` (audit finding DIST-01, re-verified).

4. **This decision does not retroactively authorize the past.** Consistent with `authority-districts-v0.1.md` Part B.1 ("Merging code does not ratify a decision"; "Shipped ≠ normative"), the work is recorded as having been **unauthorized when originally shipped**. Ratification here is **prospective only**: it governs the surface's status **from owner merge forward** and leaves the historical gap on the record exactly as the audit and §D.1 found it.

---

## 2. The exact surface ratified (commit-pinned inventory)

The ratified surface is **only** the following, at the pinned commits. Nothing outside this enumeration is ratified; §2.1 additionally marks the pre-existing **District-1** stages that the demo harness merely *composes*, which are expressly **not** ratified, re-opened, or re-scoped here.

### 2.1 `afi-reactor` @ `9b56fb107cb9f54f50f5761d6f674046eb8b976c` — the D2-native artifact layer and its demo wiring

**Implementation (`src/pipeheads/provenance/`, 7 files, 1,808 LOC):**
- `types.ts` — dev-time TS mirrors of the afi-config M1 schemas; declares the four artifact schema-id constants `afi.analyst-input-envelope.v1` (`:112`), `afi.scored-signal.v1` (`:137`), `afi.provenance-record.v1` (`:164`), `afi.replay-profile.v1` (`:187`), and the artifact/sub-artifact interfaces (`AnalystInputEnvelopeV1`, `ScoredSignalV1`, `ProvenanceRecordV1`, `ReplayProfileV1`, `EvidenceRefV1`, `SourceDisclosureProfileV1`, `EnrichmentProvenanceV1`). Header: "**Development-time types only — AJV compiled over the afi-config JSON schemas remains the single source of validation truth** … nothing here duplicates or overrides schema semantics" (`:1-6`).
- `canonicalHashV1.ts` — the `afi.hash.v1` / `sha256` CanonicalHash v1 hashing runtime (domain-separated preimage, recursive key sort, volatile-timestamp exclusion).
- `hashProjection.ts` — the field-specific canonical decimal-string projection used before hashing.
- `builders.ts` — the artifact builders and reference constants, including `REFERENCE_IMPLEMENTATION_NOTE` ("**Reference implementation / implementation profile … Not the canonical AFI pipeline — canonical status belongs to the merged afi-config schemas, validation rules, and hash doctrine only**", `:91-98`) and the `FORBIDDEN_ARTIFACT_KEYS` guard whose full twelve keys reject `claimRoot`, `rewardAmount`, `vaultAddress`, `validatorDecision`, `_id`, `createdAt`, `updatedAt`, `rawUss`, `lenses`, `_priceFeedMetadata`, `rawPayload`, `demoOnly` from any D2 output (`:115-128`).
- `envelopePipehead.ts`, `provenancePipehead.ts` — the two pipehead stations that build the envelope and the (ScoredSignal projection + ProvenanceRecord + ReplayProfile) set; `buildD2Artifacts`.
- `schemaValidation.ts` — the AJV adapter that validates emitted artifacts **against the afi-config M1 JSON schemas** ("the MERGED afi-config provenance schemas", loaded read-only from the `afi-config` dependency; "no schema content is duplicated locally", `schemaValidation.ts:2-13`). The characterization of those schemas as the sole validation authority is authored in `provenance/types.ts:4-5` ("AJV compiled over the afi-config JSON schemas remains the single source of validation truth").

**Composition & entrypoint (D2 wiring):**
- `src/pipeheads/index.ts` — barrel re-export, self-labeled "the D2-native reference implementation surface (District 2 M2)" (`:2-3`); its **D2 re-exports** are ratified.
- `src/pipeheads/harness.ts` — `runPipeheadHarness`, the offline DAG (`validate → fan-out → normalize → envelope → score → provenance`); its **D2 additions** (the `envelope` and `provenance` stages and the D2 artifacts on the aggregate) are ratified.
- `src/cli/run-pipehead-demo.ts` — the **demo CLI** and the D2 surface's **only non-test caller**; runs fully offline (no server, no listening socket, no network, no DB/vault write), self-terminating and deterministic.

**Composed but NOT ratified — pre-existing District-1 machinery.** `runPipeheadHarness` and the demo CLI also compose the pre-existing **District-1 Signal-Evaluation Pipehead POC** stages — `src/pipeheads/{schemaValidationPipehead.ts, fanOut.ts, normalizePipehead.ts, scoringPipehead.ts, clock.ts, types.ts, lanes/**}` (the five analysis lanes → deterministic scoring). Per the parent registry these belong to **District 1** (`authority-districts-v0.1.md:97`: District 1 implementation = `afi-reactor (src/pipeheads/)`), are already governed there, and are **composed but neither ratified, re-opened, nor re-scoped** by this decision. In particular the actual scoring runs in the District-1 `scoringPipehead.ts`, which binds the `afi-core/...` scorer by package name (`scoringPipehead.ts:32-37,68-76`); the harness "only COMPOSES the existing pipeheads … never touches scoring/UWR math" (`harness.ts:33-36`).

**Tests & committed fixtures (the D2-focused surface):** `test/pipeheads/{cli,scoring,d2Builders,d2SchemaValidation,canonicalHashV1,hashProjection,types,harness,crossArea}.test.ts`; the "D2 M2 golden anchor" cross-check in `test/guardrails/uwrRuntimeProfile.test.ts`; fixtures `test/pipeheads/fixtures/{golden.json, signal.uss.json, ohlcv.json, signal.invalid.uss.json, lanes/*.json}`. `golden.json` is the committed replay anchor (scoring values + four `afi.hash.v1` digest pins). (The District-1 stage tests — `fanOut`, `lanes`, `normalize*`, `clock`, `schemaValidation` — are District-1 surface, not part of this ratification.)

**Emitted artifacts:** four top-level artifacts (`AnalystInputEnvelope v1`, `ScoredSignal v1` projection, `ProvenanceRecord v1`, `ReplayProfile v1`) plus four embedded sub-artifacts (`CanonicalHash v1`, `EvidenceRef v1`, `SourceDisclosureProfile v1`, `EnrichmentProvenance v1`), printed **to stdout only**. `TradePlan v1` is **validated-only, never generated** by this surface.

### 2.2 `afi-config` @ `ce8c1deab12fc00412b1cfcf08ac5599349235ce` — the M1 draft schemas the M2 surface mirrors and validates against

The nine Draft-07 JSON schemas under `schemas/provenance/v1/` (`analyst-input-envelope`, `canonical-hash`, `enrichment-provenance`, `evidence-ref`, `provenance-record`, `replay-profile`, `scored-signal`, `source-disclosure-profile`, `trade-plan`) + their nine examples under `examples/provenance/v1/*.example.json` + `tests/provenance-schema-validation.test.ts`. Each schema **self-labels its draft, non-implementation, M1 status**: e.g. `scored-signal.schema.json` title "AFI ScoredSignal v1 Projection (**District 2 M1 DRAFT**)" (`:4`), `x-afiStatus: "draft-non-implementation"` (`:7`), `x-afiPartOf: "AFI District 2 — Canonical Data & Provenance Boundary (D2 M1)"` (`:8`).

**These M1 artifacts remain M1 and remain authorized by D-17.** This decision does **not** re-scope, re-status, or re-authorize them; it records only that the reactor M2 surface **mirrors and validates against** them (single source of validation truth), so the two layers are one artifact family, not a fork.

### 2.3 Classification of the entire ratified surface

Verified by primary-source reachability analysis: the surface is **implementation-only + CLI-only + test-reachable**. It is **NOT production-reachable** (the live server `afi-reactor/src/server.ts` — `POST /api/webhooks/tradingview`, `POST /api/ingest/cpj`, `app.listen` — imports only `froggyDemoService`, the USS/CPJ validators/mappers, `ingestDedupeService`, and the telegram collectors; it never imports `src/pipeheads/` and never reaches `runPipeheadHarness`); **NOT persisted** (no DB/vault write; the demo CLI's only filesystem call is a read-only input-fixture read via `readFileSync` — schema files are separately read read-only by the validation stage; `buildProvenanceRecord` "persists nothing"; the `froggyDemoService → tssdVaultService` MongoDB vault write belongs to the **pre-existing non-M2** live pipeline); **NOT API-exposed** (no HTTP route, no endpoint; `ReplayProfile` is an artifact/id-ref, not an endpoint); and **not an installed entrypoint** (the demo CLI is not wired into `package.json` `bin`/`main`/`scripts`).

> **Terminology guard (binding on any reader of this decision).** Three distinct things are named "provenance" in `afi-reactor` and must never be conflated: **(1)** the pre-existing **USS `provenance` ingest block** (`signalId`/`providerId`/`source`/`ingestHash`) that the live server and vault write use — **production, NOT M2**; **(2)** the **District-2 M2 D2-native artifact surface** under `src/pipeheads/provenance/` — **the subject of this decision, CLI/test-only**; **(3)** the internal `bundle.provenance.inputHash` intermediate — CLI/test-only. This decision ratifies **only (2)**.

---

## 3. What "M2 as shipped" means — and the M2/M3/M4/M5 boundary (anti-overreach)

The label "M2" in `afi-reactor` **does not match** the M0 plan's milestone numbering, and this decision governs the **shipped reality**, not the label. Per the M0 §11 milestone table (`afi-docs/…/district-2-m0-…md:553-559`), the artifact **shapes** the reactor surface emits span **four** planned milestones: `CanonicalHash v1` (planned **M2**, `:556`); `ProvenanceRecord v1` + the thin `ScoredSignal v1` projection + `EvidenceRef v1` hashes (planned **M3**, `:557`); `AnalystInputEnvelope v1` + `EnrichmentProvenance v1` + `SourceDisclosureProfile v1` (planned **M4**, `:558`); and `ReplayProfile v1` (planned **M5**, `:559`). The reactor collapses these under one "District 2 M2" caption (e.g. `afi-reactor/docs/PIPEHEAD_SYSTEM.md:69`; `afi-reactor/src/pipeheads/types.ts:7`) — the audit's DIST-03 records this collapse (and, as re-verified, understates it by omitting the M5/`ReplayProfile` reach).

**Ratification is scoped to the artifact shapes and their non-production reference realization (builders, the `CanonicalHash v1` hashing runtime, the demo CLI, the tests) as emitted over the fixture/reference harness — and to nothing more.** Concretely, this decision ratifies the **existence, structure, and non-production reference realization** of those artifact shapes. It **does not** ratify the *rest* of what those planned milestones entail, because **that rest is not shipped**:

- **Not ratified — planned-M2 remainder:** the shallow-`ingestHash` → `CanonicalHash v1` **migration** (unshipped; the live server still computes the old shallow `ingestHash`).
- **Not ratified — planned-M3 remainder:** **production-path wiring** of `ProvenanceRecord v1` and **replacement of the heavy `ReactorScoredSignalV1`** with the thin projection at the live scored seam (unshipped; the server still returns `ReactorScoredSignalV1`).
- **Not ratified — planned-M4 remainder:** **production integration** of `AnalystInputEnvelope v1` at the analyst-input seam — wrapping the *live* enriched view, populating `EnrichmentProvenance v1` upstream of normalize, and carrying `SourceDisclosureProfile v1` on the live envelope (unshipped; the production path feeds the enriched view directly to the scorer and never constructs the envelope). Only the fixture-harness envelope is shipped.
- **Not ratified — planned-M5 remainder:** **CPJ field survival** (`TradePlan v1` / `SignalLevels v1`, `authorRef`/`authorHash`) as a live behavior (unshipped; only a `validateTradePlanV1` helper exists, generating nothing).

Excluding these is a statement of **fact** (they do not exist to ratify), not a narrowing of scope. Each remains unauthorized and requires its own governance slot (§8).

---

## 4. Decision — prospective bounded ratification

Upon owner merge, and **only** then:

1. **The surface enumerated in §2, at the pinned commits, is prospectively ratified as reviewed, non-production District-2 architecture** — recorded as *shipped reality that is now governance-recognized*, per `authority-districts-v0.1.md` tier-4 (reality). This decision characterizes that tier-4 surface as an **admissible candidate** (its own term, defined in §4.3), which is exactly the prospective ratification that §D.1 option (a) authorizes (`authority-districts-v0.1.md:110`).
2. **The historical authorization gap is expressly preserved** (§1). Ratification is prospective; it does **not** declare the earlier work to have been authorized when shipped, and it does **not** cure DIST-01 retroactively.
3. **The M2 artifacts are admitted as candidate architecture evidence** for the later `OBJ-GOV` object-identity decision and related scoped decisions (§7–§8). "Admissible candidate" means available for evaluation — **not** adopted, **not** canonical, **not** final.
4. **Non-production / demo status is preserved.** The surface remains offline, CLI-only, test-reachable, unpersisted, and unexposed. Ratification confers **no** production status and authorizes **no** production enablement.
5. **No M2 object is declared canonical.** Ratifying-as-shipped does **not** make `ScoredSignal v1` the canonical scored-signal object, `ProvenanceRecord v1` the canonical persistence/provenance object, `AnalystInputEnvelope v1` the canonical input object, or any identifier the canonical Signal/Strategy identifier. The in-code word "canonical" — everywhere it appears on this surface, including `src/pipeheads/provenance/types.ts:140` ("thin canonical … projection"), `provenancePipehead.ts:5`, `afi-config/schemas/provenance/v1/scored-signal.schema.json:5`, `analyst-input-envelope.schema.json:5`, and `provenance-record.schema.json:5` ("DRAFT / NON-IMPLEMENTATION canonical provenance record"), plus `builders.ts:109`'s "D2 canonical outputs" (which means hash-canonical *serialization*, not object canon) — is read **only** in its qualified, in-place sense (a draft projection / canonicalized bytes) and is **explicitly not** an assertion of canonical object identity (see §7 OBJ-GOV).
6. **Nothing broader than the shipped surface is ratified.** The unshipped milestone remainders in §3 and the domains in §7 are outside this ratification.

---

## 5. Exclusions — withheld from ratification

The following are **outside** this decision and are neither ratified, authorized, nor endorsed:

- The unshipped planned-M2/M3/M4/M5 remainders (ingest-hash migration; production-path wiring; replacement of `ReactorScoredSignalV1` at the live seam; `AnalystInputEnvelope v1` production integration at the analyst-input seam; CPJ/`TradePlan` survival) — §3.
- Any production enablement, persistence authority, API/endpoint exposure, or behavioral change of the surface.
- The pre-existing **District-1** Signal-Evaluation Pipehead POC stages that the demo harness/CLI compose (`src/pipeheads/{lanes/**, schemaValidationPipehead.ts, fanOut.ts, normalizePipehead.ts, scoringPipehead.ts, clock.ts, types.ts}`) — governed under District 1 (`authority-districts-v0.1.md:97`), neither ratified nor re-opened here (§2.1).
- The pre-existing USS-provenance live pipeline and the `tssdVaultService` MongoDB vault write (not M2; not in scope).
- The generic `src/dag/*` "Pipehead" DAG framework (a different abstraction; not the M2 surface).
- Any `afi-config` M1 re-scoping, re-status, or promotion beyond its existing D-17 M1 authorization.
- Anything the surface's own `FORBIDDEN_ARTIFACT_KEYS` guard structurally excludes (economic, storage, and validator-decision fields).

---

## 6. ⚠ OWNER-CHOICE CLAUSE (`D-CHOICE-1a`) — the one genuinely divisible seam

The shipped surface is **homogeneously non-production**, so it is otherwise safe to ratify as a single unit. Exactly **one** seam is genuinely debatable and is surfaced here rather than silently decided: the M2 reference harness's `schemaValidation.ts` **reads and enforces the afi-config M1 draft schemas at module load** (a real runtime coupling), while D-17 M1 said "**No runtime wiring**" (`district-2-d17-…md:23`) and the afi-config schema README states "**nothing here may be referenced by runtime configuration until a later District 2 phase authorizes it**" (`afi-config/schemas/provenance/v1/README.md:7`).

The owner chooses one:

- **(A) — DEFAULT (recommended):** Ratify this coupling **only as read-only, in-process schema validation inside the non-production reference harness**. Any consumption of these schemas by **production** runtime configuration or the live scored seam remains **unauthorized** and requires a new slot (§8). *(This is the conservative reading and this decision's proposed default.)*
- **(B):** **Carve the coupling out** of ratification entirely — ratify the artifact shapes, builders, CLI, and tests, but treat even the reference harness's schema-load as unratified pending a dedicated decision.
- **(C):** Fold the disposition of this seam into the future `OBJ-GOV` / schema-authority decision and leave it **shipped-but-non-normative** in the interim (mirroring §D.1's original option (b) for this sub-part only).

This decision proposes **(A)**; it makes none of (A)/(B)/(C) a fait accompli. No other portion of the surface is split — the remainder ratifies as one unit under §4.

---

## 7. Explicit non-decisions

This decision does **not** decide, authorize, ratify, or pre-empt any of the following. Each remains for its own separately governed scoped decision, and ratifying the shipped surface **pre-decides none of them** (verified: the surface self-labels draft/non-implementation, forbids the encoding fields, and is absent-by-design for the lifecycle/store/endpoint/economic concepts):

- **OBJ-GOV** — canonical **Signal** identity; canonical **Strategy** identifier; canonical **Analyst Score / Scored Signal** shape. *(The ratified `ScoredSignal v1` is an admissible draft projection candidate only; its in-code "canonical" wording is expressly non-binding here — §4.5.)*
- **LIFE-GOV** — lifecycle states, qualification, finality, or transition ownership.
- **MONGO-GOV** — canonical MongoDB store or write ownership. *(The optional `ProvenanceRecordV1.storageProfileRef` is inert — the surface emits none — and is **not** a store commitment.)*
- **ATLAS-GOV** — API Atlas or Gateway authority; replay/read/verify endpoints. *(`ReplayProfile v1` is an artifact, not an endpoint.)*
- **CHAIN-GOV** — epoch, receipt, reputation, reward, claim, settlement, or vault semantics; minting or economics; on-chain anchoring.
- **Production scoring law.** The surface changes **no** scoring math: the D2 artifact-projection layer (`builders.ts` / `provenancePipehead.ts`) **never imports `afi-core`** (`builders.ts:24`) and re-projects the scorer's outputs **verbatim** (`provenancePipehead.ts:6` "read VERBATIM from the afi-core analystScore, never recomputed"); the actual scoring is performed by the pre-existing **District-1** `afi-core` scorer bound by the `afi-core/...` package name in `scoringPipehead.ts` (`:32-37,68-76`), which the harness "only COMPOSES … never touches scoring/UWR math" (`harness.ts:33-36`). The golden/guardrail anchors record "**District 2 M2 changed the artifact surface, NEVER the scoring math**" (`test/pipeheads/fixtures/golden.json`; `uwrScore == 0.1875` in `test/guardrails/uwrRuntimeProfile.test.ts:307`).
- **UWR changes.** No UWR profile, axis registry, weight, or decay value is added, altered, or pinned.

It also does **not** amend `authority-districts-v0.1.md`, the Charter, the Addendum, or any prior decision; it creates **no** implementation slot; and it authorizes **no** repository code, schema, package, contract, persistence, API, or economic change.

---

## 8. What still requires a new governance slot

Any of the following remains **unauthorized** until its own scoped owner decision (or owner-recorded PR authorization, per the `uwr-runtime-consumption-v0.1.md` RC-12 pattern) exists:

- **Expansion beyond the shipped surface** — implementing any unshipped milestone remainder in §3 (ingest-hash migration; production-path wiring; `ReactorScoredSignalV1` replacement at the live seam; `AnalystInputEnvelope v1` production integration; CPJ/`TradePlan` survival).
- **Production enablement** — wiring any part of the surface into `server.ts`, the DAG executor, or any live request path.
- **Persistence authority** — writing any emitted artifact to MongoDB, a vault, or any store (→ future MONGO-GOV).
- **API exposure** — exposing replay/read/verify or any endpoint over the surface (→ future ATLAS-GOV).
- **Behavioral / object-law changes** — declaring any M2 object canonical, or defining lifecycle/finality/economic semantics over it (→ future OBJ-GOV / LIFE-GOV / CHAIN-GOV).

---

## 9. Relationship to existing decisions

- **`decisions/authority-districts-v0.1.md`** — unchanged and un-amended. This decision **resolves its open `D-CHOICE-1`** by selecting option (a) within the exact bounds §D.1 specified; the District-2 registry row's recorded default (b) is superseded **prospectively** by this decision on merge, as a governance-ledger fact, without rewriting that file.
- **`district-2-d17-implementation-authorization.md`** (afi-docs) — unchanged. Its M1-only authorization and its §9 per-phase gating remain in full force; this decision neither extends nor reinterprets it, and expressly preserves the gap it did not cover.
- **`math-authority-v0.1.md`, `mint-formula-bt-86b-alignment-v0.1.md`, `uwr-profile-pin-v0.1.md`, `uwr-runtime-consumption-v0.1.md`** — unchanged. No delegation, open decision, non-authorization, or ledger row in any of them is altered. No scoring, mint, or UWR matter is touched.

---

**Accepted owner decision (afi-governance PR #15, merge commit `65997fb`). Authoritative upon owner merge. This decision ratifies an existing non-production surface within an exactly enumerated, commit-pinned scope; it authorizes no new implementation, and it does not retroactively authorize the historical gap it preserves.**
