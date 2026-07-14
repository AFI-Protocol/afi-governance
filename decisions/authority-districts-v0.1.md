# AFI Protocol-Development Authority Topology & Canonical District Registry v0.1

**Slot:** `AFI-GOV-AUTHORITY-DISTRICTS-v0.1`
**Status:** **Proposed** for owner approval. **This decision authorizes no implementation and no code, schema, package, contract, persistence, scoring, or economic change.** It becomes authoritative **only** when the owner merges it. Until merged, it is a draft with no force.
**Date:** 2026-07-14
**Type:** Foundational protocol-development governance decision (authority topology + canonical District registry). Docs/governance-ledger only.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` (canonical home `afi-config/codex/governance/droids/`) and its `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md`. Where this decision conflicts with the Charter, the Charter wins.
**Evidence basis:** the read-only Districts / API Atlas reconciliation audit preserved at `afi-docs/specs/audit/districts-api-atlas/` (96 findings; non-authoritative evidence record). This decision evaluates that evidence and the primary governance sources directly; the audit is input, not authority.

---

## 0. Why this decision exists

The reconciliation audit established that AFI's development authority is **real but distributed and partly self-referential**, and that the "District" concept is **governed functionally but numbered only in documentation**. Concretely, verified against current `origin/main`:

- All four accepted `afi-governance/decisions/*` records declare themselves *"Subordinate to `AFI_DROID_CHARTER.v0.1.md`"*, but that Charter lives in **`afi-config`**, not `afi-governance` (`afi-config/codex/governance/droids/AFI_DROID_CHARTER.v0.1.md`; Charter §8, item 3 makes `afi-config/codex/governance/` canonical for droid governance). The instrument the decisions cite as their superior thus sits outside the governance repo.
- Several `afi-docs` documents self-label **"CANONICAL"** (settlement doctrine, District reports) yet have **no ratifying `afi-governance` decision**; governance decisions nonetheless declare themselves subordinate to *"existing settlement/district doctrine in `afi-docs`"* (`decisions/math-authority-v0.1.md:6`).
- The **numbers "District 1 / District 2"** appear only in `afi-docs` reports and `afi-reactor` docs. The governing instrument — `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md` — names districts **by function and never numbers them** (§12, §13).
- Implementation has in at least one case **exceeded its authorization**: `AFI_DROID_PIPEHEAD_ADDENDUM` + the `District 2 D-17` authorization authorize District 2 **M1 only** (*"No runtime wiring"*, D-17 §3; *"does not authorize M2–M6 or any other District work"*, D-17 §2), yet a District-2 "M2" runtime surface shipped in `afi-reactor` (audit finding DIST-01).

This decision fixes the **topology and the registry** so later scoped decisions (object identity, lifecycle, persistence, API Atlas, settlement) rest on a single, explicit authority model. It resolves **none** of those substantive questions (see §8 Explicit Non-Decisions).

---

## Part A — Two governance domains

AFI has **two distinct governance domains**. They must not be conflated, and this decision concerns only the first.

### A.1 Protocol-development governance (the domain of this decision)

**This is a taxonomy of the protocol-development *domain* within which this decision and future scoped decisions operate — not a list of powers this decision exercises.** This decision decides only authority topology and the District registry (Part H). The domain controls how the protocol is *built*: canonical definitions and object identities; repository authority; schemas; lifecycle and finality semantics; authorization of implementation work; scoring-law changes; persistence/finality definitions; settlement *design* authorization; and the creation of bounded agent implementation slots.

Its bootstrap authorization act, today, is **owner merge** of a governance decision or an owner-authored approval recorded on the executing PR (mirroring the existing `uwr-runtime-consumption-v0.1.md` RC-12 pattern).

### A.2 Network / on-chain governance (out of scope here; recorded for boundary clarity)

Controls future *live-network* actions: on-chain parameter proposals; participant or token-holder voting; treasury and vault execution; contract upgrades; emissions changes; reward policies; settlement execution; and timelocked or multisig actions.

### A.3 Relationship

Protocol-development governance is the **bootstrap mechanism used to safely construct** future network/on-chain governance. It does **not** claim that every ordinary code change requires a network vote, and it does not itself execute any on-chain action. Network governance is expected to be established by a **separately governed transition** (Part F.4), at which point some authority now exercised by owner merge may pass to on-chain processes.

---

## Part B — Canonical authority hierarchy

Authority is **domain-scoped, not a single flat ranking.** A lower-numbered tier outranks a higher-numbered one **only where the two actually claim the same domain**; within a domain that a higher instrument has expressly reserved to itself, that instrument wins. In particular, **tier-1 decisions supersede the Charter and the Addendum only *outside* those instruments' stated scope** (droid operating conduct; District framing); **within** that stated scope the Charter/Addendum win — exactly as this decision's front matter and §0 record ("the Charter wins"). With that scoping, conflicts resolve in this precedence order (highest first):

1. **Direct owner-approved governance decisions in `afi-governance/decisions/`**, each **within the domain it expressly states** (Part B.1, "Scope is bounded").
2. **Owner-ratified charters and architecture decisions cited by an accepted governance decision, within their stated scope** — the `AFI_DROID_CHARTER.v0.1.md` (cited as superior by all four accepted decisions) governs **droid conduct**; the `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md` governs the **District framing**. **Standing note (non-circularity):** the Addendum self-labels *"Status: Proposed"* and is today cited by **no accepted decision**; **this decision, upon owner merge, is the accepted decision that confers tier-2 standing on the Addendum's District framing** — and no more. By the same rule, Charter §2's other named docs (the AFI Orchestrator Doctrine in `afi-reactor`; Token Architecture docs) are **not** elevated to tier 2 absent citation by an accepted decision. An `afi-docs` document reaches this tier **only where an accepted decision expressly ratifies or designates it *by name*** — a generic subordination reference that names no specific document (e.g. *"existing settlement/district doctrine in afi-docs"*) does **not** confer tier-2 standing (see Part C).
3. **Governed canonical schemas, registries, formulas, and configuration artifacts, within their expressly delegated domains** — e.g. the `afi-config` UWR profile registry (delegated by `uwr-profile-pin-v0.1.md`), `afi-math` kernels (delegated by `math-authority-v0.1.md`).
4. **Shipped implementation behavior, where it does not contradict higher authority.** Recorded as *reality*, not elevated to *law*.
5. **Canonical documentation designated by governance** — a document is canonical only when a governance decision names it so.
6. **Derived documentation** — reports, diagrams, API maps, examples, implementation notes.
7. **Proposals, drafts, experiments, demos, archived papers, and obsolete artifacts.**

### B.1 Clarifications (binding)

- **Self-labeling confers nothing.** A document does not become protocol law by labeling itself `CANONICAL`, `NORMATIVE`, or `ACCEPTED`. It attains tier 2/3/5 only through an accepted governance decision.
- **Merging code does not ratify a decision.** Code does not silently ratify an unauthorized protocol decision merely because it was merged. Shipped behavior sits at tier 4 (reality), never tier 1 (law), until governed.
- **Shipped ≠ normative.** Existing implementation may be *recorded as shipped reality* without being *declared normative protocol law*.
- **Scope is bounded.** A governance decision has authority only over the domains it expressly states. It gains no authority over unrelated domains.
- **Authority may be delegated, but only explicitly.** Mathematical, schema, config, runtime, persistence, API, and economic authority may live in different repositories — but a repository holds canonical authority in a domain **only** where a governance decision expressly delegates it.
- **Not everything is a governance act.** Ordinary implementation details and bug fixes do **not** require formal governance unless they change canonical meaning, authority, economics, finality, scoring law, or participant rights (Part E).

---

## Part C — Repository authority baseline (bootstrap roles)

Recorded as the **current bootstrap roles**, evidence-derived, **not** a claim that all ownership questions are permanently settled. Each entry states what the repo may hold as authority today; unlisted or contested domains are resolved only by later scoped decisions.

- **`afi-governance`** — canonical home for **protocol-development decisions and authorization records** (`decisions/`). Its executable stubs (e.g. `validator/proposal_scorer.ts`, a `Math.random()` placeholder) are **not** protocol authority (consistent with `math-authority-v0.1.md:80`).
- **`afi-config`** — canonical governed **configuration / schema / registry** artifacts **only where expressly delegated** (e.g. the UWR profile registry per `uwr-profile-pin-v0.1.md`; and the District 2 **M1** provenance schema drafts per D-17, see Part D). It is also the canonical home of the **DROID Charter and Pipehead Addendum**, which are classified **by their stated scope** (droid operating conduct; District framing) — **not** treated as universal protocol law over unrelated domains.
- **`afi-docs`** — **explanatory and derived documentation by default (tier 6).** A specific `afi-docs` document or surface is canonical **only** when a governance decision designates it. Settlement/District doctrine currently self-labeled "CANONICAL" is **not** ratified by this decision.
- **`afi-math`** — **mathematical kernels and formulas within explicitly governed authority** (sole canonical off-chain math per `math-authority-v0.1.md`). *(Note for a later decision, not resolved here: consumers currently pin different `afi-math` commits — `afi-core` vs `afi-mint` — audit finding DIST-H-02.)*
- **`afi-core`** — reusable **protocol/runtime primitives and validators**; may wrap `afi-math`; holds **no** unilateral economic or governance authority.
- **`afi-reactor`** — **scoring and orchestration implementation**; "**not a math authority**" (`math-authority-v0.1.md:74`); holds **no** unilateral protocol-law authority. Its District-2 runtime surface is addressed in Part D.
- **`afi-gateway`** — **API transport / exposure**; holds **no** unilateral domain-schema authority (its client surfaces are self-labeled Dev/Demo-only, and its divergent `uwrAxes` shape is recorded as **non-conformant** per `uwr-profile-pin` UP-4 — not authoritative).
- **`afi-infra`** — **infrastructure and persistence implementation**; holds **no** unilateral canonical-object or finality authority. Which persisted store/shape is canonical is **not** decided here.
- **`afi-mint`, `afi-token`, `afi-econ`** — implemented or proposed **economic machinery**, subject to explicit **economic and settlement governance**; `afi-econ` is research/non-canonical until promoted (`math-authority-v0.1.md`). No economic authority is granted or altered here.

This Part **does not** resolve object identity, lifecycle finality, MongoDB ownership, role weights, settlement doctrine, or contract deployment.

---

## Part D — Canonical District registry (initial)

Districts are **"Droid factory districts"** as defined by `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md`: governance-gated, separately-authorized implementation/mission units. The Addendum names districts **by function and does not number them** (§13). The numbers below are hereby **adopted as the canonical registry identifiers**, bound to the Addendum's functional names, so the docs-layer numbering and the governance functional naming are reconciled into **one** registry. **Only** the two evidenced districts are created; no others.

| Field | **District 1** | **District 2** |
|---|---|---|
| Canonical identifier | `District 1` | `District 2` |
| Human-readable name | Signal-Evaluation Pipehead POC | Canonical Data & Provenance Boundary |
| Functional name (Addendum) | Signal Evaluation Pipehead System (Addendum §12) | Provenance (Addendum §13 roster) |
| Purpose | Prove Droids can operate AFI's evaluation DAG (five analysis lanes → deterministic scoring/validation/audit) without becoming the source of financial truth | Define the canonical-vs-runtime data boundary, hash doctrine, and provenance/disclosure structure |
| Authority source | GOVERNED — Addendum §9/§12/§13 | GOVERNED (scope-limited) — `AFI_DROID_PIPEHEAD_ADDENDUM` (roster) + `afi-docs/reports/district-2-d17-implementation-authorization.md` (**M1 only**) |
| Implementation repo | `afi-reactor` (`src/pipeheads/`) | `afi-config` (schemas, M1); `afi-reactor` (`src/pipeheads/provenance/`, D2-native surface) |
| Implementation status | IMPLEMENTED (non-production POC) | **M1** authorized + implemented (afi-config schema drafts + tests); **"M2" runtime surface shipped in `afi-reactor`** |
| Production status | Non-production / demo-only | Non-production |
| Governed scope | The five-lane evaluation DAG POC; deterministic scoring/validation/audit; Droids may not become the source of financial truth (Addendum §14) | **M1 only** — afi-config schema drafts + tests, **"No runtime wiring"** (D-17 §3); the M0 report is a *planning baseline*, **"a planning artifact, not an implementation authorization"** (`district-2-m0-canonical-data-boundary-and-hash-doctrine.md:589`) |
| Explicitly deferred scope | Any production promotion; any financial-truth authority | **M2–M6** (D-17 §2: "does not authorize M2–M6 or any other District work"); canonical-hash unification; any settlement/reward/mint/anchor attachment |

### D.1 District 2 "M2" authorization-gap treatment (Part-D core)

The primary evidence is unambiguous on the **facts** and is recorded here without softening: the **only** District-2 authorization instrument (`district-2-d17-implementation-authorization.md`) authorizes **M1 only** and states it "does not authorize M2–M6 or any other District work," and it mandates that each later phase be separately authorized. A District-2 **"M2" D2-native artifact surface nonetheless shipped in `afi-reactor`** (`src/pipeheads/provenance/`). **No M2 authorization instrument exists in `afi-docs/reports/` or `afi-governance/decisions/`** (audit finding DIST-01); the reactor "M2" also collapses the M0 plan's separate M2/M3/M4 milestone scopes into one surface (audit finding DIST-03). This decision does **not** declare that shipped work to have "always been authorized."

**Recorded treatment (this decision): Option 2 — shipped-but-non-normative.** The District-2 M2 runtime surface is recorded in the registry as **shipped reality that is not normative protocol law**, pending a separate District-2 ratification decision. This is the evidence-consistent and Charter-consistent choice **for a topology/registry decision**, because the alternative — prospective ratification (Option 1) — is itself a **material District-scope authorization act**, which this decision's own scope excludes (§8) and which the Charter reserves to an explicit owner decision ("Propose, Don't Decide"). Recording M2 as tier-4 *reality* (Part B) preserves the historical authorization gap exactly as the audit found it (finding DIST-01) without either blessing or deleting the work.

**⚠ OWNER-CHOICE CLAUSE (D-CHOICE-1).** The ultimate disposition of the District-2 M2 surface is the **owner's** to make and is **not** silently decided here. The owner may, in a **separate** District-2 ratification decision:
- **(a)** ratify the shipped non-production M2 surface **prospectively**, expressly preserving the record of its historical authorization gap; **or**
- **(b)** leave it **shipped-but-non-normative** (this decision's recorded default) pending redesign or re-scoping; **or**
- **(c)** direct that the surface be gated/rolled back to the authorized M1 boundary.

This decision selects **(b)** as the *registry's current record* and surfaces **(a)** and **(c)** as owner options; it makes none of them a fait accompli.

### D.2 Future districts — unnumbered candidates only

The Addendum's functional roster (§13) names future districts that are **not created here and are not active Districts**: **reputation, contracts, settlement-readiness, monitoring, documentation, external-agent interfaces** (plus provenance, now realized as District 2). They are recorded as **unnumbered, uncreated candidates**. Each requires a new Addendum version or a separate mission-specific authorization before it becomes a District. **No District 0, District 3, or any higher-numbered District is created or implied.**

---

## Part E — Decision classes and change threshold

### E.1 Requires protocol-development governance (a decision or owner-recorded authorization)

Canonical object identity; identifier continuity; lifecycle / finality semantics; canonical persistence owner; scoring-law or governed-config value changes; role definitions or economic weights; epoch / receipt / reward / claim semantics; settlement doctrine; contract deployment or retirement; changes to participant rights or treasury authority; **creation or material scope change of a District**; and designation of a canonical API Atlas.

### E.2 Normally implementation-review-only (no formal governance)

Refactors preserving governed behavior; tests; comments; CI maintenance; internal performance improvements; bug fixes that **restore** already-governed behavior; and documentation corrections that do not change authority.

### E.3 Ambiguous changes

A change whose class is unclear **must be proposed for classification** by the owner. An agent or implementer **may not** decide the policy question implicitly by proceeding.

---

## Part F — Agent authority (bootstrap rule)

1. Agents may **inspect, propose, draft, test, and implement only within explicit scope**.
2. Agents **may not self-ratify governance.** Producing or merging an artifact is not its ratification.
3. Agents **may not treat a broad mission prompt as permission to cross an owner gate.** A mission provided in advance does not authorize proceeding past a gate that requires owner action.
4. **Owner merge — or an owner-authored approval recorded on the executing PR (the `uwr-runtime-consumption-v0.1.md` RC-12 pattern) — is the current bootstrap authorization act.** Future DAO / on-chain governance may replace or supplement the owner gate **only through a separately governed transition** (Part A.3), which is itself a future scoped decision.

---

## Part G — Relationship to existing decisions

- **`AFI_DROID_CHARTER.v0.1.md` / `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md`** (afi-config): unchanged and not amended. This decision **classifies** them by scope (tier 2 where cited) and reconciles the District numbering to the Addendum's functional names; it does not rewrite them.
- **`math-authority-v0.1.md`, `mint-formula-bt-86b-alignment-v0.1.md`, `uwr-profile-pin-v0.1.md`, `uwr-runtime-consumption-v0.1.md`**: unchanged. Their delegations (afi-math kernels; afi-config UWR registry; the staged runtime-consumption ledger) are the model for Part B tier 3 and remain in force as written. No open decision, non-authorization, or ledger row in any of them is altered.

---

## Part H — Explicit non-decisions

This decision does **not** decide, authorize, or ratify any of the following (each remains for a separate scoped decision):

- canonical scored-signal shape;
- canonical strategy identifier;
- lifecycle states or the finality writer;
- canonical MongoDB store;
- Gateway write authority;
- API Atlas designation;
- epoch settlement object;
- receipt standard;
- role weights;
- staking thresholds;
- emissions, mint mechanics, reward allocation, claim, or vault routing;
- settlement;
- contract deployment;
- production scoring law;
- UWR deferred work (KAT-RERUN, CONFIG-PACKAGING, flag-default flip, `uwr-default-stub` retirement, UP-8 decay canonicality, the 0650 erratum, gateway `uwrAxes` cleanup);
- and — beyond recording it as shipped-but-non-normative and surfacing the owner choice (D.1) — the prospective ratification, rollback, or re-scoping of the District-2 "M2" runtime surface.

It creates **no** implementation slot and authorizes **no** repository code, schema, package, contract, persistence, or economic change.

---

**Proposed for owner approval. Authoritative only upon owner merge. No implementation is authorized by this decision.**
