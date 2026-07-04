# AFI Mathematical Authority Model v0.1

**Status:** Accepted for cleanup planning. **Does not authorize code changes by itself.**
**Date:** 2026-07-04
**Basis:** Cross-repo mathematical authority audit (2026-07-04), which directly inspected `afi-econ`, `afi-math`, `afi-core`, `afi-mint`, `afi-token`, `afi-reactor`, and `afi-governance`. Audit recommendation: **Option A — keep `afi-math` as the canonical executable off-chain math kernel package, with sequenced cleanup.** The real problems are not `afi-math`'s existence, but authority drift in `afi-mint`, `afi-token`, `afi-core`, and stale metadata.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` and existing settlement/district doctrine in `afi-docs`. Where this decision conflicts with the Charter, the Charter wins.

---

## 1. Purpose

AFI has multiple repositories containing math-like logic, constants, schedules, formulas, reward logic, caps, and placeholders. Today these include (non-exhaustively): the emissions schedule and decay/curve/time-value kernels in `afi-math`; UWR/novelty scoring and decay wrappers in `afi-core`; an inlined emissions schedule copy, mint allocation formula, and eligibility thresholds in `afi-mint`; the on-chain supply cap and unpromoted emissions pseudocode sketches in `afi-token`; placeholder economic models, gauge splits, and simulation formulas in `afi-econ`; indicator/strategy math in `afi-reactor`; and a staking threshold constant plus stub scoring logic in `afi-governance`.

This decision records **which repo owns which class of mathematical authority**, so future cleanup PRs do not create second sources of truth. It is a boundary record, not an implementation instrument.

## 2. Whitepaper Doctrine Source

The AFI whitepaper — *"AFI: An Agentic Financial Intelligence Market"* — defines the broad protocol doctrine for the Universal Weighting Rule (UWR) and the economic engine. This authority model traces to that doctrine:

- **§7.3 — Universal Weighting Rule.** Defines the UWR as: `conf = clamp(base × product(guards) − sum(penalties) + sum(lifts), 0, 1)`
- **§9.4 — Epoch emissions.** Defines epoch emissions as `E_t = B(t) AIM_t`, and defines the AFI Index / impact-index logic.
- **§9.5 — AAG.** Defines AAG as the role-pool allocation gauge.
- **§9.6 — SES.** Defines SES as smoothing/rate-limiting/circuit-breaker logic.
- **§9.7 — Payouts.** Defines payouts as pro-rata distribution by verified credits inside role pools, with maturity hold.
- **§9.9 — Failure-mode mitigations.** Defines mitigations such as HHI breakers and correlation penalties.

Whitepaper doctrine is **not automatically executable canon**: a whitepaper formula becomes executable authority only once it is governed, version-pinned, KAT-tested (known-answer tests), and mapped into the correct repo surfaces under the authority model below.

### Disposition of repo-local AFII / AIM / AAG / SES material

AFI Index / AIM / AAG / SES are **published economic doctrine**. The open decision is how to reconcile, promote, quarantine, or rewrite repo-local sketches so they trace to the whitepaper model and pass governance, version-pin, and KAT requirements.

- `afi-econ` appears to contain research/reference implementations of whitepaper §9 concepts.
- `afi-token` may contain older or rough pseudocode sketches of related doctrine.
- These sketches are **unpromoted/unpinned implementation sketches of published whitepaper doctrine** — they are not executable authority merely because they live in a repo.
- Conflicting or obsolete sketches should be quarantined **only** where they conflict with the whitepaper or lack governance activation.
- Reintroduction or promotion requires governed versioning and test vectors.
- The cleanup target is **repo drift from doctrine, not the doctrine itself**.

## 3. Authority Model

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
- Must not treat unpromoted doctrine sketches as active authority.
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

### UWR scoring grammar (cross-repo)
- The UWR is a **canonical scoring grammar/template**, not one analyst's fixed scoring rubric.
- Analysts may deploy different **version-pinned UWR profiles**.
- Profile freedom lives in Codex-pinned mappings into `base`, `guards`, `penalties`, `lifts`, decay, precision, and bounds.
- Analysts must not silently mutate the UWR formula or use private learned weights.
- The protocol standardizes the engine, profile structure, version pins, KATs, and replayability.
- Strategies/pipelines can choose profiles, but profiles only become protocol-recognized if registered and pinned.

### Signal decay and sensitivity templates
- AFI's intended scoring model includes time/context decay and signal sensitivity dimensions, derived from a Greeks-like intuition: signal value changes with time, market movement, volatility, source quality, freshness, novelty, durability, and regime context.
- Pure decay/sensitivity kernels live in `afi-math` when promoted.
- SDK/profile wrappers live in `afi-core`.
- Profile mappings and KATs live in `afi-config`/Codex.
- Strategy-specific applications live with the strategy/pipeline.

## 4. Source-of-Truth Rules

1. There is **one** source of truth for canonical executable off-chain math: **`afi-math`**.
2. `afi-core` may wrap or expose `afi-math` but must not independently redefine `afi-math` kernels.
3. `afi-mint` executes policy and state transitions, but must not duplicate canonical schedules/formulas.
4. `afi-token` may mirror constants only with governance/test-vector traceability.
5. `afi-econ` may research and propose formulas, but formulas are not executable canon until promoted.
6. Strategy-specific formulas belong with the strategy/pipeline unless formally promoted.
7. **No formula becomes canonical merely because it appears in a repo, README, comment, pseudocode block, or implementation draft.**

## 5. Known Findings From Audit

Recorded as of the 2026-07-04 cross-repo audit (all verified by direct inspection):

- `afi-mint` currently **inlines the `afi-math` emissions schedule** (`src/adapters/EmissionsMintDataProvider.ts`, including the 86B cap constant, with no `afi-math` dependency) and should be cleaned up.
- `afi-mint` currently **documents one mint formula and implements another** (goldpaper `clamp(B(t)·Q·N·R·E_epoch)` in docstrings vs implemented proportional epoch-budget allocation; documented `baseMultiplier: 8.0` unused); this requires an **owner decision before behavioral cleanup**.
- `afi-mint` contains a **float-to-wei quantization hazard** (`BigInt(Math.floor(amount × 10^18))`) that must be removed before any settled/content-addressed mint amounts depend on it.
- `afi-token` contracts are minimal and integer-based (86B cap in wei, role gating; no schedule on-chain), but **lack traceability to `afi-math`/governance test vectors** — the repo contains zero references to `afi-math`.
- `afi-token` contains **unpromoted/unpinned implementation sketches of published AFII/AAG doctrine** (dynamic throttle, halving + floor, era transitions, novelty-bonus reward). These sketches are not executable authority; they should be reconciled to the whitepaper model, quarantined only where they conflict with it or lack governance activation, and clearly marked non-authoritative until promoted.
- `afi-core` has at least one **local half-life decay implementation** (`GreeksDecayTemplate.applyTimeDecay`) that should delegate to `afi-math` if feasible.
- `afi-reactor`'s declared `afi-math` dependency metadata (`.afi-codex.json dependsOn`) is **stale**; the reactor currently reaches decay through `afi-core` (`afi-core/decay`), with no direct `afi-math` dependency or import.
- `afi-econ` is **research/non-canonical unless formulas are promoted** (self-declared placeholder status; appears to contain research/reference implementations of whitepaper §9 concepts; expects to consume `afi-math`).
- `afi-governance` contains **placeholder/stub scoring logic** (`validator/proposal_scorer.ts` returns `Math.random()`) that must not be wired as deterministic authority.

## 6. Open Decisions

The following remain **unresolved** and are not decided by this document:

1. **Mint formula / payout model alignment.** The whitepaper separates emissions **sizing** from **allocation/routing**: epoch emissions size is determined by `B(t)` and optional AIM (§9.4); AAG routes the epoch pool across roles (§9.5); and individual payouts are proportional to verified credits inside each role pool (§9.7). The apparent `afi-mint` proportional allocation implementation may align more closely with the whitepaper than the existing docstring. The owner decision should confirm whether `afi-mint` aligns to: (a) the paper model — epoch budget → AAG role routing → pro-rata verified-credit payouts; (b) a direct clamp formula; or (c) a versioned hybrid where quality/novelty/reputation factors feed credits or merit, not independent mint authority.
2. **AFI Index / AIM / AAG / SES promotion path.** These are published doctrine, but repo-local implementations/sketches (in `afi-econ`, `afi-token`, and elsewhere) are unpromoted until governed, version-pinned, and KAT-tested. The decision is how to reconcile, promote, quarantine, or rewrite each sketch so it traces to the whitepaper model.
3. **Quantization helpers.** Whether pure D-7 decimal/integer quantization helpers live in `afi-math` as pure kernels, with mint-specific application at the `afi-mint` seam.
4. **Token constant governance.** How the 86B cap and other `afi-token` mirrored constants trace to governance and test vectors (decision format, vector location, CI enforcement).
5. **Staking threshold.** Status and authorization of the **1B staking threshold** (`MIN_SUPPLY_FOR_STAKING`) in `afi-governance` if staking activates, including how it is tested.
6. **Reactor math lineage.** Whether `afi-reactor` stays transitive through `afi-core` wrappers or eventually takes a **direct `afi-math` dependency**.
7. **B(t) / 86B cap reconciliation.** The whitepaper describes `B(t)`, including a geometric-with-floor baseline example, but does not explicitly mention 86B or the three-phase schedule. Current repos treat the three-phase 86B schedule and the 86B token cap as canonical or near-canonical. A nonzero B∞ floor can imply unbounded cumulative emissions unless constrained by a cap, truncation, or B∞ = 0. Governance must decide whether the `afi-math` three-phase 86B schedule is the pinned production instance of `B(t)`, and how it traces to the hard token cap.
8. **UWR shape/versioning.** The whitepaper defines the general UWR engine as guard/penalty/lift aggregation (§7.3). `afi-core` currently implements a four-axis weighted-average scorer, which is mathematically expressible as a pure-lifts profile under the whitepaper UWR (`base = 0`, `guards = []`, `penalties = []`, `lifts =` weighted axis contributions). There should therefore not be two rival UWR doctrines: the whitepaper UWR is the intended canonical model, and the current weighted scorer is classified as a **UWR v0.1 weighted-lifts profile** (reference profile). A later governed promotion PR should implement the general UWR combiner, Codex-pinned profile mappings, KATs, and version pins without breaking existing D2 M2 goldens.

## 7. Explicit Non-Authorization

This decision does **not** authorize:

- UWR implementation changes
- code changes
- schema changes
- moving code / repo moves
- merging repos
- archiving `afi-math`
- changing mint behavior
- changing token contracts
- changing the emissions schedule
- implementing AAG / AIM / SES
- publishing packages
- tagging releases
- starting any new district implementation or other district work
- promoting `afi-econ` formulas or code into canon
- wiring governance placeholder scorers
- changing emissions, rewards, settlement, vault, claim, tokenomics, or economic behavior

Each follow-up item in §8 requires its own scoped authorization and review before execution.

## 8. Follow-Up Cleanup Sequence

Recorded as **proposed follow-up work, not authorized execution**:

| PR | Scope |
|---|---|
| **PR-1** | `afi-math` tests/golden vectors (emissions module) + metadata/version/codex/stale-consumer cleanup |
| **PR-2** | Owner decision on `afi-mint` formula/payout alignment (paper model epoch budget → AAG → pro-rata credits vs direct clamp formula vs governed hybrid) |
| **PR-3** | `afi-mint` de-inline of the canonical emissions schedule — import from `afi-math` |
| **PR-4** | `afi-mint` float-to-wei cleanup, after the formula decision (PR-2) and aligned with the deterministic number policy |
| **PR-5** | `afi-token` traceability/test-vector cleanup (cap and any mirrored values asserted against `afi-math`/governance vectors) |
| **PR-6** | Reconciliation of unpromoted `afi-token` doctrine sketches (AFII/AAG and related pseudocode) to the whitepaper model; quarantine only where conflicting or ungoverned |
| **PR-7** | `afi-core` decay delegation to `afi-math` (preserve wrapper semantics; prove numerical equivalence) |
| **PR-8** | `afi-reactor` stale codex dependency cleanup |
| **PR-9** | `afi-econ` README/status clarification (visibility/placeholder wording) |
| **PR-10** | `afi-governance` placeholder scorer/stub hygiene |

## 9. Future District Boundary

This authority model does not replace the remaining district roadmap. It is a **cross-district guardrail**. It should be resolved before any future milestone that content-addresses, settles, mints, claims, or tokenizes reward amounts, but it does not by itself start or define a new district.
