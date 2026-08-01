# AFI City Retirement v0.1 (CITY-RET-GOV)

**Slot:** `AFI-GOV-CITY-RETIREMENT-v0.1` (CITY-RET-GOV)
**Status:** **Accepted** owner decision — accepted by merge of afi-governance PR #31 on 2026-07-30 (merge commit `6ea2708`, merged unedited). Owner authorization was recorded by the owner instruction that commissioned this decision (founder instruction of 2026-07-29: full retirement and deletion of the AFI City public ecosystem map and its repository, explicitly including the inherited GITC/USDC payment layer).
**Date:** 2026-07-29
**Type:** Scoped protocol-development governance decision (retirement record / de-ratification of a reference document / repository-existence fact). Documentation and governance-ledger only; it authorizes **no** schema, route, runtime, deployment, infrastructure, credential, or economic act, and decides nothing beyond its five clauses.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` and `decisions/authority-districts-v0.1.md`. For the District-framing, non-production, and no-financial-truth invariants it defers to `decisions/current-authority-reroot-and-golden-closure-v0.1.md` (R1-GOV). **Consumes (does not re-decide)** all twenty prior accepted decisions. **Supersedes** the D-CONST-2 ratification of the AFI City Ontology Specification v1.0 **only as stated in D-CITY-2 and nowhere else**. **Honors, and does not touch,** the reserved `ATLAS-GOV` (API/endpoint surface) and `CHAIN-GOV` (rewards / mint / settlement / on-chain / economic activation) scopes. Where this decision conflicts with the Charter, the Charter wins; where it conflicts with any accepted decision, that decision wins except on the single point D-CITY-2 expressly supersedes.
**Evidence basis:** Findings are restated inline because the workspace `reports/` area is unversioned and is never authority. Verified on 2026-07-29: the repository `AFI-Protocol/afi-web` has been deleted (GitHub API returns no such repository); it was a public fork of `srizzon/git-city` at HEAD `64ffdfa`, with 0 stars, 0 forks, 0 deployments, 0 GitHub Pages, 0 Actions runs, and no domain pointing at it — no AFI City surface was ever publicly deployed. Zero machine-readable coupling to afi-web existed anywhere in the organization: no package dependency, git-URL pin, path reference, submodule, tsconfig reference, or CI checkout in any other repository, so the deletion breaks no build, test, or workflow. Repository pins at the time of this decision: afi-governance @ `bc85fba`, afi-config @ `7423566`, afi-core @ `24513f4`, afi-reactor @ `f53f171`, afi-infra @ `6417eae`, afi-gateway @ `a8038e2`, afi-docs @ `a572035`, afi-math @ `5247e41`, afi-mint @ `eba0d93`, afi-token @ `0d3de3c`, afi-econ @ `0aa207c`, afi-tiny-brains @ `712e2ff`, afi-benchkit @ `76cde01`, afi-protocol @ `01d8728`, afi-artifacts @ `ba12307`, afi-xerc20 @ `b34ba57`, afi-factory @ `6f025d1`.
**Ledger slot:** None existed — no prior decision records the retirement of a public surface or the de-ratification of a reference document. This decision opens the surface-retirement slot. It creates **no** implementation-slot authorization.

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these five):**
1. the **retirement fact** — AFI City and its repository no longer exist (D-CITY-1);
2. the **de-ratification** of the AFI City Ontology Specification v1.0 as canonical reference doctrine (D-CITY-2);
3. that the **`afi-web @ 64ffdfa` evidence pin** in CONST-GOV is a permanently unresolvable historical citation, and that the accepted ledger is **not** rewritten to remove it (D-CITY-3);
4. that the **future AFI Protocol City** (the ATLAS-GOV Atlas-truth projection) is a **distinct, untouched, still-unbuilt** concept (D-CITY-4);
5. the **naming-register consequence** — "Machine" remains the public register label with no public renderer today (D-CITY-5).

**Does NOT decide:** any replacement public surface, its design, technology, hosting, or timing; any Atlas, schema, contract, or registry change; any endpoint or route (**ATLAS-GOV**, reserved); anything economic (**CHAIN-GOV**, reserved); the status of any other document or repository; and any cleanup edit to any file not named in D-CITY-2.

**Nature of the act.** This decision records a retirement that has already occurred by founder instruction and corrects the governance record prospectively. It conveys no implementation authorization.

---

## 1. D-CITY-1 — the retirement fact

**Decision.** The **AFI City** public ecosystem map and its repository `AFI-Protocol/afi-web` are **retired and deleted** by founder instruction of 2026-07-29. AFI has **no public ecosystem map surface** as of this decision. The deletion included the repository, its local checkout, its documentation mirrors, and the inherited GITC/USDC payment layer that the repository carried — the founder expressly authorized the payment layer's destruction, superseding the informal 2026-07-28 keep-ruling recorded outside the ledger.

**Scope-guard.** Records a fact about surface existence only. It authorizes no replacement, mandates no timeline, and says nothing about whether AFI should have a public map in future.

---

## 2. D-CITY-2 — de-ratification of the AFI City Ontology Specification v1.0

**Decision.** The **AFI City Ontology Specification v1.0**, ratified as canonical reference doctrine by CONST-GOV **D-CONST-2** (`decisions/constitutional-architecture-v1.0.md` §2 and its documentation-ledger table), is **de-ratified and retired**. It describes a surface that no longer exists. Its document has been deleted from the unversioned workspace `reports/` area. No successor City ontology is ratified, and none is owed.

**Prospective supersession.** Per the standing supersession law, the accepted CONST-GOV file is **NOT rewritten**. Its D-CONST-2 clause and documentation-ledger row remain byte-identical on the permanent record; this clause supersedes them **prospectively as a governance-ledger fact**, and only as to the City ontology document. The other two documents ratified by D-CONST-2 — *AFI Constitutional Architecture v1.0* and *AFI Component Classification Registry v1.0* — remain ratified and are unaffected, save for the removal of their afi-web rows and City cross-references as a consequence of D-CITY-1.

**Scope-guard.** De-ratifies exactly one document. It re-decides nothing else in CONST-GOV — the three-layer model, the terminology register, the PoI/PoInsight classification (D-CONST-5), the Registered Application layer (D-CONST-6), and the component-placement framework all stand unchanged.

---

## 3. D-CITY-3 — the CONST-GOV evidence pin is historical, and the ledger is not rewritten

**Decision.** CONST-GOV's evidence basis pins `afi-web @ 64ffdfa`. That commit is **no longer resolvable within the organization** because the repository is deleted. This is recorded as a **permanently unresolvable historical citation**. The accepted decision file is **not edited**; the byte-freeze on the accepted ledger holds absolutely. CONST-GOV's own text already provides that its `reports/` inputs were "input, not authority" and that "every framing this decision relies on is stated inline in its clauses" — so no clause of CONST-GOV depends on the pinned tree being fetchable, and its correctness is unaffected.

**Scope-guard.** Records a citation-resolvability fact. It authorizes no edit to any accepted decision, and it does not weaken, qualify, or reopen any CONST-GOV clause.

---

## 4. D-CITY-4 — the future AFI Protocol City is untouched

**Decision.** The **AFI Protocol City** described by ATLAS-GOV (`decisions/district-api-atlas-foundation-v0.1.md`, D-ATLAS-11 / D-ATLAS-12 / D-ATLAS-13 §14) — a future *visualization and navigation projection of Atlas truth* — is a **different concept** from the retired AFI City ecosystem map and is **entirely unaffected** by this decision. It remains **not started**, it remains a projection that "creates no architectural authority," and D-ATLAS-12's rule that discarded implementations must never appear as landmarks continues to apply to it. The documentation anchor stating the Protocol City is "not started" remains **literally true** and must not be edited.

**Scope-guard.** Confirms non-interference. It neither authorizes, schedules, designs, nor forbids the future Protocol City, and it changes no ATLAS-GOV clause.

---

## 5. D-CITY-5 — the public naming register survives its renderer

**Decision.** CONST-GOV fixes the three-register naming doctrine in which **"Machine"** is the *public* label of the scoring surface (against "the Reactor" = reference implementation, "AFI Signal Runtime" = hosted instance). That register **stands unchanged**. The retirement of AFI City removes the surface that *rendered* the public register; it does not retire the register itself. "Machine", "Factory", "Vault", and "Mint" remain the public-register labels of their respective surfaces, available to any future public surface, and carry exactly the authority their underlying protocol entities have — no more.

**Scope-guard.** Preserves existing naming law. It renames nothing, creates no new label, and confers no authority on any name.

---

## Explicit non-authorizations

This decision authorizes **no** code, schema, contract, registry, route, endpoint, runtime, deployment, infrastructure, credential, funding, or economic act. It does **not** authorize a replacement public surface. It does **not** authorize any edit to any accepted decision file. It does **not** touch the reserved ATLAS-GOV or CHAIN-GOV domains. It registers no participant, provider, application, or binding.

---

## Supersessions and interactions

Walked against every prior accepted decision:

- **`constitutional-architecture-v1.0.md` (CONST-GOV)** — **partially superseded, prospectively and narrowly**: the D-CONST-2 ratification of the AFI City Ontology Specification v1.0 only (D-CITY-2); its evidence pin recorded as historical (D-CITY-3); its naming register expressly preserved (D-CITY-5). All other clauses consumed unchanged. File not rewritten.
- **`district-api-atlas-foundation-v0.1.md` (ATLAS-GOV)** — consumed unchanged; D-ATLAS-11/12/13 expressly unaffected (D-CITY-4). Its reserved ATLAS-GOV scope is honored, not touched.
- **`current-authority-reroot-and-golden-closure-v0.1.md` (R1-GOV)** — consumed; this decision follows its forward-only pattern (retire the instrument, record the fact prospectively, never rewrite the ledger).
- **`authority-districts-v0.1.md`** — consumed; no District material-scope change occurs (AFI City owned no District; economic machinery has no owning District).
- **`research-institute-reference-services-v0.1.md` (INST-GOV)** — consumed; AFI City was Institute infrastructure filling no protocol slot, so its removal retires no protocol role and leaves no slot unfilled.
- **`mint-formula-bt-86b-alignment-v0.1.md`, `math-authority-v0.1.md`** — consumed unchanged; the deleted GITC/USDC layer was inherited third-party payment code, never an AFI economic mechanism, and no AFI economic rule referenced it.
- **`evidence-v3-provider-provenance-v0.1.md` (EV3-GOV), `persistence-v0.1.md` (MONGO-GOV), `persistence-impl-v0.1.md`, `lifecycle-v0.1.md` (LIFE-GOV), `object-identity-v0.1.md` (OBJ-GOV), `uwr-profile-pin-v0.1.md`, `uwr-runtime-consumption-v0.1.md`, `factory-configurable-pipelines-v1.md` (FCP-GOV), `five-lane-provider-runtime-v0.1.md`, `provider-byok-foundations-v0.1.md`, `district-one-signal-evaluation-capability-v0.1.md`, `district-2-m2-ratification-v0.1.md`, `district-surface-consolidation-v0.1.md`** — consumed unchanged; none referenced afi-web, and the live pipeline had zero coupling to it.

**Ledger effect:** this is the twenty-first accepted decision once merged. The retired City ontology document is not replaced.

---

**Status footer:** **Accepted** owner decision — accepted by merge of afi-governance PR #31 on 2026-07-30 (merge commit `6ea2708`, merged unedited).
