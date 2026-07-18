# AFI District One — Current Signal Evaluation Capability v0.1 (D1CAP-GOV)

**Slot:** `AFI-GOV-DISTRICT-ONE-SIGNAL-EVALUATION-CAPABILITY-v0.1` (D1CAP-GOV)
**Status:** **Proposed** for owner approval. This decision records the owner's settled model of **District One as AFI's active Signal Evaluation capability and authority domain**: its durable responsibility boundary, its exclusions, its descriptive current-implementation mapping, the implementation-replacement rule, the historical ruling on the retired Pipehead POC, the honest provider-runtime state, and the governing terminology. It becomes authoritative **only** when the owner merges it; until merged, it is a draft with no force. **Owner authorization is recorded by the owner instruction that commissioned this decision** (the Mission D1 "Current Signal Evaluation District Reconstitution" mission, 2026-07-18, issued by the owner), under the convention FCP-GOV and DSC-GOV record.
**Date:** 2026-07-18
**Type:** Scoped protocol-development governance decision (District registry / implementation-record amendment + capability record). Docs/governance-ledger only. It changes **no** runtime or protocol code (the sole mechanical change it authorizes is the bounded afi-docs guard-script amendment of D-D1CAP-8 item 3), **no** runtime behavior, **no** scoring or UWR value, **no** evidence or hash behavior, **no** provider behavior, and **no** schema. It is an implementation-record and registry-record amendment in the D-DSC-2 pattern — **not** a District creation, deletion, scope change, or production promotion.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` (canonical home `afi-config/codex/governance/droids/`), its `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md` (unamended; its §13 non-production ceiling and §14 no-financial-truth rule are honored), and `decisions/authority-districts-v0.1.md`. **Consumes (does not re-decide)** `district-surface-consolidation-v0.1.md` (DSC-GOV — this decision confirms and elaborates the District survival its D-DSC-2 recorded), `factory-configurable-pipelines-v1.md` (FCP-GOV — the five-category namespace and composition model), `provider-byok-foundations-v0.1.md` (PBF-GOV — the provider socket), `object-identity-v0.1.md`, `lifecycle-v0.1.md`, `persistence-v0.1.md`/`persistence-impl-v0.1.md`, `uwr-profile-pin-v0.1.md`/`uwr-runtime-consumption-v0.1.md`, `math-authority-v0.1.md`, `research-institute-reference-services-v0.1.md`, and `district-2-m2-ratification-v0.1.md`. **Supersedes, prospectively and only as stated in D-D1CAP-2,** six cells of the `authority-districts-v0.1.md` Part D District-1 registry row (re-recording on top of the DSC-GOV D-DSC-2 implementation-record amendment, which it cites and does not disturb). Honors, and does not touch, the reserved ATLAS-GOV and CHAIN-GOV scopes. Where this decision conflicts with the Charter, the Charter wins.
**Evidence basis:** a 3-agent read-only preflight (2026-07-18; runtime call-graph re-proof, governance-instrument scan across all 14 accepted decisions, current-docs scan; **input, not authority**; load-bearing findings restated in §1), verified against clean `origin/main` trees at: `afi-governance` @ `1c3d5a1`, `afi-reactor` @ `a8a1762`, `afi-docs` @ `7288225`, `afi-protocol` @ `9ca5306`, `afi-config` @ `a1a1279`, `afi-core` @ `54ca87a`.
**Ledger slot:** None existed — DSC-GOV D-DSC-2 amended the District-1 implementation record when it retired the POC implementation and expressly preserved the District ("This is an implementation retirement, **not** a District retirement", `district-surface-consolidation-v0.1.md:83`); this decision is the affirmative capability record that amendment anticipated.

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these 8):**

1. **D-D1CAP-1** — District One's identity: the active Signal Evaluation capability and authority domain.
2. **D-D1CAP-2** — the prospective re-record of the Part D District-1 registry row.
3. **D-D1CAP-3** — District One's durable responsibility boundary.
4. **D-D1CAP-4** — District One's exclusions.
5. **D-D1CAP-5** — the descriptive current-implementation mapping and the implementation-replacement rule.
6. **D-D1CAP-6** — the historical Pipehead ruling.
7. **D-D1CAP-7** — the honest provider-runtime state.
8. **D-D1CAP-8** — terminology, the API-Atlas/registry reservation, and the bounded documentation-guard anchors.

**Does not decide (expressly):** any production promotion or deployment (the Addendum §13 ceiling and the `authority-districts-v0.1.md:101` deferred scope — "Any production promotion; any financial-truth authority" — stand unchanged); the Five-Lane Provider Runtime Cutover (Mission B — separate future owner authorization); any sentiment or aiMl provider adapter; any API Atlas artifact (ATLAS-GOV reserved); any runtime, scoring, UWR, evidence, hash, persistence, or schema change; any District creation, deletion, or scope change; any Charter or Pipehead Addendum amendment; any reversal of DSC-GOV's deletion authorization.

---

## 1. Verified evidence restated (input, not authority)

Re-verified at the pinned commits by direct call-graph and instrument reading:

- **No accepted instrument retires District One as a capability.** DSC-GOV retired the POC **implementation** and said so explicitly (`district-surface-consolidation-v0.1.md:83`); all other retirement language across the 14 accepted decisions concerns UWR stubs, stores, enums, or contract lists — none touches the District. The gap is representational only: the Part D row still names District 1 the "Signal-Evaluation Pipehead POC" with a proof-of-concept purpose and a `src/pipeheads/` implementation pin (`authority-districts-v0.1.md:93,95,97-100`), while the POC no longer exists.
- **One live executor; one flow.** Both Reactor ingresses (`src/server.ts:215` `/api/webhooks/tradingview`, the external-facing webhook with optional shared-secret; `:374` `/api/ingest/cpj`, the internal trusted service-to-service boundary per INST-GOV) resolve a registered strategy fail-closed, then score through `graphScoringService.ts:94-103` on the **one** `GraphExecutor` (constructed once, `runtimeComposition.ts:100`), executing the registered manifest `froggy-trend-pullback@v1.0.0` (7 nodes / 9 edges; `afi-config/registries/pipelines/`) over the seven classic nodes in `src/pipeline/nodes/`; `mergeEnrichedView` enforces exactly one result per category; the scored result is handed to District Two at `server.ts:320`/`:513` (`submitScoredSignalEvidence`).
- **Score-input truth.** The analyst score (uwrScore/uwrAxes) is a function only of the afi-core `FroggyTrendPullbackInput`; the enrichment adapter reads exactly `technical.{emaDistancePct,isInValueSweetSpot,brokeEmaWithBody}`, `pattern.{patternConfidence,patternName}`, and `sentiment.tags` (`afi-core/analysts/froggy.enrichment_adapter.ts:212-261`). **news and aiMl are never read by scoring** (documented in afi-core); the sentiment/patternName sweep-hint path is wired but provably inert under the live value domains; the merge pins `brokeEmaWithBody=false`. news and aiMl do enter lenses, `enrichmentMeta`, and the composition's enrichmentHash (evidence surfaces), so they influence evidence, never the score.
- **Provider-layer truth.** `builtinProviderAdapters()` = technical (keyless local), news (HTTP BYOK, header-carried key), pattern (keyless local) — three adapters; **no sentiment or aiMl adapter exists**. Governed provider records exist for technical-local and news-http only (no pattern record file yet in `afi-config/registries/providers/`). **No registered manifest node carries a `providerInstanceRef`** (zero hits across `afi-config/registries/`), and the composition's provider runtime is constructed fail-closed at boot but consumed by nothing — the socket is a dormant forward surface for **all five** categories; every category executes live through its classic node.
- **Structure.** `src/pipeheads/`, `src/dag/`, `src/aiMl/providers/` absent; District-2 law at `src/evidence/provenance/`; no machine-readable District registry exists anywhere in afi-governance, afi-config, or afi-reactor — the Part D prose registry plus the accepted decision chain is the sole District map.

---

## 2. D-D1CAP-1 — District One identity

**Decision.** District One is **AFI's Signal Evaluation capability and authority domain. It is active.** It is not the retired Pipehead POC, and it is not any particular directory, class, manifest, analyst, provider, or strategy.

The governing doctrine is recorded as District law:

> Districts represent durable capability and authority boundaries. Implementations may be replaced without deleting the district they implement.

"Active" is a capability-domain statement, not a deployment statement: the district has a live, CI-proven current implementation, and the organization-wide posture remains **non-production** (nothing is deployed; the Addendum §13 ceiling and the Part D deferred-scope cell stand).

**Scope-guard.** Identity record only; grants no new authority.

---

## 3. D-D1CAP-2 — Part D registry row re-record (prospective)

**Decision.** The `authority-districts-v0.1.md` Part D District-1 row is re-recorded **prospectively as a governance-ledger fact, without rewriting that file** (the D2R:16/:167 convention, as DSC-GOV D-DSC-2 already did for two of these cells). The operative registry record for District 1 is now:

| Field | District 1 (operative record) |
|---|---|
| Canonical identifier | `District 1` *(unchanged)* |
| Human-readable name | **Signal Evaluation** *(re-recorded; formerly the POC-era label)* |
| Functional name (Addendum) | Signal Evaluation Pipehead System (Addendum §12) *(unchanged — bound to the unamended Addendum's literal term)* |
| Purpose | **Own AFI's signal-evaluation capability: canonical signal input → five-category enrichment → deterministic join → analyst/scorer/UWR seam → handoff to District 2 — without becoming a source of financial truth (Addendum §14)** |
| Authority source | GOVERNED — Addendum §9/§12/§13 *(unchanged)* |
| Implementation repo | **`afi-reactor` — the live GraphExecutor pipeline (`src/pipeline/`, composition in `src/config/`, scoring service in `src/services/`, provider framework in `src/providers/`); governed contracts and registries in `afi-config`** |
| Implementation status | **IMPLEMENTED — live manifest-driven GraphExecutor pipeline (sole signal-evaluation executor; DSC-GOV D-DSC-1)** |
| Production status | **Non-production** *(the POC-era "demo-only" gloss is dropped; nothing is deployed)* |
| Governed scope | **The durable responsibility boundary of D-D1CAP-3; deterministic scoring/validation/audit discipline; Droids may not become the source of financial truth (Addendum §14)** |
| Explicitly deferred scope | Any production promotion; any financial-truth authority *(unchanged)* |

The District-2 row is untouched by this decision (its location record was already re-recorded by DSC-GOV D-DSC-3).

**Scope-guard.** Registry-record amendment in the accepted D-DSC-2 pattern; no District scope change; no new District; no production promotion.

---

## 4. D-D1CAP-3 — Durable responsibility boundary

**Decision.** District One owns or governs, within the evaluation domain and under the accepted decision chain:

1. **receiving canonical signal input** from an authorized ingress/normalization boundary (USS v1.1 is the canonical convergence checkpoint; ingress operation itself is governed by INST-GOV);
2. **evaluation-time validation** of that input;
3. **execution of the five enrichment categories** (`technical`, `pattern`, `sentiment`, `news`, `aiMl` — the FCP-GOV D-FCP-1 namespace);
4. **explicit provider-instance resolution for provider-backed categories** (the PBF-GOV socket; a forward surface until the separately-authorized cutover — see D-D1CAP-7);
5. **category-result validation** against the governed `afi.enrichment.*.v1` contracts;
6. **category fan-out, dependency execution, and deterministic joining** with exactly one validated result per category at the join;
7. **analyst selection and invocation** under accepted authority (registered strategies; fail-closed resolution);
8. **canonical scorer/UWR invocation** — invoking, never re-implementing, the afi-core scorer under the pinned UWR profile law;
9. **creation of the scored evaluation result** that is handed to District Two.

Items are capability ownership, not completeness claims: the provider-backed path in item 4 exists and is governed but is not yet the live seam for any category (D-D1CAP-7).

**Scope-guard.** Boundary record; consumes existing law (FCP-GOV, PBF-GOV, UWR decisions, INST-GOV) and grants no new runtime authority.

---

## 5. D-D1CAP-4 — District One exclusions

**Decision.** District One does **not** own: canonical evidence/provenance construction after scoring (District Two); canonical persistence (MONGO-GOV; afi-infra store ownership); reputation updates; epoch qualification; receipt issuance; reward calculation; claims; settlement; treasury or vault movement; governance voting; external-agent interface discovery; or the future API Atlas (ATLAS-GOV reserved). The District One → District Two boundary is the scorer/UWR seam: District One produces the scored evaluation result; District Two constructs and validates the governed evidence record from it and owns the canonical handoff to persistence.

**Scope-guard.** Exclusion record; changes no ownership that accepted decisions already assign.

---

## 6. D-D1CAP-5 — Current implementation binding and replacement rule

**Decision.** The current governed implementation mapping of District One is recorded **descriptively**:

- the **`GraphExecutor`** (`afi-reactor/src/pipeline/executor.ts`) — the sole signal-evaluation executor (DSC-GOV D-DSC-1);
- the **runtime composition** (`src/config/runtimeComposition.ts`) and the **graph scoring service** (`src/services/graphScoringService.ts`);
- the **registered graph manifests and strategy registrations** (`afi-config/registries/pipelines/`, `registries/analyst-strategies/`, boot-validated fail-closed);
- the **current category nodes** (`src/pipeline/nodes/` — five category nodes, the merge join, the scorer node);
- the **provider framework** (`src/providers/` — the one intended provider registry/runtime/adapter socket);
- the **governed `afi.enrichment.*.v1` result contracts** (`afi-config/schemas/enrichment/` — all five exist);
- the **canonical analyst/scorer integration** (the afi-core froggy analyst and UWR kernels, invoked never re-implemented);
- the **handoff into District Two** (`submitScoredSignalEvidence` from both ingress paths).

> These paths are the current governed implementation mapping, not the permanent identity of District One. A future conforming implementation may replace them through accepted authority without retiring the district.

No line-number or commit pins are placed on this mapping (the evidence-basis pins record the verification commits only), so ordinary implementation evolution under existing authority does not invalidate the record.

**Scope-guard.** Descriptive binding; authorizes no implementation change by itself.

---

## 7. D-D1CAP-6 — Historical Pipehead ruling

**Decision.** The District One Pipehead POC was **one former non-production implementation** of this district. Mission A (DSC-GOV D-DSC-2) retired and deleted it from the active tree; **no active Pipehead implementation remains**; git history and the accepted governance record are its archive. **Its retirement did not retire District One.** The intended interpretation is fixed:

> Mission A retired the former implementation. This decision confirms the enduring district.

Nothing in this decision reverses, weakens, or re-opens DSC-GOV's deletion authorization, and nothing restores or authorizes restoring the POC, its interfaces, its demo, its lanes, an executable reference copy, or "Pipehead v2" naming for the current pipeline.

**Scope-guard.** Interpretation record; consumes DSC-GOV.

---

## 8. D-D1CAP-7 — Provider-runtime truth

**Decision.** The honest current provider state is recorded:

- `src/providers/` is the **sole intended provider framework** (PBF-GOV; DSC-GOV D-DSC-6).
- **technical, news, and pattern** have current registered provider adapters (technical keyless-local; news credentialed-HTTP with the key in a header, never a URL; pattern keyless-local). Governed provider records exist today for technical-local and news-http; a governed pattern provider record does not yet exist in `afi-config/registries/providers/`.
- **sentiment and aiMl have no provider adapter**; they (and full five-lane operation of the socket) require the future **Five-Lane Provider Runtime Cutover** (Mission B).
- The provider socket is **not yet the live seam for any category**: no registered manifest node carries a `providerInstanceRef`, and the boot-constructed provider runtime is a dormant, fail-closed forward surface. All five categories currently execute through their classic nodes.
- For scoring truth: **news and aiMl never affect the analyst score**; sentiment's only score-facing input is wired but inert under the live value domains; the live score-varying enrichment inputs are technical and pattern values. (news/aiMl do enter lenses and the evidence-side enrichment hash.)
- **Mission B remains separate and is not authorized by this decision.**

**Scope-guard.** State record; no cutover, no adapter, no credential, no wiring is authorized.

---

## 9. D-D1CAP-8 — Terminology, Atlas/registry reservation, documentation anchors

**Decision.**

1. **Terminology (normative):** District One = **Signal Evaluation** (active). District Two = **Evidence and Provenance** (active; `Canonical Data & Provenance Boundary` remains its registry long-form). `sentiment` is the current category; `social` must not appear as a sixth category. **Pipehead POC** = historical retired implementation. **GraphExecutor** = current execution implementation. **API Atlas** = reserved future discoverability layer.
2. **Atlas and registry reservation:** No canonical API Atlas exists. **District authority and the accepted decision chain — the Part D prose registry as amended by DSC-GOV and this decision — remain the current District map.** No machine-readable District registry exists anywhere in the organization, and none is created by this decision: a future machine-readable registry/catalog of District capabilities and real interfaces belongs to the reserved ATLAS-GOV program, which will describe — not define or execute — District capabilities.
3. **Documentation anchors (bounded guard amendment):** the afi-docs current-architecture guard (`scripts/check_architecture_doc.py`, scope: `AFI_Full_Architecture.md` only) is amended to additionally require the literal anchors "District 1 — Signal Evaluation" and "District 2 — Canonical Data" and the Atlas-honesty pair ("API Atlas" + "not started"), and to ban the literal "src/pipeheads". Its existing historical-vocabulary bans already prevent unqualified "retired" phrasing in that document. No larger linter is created.

**Scope-guard.** Exactly these; the guard amendment touches one existing script in its existing convention.

---

## Explicit non-authorizations

This decision does **not** authorize: restoring any Pipehead code, interface, demo, lane, or naming; any change to GraphExecutor, runtime composition, category nodes, providers, adapters, schemas, scoring, UWR, evidence, hashes, goldens, or persistence; the Five-Lane Provider Runtime Cutover or any sentiment/aiMl adapter (Mission B and later, separately owner-gated); making news or aiMl affect scoring; any API Atlas schema, registry, UI, MCP catalog, endpoint, or agent-tool manifest (ATLAS-GOV reserved); any new District or District numbering change; any production promotion, deployment, or secret provisioning; any Charter or Addendum amendment; any rewrite of accepted decision files (all supersession here is prospective ledger fact).

---

## Supersessions and interactions (every prior decision walked)

- **`authority-districts-v0.1.md`** — its Part D District-1 row is re-recorded prospectively per D-D1CAP-2 (six cells; four cells expressly unchanged), on top of and consistent with DSC-GOV D-DSC-2; the file is not rewritten; Part D's two-District rule, Part E gates, and Part F agent limits are unchanged and honored (this decision is itself the owner-commissioned governance act Part E requires for registry amendment).
- **`district-surface-consolidation-v0.1.md` (DSC-GOV)** — consumed and confirmed, not disturbed: its D-DSC-2 implementation retirement, deletion list, and "not a District retirement" ruling are the factual basis of D-D1CAP-6; its D-DSC-1 sole-executor record is restated in D-D1CAP-2/5; its D-DSC-7 terminology is extended by D-D1CAP-8.
- **`factory-configurable-pipelines-v1.md` (FCP-GOV)** — consumed: the five-category namespace (D-FCP-1), composition model and executor boundary, registry mechanism, and evidence-v2 composition reference are unchanged; D-D1CAP-3 item 3/6 restate them as District-1 responsibilities.
- **`provider-byok-foundations-v0.1.md` (PBF-GOV)** — consumed: the provider socket, BYOK boundary, and adapter law are unchanged; D-D1CAP-7 records their current dormancy honestly.
- **`district-2-m2-ratification-v0.1.md`** — untouched; the District-2 boundary in D-D1CAP-4 matches its ratified scope as relocated by DSC-GOV D-DSC-3.
- **`object-identity-v0.1.md`** — untouched; USS v1.1 and the ScoredSignal projection identities are consumed by D-D1CAP-3 items 1/9.
- **`lifecycle-v0.1.md`** — untouched; the implemented lifecycle still halts at SCORED; District One's output is the SCORED-state evaluation result.
- **`persistence-v0.1.md` / `persistence-impl-v0.1.md`** — untouched; persistence stays excluded from District One (D-D1CAP-4).
- **`uwr-profile-pin-v0.1.md` / `uwr-runtime-consumption-v0.1.md`** — untouched; the scorer/UWR seam remains invoke-never-reimplement with all pins, bans, and golden conditions in force.
- **`math-authority-v0.1.md`** — untouched; kernels stay in afi-core/afi-math.
- **`mint-formula-bt-86b-alignment-v0.1.md`** — untouched; no economic surface.
- **`research-institute-reference-services-v0.1.md` (INST-GOV)** — consumed: ingress operation and the internal-trusted classification of the direct CPJ route are its law; District One receives canonical input from that boundary (D-D1CAP-3 item 1).
- **Reserved ATLAS-GOV / CHAIN-GOV** — honored and untouched; D-D1CAP-8 records the Atlas reservation and assigns any future machine-readable District registry to ATLAS-GOV.

---

**Proposed for owner approval. Authoritative only upon owner merge.**
