# AFI Acceptance-Record Normalization v0.2 (ARN-GOV)

**Slot:** `AFI-GOV-ACCEPTANCE-RECORD-NORMALIZATION-v0.2` (ARN-GOV)
**Status:** **Accepted** owner decision — accepted by merge of afi-governance PR #33 on 2026-08-01 (merge commit `87b393d`, merged unedited). Owner authorization was recorded by the owner instruction that commissioned this decision (founder instruction of 2026-08-01: "Option B" — author a normalization decision recording the acceptance facts of the five early-era decisions whose Status text still reads Proposed, then flip their labels on its acceptance).
**Date:** 2026-08-01
**Type:** Scoped protocol-development governance decision (acceptance-record normalization — governance-ledger and status-label text only). It re-decides **no clause** of any instrument, authorizes **no** code, schema, contract, persistence, scoring, deployment, or economic act, and decides nothing beyond its six clauses. Versioned **v0.2** because the first acceptance-record normalization act is DSC-GOV **D-DSC-8** (embedded in `district-surface-consolidation-v0.1.md`, not a standalone instrument); this is the second batch, following that pattern.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` and `decisions/authority-districts-v0.1.md`. For the District-framing, non-production, and no-financial-truth invariants it defers to `decisions/current-authority-reroot-and-golden-closure-v0.1.md` (R1-GOV). **Consumes (does not re-decide)** all twenty-two prior decisions on the ledger. **Supersedes nothing** and fills no fence. **Honors, and does not touch,** the reserved `ATLAS-GOV` and `CHAIN-GOV` scopes. Where this decision conflicts with the Charter, the Charter wins; where it conflicts with any accepted decision, that decision wins.
**Evidence basis:** Findings are restated inline because the workspace `reports/` area is unversioned and is never authority. Verified 2026-08-01 against afi-governance `origin/main` @ `3d9d972` (clean tree) via `git log --follow`, `gh pr view`, the GitHub commits→pulls API, and per-file `git diff <acceptance-merge> HEAD`: each of the five instruments below landed on `main` via an **owner-merged pull request**; every pre-landing fix commit named below is **inside its landing PR** (pre-acceptance); and the current bytes of four of the five are **byte-identical** to their acceptance-merge bytes (zero diff), the fifth (LIFE-GOV) differing by exactly one owner-merged one-line amendment recorded in D-ARN-2. After the CITY-RET-GOV status flip (`3d9d972`, 2026-08-01), these five are the **only** decision files whose literal Status text still reads Proposed while standing on the accepted ledger.
**Ledger slot:** The second acceptance-record normalization batch (the first: DSC-GOV D-DSC-8, which normalized `authority-districts-v0.1.md`, `district-2-m2-ratification-v0.1.md`, and `factory-configurable-pipelines-v1.md`, whose Status lines read "acceptance recorded under DSC-GOV D-DSC-8"). It creates **no** implementation-slot authorization.

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these 6):**

1. **D-ARN-1** — the acceptance fact of `object-identity-v0.1.md` (OBJ-GOV).
2. **D-ARN-2** — the acceptance fact and single-amendment provenance of `lifecycle-v0.1.md` (LIFE-GOV).
3. **D-ARN-3** — the acceptance fact of `persistence-v0.1.md` (MONGO-GOV).
4. **D-ARN-4** — the acceptance fact of `persistence-impl-v0.1.md` (MONGO-IMPL), exercising no slot.
5. **D-ARN-5** — the acceptance fact of `provider-byok-foundations-v0.1.md` (PBF-GOV).
6. **D-ARN-6** — the bounded status-flip execution authorization.

**Does not decide (expressly):** any clause, choice, bound, or open item **inside** the five instruments (their content is untouched and is not re-read, re-ratified, or amended here); the exercise of any MONGO-IMPL slot (D-ARN-4 states the opposite); any other Status line (DIR-GOV and CITY-RET-GOV are already recorded; no further normalization exists to perform); anything about lifecycle implementation, persistence, providers, identity, scoring, or any runtime surface.

---

## 1. D-ARN-1 — `object-identity-v0.1.md` (OBJ-GOV) is accepted

**Decision.** OBJ-GOV was **accepted by the owner's merge of afi-governance PR #16 on 2026-07-14** (merge commit `4f490a5`). The terminology-fix commit `48e45f3` ("signalId 'assigned' not 'minted'") is **inside PR #16** — a pre-acceptance amendment on the proposing branch, per the ordinary pre-merge review convention. Current bytes are **byte-identical** to the accepted bytes (zero diff `4f490a5..HEAD`). Its Status-line conditional ("Until merged, it is a draft with no force") lapsed by its own terms at that merge. The accepted ledger already consumes it as law (DSC-GOV D-DSC-3(4) re-records its `:87` ScoredSignal-projection pin; the governed Evidence V3 schema cites D-OBJ-3 and D-OBJ-6 normatively). Status flip authorized per D-ARN-6.

**Scope-guard.** Acceptance-fact record only; no OBJ-GOV clause is re-decided, and its open interactions (e.g. the D-OBJ-3 cascade warnings at `:71`) remain exactly as written.

---

## 2. D-ARN-2 — `lifecycle-v0.1.md` (LIFE-GOV) is accepted, with one recorded amendment

**Decision.** LIFE-GOV was **accepted by the owner's merge of afi-governance PR #17 on 2026-07-14** (merge commit `a9fc673`); the scope-fix commit `0d69ffc` ("pre-persistence handoff applies to the canonical scored-signal evidence store only") is **inside PR #17** (pre-acceptance). It was subsequently amended **exactly once**, by the owner's merge of **PR #20 on 2026-07-16** (merge commit `1827031`, commit `f059277`): a one-line Evidence-basis re-pin adding `afi-docs @ 1f3f959` — a documentation amendment carrying its own owner acceptance, whose companion one-line evidence-pin change to `authority-districts-v0.1.md` in the same commit was later normalized to Accepted under D-DSC-8 without remark. Current bytes = accepted bytes + that single owner-merged amendment; **frozen henceforth** under the standing never-rewrite law. Status flip authorized per D-ARN-6.

**Scope-guard.** Acceptance-fact and amendment-provenance record only; no lifecycle semantics are touched, and no lifecycle implementation beyond what EV3-GOV already bounds is implied.

---

## 3. D-ARN-3 — `persistence-v0.1.md` (MONGO-GOV) is accepted

**Decision.** MONGO-GOV was **accepted by the owner's merge of afi-governance PR #18 on 2026-07-14** (merge commit `98a401b`). The `O-CHOICE-STORE` **Option-A selection** (commit `fda5953`) is **inside PR #18** — the owner accepted the text **with Option A already selected**; it was not a post-acceptance edit. Current bytes are byte-identical to the accepted bytes (zero diff). The accepted ledger already consumes it as law (EV3-GOV D-EV3-7: "afi-infra remains the sole canonical evidence writer (MONGO-GOV D-MONGO-3, unchanged)"; D-MONGO-4/D-MONGO-5 are cited as operative throughout). Status flip authorized per D-ARN-6.

**Scope-guard.** Acceptance-fact record only; no store, writer-boundary, index, or immutability rule is re-decided.

---

## 4. D-ARN-4 — `persistence-impl-v0.1.md` (MONGO-IMPL) is accepted; no slot is exercised

**Decision.** MONGO-IMPL was **accepted by the owner's merge of afi-governance PR #19 on 2026-07-14** (merge commit `2166823`); zero amendments since (byte-identical). Acceptance of the staged framework **exercises no slot**: every staged row keeps its own flip mechanics exactly as written, and **Slot 5 (`MONGO-MIGRATION`) remains unexercised and unauthorized** — as EV3-GOV D-EV3-7 already records (`persistence-impl-v0.1.md:20`). Status flip authorized per D-ARN-6.

**Scope-guard.** Acceptance-fact record only; this clause is not, and must never be cited as, the exercise of any MONGO-IMPL slot.

---

## 5. D-ARN-5 — `provider-byok-foundations-v0.1.md` (PBF-GOV) is accepted

**Decision.** PBF-GOV was **accepted by the owner's merge of afi-governance PR #23 on 2026-07-18** (merge commit `e7a57cf`); zero amendments since (byte-identical). Its own Status line already records owner authorization by commissioning instruction; the accepted ledger already builds on it (FLPR-GOV D-FLPR-5(5) consumes the D-PBF-10 composition-hash law; EV3-GOV extends the D-PBF-7 BYOK boundary to evidence). Status flip authorized per D-ARN-6.

**Scope-guard.** Acceptance-fact record only; no BYOK, adapter, or wave boundary is re-decided.

---

## 6. D-ARN-6 — Bounded status-flip execution

**Decision.** Upon acceptance of this decision, one or more direct-to-main commits are authorized editing **only** the `**Status:**` line (and the closing status footer, where one exists) of **exactly the five files named in D-ARN-1 … D-ARN-5**, replacing **only the Proposed-status fragments and the until-merged conditional sentences** with the standard Accepted formula citing the per-file facts recorded above and this decision (the D-DSC-8 / CONST-GOV / R1-GOV flip convention: `**Accepted** owner decision — accepted by merge of afi-governance PR #N on DATE (merge commit \`xxx\`); acceptance recorded under ARN-GOV D-ARN-n`). **The non-status remainder of each Status line and closing footer — the substantive designation, non-authorization, and owner-authorization sentences — is preserved verbatim**, exactly as the executed D-DSC-8 flips preserved it (see `authority-districts-v0.1.md:4` and its footer). **No other byte in any of the five files may change.** Post-flip, all five stand under the standing never-rewrite law identically to every other accepted decision.

**Scope-guard.** Exactly the named lines of exactly the five named files — plus this decision's own Status line and status footer, flipped under the standing acceptance-flip convention upon the owner's merge; any other edit is outside this authorization and must not merge. This authorization is consumed when all five named files have been flipped: each file's Status line and footer may be edited exactly once under it, and no flip may be re-executed.

---

## Explicit non-authorizations

This decision does **not** authorize: any content change to the five instruments beyond the named Status lines/footers; the exercise of any MONGO-IMPL slot or any other staged row anywhere; any change to any other decision file's Status text (other than this decision's own Status line and footer, flipped under the standing acceptance-flip convention upon the owner's merge); any code, schema, registry, KAT, runtime, persistence, deployment, or economic act; any rewrite of any accepted decision file (the flips edit only the lines the flip convention has always edited).

---

## Supersessions and interactions

Walked against every prior decision (twenty-two files). This decision supersedes **none of them**; interactions are:

- **`district-surface-consolidation-v0.1.md` (DSC-GOV)** — consumed: D-DSC-8 is the first acceptance-record normalization and the pattern this decision follows (including its treatment of the PR #20 evidence-pin amendment to AUTH-GOV). Unchanged.
- **`constitutional-architecture-v1.0.md` (CONST-GOV)** — consumed: it expressly left these stale Proposed labels as-is ("this decision touches no other Status line", `:180-:185`); that restraint is honored — this standalone decision now performs, with owner authorization, exactly what CONST-GOV declined to do in passing. Unchanged.
- **The five instruments themselves (OBJ-GOV, LIFE-GOV, MONGO-GOV, MONGO-IMPL, PBF-GOV)** — recorded, not superseded; edited only as D-ARN-6 authorizes; every clause inside them stands exactly as written.
- **`evidence-v3-provider-provenance-v0.1.md` (EV3-GOV)** — consumed: its normative citations of MONGO-GOV/MONGO-IMPL/PBF clauses now read onto formally labeled accepted instruments. Unchanged.
- **`five-lane-provider-runtime-v0.1.md` (FLPR-GOV)** — consumed (D-PBF-10 dependency, per D-ARN-5). Unchanged.
- **`authority-districts-v0.1.md` (AUTH-GOV)** — consumed: Part F honored (owner merge is the act; the flips execute a recorded owner decision, not agent self-ratification); its own PR #20 amendment history is cited as precedent in D-ARN-2. Unchanged.
- **`current-authority-reroot-and-golden-closure-v0.1.md` (R1-GOV)**, **`city-retirement-v0.1.md` (CITY-RET-GOV)**, **`scored-signal-direction-restoration-v0.1.md` (DIR-GOV)** — consumed as flip-convention precedents (`166c740`, `3d9d972`, `bab21f4`). Unchanged.
- **`district-2-m2-ratification-v0.1.md`**, **`factory-configurable-pipelines-v1.md`** — consumed (D-DSC-8 normalization peers). Unchanged.
- **`district-api-atlas-foundation-v0.1.md` (ATLAS-GOV)**, **`district-one-signal-evaluation-capability-v0.1.md` (D1CAP-GOV)**, **`research-institute-reference-services-v0.1.md` (INST-GOV)**, **`math-authority-v0.1.md`**, **`mint-formula-bt-86b-alignment-v0.1.md`**, **`uwr-profile-pin-v0.1.md`**, **`uwr-runtime-consumption-v0.1.md`** — untouched.

---

**Status footer:** **Accepted** owner decision — accepted by merge of afi-governance PR #33 on 2026-08-01 (merge commit `87b393d`, merged unedited). That merge constituted the acceptance-fact rulings D-ARN-1 … D-ARN-5 and authorized the D-ARN-6 flips.
