# AFI Decay-Horizon Purge v0.1 (DHP-GOV)

**Slot:** `AFI-GOV-DECAY-HORIZON-PURGE-v0.1` (DHP-GOV)
**Status:** **Proposed** owner decision — acceptance is constituted by the owner's merge of the afi-governance PR carrying this file. The substantive ruling it records is already the founder's: the single-word instruction **"Purge"** of 2026-08-03, given in direct answer to the question whether legacy-law outcome rows were worth preserving ("I don't want to pollute our codebase, database, or strategy unless we have a really good reason for keeping that"). The operational purge and the code retirement execute on that instruction; this filing records them on the ledger.
**Date:** 2026-08-03
**Type:** Scoped operational-plane governance decision (outcome-data law simplification). No evidence-plane act, no scorer/UWR/schema/composition change, no golden movement, no hash rotation. It authorizes exactly **one bounded implementation act** (one afi-reactor PR + one operational purge of the analytics store) and decides nothing beyond its two clauses.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` and `decisions/authority-districts-v0.1.md`. **Consumes (does not re-decide)** all twenty-seven prior decisions. **Supersedes, prospectively, in two bounded respects of `decay-horizon-alignment-v0.1.md` (DH-GOV) and nowhere else:** (1) D-DH-2(3)'s legacy-completion branch — pre-cutover docs no longer "complete their capture under the legacy global set"; they are never captured; (2) D-DH-3(1)'s sentence "Existing v0 rows are valid historical rows and are never rewritten" — v0 and all other non-decay-derived rows are **deleted**, not preserved. Where this decision conflicts with the Charter, the Charter wins; where it conflicts with any accepted decision other than the two bounded DH-GOV respects above, that decision wins.
**Evidence basis:** afi-governance @ `75499be`, afi-reactor @ post-#73 main, live stores as of 2026-08-03 ~07Z: `signal_outcomes` carried only legacy-law rows (v0 shape plus six v0.1 `legacy-global` rows written by the 06:45Z job run); zero `decay-derived` rows existed yet (first post-cutover signal had not matured), making this the cheapest possible moment to converge on one law. Forward math: at the live signal rate (~17–20/day × 3 derived rows each) the purged corpus is out-accrued by clean one-law data within days; the purged 4h/24h windows measure beyond the qualified life bound recorded in DH-GOV §1.4.

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these 2):**

1. **D-DHP-1 — One law on the books.** The legacy global horizon set (`1h/4h/24h`) is **retired**: scoring-context docs captured before the DH-GOV cutover, docs with an absent or malformed decay stamp, and any run under an unparseable cutover are **never captured** (skip — surfaced in the job summary as a dedicated counter), not captured under a fallback law. The only horizon bases that can produce rows are `decay-derived` and `operator-override`. All existing non-`decay-derived` outcome rows (the v0 corpus and the six v0.1 `legacy-global` rows) are **purged** from `afi_signal_analytics.signal_outcomes` — an operational-plane deletion (MONGO-GOV D-MONGO-4 plane separation honored; the canonical evidence plane is untouched, D-MONGO-5 unimplicated).
2. **D-DHP-2 — The bounded act.** One afi-reactor PR (capture skip semantics, legacy-set removal, derivation-test updates) plus one operational purge, sequenced **code → job-image deploy → purge** so the hourly cron cannot re-create legacy rows between deletion and rollout. Purge counts are recorded in the PR/execution record. Deployment itself remains an operational act.

**Does not decide (expressly):** anything about evidence records, scoring, composition, decay templates, or the DH-GOV derivation law itself (all DH-GOV clauses stand except the two bounded respects superseded above); no backfill of any kind (the pre-cron era stays uncovered, now permanently and uniformly); no readout surface (owner ruling stands: parked until ≥150 rows/horizon — now counted purely in one-law rows); no front-end act.

---

## 1. Supersessions walk

- **DH-GOV (decay-horizon-alignment-v0.1)** — amended in exactly the two bounded respects stated in the Governance line (legacy-completion branch → never-capture; v0-rows-preserved → purged). Every other clause — the derivation law {⌈H/4⌉, ⌈H/2⌉, H}, the stamped-value principle, the cutover instant, outcome row v0.1, the self-cleaning probe, the D-MONGO-5 probe-row carve-out, the pin walk — stands unchanged.
- **MONGO-GOV (persistence-v0.1) + MONGO-IMPL** — consumed: the purge is an operational-plane deletion in `afi_signal_analytics`; D-MONGO-4 plane separation honored verbatim; D-MONGO-5 governs the canonical evidence record and is untouched by this act.
- **EQ-GOV, AR-GOV, EV3-GOV, DSC-GOV, SV-GOV, UP-GOV, RC-GOV, DIR-GOV, FCP-GOV, PBF-GOV, ARN-GOV, R1-GOV, CONST-GOV, CITY-RET-GOV, INST-GOV, ATLAS-GOV, LIFE-GOV, D1CAP-GOV, D2R, OBJ-GOV, math-authority, mint-formula-bt-86b-alignment, and every other accepted decision** — untouched: no scorer, golden, hash, schema, registry, evidence, identity, or economic act.

---

**Status footer:** **Proposed** owner decision — acceptance is constituted by the owner's merge of the afi-governance PR carrying this file, recording the founder's 2026-08-03 "Purge" ruling as D-DHP-1 (one law on the books; legacy set retired; non-derived rows purged) and D-DHP-2 (the bounded code + purge act).
