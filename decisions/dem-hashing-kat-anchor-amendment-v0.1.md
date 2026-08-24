# DEM-GOV Hashing-KAT Example-Anchor Amendment v0.1 (DKA-GOV)

**Slot:** `AFI-GOV-DEM-HASHING-KAT-ANCHOR-AMENDMENT-v0.1` (DKA-GOV)

**Status:** **Proposed** for owner approval — this touch-scoped amendment becomes authoritative only when the owner merges it. Drafting is within the DEM-BIND slot authorization (founder instruction of 2026-08-22, *"Authorized."*); **acceptance is expressly NOT** — DEM-GOV §8 (:177) withholds any hashing-KAT change from every implementation slot, so lifting it in a bounded respect requires this owner-merged act (GPR-GOV D-GPR-3(2): stop and upgrade, never read around express text).

**Date:** 2026-08-23

**Type:** Touch-scoped amendment to `declarative-enrichment-mapping-v0.1.md` (DEM-GOV) in exactly one bounded respect. **Tier S** under GPR-GOV D-GPR-2 as amended by CFG-GOV D-CFG-5(2): it moves no scored value, no golden, no hash **law**, no schema shape, and no hash-law KAT byte; it authorizes only the mechanical consequence of a governed example evolving.

**Governance:** Subordinate to `AFI_DROID_CHARTER.v0.1.md` and `decisions/authority-districts-v0.1.md`. Amends DEM-GOV §8 (:177) and clarifies D-DEM-6(3) in the single respect below; every other DEM-GOV clause, non-authorization, and gate is untouched.

---

## 1. The collision this resolves

The governed hashing KAT (`afi-config/kats/hashing/v1/canonical-json-hashing.kat.json`) contains two classes of vector, proven by `tests/canonical-hashing-kat.test.ts`:

1. **Hash-LAW vectors** (`key-sorting-nested`, `unicode-and-escapes`, `number-forms`, `exclusion-is-top-level-only`): synthetic inputs pinning the canonicalization discipline itself. These define `afi.hash.v1` behavior.
2. **Example-ANCHOR vectors** (`pipeline-manifest-excludes`, `analyst-config-excludes`): their `input` is deep-equal-pinned **to the live governed example documents** (the suite's own describe title: *"the KATs are the REAL hashes the examples pin"*). They prove the examples and the KAT agree — they do not define the law.

DEM-BIND's final bounded step (D-DEM-2(5)(e)) declares `mappingRef` required, which forces the analyst-strategy-config **example** to gain `mappingRef` — and therefore forces the `analyst-config-excludes` anchor vector's `input` and `expectedSha256` to move with it. DEM-GOV §8 (:177) expressly withholds "any change to any hashing KAT" from every slot, and D-DEM-6(3) requires "every hashing KAT byte-identical". Read literally, the required-field step DEM-GOV itself mandates is unexecutable. This amendment resolves that internal contradiction the narrow way.

## 2. D-DKA-1 — the amendment (exactly one clause)

**Decision.** DEM-GOV §8 (:177) and D-DEM-6(3) are amended in this single bounded respect: the hashing KAT's **example-anchor vectors** (`pipeline-manifest-excludes`, `analyst-config-excludes` — exactly these two, enumerated, non-extensible) **track governed example evolution**: when an owner-authorized act changes a governed example document those vectors pin, the vectors' `input` and `expectedSha256` are updated to the evolved example **in the same PR**, with the change named in that PR's itemization. The four **hash-law vectors** remain byte-frozen exactly as DEM-GOV holds them; any change to them, to the vector set's membership, to `canonical-json-hashing.v1.md`, or to either canonicalization discipline remains expressly non-authorized by every implementation slot.

**Scope-guard.** This amendment changes no hash law, no discipline text, no exclusion list, no domain tag, and no scored value. It does not authorize the example changes themselves — those carry their own authorization (for DEM-BIND step (e), D-DEM-2(3)/(5)(e)). It creates no discretion: an anchor vector may move only in lockstep with the governed example it pins, and the KAT suite's deep-equality assertions make any other movement a red test.

## 3. Supersessions and interactions (touch-scoped, GPR-GOV D-GPR-1)

- **DEM-GOV** — amended in the single respect above; §8's every other withholding, every slot gate, and D-DEM-6's every other requirement are **unchanged**.
- **Every other accepted decision** — untouched.

---

**Status footer:** **Proposed** — becomes authoritative on owner merge; the owner's merge is the acceptance act. On acceptance, record it with the standing acceptance-record convention and regenerate `decisions/INDEX.md`. This amendment authorizes **zero** code PRs by itself; DEM-BIND step (e1) proceeds under its own slot authorization once this is accepted.
