# D5 Scoring Silent-Defaults — Zero-Movement Declaration v0.1 (D5-GOV)

**Slot:** `AFI-GOV-D5-SCORING-SILENT-DEFAULTS-ZERO-MOVEMENT-v0.1` (D5-GOV)

**Status:** **Proposed** — not accepted until owner merge of the afi-governance PR that carries this file. This filing does **not** self-accept and does **not** flip its own Status line. The linked afi-core / afi-reactor PRs implement this option **contingently**; implementation is not an argument for acceptance.

**Date:** 2026-08-04

**Type:** Scoped **Tier S** hygiene / correctness-gate declaration (no score movement). Size-class precedent: DHP-GOV short form. If GPR-GOV (`governance-process-rightsize-v0.1`, still Proposed as of this filing) is later accepted, this filing is intended to sit under its Tier S rules; until then it stands on the same short-record practice DHP-GOV already demonstrated.

**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` and `decisions/authority-districts-v0.1.md`. **Consumes (does not re-decide)** FLPR-GOV (five-lane view projection), UP-GOV / RC-GOV (UWR consumption), EQ-GOV / AR-GOV (adjacent scorer inputs). **Authorizes no** score change, hash preimage change, golden refresh, era cutover, or deploy.

**Evidence basis (input, not authority):** Measured 2026-08-04 on `afi-reactor` @ `0f472b9` / `afi-core` @ `dcb4916` worktrees: (1) `brokeEmaWithBody` produced only as a pin in `laneView.viewTechnical` with **no candle producer** anywhere; read by structure and risk axes; forcing `true` on all 12 oracle goldens yields ΔUWR = **−0.2875** (100% affected); (2) `conviction = uwrScore` alias; both keys in `SCORE_DECIMAL_KEYS` — omitting conviction **does** change `outputHash`; live reactor path does **not** weight-combine the two; (3) historical score↔outcome re-correlation under counterfactual options **not feasible here** (no analytics Mongo URI; candles not persisted; every live record already carries stub `false`). Provenance golden pin unchanged: `312da1180b0bd418c03f595093516ebdc755ba81465a0b526ace43d002126e06`.

**Relevance:** Outside the building, this closes correctness-gate item #1 ("no silent defaults in scoring") without changing any emitted commercial score — so the product can keep shipping while the owner separately decides whether to implement a real EMA-break guard or a distinct conviction metric (each a Tier-F scoring change).

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these 2):**

1. **D-D5-1 — `brokeEmaWithBody` is an explicit unimplemented-input stub.** The live value is the named constant `BROKE_EMA_WITH_BODY_UNIMPLEMENTED_STUB` (`false`) in `afi-core/analysts/froggy.enrichment_adapter.ts`, pinned by reactor `viewTechnical`. Adapter `??` falls back to that same constant. This is **not** a silent missing-data default. Wiring a candle-derived producer, changing the stub value, or removing the input from the axes is a **separate modelling / Tier-F** act — expressly **not** decided here.

2. **D-D5-2 — `conviction` is a declared alias of `uwrScore` for froggy `trend_pullback_v1`.** Emitting both names is intentional record shape. Downstream MUST NOT treat them as independent quality numbers in a weighted sum without a further modelling filing. Stopping emission, or computing a distinct conviction, is **not** decided here (either moves hashes and/or scores).

**Does not decide (expressly):** any real candle definition of EMA-body break; any distinct conviction formula; any UWR weight change; any era / `analystConfigHash` cutover; any golden regeneration; any deploy; disposition of adjacent silent defaults (`haFlatBackConfirmed`, HTF bias neutrals) — those remain open inventory items.

---

## 1. Contingent implementation act

Owner acceptance of this filing **ratifies** the zero-movement code on:

- `afi-core` branch `mission/d5-zero-movement-v0.1` (merge **first** — reactor CI checks out afi-core default branch with no `ref:`)
- `afi-reactor` branch `mission/d5-zero-movement-v0.1` (merge **second**)

Verification bar for that act: full suites green; oracle golden sha256 list byte-identical to pre-change; 12/12 oracle `scorerInput` → `analystScore` identity preserved.

**If the owner chooses a different option from the D5 options table** (implement producer / remove axes / distinct conviction / stop emitting conviction), reject or supersede this filing and do **not** merge these PRs as-is — those options need Tier-F filings, golden refresh, and cutover.

---

## 2. Touch-scoped supersessions

- **FLPR-GOV** — consumed: view projection remains the pin site; this filing only names the stub law explicitly.
- **Every other accepted decision** — untouched: no score, hash law, golden, schema, registry, evidence, identity, or economic act.

---

**Status footer:** **Proposed** — awaiting owner merge. Do not flip Status in this PR.
