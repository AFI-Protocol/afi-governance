# AFI Mint Formula and B(t)/86B Alignment v0.1 (PR-2)

**Status:** Accepted owner decision for the AFI v1 interpretation. **Does not authorize implementation changes by itself.**
**Date:** 2026-07-04
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md`, `decisions/math-authority-v0.1.md`, and existing settlement/district doctrine in `afi-docs`. Where this decision conflicts with the Charter, the Charter wins.

---

## 1. Purpose

`decisions/math-authority-v0.1.md` recorded which repo owns which class of mathematical authority, and left several items open — most directly Open Decision 1 (mint formula / payout model alignment) and Open Decision 7 (B(t) / 86B cap reconciliation).

This decision record resolves the **AFI v1 interpretation** of:

- `B(t)` (the production emissions baseline instance)
- the 86B hard supply cap
- the mint formula / payout skeleton
- the status of any direct clamp formula
- Q/N/R-style factors
- AIM activation status
- AAG activation status
- what future `afi-mint` cleanup is allowed to assume

This is a governance/docs decision only. It does not change runtime behavior anywhere.

## 2. Sources

1. **Existing governance decision:** `decisions/math-authority-v0.1.md` (merged via afi-governance PR #6, merge commit `d421447`).
2. **AFI whitepaper doctrine** (*"AFI: An Agentic Financial Intelligence Market"*):
   - §9.4 defines epoch emissions as `E_t = B(t) AIM_t`, and defines the AFI Index / impact-index logic.
   - §9.5 defines AAG role-pool allocation.
   - §9.6 defines SES smoothing/rate limits.
   - §9.7 defines payouts as pro-rata distribution by verified credits inside role pools, with maturity hold.
   - §9.9 defines failure-mode mitigations such as HHI breakers and correlation penalties.
3. **afi-math PR-1 result** (merged, merge commit `f20c0dd` in `afi-math`): the current `afi-math` three-phase front-loaded 86B emissions schedule is hardened with deterministic tests/goldens. PR-1 did not change `src/` behavior.

## 3. Decision Summary

| # | Decision | v1 outcome |
|---|---|---|
| D1 | Production B(t) | The `afi-math` three-phase 86B emissions schedule is the pinned AFI v1 production instance of `B(t)` |
| D2 | 86B hard cap | 86B AFI is the hard maximum AFI supply cap for v1 |
| D3 | Mint settlement skeleton | Epoch budget from pinned `B(t)` → `AIM_t` (= 1 for v1) → role pools via governed baseline role weights → pro-rata verified credits → challenge/maturity/escrow before settlement |
| D4 | Direct clamp formula status | Not adopted as independent AFI v1 mint authority |
| D5 | Q/N/R-style factors | Feed credit/merit calculations, not independent direct mint authority |
| D6 | AIM activation status | Published doctrine; inactive for v1 launch (`AIM_t = 1` unless separately governed) |
| D7 | AAG activation status | Published doctrine; adaptive merit routing inactive for v1 launch (governed baseline role weights first) |
| D8 | Future afi-mint cleanup assumptions | Recorded below; this decision does not itself modify `afi-mint` |

## 4. Detailed Decisions

### Decision 1 — Production B(t)

**Recorded:** The current `afi-math` three-phase 86B emissions schedule is the **pinned AFI v1 production instance of `B(t)`**.

Clarifications:

- The whitepaper geometric-with-floor `B(t)` example remains a **baseline-family/conceptual expression**, not the v1 production schedule.
- Any future replacement or activation of a different `B(t)` requires governance, version pins, KATs/goldens, and explicit migration rules.
- The nonzero B∞ infinite-emissions concern raised in `math-authority-v0.1.md` (Open Decision 7) is avoided for v1 because the pinned production `B(t)` is the **finite** three-phase 86B schedule.

### Decision 2 — 86B hard cap

**Recorded:** **86B AFI is the hard maximum AFI supply cap for v1.**

Clarifications:

- The cap must trace through governance, `afi-math` goldens/test vectors, and `afi-token` on-chain enforcement.
- `afi-token` may enforce the hard outer boundary on-chain, while `afi-math` supplies the canonical off-chain epoch schedule.
- Mirrored constants require traceability and tests; this decision does not modify contracts.

### Decision 3 — Mint settlement skeleton

**Recorded:** AFI v1 mint settlement follows the whitepaper-aligned skeleton:

1. Determine the epoch budget from the pinned `B(t)`.
2. Apply `AIM_t`. For v1 launch, `AIM_t = 1` unless separately governed.
3. Route the epoch budget into role pools using governed baseline role weights.
4. Allocate each role pool pro rata by verified credits.
5. Apply challenge/maturity/escrow rules before final settlement.

Clarifications:

- The production skeleton is **epoch budget → role pools → pro-rata verified credits**.
- It is **not** independent direct per-signal mint authority.
- Minting remains gated by vault finality, challenge windows, maturity rules, and receipt-verified work.
- This decision does not choose numeric baseline role weights: **no accepted governance record in `afi-governance` currently defines numeric baseline role weights**, so they remain a **required follow-up decision before live mint activation**.

### Decision 4 — Direct clamp formula status

**Recorded:** A direct formula such as `clamp(B(t) · Q · N · R · E_epoch)`, if present in docs/comments/drafts, is **not adopted as independent AFI v1 mint authority**.

Clarifications:

- Q/N/R-style factors may remain meaningful.
- They should feed verified credits, role merit, analyst scoring, AAG merit, or related profile calculations.
- They must not independently create uncapped or separate token issuance outside the epoch pool.
- Any direct clamp formula retained for research/docs must be marked as **non-authoritative until governed**.

### Decision 5 — Q/N/R-style factors

**Recorded:** Quality, novelty, reputation, durability, timeliness, reliability, and similar factors **feed credit/merit calculations, not independent direct mint authority**.

Clarifications:

- These factors can influence `C_i` verified credits, role merit `m_r,t`, AAG merit, or UWR/profile scoring once governed.
- Their exact mappings remain future work requiring version pins, KATs, and correct repo placement.
- This decision does not implement those mappings.

### Decision 6 — AIM activation status

**Recorded:** AFI Index / AIM are **published economic doctrine**, but **AIM is inactive for v1 launch**.

Set: **`AIM_t = 1` for v1 launch**, unless and until a later governance decision activates adaptive issuance.

Clarifications:

- This preserves the whitepaper doctrine without prematurely activating feedback-coupled issuance.
- Future AIM activation requires AFI Index definitions, bounds, smoothing, KATs, replay rules, safety analysis, and governance activation.

### Decision 7 — AAG activation status

**Recorded:** AAG is **published economic doctrine**, but **adaptive AAG merit routing is inactive for v1 launch**.

Clarifications:

- v1 uses governed baseline role weights first.
- Adaptive AAG routing requires later governance, role caps, merit definitions, smoothing/SES interaction, KATs, and replay rules.
- This decision does not invent numeric role weights. Baseline role weights are **not yet governed** and are a **required follow-up decision** (see Decision 3 and §7).

### Decision 8 — Future afi-mint cleanup assumptions

**Recorded:** After this decision is merged, a future scoped `afi-mint` PR may align to the following assumptions:

- `afi-math` is the source for pinned `B(t)` schedule behavior.
- 86B is the hard cap.
- Mint settlement is epoch-budget-based.
- Q/N/R-style factors feed credits/merit, not independent mint authority.
- AIM and adaptive AAG are inactive for v1 unless separately governed.

Clarification: this decision does not itself modify `afi-mint`, authorize contract changes, or change mint behavior.

## 5. Rationale

- **One pinned schedule, one cap.** `afi-math` PR-1 hardened the three-phase 86B schedule with deterministic tests/goldens without changing behavior, making it the natural pin for the v1 production `B(t)`. Pinning a finite schedule also resolves the B∞ cumulative-emissions question for v1 without amending whitepaper doctrine.
- **Whitepaper alignment over docstring drift.** The epoch-budget → role-pool → pro-rata-credits skeleton follows whitepaper §9.4/§9.5/§9.7 directly. The proportional epoch-budget structure already present in `afi-mint` is closer to this doctrine than a direct per-signal clamp formula; recording the skeleton lets future cleanup align implementation drafts to doctrine rather than to inherited docstrings.
- **Factors feed merit, not the mint.** Keeping Q/N/R-style factors inside credit/merit/scoring surfaces preserves their value while guaranteeing all issuance stays inside the capped epoch pool.
- **Doctrine preserved, activation staged.** Setting `AIM_t = 1` and deferring adaptive AAG routing keeps AFI Index / AIM / AAG / SES as published doctrine with a clear, governed activation path, avoiding feedback-coupled issuance before definitions, bounds, KATs, and replay rules exist.

## 6. Explicit Non-Authorization

This decision does **not** authorize:

- code changes
- schema changes
- contract changes
- emissions schedule changes
- token cap changes
- UWR implementation
- AFI Index / AIM implementation
- AAG implementation
- SES implementation
- baseline role-weight numeric selection (none is already governed)
- `afi-mint` changes
- `afi-token` changes
- `afi-math` changes
- package publishing
- release tagging
- district work
- repo moves

Each follow-up item in §7 requires its own scoped authorization and review before execution.

## 7. Follow-Up PRs / Open Items

Recorded as **proposed follow-up work, not authorized execution**:

| Item | Scope |
|---|---|
| **PR-3** | `afi-mint` de-inline emissions schedule and consume `afi-math`, preserving behavior |
| **PR-4** | `afi-mint` decimal/integer/float-to-wei cleanup after formula alignment |
| **PR-5** | `afi-token` cap/constant traceability and tests |
| **Future decision** | Numeric baseline role weights (not yet governed; required before live mint activation) |
| **Future decision/promotion** | AFI Index / AIM activation |
| **Future decision/promotion** | AAG adaptive routing activation |
| **Future decision/promotion** | SES interaction and circuit breakers |
| **Future decision/promotion** | Q/N/R-style credit/merit mappings |
| **Future decision/promotion** | UWR profile/mapping system |

## 8. Impact on Repo Authority Model

This decision operates inside the boundaries of `decisions/math-authority-v0.1.md` and updates its open items as follows:

- **Open Decision 1 (mint formula / payout model alignment): resolved for v1** — option (a), the paper model (epoch budget → role routing → pro-rata verified credits), with governed baseline role weights standing in for adaptive AAG routing until separately governed.
- **Open Decision 7 (B(t) / 86B cap reconciliation): resolved for v1** — the `afi-math` three-phase 86B schedule is the pinned production instance of `B(t)`, and 86B is the hard cap traced through governance, `afi-math` goldens, and `afi-token` enforcement.
- **Open Decision 2 (AFI Index / AIM / AAG / SES promotion path): narrowed** — activation status for v1 is now recorded (AIM inactive with `AIM_t = 1`; adaptive AAG routing inactive); the promotion path for repo-local implementation drafts and research/reference surfaces remains future work.
- Authority boundaries are unchanged: `afi-math` remains the canonical executable off-chain math kernel; `afi-mint` executes policy without duplicating canonical formulas; `afi-token` enforces the on-chain boundary with traceable mirrored constants; `afi-econ` remains research/reference; repo-local artifacts remain **not yet promoted** until governed, version-pinned, and KAT-tested.
