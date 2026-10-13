# Almost Stacked Proof

**Objective:** settle the **intended critical-form Almost Stacked Hypothesis (ASH*)** of Tamás Csernák and Lajos Soukup, by an unconditional universal proof or a finite, fully certified counterexample (stacking and clearing separately); retain the verified counterexamples to the distinct *printed* formulation. The source is [The Almost Stacked Hypothesis: A Conjectural Analogue of Sjöstrand's Cover Pebbling Theorem](https://arxiv.org/abs/2610.09650) (October 2026), building on [Stacking and clearing in graph pebbling](https://arxiv.org/abs/2604.22341).

This is a research programme. **Status after S003:**
- The hypothesis **as printed** (October Hypothesis 3.2 = April Hypothesis 9.1, a pointwise "least t" equality) is false for both stacking and clearing. Certified finite counterexamples: P4 at t=12, and the bull graph at t=12. Lean formalisation and an independent cold audit are still pending.
- The authors' own computations test a *critical (monotone)* form, ASH\*. ASH\* remains **open**: it is proved for trees and computed true on every connected graph with at most 7 vertices whose threshold was found, and on every connected 8-vertex graph whose threshold is at most 26.
- **Author contact:** John reports having sent the correspondence prepared on 12 October. On 13 October 2026, Tamás Csernák replied (cc Lajos Soukup), explicitly confirming **ASH* is the intended conjecture** and that the stronger printed wording is false. He described the upward bad-configuration recurrence and reported successful calculations for all graphs up to seven vertices; this is author testimony, not a published correction or independent replication of the remaining higher-threshold cases. The complete private reply is not mirrored in this public repo; see the [attributed correspondence summary](outreach/2026-10-csernak-soukup/2026-10-13_AUTHOR_REPLY.md). The independent cold audit, Lean, Palomar and arXiv stages are still pending.
- See [research/S003_AS_GAP_AND_ATTACKS.md](research/S003_AS_GAP_AND_ATTACKS.md) and the [ASH* direct attack brief](research/ASHSTAR_ATTACK_BRIEF.md). **S004 remains future, unexecuted**; the 2026-10-13 correspondence update was not a research session.

## Essential distinction: our already proved tree theorem

The separate [TreeStack research repository](https://github.com/jfairfaxball-348/TreeStack-Structural-Certificates-for-Stacking-on-Trees) gives an independently developed and Lean-formalised proof that `stack(T) = estim(T)` for finite trees with at least two vertices, as defined in that work. Its paper is [arXiv:2609.31811](https://arxiv.org/abs/2609.31811), publicly posted before the October ASH preprint, and its recorded Palomar entry is [PALOMAR-2026-09-25-000010](https://palomar-registry.org/entry.html?id=PALOMAR-2026-09-25-000010&version=1). The October preprint's abstract calls the corresponding tree equality conjectural and proves it under ASH. **The tree equality is not itself a proof of universal ASH, and must not be sold as a new result here.** Independently compare the precise definitions, one-vertex convention, estimator, revisions and dependencies before asserting theorem identity in a manuscript. See [research/TREESTACK_BRIDGE.md](research/TREESTACK_BRIDGE.md).

## Problem outline

A pebbling move removes two pebbles at a vertex and adds one at an adjacent vertex. A configuration is *almost stacked* when at most one vertex carries more than one pebble. In the source's setting, ASH proposes that testing almost stacked configurations suffices to determine the universal **stacking** threshold for connected graphs and the **clearing** threshold for connected non-bipartite graphs. The exact original (now inspected in S003) and intended critical-form quantifiers are distinguished in [research/ASH_SPEC.md](research/ASH_SPEC.md); recheck the current primary paper version in S004. Read [research/PROBLEM_SPEC.md](research/PROBLEM_SPEC.md).

## Milestone pipeline

| Stage | Exit gate |
|---|---|
| 0. Bootstrap | Research governance, provenance, source and claim registers |
| 1. Exact problem and proof/counterexample research | Definitive source transcription, proof or reproducible candidate and fully specified gaps |
| 2. First prior-art and novelty check | Closest literature and equivalent formulations checked before expensive formalisation |
| 3. Lean formalisation | Pinned toolchain; no admitted gaps; independent kernel/checker review |
| 4. Final comprehensive novelty audit | Re-run direct and adjacent novelty search against the **final exact theorem and proof** |
| 5. Palomar | Owner-authorised submission, exact frozen commit, successful independent mechanical preflight and registry record |
| 6. Paper / arXiv | Complete standalone manuscript with accurate citations, reproducibility and arXiv release after owner authorisation |

A negative result or counterexample may require adapting the formal proof package; do not force a proof-shaped manuscript onto a counterexample.

## Quick start

1. Read `AGENTS.md`, `authoritative/START_HERE.md`, `authoritative/STATE.json` and `docs/SESSION_PROTOCOL.md`.
2. Read source and claim catalogues, `research/PROBLEM_SPEC.md` and the TreeStack bridge.
3. Execute **only** the separately owner-invoked session described in [authoritative/NEXT_SESSION_PROMPT.md](authoritative/NEXT_SESSION_PROMPT.md).
4. Keep independent proof, computation, source-stated facts and Lean results separate. Do not mistake absent hosted CI for passing tests.

Borrowed methodology and staged assurance are inspired by [Davenport-Counterexample-Hunt](https://github.com/jfairfaxball-348/Davenport-Counterexample-Hunt), but the mathematical target and release gates belong to this repository.
