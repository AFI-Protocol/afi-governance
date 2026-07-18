# AFI Clean-Cut District Surface Consolidation v0.1 (DSC-GOV)

**Slot:** `AFI-GOV-DISTRICT-SURFACE-CONSOLIDATION-v0.1` (DSC-GOV)
**Status:** **Accepted** owner decision — accepted by merge of afi-governance PR #24 on 2026-07-18 (merge commit `bebe839`, merged unedited). This decision records the owner's settled clean-cut consolidation doctrine for the District surfaces in `afi-reactor`: the **sole-executor authority record**, the **retirement of the historical District-1 pipehead POC implementation**, the **organizational relocation of the live District-2 provenance law** out of the `src/pipeheads/` tree, the **deletion of the dead alternate ML-provider scaffolding**, the **single-provider-framework clarification**, the **category-terminology rule**, and the **bounded guardrail amendments** those changes require. It became authoritative on that owner merge. **Owner authorization is recorded by the owner instruction that commissioned this decision** (the Mission A "Clean-Cut District Surface Consolidation" mission, 2026-07-18, issued by the owner), under the same convention FCP-GOV records (`factory-configurable-pipelines-v1.md:4`).
**Date:** 2026-07-18
**Type:** Scoped protocol-development governance decision (District implementation disposition + code-organizational relocation authorization + dead-code removal authorization). It changes **no** scoring value, **no** UWR profile, **no** Evidence V2 semantics, **no** canonical hash, **no** provider behavior, and **no** category contract.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` (canonical home `afi-config/codex/governance/droids/`), its `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md`, and `decisions/authority-districts-v0.1.md`. **Consumes (does not re-decide)** `decisions/object-identity-v0.1.md` (OBJ-GOV), `decisions/lifecycle-v0.1.md` (LIFE-GOV), `decisions/persistence-v0.1.md` (MONGO-GOV), `decisions/persistence-impl-v0.1.md` (MONGO-IMPL), `decisions/provider-byok-foundations-v0.1.md` (PBF-GOV), and the enrichment-category contract family delegated by FCP-GOV D-FCP-2. **Supersedes, in the exact bounded respects stated in D-DSC-2, D-DSC-3, and D-DSC-8 and nowhere else,** clauses of `factory-configurable-pipelines-v1.md` (FCP-GOV), `authority-districts-v0.1.md`, `district-2-m2-ratification-v0.1.md`, and the guardrail path coverage recorded in `uwr-runtime-consumption-v0.1.md` (RC-7). Honors, and does not touch, the reserved ATLAS-GOV and CHAIN-GOV scopes. Where this decision conflicts with the Charter, the Charter wins.
**Evidence basis:** a 10-agent read-only preflight verification (2026-07-18; authority-chain reconstruction + independent import/caller tracing; **input, not authority**; every load-bearing finding is restated inline with its citation because the workspace `reports/` area is unversioned), verified against clean `origin/main` trees at: `afi-reactor` @ `8b680ac`, `afi-governance` @ `e7a57cf`, `afi-docs` @ `9f51553`, `afi-config` @ `a1a1279` (read-only reference; not modified by this program). Key verified facts are restated in §1.
**Ledger slot:** None existed — no prior decision reserves a row for District-surface consolidation. FCP-GOV D-FCP-10 deliberately restated the fence without deciding disposition ("it neither ratifies, promotes, nor demotes any District surface", `factory-configurable-pipelines-v1.md:202`); this decision is the disposition decision that fence anticipated.

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these 8):**

1. **D-DSC-1** — the current-runtime authority record: one live executor; the D1 POC is not a second runtime.
2. **D-DSC-2** — District One disposition: the historical POC implementation is retired and deleted from the active tree; git history is the archive.
3. **D-DSC-3** — District Two disposition: the live provenance law relocates to a District-2-named location; relocation is organizational only; the reference emission wrappers retire with the POC.
4. **D-DSC-4** — shared-law extraction: the one live cross-boundary carrier type moves to a neutral module; the D1 lane taxonomy retires with the POC.
5. **D-DSC-5** — dead alternate ML-provider scaffolding is deleted.
6. **D-DSC-6** — provider-architecture clarification: `src/providers/` is the one current provider framework; no cutover is performed here.
7. **D-DSC-7** — category terminology: five current categories; no `social` sixth category; "pipehead" survives as stage-discipline vocabulary only.
8. **D-DSC-8** — bounded guardrail and acceptance-record amendments (RC-7-style act; status normalization of the three directly touched instruments).

**Does not decide (expressly):** any provider-runtime cutover (Mission B remains a separate future owner authorization); any sentiment or aiMl provider adapter; any Evidence V3; any change to Evidence V2 semantics, canonical hashing, hash projection, scorer/UWR behavior, category weights, UWR profiles, Mongo persistence, category contracts, or the analyst strategy; any API Atlas or endpoint work (ATLAS-GOV reserved); any deployment or secret provisioning; any District creation or deletion; any change to the Charter or the Pipehead Addendum.

---

## 1. Verified evidence restated (input, not authority)

The following facts were independently re-verified at the pinned commits (imports traced by file:line, not by prior report):

- **Exactly one live executor.** `class GraphExecutor` (`afi-reactor/src/pipeline/executor.ts:374`) is constructed in production exactly once (`src/config/runtimeComposition.ts:100` — "the ONE GraphExecutor the live endpoints score through", `:5-6`) and executed only via `src/services/graphScoringService.ts:94-103`, reached from both Reactor ingresses (`src/server.ts:215` `/api/webhooks/tradingview`; `:374` `/api/ingest/cpj`). `src/dag/` does not exist. The D1 pipehead harness (`src/pipeheads/harness.ts`) is reachable only from the demo CLI (`src/cli/run-pipehead-demo.ts`, no npm script) and `test/pipeheads/**`.
- **The live evidence path module-loads D1 files but calls none of their orchestration.** `src/evidence/reactorEvidenceRecord.ts:32` type-imports `InternalScoringResult` from `src/pipeheads/types.ts` (a D1 file); `src/pipeheads/provenance/builders.ts:34-35` value-imports `ANALYSIS_LANE_IDS` (D1 `types.ts`) and `isDegradedLaneResult`/`LANE_PROVISIONAL` (D1 `fanOut.ts`), which transitively module-loads all five D1 lanes. The live call path (`buildScoredSignalProjection`, `computeInputHash`, `computeScoredOutputHash`, `provenanceRecordRefFor`) **never invokes** any lane, fan-out, envelope, or replay function; the lane taxonomy has **no surviving live consumer** once the POC's emission surface retires.
- **Live District-2 provenance law** = `src/pipeheads/provenance/{types,canonicalHashV1,hashProjection,builders,schemaValidation}.ts`, reached from `src/server.ts` via `src/evidence/{reactorEvidenceRecord,submitScoredSignalEvidence}.ts`. `envelopePipehead.ts` and `provenancePipehead.ts` are demo/test-only (imported only by the D1 harness, the D1 barrel, and pipehead tests).
- **Dead alternate ML-provider scaffolding.** `src/aiMl/providers/{MLProviderRegistry,TinyBrainsProvider,types,index}.ts` has zero importers outside itself (sole external mention: a negative guard at `test/pipeheads/provisionalLanes.test.ts:251`). The live aiMl surface is `src/aiMl/tinyBrainsClient.ts` (live node `src/pipeline/nodes/aiml.ts`) and `src/aiMl/patternServiceClient.ts` (provider adapter), both retained.
- **No external consumer.** Across every other repository in the organization, zero code imports `src/pipeheads/**`, `MLProviderRegistry`, `TinyBrainsProvider`, `socialLane`, or the demo CLI. (The single stale reference anywhere, `afi-starters/self-hosted-pipeline/plugins/custom.plugin.ts:2`, targets the long-removed `src/types/dag.js`, was dead before this decision, and is untouched by it.)
- **Standing golden condition.** `afi-reactor/test/pipeheads/fixtures/golden.json` (sha256 `312da1180b0bd418c03f595093516ebdc755ba81465a0b526ace43d002126e06`) is bound by standing byte-stability conditions: `uwr-runtime-consumption-v0.1.md:175` (with the sha recorded at `:40`), `uwr-profile-pin-v0.1.md:161`, and `afi-config/schemas/uwr-profile/v0/README.md:26` (a mint-eligibility gate). The operative conditions name the literal path without commit-pinning the file.
- **`social` never reaches live evidence bytes.** The live `afi.scored-signal-evidence.v2` record carries the ScoredSignal v1 projection, the input/output-hash provenance record, the UWR profile stamp, and the composition ref — no lane identifiers. All identifier-level `social` usage is inside the D1 POC and its fixtures.

---

## 2. D-DSC-1 — Current runtime authority

**Decision.**

- The current manifest-driven `GraphExecutor` pipeline (`afi-reactor/src/pipeline/` + `src/config/runtimeComposition.ts` + `src/services/graphScoringService.ts`) is AFI's **sole signal-evaluation executor**. Both Reactor ingresses flow into it; no other executor exists or may be introduced without a new owner decision.
- The historical District-1 pipehead POC is **not a second runtime** and **no longer represents current intended implementation**. Its purpose — proving that a bounded, staged, deterministic evaluation path can run without becoming a source of financial truth — is fulfilled and its lesson is embodied by the live pipeline.
- **Pipehead-style stage discipline survives as an architectural principle implemented by the current pipeline nodes**: one node → one validated category result → exactly one result per category enforced at the merge (`src/pipeline/nodes/mergeEnrichedView.ts`) → one scorer-facing join → the canonical afi-core scorer → the District-2 evidence boundary. The principle is what the Addendum governs; the retired POC was one demonstration of it.
- The retired POC implementation itself is **not required to remain in the active tree**.

**Scope-guard.** Records authority already factually true at the pinned commits; changes no runtime behavior.

---

## 3. D-DSC-2 — District One disposition (retirement of the POC implementation)

**Decision.** The historical District-1 POC implementation in `afi-reactor` is **retired and deleted from the active tree**. This clause is a **new bounded removal authorization** in the D-FCP-9 style, and it **supersedes, prospectively and in exactly these respects**:

- FCP-GOV **D-FCP-10**'s fence bullets "they are **not deleted** (expressly excluded from D-FCP-9)" and "remain non-production/reference exactly as governed" (`factory-configurable-pipelines-v1.md:195-200`) — superseded for the D1 surface enumerated below and for the D2 organizational relocation in D-DSC-3;
- FCP-GOV **§12**'s non-authorization of "deleting or wiring the D1 pipeheads / D2 M2 surface" (`factory-configurable-pipelines-v1.md:233`) — superseded for **deletion/relocation only**; wiring any reference surface into the live executor remains unauthorized;
- FCP-GOV **D-FCP-9**'s exhaustive-list scope-guard (`factory-configurable-pipelines-v1.md:189`) — not stretched: this decision **is** the new list.

**Authorized for deletion (exhaustive; afi-reactor):**

1. D1 orchestration: `src/pipeheads/harness.ts`, `src/pipeheads/index.ts` (barrel).
2. D1 lane implementations: `src/pipeheads/lanes/**` (all six files, including `socialLane.ts` and `technicalIndicators.ts`).
3. D1 fan-out composition: `src/pipeheads/fanOut.ts` (after the D-DSC-4 verification that its taxonomy has no surviving consumer).
4. D1 normalization, scoring, validation, and clock machinery: `src/pipeheads/{normalizePipehead,scoringPipehead,schemaValidationPipehead,clock}.ts`.
5. D1 types: `src/pipeheads/types.ts` (after the D-DSC-4 carrier extraction).
6. The demo CLI: `src/cli/run-pipehead-demo.ts` (and the `src/cli/` directory if empty).
7. D1-only fixtures: `test/pipeheads/fixtures/{signal.uss.json,signal.invalid.uss.json,ohlcv.json,lanes/**}` — **expressly excluding `test/pipeheads/fixtures/golden.json`** (see D-DSC-3).
8. The D1-era test files under `test/pipeheads/` (all sixteen): the pure-D2 suites relocate or transfer with the provenance law per D-DSC-3/D-DSC-8 item 3; the remainder are deleted after their unique invariants are transferred.
9. D1-only build machinery: `tsconfig.pipeheads.json`, `scripts/esm-check-pipeheads.sh`.
10. Active documentation whose sole purpose is describing the retired implementation as current: `docs/PIPEHEAD_SYSTEM.md`, the `README.md` pipehead section, and the stale `AGENTS.md` entries presenting the POC, the demo CLI, `src/dags/`, or the dead ML-provider island as current.
11. Stale comments and imports referencing the deleted surfaces or the long-removed `src/dag`/`runPipelineDag`, within the files touched by this program.

**Git history and this accepted retirement decision provide historical preservation. No executable archive copy is required.** Per the D-FCP-9 doctrine (`factory-configurable-pipelines-v1.md:187`): no tombstones, no placeholder files, no deprecation stubs, no commented-out remains — and no `archive/`, `legacy/`, or `deprecated/` directory, no disabled feature flag, no compatibility façade, no retained demo package, no second reference executor.

**Documentation alignment (bounded).** The current-state documentation corrections this retirement requires are authorized, each limited to describing only the current architecture: in `afi-reactor`, the item-10 surfaces above; in `afi-docs`, the Districts/flow statements of `AFI_Full_Architecture.md`, the `ARCHITECTURE_STATUS.md` pipehead glossary row, and the stale orchestration-doctrine lines naming removed `src/dag(s)` surfaces; in `afi-protocol`, the README's District-1 implementation sentence. Historical reports, accepted decisions at their pinned commits, and the D-17 instrument are **not** rewritten; no archive copies of corrected documents are created.

**District registry record (prospective amendment of `authority-districts-v0.1.md` Part D, District 1 row).** District 1 — Signal Evaluation — **remains a registered District with its Addendum authority unchanged** (`AFI_DROID_PIPEHEAD_ADDENDUM` §9/§12/§13; the Addendum itself is untouched, per `authority-districts-v0.1.md:149`). What changes is the **implementation record only**: the District's current implementation is the live `GraphExecutor` pipeline (`afi-reactor/src/pipeline/` and its composition); the row's former implementation pin `afi-reactor (src/pipeheads/)` and status "IMPLEMENTED (non-production POC)" are superseded prospectively as a governance-ledger fact, **without rewriting that file** (the D2R:16/:167 convention). This is an implementation retirement, **not** a District retirement, a District scope change, or any promotion of the live pipeline to "production" status (the deployment posture is unchanged: nothing is deployed).

**Scope-guard.** Authorizes exactly this list. Nothing else is removed. The live pipeline, the provider framework, the evidence path, the scorer seam, the category contracts, and all governed schemas are untouched.

---

## 4. D-DSC-3 — District Two disposition (organizational relocation of the live provenance law)

**Decision.** The live District-2 provenance law relocates out of the misleading D1-oriented `src/pipeheads/` tree into a District-2-named location under the current evidence architecture:

| Surface | Old path | New path |
|---|---|---|
| D2 artifact types (incl. the OBJ-GOV-pinned canonical ScoredSignal reference realization) | `src/pipeheads/provenance/types.ts` | `src/evidence/provenance/types.ts` |
| Canonical hash v1 (`afi.hash.v1`) | `src/pipeheads/provenance/canonicalHashV1.ts` | `src/evidence/provenance/canonicalHashV1.ts` |
| Decimal hash projection | `src/pipeheads/provenance/hashProjection.ts` | `src/evidence/provenance/hashProjection.ts` |
| Live builders (projection, input/output hashes, provenance-record ref, forbidden-artifact-key guard) | `src/pipeheads/provenance/builders.ts` | `src/evidence/provenance/builders.ts` |
| D2 M1 schema validation (all nine governed artifact-kind validators) | `src/pipeheads/provenance/schemaValidation.ts` | `src/evidence/provenance/schemaValidation.ts` |

**Binding terms:**

1. **Relocation is organizational only.** District Two's authority and behavior are preserved. It is **forbidden under this decision** to change Evidence V2 semantics, the `afi.scored-signal-evidence.v2` record shape, canonical hash algorithms or serialization, hash projection rules, domain tags, the forbidden money-plane key set, scorer output projection, the persistence handoff, signal identity, or UWR profile stamping. The oracle byte-equivalence goldens and all canonical hashes must be byte-stable across the move; no golden may be regenerated.
2. **Ratification coverage re-recorded.** `district-2-m2-ratification-v0.1.md` ratified the D2 surface **by path at pinned commits** (`:44,:100`; `afi-reactor @ 9b56fb1`). This decision **re-records that prospective, non-production ratification at the new paths above** for the relocated law, under the same bounds: non-production/demo status preserved; no production enablement, persistence expansion, API exposure, or canonical-object declaration is added (D2R §8 gates remain in force); the `D-CHOICE-1a` bound on the `schemaValidation.ts` afi-config schema-load coupling (read-only, in-process validation) is preserved unchanged in behavior and scope. The historical authorization-gap record (DIST-01; D2R:36,:101) is **preserved exactly** — relocation neither cures nor launders it.
3. **Reference emission wrappers retire with the POC.** `src/pipeheads/provenance/{envelopePipehead,provenancePipehead}.ts` and the emission-only builder surface — the provenance-record, replay-profile, envelope, evidence-ref, source-disclosure, and enrichment-provenance builders; the enrichment-bundle hash helpers; and the demo identity/fixture constants (engine id/version, per-lane version pins, fixture source/dataset ids, strategy-view declarations, the reference-implementation note) — exist solely to demonstrate D1-style staged emission of the D2 artifact family and are reachable only from the retired harness/CLI/tests. They are **deleted with the POC**. (The live projection's analyst/strategy identity fallback constants, the forbidden-artifact-key guard, and the four live-called functions are the retained builder surface.) The canonical D2 artifact contracts remain, unchanged, the merged afi-config M1 schemas (`afi-config/schemas/provenance/v1/`), and the relocated `schemaValidation.ts` retains validators for **all nine** governed artifact kinds. No canonical contract loses coverage; only the non-canonical reference emitter retires.
4. **OBJ-GOV pin re-recorded.** `object-identity-v0.1.md:87` pins the canonical Scored Signal's reference realization to `src/pipeheads/provenance/types.ts:145-162`; that pin now reads onto the **same section of the relocated, content-identical** `src/evidence/provenance/types.ts` (prospective re-record; OBJ-GOV's selection itself is untouched).
5. **The governed golden stays at its governed path.** `test/pipeheads/fixtures/golden.json` remains **byte-identical at its current literal path**, satisfying the three standing byte-stability conditions (§1) **verbatim** — no re-pin of any UWR-GOV or afi-config condition is required or performed. A new guardrail (D-DSC-8) enforces its sha256 in CI. The golden is a governed byte-stability anchor, not an executable archive copy.
6. **The shared carrier extraction** (D-DSC-4) and the relocated live builders keep the live evidence construction **call-for-call identical**; a legacy re-export at the old `src/pipeheads/...` paths is **not permitted** (all internal importers are updated in the same change).

**Scope-guard.** Organizational relocation + reference-emitter retirement only. If the relocation cannot be completed with byte-stable evidence, hashes, and goldens, the change must not merge.

---

## 5. D-DSC-4 — Shared-law extraction and lane-taxonomy retirement

**Decision.**

- The one piece of genuinely shared cross-boundary law — the **`InternalScoringResult` scoring-carrier type** (consumed by the live evidence construction and the D2 projection builder) — is extracted **verbatim** from D1 `src/pipeheads/types.ts` into a neutral single-purpose module under the current evidence architecture (`src/evidence/analysis/internalScoringResult.ts`). No broad "shared"/"legacy"/"compat"/"common" module is created.
- The **D1 lane taxonomy retires with the POC**: `ANALYSIS_LANE_IDS` (`["technical-indicators","pattern-recognition","news","social","ai-ml"]`), `AnalysisLaneId`, `AnalysisLaneResult`, `AnalysisBundle`, `LANE_PROVISIONAL`, `isDegradedLaneResult`, and the `Pipehead<I,O>` stage interface. Preflight verified (§1) that after the reference emitters retire, **no live or surviving code consumes any of them**; they are not carried into the live tree, per the doctrine that an abstraction is not preserved merely because it exists. The five-lane completeness discipline is already enforced live at the merge node; the degraded-result discipline of the live pipeline is the executor's own fail-soft/error-isolation model, governed by FCP-GOV.
- Invariants transferred out of the retired D1 test suite (with their new enforcement site): forbidden-artifact-key law (relocated `builders.ts` + a focused relocated test); acyclic ScoredSignal↔ProvenanceRecord commitment (relocated builders header law + focused test); verbatim scoring projection (focused test); canonical-hash and projection determinism (relocated pure-D2 tests); golden byte-stability (D-DSC-8 sha guardrail); scoring authority — the Reactor invokes and never re-implements the canonical scorer/UWR — remains enforced by the live UWR guardrail suite and the oracle byte-equivalence goldens.

**Scope-guard.** One type moves; nothing else from D1 survives.

---

## 6. D-DSC-5 — Dead alternate ML-provider scaffolding deleted

**Decision.** `src/aiMl/providers/MLProviderRegistry.ts`, `src/aiMl/providers/TinyBrainsProvider.ts`, `src/aiMl/providers/types.ts`, and `src/aiMl/providers/index.ts` are **deleted**, together with any dead index exports, dead tests/mocks, dead configuration shapes, and comments describing that registry as current. Preflight verified zero callers (§1). **No alternate ML-provider registry is retained.** The live Tiny Brains HTTP client (`src/aiMl/tinyBrainsClient.ts`), the pattern service client (`src/aiMl/patternServiceClient.ts`), the live aiMl node, and the shared `TINY_BRAINS_URL` configuration seam are expressly **retained unchanged** (the env var is shared with live code and is not dead-registry-only).

**Scope-guard.** Dead-code deletion with trivial equivalence (no callers). No live aiMl surface changes.

---

## 7. D-DSC-6 — Current provider architecture (clarification)

**Decision.** `src/providers/` (registry, runtime, socket, records, secret resolution, redaction, output validation, and the technical/news/pattern reference adapters) is the **one current provider framework** and the intended sole future category-execution seam. Provider-backed category execution remains a **current-intent forward surface**: this decision binds **no** category node to a provider adapter, adds no remote provider, changes no credential kind, adds no dynamic loading or marketplace code, and changes no `ProviderInstanceRef` semantics. The five-lane provider-runtime cutover is **Mission B** — a separate future owner authorization that must precede any such wiring.

**Scope-guard.** Restates PBF-GOV/Mission-4 reality; authorizes nothing new.

---

## 8. D-DSC-7 — Category terminology

**Decision.**

- AFI has exactly **five current enrichment categories**: `technical`, `pattern`, `sentiment`, `news`, `aiMl` (FCP-GOV D-FCP-1 canonical namespace, unchanged).
- The historical **`social` label must not survive as a sixth category** or as a category identifier in current enrichment code (`src/pipeline/`, `src/providers/`, `src/enrichment/`). Its remaining occurrences at the pinned commit are D1-only and retire with the POC. (Frozen historical surfaces — governed schemas, USS v1.1 contract field documentation, accepted decisions, historical reports — are not rewritten.)
- **"Pipehead"** may continue to describe the bounded stage discipline historically or conceptually (the Addendum's own vocabulary), but must not be used to imply the retired D1 implementation remains active.

**Scope-guard.** Terminology only; no contract or schema changes.

---

## 9. D-DSC-8 — Bounded guardrail amendments and acceptance-record normalization

**Decision.** RC-7 (`uwr-runtime-consumption-v0.1.md:60,146,148`) provides that amending the standing UWR guardrail tests is a governance act. **This decision is that act**, for exactly these bounded amendments in `afi-reactor`:

1. The directory lists scanned by `test/guardrails/uwrProfileStamp.test.ts` and `test/guardrails/uwrRuntimeProfile.test.ts` — currently `["src/pipeheads","src/cli"]`, which become vacuous when those directories are deleted (both scans skip missing directories silently) — are updated to cover the relocated District-2 surfaces (`src/evidence/provenance`, `src/evidence/analysis`). The banned-identifier sets, the RC-6 `source` vocabulary and meaning, and every other RC-7 ban are **preserved unchanged**.
2. A new consolidation guardrail suite is added (and the jest allowlist amended to run it) enforcing exactly: no path beneath `src/pipeheads/` may return; no `MLProviderRegistry`/`TinyBrainsProvider` symbol may return; no second executor implementation may be introduced; no `social` category identifier may be introduced in current enrichment code; the relocated District-2 provenance imports no retired module; current runtime imports no demo/reference code; and `test/pipeheads/fixtures/golden.json` remains byte-identical (sha256 `312da1180b0bd418c03f595093516ebdc755ba81465a0b526ace43d002126e06`).
3. The D1-only test files enumerated in D-DSC-2 are removed **after** their unique invariants transfer (D-DSC-4); the pure-D2 tests relocate with the provenance law. No test is weakened, skipped, or repinned to pass.

**Acceptance-record normalization (directly touched instruments only).** The three accepted decisions this decision supersedes-in-part are merged and in force but still literally read "Status: Proposed". Following the repository's explicit acceptance-record convention (`research-institute-reference-services-v0.1.md:4`, recorded by commit `88304b8`; `uwr-runtime-consumption-v0.1.md:3`), their Status and closing-footer lines are normalized to record the acceptance facts (the same three-line pattern commit `88304b8` applied) — and nothing else in those files is rewritten:

- `authority-districts-v0.1.md` — accepted by merge of afi-governance PR #14 on 2026-07-14 (merge commit `1b15fd2`).
- `district-2-m2-ratification-v0.1.md` — accepted by merge of afi-governance PR #15 on 2026-07-14 (merge commit `65997fb`).
- `factory-configurable-pipelines-v1.md` — accepted by merge of afi-governance PR #21 on 2026-07-16 (merge commit `414beb9`).

No repository-wide status sweep is performed.

**Scope-guard.** Exactly the amendments above; any other guardrail change remains outside these pre-authorizations and requires its own decision (RC-7 rule restated).

---

## Explicit non-authorizations

This decision does **not** authorize:

- wiring any reference or provider surface into the live executor (the FCP-GOV §12 wiring ban **survives** this decision);
- the five-lane provider-runtime cutover, any sentiment/aiMl provider adapter, or making news/aiMl affect UWR (Mission B and later, each separately owner-gated);
- any change to scorer/UWR behavior, category weights, UWR profiles, or the analyst strategy;
- any change to Evidence V2, any Evidence V3, any canonical-hash or hash-projection change, any golden regeneration;
- any Mongo persistence change (MONGO-GOV/MONGO-IMPL invariants unchanged);
- any API Atlas, REST/MCP/RPC endpoint, or gateway-surface work (ATLAS-GOV reserved, untouched);
- any deployment, secret provisioning, or GCP resource;
- any archive directory, compatibility shim, dormant executable copy, or migration framework;
- any modification to `afi-config` (its schemas, KATs, README conditions, and the Charter/Addendum are consumed read-only and remain unchanged);
- deciding anything about District creation, deletion, or scope beyond the implementation-record amendment in D-DSC-2.

---

## Supersessions and interactions (every prior decision walked)

- **`factory-configurable-pipelines-v1.md` (FCP-GOV)** — superseded **only** as stated in D-DSC-2/D-DSC-3: the D-FCP-10 "not deleted / remain exactly as governed" fence bullets and the §12 "deleting … the D1 pipeheads / D2 M2 surface" non-authorization are replaced by this decision's bounded removal/relocation authorization; the D-FCP-9 scope-guard is respected (this is a new list, not a stretch of that one). Everything else in FCP-GOV — the five-category namespace, composition model, executor boundaries, contract delegation, registry mechanism, evidence v2 composition ref, no-demo-fallback rule, slot ledger — is **unchanged and in force**. The §12 **wiring** ban survives verbatim.
- **`authority-districts-v0.1.md`** — the Part D District-1 registry row's implementation pin/status is superseded prospectively per D-DSC-2, and the District-2 row's `afi-reactor` implementation pin now reads onto `src/evidence/provenance/` per D-DSC-3; the file is not rewritten (its own E.1 requirement — a governance decision for material scope change — is satisfied by this decision; Part F is honored: this decision was commissioned by the owner and becomes authoritative only on owner merge). The topology, precedence model, both Districts' authority sources, and the Addendum's standing are unchanged.
- **`district-2-m2-ratification-v0.1.md`** — its §2 enumerated ratification coverage is re-recorded at the relocated paths per D-DSC-3 (same non-production bounds; D-CHOICE-1a preserved; DIST-01 historical-gap record preserved verbatim); the retired reference emitters and D1 stage files leave the ratified-coverage record as retired history rather than active surface. Nothing else is re-opened; no M2 object becomes canonical.
- **`uwr-runtime-consumption-v0.1.md`** — consumed; RC-7's provision that guardrail amendment is a governance act is exercised by D-DSC-8 for exactly the listed amendments; RC-6 stamp semantics, the RC-3 flag posture, the `registries/uwr-profiles` string ban, and the golden byte-stability conditions are unchanged (the golden stays byte-identical at its literal pinned path).
- **`uwr-profile-pin-v0.1.md`** — unchanged; its golden byte-stability condition (`:161`) is honored verbatim at the unchanged path; no profile value, axis, weight, or KAT vector is touched.
- **`object-identity-v0.1.md` (OBJ-GOV)** — consumed; the canonical Scored Signal selection is unchanged; its reference-realization pin is re-recorded at the relocated path per D-DSC-3 item 4.
- **`persistence-v0.1.md` (MONGO-GOV) / `persistence-impl-v0.1.md` (MONGO-IMPL)** — unchanged; single store, afi-infra write ownership, idempotency, and the evidence submit path's behavior are untouched (the submit path's imports are repointed, call-for-call identical).
- **`lifecycle-v0.1.md` (LIFE-GOV)** — unchanged; SCORED remains the Reactor's submitted state; its at-decision-time evidence citations of pipehead files remain valid historical citations at their pinned commits.
- **`provider-byok-foundations-v0.1.md` (PBF-GOV)** — unchanged and restated by D-DSC-6; the provider socket, BYOK boundary, and adapter set are untouched.
- **`math-authority-v0.1.md`** — unchanged; kernels stay in afi-core/afi-math; nothing here touches math.
- **`research-institute-reference-services-v0.1.md` (INST-GOV)** — unchanged; the Institute's operator designation and ingress doctrine are untouched.
- **`mint-formula-bt-86b-alignment-v0.1.md`** — unchanged; no economic surface is touched (and the mint-eligibility golden gate is honored byte-identically).
- **Reserved ATLAS-GOV / CHAIN-GOV** — honored and untouched; no API Atlas exists and none is started.

---

**Accepted owner decision (afi-governance PR #24, merge commit `bebe839`). Authoritative upon owner merge.**
