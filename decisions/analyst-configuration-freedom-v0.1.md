# AFI Analyst Configuration Freedom v0.1 (CFG-GOV)

**Slot:** `AFI-GOV-ANALYST-CONFIGURATION-FREEDOM-v0.1` (CFG-GOV)
**Status:** **Proposed** for owner approval — this decision becomes authoritative only when the owner merges it. Owner authorization for its subject matter is recorded by the owner instruction that commissioned this decision (founder instruction of 2026-08-05: *"let's get this governance update or supersession over and done with so we can move forward with our new purpose. I fully approve removing these blockers and setting the new tone."*).
**Date:** 2026-08-05
**Type:** Scoped protocol-development governance decision (**Tier F** under GPR-GOV D-GPR-2 — it amends governed schemas and laws that scoring and evidence surfaces depend on). Records settled owner decisions across six clauses; it is **not** a constitution and decides nothing beyond them.
**Relevance (GPR-GOV D-GPR-4):** *An analyst who is not a programmer can register a second strategy, choose which enrichment categories it uses, set its own UWR weights, and adjust them as market conditions change — while every scored record remains sealed and proves exactly which configuration produced it.* Today none of that is possible: exactly one strategy is registrable, its weights are pinned by a loader predicate, a subset of categories cannot produce a valid record, and no record is ever made immutable.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` and `decisions/authority-districts-v0.1.md`. For the District-framing, non-production, and no-financial-truth invariants it defers to `decisions/current-authority-reroot-and-golden-closure-v0.1.md` (R1-GOV). **Consumes (does not re-decide)** `decisions/factory-configurable-pipelines-v1.md` (FCP-GOV), `decisions/object-identity-v0.1.md` (OBJ-GOV), `decisions/lifecycle-v0.1.md` (LIFE-GOV), `decisions/strategy-version-semantics-v0.1.md` (SV-GOV), `decisions/scored-signal-direction-restoration-v0.1.md` (DIR-GOV), and `decisions/challenge-retirement-v0.1.md` (CHR-GOV). **Amends or supersedes, prospectively and only as stated in D-CFG-2 through D-CFG-6 and nowhere else,** named clauses of `decisions/persistence-v0.1.md` (MONGO-GOV), `decisions/evidence-v3-provider-provenance-v0.1.md` (EV3-GOV), `decisions/uwr-runtime-consumption-v0.1.md` (RC-GOV), `decisions/uwr-profile-pin-v0.1.md` (UP-GOV), and `decisions/governance-process-rightsize-v0.1.md` (GPR-GOV). **Every other accepted decision on `decisions/INDEX.md` — untouched.** Honors, and does not touch, the reserved `ATLAS-GOV` and `CHAIN-GOV` scopes. Where this decision conflicts with the Charter, the Charter wins.
**Evidence basis:** Findings are restated inline because the workspace `reports/` area is unversioned and is never authority. Established by read-only source verification on 2026-08-05 against clean `origin/main` at: afi-reactor @ `70ad00c`, afi-core @ `7faa2fd`, afi-infra @ `71286bb`, afi-config @ `666b247`, afi-governance @ `b33bc2f`.

1. **No record is ever made immutable.** MONGO-GOV D-MONGO-5 (`persistence-v0.1.md:80`) makes a canonical record immutable *"once its signal reaches the LIFE-GOV `FINALIZED` state."* The LIFE-GOV machine (`lifecycle-v0.1.md:47`) reaches `FINALIZED` only via `CERTIFIED → QUALIFIED → CHALLENGE_OPEN`. Qualification is unbuilt, and the challenge layer was retired by CHR-GOV. Consequently **every canonical record ever written carries `finalized: false`** (`afi-reactor/src/evidence/reactorEvidenceRecord.ts:156,689`; enforced at submit, `src/evidence/submitScoredSignalEvidence.ts:103`), nothing calls `supersede()` or finalizes (no callers), and every record therefore sits permanently in the supersedable state (`afi-infra` `MongoScoredSignalEvidenceStore.ts:236-241,269-300`). Records are re-read only as a boot warmup (`evidenceStore.ts:83`) — there is no verify-on-read and no periodic re-hash. **The law is sound; its trigger is unreachable by construction.**
2. **A subset of enrichment categories cannot produce a record.** EV3-GOV D-EV3-5(1) requires all five lanes; a missing category throws *"a scored evaluation requires all five lanes (D-EV3-5(1))"* (`reactorEvidenceRecord.ts:335-350`). Its stated purpose is to retire the **five-lane degrade allowance** so a *failed or degraded* lane cannot yield a record. It does not contemplate a lane an analyst deliberately did not select. Meanwhile the governed config schema already admits `nodeOverrides.enabled: false` on lane nodes, so a config-disabled lane today produces an unpersistable signal.
3. **Registered weights cannot differ from the builtin.** RC-GOV RC-5's identity predicate requires a loaded profile's weights to **equal** `defaultUwrConfig`; the implementing loader states *"registry-supplied numbers never flow into the result"* (`afi-core/validators/UwrProfileLoader.ts:95-112`), re-enforced at boot (`afi-reactor/src/pipeline/registryLoader.ts:21-22`). UP-GOV UP-10 recognizes profile `uwr-weighted-lifts-v0.1` for `analystId "froggy"` / `strategyId "trend_pullback_v1"` only. The runtime resolves UWR config **once per process** (`afi-reactor/src/config/uwrRuntimeProfile.ts:194-200`), so per-strategy weights are architecturally absent, not merely pinned.
4. **The configurable model already exists and is already governed.** FCP-GOV established the canonical five-category namespace, the configurable composition model, and the generic registration rule; `analyst-strategy-config.schema.json` carries `analystId`, `strategyId`, `pipelineRef`, `scorerRef`, `uwrProfileRef`, `decayConfig`, `nodeOverrides`. RC-GOV RC-3 expressly reserves the source-flag default flip to *"a separate future decision"*, and UP-10 expressly contemplates *"new profile versions — always registered and pinned, never silent."* **This decision is the future decision those clauses reserved.**
5. **Provenance is already recorded.** Every canonical record stamps `compositionRef` = {pipelineId, pipelineVersion, `manifestHash`, `analystConfigHash`, scorer identity, `pluginSetHash`, `executionSummaryHash`, `enrichmentHash`} (`afi-reactor/src/pipeline/graphScoringService.ts:277-288`), required fail-closed (`reactorEvidenceRecord.ts:282-286,617`). The analytics plane omits it (`src/analytics/scoringContextStore.ts:106-127`) while remaining joinable by `signalId`.

**Ledger slot:** None existed. FCP-GOV built the configurable composition model; RC-GOV, UP-GOV and EV3-GOV each bounded it to a single instance for reasons that were correct at the time. No decision states what happens when a **second** analyst configuration exists, nor what makes a scored record immutable when the lifecycle stages preceding `FINALIZED` are unbuilt or retired. This decision opens the analyst-configuration slot. It authorizes **zero** code PRs; each implementation is a separately authorized §8 slot.

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these six):**

1. **D-CFG-1** — the governing mechanism: correctness by recorded identity, not by removed freedom.
2. **D-CFG-2** — record immutability attaches at `SCORED`, not at `FINALIZED`, plus its enforcement duties.
3. **D-CFG-3** — proof-set completeness is scoped to the registered composition, not fixed at five.
4. **D-CFG-4** — registered UWR profiles become per-strategy configuration.
5. **D-CFG-5** — configuration-version immutability, and the tier treatment of a configuration change.
6. **D-CFG-6** — goldens pin the `(configuration, input) → score` pair.

**Does not decide:** any scoring value, weight, axis, or rubric change for the existing `froggy` / `trend_pullback_v1` identity; the enrichment→scorer input mapping contract; qualification, reputation, reward, mint, or settlement anything; execution/order-placement; authentication or tenancy; UP-8 decay-engine canonicality; the D3 half-life unit question; or any deployment.

---

## 1. D-CFG-1 — The governing mechanism: recorded identity, not removed freedom

**Decision.** For the analyst-configuration span between `VALIDATED` and `SCORED` (the interior FCP-GOV governs), AFI's governance guarantees correctness by **recording the identity of the configuration that produced a determination**, not by **restricting configurations to a single approved instance**. Where a prior clause achieves an anti-drift guarantee by pinning a value that an analyst is entitled to choose, and an equivalent guarantee is available by stamping that value's identity into the sealed record, the stamping form is the governed form.

This clause is **interpretive and prospective**. It creates no authority on its own, moves no value, and does not license any change not enumerated in D-CFG-2 through D-CFG-6. It is the standard against which future filings in this span are read.

Two invariants it does **not** relax, and which every clause below preserves:

- **No silent drift.** A determination made under a different configuration must be distinguishable from one made under another, by hash, in the record itself.
- **No fabricated completeness.** A determination that could not be computed as composed yields **no record** — never a degraded, defaulted, or partial one.

**Scope-guard.** Fixes an interpretive standard for the `VALIDATED`→`SCORED` span only. It amends no clause by itself, reaches no other span, and never supplies authority a subsequent decision would otherwise need.

## 2. D-CFG-2 — Record immutability attaches at `SCORED`

**Decision.** MONGO-GOV D-MONGO-5's immutability trigger is amended, prospectively as a governance-ledger fact: **a canonical scored-signal evidence record becomes immutable at the moment it is admitted to the canonical store in the LIFE-GOV `SCORED` state** — not at `FINALIZED`. Determination sealing and economic finality are different acts and are hereby separated.

Consequently:

1. **Records are written finalized.** The `finalized` marker on a canonical record henceforth means *"this determination is sealed"* and is set at admission. The `supersede()` path remains reachable **only** by an explicitly governed correction act naming the record and its cause; routine writes may never supersede.
2. **Verification is a duty, not a capability.** Admission-time recomputation of `recordHash`/`replayHash` (EV3-GOV D-EV3-7) is joined by a **periodic re-verification obligation** over the canonical store, and by **verify-on-read** wherever a canonical record is served outside the store. An unverifiable or mismatched record is surfaced as an integrity fault; it is never silently served.
3. **Custody is enforced, not assumed.** Write access to the canonical evidence store is restricted to the sole canonical writer (MONGO-GOV D-MONGO-3, unchanged). Read-only credentials are used for every non-writer consumer, including analytics and readout tooling.
4. **The analytics plane is unaffected and remains non-canonical** (MONGO-GOV `persistence-v0.1.md:72`). It carries no evidentiary weight and no immutability duty.

This changes **no** LIFE-GOV state, transition, or terminal; `FINALIZED` and `EPOCH_ELIGIBLE` retain their meaning and their CHAIN-GOV boundary role. It is **storage-layer immutability only** and MUST NOT be conflated with settlement finality (MONGO-GOV `persistence-v0.1.md:82`, unchanged and reaffirmed).

**Scope-guard.** Moves the immutability trigger and states three enforcement duties. It creates no lifecycle state, no correction workflow, no audit service, and no on-chain anything; it does not authorize the implementation, which is §8 slot `CFG-IMMUTABILITY`.

## 3. D-CFG-3 — Proof-set completeness is composition-scoped

**Decision.** EV3-GOV D-EV3-5(1) and the D-EV3-2 proof-set rule are amended, prospectively, to be **scoped to the registered composition** rather than fixed at five:

1. A scored evaluation requires **every enrichment lane its registered composition declares** to succeed. A declared lane that fails or degrades yields **no scored evaluation, no scored signal, and no evidence record** — the fail-closed law of D-EV3-5(1) is retained in full and is not weakened.
2. A canonical V3 record carries **exactly as many category proofs as its composition declares lanes**, unique by category, ordered ascending — replacing the fixed count of five. Proof validation continues to fail closed on a missing, duplicate, unknown, mis-ordered, or mismatched proof.
3. **A lane the analyst did not select is not a failure.** Deliberate non-selection is expressed in the registered composition — including via `nodeOverrides.enabled: false` on a lane node, which the governed config schema already admits and which today produces an unpersistable signal. This clause resolves that conflict in favour of the composition.
4. The declared lane set is part of the composition and is therefore already committed by `manifestHash` and `analystConfigHash`. A change to which lanes a strategy uses is a new registered composition, never a silent runtime variation.
5. **The canonical five-category namespace (FCP-GOV D-FCP-1) is unchanged.** This clause governs how many of those five a composition may select — never what the categories are, nor their identities, ordering, or schemas.

**Scope-guard.** Re-scopes proof-count completeness to the registered composition and reconciles it with `nodeOverrides.enabled`. It changes no category identity, no proof schema, no hash law, no graph geometry, no join semantics, and no scored value on any existing composition; the existing five-lane `froggy` composition is byte-unaffected.

## 4. D-CFG-4 — Registered UWR profiles become per-strategy configuration

**Decision.** RC-GOV and UP-GOV are amended, prospectively, in exactly these respects:

1. **RC-5's identity predicate is retired as a permanent invariant.** It was expressly a v0.1 provision under which *"consumption is provenance, not behavior."* Henceforth a registered UWR profile's weights **are** behavior: the validated registry values flow into the computed configuration. Validation continues to fail closed on a malformed, unregistered, or schema-invalid profile — **no silent fallback**, RC-4's fail-closed rule retained in full.
2. **RC-3's source default flips to `registry`.** RC-3 reserved this flip to "a separate future decision"; this is that decision. `defaultUwrConfig` (RC-8) is retained as the compile-time fallback of last resort **only** for a strategy whose registration names no profile.
3. **UP-10's single-identity recognition is generalized.** A registered profile is recognized for the analyst/strategy identities its registration names. UP-10's requirement that additional analysts, strategies, or profiles be **registered and pinned, never silent**, is retained in full and extended to all of them.
4. **UWR resolution becomes per-strategy.** The per-process singleton is retired; configuration is resolved per determination from the strategy registration in scope. The resolved profile's identity continues to be stamped in the record.
5. **RC-6's stamp semantics are retained and extended:** the persisted source discriminator remains, and the stamp now records the resolved profile identity per determination rather than per process.
6. **RC-7 is amended** by this decision to pre-authorize the bounded guardrail amendments the above requires, each inert until its §8 slot is authorized: the `registries/uwr-profiles` string ban and the stamp-shape assertions may be updated to reflect per-strategy resolution. **The `src/pipeheads` and `src/cli` bans stay unchanged.**
7. **UP-3 (engine), UP-4 (axes), UP-6 (output surface), UP-7 (decay template set) are unchanged.** What becomes configurable is the **weights**, and which registered profile applies — not the combiner, the axis set, the output ranges, or the template surface.

**Scope-guard.** Frees registered weights and per-strategy profile resolution only. It changes no weight value for any existing registration — `uwr-weighted-lifts-v0.1` keeps `0.25/0.25/0.25/0.25` and the `uwrScore 0.1875` anchor holds for the `froggy` identity — and it authorizes no scoring change to any existing strategy. UP-8, UP-9, UP-11, and RC-11's untouched boundaries remain untouched.

## 5. D-CFG-5 — Configuration-version immutability, and the tier of a configuration change

**Decision.**

1. **A registered configuration version is immutable once any signal has been scored under it.** Changes register a **new** version; a version under which determinations exist is never edited. This is the analyst-facing counterpart of D-CFG-2 and it is what makes configuration freedom safe: an analyst may create v2 at any time, and every prior record still resolves to the exact v1 that produced it.
2. **Tier treatment (amending GPR-GOV D-GPR-2 in this bounded respect).** Registering a **new** configuration version — a new UWR profile, a new composition selecting a different lane subset, a new decay configuration — that (a) moves no already-persisted scored value, (b) moves no golden, KAT, or oracle byte, (c) changes no governed schema, hash law, or hash preimage, and (d) touches no token, mint, settlement, emissions, or staking surface, is **Tier S**. It is recorded, never unrecorded — the registration and its hash remain governed facts.
3. **The Tier F trigger is otherwise unchanged.** Changing the *schema* of what is configurable, the loader law, the combiner, the hash law, the axis set, or any existing registration's scored values remains **Tier F**. This clause narrows the tier of *exercising* a governed configuration surface; it does not narrow the tier of *changing* one. GPR-GOV D-GPR-3 continues to apply in full: if a change believed to be Tier S turns out to move a score, hash, or golden byte, **stop and upgrade to Tier F**.
4. **SV-GOV D-SV-1 is consumed, not re-decided.** Axis-semantics changes do not bump `strategyVersion`; a new configuration version under this clause is a configuration-identity act, expressed through `analystConfigHash` and the composition pin, exactly as SV-GOV's reading of the change-control texts provides.

**Scope-guard.** Fixes configuration-version immutability and the tier of exercising a governed configuration surface. It does not narrow Tier F for schema, loader, combiner, hash, or scored-value changes; it creates no automatic-acceptance path; and no Tier S act may ever authorize a Tier F act.

## 6. D-CFG-6 — Goldens pin the `(configuration, input) → score` pair

**Decision.** Where a golden, KAT, or oracle fixture pins a scored value, it pins that value **against a named configuration identity** — minimally the resolved profile identity and `analystConfigHash` — rather than against an input alone. Existing fixtures are re-recorded to name the configuration they already assume; **their scored-value bytes do not move**, and any regeneration must document field-level intentional diffs with all scored-value fields byte-unchanged (the D-FLPR-5(5) / D-EV3-5(1) precedent). The `312da118…126e06` golden anchor and the `uwrScore 0.1875` KAT anchor remain acceptance criteria for the `froggy` identity.

**Scope-guard.** Changes what a fixture *identifies*, never what it *asserts*. It authorizes no scored-value movement, creates no new fixture family, and does not relax the byte-stability gate for any existing composition.

---

## 7. Explicit non-authorizations

This decision does **not** authorize, and no implementation may infer from it:

- Any change to a scored value, weight, axis, rubric, or golden byte for the existing `froggy` / `trend_pullback_v1` identity.
- Feeding a submitted or declared trade direction into any analyst bias or axis input — **DIR-GOV D-DIR-3 stands unamended and is expressly reaffirmed**, including its finding that doing so hands score to a signal merely for asserting a side.
- Any change to the enrichment→scorer input mapping, which remains implementation-layer code and is not governed by this decision.
- Qualification, reputation, reward eligibility, mint, emissions, or settlement work of any kind; the reserved ATLAS-GOV and CHAIN-GOV scopes are untouched.
- Execution, order placement, authentication, tenancy, a read API, a preview/dry-run surface, or a user interface.
- Resolving UP-8 decay-engine canonicality or the half-life unit question.
- Any deployment, any migration framework, any second executor, any relaxation of FCP-GOV D-FCP-8's no-demo-fallback rule, or any implication of production promotion (R1-GOV D-R1-2).
- Self-ratification: acceptance is the owner's merge (AD Part F).

## 8. Implementation slots

Each slot is **inert until the owner authorizes it**. Accepting this decision authorizes zero code PRs.

| Slot | Scope | Gate |
|---|---|---|
| `CFG-IMMUTABILITY` | D-CFG-2: finalize at admission, periodic re-verification, verify-on-read, store role separation. **Note for the implementer:** the submit validator presently *requires* the opposite — `"finalized must be false for a SCORED record"` (`afi-reactor/src/evidence/submitScoredSignalEvidence.ts:103`) — and the store's supersession guard keys off `isFinalized` (`afi-infra` `MongoScoredSignalEvidenceStore.ts:236-241`). Both are inside this slot's authorization; neither may be changed outside it | Goldens byte-stable; no scored value moves; re-verification proven against seeded records; the governed-correction path proven to remain reachable |
| `CFG-PROOF-SCOPE` | D-CFG-3: composition-scoped proof count; `nodeOverrides.enabled` reconciliation | Existing five-lane composition byte-unchanged; fail-closed on declared-lane failure proven by test |
| `CFG-WEIGHTS` | D-CFG-4: loader predicate retirement, source default flip, per-strategy resolution, singleton retirement, RC-7 bounded guardrail amendments | `uwrScore 0.1875` anchor holds for `froggy`; `312da118…126e06` byte-stable; new tests added to the jest allowlist |
| `CFG-FIXTURES` | D-CFG-6: re-record fixtures to name their configuration identity | Scored-value fields byte-unchanged; intentional diffs documented |
| `CFG-ANALYTICS-STAMP` | Copy `compositionRef` into the analytics plane (`scoringContextStore`) | Non-canonical plane; no canonical surface touched |

## 9. Supersessions and interactions (touch-scoped, GPR-GOV D-GPR-1)

- **MONGO-GOV** (`persistence-v0.1.md`) — **amended** by D-CFG-2: the D-MONGO-5 immutability trigger moves from `FINALIZED` to `SCORED`. Write-once/append-only, one-current-record-per-`signalId`, supersession-not-in-place-edit, durable retention, the operational-store carve-out (`:72`), and the settlement-finality separation (`:82`) are **unchanged**. D-MONGO-3 sole-writer is unchanged and reinforced.
- **EV3-GOV** (`evidence-v3-provider-provenance-v0.1.md`) — **amended** by D-CFG-3: D-EV3-5(1)'s fixed five-lane completeness and D-EV3-2's fixed five-proof set become composition-scoped. The fail-closed law, the sole-builder rule, the capture seam, the no-re-versioning determination, D-EV3-4's hash law, and D-EV3-7's admission contract are **unchanged**. D-EV3-7's recomputation-before-insert is **extended**, not replaced, by D-CFG-2(2).
- **RC-GOV** (`uwr-runtime-consumption-v0.1.md`) — **amended** by D-CFG-4: RC-5's identity predicate retired as a permanent invariant; RC-3's default flipped to `registry` (the flip RC-3 reserved); RC-8 demoted to last-resort fallback; RC-6 extended to per-determination resolution; RC-7 extended with bounded pre-authorizations. RC-4's fail-closed rule and RC-11's untouched boundaries are **retained in full**. RC-1's single-identity program scope is **completed and superseded** by generalization.
- **UP-GOV** (`uwr-profile-pin-v0.1.md`) — **amended** by D-CFG-4: UP-10's single-identity recognition generalized to registered identities; its registered-and-pinned-never-silent requirement retained and extended. UP-3, UP-4, UP-6, UP-7 **unchanged**; UP-5's weights remain the pinned values *for `uwr-weighted-lifts-v0.1`*; UP-8, UP-9, UP-11 **untouched and still open/binding as written**.
- **GPR-GOV** (`governance-process-rightsize-v0.1.md`) — **amended** by D-CFG-5(2) in one bounded respect: registering a new configuration version that moves no persisted value, golden byte, or governed schema is Tier S. D-GPR-1, D-GPR-3, and D-GPR-4 are **unchanged**; the Tier F trigger is otherwise unchanged.
- **FCP-GOV** (`factory-configurable-pipelines-v1.md`) — **consumed and completed, not amended.** This decision releases the single-instance bounds that RC/UP/EV3 placed on the composition model FCP-GOV authored. D-FCP-1's five-category namespace, D-FCP-2's executor boundaries, D-FCP-3's contract delegation, D-FCP-5's generic registration rule, and D-FCP-8's no-demo-fallback rule are **unchanged and depended upon**.
- **LIFE-GOV** (`lifecycle-v0.1.md`) — **consumed, not amended.** No state, transition, or terminal changes. D-CFG-2 changes only *when a storage-layer property attaches*, not the machine. The observation that `FINALIZED` is presently unreachable is recorded as a fact, not a lifecycle change.
- **CHR-GOV** (`challenge-retirement-v0.1.md`) — **consumed.** Its retirement of the challenge layer is one reason `CHALLENGE_OPEN`, and therefore `FINALIZED`, is unreachable; its carve-outs (qualification, maturity/escrow, settlement-layer challenge, DAO infrastructure) are **untouched**.
- **SV-GOV** (`strategy-version-semantics-v0.1.md`) — **consumed, not re-decided** (D-CFG-5(4)).
- **DIR-GOV** (`scored-signal-direction-restoration-v0.1.md`) — **consumed and expressly reaffirmed** (§7). D-DIR-3 stands unamended.
- **OBJ-GOV**, **R1-GOV**, **AD** — consumed as framing; unchanged.
- **Every other accepted decision on `decisions/INDEX.md` — untouched.**

---

**Status footer:** **Proposed** — becomes authoritative on owner merge. On acceptance, add a direct-to-main record-acceptance commit flipping only this Status line and this footer, per the established convention.
