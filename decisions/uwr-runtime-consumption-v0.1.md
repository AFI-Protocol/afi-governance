# AFI Runtime UWR Registry Consumption v0.1 (Staged Authorization Framework, Testnet-Provisional)

**Status:** **Accepted** owner decision — accepted by merge of afi-governance PR #9 on 2026-07-13 (merge commit `d600c5c`, merged unedited, so every **OWNER DECISION** proposed default below is in force as written). **This decision authorizes no code change by itself**: it authorizes no implementation PR until the owner flips the corresponding §7 row (all rows remain "No" as of acceptance). This is **not** production scoring law: everything below is **testnet-provisional** unless separately re-governed.
**Date:** 2026-07-12 (draft authored); accepted 2026-07-13 (PR #9, merge commit `d600c5c`)
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md`, `decisions/math-authority-v0.1.md`, `decisions/mint-formula-bt-86b-alignment-v0.1.md`, `decisions/uwr-profile-pin-v0.1.md`, and existing settlement/district doctrine in `afi-docs`. Where this decision conflicts with the Charter, the Charter wins.
**Ledger slot:** None existed — that gap is this decision's reason for being. `decisions/uwr-profile-pin-v0.1.md` §7 enumerates follow-up work but reserves **no row** for runtime consumption; its UP-2 explicitly anticipates "a separately-authorized runtime PR" but reserves no ledger row for it, and UP-12/§6/§8 defer the work to a future scoped authorization. This decision creates the missing authorization framework and named PR slots.

---

## 1. Purpose

The version-pinned profile chain is complete through stamping and CI enforcement, and **nothing consumes the registered profile at runtime**:

- `decisions/uwr-profile-pin-v0.1.md` (accepted 2026-07-11, merged via afi-governance PR #8, merge commit `ba790fd`) pinned profile `uwr-weighted-lifts-v0.1` (UP-1…UP-12).
- **PR-UWR-CONFIG** (afi-config PR #17, merge `fe32916`) registered the profile: schema, sole registry instance, KAT vectors — pure data.
- **PR-UWR-KAT-EXEC** (afi-core PR #17, merge `23fb99a`) executes the vendored KAT vectors in afi-core's test suite.
- **PR-7** (afi-core PR #16, merge `2541853`) delegated the Greeks decay kernel to `afi-math` bit-exactly; UP-8 (decay-engine canonicality) remains OPEN.
- **PR-UWR-STAMP** (afi-reactor PR #39, merge `175940a`) stamps the profile id into persisted `ReactorScoredSignalDocument` records — as **value-identity metadata only**: the stamp is hardcoded in `src/config/uwrProfilePin.ts` and performs no registry read.
- afi-config PR #18 (merge `ce8c1de`) made CI actually run the 197 vitest pin guards protecting the registered data.

Meanwhile the live scorer still runs `defaultUwrConfig` (`id: "uwr-default-stub"`, `afi-core/validators/UniversalWeightingRule.ts`), whose in-code TODO says to replace it with governance-approved weights sourced from `afi-config`. The registered profile and the builtin stub are **value-identical by construction** (UP-5: four 0.25 weights; D2 M2 golden anchor `uwrScore 0.1875`), so consuming the registry is a **provenance upgrade, not a behavior change** — the whole point is that the config a signal was scored under becomes a loadable, pinnable, replayable artifact instead of a compile-time constant.

This decision defines the staged program under which that consumption may be built: ownership, source-selection, failure mode, stamp semantics, guardrail amendments, and gates — each stage a named §7 slot requiring its own explicit go-ahead.

This is a governance/docs decision only. It does not change runtime behavior anywhere.

## 2. Sources

Repo states verified 2026-07-12 against `origin/main` (the newest cited merge timestamps fall on 2026-07-13 UTC): afi-governance @ `ba790fd`, afi-core @ `23fb99a`, afi-reactor @ `175940a`, afi-config @ `ce8c1de`. A read-only planning recon (multi-agent, with adversarial re-verification of every cited reference) preceded this decision; its material findings are restated here rather than referenced, because the planning report lives outside version control.

1. **afi-core** @ `23fb99a`:
   - `validators/UniversalWeightingRule.ts` — `UniversalWeightingRuleConfig`; `defaultUwrConfig` (`id: "uwr-default-stub"`, four 0.25 weights; TODO: "Replace with governance-approved weights sourced from afi-config"); `computeUwrScore(axes, config = defaultUwrConfig)`.
   - `analysts/froggy.trend_pullback_v1.ts` — **imports** `defaultUwrConfig` from the canonical module (it is not an inline copy): `scoreFroggyTrendPullback` takes it as a default parameter and `scoreFroggyTrendPullbackFromEnriched` passes it explicitly. There is exactly **one** definition of the default config in the codebase — a single substitution point.
   - Packaging: `validators/index.ts` does **not** re-export `UniversalWeightingRule`; the module is reachable only via the `./validators/*` subpath export, and the root entry dangles (`main`/`exports["."]` point at `./dist/index.js`, which is not built — no root `index.ts` exists). afi-core has **no dependency on afi-config** and **no production `fs` use** (`node:fs` appears only in the two KAT test files).
2. **afi-reactor** @ `175940a`:
   - afi-reactor imports **no** UWR-config symbols (`computeUwrScore`, `defaultUwrConfig` appear nowhere as imports). UWR config is exercised only *implicitly*, inside the afi-core scorer call, on two paths: the D2 scoring pipehead (`src/pipeheads/scoringPipehead.ts`, dynamic import of the froggy scorer) and the froggy plugin path (`plugins/froggy.trend_pullback_v1.plugin.ts` → `src/services/froggyDemoService.ts`).
   - `src/config/uwrProfilePin.ts` — hardcoded pin (`UWR_PROFILE_ID = "uwr-weighted-lifts-v0.1"`), no `fs` import, no registry read; `uwrProfileStampFor` recognizes only the UP-10 identity.
   - `test/guardrails/uwrProfileStamp.test.ts` (jest-allowlisted) enforces the UP-12 boundary in source text: **no TypeScript source file (`.ts`) under `src/` may contain the string `registries/uwr-profiles`**, and **no `.ts` file under `src/pipeheads` or `src/cli` may reference the UWR-profile pin identifiers** (the scan covers `.ts` files only — a recorded limitation; see RC-7). It also performs a test-only sibling cross-check against the afi-config registry instance when present, comparing `profileId`, `status`, and `scorerIdentity` — **not** weight values.
   - **Load precedent:** `package.json` declares `"afi-config": "file:../afi-config"`, and three modules load afi-config schema JSON at module top-level via `readFileSync(join(process.cwd(), "node_modules/afi-config/…"))` inside try/catch, degrading to structured `{ok:false}` results: `src/pipeheads/provenance/schemaValidation.ts` (nine provenance v1 schemas), `src/uss/ussValidator.ts`, `src/cpj/cpjValidator.ts`.
   - `test/pipeheads/fixtures/golden.json` — D2 M2 golden; sha256 `312da1180b0bd418c03f595093516ebdc755ba81465a0b526ace43d002126e06`; must never change under this program.
3. **afi-config** @ `ce8c1de`:
   - `registries/uwr-profiles/uwr-weighted-lifts-v0.1.json` — the sole registry instance (single-profile rule test-enforced), value-identical to `defaultUwrConfig`.
   - **Packaging defect (recorded, not fixed here):** `package.json` `main` points at `dist/index.js`, which is not built (no root `index.ts`; `dist/` holds only compiled `cli_utils` and tests, zero JSON); there is **no `exports` field** and **no `files` field**. Consequence: the package entry is unusable, and raw file read (or a deep JSON path) is the **only** way a consumer can load the registry today. Conversely, if afi-config ever adds an `exports` map that omits `./registries/*`, deep imports would break — packaging must be decided deliberately (RC-9).
   - CI: since PR #18 (merge `ce8c1de`), the workflow runs `npm run test:run` — 197 pin guards (schema consts, single-profile rule, KAT anchors, byte-identical example drift guard) verified passing on `main`.
4. **afi-governance** @ `ba790fd`: `decisions/uwr-profile-pin-v0.1.md` — UP-2 ("Once a separately-authorized runtime PR consumes the registered profile, `uwr-default-stub` is superseded… Until then, `defaultUwrConfig` remains in place unchanged"); UP-12 ("It does **not** authorize: consuming the registry at runtime, modifying `defaultUwrConfig`…"); §6 ("runtime code changes (any repo)"); §7 (no runtime-consumption row); §8 ("runtime consumption… remain future governed promotions").
5. **Cross-repo negative findings** (recon, adversarially verified): no repo outside afi-core/afi-reactor consumes UWR config in any form. `afi-gateway` holds only a response-contract *type* with drifted axis names (the UP-4-noted non-conformant copy) and score logging from reactor HTTP responses. `afi-mint`'s `ValidatorConfig` doc-comment "(sourced from afi-config)" has **no loading code behind it** — a recorded anti-pattern this program must not repeat: never claim config sourcing that is not implemented.

## 3. Decision Summary

Identifier note (mirroring UP-1's identifier-overloading caution): **OWNER DECISION n** identifiers are local to this document's acceptance checklist and are unrelated to `math-authority-v0.1.md`'s "Open Decision" numbering.

| # | Decision | Testnet-provisional outcome |
|---|---|---|
| RC-1 | Program scope | Staged runtime-consumption program for exactly profile `uwr-weighted-lifts-v0.1`, scorer identity per UP-10; each stage is a named §7 slot, none authorized by this decision itself |
| RC-2 | Ownership split | `afi-core` owns validation semantics via a **pure loader** (no `fs`, no afi-config dependency); `afi-reactor` owns the file read at its **composition root**; `afi-gateway` owns nothing — **OWNER DECISION 2** |
| RC-3 | Source selection | An explicit flag (proposed `AFI_UWR_PROFILE_SOURCE`, values `builtin \| registry`, **default `builtin`**) selects the config source; flipping the default is a separate future decision — **OWNER DECISION 3** |
| RC-4 | Failure mode | While the flag selects `registry`: load + validate + identity cross-check (predicate defined in RC-5), **fail-closed** on load failure or predicate failure; **no silent fallback**. Fallback-with-warning is rejected for scoring config — **OWNER DECISION 1** |
| RC-5 | Identity invariant | For v0.1 the loaded profile must satisfy an explicit identity predicate against `defaultUwrConfig` (weights and axes equal; ids related by pinned supersession, not equality); consumption is provenance, not behavior; goldens and the `0.1875` anchor are acceptance criteria for every program PR. Cross-check permanence: **OWNER DECISION 8** |
| RC-6 | Stamp semantics | Stamp upgrades from value-identity to consumed-profile **only** when the flag selects `registry` and the cross-check passed; persisted records carry a **source discriminator** forever — **OWNER DECISION 5** |
| RC-7 | Guardrail amendment | `test/guardrails/uwrProfileStamp.test.ts` may be amended only via two bounded pre-authorizations, each inert until its §7 row flips: (1) inside PR-UWR-RUNTIME-READ, the `src/`-wide `registries/uwr-profiles` string ban is narrowed to exempt the single authorized loader module; (2) inside PR-UWR-STAMP-SEMANTICS, the stamp-shape/wiring assertions are updated to reflect RC-6. The `src/pipeheads` + `src/cli` bans stay unchanged in both |
| RC-8 | `defaultUwrConfig` transition role | Remains the builtin source, unmodified, while the flag defaults `builtin`; retirement requires a future decision and defined preconditions — **OWNER DECISION 4** |
| RC-9 | Packaging mechanism | Raw file read via the existing `file:` dependency precedent is the sanctioned load mechanism for now; an optional packaging slot (exports map) is reserved — **OWNER DECISION 7** |
| RC-10 | Program gates | Every program PR: afi-config pin guards green in CI, afi-core KAT suites green, afi-reactor goldens byte-stable (`312da118…126e06`), new test files added to the jest allowlist, and the PR body names its §7 slot and links the owner's go-ahead |
| RC-11 | Untouched boundaries | Qualification wiring (UP-9), mint/reward/payout/settlement, UP-8 canonicality, production scoring law, additional profiles/strategies: all **unchanged and not authorized** |
| RC-12 | Authorization scope | Accepting this decision authorizes **zero code PRs**; it creates the framework and the §7 ledger; each slot needs its own explicit owner go-ahead (flipped row, or an owner-authored PR approval comment with the row flipped no later than merge) — **OWNER DECISION 6** is the acceptance of this framework itself |

## 4. Detailed Decisions

### Decision RC-1 — Program scope and object

**Recorded:** This decision defines a staged program to make the afi-reactor scoring path consume the registered profile `uwr-weighted-lifts-v0.1` from the afi-config registry at runtime, superseding reliance on the compile-time `defaultUwrConfig` stub **for the UP-10 scorer identity only** (`analystId "froggy"` / `strategyId "trend_pullback_v1"`).

Clarifications:

- The program covers exactly one profile and one scorer identity. Additional analysts/strategies or profiles remain governed by UP-10's registration rule and are out of scope.
- The program's end state (all §7 slots landed, flag default flipped by a future decision) is: scorer config loaded from the registry, validated, cross-checked, stamped as consumed, KAT-re-executed — with `uwr-default-stub` retired per RC-8's preconditions.
- Nothing in this decision or its program touches scored *values*. Any PR that changes a scored value has exceeded its authorization and must be rejected (RC-5, RC-10).

### Decision RC-2 — Ownership split (OWNER DECISION 2)

**Recorded (proposed default):** Validation semantics belong to `afi-core`; I/O belongs to `afi-reactor`; `afi-gateway` owns nothing.

- `afi-core` gains a **pure** loader/validator — working name `loadUwrProfile(profileJson: unknown): UniversalWeightingRuleConfig` — that validates a passed-in, already-parsed JSON document (profile id, schema id, axes registry and order, weight shape and bounds) and maps it onto `UniversalWeightingRuleConfig`. **No `fs`, no path resolution, no afi-config dependency**: afi-core's zero-fs, zero-afi-config posture is preserved (verified in §2 item 1). Export via an explicit subpath consistent with the existing `./validators/*` pattern; the dangling root export (§2 item 1) must not be relied upon.
- `afi-reactor` reads the registry file at its composition root, following its own three-site precedent (§2 item 2): `file:` dependency, `readFileSync` under `node_modules/afi-config/`, top-level try/catch — but with RC-4's fail-closed semantics instead of the schema validators' degrade-to-`{ok:false}` semantics, because scoring config is not a validation convenience (see RC-4 rationale).
- The read must live **outside `src/pipeheads` and `src/cli`** (RC-7 keeps those bans), under `src/config/` where the pin module already lives; the final module path is fixed by the module named in the PR-UWR-RUNTIME-READ body.

Alternatives the owner may substitute: (a) afi-reactor also owns validation (self-contained, but duplicates schema knowledge afi-core must hold anyway for KAT re-execution); (b) afi-core reads files itself (rejected as proposed default: breaks afi-core's pure posture and adds an afi-config dependency to the engine repo).

### Decision RC-3 — Explicit source-selection flag (OWNER DECISION 3)

**Recorded (proposed default):** Consumption is **flag-gated**. A single explicit configuration input — proposed name `AFI_UWR_PROFILE_SOURCE`, values `builtin | registry`, **default `builtin`** — selects the config source at the afi-reactor composition root.

Clarifications:

- With `builtin` (default), behavior is today's: `defaultUwrConfig` inside the afi-core scorer; the registry file is not read; the stamp stays value-identity (RC-6).
- With `registry`, the RC-2 read + RC-4 semantics apply.
- **Flipping the default to `registry` is a separate future decision**, expected only after the program's slots have all landed and soaked. A flag that never flips is governance debt; the flip decision should be scheduled, not forgotten (§7 "Future decision" row).
- The exact mechanism (environment variable vs config file field) is an implementation detail for PR-UWR-RUNTIME-READ, but it must be explicit, logged at startup, and impossible to enable by accident.
- Alternative the owner may substitute: no flag — direct cutover with value-identity cross-check. Rejected as proposed default because it removes the staged-rollout and replay-comparison affordances at near-zero savings.

### Decision RC-4 — Failure mode: fail-closed, no silent fallback (OWNER DECISION 1)

**Recorded (proposed default):** While the flag selects `registry`: the composition root loads the registry file, validates it via the RC-2 loader, and cross-checks the result against `defaultUwrConfig` under the RC-5 identity predicate. **Any failure — missing file, parse error, schema violation, or failure of any RC-5 predicate condition — refuses to score** (fail-closed). There is **no automatic fallback to `defaultUwrConfig`**.

Clarifications:

- The fallback-with-loud-warning pattern is explicitly **rejected** for scoring config, for a reason specific to this program: the registry and the builtin are value-identical, so a silently flipped source is **invisible in every output**. The one failure the fallback "handles" is precisely the one it cannot surface. A warning nobody reads is not a control; a refusal is.
- Fail-closed is deliberately *stricter* than the reactor's existing schema-load precedent (degrade to structured `{ok:false}`). Schema validation is an annotation on artifacts; scorer config *is* the scoring law's runtime carrier. The asymmetry is intended and recorded.
- Because the flag defaults `builtin`, fail-closed cannot brick any environment that has not explicitly opted in. Dev environments without a sibling/installed afi-config simply stay on `builtin`.
- Alternatives the owner may substitute: (a) fallback-with-warning (rejected above); (b) fail-closed only in non-dev environments (adds an environment-detection surface — more machinery than the flag itself).

### Decision RC-5 — Identity invariant and golden gates (OWNER DECISION 8 for permanence)

**Recorded:** For profile v0.1 the loaded registry document must satisfy the following **identity predicate** — which is also RC-4's mismatch definition:

1. the four weights equal `defaultUwrConfig`'s per axis (`structureWeight` / `executionWeight` / `riskWeight` / `insightWeight`, each exactly `0.25`);
2. the axes array equals `["structure", "execution", "risk", "insight"]` in content and order (UP-4);
3. `profileId` equals the pinned `uwr-weighted-lifts-v0.1` (UP-2/UP-10) **and** `supersedes` equals `defaultUwrConfig`'s id `uwr-default-stub` (UP-2's supersession, checked as data);
4. id fields are deliberately **excluded** from direct equality against `defaultUwrConfig.id` — the ids differ by design; supersession, not equality, is the pinned relationship.

Consumption under this program is a **provenance upgrade with provably unchanged behavior**: the D2 M2 goldens (sha256 `312da118…126e06`) and the `uwrScore 0.1875` anchor are byte-stable acceptance criteria for **every** PR in the program (RC-10).

Clarifications:

- The runtime predicate is **strictly stronger** than the guardrail test's existing offline sibling check, which compares `profileId`/`status`/`scorerIdentity` only (§2 item 2). Weight-value identity is currently enforced only by afi-config's pin guards plus construction; RC-4 makes it runtime-checked for the first time.
- **OWNER DECISION 8:** whether the cross-check is (a) transition-only — removed by the future decision that flips the flag default and retires the stub — or (b) a **permanent invariant while exactly one profile exists** (proposed default: **(b)**; it is cheap, and it converts any future registry tampering or accidental value drift into an immediate, loud refusal instead of a silent scoring-law change).
- When a genuinely different profile version is ever registered (new id, per UP-5), the cross-check's referent changes by definition and this clause must be revisited by that profile's decision.

### Decision RC-6 — Stamp semantics upgrade (OWNER DECISION 5)

**Recorded (proposed default):** The persisted stamp's meaning upgrades from *value-identity* to *consumed-profile* **only** for records scored while the flag selected `registry` **and** the RC-4 cross-check passed. Persisted records gain a **source discriminator** — e.g. `uwrProfile.source: "builtin-value-identity" | "registry-consumed"` — carried **forever**, so records written before, during, and after the transition remain unambiguously interpretable in replay and challenge contexts.

Clarifications:

- PR-UWR-STAMP's post-merge clarification stands: today's stamp is persisted-record metadata only. Nothing may claim consumption before consumption exists (the afi-mint "(sourced from afi-config)" comment-only fiction in §2 item 5 is the recorded cautionary example).
- The discriminator's exact field name/values are PR-UWR-STAMP-SEMANTICS implementation detail; what is decided here is that the distinction **must** exist in the persisted record, not in logs or convention.
- Records already written with the value-identity stamp are not rewritten; absence of the discriminator identifies the pre-program era.

### Decision RC-7 — Guardrail amendment authorization

**Recorded:** `afi-reactor/test/guardrails/uwrProfileStamp.test.ts` encodes the UP-12 boundary in source text; amending it is a governance act. This decision pre-authorizes exactly **two** bounded amendments. A pre-authorization is **inert until the named slot's §7 row is flipped** (RC-12): it bounds what that slot's executing PR may contain; it does not itself authorize the PR or the amendment. Each slot name means *the PR executing that flipped row*, not any PR bearing the name.

1. **Inside PR-UWR-RUNTIME-READ only:** the `src/`-wide ban on the string `registries/uwr-profiles` is narrowed to: **banned everywhere under `src/` except the single authorized loader module** named in that PR's body (expected under `src/config/`).
2. **Inside PR-UWR-STAMP-SEMANTICS only:** the stamp-shape and wiring assertions (exact-shape stamp equality; the conditional-spread wiring check) may be updated to reflect the RC-6 source discriminator and consumed-profile condition — and only that.

In both cases: the bans covering `src/pipeheads` and `src/cli` (UWR-pin identifiers; D2 golden byte-stability per UP-5/UP-11) remain **unchanged**; the test-only sibling cross-check remains (or is strengthened — e.g. extended to weight values per RC-5), never deleted. The guardrail scan currently covers `.ts` files only (§2 item 2); either amendment may additionally **strengthen** the scan's file coverage, and neither may weaken it.

Any other change to the guardrail test — including deletions, renames, or allowlist widening — is outside these pre-authorizations and requires its own decision.

### Decision RC-8 — `defaultUwrConfig` transition role and retirement (OWNER DECISION 4)

**Recorded (proposed default):** `defaultUwrConfig` remains in place, **unmodified**, as the builtin source while the flag defaults `builtin`. Its retirement (deletion or demotion to test fixture) requires a **future decision**, with proposed preconditions: (1) the flag default has been flipped to `registry` by decision; (2) at least one full KAT re-execution cycle (PR-UWR-KAT-RERUN) has passed against the loaded profile; (3) goldens byte-stable throughout. Until that future decision, modifying `defaultUwrConfig` remains unauthorized (UP-12 posture unchanged).

Clarifications:

- The stub's in-code TODO ("Replace with governance-approved weights sourced from afi-config") is finally on a governed path to resolution; the TODO text itself may be updated to reference this decision **only inside PR-UWR-RUNTIME-LOADER** (named in that slot's §7 scope row) — never as a drive-by edit in any other PR.
- `computeUwrScore`'s default-parameter signature is an afi-core API question for PR-UWR-RUNTIME-LOADER to preserve; removing the default parameter is **not** authorized by this decision.

### Decision RC-9 — Packaging mechanism (OWNER DECISION 7)

**Recorded (proposed default):** The sanctioned load mechanism is the **raw file read through the existing `file:` dependency precedent** (§2 item 2). The afi-config packaging defect (§2 item 3: dangling `main`, no `exports`, no `files`, no JSON in `dist`) is recorded as a known defect, **not fixed by this program by default**.

Clarifications:

- An optional slot **PR-UWR-CONFIG-PACKAGING** is reserved in §7: afi-config gains an `exports` map including at least `./registries/*`, `./schemas/*`, `./kats/*`, and fixes or removes the dangling `main` entry (pure packaging; zero value changes; the 197 pin guards must stay green; the reactor's three existing schema-load sites must keep working). The owner may activate it before or after the runtime slots — or never.
- Constraint recorded for whoever lands packaging: an `exports` map that omits currently-deep-imported paths **breaks** the existing readFileSync consumers' path assumptions only if they migrate to import specifiers; the raw `node_modules/...` file path keeps working regardless. The packaging PR must state which consumers move and which do not.
- The path-resolution brittleness of `join(process.cwd(), "node_modules/…")` (breaks when the process launches from another cwd) is a **pre-existing** defect of the three schema-load sites. PR-UWR-RUNTIME-READ should prefer a cwd-independent resolution (e.g. `createRequire`/`import.meta.url`-anchored) for the new read; retrofitting the three existing sites is separate cleanup, not authorized here.

### Decision RC-10 — Program-wide gates

**Recorded:** Every PR executed under this program must satisfy, as acceptance criteria:

1. afi-config pin guards green in CI (the 197 vitest tests, CI-enforced since merge `ce8c1de`);
2. afi-core test suite green, including both KAT executor suites;
3. afi-reactor jest suite green **and** goldens byte-identical (`test/pipeheads/fixtures/golden.json` sha256 `312da1180b0bd418c03f595093516ebdc755ba81465a0b526ace43d002126e06`);
4. any new test file added to afi-reactor's explicit jest `testMatch` allowlist (unlisted test files silently do not run — recorded hazard);
5. the PR body states which §7 slot it executes and links the owner's go-ahead for that slot in the RC-12 form (flipped row commit, or owner-authored approval comment on that PR).

### Decision RC-11 — Boundaries this program does not touch

**Recorded:** The program changes where the scorer's configuration **comes from**, and nothing else:

- The qualification gate stays unwired (UP-9 posture; no `IValidatorScorer` implementation or composition).
- No mint, reward, payout, reactor→mint bridge, staking, or settlement work; UP-11's reward/mint gate is not advanced or interpreted by this program.
- UP-8 (decay-engine canonicality) stays OPEN; the program neither resolves nor prejudices it.
- No production scoring law; no non-provisional values; no additional profiles, analysts, or strategies.
- No gateway changes; the UP-4-noted gateway axes drift stays in its existing cleanup row in the pin decision's §7.

### Decision RC-12 — Authorization scope (OWNER DECISION 6)

**Recorded:** Accepting this decision (merging its PR) **authorizes zero code PRs**. It establishes the program's invariants (RC-1…RC-11) and the §7 authorization ledger. Each §7 slot is executed only after the owner flips its row to "Yes" by editing this document in a follow-up governance commit. As the sole alternative path, an **owner-authored approval comment on the executing PR itself** (attributable and timestamped on that PR's record) suffices to begin execution — provided a governance commit flipping the corresponding §7 row lands **no later than that PR's merge**, so this ledger never reads "No" for work that has shipped.

Clarifications:

- This mirrors UP-12's single-phase scoping discipline and the District 2 D-17 pattern, extended to a multi-slot ledger because this program has genuinely separable stages.
- **OWNER DECISION 6** is the meta-decision: accepting this framework at all. Rejecting it (closing the PR unmerged) leaves runtime consumption in its current state — deferred with no authorization path.

## 5. Rationale

- **The gap is real and this is the smallest thing that fills it.** Unlike KAT-EXEC and STAMP, runtime consumption had no named slot anywhere in governance; every prior mention defers it to a future scoped authorization. Without this framework, any consumption PR would arrive unauthorized by construction.
- **Fail-closed is chosen because the failure is invisible.** Value-identity between registry and builtin means output inspection can never reveal which source was used. The only honest control is refusal on mismatch plus a persisted source discriminator.
- **The staged ledger beats one big authorization.** Loader, read, stamp semantics, and KAT re-run have different blast radii and different reviewers' attention profiles; separate slots keep each merge a meaningful acceptance act (the existing chain — CONFIG, KAT-EXEC, STAMP — worked exactly this way).
- **Proposed defaults are taken from the verified recon, not preference.** Ownership follows the repos' demonstrated postures (afi-core: pure, no fs; afi-reactor: existing afi-config load precedent). The rejected alternatives are recorded alongside, so the owner edits rather than reconstructs.

## 6. Explicit Non-Authorization

This decision does **not** authorize (neither before nor after acceptance, until the corresponding §7 row is flipped):

- any code change in any repo — including the loader (PR-UWR-RUNTIME-LOADER), the registry read (PR-UWR-RUNTIME-READ), stamp changes (PR-UWR-STAMP-SEMANTICS), KAT re-execution changes (PR-UWR-KAT-RERUN), and packaging (PR-UWR-CONFIG-PACKAGING)
- modifying `defaultUwrConfig` or `computeUwrScore`'s signature or semantics
- amending `test/guardrails/uwrProfileStamp.test.ts` (pre-authorized only inside PR-UWR-RUNTIME-READ and PR-UWR-STAMP-SEMANTICS, per RC-7's two bounded grants, and only to the exact extent RC-7 states)
- flipping the RC-3 flag default to `registry` (future decision)
- retiring `uwr-default-stub` / `defaultUwrConfig` (future decision, RC-8 preconditions)
- changing UWR profile values, axes, weights, KAT vectors, or registering additional profiles/analysts/strategies
- re-pinning or regenerating D2 M2 goldens
- wiring the qualification gate; minting, reward routing, or the reactor→mint bridge; staking; settlement, vault, claims, or anchoring work
- resolving UP-8 / PR-7 decay canonicality
- gateway changes of any kind (including the axes-drift cleanup)
- the whitepaper §7.3 UWR combiner; AIM / AAG / SES; role weights
- production scoring law of any kind

## 7. Follow-Up PRs / Authorization Ledger

All rows start **not authorized**. The owner flips a row by editing this document in a follow-up governance commit; the sole alternative is an owner-authored approval comment on the executing PR with the row flipped no later than merge (RC-12; gate RC-10.5). Proposed execution order: top to bottom.

| Item | Repo | Scope | Authorized? |
|---|---|---|---|
| **PR-UWR-RUNTIME-LOADER** | afi-core | Pure `loadUwrProfile(profileJson)` validator mapping a registry document onto `UniversalWeightingRuleConfig` per the RC-5 predicate; no `fs`; no afi-config dependency; subpath export; unit tests; may update the `defaultUwrConfig` TODO comment to reference this decision (RC-8) | **Yes — row flip merged by owner per RC-12 (recorded 2026-07-13)** |
| **PR-UWR-RUNTIME-READ** | afi-reactor | Composition-root registry read behind the RC-3 flag (default `builtin`); RC-4 fail-closed semantics; cwd-independent path resolution preferred; guardrail amendment exactly per RC-7 grant (1); new tests jest-allowlisted | No — owner flips this row |
| **PR-UWR-STAMP-SEMANTICS** | afi-reactor | RC-6 source discriminator + consumed-profile stamp condition; guardrail stamp-shape/wiring assertions updated exactly per RC-7 grant (2) | No — owner flips this row |
| **PR-UWR-KAT-RERUN** | afi-core | Parameterize KAT executor suites to also run against a loaded (not builtin) profile document; zero vector changes | No — owner flips this row |
| **PR-UWR-CONFIG-PACKAGING** (optional) | afi-config | `exports` map incl. `./registries/*`, `./schemas/*`, `./kats/*`; fix or remove dangling `main`; zero value changes; pin guards + reactor schema loads keep working | No — owner flips this row |
| Future decision | afi-governance | Flip RC-3 flag default to `registry`; schedule per RC-3 clarification | No — separate decision |
| Future decision | afi-governance | Retire `uwr-default-stub` / `defaultUwrConfig` per RC-8 preconditions | No — separate decision |

## 8. Impact on Repo Authority Model

- **`uwr-profile-pin-v0.1.md`:** unchanged and not amended. Its UP-2 clarification ("Once a separately-authorized runtime PR consumes the registered profile…") now has the authorization *framework* it anticipated. Its §6/UP-12 non-authorizations remain accurate as written — this decision, not the pin, is the scoped authorization UP-12 anticipated, and each item is authorized only when the corresponding §7 row **here** is flipped. UP-8 remains OPEN. The gateway-axes and wording cleanups stay in that decision's ledger, untouched.
- **`math-authority-v0.1.md` Open Decision 8:** narrowed further only in that runtime consumption — one of the items §8 of the pin decision listed as "future governed promotions" — now has a governed path. The general combiner, mapping system, and production values remain future promotions.
- **Authority boundaries unchanged:** the engine stays in `afi-core`; registration and KAT vectors stay in `afi-config`; `afi-reactor` remains "Not a math authority" — it composes and persists, and under this program additionally *selects the source* of the pinned configuration without ever defining values; `afi-mint`, `afi-token`, `afi-math`, `afi-gateway` are untouched.

---

**OWNER DECISION checklist** (accept defaults by merging, or edit before merge):

1. **Failure mode** — fail-closed, no silent fallback (RC-4). *Proposed: accept.*
2. **File-read ownership** — afi-reactor composition root reads; afi-core validates purely (RC-2). *Proposed: accept.*
3. **Flag-gated** — yes; `builtin` default; flip is a future decision (RC-3). *Proposed: accept.*
4. **`defaultUwrConfig` retirement preconditions** (RC-8). *Proposed: accept.*
5. **Stamp source discriminator, consumed-only-after-consumption** (RC-6). *Proposed: accept.*
6. **Accept this framework at all** (RC-12) — the merge itself.
7. **Packaging** — raw file read sanctioned now; packaging slot optional (RC-9). *Proposed: accept.*
8. **Cross-check permanence** — permanent while a single profile exists (RC-5). *Proposed: accept.*
