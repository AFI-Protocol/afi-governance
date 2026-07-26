# AFI Constitutional Architecture v1.0 (CONST-GOV)

**Slot:** `AFI-GOV-CONSTITUTION-v1.0` (CONST-GOV)
**Status:** **Accepted** owner decision — accepted by merge of afi-governance PR #30 on 2026-07-26 (merge commit `7adf52c`, merged unedited). It ratifies a **canonical three-layer constitutional framing** of AFI — (1) **AFI Protocol** primitives, (2) **AFI Research Institute** replaceable reference implementations and non-exclusive reference services, (3) externally-owned **Registered Applications** — records the canonical/retired terminology, and records the owner's classification ruling that **Proof-of-Intelligence (PoI)** and **Proof-of-Insight (PoInsight)** are two distinct **reserved** reputation primitives. It **re-decides nothing** owned by a prior decision, authorizes **no** implementation, and touches **no** reserved domain.
**Date:** 2026-07-25 (draft authored)
**Type:** Scoped protocol-development governance decision (constitutional framing / layer taxonomy / terminology record / classification ruling). Docs and governance-ledger only; it authorizes **no** implementation, schema, route, runtime, deployment, infrastructure, credential, or economic act, and decides nothing beyond its eight clauses.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` (canonical home `afi-config/codex/governance/droids/`), its `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md`, and `decisions/authority-districts-v0.1.md`. **Consumes and frames (does not re-decide)** all nineteen prior accepted decisions (enumerated in §11); every primitive named here retains its existing owner and definition unchanged. For the District-framing, non-production, and no-financial-truth invariants it defers to `decisions/current-authority-reroot-and-golden-closure-v0.1.md` (R1-GOV); District One's functional name is **Signal Evaluation** (R1-GOV D-R1-1). **Honors, and does not touch,** the reserved `ATLAS-GOV` (API/endpoint surface, incl. the Gateway endpoint) and `CHAIN-GOV` (rewards / mint / settlement / on-chain / economic activation) scopes. Where this decision conflicts with the Charter, the Charter wins; where it conflicts with any accepted decision, **that decision wins** and this framing is corrected (D-CONST-8).
**Evidence basis:** the verified constitutionalization pass and its three companion reference documents in the unversioned workspace `reports/` area (`afi-constitutional-architecture-v1.0.md`, `afi-city-ontology-specification-v1.0.md`, `afi-component-classification-registry-v1.0.md`) and the prior `afi-ecosystem-architecture-assessment-v0.1.md` — **input, not authority**; because `reports/` is unversioned, every framing this decision relies on is stated inline in its clauses. Pinned at: afi-governance @ `166c740` (all nineteen prior accepted decisions read in full), afi-config @ `7423566`, afi-core @ `24513f4`, afi-reactor @ `f53f171`, afi-infra @ `6417eae`, afi-gateway @ `a8038e2`, afi-docs @ `a572035`, afi-math @ `5247e41`, afi-mint @ `eba0d93`, afi-token @ `0d3de3c`, afi-econ @ `471f4fe`, afi-tiny-brains @ `712e2ff`, afi-benchkit @ `76cde01`, afi-protocol @ `01d8728`, afi-artifacts @ `ba12307`, afi-xerc20 @ `b34ba57`, afi-web @ `64ffdfa`. The classification was verified against live schemas/code (e.g. `afi.scored-signal-evidence.v3` sole evidence contract; UWR the live scoring rule; PoI/PoInsight encoded as analyst-level reputation metrics in `afi-core/validators/ValidatorDecision.ts`, `afi-core/schemas/validator_metadata_schema.ts`) and the nineteen decisions. The owner classification ruling on PoI/PoInsight was given 2026-07-25.
**Ledger slot:** None existed — no prior decision states AFI's layer taxonomy, the reference-implementation-vs-primitive framing, the canonical/retired terminology register, or the PoI/PoInsight classification as a governance fact. This decision opens the constitutional-framing slot. It creates **no** implementation-slot authorization and consumes (does not re-decide) every prior decision's owned scope.

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these eight):**
1. the **three-layer constitutional model** (Protocol primitives / Institute reference implementations & services / Registered Applications) and the **identity test** as the canonical classifier (D-CONST-1);
2. **ratification of the three companion reference documents** as the canonical constitutional reference, as governance-ledger doctrine (D-CONST-2);
3. the **role → reference-implementation → hosted-instance pattern**, with **replaceability** and Institute **non-exclusivity** (D-CONST-3);
4. the **naming registers and the retired-terminology register** (D-CONST-4);
5. the **PoI / PoInsight classification** as two distinct **reserved** reputation primitives, per the owner ruling (D-CONST-5);
6. the **Registered Application layer**, its criteria, and the **reserved** applications registry (D-CONST-6);
7. the **component-placement decision framework** for future components (D-CONST-7);
8. **reserved-domain honoring, precedence, and amendment** (D-CONST-8).

**Does NOT decide (reserved to their own scoped decisions / owners; see §10–§11):** the **shape or semantics** of any schema or contract (USS, CPJ, Evidence V3, provenance, provider-strategy-binding, identity, enrichment categories — owners unchanged, delegated to `afi-config` by FCP-GOV D-FCP-3); any **UWR / scoring / math / evidence / provenance / lifecycle / persistence** rule (their existing owners, unchanged); any **PoI / PoInsight formula, reputation weighting, or reputation math**, and any **mint / rewards / settlement / emissions / economic activation** of PoI/PoInsight or anything else (**CHAIN-GOV**, reserved and unfiled); any **API / endpoint / route / query surface**, including the Gateway endpoint contract and any read/replay/verify surface (**ATLAS-GOV**, reserved and unfiled); the **`afi.registered-application.v1`** schema, registry, or any registration record (its own future decision, `registered-application-v0.1`); any **repository, service, schema, or field rename**; any **cleanup edit** to discarded-terminology residue (owner-driven backlog, not authorized here); any **deployment, infrastructure, credential, or funding** act; and the **registration of any specific participant, provider, application, or binding** (FCP-GOV D-FCP-5 already provides that mechanism).

**Nature of the act.** This decision establishes a **constitutional-framing governance record**: it names AFI's layers, fixes terminology, and records a classification ruling. It conveys **no implementation authorization** — there is no implementation-slot ledger, and nothing here permits code, schema, route, deployment, or economic change. In-code self-labels confer nothing (`authority-districts-v0.1.md` Part B.1); the framing confers nothing beyond what these clauses expressly say.

---

## 1. D-CONST-1 — the three-layer constitutional model and the identity test

**Decision.** AFI's architecture is canonically framed in three layers, distinguished by ownership and governance:

- **Layer 1 — AFI Protocol.** The set of **primitives**: governed roles, contracts, and rules such that *if any one changed fundamentally, AFI would no longer be the same protocol.* Governed exclusively by accepted `afi-governance` decisions (or held in a reserved governance domain). A primitive is a specification/contract, not a running service; nothing in this layer registers.
- **Layer 2 — AFI Research Institute.** The originating institution that builds governed, **replaceable reference implementations** of protocol roles and operates **non-exclusive reference services**. Building or operating reference infrastructure is **never protocol authority and never product ownership** (INST-GOV D-INST-1/D-INST-9). Nothing in this layer registers.
- **Layer 3 — Registered Ecosystem Applications.** **Externally owned, user-facing, purpose-specific** applications built on AFI primitives, plus their upstream **provider** mirror. They **register** to be recognized and routed; registration confers recognition and routing **only, never authority**; they are **never AFI or Institute property**; there is **no "official application" category**.

The **identity test** — *"if this changed fundamentally, would AFI stop being AFI?"* — is the canonical first question for classifying any component, applied by the framework in D-CONST-7.

**Scope-guard.** Fixes the **layer taxonomy and the identity test** only. It defines, changes, or removes **no** primitive, and grants or removes **no** authority from any repository or party.

---

## 2. D-CONST-2 — ratification of the three companion reference documents

**Decision.** The following three documents are ratified as the **canonical constitutional reference** for AFI, as governance-ledger doctrine:

- **AFI Constitutional Architecture v1.0** — the long-form constitution (layers, primitives, principles, decision framework);
- **AFI City Ontology Specification v1.0** — the City building classification (landmarks / building classes / ownership / registration);
- **AFI Component Classification Registry v1.0** — the master component table.

They are **reference**: where any of them conflicts with an accepted `afi-governance` decision, **the decision wins** and the document is corrected. They authorize **no** implementation. They currently live in the unversioned workspace `reports/` area; this decision records their **load-bearing framing** (restated across these clauses), not their file location — if they are moved or versioned, this decision continues to govern the framing.

**Scope-guard.** Ratifies the documents as **reference doctrine** only. It gives them no authority over any accepted decision, no implementation power, and no dependence on their storage location.

---

## 3. D-CONST-3 — the role → reference-implementation → hosted-instance pattern

**Decision.** AFI's core surfaces each resolve across three registers, and none is an AFI/Institute product:

- **the protocol role/contract** (Layer 1) — e.g. the Machine = the Signal-Evaluation scoring role + UWR/Evidence-V3 contracts (D1CAP-GOV; `uwr-*`; EV3-GOV); the Factory = the FCP configurable-pipeline slot `SLOT-FCP-FACTORY` + delegated contract family (FCP-GOV D-FCP-2/3); the Gateway = the "routes-not-writes" submission-boundary invariant (INST-GOV D-INST-2; FCP-GOV D-FCP-4);
- **the replaceable reference implementation** (Layer 2) — afi-reactor ("the Reactor", FCP D-FCP-4 "governed, replaceable runtime"), afi-factory ("the replaceable authoring implementation"), afi-gateway (MIT ingress), afi-tiny-brains (FLPR-GOV "replaceable, non-authority" aiMl lane), and the afi-infra Evidence V3 writer (a conforming implementation of the persistence contract);
- **the non-exclusive hosted instance** (Layer 2) — e.g. "AFI Signal Runtime" (hosted Machine, parked) and the designated (not-deployed) Institute Gateway reference service (INST-GOV D-INST-8).

**Replaceability is constitutional:** every reference implementation may be replaced by a conforming implementation; conformance is to the governed contracts, not to authorship or who hosts it. **Non-exclusivity is constitutional:** independent conforming operators remain permitted (INST-GOV D-INST-4).

**Scope-guard.** **Consumes** D1CAP-GOV, FCP-GOV (D-FCP-4), FLPR-GOV, INST-GOV, `uwr-*`, EV3-GOV, and the persistence decisions and **re-decides none of them**; it transfers **no** authority to the Institute, renames nothing, and authorizes no implementation or deployment.

---

## 4. D-CONST-4 — naming registers and the retired-terminology register

**Decision.** Two terminology registers are fixed for consistent use across governance and documentation.

**Canonical names.** The scoring surface is **"Machine"** (public/City label), **"the Reactor" / afi-reactor** (reference implementation), and **"AFI Signal Runtime"** (hosted instance); these are distinct registers and must not be conflated. The **scoring primitive is UWR** (`uwrScore` → `afi.scored-signal-evidence.v3`). "Factory" (capital-F) is the AFI authoring slot/implementation; "Gateway" is the submission-boundary implementation. "CPJ" expands to **Canonical Parsed JSON** (`afi.cpj.v0.1`).

**Retired terms** (named only to retire; never enshrined as live): **T.S.S.D. Vault / "Time-Series Signal Data" store** (distinct from the live **Vault** = Evidence V3 + provenance); **"Agent Registry"**; **Codex / `.afi-codex.json` / "codex logging"** (superseded by the canonical Atlas); **personas / ElizaOS / `character.schema.json` / PHOENIX_PERSONA / "neural spine"**; **mentors / "Validators & Mentors" / mentorChain**; **DAO** as a *current* governance mechanism (reserved-future only); **`signal_finalization_request` / validator `finalScore` finalization** (finality is `Evidence V3 lifecycleState=FINALIZED` under LIFE-GOV/MONGO-GOV); the third-party **`.factory/` "Droids"** dev-tool namespace as any AFI primitive (a word collision with the AFI Factory surface); and **"canonical provenance journal"** as an expansion of CPJ.

**Scope-guard.** Records **terminology** only. It renames **no** repository, service, schema, field, or Atlas structure, and it **edits no residue file** — retiring a term here does not authorize any cleanup edit (that remains an owner-driven backlog act, unauthorized by this decision).

---

## 5. D-CONST-5 — PoI / PoInsight classification (owner ruling)

**Decision.** Recorded as a governance fact per the owner ruling of 2026-07-25: **Proof-of-Intelligence (PoI)** and **Proof-of-Insight (PoInsight)** are **two distinct** AFI reputation primitives, both **reserved (governed-but-dormant)**, both **preserved** — neither is a discarded term:

- **Proof-of-Intelligence (PoI)** — proof of an analyst's **capability to score** across markets, asset classes, regimes, and strategies;
- **Proof-of-Insight (PoInsight)** — proof of the **insight provided *beyond* the UWR score** (value-add above raw scoring ability).

Both are **analyst/validator-level reputation metrics** whose invariants are already encoded in afi-core (computed by validators over time; **not** per-signal fields; and they **MUST NOT override UWR output** — `afi-core/validators/ValidatorDecision.ts`, `afi-core/schemas/validator_metadata_schema.ts`, `afi-core/src/analyst/AnalystScoreTemplate.ts`). They are **distinct from UWR**, which remains the sole live scoring rule. This clause **corrects, on the governance record**, any prior audit framing that labelled PoI/PoInsight discarded.

**Scope-guard.** Records the **classification and terminology distinction** only. It decides **no** PoI or PoInsight formula, reputation weighting, or reputation math; it authorizes **no** mint, reward, settlement, emissions, or any economic conversion of reputation (all reserved to **CHAIN-GOV**); and it changes **no** afi-core code and **no** schema. Their activation is reserved to a future CHAIN-GOV/reputation decision.

---

## 6. D-CONST-6 — the Registered Application layer and the reserved applications registry

**Decision.** **Registered Applications** (Layer 3) are externally owned, user-facing, purpose-specific applications built on AFI primitives — e.g. BUY SELL TERMINAL, Munni, agent-as-a-service, research and commercial applications — together with their upstream **provider** mirror. Criteria: externally owned; user-facing; purpose-specific; built on AFI primitives; **registered**. They are **never AFI or Institute property** (a trader cockpit is a product, not a reference service; the Institute may operate reference *services*, never own an *application*), and there is **no "official application" category** and no field encoding one. Providers/tenants register **today** via the FCP-GOV D-FCP-5 mechanism (consumed unchanged; the `afi.provider-strategy-binding.v1` precedent). The **applications** family **`afi.registered-application.v1`** is **reserved** — recognized here as the intended Layer-3 registration contract but **not built and not decided**; it awaits its own enabling decision (`registered-application-v0.1`).

**Scope-guard.** Records the **layer, its criteria, and the reserved registry** only. It builds and authorizes **no** registry, schema, or record; the applications registry remains reserved; it registers **no** participant; and it changes nothing in the existing provider-binding mechanism.

---

## 7. D-CONST-7 — the component-placement decision framework

**Decision.** Future components are placed by this canonical framework (full form in the ratified Constitutional Architecture document, Article VI):

1. If the component is a **retired term/concept**, do not enshrine it — retire it explicitly.
2. **Identity test** — *if it changed fundamentally, would AFI stop being AFI?* If **yes** and it is governed (or reserved), it is a **Protocol Primitive** (Layer 1) — of the appropriate kind (core protocol-law contract; verification law; role/slot; meta-primitive; governed adapter/domain contract; or reserved primitive). If it is not yet governed, a governance decision must precede building it.
3. If **no**: must the Institute build/operate it to bootstrap the ecosystem? If it **fills a protocol slot**, it is an **Institute reference implementation** (replaceable); if it does not, it is **Institute infrastructure** — both non-authoritative, non-exclusive, and non-registering (Layer 2).
4. Otherwise, if it is externally owned, user-facing, and built on AFI primitives, it is a **Registered Application** (Layer 3) — external, must register, never AFI/Institute property.

Ambiguity is never resolved by inventing a first-party application; a component that a conforming third party could replace without changing what AFI *is* is an implementation, not a primitive.

**Scope-guard.** Records a **classification guidance rule** only. It classifies and authorizes **no** specific component and creates **no** new authority; each future component's placement is recorded by its own decision or registry act.

---

## 8. D-CONST-8 — reserved-domain honoring, precedence, and amendment

**Decision.** This decision **honors and does not touch** the reserved domains: **CHAIN-GOV** (rewards / mint / settlement / on-chain / economic activation — including Mint, the 86B cap and B(t) emissions, the epoch emissions cadence, AIM/AAG/SES adaptive issuance, and any PoI/PoInsight economic conversion) and **ATLAS-GOV** (any API/endpoint/route/query surface, including the Gateway endpoint contract). It **activates nothing** in either. This decision is **subordinate** to the Charter and `authority-districts-v0.1.md`; where it conflicts with any accepted decision, **that decision wins** and this framing is corrected; and it is **amended only by a new accepted decision** (never by editing an accepted file). Per `authority-districts-v0.1.md` Part F, agent self-ratification is forbidden — **acceptance is the owner's merge**.

**Scope-guard.** Asserts **reserved-domain honoring, precedence, and the amendment rule** only. It touches no reserved domain, removes no existing authority, and authorizes nothing.

---

## 9. Explicit non-authorizations

This decision does **not** authorize, decide, ratify, or pre-empt any of the following:

- **CHAIN-GOV** — no rewards, mint, settlement, emissions, staking, epoch settlement, or on-chain act; **no PoI/PoInsight reputation formula, weighting, math, or economic conversion**; no treasury/validator/governance privilege.
- **ATLAS-GOV** — no API/endpoint/route/query surface, including the Gateway endpoint contract and any read/replay/verify surface over evidence.
- **Schema/contract changes** — no change to USS, CPJ, Evidence V3, provenance, provider-strategy-binding, identity, enrichment-category, or any afi-config schema, registry, or KAT.
- **Runtime behavior** — no change to any Reactor/Gateway/afi-core route, handler, scorer, validator, or dedup/provenance behavior; no runtime code change in any repository.
- **`afi.registered-application.v1`** — no schema, no registry directory, no registration record; the applications family remains reserved to `registered-application-v0.1`.
- **Renames and cleanup** — no repository, service, schema, field, or Atlas-structure rename; no edit to any discarded-terminology residue (owner-driven backlog).
- **Deployment/infrastructure** — no deployment, GCP/cloud provisioning, DNS, service account, credential, funding, or onboarding system.
- **Registering any specific participant, provider, application, or binding** — FCP-GOV D-FCP-5 remains the mechanism; this decision registers nothing.
- **Status of other decisions** — it flips no other instrument's Status line and rewrites no accepted decision.

---

## Documentation ledger

This decision authorizes **no implementation**. It records the following **reference documents** (recorded, not extended); non-code, non-runtime, non-deployment.

| Surface | Location | Change | Authorized? |
|---|---|---|---|
| AFI Constitutional Architecture v1.0 | workspace `reports/` (unversioned) | Ratified as canonical constitutional reference (D-CONST-2) | Yes — reference doctrine; no code/runtime |
| AFI City Ontology Specification v1.0 | workspace `reports/` (unversioned) | Ratified as canonical City ontology reference | Yes — reference doctrine; no code/runtime |
| AFI Component Classification Registry v1.0 | workspace `reports/` (unversioned) | Ratified as canonical component classification | Yes — reference doctrine; no code/runtime |

Any future mirroring of this framing into versioned docs (e.g. afi-docs, afi-protocol, the org profile) is its **own** doc-only act and is **not** authorized here.

---

## 10. Reserved and unreached (explicit)

- **CHAIN-GOV (reserved, unfiled)** — the entire economic layer (Mint, 86B/B(t) emissions, epoch cadence, AIM/AAG/SES, and any PoI/PoInsight economic activation) remains reserved and is only *classified* (as reserved) by this decision, never activated.
- **ATLAS-GOV (reserved, unfiled)** — all endpoint/API/route authority, including the Gateway endpoint surface, remains reserved; this decision decides no endpoint.
- **`registered-application-v0.1` (unfiled)** — the applications-registry schema/mechanism is reserved to that future decision.
- **A future CHAIN-GOV/reputation decision** — the activation, formulas, and economic conversion of PoI/PoInsight are reserved there.

---

## 11. Supersessions and interactions

This is a **meta-framing decision**: it **supersedes none** of the nineteen prior accepted decisions in content, **consumes and frames all of them** into the three-layer model, and **re-decides nothing**. Each is named, with the layer it contributes to:

- **`authority-districts-v0.1.md`** — consumed; its authority-tier discipline ("self-labeling confers nothing", Part B.1; owner-merge acceptance, Part F; reserved ATLAS-GOV/CHAIN-GOV) is the basis for D-CONST-1/D-CONST-8. Not changed.
- **`current-authority-reroot-and-golden-closure-v0.1.md` (R1-GOV)** — consumed; District One = "Signal Evaluation", the non-production ceiling, and no-financial-truth are honored (D-R1-1/D-R1-2). The five enrichment categories (D-R1-4) are recorded as a Layer-1 core contract. Not changed.
- **`district-api-atlas-foundation-v0.1.md` (ATLAS-GOV)** — consumed; the canonical Atlas is framed as a Layer-1 meta-primitive (registry-of-record map); the `role-application-integrator` role is a `planned` element within it pointing at the reserved Layer-3 applications tier. ATLAS-GOV endpoint authority remains reserved. Not changed.
- **`district-one-signal-evaluation-capability-v0.1.md` (D1CAP-GOV)** — consumed; the Signal-Evaluation scoring capability is the Machine role (Layer 1); the GraphExecutor is its reference implementation (Layer 2). Not changed.
- **`district-2-m2-ratification-v0.1.md`** and **`district-surface-consolidation-v0.1.md` (DSC-GOV)** — consumed; District/surface topology is framed as Layer-1 authority structure. Not changed.
- **`evidence-v3-provider-provenance-v0.1.md` (EV3-GOV)** — consumed; Evidence V3, the provenance model, and the five-lane fail-closed verification law are recorded as Layer-1 core protocol-law contracts / verification law (the City **Vault**). Not changed.
- **`factory-configurable-pipelines-v1.md` (FCP-GOV)** — consumed; the Factory slot + contract family is Layer-1 (D-FCP-2/3), afi-factory is a replaceable Layer-2 reference implementation (D-FCP-4), and D-FCP-5 remains the sole provider/tenant registration mechanism for Layer 3. Not changed.
- **`five-lane-provider-runtime-v0.1.md` (FLPR-GOV)** — consumed; establishes the replaceable-implementation precedent (Tiny Brains "replaceable, non-authority") that D-CONST-3 generalizes. Not changed.
- **`lifecycle-v0.1.md` (LIFE-GOV)** — consumed; `lifecycleState=FINALIZED` is the finality primitive (retiring `signal_finalization_request`). Not changed. (Its standing "Proposed" Status is left as-is; this decision touches no other Status line.)
- **`math-authority-v0.1.md` (MATH-GOV)** — consumed; afi-math is the Layer-1 canonical math authority; afi-econ is Layer-2 research infrastructure (non-canonical, MATH-GOV §3). Not changed.
- **`mint-formula-bt-86b-alignment-v0.1.md`** — consumed; the Mint formula, 86B cap, B(t) emissions, and AIM/AAG/SES are recorded as **reserved** Layer-1 economic primitives (CHAIN-GOV). Not changed; nothing activated.
- **`object-identity-v0.1.md` (OBJ-GOV)** — consumed; USS v1.1 is the Layer-1 core ingestion contract and the identity model is a Layer-1 meta-primitive; CPJ is recorded as a governed **subordinate** adapter contract ("classified, not elevated", D-OBJ-2), not co-equal with USS. Not changed. (Standing "Proposed" Status left as-is.)
- **`persistence-v0.1.md` (MONGO-GOV)** and **`persistence-impl-v0.1.md`** — consumed; routes-not-writes and the single canonical writer are honored; the afi-infra Evidence V3 writer is a Layer-2 reference implementation of the persistence contract. Not changed. (Standing "Proposed" Statuses left as-is.)
- **`provider-byok-foundations-v0.1.md` (PBF-GOV)** — consumed; provider identity is part of the Layer-1 identity substrate; providers are the Layer-3 upstream mirror. Not changed. (Standing "Proposed" Status left as-is.)
- **`research-institute-reference-services-v0.1.md` (INST-GOV)** — consumed; the operator-vs-protocol distinction, non-exclusivity, and "official ≠ canonical" are the foundation of Layer 2 (D-CONST-1/D-CONST-3). Not changed.
- **`uwr-runtime-consumption-v0.1.md`** and **`uwr-profile-pin-v0.1.md`** — consumed; UWR is recorded as the Layer-1 live scoring primitive (invoked, never re-implemented), distinct from and un-overridable by PoI/PoInsight (D-CONST-5). Not changed.

**Reserved domains** — **`ATLAS-GOV`** and **`CHAIN-GOV`** are honored and untouched (§10). No prior decision's Status line is flipped by this decision.

---

**Accepted owner decision (afi-governance PR #30, merge commit `7adf52c`, merged unedited on 2026-07-26). Authoritative upon owner merge.** This decision ratifies AFI's three-layer constitutional model (Protocol primitives / Institute replaceable reference implementations & non-exclusive reference services / externally-owned Registered Applications), ratifies the three companion reference documents, fixes the canonical and retired terminology registers, records the owner ruling that Proof-of-Intelligence (PoI) and Proof-of-Insight (PoInsight) are two distinct **reserved** reputation primitives distinct from UWR, records the Registered Application layer and its reserved applications registry, and fixes the component-placement framework — and nothing else. It re-decides no prior decision, touches no schema, no route, no runtime, no deployment, no ATLAS-GOV endpoint surface, and no CHAIN-GOV economic act, and transfers no protocol authority to any party.
