# AFI Five-Lane Provider Runtime Activation v0.1 (FLPR-GOV)

**Slot:** `AFI-GOV-FIVE-LANE-PROVIDER-RUNTIME-v0.1` (FLPR-GOV)
**Status:** **Proposed** owner decision — becomes authoritative **only** when the owner merges it into `afi-governance` main. **Owner authorization is recorded by the owner instruction that commissioned this decision** (the Mission B "Five-Lane Provider Runtime Activation and Forward-Only Consolidation v0.1" mission, 2026-07-18, issued by the owner), under the convention FCP-GOV, DSC-GOV, and D1CAP-GOV record. This is the **separate future owner authorization** that DSC-GOV D-DSC-6 and D1CAP-GOV expressly reserved for the five-lane provider-runtime cutover.
**Date:** 2026-07-18
**Type:** Scoped protocol-development governance decision (runtime activation + bounded contract amendment + forward-only consolidation mandate). It authorizes: making the PBF-GOV provider framework the sole live enrichment-execution seam for all five District One categories; the sentiment and aiMl adapters (plus a first-party candlestick pattern adapter and a keyless SEC-EDGAR news adapter); one bounded additive amendment to `afi.enrichment.pattern.v1`; and the deletion of every superseded classic category-execution path once byte-level scoring equivalence is proven. It changes **no** scored value, **no** analyst/UWR/decay law, **no** Evidence V2 shape or hashing law, **no** persistence, and deploys **nothing**.
**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` (canonical home `afi-config/codex/governance/droids/`), its `AFI_DROID_PIPEHEAD_ADDENDUM.v0.1.md` (unamended; its §13 non-production ceiling and §14 no-financial-truth rule are honored — nothing here is a production promotion), and `decisions/authority-districts-v0.1.md`. **Consumes (does not re-decide)** `provider-byok-foundations-v0.1.md` (PBF-GOV — the socket, the three non-secret objects, the adapter and credential law), `factory-configurable-pipelines-v1.md` (FCP-GOV — the five-category namespace, composition model, and D-FCP-5 registration mechanism), `district-surface-consolidation-v0.1.md` (DSC-GOV), `district-one-signal-evaluation-capability-v0.1.md` (D1CAP-GOV), and the decisions walked below. **Supersedes, prospectively and only as stated in D-FLPR-1,** the Mission-B wiring fences those decisions recorded. Where this decision conflicts with the Charter, the Charter wins.
**Evidence basis:** three read-only preflight/seam investigations (2026-07-18; 13 agents total: repository/authority/runtime preflight, provider inventory, per-lane shape-and-seam trace; **input, not authority**; load-bearing findings restated in §1), verified against clean `origin/main` trees at: `afi-governance` @ `9fd3407`, `afi-reactor` @ `a8a1762`, `afi-docs` @ `3f708ef`, `afi-protocol` @ `bcf227e`, `afi-config` @ `a1a1279`, `afi-core` @ `54ca87a`, `afi-tiny-brains` @ `8546ed3`.
**Ledger slot:** None existed — DSC-GOV D-DSC-6 named "the five-lane provider-runtime cutover" as "**Mission B** — a separate future owner authorization that must precede any such wiring" (`district-surface-consolidation-v0.1.md:136`); D1CAP-GOV D-D1CAP-7 recorded the per-lane state that cutover would change and restated "**Mission B remains separate and is not authorized by this decision**" (`district-one-signal-evaluation-capability-v0.1.md:149`). This decision fills exactly that reserved slot.

---

## 0. Scope — what this decision does and does not decide

**Decides (and only these 8):**

1. **D-FLPR-1** — Activation: the provider framework becomes the sole live enrichment-execution seam; the reserved wiring fences are lifted for this bounded activation.
2. **D-FLPR-2** — The new adapters (sentiment keyless + BYOK, aiMl first-party, candlestick pattern, SEC-EDGAR news) and their administrative registration.
3. **D-FLPR-3** — One bounded additive amendment to `afi.enrichment.pattern.v1` (the `candlestick` block).
4. **D-FLPR-4** — The explicit-selection law (`providerInstanceRef` mandatory per enabled lane; fail-closed resolution; no fallback; no env-var vendor selection).
5. **D-FLPR-5** — The invariance obligations (byte-equal scored values for the reference profile; Evidence V2 frozen; composition-hash movement is the governed D-PBF-10 consequence).
6. **D-FLPR-6** — The forward-only removal mandate (classic direct paths deleted on proof of equivalence; superseded governed registry records removed and the froggy 1.0.0 composition pin re-recorded; no shims, dual-runs, or archives).
7. **D-FLPR-7** — The committed all-five keyless/self-hosted reference profile and the BYOK credential posture.
8. **D-FLPR-8** — Non-goals and reservations (no Evidence V3, no Atlas, no analyst change, no ensembles, no marketplace, nothing deployed; tiny-brains remains a non-authority service).

**Does not decide:** any analyst, scorer, UWR, or decay change; any Evidence V2/V3 change; any persistence change; any District creation, scope change, or production promotion; any API Atlas surface; any MCP/RPC/SDK interface; any deployment or secret-manager provisioning; any Charter or Addendum amendment; any rewrite of accepted decision files.

## 1. Verified evidence restated (input, not authority)

1. **The socket is fully built and dormant end-to-end.** `createProviderBackedNode` (`afi-reactor/src/providers/providerBackedNode.ts:21`) is referenced nowhere in production wiring; `builtinPluginRegistry` binds only the direct nodes; `buildProviderRuntime()` is called argument-less at `src/config/runtimeComposition.ts:114` (empty record store, fail-closed `NoCredentialsResolver`); zero `providerInstanceRef` appears in any committed registry (grep over `afi-config/registries/` = 0).
2. **The registry loader reads only four dirs** — `registries/{analysis-plugins,pipelines,analyst-strategies,provider-bindings}` (`src/pipeline/registryLoader.ts:201-206`); `registries/providers/` exists in afi-config (two records) but nothing loads it.
3. **The scorer's complete enrichment read-set** (`afi-core/analysts/froggy.enrichment_adapter.ts:212-261`) is: `technical.emaDistancePct`, `technical.isInValueSweetSpot`, `technical.brokeEmaWithBody` (pinned `false` by the merge), `pattern.patternConfidence`, and `pattern.patternName` + `sentiment.tags` (only via the `liquiditySwept` substring hint). News content, `newsFeatures`, aiMl, and `sentiment.score` are never read. The live tag and pattern-name domains contain no sweep substring, so the sentiment hint is provably inert today.
4. **The governed pattern contract cannot carry the score-bearing pattern observation.** `afi.enrichment.pattern.v1` (`afi-config/schemas/enrichment/pattern/v1/enrichment-pattern.schema.json`) is closed at every level around `series/motifs/discords/changePoints/pivots`; the classic node's `patternName`/`patternConfidence` (constants 75/65/60 per detected name, `src/enrichment/patternRecognition.ts:61-73`) have no representation. A naive cutover to the kernel-only contract silently drops `view.pattern`, moving `triggerPatternQuality` from 2 to 0 — a live score change. This is the specific contract gap D-FLPR-3 closes.
5. **Evidence records embed enrichment content only through composition hashes.** The evidence record carries the scored projection plus `composition` (`manifestHash`, `analystConfigHash`, `pluginSetHash`, `executionSummaryHash`, `enrichmentHash`); no lens/news/sentiment/aiMl bytes appear in evidence (`src/services/graphScoringService.ts:165-192`, `src/evidence/reactorEvidenceRecord.ts:171-260`). D-PBF-10 already provides that composition "may commit to a non-secret ProviderInstance reference through its existing artifact hash where composition rules naturally include it" (`provider-byok-foundations-v0.1.md:131-135`).

## 2. D-FLPR-1 — Activation: the provider framework is the sole live enrichment-execution seam

The PBF-GOV provider framework (`afi-reactor/src/providers/` — statically registered adapters, `ProviderRuntime`, `providerBackedNode`, the three non-secret record objects, the injected least-privilege `SecretResolver`) **is activated as the one and only live enrichment-execution seam for all five District One categories** (`technical`, `pattern`, `sentiment`, `news`, `aiMl`). Wiring `providerInstanceRef` values into registered runtime manifests, binding the five category nodes to `providerBackedNode`, and loading the governed provider/provider-instance/credential-ref registries at boot are authorized.

The reserved fences are lifted, prospectively and only insofar as this bounded activation:

- DSC-GOV D-DSC-6 reserved this act: "The five-lane provider-runtime cutover is **Mission B** — a separate future owner authorization that must precede any such wiring" (`district-surface-consolidation-v0.1.md:136`); its non-authorizations kept "the FCP-GOV §12 wiring ban" alive (`:178`) and named "the five-lane provider-runtime cutover, any sentiment/aiMl provider adapter" as "separately owner-gated" (`:179`). **This decision is that owner authorization**; those fences are lifted for this activation only.
- D1CAP-GOV recorded "**Mission B remains separate and is not authorized by this decision**" (`district-one-signal-evaluation-capability-v0.1.md:149`, restated `:169`). This decision supplies the missing authorization; D-D1CAP-7's dormancy state record is superseded prospectively by the activation it anticipated (its text is not rewritten — it remains the honest pre-activation record).
- The FCP-GOV §12 wiring ban is lifted **only** for wiring the five category lanes to the provider framework under this decision's bounds; every other FCP-GOV bound (one executor, fail-closed registration, no eval, no silent fallback, no demo/mock production path) survives untouched.

**Scope-guards:** exactly one `GraphExecutor` remains (DSC-GOV D-DSC-1 unchanged); the provider runtime is not an executor; no second provider framework, no alternate registry, and no dynamic adapter loading may exist; category nodes remain vendor-neutral — no vendor name, endpoint, key, or vendor-specific parsing in any category node.

## 3. D-FLPR-2 — The new adapters and their registration

The following adapters are authorized as trusted, compiled-with-runtime, statically registered adapters under D-PBF-5, and their Provider/ProviderInstance/CredentialRef records as administrative D-FCP-5 / D-PBF-6 registry updates:

1. **Sentiment, keyless reference:** `afi-adapter-sentiment-cftc-cot` — CFTC Commitments of Traders (public-domain Socrata JSON; keyless; derived positioning/open-interest axes; weekly horizon).
2. **Sentiment, credentialed BYOK:** `afi-adapter-sentiment-coinalyze` — Coinalyze perp positioning (header-carried `api_key`; never in a URL; derived axes only).
3. **aiMl, first-party:** `afi-adapter-aiml-tiny-brains` — invokes the self-hosted Tiny Brains service and emits exactly one `afi.enrichment.aiml.v1` result (D-PBF-3 posture unchanged: no scoring authority, replaceable, internal orchestration subordinate).
4. **Pattern, first-party local:** `afi-adapter-pattern-candlestick` — the existing in-process candlestick/structure kernels behind the governed contract (the scoring-equivalence anchor).
5. **Pattern, first-party service:** the existing Tiny Brains pattern adapter re-identified honestly as `afi-adapter-pattern-tiny-brains` (it invokes the remote-topology self-hosted pattern service; "local" naming is retired with no governed-record blast radius since no pattern provider record existed).
6. **News, keyless reference:** `afi-adapter-news-sec-edgar` — SEC EDGAR (keyless US-government source; the required descriptive `User-Agent` is a non-secret identifier, not a credential).

The incumbent `afi-adapter-technical-local` and `afi-adapter-news-http` (NewsData BYOK) remain as-is. The same administrative D-FCP-5 registration authority covers the **successor composition artifacts** the activation requires: the five-lane pipeline manifest (`froggy-trend-pullback v1.1.0`, every lane node carrying its `providerInstanceRef`), the vendor-neutral lane-plugin manifests (`afi-analysis-{technical,pattern,sentiment,news,aiml} 2.0.0`), and the five-category merge manifest (`afi-merge-enriched-view 1.1.0`). **Scope-guards:** no arbitrary operator code, no operator-supplied endpoints beyond adapter policy (`invocation.endpointProfile` stays `"default"`-only), registry presence is not endorsement (D-PBF-6), derived-values-only posture for external sources, and adapters may not fabricate enrichment on failure — a failed lane degrades or aborts per declared manifest policy, recorded, never silently substituted.

## 4. D-FLPR-3 — Bounded additive amendment: `afi.enrichment.pattern.v1` `candlestick` block

`afi.enrichment.pattern.v1` gains **one optional, closed, vendor-neutral `candlestick` object**: required `patternName` (enum of the four current names: `bullish engulfing`, `bearish engulfing`, `pin bar`, `inside bar`) and `patternConfidence` (integer 0–100); optional closed `flags` (the four detection booleans), `structureBias` (`higher-highs`/`lower-lows`/`choppy`), and `trendPullbackConfirmed` (boolean). This closes the §1.4 gap so the score-bearing pattern observation can ride the governed contract. Authorized under FCP-GOV D-FCP-3's rule that contract shape changes beyond the original decision require new governance — this is that governance. **Scope-guards:** additive and optional only (every existing valid instance remains valid); no other governed contract shape changes under this decision; the block is an observation vocabulary, not a scoring instruction — scorer law is untouched.

## 5. D-FLPR-4 — Explicit-selection law

1. Every **enabled** category node in a registered runtime manifest MUST carry exactly one `providerInstanceRef` (identity + version only, per the governed pipeline schema).
2. Resolution is **fail-closed at composition and invocation**: an unknown or inactive ProviderInstance, a category mismatch, an adapter not in the static build-time registry, a provider/adapter identity mismatch, or a credential-scope violation refuses composition or fails the node — never a silent substitute.
3. **No silent provider fallback** of any kind: a lane's failure may only degrade or abort per its declared manifest policy; no re-invocation of a different provider, no re-call inside the join.
4. **No environment-variable vendor selection and no code-level default vendor**: selecting a different supported provider is a registry/record change (a new or different ProviderInstance reference), never a category-node code change and never an ambient environment switch. (Deployment-scoped, non-vendor operational parameters of a selected first-party adapter — e.g. the configured exchange feed of the local technical provider and the self-hosted Tiny Brains service address — remain deployment configuration under adapter policy, recorded honestly in documentation.)
5. Credential resolution stays least-privilege: one instance ⇒ at most one CredentialRef ⇒ exactly one secret, resolved only at invocation, header-carried, never in URLs, logs, errors, evidence, snapshots, or provider-result objects (D-PBF-7 unchanged).

## 6. D-FLPR-5 — Invariance obligations

For the committed reference profile, the activation MUST be proven scoring-invariant before any superseded path is deleted:

1. **Byte-equal scored values:** analyst score, UWR axes, UWR resolved source, decay parameters, scorer direction behavior, and the canonical ScoredSignal projection must equal the pre-activation runtime's values for identical canonical input.
2. **News and aiMl remain non-scoring**; `sentiment.score` remains unread; the sentiment/pattern-name hint mechanism (`liquiditySwept`) remains wired and its live inertness is preserved (the activated lanes' tag vocabularies contain no sweep substring).
3. **Evidence V2 stays frozen:** no provider, provider-instance, credential, or provider-provenance field may be added to the evidence record or its vendored schema; the freeze guard stays.
4. **Hashing law is untouched:** `afi.hash.v1`, all hashing KATs, the DSC-7 governed golden, and the UWR pins/anchors remain byte-identical.
5. **Composition-hash movement is governed, expected, and bounded:** wiring `providerInstanceRef` into the manifest changes `manifestHash` (and therefore `analystConfigHash`, `pluginSetHash`, `executionSummaryHash`) exactly as D-PBF-10 provides for; regenerated composition-bearing regression goldens must document field-level intentional diffs and must show the scored-value fields byte-unchanged.

## 7. D-FLPR-6 — Forward-only removal mandate

Upon proof of the D-FLPR-5 equivalences, the superseded classic execution paths MUST be deleted in the same program: the direct-call category nodes; the direct price-feed node wiring outside the framework; direct Coinalyze/NewsData/Tiny-Brains enrichment calls outside adapters; the post-merge aiMl augmentation client; the BTC-fixed pattern-regime fetch stack; fixed-symbol and fixed-timeframe fallbacks; superseded env-var gates; and every obsolete type, export, fixture, test, script, and dependency of those paths. **No compatibility shims, aliases, dual-run modes, fallback flags, archive directories, or commented-out copies may remain.** Ordinary git history and accepted governance records are the archive. Temporary equivalence-comparison scaffolding is permitted on the mission branch only and must be deleted before merge.

## 8. D-FLPR-7 — Reference profile and BYOK posture

1. One **committed, non-secret, all-five keyless/self-hosted reference profile** — the registered manifest's five `providerInstanceRef` values — is the canonical smoke surface: local technical kernels over a keyless exchange feed; the first-party candlestick pattern instance; CFTC-COT sentiment; SEC-EDGAR news; self-hosted Tiny Brains aiMl. It must be executable end-to-end with zero paid or personal credentials.
2. **BYOK instances** (NewsData news; Coinalyze sentiment) ride CredentialRef records with header-carried keys resolved at invocation by the injected least-privilege resolver. The current backend is the env-backed development resolver, **honestly non-production**; deployment-grade secret backends remain a later staging wave (PBF posture unchanged). Absent operator keys, credentialed lanes fail closed and deterministic transport-fixture proofs stand in for live-key proofs — a missing live-key proof is reported, never claimed.

## 9. D-FLPR-8 — Non-goals and reservations

This decision does **not** authorize: Evidence V3 or any provider-invocation provenance field (deferred; a future decision); any API Atlas schema, registry, UI, MCP catalog, endpoint, or agent-tool manifest (ATLAS-GOV reserved); any analyst, scorer, UWR, or decay change; making news or aiMl affect scoring; generic or cross-provider ensembles or provider-substitution fallback (D-PBF-2 unchanged); a provider marketplace or dynamic/operator-supplied adapters; any MCP/RPC/SDK interface; any deployment, production promotion, or secret-manager provisioning; any second executor or second provider framework; any Charter or Addendum amendment. Tiny Brains remains a replaceable, non-authority, first-party enrichment service (D-PBF-3 restated in full force).

## Explicit non-authorizations

This decision does **not** authorize: any change to scored values, analyst law, UWR law, decay law, Evidence V2 shape, hashing law, canonical goldens/KATs, or persistence; any District creation, deletion, scope change, numbering change, or production promotion; restoring any Pipehead code or naming; any dormant alternate registry; any rewrite of accepted decision files (all supersession here is prospective ledger fact); anything in D-FLPR-8.

---

## Supersessions and interactions (every prior decision walked)

- **`authority-districts-v0.1.md`** — untouched; no Part D row change (D1CAP-GOV's re-record stands); Part E gates and Part F agent limits honored — this decision is itself the owner-commissioned governance act those gates require before live wiring.
- **`district-surface-consolidation-v0.1.md` (DSC-GOV)** — consumed and completed, not disturbed: D-DSC-6 named `src/providers/` "the intended sole future category-execution seam" pending "a separate future owner authorization that must precede any such wiring" — this decision is that authorization; its D-DSC-1 sole-executor rule, deletion guardrails, and D2 relocation records remain in force; its Mission-B fences (`:136`, `:178-179`) are lifted prospectively for this activation only.
- **`district-one-signal-evaluation-capability-v0.1.md` (D1CAP-GOV)** — consumed: District One's identity, boundary, exclusions, and replacement rule are unchanged and are the frame this activation fills; D-D1CAP-5 expressly permits implementation evolution "through accepted authority" — this is that authority; D-D1CAP-7's provider-runtime dormancy record is superseded prospectively by the activation (the file is not rewritten; it remains the honest pre-activation record); the D-D1CAP-8 documentation anchors are honored by the paired docs amendment.
- **`factory-configurable-pipelines-v1.md` (FCP-GOV)** — consumed: the five-category namespace (D-FCP-1), graph composition model (D-FCP-2), delegated contract home and its new-governance rule for shape changes (D-FCP-3 — satisfied by D-FLPR-3), the administrative registration mechanism (D-FCP-5), and the no-demo/no-silent-fallback production rule (D-FCP-8) all remain in force; the §12 wiring ban is lifted only as stated in D-FLPR-1.
- **`provider-byok-foundations-v0.1.md` (PBF-GOV)** — consumed wholesale and activated: the five open lanes (D-PBF-1), one-result-per-lane and no-ensembles (D-PBF-2), Tiny Brains posture (D-PBF-3), the three non-secret objects (D-PBF-4), static adapter law (D-PBF-5), administrative registration (D-PBF-6), BYOK credential law (D-PBF-7), canonical output validation before scoring (D-PBF-8), deterministic non-agentic runtime (D-PBF-9), and the Evidence-V2 freeze with hash-committed instance references (D-PBF-10) are the operating law of the activated seam; nothing in PBF-GOV is amended.
- **`district-2-m2-ratification-v0.1.md`** — untouched; District Two evidence/provenance law is unchanged; composition-hash movement under D-FLPR-5(5) is the D-PBF-10 mechanism District Two already ratified.
- **`object-identity-v0.1.md`** — untouched; USS v1.1 and the ScoredSignal projection identities are consumed by the invariance obligations.
- **`lifecycle-v0.1.md`** — untouched; the implemented lifecycle still halts at SCORED.
- **`persistence-v0.1.md` / `persistence-impl-v0.1.md`** — untouched; the evidence store law and its sole writer are unchanged.
- **`uwr-profile-pin-v0.1.md` / `uwr-runtime-consumption-v0.1.md`** — untouched; the scorer/UWR seam remains invoke-never-reimplement with all pins, bans, RC-rules, and golden conditions in force; D-FLPR-5 makes their preservation an explicit gate of this activation.
- **`math-authority-v0.1.md`** — untouched; kernels stay in afi-core/afi-math; adapters normalize, they do not score.
- **`mint-formula-bt-86b-alignment-v0.1.md`** — untouched; no economic surface.
- **`research-institute-reference-services-v0.1.md` (INST-GOV)** — untouched; ingress operation and boundary classifications are unchanged; the activated lanes sit strictly below the ingress → evaluation seam INST-GOV describes.
- **Reserved ATLAS-GOV / CHAIN-GOV** — honored and untouched; no discoverability or chain surface is created here.

---

**Proposed owner decision. Authoritative upon owner merge.**
