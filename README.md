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

## Current S013 authority - 2026-10-15

Earlier current/future sections are historical. Last S013, next S014 strictly FUTURE/UNEXECUTED. Universal critical STACK/CLEAR OPEN; printed PASS separate. S01259-62 cold challenge and18 needed replays PASS with historical hashes/cutoffs retained. New63-70 prove exact open-neighborhood even concentration (zero/singleton receivers with precise mass3 STACK exception), GLOBAL Q/P minimal-heavy-neighborhood selection and an equivalent restriction of BOTH extremal maxima; conditional CLEAR comparable-component consequence/private-exit burden/all-root THREE exclusion retain explicit scopes. Incomparable minimal neighborhoods and general integer-hole/gluing comparison remain. Actual gap1 first-step shadow and threshold/GLOBAL-Q deletion-independence routes fail, not ASH*. Six registered dual-validator campaigns PASS, no universal/human/kernel/priority assurance. Read S013 research/primary/AUDIT/MILESTONES. Fresh proof cold challenge FUTURE S014; phases2-6 unchanged/deferred. Actual outgoing integration evidence is in S013 PR metadata.

## Final S014 authority - owner-requested closeout, 2026-10-16

The owner's later explicit request, `Can you commit and close out this session`, supersedes all earlier S014 keep-going/no-closeout instructions in this file. Those earlier checkpoint paragraphs are historical. S014 is COMPLETED at the administrative session boundary; universal critical STACK and CLEAR remain OPEN. Phase1 remains IN_PROGRESS; phases2-6, Lean, registration, publication and contact are unchanged and unexecuted. S015 is strictly FUTURE, UNEXECUTED; its complete prompt is sessions/S014/FUTURE_S015.md and authoritative/NEXT_SESSION_PROMPT.md.

S014 preserves 81 preregistered bounded campaigns and local proof items71-121, at their exact scopes and LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING assurance. Main advances include arbitrary-buffer join-class ASH*, exact Q4 stack31/L_AS30 and FanoInc14 stack30/L_AS29, subcubic boundary-tree and unique-marker characterizations, prescribed-heavy-source first-move existence, safe graph-leaf firing, odd-leaf contraction and critical leaf/neighbor restrictions. None proves universal SAME-GRAPH L_all(G)<=L_AS(G). Earlier TreeStack is credited prior work. Direct unit exchange is false; rescaled-sector exchange, H2r, critical core oddness and arbitrary-buffer domination remain unproved. All caps, prior-scope UNKNOWNs, unexecuted suffixes, mathematical failures and separate repairs remain archived. CAM77 excludes only F8; F9/F10/F12 remain UNKNOWN. See CLOSEOUT for the exact final synthesis.

Final governance/provenance validation and immutable hashes are required before the one atomic authored commit, ordinary PR and non-force two-parent merge. Actual outgoing head/tree/parents, hosted jobs and final main are verified after creation and recorded in PR metadata, without circular self-SHA claims in this commit. Administrative memory failures are retained separately under evidence/S014/admin_recovery; no resource failure becomes a mathematical conclusion.

## S015 final - critical ASH*-STACK counterexample G9 (2026-10-16)

S015 executed under the owner invocation `Run a sustained attack on the next session, aim to resolve a major obligation or proof`. Result: universal critical ASH*-STACK is FALSE at COMPUTED_EXACT level. On G9 = graph6 HCQTaXi, edges 0-3,0-5,0-6,1-4,1-7,1-8,2-6,2-8,3-5,3-6,4-7,4-8,5-7,6-8, stack=15, the only mass-14 losers are (0,0,1,0,0,5,0,8,0) and its automorphic image, and every AS configuration of mass 14 stacks, so L_all=14>L_AS=13. Checkers: two separately written compiled loser-layer tools, a bare-definition brute force over all configurations of masses 1..16, closed-set and AS winning-sequence certificates (separate verifier), 490314 replayed mass-15 winning sequences, a Python layer validator, and the source authors' own public atlas code (is_critical_stacked_almost_stacked False). A human-readable non-stackability proof uses S014-111/112/113, cold-challenged in S015. Status LEAN_PENDING and INDEPENDENT_COLD_RECHECK_PENDING; no author contact. Complete atlases: every connected graph of order <=8 satisfies the STACK equality (minimum counterexample order is 9); order 9: 261080 graphs, 261008 dual-verified ASH_OK, 1 failing (HCQTaXi), 71 UNKNOWN/not dual-compared (listed in evidence/S015/cam85/summary.json). CAM90/91 families give further dual-verified counterexamples of orders 10-13 (bridge-path family PB(4,4,l,1) fails at l=0,2,4 with L_all=14,30,62; infinite family is a conjecture only). Universal critical ASH*-CLEAR remains OPEN (deferred). Earlier TreeStack and the printed-form counterexamples are unaffected and remain credited/separate. See research/S015_G9_COUNTEREXAMPLE.md, research/S015_UNIVERSAL_RESEARCH.md, sessions/S015/CLOSEOUT.md.

Current status after S015: the intended critical Almost Stacked Hypothesis for STACKING is false; the nine-vertex graph G9 is a counterexample (computer-verified several independent ways, Lean and independent re-check pending). The clearing version remains open.

## S016 final - G9 refutes both clauses (2026-10-16)

The intended critical ASH* fails for **both** clauses on the nine-vertex graph G9 = graph6 `HCQTaXi`: stack(G9)=clear(G9)=15, and in both games the only mass-14 losers are (0,0,1,0,0,5,0,8,0) and its automorphic image, neither almost stacked (L_all=14 > L_AS=13). The STACK refutation passed an independent cold re-check in S016 (sessions/S016/GATE1_AUDIT.md); the CLEAR refutation is computed and certified (research/S016_CLEAR.md) with its fresh-session cold re-check scheduled for S017. Lean formalisation is pending (owner-gated). Every connected graph of order <=8 satisfies both clauses, so 9 is the minimum order. Earlier TreeStack (arXiv:2609.31811) and the printed-form counterexamples remain separate, credited results.
