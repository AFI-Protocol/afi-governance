# AFI Version-Pinned UWR Profile v0.1 (Testnet-Provisional Pin)

**Status:** Accepted owner decision for the AFI testnet-provisional interpretation. **Does not authorize implementation changes by itself.** This is **not** final production scoring law: every value pinned below is **testnet-provisional** unless separately re-governed.
**Date:** 2026-07-11
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md`, `decisions/math-authority-v0.1.md`, `decisions/mint-formula-bt-86b-alignment-v0.1.md`, and existing settlement/district doctrine in `afi-docs`. Where this decision conflicts with the Charter, the Charter wins.
**Ledger slot:** Fills the reserved item "**Future decision/promotion | UWR profile/mapping system**" (`decisions/mint-formula-bt-86b-alignment-v0.1.md` §7) and narrows `decisions/math-authority-v0.1.md` Open Decision 8.

---

## 1. Purpose

`decisions/math-authority-v0.1.md` §3 ("UWR scoring grammar (cross-repo)") establishes that:

- "The UWR is a **canonical scoring grammar/template**, not one analyst's fixed scoring rubric."
- "Analysts may deploy different **version-pinned UWR profiles**."
- "The protocol standardizes the engine, profile structure, version pins, KATs, and replayability."
- "profiles only become protocol-recognized if registered and pinned."

No registered profile exists today. The live scorer runs the placeholder configuration `defaultUwrConfig` (`id: "uwr-default-stub"`, `afi-core/validators/UniversalWeightingRule.ts`), which carries an in-code TODO to source governance-approved weights from `afi-config`. Persisted scored records pin no scorer or configuration version, and `afi-docs/specs/AFI_REPLAY_READINESS_MATRIX.md` records that no lifecycle stage is deterministically replayable today, citing the unpinned `uwr-default-stub` placeholder among the causes.

This decision registers the **first version-pinned UWR profile** so that testnet signal scoring runs against a named, pinned, KAT-gated profile instead of an anonymous stub — without changing a single scored value.

This is a governance/docs decision only. It does not change runtime behavior anywhere.

## 2. Sources

1. **Existing governance decisions:** `decisions/math-authority-v0.1.md` (merged via afi-governance PR #6, merge commit `d421447`) — §3 UWR scoring grammar; Open Decision 8 (the current scorer is classified as a "**UWR v0.1 weighted-lifts profile** (reference profile)"); §8 Follow-Up Cleanup Sequence item **PR-7** ("`afi-core` decay delegation to `afi-math` (preserve wrapper semantics; prove numerical equivalence)"). `decisions/mint-formula-bt-86b-alignment-v0.1.md` (merged via afi-governance PR #7, merge commit `0cd8f46`) — Decision 5 (Q/N/R-style factors feed credit/merit calculations); §7 reserved slot "UWR profile/mapping system".
2. **afi-core** @ `390b440`:
   - `validators/UniversalWeightingRule.ts` — `computeUwrScore` (normalized weighted average of four clamped axes), `UniversalWeightingRuleConfig`, `defaultUwrConfig` (`id: "uwr-default-stub"`, four weights of `0.25`), axis inputs `structureAxis` / `executionAxis` / `riskAxis` / `insightAxis`, and the `UniversalWeightingRuleConfig` docblock rule "UWR is a protocol-level primitive and MUST NOT be modified by reputation".
   - `src/decay/GreeksDecayTemplate.ts` — "Canonical time-decay template for AFI Protocol signals … inspired by options Greeks (particularly theta - time decay)"; `DEFAULT_DECAY_TEMPLATES_BY_HORIZON` with template ids `decay-scalp-v1` / `decay-intraday-v1` / `decay-swing-v1` / `decay-position-v1`; `applyTimeDecay` (`decayed = baseScore * 0.5 ^ (elapsedMinutes / halfLifeMinutes)`); `DecayParams { halfLifeMinutes, greeksTemplateId }`.
   - `validators/SignalDecay.ts` — the parallel afi-math-backed decay wrapper (`applyTimeDecayToUwrScore`, hours, `e^(-λ·age)`). The `math-authority-v0.1.md` §5 audit finding flags its counterpart, `GreeksDecayTemplate.applyTimeDecay`, as a "local half-life decay implementation … that should delegate to `afi-math` if feasible"; that delegation is the reserved PR-7 scope.
   - `analysts/froggy.trend_pullback_v1.ts` — the reference analyst (`analystId "froggy"`, `strategyId "trend_pullback_v1"`).
3. **afi-reactor** @ `79c4a6f` (District 2 M2): `test/pipeheads/fixtures/golden.json` — the D2 M2 golden replay anchor (`uwrScore 0.1875`; `uwrAxes` `structure 0.15 / execution 0 / risk 0.2 / insight 0.4`; `conviction 0.1875`; `riskBucket "medium"`), with its own in-file statement that District 2 M2 "changed the artifact surface, NEVER the scoring math"; `src/types/ReactorScoredSignalV1.ts` — `decayParams { halfLifeMinutes, greeksTemplateId }` ("Greeks-style time decay").
4. **afi-config** @ `ad97cc5`:
   - `schemas/provenance/v1/scored-signal.schema.json` — open items **SS-O1** (riskBucket taxonomy) and **SS-O2** (uwrScore range/normalization policy), each "scoring-doctrine-owned and deliberately OPEN", and **SS-O3** (uwrAxes axis-name registry — "OPEN; free-form axis→number map in this draft").
   - `schemas/validatorConfig.schema.json` — `minDecayScoreThreshold` (default `0.5`, "Minimum decay score to pass threshold") and `challengeWindowDurationHours` (default `24`, "Duration of challenge window in hours (max 7 days)"); mirrored (with naming drift) in `afi-mint/src/orchestrator/types.ts` `DEFAULT_VALIDATOR_CONFIG`.
   - `docs/REGISTRIES_AND_REPUTATION.v0.1.md` — "Reputation cannot alter the Unified Weighting Rule (UWR) or scoring logic for individual signals" (see UP-1 terminology note).
5. **afi-math** @ `f20c0dd`: `src/decay/decayModels.ts` — the canonical decay kernels (`exponentialDecay`, `adjustedHalfLife`, `greeksAdjustedHalfLife`, …) relevant to the PR-7 delegation question. This decision does not modify or re-pin them.

## 3. Decision Summary

| # | Decision | Testnet-provisional outcome |
|---|---|---|
| UP-1 | Canonical artifact term | "**version-pinned UWR profile**" is the canonical term; "Testnet Scoring Profile v0" is recorded as an **optional human-facing alias only**, never a repo identifier |
| UP-2 | Profile id + registration | Profile id **`uwr-weighted-lifts-v0.1`**, to be registered in `afi-config`; supersedes the placeholder id `uwr-default-stub` as the referenced configuration (code switch **not** authorized here) |
| UP-3 | Engine pin | `computeUwrScore` normalized weighted average — the "UWR v0.1 weighted-lifts profile" per Open Decision 8; the whitepaper §7.3 combiner (`base` / `guards` / `penalties` / `lifts`) remains **deferred** |
| UP-4 | Axes pin | `structure`, `execution`, `risk`, `insight` — provisionally closes SS-O3 **for this profile only** |
| UP-5 | Weights pin | `0.25 / 0.25 / 0.25 / 0.25` — preserves the D2 M2 goldens byte-for-byte (`uwrScore 0.1875` anchor) |
| UP-6 | Output surface | `uwrScore` normalized to `[0, 1]` (SS-O2 provisional, this profile only); `riskBucket` taxonomy `low \| medium \| high \| extreme` (SS-O1 provisional, this profile only); `conviction` in `[0, 1]` |
| UP-7 | Decay template set | GreeksDecayTemplate v1: `decay-scalp-v1` (8) / `decay-intraday-v1` (60) / `decay-swing-v1` (720) / `decay-position-v1` (5040) `halfLifeMinutes`; `decayModel "exp"`; unit **minutes**; `thetaBias` recorded as declared-but-not-consumed; `linear` / `cliff` models **not pinned** (documented only) |
| UP-8 | Decay-engine canonicality | **OPEN — deferred to the existing PR-7 slot** (`math-authority-v0.1.md` §8); this profile pins the GreeksDecayTemplate **surface** without resolving canonicality |
| UP-9 | Qualification values | `minDecayScoreThreshold = 0.5` and `challengeWindowDurationHours = 24` recorded as **testnet-provisional**; the qualification rule remains `decayedScore >= minDecayScoreThreshold`; the canonical term is "challenge window" |
| UP-10 | Scorer identity | Profile v0.1 is recognized only for `analystId "froggy"` / `strategyId "trend_pullback_v1"` (plus `strategyVersion` where present) |
| UP-11 | KAT/golden gate | The profile may not back any reward-qualified or mint-eligible flow until KAT vectors exist (`computeUwrScore` + `applyTimeDecay`) and the D2 M2 goldens remain byte-stable |
| UP-12 | Authorization scope | Authorizes **only** the single scoped `afi-config` schema + registry-instance + tests PR (§7, PR-UWR-CONFIG); all runtime consumption is separately authorized |

## 4. Detailed Decisions

### Decision UP-1 — Canonical artifact term

**Recorded:** The canonical artifact term is "**version-pinned UWR profile**", exactly as established in `math-authority-v0.1.md` §3. "**Testnet Scoring Profile v0**" is an optional, human-facing alias only. It must never appear as a repo identifier, schema `$id`, field name, or profile id.

Clarifications:

- UWR expands as "**Universal Weighting Rule**" (`afi-core/validators/UniversalWeightingRule.ts`, `math-authority-v0.1.md` §2 "Whitepaper Doctrine Source"). The variant expansion "Unified Weighting Rule" in `afi-config/docs/REGISTRIES_AND_REPUTATION.v0.1.md` is recorded as a known terminology inconsistency; correcting it is cleanup work, not authorized here.
- Decision identifiers in this document use the **UP-n** prefix to avoid further overloading "D-n"-style identifiers, which already carry three distinct meanings in the org (District 2 decisions D-1…D-17 in `afi-docs`; the Settlement v1 session's locked decisions D1–D10; this repo's mint-formula decisions D1–D8).

### Decision UP-2 — Profile id and registration

**Recorded:** The first version-pinned UWR profile has id **`uwr-weighted-lifts-v0.1`** and is to be **registered in `afi-config`**, consistent with `math-authority-v0.1.md` §3 ("Profile mappings and KATs live in `afi-config`/Codex") and §3's registration rule ("profiles only become protocol-recognized if registered and pinned").

Clarifications:

- The id encodes Open Decision 8's own classification of the current scorer ("UWR v0.1 weighted-lifts profile") and follows the existing kebab-case id convention (`uwr-default-stub`) with the versioned-suffix pattern of the decay template ids (`decay-scalp-v1`).
- Once a separately-authorized runtime PR consumes the registered profile, `uwr-default-stub` is superseded as the referenced configuration. Until then, `defaultUwrConfig` remains in place unchanged; **this decision does not modify `afi-core`**.
- The profile registration is value-identical to `defaultUwrConfig` by construction (UP-5), so registration introduces no behavioral change anywhere.

### Decision UP-3 — Engine pin

**Recorded:** The engine for profile `uwr-weighted-lifts-v0.1` is `computeUwrScore` (`afi-core/validators/UniversalWeightingRule.ts`): a normalized weighted average of four clamped axes, returning a score in `[0, 1]`.

Clarifications:

- Per Open Decision 8, this engine "is mathematically expressible as a pure-lifts profile under the whitepaper UWR (`base = 0`, `guards = []`, `penalties = []`, `lifts =` weighted axis contributions)". There are not two rival UWR doctrines: the whitepaper UWR remains the intended canonical model.
- The general whitepaper §7.3 combiner (`conf = clamp(base × product(guards) − sum(penalties) + sum(lifts), 0, 1)`) remains **not implemented and deferred** ("Intentionally Not Implemented (Yet)", `afi-math/README.md`). Nothing in this decision advances or authorizes it.
- The engine remains a protocol-level primitive that "MUST NOT be modified by reputation" and must not be silently mutated by analysts ("Analysts must not silently mutate the UWR formula or use private learned weights", `math-authority-v0.1.md` §3).

### Decision UP-4 — Axes pin

**Recorded:** The axis registry for this profile is exactly `structure`, `execution`, `risk`, `insight` (order significant), matching `AnalystScoreTemplate.uwrAxes` and `UwrAxesInput` in `afi-core`.

Clarifications:

- This **provisionally closes SS-O3 for this profile only**. The org-wide open item in `afi-config/schemas/provenance/v1/scored-signal.schema.json` remains OPEN until that schema leaves `draft-non-implementation` status under District 2 authority.
- The divergent `uwrAxes` shape carried in `afi-gateway/src/afiClient.ts` (`utility`, `workQuality`, `rarity`) is recorded as **non-conformant** with this profile. Correcting it is cleanup work, not authorized here.

### Decision UP-5 — Weights pin

**Recorded:** The weights for profile `uwr-weighted-lifts-v0.1` are `structureWeight 0.25`, `executionWeight 0.25`, `riskWeight 0.25`, `insightWeight 0.25`.

Clarifications:

- These are the values already used by `defaultUwrConfig`, so pinning them changes no scored output. The D2 M2 golden anchor must hold: `uwrScore 0.1875 = mean(0.15, 0, 0.2, 0.4)` (`afi-reactor/test/pipeheads/fixtures/golden.json`).
- **Golden compatibility is an acceptance criterion:** the D2 M2 goldens remain byte-stable under this decision and under the follow-up config PR. Re-pinning or regenerating those goldens is not authorized here.
- Any future weight change is a **new profile version** (a new id), never a mutation of `uwr-weighted-lifts-v0.1`. These weights are testnet-provisional, not production scoring law.

### Decision UP-6 — Output surface pins

**Recorded:** For this profile: `uwrScore` is normalized to `[0, 1]` (SS-O2, provisional, this profile only); the `riskBucket` taxonomy is `low | medium | high | extreme` (SS-O1, provisional, this profile only), matching `AnalystScoreTemplate.riskBucket`; `conviction` is in `[0, 1]`.

Clarifications:

- As with UP-4, these close SS-O1 and SS-O2 **for this profile only**; the District 2 draft-schema open items themselves remain OPEN.
- The D2 example value `riskBucket: "moderate"` (`afi-config/examples/provenance/v1/scored-signal.example.json`) is recorded as inconsistent with the pinned taxonomy; reconciling examples is part of the follow-up config PR's scope, not a change to District 2 schemas.

### Decision UP-7 — Decay template set pin

**Recorded:** The profile's pinned decay surface is **GreeksDecayTemplate v1** (`afi-core/src/decay/GreeksDecayTemplate.ts`): template ids `decay-scalp-v1` (halfLifeMinutes 8), `decay-intraday-v1` (60), `decay-swing-v1` (720), `decay-position-v1` (5040); `decayModel "exp"`; the pinned unit is **minutes** (`halfLifeMinutes`), as carried by `ReactorScoredSignalV1.decayParams { halfLifeMinutes, greeksTemplateId }`.

Clarifications:

- `thetaBias` (0.8 / 0.6 / 0.4 / 0.2 across the four templates) is recorded as **declared but not consumed** by any computation. It is not pinned as behavior; any future activation requires its own decision.
- The `linear` and `cliff` decay models exist only as type/schema surface with no evaluator; they are **not pinned** (documented only).
- The horizon-selection mapping (`pickDecayParamsForAnalystScore`: `long-term` → `position`; unknown/missing → `swing`) is pinned as the profile's selection rule.
- Half-life unit drift exists across layers (`halfLifeMinutes` in afi-core/afi-reactor, `baseHalfLifeHours` in `validatorConfig`/afi-mint, `halfLifeDays` in USS `telemetry.decay`). This profile pins **minutes** at the profile surface; unit reconciliation elsewhere is follow-up work.

### Decision UP-8 — Decay-engine canonicality (OPEN, deferred to PR-7)

**Recorded:** The question of which decay engine is canonical — `GreeksDecayTemplate.applyTimeDecay` (minutes, `0.5^(elapsed/halfLife)`, no afi-math import) versus `validators/SignalDecay.ts` (hours, `e^(−λ·age)`, wrapping `afi-math` `decay`) — remains **OPEN** and is **deferred to the existing PR-7 slot** (`math-authority-v0.1.md` §8: "`afi-core` decay delegation to `afi-math` (preserve wrapper semantics; prove numerical equivalence)").

Clarifications:

- The two forms are mathematically equivalent families (`0.5^(t/H) = e^(−ln2·t/H)`) but differ in units, clamping behavior, and afi-math compliance; proving numerical equivalence is exactly PR-7's recorded scope.
- This profile pins the GreeksDecayTemplate **surface** (template ids, half-lives, model, unit) so testnet artifacts are replayable, without prejudging PR-7's outcome. If PR-7 lands a delegation, the pinned surface values must be preserved or a new profile version issued.

### Decision UP-9 — Qualification values (testnet-provisional)

**Recorded:** `minDecayScoreThreshold = 0.5` and `challengeWindowDurationHours = 24` — the existing defaults in `afi-config/schemas/validatorConfig.schema.json` and `afi-mint` `DEFAULT_VALIDATOR_CONFIG` — are recorded as **testnet-provisional** values for flows that reference this profile. The qualification rule remains `decayedScore >= minDecayScoreThreshold`.

Clarifications:

- The canonical term is "**challenge window**"; the variant "challenge period" (`afi-mint/src/snapshot/ProposalBuilder.ts` generated text) is recorded as an inconsistency, not adopted.
- Recording these values does **not** wire the qualification gate: no `IValidatorScorer` implementation or composition root exists, and wiring remains separately authorized (see §6).
- These values are not production law; production values require their own decision informed by testnet data.

### Decision UP-10 — Scorer identity pin

**Recorded:** Profile `uwr-weighted-lifts-v0.1` is recognized only for the reference scorer pair `analystId "froggy"` / `strategyId "trend_pullback_v1"` (plus `strategyVersion` where present), invoked as `scoreFroggyTrendPullbackFromEnriched` from `afi-core`.

Clarifications:

- Additional analysts/strategies require either registration under this profile (if value-identical) or new profile versions — always registered and pinned, never silent.
- The analyst's internal axis-mapping heuristics remain strategy-local; what this profile pins is the engine, axes, weights, output surface, decay surface, and identity — not the strategy's internal feature logic.

### Decision UP-11 — KAT/golden gate

**Recorded:** Profile `uwr-weighted-lifts-v0.1` may not back any **reward-qualified or mint-eligible flow** — meaning any flow in which `uwrScore`-derived outcomes affect rewards, qualification for rewards, or minting — until:

1. KAT vectors exist for `computeUwrScore` under this profile (including the `0.1875` anchor), stored per PR-UWR-CONFIG;
2. KAT vectors exist for `applyTimeDecay` over the pinned template set;
3. the D2 M2 goldens (`afi-reactor/test/pipeheads/fixtures/golden.json`) remain byte-stable.

Clarifications:

- This implements the standing doctrine that promotion requires artifacts to be "governed, version-pinned, and KAT-tested".
- KAT **vectors** (pure data) live in `afi-config` per `math-authority-v0.1.md` §3; KAT **execution** against afi-core code is a separately-authorized afi-core PR (PR-UWR-KAT-EXEC), following the established vendored-golden-with-source-pin pattern used by `afi-mint` for the emissions goldens.

### Decision UP-12 — Authorization scope

**Recorded:** This decision authorizes **only** the single scoped `afi-config` PR described in §7 as **PR-UWR-CONFIG**: profile schema + registry instance + examples + positive/negative tests + KAT vector files + documentation section, all marked `x-afiStatus: "draft-non-implementation"`.

Clarifications:

- This mirrors the District 2 D-17 pattern of scoping authorization to exactly one implementation phase.
- It does **not** authorize: consuming the registry at runtime, modifying `defaultUwrConfig`, stamping profile ids into persisted records, wiring qualification, or any other item in §6. Each requires its own scoped authorization.
- Merging PR-UWR-CONFIG is the owner-review acceptance act for that phase, consistent with existing practice.

## 5. Rationale

- **A registered profile beats an anonymous stub.** Replacing reliance on `uwr-default-stub` with a registered, version-pinned profile makes scoring identifiable and replay-pinnable without changing a single scored value (0.25×4 preserved → `uwrScore 0.1875` anchor stable).
- **This is Open Decision 8's own instruction, executed minimally.** OD-8 classified the current scorer as the "UWR v0.1 weighted-lifts profile" and asked for registration/pins "without breaking existing D2 M2 goldens". This decision does exactly that and no more; the general combiner remains deferred.
- **Decay surface and decay canonicality are separated.** Pinning template ids, half-lives, model, and unit gives testnet artifacts a replayable decay surface now, while the engine-delegation question stays in its reserved PR-7 slot instead of being resolved under time pressure.
- **Provisional closures are scoped, not global.** SS-O1/O2/O3 are closed *for this profile only*, respecting District 2's ownership of the scored-signal draft schema and avoiding cross-instrument reach.

## 6. Explicit Non-Authorization

This decision does **not** authorize:

- runtime code changes (any repo) — the only code this decision touches is the schema-test and KAT-vector material bundled inside PR-UWR-CONFIG (UP-12)
- scoring code changes, including `afi-core/validators/UniversalWeightingRule.ts` and `defaultUwrConfig`
- schema changes outside the single scoped PR-UWR-CONFIG in §7
- changes to `afi-core`, `afi-reactor`, `afi-mint`, `afi-token`, `afi-math`, or `afi-gateway`
- re-pinning or regenerating D2 M2 goldens
- wiring the qualification gate (`IValidatorScorer` implementations, `ValidatorDaemon` composition)
- minting, reward routing, or the reactor→mint bridge
- numeric baseline role weights (still the required pre-mint follow-up per `mint-formula-bt-86b-alignment-v0.1.md` Decision 3)
- AFI Index / AIM implementation or activation
- adaptive AAG implementation or activation
- SES implementation or activation
- staking activation
- settlement, vault, claims, or anchoring work
- the whitepaper §7.3 UWR combiner
- analyst-supplied weights or private learned weights
- resolving PR-7 (decay delegation)
- district work
- package publishing or release tagging
- production scoring law of any kind

Each follow-up item in §7 requires its own scoped authorization and review before execution.

## 7. Follow-Up PRs / Open Items

Recorded as **proposed follow-up work**; only PR-UWR-CONFIG is authorized (UP-12):

| Item | Scope | Authorized? |
|---|---|---|
| **PR-UWR-CONFIG** | `afi-config`: `uwr-profile` schema + registry instance (`uwr-weighted-lifts-v0.1`) + examples + positive/negative tests + KAT vector files + docs section, all `draft-non-implementation` | **Yes — by UP-12** |
| **PR-UWR-KAT-EXEC** | `afi-core`: execute vendored KAT vectors against `computeUwrScore` / `applyTimeDecay` (vendored-golden-with-source-pin pattern) | No — separate authorization |
| **PR-UWR-STAMP** | `afi-reactor`: stamp the profile id into persisted `ReactorScoredSignalDocument` records (addresses the replay-readiness finding that records pin no scorer/config version) | No — separate authorization |
| **PR-7** (existing) | `afi-core` decay delegation to `afi-math` — unchanged, still open (`math-authority-v0.1.md` §8) | No — pre-existing slot |
| Cleanup | `afi-gateway` divergent `uwrAxes` copy (`utility` / `workQuality` / `rarity` in `src/afiClient.ts`) — non-conformant with UP-4 | No |
| Cleanup | "Unified Weighting Rule" wording in `afi-config/docs/REGISTRIES_AND_REPUTATION.v0.1.md`; "challenge period" wording in `afi-mint` ProposalBuilder output | No |
| Future decision | Production (non-provisional) profile values; additional analyst/strategy registrations; `x-afiStatus` lifecycle beyond `draft-non-implementation` | No |
| Future decision/promotion | Whitepaper §7.3 UWR combiner; role weights; AIM / AAG / SES (unchanged from prior decisions) | No |

## 8. Impact on Repo Authority Model

This decision operates inside the boundaries of `decisions/math-authority-v0.1.md` and `decisions/mint-formula-bt-86b-alignment-v0.1.md`, and updates their open items as follows:

- **Open Decision 8 (UWR shape/versioning): narrowed** — the four-axis weighted-average scorer is now a **registered** version-pinned UWR profile (`uwr-weighted-lifts-v0.1`, testnet-provisional) rather than an unregistered reference implementation running a placeholder config. The general UWR combiner, the full profile/mapping system, KAT execution, runtime consumption, and production values remain future governed promotions.
- **mint-formula §7 "UWR profile/mapping system" slot: partially filled** — the profile-registration half is decided (this document); the mapping-system half (Codex-pinned mappings into `base`, `guards`, `penalties`, `lifts`, decay, precision, and bounds for arbitrary analysts) remains open.
- Authority boundaries are unchanged: the engine implementation stays in `afi-core`; profile registration and KAT vectors live in `afi-config`; `afi-reactor` remains "Not a math authority"; `afi-mint` consumes pinned values without duplicating formulas; nothing here touches `afi-token` or `afi-math`.
