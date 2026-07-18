# AFI Provider Adapter and BYOK Foundations v0.1 (PBF-GOV)

**Slot:** `AFI-GOV-PROVIDER-BYOK-FOUNDATIONS-v0.1` (PBF-GOV)
**Status:** **Proposed** for owner approval. This decision records the owner's settled decisions establishing the **provider-neutral adapter socket and the secure bring-your-own-key (BYOK) credential boundary** for the span between canonical category enrichment and scoring: the **five categories as open capability lanes**, the **separation of category identity from provider and implementation identity**, the **one-resolved-result-per-category invariant**, the **three canonical non-secret objects (Provider, CredentialRef, ProviderInstance)**, the **trusted registered-adapter rule**, the **credential-never-in-artifact and least-privilege runtime-resolution invariants**, the **canonical category-output-validation-before-scoring rule**, the **deterministic-runtime / agentic-authoring authority bound**, the **Evidence V2 freeze with provider-invocation provenance deferred**, and the **non-exclusive, no-automatic-privilege, no-deployment** boundaries. It becomes authoritative **only** when the owner merges it; until merged, it is a draft with no force. **Owner authorization for this decision and the Wave-1 foundation implementation it governs is recorded by the owner instruction that commissioned this mission** — the scoped afi-config / afi-factory / afi-reactor changes merge when their gates pass; no per-clause row flip is required.
**Date:** 2026-07-17
**Type:** Scoped protocol-development governance decision (provider-neutral adapter contract / BYOK credential boundary / bounded Wave-1 foundation program). Records settled owner decisions; it is **not** a constitution and decides nothing beyond its eleven clauses.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` (canonical home `afi-config/codex/governance/droids/`) and `decisions/authority-districts-v0.1.md`. **Consumes (does not re-decide)** `decisions/factory-configurable-pipelines-v1.md` (FCP-GOV — the D-FCP-1 five-category namespace, the D-FCP-3 delegated afi-config contract family, the D-FCP-4 repository roles, and the D-FCP-5 generic-registration/fail-closed rule), `decisions/object-identity-v0.1.md` (OBJ-GOV — USS v1.1 and the strategy triple), `decisions/persistence-v0.1.md` (MONGO-GOV — the routes-not-writes boundary and the single canonical evidence writer), and `decisions/research-institute-reference-services-v0.1.md` (INST-GOV — the non-exclusive designated-operator role). Coordinates with (does **not** override) `decisions/lifecycle-v0.1.md` (LIFE-GOV) and `decisions/math-authority-v0.1.md`. **Honors, and does not touch,** the reserved `ATLAS-GOV` (API Atlas / Gateway endpoint authority) and `CHAIN-GOV` (rewards / mint / settlement / on-chain) scopes, both as-yet-unfiled. Where this decision conflicts with the Charter, the Charter wins.
**Evidence basis:** the verified read-only Mission-1 audit and blueprint `reports/afi-agentic-enrichment-pipeline-readiness-audit-and-blueprint.md` and its handoff `reports/afi-enrichment-mission-2-handoff.md` (2026-07-17; **input, not authority**; they live in the unversioned workspace `reports/` area, so every finding this decision relies on is restated inline with its citation). Pinned at: afi-config @ `a64c62f`, afi-factory @ `232707b`, afi-reactor @ `547bcbe`, afi-core @ `54ca87a`, afi-infra @ `12c3827`, afi-docs @ `a786146`, afi-tiny-brains @ `a30c2ad`, afi-governance @ `88304b8` (all prior accepted decisions read in full). The audit confirmed: AFI already has one data-driven `GraphExecutor`, a manifest-configurable DAG, category-separate-from-implementation, hash-pinned composition, Evidence V2, a technical `PriceFeedAdapter` interface, and a `NewsProvider` interface — but **no generalized provider identity, no BYOK credential object, no secret manager (the `VaultService` is a throwing stub), no least-privilege secret resolver, and one concrete credential-in-URL leak on the news path**. This decision governs the smallest coherent provider socket and credential boundary that closes those gaps additively.
**Ledger slot:** None existed — no prior decision governs a compute/data-provider identity, a credential-reference object, a provider-instance object, or a BYOK boundary; the strings "CredentialRef", "ProviderInstance", and "BYOK" appear in no prior decision. This decision opens that slot. It authorizes the bounded Wave-1 foundation across afi-config (schemas/registries/KATs), afi-factory (authoring), and afi-reactor (adapter socket, resolver, two reference proofs) — and nothing beyond it. It consumes (does not re-decide) the FCP-GOV D-FCP-1 namespace and D-FCP-5 registration mechanism, and it leaves the ATLAS-GOV Gateway-endpoint reservation and the CHAIN-GOV reservation intact.

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these eleven):**
1. the **five analysis categories as open capability lanes**, and that **category identity is separate from provider identity and from implementation identity** (D-PBF-1);
2. that the scorer-facing pipeline consumes **exactly one resolved result per category**, and that **generic cross-category or same-category ensembles are not part of this version** (D-PBF-2);
3. the **Tiny Brains future internal AI/ML ensemble boundary** — it may later orchestrate several internal models but emits **one** resolved `aiMl` result and remains subordinate to canonical scoring (D-PBF-3);
4. the **three canonical non-secret objects** — **Provider**, **CredentialRef**, **ProviderInstance** — and their scopes (D-PBF-4);
5. that **provider adapters are trusted, registered, versioned, boot-validated implementations — not arbitrary runtime code** (D-PBF-5);
6. that **provider identity does not imply AFI endorsement**, and that **independent conforming providers and adapters remain permitted** (D-PBF-6);
7. the **BYOK credential boundary** — pipeline artifacts may reference ProviderInstances but **never** contain credentials, and runtime secret access is **least-privilege and scoped to the active provider instance** (D-PBF-7);
8. that **provider outputs must pass canonical category validation before scoring**, and that **existing scoring, UWR, Core, and Math authority remain unchanged** (D-PBF-8);
9. that **runtime agents receive no unrestricted provider-selection or credential authority** — the runtime is deterministic and policy-bound; agents author future versions only (D-PBF-9);
10. that **Evidence V2 remains unchanged in this version**, and that **provider-invocation provenance requires a later governed evidence decision** (D-PBF-10);
11. that **Institute-operated reference adapters are non-exclusive**, that **no automatic reward, validator, governance, or treasury privilege follows from provider operation**, and that **no deployment and no specific secret backend is mandated** (D-PBF-11).

**Does NOT decide (reserved to their own scoped decisions; see §12):** any **generic ensemble contract** (weighting, quorum, membership, provider-substitution fallback — deferred); any **runtime agent-operation authority** (provider discovery, autonomous selection, health-based switching, cost optimization — deferred); any **provider-invocation provenance shape or Evidence V3** (deferred to a later governed evidence decision, after real adapters reveal the true fields); any **API/endpoint/route/query surface**, including a provider read/catalog API (**ATLAS-GOV**, unfiled); any **rewards / mint / settlement / claims / on-chain** act (**CHAIN-GOV**, unfiled); **which specific providers, adapters, credential references, or provider instances exist** (each is a registry/deployment update under FCP-GOV D-FCP-5, reviewed on its own PR); **UWR law, scorer logic, Core or Math authority, the scorer-facing category join, signal lifecycle, finality, reputation, incentives, or settlement** (their existing owners, all unchanged); and any **deployment, GCP/cloud provisioning, Secret Manager resource, IAM, service account, or specific cloud/logging SDK or vendor** (out of scope entirely, §12).

**Nature of the act.** This decision establishes a **contract-and-boundary governance record**: it fixes the semantics of a provider-neutral adapter socket and a secure credential boundary, and it authorizes the smallest coherent Wave-1 foundation that realizes them additively on the existing executor and Evidence V2. It adds **no** vendor, **no** deployment, **no** ensemble, **no** runtime agent, and **no** economic act. It does not choose a specific cloud SDK, secret backend, logging library, implementation class name, provider allowlist, commercial pricing, or deployment IAM detail — those are implementation or deployment concerns, not protocol law.

---

## 1. D-PBF-1 — five open capability lanes; category ≠ provider ≠ implementation

**Decision.** AFI's five analysis categories — `technical`, `pattern`, `sentiment`, `news`, `aiMl` (the FCP-GOV D-FCP-1 canonical namespace, unchanged; casing `aiMl` exact) — are each an **open capability lane**. A category is **not** a vendor, not one hardcoded service, not one required algorithm, not one Institute-controlled provider, and not an ensemble. Three identities are fixed and must be used consistently:

- **Category** — the semantic analysis lane a node occupies (governed enum; unchanged).
- **Plugin / adapter** — a trusted, registered, executable implementation identity (the existing `afi.analysis-plugin.v1` plugin identity is the adapter boundary where it fits; the runtime provider-adapter is its below-the-node execution surface).
- **Provider** — the service, library, model family, or implementation source that supplies an analytical capability (a new non-secret identity, D-PBF-4).

An analyst may ultimately choose any conforming implementation or provider for each selected category. Category identity never encodes a vendor and never determines a provider.

**Scope-guard.** Fixes the **open-lane character and the three-identity separation** only. It renames no category, changes no category enum, and mandates no provider for any lane.

---

## 2. D-PBF-2 — one resolved result per category; no generic ensembles in this version

**Decision.** The scorer-facing pipeline continues to consume **at most one resolved result per category** (`technical → one`, `pattern → one`, `sentiment → one`, `news → one`, `aiMl → one`). The existing deterministic one-per-category join (which fails closed on a duplicate-category contribution) is **preserved unchanged**; it must **not** be turned into a generic ensemble engine. A provider may internally aggregate many data points or sources (a news provider may evaluate many articles; a sentiment provider may read several social sources; a technical implementation may compute many indicators), but AFI treats one provider invocation as **one** category implementation producing **one** category result at the pipeline boundary.

**Generic cross-category or same-category provider ensembles are not part of this version.** No duplicate-category reconciliation, no weighting, no quorum, and no ensemble-join contract is created here. Ensemble semantics and fallback disclosure are reserved to their own later scoped decision (§12).

**Scope-guard.** Fixes the **one-result-per-category invariant and the no-ensemble boundary** only. It changes no join code, adds no ensemble plugin, and weakens no existing join constraint.

---

## 3. D-PBF-3 — Tiny Brains future internal AI/ML ensemble boundary

**Decision.** Tiny Brains is the special AI/ML enrichment service for the `aiMl` category. It **may later** operate multiple specialized models internally (for example several forecasters plus a critic or meta-model) and combine them **inside** the service. At the AFI pipeline boundary it emits **exactly one** resolved `aiMl` category result. Tiny Brains:

- enriches the `aiMl` category only;
- may later use an internal model ensemble that is invisible to AFI except as one canonical `aiMl` result;
- does **not** replace the canonical scorer, does **not** modify UWR law, does **not** override Core or Math, and does **not** determine final signal status independently.

Its internal orchestration is not an AFI-level ensemble and never creates duplicate `aiMl` results (D-PBF-2). This version implements no Tiny Brains ensemble behavior and creates no general ensemble contract.

**Scope-guard.** Documents the **future internal-ensemble boundary and Tiny Brains' subordination to canonical scoring** only. It implements nothing in `afi-tiny-brains`, changes no model orchestration, and grants Tiny Brains no scoring authority.

---

## 4. D-PBF-4 — three canonical non-secret objects: Provider, CredentialRef, ProviderInstance

**Decision.** The provider socket is modeled with exactly **three** new first-class, non-secret canonical objects, delegated to the afi-config contract family (FCP-GOV D-FCP-3):

- **Provider** (`afi.provider.v1`) — a stable, non-secret identity describing who or what supplies an analytical capability (local AFI implementation, open-source library, external API, data vendor, hosted inference service, local model runtime, proprietary service, or Tiny Brains). It carries only minimum non-secret metadata (provider id, record version, display name, supported categories, execution class, deterministic/probabilistic posture, the supported adapter identity, and — only where a capability requires one — the *kind* of credential required, never a value). Registry presence means **available to the relevant AFI deployment or configuration**, not universally approved by AFI Protocol.
- **CredentialRef** (`afi.credential-ref.v1`) — a **non-secret, opaque, scoped reference** to credentials. It **must not contain** an API key, bearer token, password, private key, session cookie, OAuth refresh token, complete authorization header, or any secret payload. It carries only the minimum needed to resolve a credential safely (an opaque reference id whose backend-specific location remains deployment-local, a tenant/owner scope, provider compatibility, a credential kind, and a disabled/revoked state); rotation happens **behind** the reference. It must not expose cloud project names, Secret Manager paths, filesystem locations, or backend topology.
- **ProviderInstance** (`afi.provider-instance.v1`) — a **tenant- or operator-scoped, non-secret** configuration binding one provider to one registered adapter for exactly one category. It identifies exactly one category, exactly one provider, and one registered adapter implementation (id and version); it is version-pinned sufficiently for deterministic composition; it **optionally** references one compatible CredentialRef; it contains **no** credential value, **no** arbitrary executable code, and **no** unrestricted remote endpoint supplied by the analyst; and it fails validation when provider, category, adapter, or credential requirements conflict.

The existing category and plugin concepts are reused, not duplicated: `Category` = the semantic lane, `Plugin/adapter` = the trusted executable implementation, `Provider` = the source, `ProviderInstance` = this tenant/operator's configured use, `CredentialRef` = the non-secret pointer to required credential material. No separate adapter-code object and no agent-policy object is created in this version.

**Scope-guard.** Fixes the **three object identities and their non-secret, scoped character** only. It defines the schemas' semantics; the exact fields, registries, and KATs are the afi-config implementation of this clause under D-FCP-3, and no object may ever carry a secret value.

---

## 5. D-PBF-5 — provider adapters are trusted registered implementations, not arbitrary runtime code

**Decision.** A provider adapter in this version must be **compiled with the trusted runtime, explicitly registered, versioned, validated at boot, and invoked through a bounded interface**. The adapter registry is explicit and fail-closed: an unknown adapter is refused, a duplicate registration is refused, and adapter/category incompatibility is refused. This version implements **none** of: arbitrary npm-package loading, arbitrary Python execution, remote code loading, user-supplied JavaScript, user-supplied executable URLs, dynamic plugin installation, a provider marketplace, or a universal plugin-approval authority. The existing build-time static plugin-registry discipline (no dynamic import, no lazy discovery) is preserved and extended to the adapter layer.

**Scope-guard.** Fixes the **trusted-registered-adapter rule** only. It authorizes no code-loading mechanism and creates no sandbox governance (a third-party-code-execution / sandbox decision, if ever needed, is separate — this version ships first-party and Institute-designated adapters only).

---

## 6. D-PBF-6 — provider identity is not endorsement; independent conforming operation is permitted

**Decision.** The presence of a provider, adapter, credential reference, or provider instance in a registry or deployment configuration conveys **no** commercial endorsement by AFI Protocol and **no** protocol authority. Registry presence means **available to the relevant AFI deployment or configuration**. Independent parties may author and operate **conforming** providers and adapters; a conforming implementation is not invalid because AFI did not author it, and an AFI-authored reference implementation is not privileged because AFI authored it. Adding a conforming provider, adapter, credential reference, or provider instance is an administrative, schema-validated registry or deployment update under FCP-GOV D-FCP-5 — **not** per-participant governance.

**Scope-guard.** Fixes the **identity-is-not-endorsement and independent-conforming-operation** invariants only. It endorses no vendor, ranks no provider, and creates no allowlist or certification authority.

---

## 7. D-PBF-7 — the BYOK credential boundary

**Decision.** Two invariants are fixed and are security-critical:

- **Pipeline artifacts identify provider configurations but never contain provider credentials.** A pipeline node may reference a versioned ProviderInstance; it may never embed a CredentialRef value, a secret value, or a complete credentialed endpoint. Canonical hashing, evidence, logs, traces, and packaged artifacts are all credential-free by construction (`additionalProperties:false` closed schemas plus explicit allowed fields plus a redaction boundary — never field-name checks alone).
- **Runtime secret access is least-privilege and scoped to the active provider instance.** Secrets are resolved **only at runtime**, **only at the adapter edge below the node**, through an injected resolver that can resolve **only** the exact CredentialRef already authorized for the active ProviderInstance. The resolver must not list secrets, resolve arbitrary references, read another tenant's credential, discover backend paths, or write/delete/rotate secrets, and it never hands the adapter an unrestricted secret-management client. A required-but-unresolved credential **fails closed** with a useful but non-revealing error (never the secret value, secret path, complete authorization header, complete credentialed URL, or another tenant's identity).

Factory (the authoring surface) cannot resolve credentials, call providers, inspect a secret backend, test credential validity, or print secret values.

**Scope-guard.** Fixes the **credential-never-in-artifact and least-privilege-runtime-resolution** invariants only. It mandates no specific secret backend (D-PBF-11) and no specific redaction library.

---

## 8. D-PBF-8 — canonical category validation before scoring; scoring authority unchanged

**Decision.** A provider-produced category result must **pass canonical category-output validation before it reaches the scorer-facing path**; a malformed provider output never reaches scoring and fails closed. Provider-backed enrichment is **input** to the existing scorer — never a replacement for it. This decision changes **none** of: category weighting, scorer logic, UWR, Core mathematical behavior, Math kernels, scorer sink rules, the one-result-per-category join semantics, signal lifecycle, finality, reputation, incentives, minting, or settlement. The accepted flow remains: provider-backed category result → existing category join → existing canonical scorer → existing UWR.

**Scope-guard.** Fixes the **output-validation-before-scoring rule and the scoring-authority-unchanged** invariant only. It moves no scoring value, touches no UWR pinned profile, and alters no Math law.

---

## 9. D-PBF-9 — deterministic runtime, agentic authoring; bounded agent authority

**Decision.** The Reactor executor remains **deterministic** with respect to the approved pipeline artifact and runtime configuration. Agents may use Factory's existing authoring operations to author, inspect, validate, and propose future pipeline configurations. No runtime agent may autonomously discover providers, choose an undeclared provider, access arbitrary credentials, change model versions, add pipeline nodes, exceed declared budgets, alter scoring, invoke a hidden fallback, or rewrite the active pipeline. Runtime behavior in this version is **declarative and policy-bound**; any future bounded runtime agent authority is a separate scoped decision (§12).

**Scope-guard.** Fixes the **deterministic-runtime / agentic-authoring authority bound** only. It grants no runtime agent any provider-selection or credential authority and authorizes no runtime agent controller.

---

## 10. D-PBF-10 — Evidence V2 freeze; provider provenance deferred

**Decision.** This version does **not** change the governed Evidence V2 schema, its semantics, the canonical Mongo record shape, the Evidence V2 store version pin, existing lifecycle status, or canonical persistence behavior. The versioned pipeline composition may commit to a **non-secret** ProviderInstance reference through its existing artifact hash where the current composition rules naturally include it; it must **not** add provisional provider-provenance fields to Evidence V2, and it persists **no** provider credential, provider-invocation object, or new Mongo collection. Detailed provider/model **invocation provenance** (provider identity, model id/version, deterministic-vs-probabilistic posture, invocation commitments) is **deferred to a later governed evidence decision** that will determine Evidence V3 **after** real adapters reveal the true provenance fields. Documentation must not claim Evidence V2 contains provider-invocation provenance.

**Scope-guard.** Fixes the **Evidence V2 freeze and the deferral of provider provenance** only. It authorizes no store schema-const change and mints no Evidence V3.

---

## 11. D-PBF-11 — Institute reference adapters non-exclusive; no privilege; no deployment mandate

**Decision.** AFI Research Institute (INST-GOV) is the designated, non-exclusive operator of official open reference services; that designation does **not** make Institute adapters mandatory or canonical, and this version documents a possible future Institute reference-adapter role **without** deploying or privileging one. Operating a provider confers **no** automatic reward, validator, governance, or treasury privilege (reserved to CHAIN-GOV, unchanged). This decision mandates **no** deployment and **no** specific secret backend: a real GCP Secret Manager backend belongs to a separate staging/deployment wave; this version provisions no GCP resource, no IAM, and no service, and represents no existing stub as production-ready.

**Scope-guard.** Fixes the **Institute-non-exclusivity, no-automatic-privilege, and no-deployment-mandate** invariants only. It deploys nothing, privileges no operator, and reserves every economic consequence to CHAIN-GOV.

---

## 12. Explicit non-authorizations

This decision does **not** authorize, decide, ratify, or pre-empt any of the following; each remains for its own scoped decision or is out of scope entirely:

- **Generic ensembles** — no cross-category or same-category ensemble contract, no duplicate-category reconciliation, no weighting/quorum/membership, and no provider-substitution fallback; the one-per-category join is preserved as-is.
- **Runtime agent operation** — no runtime provider discovery, autonomous provider selection, health/latency/cost-based switching, cost-optimization agent, or any runtime agent controller.
- **Provider-invocation provenance / Evidence V3** — no change to Evidence V2, no provider-provenance object, no store schema-const bump; deferred to a later governed evidence decision.
- **ATLAS-GOV** — any API/endpoint/route/query surface, including a provider catalog/read endpoint and any read/replay/verify surface over evidence.
- **CHAIN-GOV** — any rewards, mint, settlement, claims, receipts, staking, or on-chain act, and any treasury/validator/governance privilege following from provider operation.
- **Deployment and infrastructure** — no deployment of any provider, adapter, or service; no GCP/cloud provisioning, Secret Manager resource, IAM, service account, DNS, budget, or onboarding system; no specific cloud SDK, no specific secret-management platform, and no specific logging library is mandated.
- **Registering any specific provider, adapter, credential reference, or provider instance** — FCP-GOV D-FCP-5 already provides that mechanism; each is a reviewed registry or deployment update.
- **Implementation particulars** — no implementation class name, no arbitrary provider allowlist, no commercial pricing, and no deployment IAM detail is governed here.
- **District pipeheads, the API Atlas, post-`SCORED` lifecycle, finality writing, reputation, incentives** — all unchanged and unreached; pipeheads remain reference-only.

---

## 13. Supersessions and interactions

- **FCP-GOV (`factory-configurable-pipelines-v1.md`)** — **consumed, not re-decided.** The D-FCP-1 five-category namespace is used exactly (casing `aiMl`). The D-FCP-3 delegation of the V1 contract family to afi-config is the home for the three new schemas and the two category-output contracts. The D-FCP-4 repository roles (afi-config owns contracts; afi-factory authors and is not runtime; afi-reactor is the governed replaceable runtime that constructs Evidence V2 and submits through afi-infra; afi-infra is the sole canonical writer) are used exactly. The D-FCP-5 generic-registration/fail-closed rule remains the sole mechanism for adding a conforming provider, adapter, credential reference, or provider instance.
- **OBJ-GOV (`object-identity-v0.1.md`) + MONGO-GOV (`persistence-v0.1.md`)** — **consumed.** USS v1.1 and the strategy triple are unchanged; the routes-not-writes boundary and single canonical writer are honored; the Evidence V2 store binding is frozen (D-PBF-10).
- **INST-GOV (`research-institute-reference-services-v0.1.md`)** — **consumed.** The Institute's non-exclusive designated-operator role is honored; provider/adapter registration remains the D-FCP-5 mechanism; a future Institute reference-adapter role is documented, not privileged or deployed (D-PBF-11).
- **ATLAS-GOV (reserved, unfiled)** — **honored, not touched.** All API/endpoint/route authority — including any provider catalog/read surface — remains reserved to ATLAS-GOV. This version builds no provider read-API.
- **CHAIN-GOV (reserved, unfiled)** — **honored, not touched.** No economic, reward, validator, or settlement consequence follows from provider operation.
- **LIFE-GOV / math-authority** — **coordinated, not overridden.** The lifecycle reaches `SCORED`; nothing here writes finality or touches scoring/math law.
- **`authority-districts-v0.1.md`** — its authority-tier discipline ("self-labeling confers nothing") is the basis for D-PBF-6's "registry presence is not endorsement" rule; District pipeheads remain reference-only and unreached.

---

**Proposed for owner approval. Authoritative only upon owner merge.** This decision fixes the five categories as open capability lanes, separates category from provider and implementation identity, preserves one resolved result per category, defines the three non-secret objects Provider / CredentialRef / ProviderInstance, requires provider adapters to be trusted registered implementations, keeps provider identity free of endorsement, fixes the credential-never-in-artifact and least-privilege-runtime-resolution BYOK boundary, requires canonical category-output validation before scoring, keeps the runtime deterministic and agent authoring bounded, freezes Evidence V2 while deferring provider-invocation provenance to a later governed evidence decision, and keeps Institute reference adapters non-exclusive with no automatic privilege and no deployment — and nothing else. It touches no scoring-law value, no UWR pinned profile, no Math kernel, no Evidence V2 shape, no canonical persistence, no ensemble, no runtime agent, no ATLAS-GOV surface, no CHAIN-GOV economic act, no District scope, and no deployment; it provisions no GCP or Secret Manager resource and creates no new repository.
