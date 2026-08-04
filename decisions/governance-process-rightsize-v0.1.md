# Governance Process Right-Size v0.1 (GPR-GOV)

**Slot:** `AFI-GOV-GOVERNANCE-PROCESS-RIGHTSIZE-v0.1` (GPR-GOV)

**Status:** **Proposed** — not accepted until owner merge of the afi-governance PR that carries this file. This filing does **not** self-accept and does **not** flip its own Status line.

**Date:** 2026-08-04

**Type:** Scoped **process** governance decision (how future ledger filings are authored and sized). Documentation and ledger-process only. It authorizes **no** schema, route, runtime, scoring, hash, golden, deployment, credential, mint, or settlement act, and decides nothing beyond its four clauses.

**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` and `decisions/authority-districts-v0.1.md`. **Consumes (does not re-decide)** CONST-GOV's no-rewrite law and authority topology. **Supersedes, prospectively and only as stated in D-GPR-1 and D-GPR-2, the informal convention that every new filing must walk every prior decision by name.** Accepted decision files are never rewritten (CONST-GOV D-CONST-8). Where this decision conflicts with the Charter, the Charter wins; where it conflicts with any accepted decision on substance other than filing-process convention, that decision wins.

**Evidence basis (input, not authority):** Measured 2026-08-04 against `afi-governance` @ `4af541f`: **30** accepted decision files; **796,979** bytes total; **mean 26,566** bytes; newest full-treatment filings **40.5–46.1 KB** (`challenge-retirement-v0.1.md`, `timeframe-decay-resolution-v0.1.md`, `evidence-v3-provider-provenance-v0.1.md`) with supersessions sections of several KB that restate untouched decisions. A short operational precedent already exists (`decay-horizon-purge-v0.1.md`, **5,682** bytes) that collapses untouched decisions into one bullet — proving the ledger already tolerates short form when blast radius is small. Investor-facing friction is compounding: cost-per-filing grows roughly linearly with ledger size under a mandatory full walk, so total ceremony cost is quadratic. Nine decisions were filed in the four days preceding this measurement, several filing→production same day — rigor is not the bottleneck; **undifferentiated ceremony** is.

**Bridge statement:** This filing is the **last** filing expected under the old "pay a full walk even when nothing is touched" informal convention. It demonstrates the new short form for a process-only change (following the DHP-GOV size class). **Acceptance of this filing is what switches the convention** for subsequent filings. Until acceptance, authors continue under prior practice.

**Relevance (Appendix B filter):** Outside the building, this unblocks cheaper, faster recording of non-money work and makes the money-relevant trail easier to find — investors see fewer competing process documents and a measurable drop in filing cost, without weakening settlement defensibility.

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these four):**

1. **D-GPR-1** — Replace the mandatory walk-every-prior-decision convention with a touch-scoped supersessions walk, backed by a generated decisions index.
2. **D-GPR-2** — Tier filings by blast radius: full treatment vs short record.
3. **D-GPR-3** — Preserve the money-relevant record; short form never covers money-relevant blast radius.
4. **D-GPR-4** — Require a one-line external relevance statement on every filing (full or short).

**Does not decide (expressly):** any scored value, hash preimage, golden byte, schema shape, registry pin, decay law, UWR law, evidence contract, lifecycle state, mint/settlement/token surface, or dormant-surface disposition (inventory D1–D8 remain owner questions). It does **not** unify the two `afi.hash.v1` hashing laws. It does **not** authorize deletion of code or fixtures.

---

## 1. D-GPR-1 — touch-scoped supersessions + generated index

**Decision.**

1. **Touch-scoped walk.** A filing's supersessions / interactions section MUST enumerate, by name, only the accepted decisions this filing **consumes with effect**, **amends**, or **supersedes**. Decisions that are merely ambient background MAY be covered by a single closing bullet of the form: *"Every other accepted decision on `decisions/INDEX.md` — untouched."* A filing MUST NOT be rejected solely for omitting an exhaustive name-by-name restatement of untouched decisions.
2. **Generated index.** `decisions/INDEX.md` is the single register of decision files and Status values. It is generated from Status lines (see `scripts/generate-decisions-index.py`). The index does not rewrite accepted decisions. Authors refresh it when adding a filing. Status flips after owner merge continue to be recorded in the decision file itself (existing practice); the index is regenerated to match.
3. **Quote accuracy unchanged.** Where a filing amends or supersedes a prior clause, it MUST still cite the prior file and the affected clause precisely. Cutting the untouched walk does not cut citation duty for what is actually touched.

**Scope-guard.** Changes filing-process convention only. It does not weaken CONST-GOV's no-rewrite law, does not allow silent supersession without naming the touched decision, and does not make `reports/` authoritative.

---

## 2. D-GPR-2 — blast-radius tiers

**Decision.** Every filing declares exactly one tier:

### Tier F — Full treatment (money-relevant or integrity-relevant)

**Required when the filing authorizes or records a change that moves any of:** a scored value; a hash preimage or hash law; a golden/KAT/oracle fixture byte; a governed schema that those surfaces depend on; or a token, mint, settlement, emissions, or staking surface.

**Minimum content:** scope (decides / does not decide); evidence basis with file:line citations where claims about the tree are made; numbered decision clauses with scope-guards; explicit non-authorizations; touch-scoped supersessions (D-GPR-1); relevance line (D-GPR-4). Length is whatever the substance needs — **no artificial KB cap** on Tier F.

### Tier S — Short record (hygiene / process / docs)

**Allowed only when none of the Tier F triggers apply.** Typical: process rules, documentation corrections that do not move goldens, dead-code harvest *after* an accepted disposition already named the survivor, type/hygiene work with proven zero behavior change.

**Minimum content (target under ~2 KB of prose, exclusive of the generated index update):** one paragraph of ruling; scope-guard; touch-scoped supersessions (often a single "untouched" bullet); relevance line (D-GPR-4). The DHP-GOV filing (~5.7 KB including headers) is the size-class precedent, not a floor.

**Retrospective sizing (measurement, not reclassification).** Of the **30** accepted ledger files as of this filing's evidence basis, a conservative read is: **~20** would remain **Tier F** under this rule (score/hash/golden/schema/lifecycle/settlement-adjacent), and **~10** could have been **Tier S** (city-retirement, acceptance-record-normalization, strategy-version-semantics, decay-horizon-purge, persistence-impl authorization wrapper, and several district/process records whose operative act was consolidation or process rather than score movement). This is a sizing estimate for investor metrics; it does not rewrite those files' Status or tier.

**Scope-guard.** Mis-tiering a Tier F change as Tier S is a process defect: the filing is incomplete until upgraded. Short form is never a path to skip evidence for money-relevant acts.

---

## 3. D-GPR-3 — money-relevant record preserved

**Decision.** The purpose of right-sizing is to **cut ceremony, never the record**, for changes that will matter when settlement carries real value.

1. Tier F filings remain the durable trail for scored values, hashes, goldens, and token/settlement surfaces.
2. Tier S MUST NOT authorize a Tier F act. If discovery during a hygiene PR shows a score/hash/golden/settlement impact, stop and file Tier F (or amend the in-flight filing upward) before merge.
3. Accepted decisions stay append-only / prospectively superseded (CONST-GOV). This filing adds no rewrite path.

**Scope-guard.** If any clause of D-GPR-1 or D-GPR-2 were read to weaken Tier F duties, D-GPR-3 controls and that reading is rejected.

---

## 4. D-GPR-4 — external relevance line

**Decision.** Every filing (Tier F or Tier S) MUST include a short **Relevance** statement answering: *what does this unblock for someone outside the building?* One or two sentences. This is a cheap filter against rigor-without-purpose; it is not a marketing section and MUST NOT expand into roadmap narrative.

**Scope-guard.** Relevance is required prose, not a new approval board. Absence of a Relevance line is a process defect for filings authored after acceptance of this decision.

---

## Explicit non-authorizations

- No code deletion, harvest, or dormant-surface disposition.
- No change to hashing laws, decay laws, UWR, evidence V3, lifecycle, or registries.
- No self-acceptance; Status remains Proposed until owner merge.
- No authority to treat `reports/` as governance.
- No unification of composition-law and evidence-law `afi.hash.v1` implementations.

---

## Supersessions and interactions (touch-scoped; D-GPR-1 demonstrated)

- **Informal full-walk convention** (practice visible in CHR-GOV / TDR-GOV / EV3-GOV supersessions sections) — superseded prospectively by D-GPR-1 for filings authored after acceptance of this decision. Those accepted files are not rewritten.
- **DHP-GOV (decay-horizon-purge-v0.1)** — consumed as the short-form size-class precedent for Tier S; not amended.
- **CONST-GOV (constitutional-architecture-v1.0)** — consumed: no-rewrite law re-affirmed (D-GPR-3); this filing amends process convention only, not constitutional substance.
- **AUTH-GOV / authority-districts-v0.1** — consumed: district and reserved-scope topology untouched.
- **Every other accepted decision on `decisions/INDEX.md`** — untouched: no scorer, golden, hash, schema, registry, evidence, identity, lifecycle, or economic act.

---

**Status footer:** **Proposed** — awaiting owner merge. Acceptance constitutes D-GPR-1 (touch-scoped walk + index), D-GPR-2 (Tier F / Tier S), D-GPR-3 (money-relevant record preserved), and D-GPR-4 (relevance line).
