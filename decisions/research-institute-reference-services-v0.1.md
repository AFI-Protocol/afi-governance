# AFI Research Institute Reference Services Authority v0.1 (INST-GOV)

**Slot:** `AFI-GOV-AUTHORITY-INSTITUTE-REFERENCE-SERVICES-v0.1` (INST-GOV)
**Status:** **Proposed** for owner approval. This decision records the owner's settled decision that **AFI Research Institute is the designated operator of AFI's official open reference services** — an official hosted **Gateway reference service** for structured signal ingress and an official **oracle-ingress and CPJ-normalization reference service** for message- and source-derived candidate signals — while fixing that the designation is **non-exclusive**, that **independent conforming operators remain permitted**, that **operating a reference service confers no protocol authority**, that the **direct Reactor CPJ route is an internal trusted service boundary** (not a public API), and that **USS remains the canonical convergence checkpoint** with **CPJ an optional upstream adapter contract**. It becomes authoritative **only** when the owner merges it; until merged, it is a draft with no force.
**Date:** 2026-07-17
**Type:** Scoped protocol-development governance decision (research-institute operator designation / reference-service roles / trust-boundary documentation). Docs/governance-ledger only; it authorizes **no** implementation, deployment, infrastructure, credential, runtime change, or economic act, and decides nothing beyond its nine clauses.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` (canonical home `afi-config/codex/governance/droids/`), its `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md`, and `decisions/authority-districts-v0.1.md`. **Consumes (does not re-decide)** `decisions/factory-configurable-pipelines-v1.md` (FCP-GOV — the D-FCP-4 repository roles and the D-FCP-5 generic-registration/fail-closed rule), `decisions/persistence-v0.1.md` (MONGO-GOV — the routes-not-writes boundary and single canonical writer), and `decisions/object-identity-v0.1.md` (OBJ-GOV — USS v1.1 and the strategy triple). Coordinates with (does **not** override) `decisions/lifecycle-v0.1.md` (LIFE-GOV) and `decisions/math-authority-v0.1.md`. **Honors, and does not touch,** the reserved `ATLAS-GOV` (API Atlas / Gateway endpoint authority) and `CHAIN-GOV` (rewards / mint / settlement / on-chain) scopes, both as-yet-unfiled. Where this decision conflicts with the Charter, the Charter wins.
**Evidence basis:** the verified read-only verification report `reports/afi-research-institute-reference-services-v0.1.md` (2026-07-17; 7 verification agents + a bounded adversarial review; **input, not authority**; it lives in the unversioned workspace `reports/` area, so every finding this decision relies on is restated inline with its citation). Pinned at: afi-gateway @ `3cb4cb7`, afi-reactor @ `1f48dbf`, afi-config @ `a64c62f`, afi-docs @ `5f1954f`, afi-protocol @ `33838ae`, .github @ `5abb026`, afi-governance @ `414beb9` (all prior accepted decisions read in full). The verification confirmed: the Gateway and the direct CPJ route exist as runnable, CI-tested source, but **no Institute-operated Gateway or oracle-ingress service is deployed** (no CD pipeline, no hosted URL/DNS, no container/cloud manifest, `NODE_ENV=development`, localhost defaults); the direct CPJ route's authentication is optional and off by default; and no repository grants the Institute any protocol, economic, or validator authority.
**Ledger slot:** None existed — no prior decision governs a research-institute operator role, reference services, or an oracle-ingress trust boundary; the string "Institute" appears in no prior decision. This decision opens that slot. It creates no implementation-slot authorization (it ships documentation only, §Documentation ledger). It consumes (does not re-decide) the FCP-GOV D-FCP-4 roles and D-FCP-5 registration mechanism and the MONGO-GOV write boundary, and it leaves the ATLAS-GOV Gateway-endpoint reservation (`persistence-v0.1.md:26,126`; `lifecycle-v0.1.md:23,123`; `object-identity-v0.1.md:27,111`) and the CHAIN-GOV reservation intact.

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these nine):**
1. the **protocol-versus-operator distinction** and the three definitions it rests on — *canonical*, *official reference service*, *independent conforming operator* (D-INST-1);
2. the **official Institute Gateway reference-service role** for structured signal ingress (D-INST-2);
3. the **official Institute oracle-ingress and CPJ-normalization reference-service role** for message- and source-derived candidate signals (D-INST-3);
4. the **non-exclusive** character of both roles and the standing right of **independent conforming operators** (D-INST-4);
5. **USS as the canonical convergence checkpoint**, **CPJ as an optional upstream adapter contract**, and **collectors as distinct from CPJ** (D-INST-5);
6. that the **direct Reactor CPJ route is an internal trusted service boundary**, and that any future public or partner CPJ access must be mediated by an **authenticated Institute oracle-ingress boundary** or another conforming external trust boundary (D-INST-6);
7. the **separation of Institute operational/data/privacy policy from AFI protocol law**, limited to Institute-operated instances (D-INST-7);
8. that **designation is not deployment** — no service is claimed live, and no deployment is authorized by this decision (D-INST-8);
9. that **no protocol authority and no economic, validator, governance, or treasury privilege** transfers to the Institute by virtue of operating a reference service (D-INST-9).

**Does NOT decide (reserved to their own scoped decisions; see §10):** any **API/endpoint/route/query surface** — including Gateway endpoint authority and any read/replay/verify surface over evidence (**ATLAS-GOV**, unfiled); any **rewards / mint / settlement / claims / receipts / on-chain** act (**CHAIN-GOV**, unfiled); the **shapes or semantics** of the USS, CPJ, provider-strategy-binding, or evidence schemas (`afi-config`, delegated by FCP-GOV D-FCP-3; unchanged); **provider or strategy identity, provenance requirements, pipeline law, UWR law, evidence semantics, finality, reputation, incentives, or settlement** (their existing owners, all unchanged); **which specific collectors, providers, or bindings exist** (each is a registry update under FCP-GOV D-FCP-5, reviewed on its own PR); **post-`SCORED` lifecycle** (LIFE-GOV, consumed as-is); and any **deployment, infrastructure, DNS, service account, credential, funding, or onboarding system** (out of scope entirely, §10).

**Nature of the act.** This decision establishes an **institutional-position governance record**: it designates an operator role and documents a target trust boundary. It conveys **no implementation authorization** — there is no implementation-slot ledger, and nothing here permits code, schema, route, deployment, or economic change. It records who is **designated to operate** AFI's official open reference instances; it does not make those instances exist. In-code self-labels confer nothing (`authority-districts-v0.1.md` Part B.1); designation confers nothing beyond what these clauses expressly say.

---

## 1. D-INST-1 — protocol versus operator, and three definitions

**Decision.** AFI's institutional structure separates the **protocol** from its **operators**:

- **AFI Protocol** defines the interoperable rules and contracts — the governed schemas, registries, mathematics, identities, provenance requirements, pipeline law, evidence semantics, and lifecycle. Authority over these lives in AFI's accepted source-of-truth hierarchy (governance → config → math → implementation → tests → maps → docs; `authority-districts-v0.1.md`).
- **AFI Research Institute** is designated to **operate official open reference implementations and hosted research services** that make those contracts accessible.
- **Independent operators** may operate alternative conforming implementations and services.

Three terms are fixed and must be used consistently across governance and documentation:

- **Canonical** — a contract, schema, registry, rule, identity, or mathematical definition that holds authority through AFI's accepted source-of-truth hierarchy.
- **Official reference service** — a service operated, or designated for operation, by AFI Research Institute to provide accessible, tested, documented, open research infrastructure. **An Institute-operated service is not canonical merely because the Institute operates it.**
- **Independent conforming operator** — a third party operating a compatible ingress, collector, Gateway, or AFI stack in accordance with the canonical contracts. **A conforming implementation is not invalid merely because the Institute did not operate it.**

**Scope-guard.** Fixes the **distinction and the three definitions** only. It grants the Institute no authority over any canonical contract, and it invalidates no independent implementation.

---

## 2. D-INST-2 — official Institute Gateway reference service

**Decision.** AFI Research Institute is **designated to operate an official hosted AFI Gateway reference service** for structured financial-intelligence ingress.

The underlying **AFI Gateway** is the open-source ingress implementation homed in `afi-gateway` (MIT-licensed; verified: `POST /api/v1/signals` authenticates an API key, resolves the tenant, rate-limits per key, performs a presence-only field check, stamps provenance `providerId = gateway:<tenantId>`, forwards to the Reactor, and returns the Reactor's answer verbatim; it is **routes-not-writes** and never constructs or writes canonical evidence, enforced by an executable guardrail and a real-MongoDB boundary proof in CI). The Gateway's endpoint and API authority is **reserved to ATLAS-GOV** and is **not** decided here.

The **Institute Gateway reference service** is the official **hosted instance** of that implementation, designated for operation by the Institute so that researchers, analysts, signal providers, agent developers, structured-webhook and API clients, and experimental participants can submit authorized structured intelligence without first deploying the full AFI ingress stack. The Institute's hosted instance **may enforce its own operational policies** — authentication, onboarding, quotas, rate limits, tenant isolation, provider/tenant registration (API-key admission), abuse prevention, audit logging, privacy, retention, and availability. **Those instance policies are not universal protocol law** (D-INST-7). Provider-to-strategy binding is **not** among them: it is a canonical contract in `afi-config`, resolved at the **Reactor** (the Gateway does not authorize strategies — it presence-checks the field and stamps `providerId = gateway:<tenantId>`), and changed only through a reviewed registry update under FCP-GOV D-FCP-5.

**Scope-guard.** Designates an **operator role for a hosted reference instance** only. It changes no Gateway route, contract, or behavior; it grants the Institute no endpoint authority (ATLAS-GOV) and no authority to make its instance policies canonical; and it does not assert the instance is deployed (D-INST-8).

---

## 3. D-INST-3 — official Institute oracle-ingress and CPJ-normalization reference service

**Decision.** AFI Research Institute is **designated to operate an official oracle-ingress reference service** — an authenticated external trust boundary in front of AFI's internal CPJ processing — for message-derived and source-derived candidate signals.

This designated service may support Institute-operated and approved third-party **source collectors** (for example Telegram, Discord, X, email/alert, and news/community adapters — named as **examples, not as guaranteed current integrations**) and may carry responsibilities including collector identity, source authorization, credential validation, provider binding, source provenance, message identity, replay protection, deduplication, rate limiting, CPJ schema validation, audit trails, bounded normalization, and safe forwarding to the internal CPJ processing boundary.

**Verified current state (restated inline):** the internal CPJ processing route exists in `afi-reactor` (`POST /api/ingest/cpj`) and converges on the canonical scoring and Evidence V2 path; a **dedicated external oracle-ingress service does not exist** (the route is served in-process by the Reactor's own server, with authentication optional and off by default); a Telegram collector **client** exists in-repo but is env-gated and undeployed; Discord, X, and email collectors are **not implemented**. The Institute oracle-ingress reference service is therefore **designated and not implemented or deployed** (D-INST-8).

**Scope-guard.** Designates an **operator role for a future external trust boundary** only. It implements no service and no collector, claims no live source integration, and creates no endpoint (ATLAS-GOV) or schema (afi-config) authority.

---

## 4. D-INST-4 — non-exclusivity and independent conforming operators

**Decision.** Both Institute reference-service roles (D-INST-2, D-INST-3) are **non-exclusive**. The Institute is **not** the exclusive operator of AFI ingress. At least three participation models are legitimate and permanently permitted:

1. **Hosted Institute access** — a researcher or provider submits through the Institute Gateway or Institute oracle-ingress service.
2. **Bring-your-own collector** — an independent collector submits through an authorized Institute oracle-ingress boundary, producing CPJ that maps to USS.
3. **Independent conforming operation** — an independent party runs its own source adapters, its own conforming ingress (the open-source Gateway or a conforming re-implementation), and/or its own AFI-compatible infrastructure, submitting canonical USS signals through authorized conforming ingress.

The Institute reference path is designated to be the **lowest-friction** option; it does **not** own all valid paths. Independent conforming operation is an **architectural right**, defined by the afi-config contracts and KATs — not by who operates the service.

**Scope-guard.** Fixes **non-exclusivity and the standing right to conforming operation** only. It obliges no participant to use Institute-hosted services and mandates no submission format beyond what canonical processing already requires (D-INST-5).

---

## 5. D-INST-5 — USS is canonical; CPJ is an optional adapter; collectors are distinct

**Decision.**

- **USS is the canonical AFI signal checkpoint.** All canonical AFI signal processing converges on the governed Universal Signal Schema (currently `afi.usignal.v1.1`, the runtime canon in afi-config) or its accepted canonical successor. At USS and beyond, canonical AFI rules apply.
- **CPJ is an optional upstream adapter contract** for candidate signals derived from conversational, social, oracle, or semi-structured sources (currently `afi.cpj.v0.1`, "the first normalization stage before USS v1.1 mapping"). CPJ is **not** a universal mandatory submission format; ingress paths that already carry structured signals need not pass through CPJ.
- **A source collector is distinct from CPJ.** A collector is a source-specific component that communicates with a platform (Telegram, Discord, X, email, news, …) and produces a structured candidate signal. **CPJ does not itself log into platforms, scrape messages, or discover signals** — collectors and parsers perform those functions; CPJ is the structured handoff of what a collector produced.

The governing rule: **AFI does not dictate how financial intelligence must be discovered; it dictates how intelligence must be represented, attributed, validated, and proven once submitted for canonical processing.** External operators may innovate freely before USS.

**Scope-guard.** Fixes the **canonical convergence point and the CPJ/collector distinction** only. It changes no USS, CPJ, or provider-binding schema (afi-config), and it does not alter the CPJ→USS mapping in the Reactor.

---

## 6. D-INST-6 — the direct Reactor CPJ route is an internal trusted service boundary

**Decision.** The current direct Reactor CPJ endpoint (`POST /api/ingest/cpj`) is governed and documented as an **internal trusted service-to-service boundary**. It must **not** be positioned as a general public API, an alternative public route around the Gateway, an unauthenticated ingestion shortcut, the Institute's final public oracle API, or a universal third-party endpoint.

The rationale is a verified trust property, restated inline: on the direct route, authentication is **optional and off by default** (a single static shared secret via `WEBHOOK_SHARED_SECRET`, compared against a request-body field when set), and provider identity is **self-asserted, not cryptographically authenticated** (no mTLS, signature verification, or IP allowlist). Provider-to-strategy binding, CPJ schema validation, and provenance attribution are **always enforced** on the route regardless of its exposure; ingest deduplication/replay protection is available but **opt-in** (`AFI_INGEST_DEDUPE=1`) and off by default.

The **designated target deployment model** for public or partner CPJ access is:

```text
Institute or approved collector
      ↓
Institute oracle-ingress service   (authentication · source registration · quotas · provider binding · validation · audit)
      ↓
internal Reactor CPJ route
      ↓
CPJ → USS
      ↓
canonical AFI processing
```

Any future public or partner CPJ access must terminate at a **separate authenticated Institute oracle-ingress boundary** (D-INST-3) or another conforming external trust boundary. This decision **documents** that target boundary; it does **not** implement it, does not rename or move the route, and does not change the route's behavior.

**Scope-guard.** Fixes the **internal-boundary classification and the mediated-access model** only. It authorizes no code change, no route change, and no exposure change; Reactor remains the execution engine, not a general public trust gateway.

---

## 7. D-INST-7 — Institute operational and data/privacy policy is instance-scoped, not protocol law

**Decision.** Institute-operated services may establish their own transparent research and service policies — covering source authorization, participant consent, platform terms of service, raw-message retention, personally identifying information, proprietary signal data, delayed disclosure, research-dataset publication, access control, deletion/retention requests, and auditability. These policies **apply only to Institute-operated instances**; they do **not** silently become AFI protocol law, and they bind no independent conforming operator.

Two boundaries are fixed: **raw source content is not automatically written on-chain and is not automatically published** — nothing in an Institute reference-service role makes any submitted signal, raw message, or proprietary alpha artifact public; and the Institute's open-research purpose (reducing integration friction, reproducible experiments, provenance and normalization studies, reference datasets, PoI/PoInsight research, reference adapters) does **not** imply that every submitted artifact is disclosed.

**Scope-guard.** Fixes the **instance-scope of operational/data/privacy policy and the no-automatic-disclosure boundary** only. It writes no privacy policy, promises no dataset, and changes no protocol data-handling law.

---

## 8. D-INST-8 — designation is not deployment

**Decision.** Designation under this decision is **not** deployment. As verified at the pinned commits, **no Institute-operated Gateway or oracle-ingress service is deployed**: there is no CD/deploy pipeline, no hosted URL, DNS, container, or cloud manifest, and the runtime defaults are development/localhost. Accordingly, governance and documentation describing these roles must use status language such as **governed / designated / authorized / reference-service role / not currently deployed**, and must **not** use "operates," "provides," or "hosts" in the present tense for any hosted instance while no live deployment is proven.

**Scope-guard.** Fixes the **designation-versus-deployment truth posture** only. It neither authorizes nor forbids a future deployment — a live deployment, if pursued, is separate work outside this decision's authorization (§10).

---

## 9. D-INST-9 — no authority transfer and no automatic privilege

**Decision.** Operating an official reference service grants AFI Research Institute **no** unilateral authority over AFI Protocol and **no** automatic economic standing. Specifically, the Institute does **not** gain, by virtue of this role:

- authority to alter canonical signal schemas, CPJ or USS semantics, strategy identity, provider attribution, provenance requirements, pipeline law, UWR law, evidence semantics, finality, reputation, incentives, or settlement — these remain with governance, `afi-config`, `afi-math`, and the governed implementation owners (`afi-reactor` constructs Evidence V2; `afi-infra` is the sole canonical writer; `afi-factory` authors pipeline artifacts and is not the ingress operator; `afi-benchkit` remains research/reproducibility tooling);
- ownership or control of `afi-gateway`, `afi-reactor`, `afi-config`, `afi-core`, or `afi-infra` (the Institute is the MIT copyright holder of record across the organization's licenses — an open-source stewardship fact — which is **not** operational or protocol control);
- any reward claim, treasury entitlement, validator status, governance vote, epoch eligibility, or mint/settlement privilege (all reserved to CHAIN-GOV and the applicable governance, unchanged).

**Scope-guard.** Fixes the **no-authority-transfer and no-automatic-privilege** invariants only. It removes no existing authority from any repository and creates no new privilege for any party.

---

## 10. Explicit non-authorizations

This decision does **not** authorize, decide, ratify, or pre-empt any of the following; each remains for its own scoped decision or is out of scope entirely:

- **ATLAS-GOV** — any API/endpoint/route/query surface, including Gateway endpoint authority and any read/replay/verify surface over evidence; the direct CPJ route is neither renamed, moved, nor exposed by this decision.
- **CHAIN-GOV** — any rewards, mint, settlement, claims, receipts, staking, epoch settlement, or on-chain act; and any treasury, validator, or governance privilege for the Institute.
- **Schema/contract changes** — no change to USS, CPJ, provider-strategy-binding, evidence, or any afi-config schema, registry, KAT, provider binding, or strategy binding.
- **Runtime behavior** — no change to any Gateway or Reactor route, handler, authentication mechanism, or dedup/provenance behavior; no runtime code change in any repository.
- **Deployment and infrastructure** — no deployment of the Institute Gateway or oracle-ingress service; no GCP/cloud provisioning, DNS, service accounts, credentials, budgets, funding, or onboarding systems; no privacy-policy legal document; no Research Institute website; no new repository; no collector implementation.
- **Registering any specific participant, collector, provider, or binding** — FCP-GOV D-FCP-5 already provides that mechanism; each registration is a reviewed registry update.
- **Post-`SCORED` lifecycle**, finality writing, reputation, incentives, or the API Atlas — all unchanged and unreached.

---

## Documentation ledger

This decision authorizes **no implementation**. It governs the following **documentation and positioning surfaces**, each of which records (does not extend) this decision. Non-code, non-runtime, non-deployment.

| Surface | Repo | Change | Authorized? |
|---|---|---|---|
| Reference-services specification `specs/AFI_RESEARCH_INSTITUTE_REFERENCE_SERVICES.v0.1.md` + index | afi-docs | New spec + Reference Index / SUMMARY entries; surgical `AFI_Full_Architecture.md` updates (Research Institute, Gateway plane, CPJ lane, ingress-topology diagram, not-implemented list) | Yes — documents this decision; current-state discipline preserved |
| Gateway operation & reference-service note | afi-gateway | Doc-only: designated official hosted reference instance; non-exclusive; routes-not-writes; not the API Atlas; instance policies instance-scoped; not deployed | Yes — doc-only; no runtime change |
| CPJ internal trust-boundary note | afi-reactor | Doc-only: `POST /api/ingest/cpj` is an internal trusted service boundary; future public/partner access mediated by an authenticated oracle-ingress boundary; route unchanged | Yes — doc-only; no runtime change |
| Public positioning | afi-protocol | Concise "protocol vs operation" statement: protocol defines rules; Institute designated to operate official open reference services; non-exclusive; independent operation permitted; no live deployment claimed | Yes — doc-only |
| Organization profile | .github | One concise paragraph mirroring the above | Yes — doc-only |

---

## 11. Supersessions and interactions

- **FCP-GOV (`factory-configurable-pipelines-v1.md`)** — **consumed, not re-decided.** The D-FCP-4 repository roles (Gateway authenticates and routes only; Reactor is the governed replaceable runtime that constructs Evidence V2 and submits through afi-infra; afi-infra is the sole canonical writer; afi-factory authors and is not the executor/ingress operator) are used exactly. The D-FCP-5 generic-registration/fail-closed rule remains the sole mechanism for adding a conforming provider, binding, or strategy; this decision registers nothing.
- **MONGO-GOV (`persistence-v0.1.md`) + OBJ-GOV (`object-identity-v0.1.md`)** — **consumed.** The routes-not-writes boundary, single canonical writer, and `signalId`/USS v1.1 identity are honored, not changed. The ATLAS-GOV Gateway-endpoint reservation these decisions carry (`persistence-v0.1.md:26,126`) is left intact.
- **ATLAS-GOV (reserved, unfiled)** — **honored, not touched.** All API/endpoint/route authority — including any read/replay/verify surface and the Gateway's endpoint contract — remains reserved to ATLAS-GOV. This decision designates an *operator* for a hosted reference instance; it decides no endpoint.
- **CHAIN-GOV (reserved, unfiled)** — **honored, not touched.** No economic, reward, validator, or settlement consequence follows from the operator role.
- **LIFE-GOV / math-authority** — **coordinated, not overridden.** The lifecycle reaches `SCORED`; nothing here writes finality or touches scoring/math law.
- **`authority-districts-v0.1.md`** — its authority-tier discipline ("self-labeling confers nothing") is the basis for D-INST-1's "official ≠ canonical" and D-INST-9's no-privilege rule.

---

**Proposed for owner approval. Authoritative only upon owner merge.** This decision designates AFI Research Institute as the non-exclusive operator of AFI's official open reference services — a hosted Gateway reference service and a designated oracle-ingress/CPJ-normalization reference service — fixes that operation confers no protocol authority and no economic privilege, classifies the direct Reactor CPJ route as an internal trusted service boundary whose public successor must be an authenticated oracle-ingress boundary, affirms USS as the canonical convergence checkpoint and CPJ as an optional upstream adapter contract, and preserves the standing right of independent conforming operators — and nothing else. It touches no schema, no route, no runtime, no deployment, no ATLAS-GOV endpoint surface, no CHAIN-GOV economic act, and no protocol-authority assignment.
