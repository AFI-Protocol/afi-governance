# AFI Mathematical Authority Model v0.1

**Status:** Accepted for cleanup planning. **Does not authorize code changes by itself.**
**Date:** 2026-07-04
**Basis:** Cross-repo mathematical authority audit (2026-07-04), which directly inspected `afi-econ`, `afi-math`, `afi-core`, `afi-mint`, `afi-token`, `afi-reactor`, and `afi-governance`. Audit recommendation: **Option A — keep `afi-math` as the canonical executable off-chain math kernel package, with sequenced cleanup.** The real problems are not `afi-math`'s existence, but authority drift in `afi-mint`, `afi-token`, `afi-core`, and stale metadata.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` and existing settlement/district doctrine in `afi-docs`. Where this decision conflicts with the Charter, the Charter wins.

---

## 1. Purpose

AFI has multiple repositories containing math-like logic, constants, schedules, formulas, reward logic, caps, and placeholders. Today these include (non-exhaustively): the emissions schedule and decay/curve/time-value kernels in `afi-math`; UWR/novelty scoring and decay wrappers in `afi-core`; an inlined emissions schedule copy, mint allocation formula, and eligibility thresholds in `afi-mint`; the on-chain supply cap and legacy emissions pseudocode in `afi-token`; placeholder economic models, gauge splits, and simulation formulas in `afi-econ`; indicator/strategy math in `afi-reactor`; and a staking threshold constant plus stub scoring logic in `afi-governance`.

This decision records **which repo owns which class of mathematical authority**, so future cleanup PRs do not create second sources of truth. It is a boundary record, not an implementation instrument.

## 2. Authority Model

### afi-econ
- Owns economic research, incentive theory, simulations, exploratory models, and doctrine proposals.
- **Non-canonical unless a formula is formally promoted.**
- Research or placeholder models must not be used as production, contract, mint, or settlement authority.
- If a formula is promoted, it moves through governance into an executable `afi-math` kernel and/or `afi-config` parameterization, as appropriate.

### afi-math
- Owns **canonical executable off-chain math kernels**.
- Sole source of truth for promoted deterministic formulas such as emissions schedules, decay kernels, reward/math kernels, and other executable formulas accepted as protocol math.
- Should remain low-dependency (currently zero-dependency) and independently auditable.
- Other repos must **import, wrap, derive from, or test against** `afi-math` rather than independently redefining its kernels.

### afi-core
- Owns protocol SDK surfaces, validators, types, score envelopes, scoring contracts, and integration wrappers.
- May consume or wrap `afi-math`.
- **Must not independently redefine canonical formulas that belong in `afi-math`.**
- Scoring contracts and validation envelopes may live in `afi-core`, but formula authority remains in `afi-math` unless explicitly governed otherwise.

### afi-mint
- Owns mint/reward **execution** behavior, state machine, eligibility, and policy application.
- Must import or derive canonical schedules/kernels from `afi-math` where possible.
- **Must not inline or fork canonical formulas without explicit governance authorization.**
- Any mint formula that affects reward amounts, supply budgets, or content-addressed settlement amounts requires an explicit owner/governance decision and a deterministic number policy.

### afi-token
- Owns on-chain enforcement, role/cap checks, and Solidity-level constraints.
- Because Solidity may need mirrored constants or integer formulas, **every mirrored value must trace to governance and/or canonical `afi-math` test vectors**.
- Should not contain stale second-doctrine formulas as active authority.
- On-chain math must use integer/base-unit math, not floating point.

### afi-reactor
- Owns reference runtime behavior and D2-native artifact generation.
- **Not a math authority.**
- Should consume math through the `afi-core`/`afi-math` lineage where applicable.
- Strategy/indicator math inside the reactor is implementation/profile math unless separately promoted.

### afi-governance
- Owns formal authority decisions, proposal lifecycle, accepted/rejected/open status, and future enforcement records.
- **Placeholder or stub scoring logic in governance must never be treated as deterministic protocol authority.**

### Strategy/pipeline repos
- Own strategy-specific math and analyst-specific formulas.
- Strategy math is **not protocol canon merely because it lives in the AFI org**.
- Strategy math may become AFI-compatible if it emits valid protocol artifacts, but it does not become protocol law.

## 3. Source-of-Truth Rules

1. There is **one** source of truth for canonical executable off-chain math: **`afi-math`**.
2. `afi-core` may wrap or expose `afi-math` but must not independently redefine `afi-math` kernels.
3. `afi-mint` executes policy and state transitions, but must not duplicate canonical schedules/formulas.
4. `afi-token` may mirror constants only with governance/test-vector traceability.
5. `afi-econ` may research and propose formulas, but formulas are not executable canon until promoted.
6. Strategy-specific formulas belong with the strategy/pipeline unless formally promoted.
7. **No formula becomes canonical merely because it appears in a repo, README, comment, pseudocode block, or implementation draft.**

## 4. Known Findings From Audit

Recorded as of the 2026-07-04 cross-repo audit (all verified by direct inspection):

- `afi-mint` currently **inlines the `afi-math` emissions schedule** (`src/adapters/EmissionsMintDataProvider.ts`, including the 86B cap constant, with no `afi-math` dependency) and should be cleaned up.
- `afi-mint` currently **documents one mint formula and implements another** (goldpaper `clamp(B(t)·Q·N·R·E_epoch)` in docstrings vs implemented proportional epoch-budget allocation; documented `baseMultiplier: 8.0` unused); this requires an **owner decision before behavioral cleanup**.
- `afi-mint` contains a **float-to-wei quantization hazard** (`BigInt(Math.floor(amount × 10^18))`) that must be removed before any settled/content-addressed mint amounts depend on it.
- `afi-token` contracts are minimal and integer-based (86B cap in wei, role gating; no schedule on-chain), but **lack traceability to `afi-math`/governance test vectors** — the repo contains zero references to `afi-math`.
- `afi-token` contains **stale AFII/AAG / second-doctrine pseudocode** (dynamic throttle, halving + floor, era transitions, novelty-bonus reward) that should be quarantined or clearly marked non-authoritative.
- `afi-core` has at least one **local half-life decay implementation** (`GreeksDecayTemplate.applyTimeDecay`) that should delegate to `afi-math` if feasible.
- `afi-reactor`'s declared `afi-math` dependency metadata (`.afi-codex.json dependsOn`) is **stale**; the reactor currently reaches decay through `afi-core` (`afi-core/decay`), with no direct `afi-math` dependency or import.
- `afi-econ` is **research/non-canonical unless formulas are promoted** (self-declared placeholder status; expects to consume `afi-math`).
- `afi-governance` contains **placeholder/stub scoring logic** (`validator/proposal_scorer.ts` returns `Math.random()`) that must not be wired as deterministic authority.

## 5. Open Decisions

The following remain **unresolved** and are not decided by this document:

1. **Goldpaper clamp formula vs proportional epoch-budget allocation** in `afi-mint` — which is the intended protocol mint formula.
2. Whether the **AFII/AAG throttle, novelty bonus, era transition, or other second-doctrine pseudocode** should be archived, deleted, or reintroduced through a new governed proposal.
3. Where exactly **D-7 decimal/integer quantization helpers** should live (inside `afi-math` as pure kernels vs at the consumer seam).
4. How **`afi-token` mirrored constants** should be governed and test-vectored (decision format, vector location, CI enforcement).
5. How the **1B staking threshold** (`MIN_SUPPLY_FOR_STAKING`) in `afi-governance` should be authorized and tested if staking activates.
6. Whether `afi-reactor` should eventually have a **direct `afi-math` dependency** or continue consuming math transitively through `afi-core` wrappers.

## 6. Explicit Non-Authorization

This decision does **not** authorize:

- moving code
- merging repos
- archiving `afi-math`
- changing mint behavior
- changing token contracts
- publishing packages
- tagging releases
- starting any new district implementation
- promoting `afi-econ` formulas into canon
- wiring governance placeholder scorers
- changing emissions, rewards, settlement, vault, claim, tokenomics, or economic behavior

Each follow-up item in §7 requires its own scoped authorization and review before execution.

## 7. Follow-Up Cleanup Sequence

Recorded as **proposed follow-up work, not authorized execution**:

| PR | Scope |
|---|---|
| **PR-1** | `afi-math` tests/golden vectors (emissions module) + metadata/version/codex/stale-consumer cleanup |
| **PR-2** | Owner decision on the `afi-mint` formula mismatch (documented goldpaper vs implemented proportional allocation) |
| **PR-3** | `afi-mint` de-inline of the canonical emissions schedule — import from `afi-math` |
| **PR-4** | `afi-mint` float-to-wei cleanup, after the formula decision (PR-2) and aligned with the deterministic number policy |
| **PR-5** | `afi-token` traceability/test-vector cleanup (cap and any mirrored values asserted against `afi-math`/governance vectors) |
| **PR-6** | Stale `afi-token` doctrine quarantine (AFII/AAG and related pseudocode) |
| **PR-7** | `afi-core` decay delegation to `afi-math` (preserve wrapper semantics; prove numerical equivalence) |
| **PR-8** | `afi-reactor` stale codex dependency cleanup |
| **PR-9** | `afi-econ` README/status clarification (visibility/placeholder wording) |
| **PR-10** | `afi-governance` placeholder scorer/stub hygiene |

## 8. Future District Boundary

This authority model does not replace the remaining district roadmap. It is a **cross-district guardrail**. It should be resolved before any future milestone that content-addresses, settles, mints, claims, or tokenizes reward amounts, but it does not by itself start or define a new district.
