# DLC-GOV Decay-KAT Status-Marker Amendment v0.1 (DKS-GOV)

**Slot:** `AFI-GOV-DLC-DECAY-KAT-STATUS-AMENDMENT-v0.1` (DKS-GOV)

**Status:** **Proposed** for owner approval — this touch-scoped amendment becomes authoritative only when the owner merges it. Drafting is within the DLC-APPLY slot authorization (founder instructions of 2026-08-24, recorded in DLC-GOV's Status line); **acceptance is expressly NOT** — DLC-GOV §5 withholds "any uwr-profile v0 schema or registered-profile edit" from every slot, so lifting it in one bounded respect requires this owner-merged act (GPR-GOV D-GPR-3(2): stop and upgrade, never read around express text).

**Date:** 2026-08-24

**Type:** Touch-scoped amendment to `decay-lifecycle-v0.1.md` (DLC-GOV) in exactly one bounded respect. **Tier S** under GPR-GOV D-GPR-2: it moves no scored value, no golden, no hash law, no vector byte, and no expected value; it authorizes only the mechanical consequence of a status marker DLC-GOV itself orders flipped.

**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` and `decisions/authority-districts-v0.1.md`. Amends DLC-GOV §5 in the single respect below; every other DLC-GOV clause, non-authorization, and gate is untouched.

---

## 1. The collision this resolves

DLC-GOV's `DLC-APPLY` gate orders, inside the slot, that the governed decay KAT's implementation marker flips: *"that KAT's `x-afiStatus: draft-non-implementation` marker flips to implemented inside the slot — the only KAT byte the slot may move."* The rest of DLC-APPLY shipped 2026-08-24 (afi-core PR #34, afi-reactor PR #85 — the production derivation reproduces all 32 vectors bit-exactly); the flip is the one clause still standing, because it is **forced through a surface DLC-GOV §5 expressly bars**:

`afi-config/schemas/uwr-profile/v0/uwr-decay-kat.schema.json` declares the KAT instance's marker as a **required const** — `properties.x-afiStatus = { "const": "draft-non-implementation" }` (:36-38) — and `tests/uwr-profile-schema-validation.test.ts` validates the KAT against that schema. Flipping the KAT's marker therefore forces one line of that schema to move in lockstep, and DLC-GOV §5 withholds "any uwr-profile v0 schema or registered-profile edit" from every slot. The authorized act and its forced mechanical consequence collide; a PR-body reading cannot lift express decision text (the DKA-GOV precedent, `dem-hashing-kat-anchor-amendment-v0.1.md`).

## 2. D-DKS-1 — the amendment (exactly one clause)

**Decision.** DLC-GOV §5 is amended in this single bounded respect: when the `DLC-APPLY` slot flips `kats/uwr-profile/v0/apply-time-decay.kat.json`'s `x-afiStatus` from `draft-non-implementation` to **`implemented`**, the following move **in lockstep, in the same PR, and only then**:

1. `schemas/uwr-profile/v0/uwr-decay-kat.schema.json` `properties.x-afiStatus.const` — `draft-non-implementation` → `implemented` (the one schema line the flip forces);
2. the corresponding pinned expectation in `tests/uwr-profile-schema-validation.test.ts`, if any names the instance marker;
3. afi-core's byte-mirror of the KAT (`src/decay/__tests__/kats/apply-time-decay.kat.json`) and its vendoring pins (`applyTimeDecay.kat.test.ts`: the pinned sha256, the `x-afiStatus` expectation, and the vendoring change-log) — the re-vendor its own DRIFT_MESSAGE requires scoped authorization for; this clause, together with DLC-GOV's gate sentence, is that authorization.

**Scope-guard.** No vector byte, no expected value, no template value, no exactness rule, no engine field, no hash law, and no other schema line moves. The schema file's **own** top-level `x-afiStatus` (:7) stays `draft-non-implementation` — the uwr-profile v0 family's honesty overhaul (including its now-stale "UP-8 remains OPEN" prose, superseded by DLC-GOV's closure of UP-8) is expressly NOT taken here; it belongs to the successor uwr-profile schema filing DLC-GOV D-DLC-2 directs. This amendment authorizes the marker flip's forced consequences and nothing else; the four hashing-law KAT vectors and every other KAT remain untouched by every slot.

## 3. Supersessions and interactions (touch-scoped, GPR-GOV D-GPR-1)

- **DLC-GOV** — amended in the single respect above; §5's every other withholding, every slot gate, and every clause are **unchanged**.
- **uwr-profile-pin (UP-GOV)** — untouched; UP-12's marker discipline is honored (the marker moves to record reality: the KAT is now executed by production code).
- **Every other accepted decision on `decisions/INDEX.md` — untouched.**

---

**Status footer:** **Proposed** — becomes authoritative on owner merge; the owner's merge is the acceptance act. On acceptance, record it with the standing ARN-GOV acceptance-record convention and regenerate `decisions/INDEX.md` (**38th** accepted decision — verify at flip time). This amendment authorizes exactly the lockstep flip PR described in D-DKS-1, which completes the DLC-APPLY gate; it authorizes nothing else.
