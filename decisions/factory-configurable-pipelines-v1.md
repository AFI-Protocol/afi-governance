# AFI Factory Analyst-Configurable Pipelines v1 (FCP-GOV)

**Slot:** `AFI-GOV-FACTORY-CONFIGURABLE-PIPELINES-v1` (FCP-GOV)
**Status:** **Proposed** for owner approval. This decision records the owner's settled decisions establishing the **configurable analysis-pipeline composition model** for the span between canonical USS validation and scoring: the **canonical five-category namespace**, the **composition model and its executor boundaries**, the **express delegation** of the V1 contract/registry family to `afi-config`, the **repository roles**, the **generic registration rule**, **pipeline and analyst-execution identity**, the **scored-evidence v2 composition reference and hash-domain tags**, the **no-demo-fallback runtime rule**, the **bounded removal authorization**, the **unchanged District fences**, and the **bounded implementation-slot ledger**. It becomes authoritative **only** when the owner merges it; until merged, it is a draft with no force. **Owner authorization for the §13 slot merges is recorded by the owner instruction that commissioned this decision** — each slot merges when its gates (D-FCP-11) pass; no per-slot row flip is required.
**Date:** 2026-07-16
**Type:** Scoped protocol-development governance decision (configurable pipeline composition / contract delegation / bounded implementation program). Records settled owner decisions; it is **not** a constitution and decides nothing beyond its eleven clauses.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` (canonical home `afi-config/codex/governance/droids/`), its `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md`, and `decisions/authority-districts-v0.1.md`. **Consumes (does not re-decide) `decisions/object-identity-v0.1.md` (OBJ-GOV), `decisions/lifecycle-v0.1.md` (LIFE-GOV), `decisions/persistence-v0.1.md` (MONGO-GOV), and `decisions/persistence-impl-v0.1.md` (MONGO-IMPL).** Coordinates with (does **not** override) `uwr-profile-pin-v0.1.md`, `uwr-runtime-consumption-v0.1.md`, `math-authority-v0.1.md`, and `district-2-m2-ratification-v0.1.md`. Where this decision conflicts with the Charter, the Charter wins.
**Evidence basis:** the verified read-only reconciliation report `reports/afi-configurable-dag-live-runtime-reconciliation.md` (2026-07-16; 8 investigators + 3 adversarial verifiers; **input, not authority**; it lives in the unversioned workspace `reports/` area, so every finding this decision relies on is restated inline with its citation rather than referenced), pinned at: afi-reactor @ `a5b3376`, afi-core @ `4863abda`, afi-infra @ `43aab585`, afi-config @ `1d38944`, afi-factory @ `9f39fa2`-era tree, afi-governance @ `1827031` (all 10 accepted decisions read in full). Its governance verdict — no accepted decision forbids analyst-configurable enrichment composition between `VALIDATED` and `SCORED`, and the interior of that span is deliberately unclaimed (lifecycle-v0.1.md carve-out of "intermediate/DAG state"; persistence-v0.1.md §5 operational classification; math-authority-v0.1.md's assignment of strategy/pipeline composition to the implementation layer) — was adversarially re-verified.
**Ledger slot:** None existed — no prior decision reserves a row for configurable composition; LIFE-GOV fixes only the lifecycle endpoints and MONGO-GOV classifies intermediate DAG state as operational storage. This decision fills that deliberately unclaimed interior with a bounded composition model and creates the missing implementation-slot ledger (§13).

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these eleven):**
1. the **canonical five-category analysis namespace** (D-FCP-1);
2. the **configurable composition model** and its executor boundaries (D-FCP-2);
3. the **express delegation** of the V1 contract/registry family to `afi-config` (D-FCP-3);
4. the **repository roles** for authoring, runtime, kernels, persistence, and gateway (D-FCP-4);
5. the **generic registration rule** for conforming participants (D-FCP-5);
6. **pipeline identity** and **analyst execution identity** (D-FCP-6);
7. the **scored-evidence v2 composition reference** and new canonical-hash domain tags (D-FCP-7);
8. the **no-production-demo/mock/fallback** runtime rule (D-FCP-8);
9. the **bounded removal authorization** for superseded scaffolding (D-FCP-9);
10. that **District fences are unchanged** (D-FCP-10);
11. the **bounded implementation slots and their gates** (D-FCP-11, ledger §13).

**Does NOT decide (reserved to their own scoped decisions; see §12):** post-`SCORED` lifecycle phases or their wiring (certification, qualification, challenge, finalization, epoch eligibility — LIFE-GOV, consumed as-is); rewards / mint / settlement / claims / receipts (CHAIN-GOV); API Atlas / Gateway endpoint authority (ATLAS-GOV); District scope changes; **scoring law values** of any kind; the **UWR pinned profile values** (UP-1…UP-12 unchanged); the `uwr-runtime-consumption-v0.1.md` **RC-3 flag default flip** (expressly NOT included here); regeneration of any golden (UP-5 goldens stay **byte-stable** as acceptance criteria).

**Nature of the act.** This decision establishes protocol-development law (its clauses) **and** conveys a bounded implementation authorization: the §13 slots are authorized by the owner instruction that commissioned this decision, gated per D-FCP-11. It follows MONGO-GOV's delegation pattern (D-MONGO-2) for the contract family and the `uwr-runtime-consumption-v0.1.md` RC-12 ledger pattern for the slots — with the RC-12 activation mechanism replaced by the commissioning instruction (§13). Shipped code remains tier-4 reality until it conforms; in-code self-labels confer nothing (`authority-districts-v0.1.md` Part B.1).

---

## 1. D-FCP-1 — canonical five-category analysis namespace

**Decision.** The canonical analysis-category namespace is **exactly five categories**, with these **exact strings** in every external JSON contract (manifests, registries, plugin declarations, evidence references, vectors):

`technical`, `pattern`, `sentiment`, `news`, `aiMl`

These are the strings already typed by the live enrichment surface (afi-core `analysts/froggy.enrichment_adapter.ts:43-70`, per the evidence basis). Competing aliases — including `social` and `ai-ml` — are **not part of current contracts**: no external JSON contract under this program may emit, accept, or map them as category identifiers. This clause closes the previously OPEN lane-id namespace (the evidence basis's EP-O1 note: governance counted "five analysis lanes" without naming them, `authority-districts-v0.1.md:95,100`).

**Scope-guard.** Fixes the **category identifier strings** only. It does not fix category *semantics*, plugin implementations, presets, or parameters (implementation, validated per D-FCP-2/D-FCP-3), and does not add or remove categories (a future decision).

---

## 2. D-FCP-2 — configurable composition model and executor boundaries

**Decision.** Between canonical USS validation and scoring, a **pipeline graph** may compose registered analysis plugins as follows:

1. **Selection** — the graph may select **any subset** of registered analysis plugins (registration per D-FCP-5); no category is mandatory.
2. **Multiplicity** — **multiple nodes of the same category** are permitted in one graph.
3. **Ordering** — nodes may execute **sequentially or concurrently**; concurrency is derived from the dependency structure, never assumed.
4. **Dependencies** — inter-node dependencies are **explicit** in the manifest (`dependsOn`-style edges); no implicit ordering.
5. **Conditional branches** — permitted only as a **bounded declarative predicate tree** evaluated over declared node inputs/outputs; **no `eval`, no arbitrary code, no user-supplied executable expressions** in any manifest.
6. **Joins** — multi-parent joins are **deterministic**: a defined, order-independent merge over the declared parent outputs.
7. **Parameters** — per-node parameters are **schema-validated** against the plugin's declared parameter contract (D-FCP-3) before execution.

**Executor boundaries (hard):**

- **Ingestion and canonical USS validation stay OUTSIDE the graph.** The graph begins only after the `INGESTED → VALIDATED` transition (LIFE-GOV D-LIFE-3, Ingest validator).
- **Canonical persistence stays OUTSIDE the graph executor.** Evidence submission goes through the afi-infra canonical persistence interface (MONGO-GOV D-MONGO-3), never from a graph node.
- **Exactly ONE registered scorer terminates a valid scoring pipeline** and performs the **sole `VALIDATED → SCORED` transition** — consistent with the LIFE-GOV D-LIFE-2/D-LIFE-3 transition monopoly (one owning authority per transition). A manifest with zero or multiple scorer terminals is invalid.
- **Enrichment/graph nodes may not create lifecycle transitions and may not write canonical evidence.** Node outputs are operational intermediate state (MONGO-GOV D-MONGO-4) until the scorer terminal and the evidence path consume them.

**Scope-guard.** Fixes the **composition model and its boundaries** only. It does not select an executor implementation (D-FCP-4 assigns the runtime role; the executor is replaceable), does not define manifest byte-level fields (delegated, D-FCP-3), and does not alter any lifecycle phase, owner, or state name (LIFE-GOV, consumed).

---

## 3. D-FCP-3 — express delegation of the V1 contract/registry family to afi-config

**Decision.** Exercising `authority-districts-v0.1.md` Part C's provision that `afi-config` is the canonical schema/registry home **where expressly delegated**, and following the delegation model of `persistence-v0.1.md` D-MONGO-2 (which so delegated the evidence contract), this decision **expressly delegates to `afi-config`** as canonical home the following V1 contract/registry family:

**Schema contracts:**
- `afi.pipeline.v1` — the pipeline manifest (graph, nodes, edges, predicates, parameters);
- `afi.pipeline-template.v1` — reusable pipeline templates;
- `afi.analysis-plugin.v1` — plugin declaration (category per D-FCP-1, parameter contract, version);
- `afi.analyst-strategy-config.v1` — analyst strategy configuration;
- `afi.analyst-strategy-registration.v1` — analyst/strategy registry entry shape;
- `afi.provider-strategy-binding.v1` — provider-to-strategy binding;
- `afi.composition-ref.v1` — the thin composition reference carried on evidence (D-FCP-7);
- `afi.scored-signal-evidence.v2` — the evidence contract's new version (D-FCP-7), superseding `.v1` per that contract's own change-control rule (§11).

**Registries:**
- the **analyst-strategy registry**;
- the **registered pipeline-manifest registry**;

**plus their validation vectors/KATs** (positive and negative, same conventions as the existing evidence-contract and UWR-profile vector suites).

`afi-config` holds these as **governed contracts**: it gains no authority to change what the clauses of this decision fix (namespace, boundaries, identity composition); shape changes beyond this decision require new governance per the change-control discipline (§11).

**Scope-guard.** Delegates the **contract/registry home** only. Byte-level schema authoring is SLOT-FCP-CONFIG implementation; this clause fixes the family's names, home, and governed status, not its field lists.

---

## 4. D-FCP-4 — repository roles

**Decision.** Roles under this program, consistent with `authority-districts-v0.1.md` Part C:

- **`afi-factory`** — the **replaceable authoring implementation**: pipeline/template authoring, template instantiation, manifest validation tooling, and canonical hashing utilities. It is **not a protocol authority** and **not the live executor**; nothing it emits is canonical until validated against the delegated `afi-config` contracts.
- **`afi-reactor`** — **AFI's governed, replaceable runtime**: identity resolution, manifest loading, plugin binding, graph execution, scorer invocation, UWR/decay resolution, composition provenance, evidence construction, and **submission through the afi-infra canonical persistence interface** (MONGO-GOV D-MONGO-3 — submitter, not writer).
- **`afi-core`** — keeps the **deterministic scoring/enrichment kernels**. Kernel math stays where it is; the program composes kernels, it does not move or reimplement them (math-authority posture unchanged).
- **`afi-infra`** — keeps the **canonical store and authoritative validation** (MONGO-GOV D-MONGO-2/D-MONGO-3): the sole canonical evidence persistence interface and mutation path, now validating `afi.scored-signal-evidence.v2` submissions authoritatively.
- **`afi-gateway`** — **authenticates and routes only**; it **never constructs and never writes canonical evidence** (unchanged from MONGO-GOV).

**Scope-guard.** Assigns **roles** only; it grants no repo authority over identity, lifecycle, finality, scoring law, or economics (OBJ-GOV / LIFE-GOV / UWR decisions / CHAIN-GOV, all unchanged).

---

## 5. D-FCP-5 — generic registration rule

**Decision.** Adding a **conforming** analyst, strategy, strategy version, pipeline, scorer plugin, UWR profile, or provider binding to the delegated registries (D-FCP-3) is an **administrative, schema-validated, reviewable, versioned registry update authorized under THIS decision** — it does **NOT** require a new governance decision per participant.

Runtime obligations (hard):
- the runtime **fails closed** for unknown, unregistered, or inactive identities — an unrecognized identity **refuses to execute**, never degrades;
- **no hardcoded identity conditionals** in runtime code (no `if (analystId === "…")` gates);
- **no silent identity fallback** — no defaulting to a known identity when resolution fails.

This clause **generalizes `uwr-profile-pin-v0.1.md` UP-10's registration requirement into a registry mechanism**: UP-10's recognition rule — "always registered and pinned, never silent" — is preserved exactly; what changes is that registration is now performed against the delegated registries rather than requiring a per-participant governance decision. **Official/default profiles may retain stronger governance metadata** (e.g. a governance-decision reference on the registry entry) than ordinary registered participants.

**Scope-guard.** Fixes the **registration mechanism and fail-closed rule** only. It does not register anyone (registrations are registry updates under SLOT-FCP-CONFIG conventions), does not change any pinned profile's values or status, and does not alter UP-10's recognition semantics for the existing pinned profile.

---

## 6. D-FCP-6 — pipeline identity and analyst execution identity

**Decision.**

- **Pipeline identity** is the triple **`pipelineId` + `pipelineVersion` + canonical `manifestHash`**, where `manifestHash` is computed by **canonical normalized-JSON hashing** and is **timestamp-free** (no volatile processing timestamps in the hashed material — District 2 hash doctrine).
- **Analyst execution identity** comprises:
  1. the **strategy triple `analystId` + `strategyId` + `strategyVersion`** — **OBJ-GOV D-OBJ-3, unchanged and consumed exactly**;
  2. the **`analystConfigHash`** (canonical hash of the resolved `afi.analyst-strategy-config.v1` document);
  3. the **registered scorer reference** (scorer plugin id + version, per D-FCP-5 registration);
  4. the **pipeline reference** (D-FCP-6 pipeline identity);
  5. the **UWR profile reference** (registered profile id/version — values untouched);
  6. the **decay/Greeks configuration reference**, or its **canonical inline configuration** where no registered reference exists.

**Scope-guard.** Fixes **identity composition** only. It does not re-open D-OBJ-3 (the triple's name/format are consumed, not re-decided), does not change any UWR or decay *value*, and leaves hash algorithm/serialization details to the delegated contracts (canonical-hash family, D-FCP-7).

---

## 7. D-FCP-7 — scored evidence v2: thin composition reference and hash-domain tags

**Decision.** The canonical evidence record gains a **thin canonical composition reference** — the `afi.composition-ref.v1` object — carried on **`afi.scored-signal-evidence.v2`**, containing exactly the composition identity fields:

`pipelineId`, `pipelineVersion`, `manifestHash`, `analystConfigHash`, `scorerPluginId`, `scorerPluginVersion`, `pluginSetHash`, `executionSummaryHash`, `enrichmentHash`

Rules:
- **Heavy node outputs stay operational** (MONGO-GOV D-MONGO-4), **hash-addressed** — the canonical record carries digests, never node payloads.
- **Execution summaries are timestamp-free in replay-critical material** (volatile processing timestamps are excluded from hashed content, per the District 2 timestamp policy).
- The following **canonical-hash domain tags are registered**, narrowing the canonical-hash contract's open domain-tag registry (**CH-O2**, `afi-config/schemas/provenance/v1/canonical-hash.schema.json`) **for these tags only** — CH-O2 remains otherwise open:
  `afi.d2.composition-manifest`, `afi.d2.analyst-config`, `afi.d2.plugin-set`, `afi.d2.execution-summary`, `afi.d2.enrichment-bundle`
- The **"composition" naming is deliberately distinct** from the three "provenance" meanings guarded by `district-2-m2-ratification-v0.1.md` §2.3 (the binding terminology guard: USS `provenance` ingest block / D2 M2 artifact surface / internal `bundle.provenance` intermediate). Nothing here conflates or renames any of the three.

**Scope-guard.** Fixes the **composition-reference composition, its carrier version, and the five registered tags** only. Byte-level `.v2` schema authoring is SLOT-FCP-CONFIG/SLOT-FCP-INFRA implementation under the change-control rule (§11); no other CH-O2 tag is decided; no provenance-record field is mutated (see §11 on PR-O1).

---

## 8. D-FCP-8 — no production demo/mock/synthetic/offline fallback

**Decision.** The runtime under this program contains **no production demo, mock, synthetic, or offline fallback path**:

- **missing required configuration or infrastructure fails honestly** — a load, resolution, or connection failure refuses to proceed and surfaces the failure (the MONGO-GOV D-MONGO-8 posture, generalized to composition inputs);
- **optional nodes degrade only per a declared fail-soft policy** in the manifest, and every such degradation is **recorded** (in the execution summary) — never silent;
- no code path substitutes demo prices, mock enrichment, or synthetic data in production execution.

**Scope-guard.** Fixes the **runtime failure/degradation contract** only; test harnesses, fixtures, and the SLOT-FCP-ORACLE test-only oracle are unaffected (they are not production paths).

---

## 9. D-FCP-9 — bounded removal authorization (after gates pass)

**Decision.** The following removals are **authorized, to be executed only after the D-FCP-11 gates pass** for the slots that replace each item (executed under SLOT-FCP-CLEANUP; evidence-basis citations pinned in the header):

In `afi-reactor`:
1. the **dead `src/dag/` scaffold** (DAGBuilder/DAGExecutor/PluginRegistry — zero production callers), its **mock plugins**, and the dead **`AnalystNode`/afi-factory dynamic import**;
2. the **dead linear `runPipeline`** (`src/services/pipelineRunner.ts:161-309`, tests-only);
3. the **duplicated `types/dag.ts` + `types/pipeline.ts` contracts** (superseded by the delegated `afi.pipeline.v1` family);
4. the **hardcoded `FROGGY_TREND_PULLBACK_PIPELINE`** constant and the **combined category plugins** it binds;
5. the **hardcoded Froggy identity gates** — including the `src/config/uwrProfilePin.ts` froggy-only stamp gate, **replaced by registry-backed stamping** (D-FCP-5; stamp semantics per RC-6 unchanged in meaning);
6. the **`cpj-ingested` strategy assignment** (static strategy selection at ingest);
7. the **hardcoded `swing` decay selection** (`pickDecayParamsForAnalystScore` hardcoded holdingHorizon), replaced by the D-FCP-6 decay configuration reference;
8. **production demo price-source support** (per D-FCP-8).

In `afi-config`:
9. the **superseded draft topology schemas**: `pipeline.schema.json`, `blueprint.schema.json`, `analyst-config.schema.json`, `definitions/enrichment-node.schema.json` (superseded by the D-FCP-3 family).

**Git history is the archive — no tombstones.** No placeholder files, no deprecation stubs, no commented-out remains.

**Scope-guard.** Authorizes **exactly this list**, and only after the replacing slots' gates pass. Nothing else is removed; in particular the District-1 pipeheads and the D2 M2 surface are **not** on this list (D-FCP-10).

---

## 10. D-FCP-10 — District fences unchanged

**Decision.** District boundaries are untouched:

- the **District-1 pipeheads** and the **District-2 M2 surface** (`src/pipeheads/`, including `src/pipeheads/provenance/`) remain **non-production/reference** exactly as governed (`district-2-m2-ratification-v0.1.md`);
- they are **not wired into the live executor** by this program;
- they are **not deleted** (expressly excluded from D-FCP-9);
- **no District scope change** is made or implied.

**Scope-guard.** Restates the fence; it neither ratifies, promotes, nor demotes any District surface.

---

## 11. D-FCP-11 — bounded implementation slots and gates

**Decision.** The program executes as the bounded slots ledgered in §13 (RC-12-style rows). **Gates — every slot merges only when all of the following hold:**

1. the slot's **CI is green** in every touched repo;
2. the program's **equivalence/configurability gates pass**: the SLOT-FCP-ORACLE behavioral oracle proves the configured default graph reproduces the current live workflow (equivalence), and the configurability acceptance vectors pass (subset selection, same-category multiplicity, concurrency, conditional branch, multi-parent join — per D-FCP-2). **Sequencing rule:** gate 2 binds each slot **from the earliest slot at which its subject exists** — for SLOT-FCP-CONFIG/ORACLE/FACTORY/INFRA/CORE it requires only that slot's own vectors/suites (the configured default graph does not yet exist); it is a **hard precondition for SLOT-FCP-REACTOR's production switch and for SLOT-FCP-CLEANUP** in full;
3. **no accepted decision is contradicted** — in particular: UP-5 goldens **byte-stable**, `uwrScore 0.1875` anchor intact, no scored *value* changes anywhere, LIFE-GOV transition ownership intact, MONGO-GOV write boundary intact;
4. the PR body names its slot.

**Activation.** Owner authorization for these slot merges is **recorded by the owner instruction that commissioned this decision**; acceptance of this decision (owner merge) makes that authorization effective. No per-slot row flip is required (deliberate difference from RC-12, recorded here so the ledger never misleads). Any work **outside** a slot's scope column, or violating a gate, exceeds its authorization and must be rejected.

**Scope-guard.** Creates the ledger and gates only; slot internals (module paths, schema fields, test names) are implementation, bounded by the clauses above.

---

## 12. Explicit non-authorizations

This decision does **not** authorize, decide, ratify, or pre-empt any of the following; each remains for its own scoped decision:

- **post-`SCORED` lifecycle** — certification, qualification (the gate stays unwired), challenge, finalization, epoch eligibility, or any finality-writer wiring (LIFE-GOV, consumed as-is);
- **rewards / mint / settlement** — mint, reward routing, payout, staking, claims, receipts, epoch settlement/emissions, on-chain anchoring (CHAIN-GOV);
- **ATLAS-GOV** — any API/endpoint/route/query surface, including read/replay/verify endpoints over evidence;
- **District scope changes** of any kind;
- **scoring law values** — no weight, threshold, decay parameter, or scored value changes; no production scoring law;
- **UWR pinned profile values** — `uwr-weighted-lifts-v0.1` (UP-1…UP-12) unchanged; UP-8 decay canonicality stays OPEN, neither resolved nor prejudiced;
- the **RC-3 source-flag default flip** (`uwr-runtime-consumption-v0.1.md`) — expressly **NOT** included in this program;
- **golden regeneration** — the UP-5/D2 M2 goldens stay byte-stable and are acceptance criteria (D-FCP-11 gate 3), never regenerated under this program;
- **deleting or wiring the D1 pipeheads / D2 M2 surface** (D-FCP-10);
- **new canonical stores or store-shape changes** beyond the `afi.scored-signal-evidence.v2` version defined here (MONGO-GOV invariants — single store, afi-infra write ownership, idempotency by `signalId` — all unchanged);
- **registering any specific participant** — D-FCP-5 creates the mechanism; each registration is a registry update, reviewed on its own PR.

---

## 13. Implementation-slot ledger

Authorization for every row below is conveyed per D-FCP-11 (owner instruction recorded; effective on owner merge of this decision; merge gated on D-FCP-11 gates). Proposed execution order: top to bottom.

| Item | Repo | Scope | Authorized? |
|---|---|---|---|
| **SLOT-FCP-CONFIG** | afi-config | The D-FCP-3 contract family (`afi.pipeline.v1`, `afi.pipeline-template.v1`, `afi.analysis-plugin.v1`, `afi.analyst-strategy-config.v1`, `afi.analyst-strategy-registration.v1`, `afi.provider-strategy-binding.v1`, `afi.composition-ref.v1`, `afi.scored-signal-evidence.v2`), the analyst-strategy and pipeline-manifest registries, validation vectors/KATs; D-FCP-1 strings exact | Yes — per D-FCP-11 activation |
| **SLOT-FCP-ORACLE** | afi-reactor | Behavioral-oracle harness capturing the current live workflow as the equivalence baseline — **test-only**, no production code | Yes — per D-FCP-11 activation |
| **SLOT-FCP-FACTORY** | afi-factory | The D-FCP-4 authoring system: template authoring, instantiation, manifest validation, canonical hashing (D-FCP-6 rules) | Yes — per D-FCP-11 activation |
| **SLOT-FCP-INFRA** | afi-infra | Authoritative `afi.scored-signal-evidence.v2` validation at the canonical persistence interface (MONGO-GOV boundary unchanged) | Yes — per D-FCP-11 activation |
| **SLOT-FCP-CORE** | afi-core | Minimal kernel exports **only if genuinely required** for plugin binding; no kernel math changes; empty slot if not required | Yes — per D-FCP-11 activation |
| **SLOT-FCP-REACTOR** | afi-reactor | Manifest-driven executor (D-FCP-2 model), five category nodes (D-FCP-1), identity/registry resolution (D-FCP-5/D-FCP-6), composition provenance + evidence construction (D-FCP-7), the production switch to the configured default graph (equivalence-gated) | Yes — per D-FCP-11 activation |
| **SLOT-FCP-GATEWAY** | afi-gateway | CI/dependency hygiene **only** (e.g. the afi-factory `file:` install-time coupling); no evidence construction, no routing semantics changes | Yes — per D-FCP-11 activation |
| **SLOT-FCP-CLEANUP** | afi-reactor, afi-config | The D-FCP-9 removals, exactly as listed, plus guardrails preventing reintroduction (hardcoded-identity bans per D-FCP-5) | Yes — per D-FCP-11 activation (after the replacing slots' gates pass) |
| **SLOT-FCP-DOCS** | afi-docs / repo docs | Documentation of the shipped composition model and contract family; no normative additions beyond this decision | Yes — per D-FCP-11 activation |

---

## 14. Supersessions and interactions

- **OBJ-GOV / LIFE-GOV / MONGO-GOV (+ MONGO-IMPL)** — **consumed, not re-decided.** The D-OBJ-3 strategy triple is used exactly (D-FCP-6); the D-LIFE-2/D-LIFE-3 phase separation and transition monopoly are the source of the one-scorer-terminal rule (D-FCP-2); the MONGO-GOV store/write-boundary/idempotency invariants are untouched, and `afi-infra`'s D-MONGO-3 interface remains the sole canonical write path (D-FCP-4).
- **CH-O2** (`canonical-hash.schema.json` open domain-tag registry) — **narrowed for the five named tags only** (D-FCP-7): `afi.d2.composition-manifest`, `afi.d2.analyst-config`, `afi.d2.plugin-set`, `afi.d2.execution-summary`, `afi.d2.enrichment-bundle`. CH-O2 remains open for all other tags.
- **PR-O1** (`provenance-record.schema.json` open question on enrichment-hash binding) — **narrowed only insofar as composition identity lives in a NEW `afi.composition-ref.v1` object rather than any provenance-record mutation.** No `afi.provenance-record.v1` field is added, changed, or reinterpreted; PR-O1's own question (per-lane list vs single bundle hash) is not otherwise resolved here.
- **Evidence contract change-control** — the `afi.scored-signal-evidence` v1 README's rule ("any shape change requires a new governance decision and a new schema version — never a silent mutation") is followed exactly: the **new decision is this one**; the **new version is `.v2`**. The `.v1` contract is superseded on `.v2` adoption per that rule; existing `.v1` records are not rewritten.
- **`uwr-profile-pin-v0.1.md`** — unchanged; UP-10's registration requirement is **generalized into the D-FCP-5 registry mechanism** (recognition still "always registered and pinned, never silent"); no profile value, axis, weight, or KAT vector is touched; UP-5 goldens are byte-stable gates.
- **`uwr-runtime-consumption-v0.1.md`** — its ledger and RC-3 flag default are not advanced (RC-3 flip expressly excluded, §12); its RC-6 stamp-semantics meaning is preserved while the froggy-only stamp gate is replaced by registry-backed stamping (D-FCP-9 item 5). Because RC-7 provides that amending the standing guardrail test is a **governance act**, **this decision is that act** for one further bounded amendment: `afi-reactor test/guardrails/uwrProfileStamp.test.ts` may be amended under SLOT-FCP-REACTOR **solely** to recognize registry-backed (D-FCP-5) stamp resolution in place of the froggy-only identity gate — the RC-6 `source` discriminator vocabulary and meaning, the `registries/uwr-profiles` string ban across `src/`, and the `src/pipeheads` + `src/cli` pin-identifier bans are all **preserved unchanged**.
- **`district-2-m2-ratification-v0.1.md`** — unchanged; its §2.3 terminology guard is respected by the deliberate "composition" naming (D-FCP-7); its ratified surface stays fenced (D-FCP-10).
- **`math-authority-v0.1.md`** — unchanged; kernels stay in afi-core/afi-math; this program composes, it does not redefine math.

---

**Proposed for owner approval. Authoritative only upon owner merge.** This decision fixes the five-category namespace, the configurable composition model and its executor boundaries, the express afi-config delegation of the V1 contract/registry family, the repository roles, the generic registration rule, pipeline and analyst-execution identity, the scored-evidence v2 composition reference and its hash-domain tags, the honest-failure runtime rule, the bounded removal list, the unchanged District fences, and the gated slot ledger — and nothing else. It touches no post-SCORED lifecycle, no rewards/mint/settlement, no ATLAS-GOV surface, no District scope, no scoring-law value, and no UWR pinned profile value; the RC-3 default flip is not included; UP-5 goldens stay byte-stable.
