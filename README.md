# Almost Stacked Proof

**Objective:** settle the **intended critical-form Almost Stacked Hypothesis (ASH*)** of Tamás Csernák and Lajos Soukup, by an unconditional universal proof or a finite, fully certified counterexample (stacking and clearing separately); retain the verified counterexamples to the distinct *printed* formulation. The source is [The Almost Stacked Hypothesis: A Conjectural Analogue of Sjöstrand's Cover Pebbling Theorem](https://arxiv.org/abs/2610.09650) (October 2026), building on [Stacking and clearing in graph pebbling](https://arxiv.org/abs/2604.22341).

This is a research programme. **Historical status after S003 (superseded by S004 below):**
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

## Historical result after S004

**Universal intended ASH* remains open for both stacking and clearing.** Printed-form counterexamples are independently cold-audited (mathematics PASS; Lean pending).

A symbolic theorem now produces an almost-stacked non-stackable state of mass3k for every independent set of size k>=2, even with edges outside the independent set. This proves ASH* for all complete multipartite graphs using the authors' exact threshold formulas, and more generally at g=n+1 or3alpha+1. This is a family result; novelty has not been audited.

The complete order-seven atlas now has independently computed thresholds: 853/853 stack,809/809 clear. Selected new values include C9 37/46 and triangle-tail stack128. C10 only through t16 and triangle-tail clear>140 are cutoff cases with no ASH* verdict.

See [S004 proof report](research/S004_ASHSTAR_ATTACK.md), [cold audit](sessions/S004/AUDIT.md), [closeout](sessions/S004/CLOSEOUT.md) and the strictly [current next-session prompt](authoritative/NEXT_SESSION_PROMPT.md). No Lean, Palomar or arXiv action.

## Current result after S005

**Universal ASH* remains open**, separately stacking and clearing. Exact clearing of a pure pile is classified by its residue modulo3 and the rooted odd-walk height; the source lower bound and reduction operation are credited, with no novelty claim. Global square/extremum selection remains unproved.

C10 stack63 and triangle with five-edge tail clear190 now have complete independently replayed layers. All finite counts and explicit remaining cutoffs are in [S005 audit](sessions/S005/AUDIT.md). See the [proof report](research/S005_ASHSTAR_EXTREMA_AND_ROOTED_CLEARING.md) and [closeout](sessions/S005/CLOSEOUT.md). [S006](authoritative/NEXT_SESSION_PROMPT.md) is future/unexecuted. No Lean, registration, submission or new contact.

## Current result after S006

Universal ASH* remains OPEN separately for stacking and clearing. Exact rooted pure-pile and arbitrary fixed-buffer conductors are proved via binary clearing trees and nonempty stacking forests; positive-source residues and zero-source inputs are distinct. A constructive finite rooted bound and exact AS-ray last-loser formula do not prove the missing general-versus-binary extremal comparison. Scalar leaf attachment is refuted in both directions by complete legal closures/traces.

Independent grammar/certificate checkers and full distinct forward/reverse rooted masks validate the registered finite scopes; no new threshold frontier or infinite family upper was claimed. Read [S006 report](research/S006_ROOTED_CONDUCTORS_AND_EXTREMAL_GAP.md), [audit](sessions/S006/AUDIT.md), and [closeout](sessions/S006/CLOSEOUT.md). S007 is strictly FUTURE/UNEXECUTED. Printed-form PASS remains separate; no novelty, Lean, contact or submission promotion.

## Current S011 authority - 2026-10-15

Earlier current/future sections are historical. Last S011, next S012 strictly FUTURE/UNEXECUTED. Universal critical STACK/CLEAR OPEN, printed PASS separate. S01044-52 cold challenge and25 inherited check-only replays PASS at stated scopes with old bytes/cutoffs retained. New53 nonempty terminal-vector forest,54 three-output used-label re-root/edge exposure,55 stackable CLEAR deletion/triangle-free history and gap>=2 heavy-site restriction,56 bipartite common CLEAR root obstruction,57 donor1/2 exact terminal transport,58 CLEAR/TWO root typing are programme-proved at explicit scopes. They do NOT provide global AS selection. Actual C5 odd-cycle3-witness can still fail clearing; abstract typed/self-root families can lack common STACK roots and are NOT actual configuration counterexamples. Three registered dual-validator campaigns pass; no universal/human/kernel or priority assurance. Read S011 research/primary/AUDIT/MILESTONES. New proof cold challenge FUTURE S012; phases2-6 unchanged/deferred. Actual outgoing integration IDs/jobs/main reread belong in S011 PR metadata.

## Current S012 authority - 2026-10-15

Earlier current/future sections are historical. Last S012, next S013 strictly FUTURE/UNEXECUTED. Universal critical STACK/CLEAR OPEN, printed PASS separate. S01153-58 cold challenge and12 needed check-only replays PASS; historical hashes/cutoffs retained. New59 exact marked-input reciprocity/symmetric TWO insertion and zero-bit protected first move,60 exact donor1/2 languages,61 whole-history originalR3/triangular escape/fuel/componentwise conditional AS at gap>=2,62 distinguished-output occurrence permutation are programme-proved at stated scopes. They do NOT establish global AS selection/gluing. Symmetric assigned C6 masks are not realized inputs; actual critical C5 unit donor exception and double transfer winning only at other roots expose missing root availability, not ASH*. Three prior-hashed dual-validator campaigns pass; two fixed n6 exact threshold controls8/8 and12/12 are computed only. Draft zero-base/donor interpretation failures retained/corrected. Read S012 research/primary/AUDIT/MILESTONES. Fresh new-proof cold challenge FUTURE S013; phases2-6 unchanged/deferred, no human/kernel or worldwide priority assurance. Actual outgoing integration IDs/jobs/main reread belong in S012 PR metadata.
