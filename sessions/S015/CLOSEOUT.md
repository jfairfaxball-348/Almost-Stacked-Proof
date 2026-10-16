# S015 closeout - critical ASH*-STACK refuted by a nine-vertex graph (computed, multi-checker); CLEAR OPEN

Closeout was requested by the owner (`Think its stalled, maybe best to commit and push and merge what we have and closeout the session`, OWNER_CLOSEOUT.txt); unfinished order-9 workers were stopped and their graphs recorded UNKNOWN. Owner invocation: `Run a sustained attack on the next session, aim to resolve a major obligation or proof` (OWNER_INVOCATION.txt). Exactly S015 executed from the frozen S014 handoff (AUTHORISED_PROMPT.md). S016 and all later stages remain unexecuted.

## Mathematical outcome

**Universal critical ASH*-STACK is FALSE** (COMPUTED_EXACT, multiple independent checkers; LEAN_PENDING; INDEPENDENT_COLD_RECHECK_PENDING). On G9 = graph6 `HCQTaXi` with edges 0-3, 0-5, 0-6, 1-4, 1-7, 1-8, 2-6, 2-8, 3-5, 3-6, 4-7, 4-8, 5-7, 6-8 (two diamonds joined at both tip pairs, plus a vertex adjacent to one tip pair):

- stack(G9) = 15: every configuration of mass 15 stacks (490,314 replayed winning sequences; brute force), hence every larger mass;
- the only non-stackable configurations of mass 14 are (0,0,1,0,0,5,0,8,0) and its automorphic image; non-stackability has closed reachable-set certificates (1974 states) AND a human-readable proof via S014-111/112/113;
- every almost-stacked configuration of mass 14 stacks (2304 replayed sequences);
- so L_all = 14 > L_AS = 13: no AS configuration of size stack(G9)-1 is non-stackable.

Independent confirmations: two separately written compiled loser-layer tools; a bare-definition brute force over all configurations of masses 1..16; a Python layer validator; and the source authors' own public atlas code (lajossoukup/pebbling@701cdd93), whose `is_critical_stacked_almost_stacked()` returns False on G9 with the same stacking number and witnesses (controls P4, C5 True). Full report: research/S015_G9_COUNTEREXAMPLE.md.

Atlases: every connected graph of order 2..8 (12,112 graphs) satisfies L_all = L_AS (dual compiled, byte-identical critical layers; agreement with all frozen S003 thresholds), so 9 is the minimum counterexample order. Order 9 (261,080 graphs, nauty-geng): 261,008 dual-verified ASH_OK, exactly ONE failure (G9), 71 UNKNOWN (22 trees, which satisfy critical ASH* by the earlier credited TreeStack theorem + S003 Thm 8, and 49 non-trees left unfinished when the owner requested closeout; listed in evidence/S015/cam85/summary.json). Amendment-7 Python sampling of order 9 and CAM88 were not executed.

Families: CAM90 finds 12 dual-verified counterexample graphs of orders 9-13 around G9 (eight one-vertex extensions, F(4,5,1), bridge-path P(4,2) and P(5,2) with L_all=30, L_AS=29); all twelve are also confirmed by the source authors' code (CAM92) and three by the Python validator. CAM91 (producer; checker re-run per graph) gives PB(4,4,l,1) failures for l=0,2,4 with L_all = 14, 30, 62 and successes for l=1,3: an infinite family for even l is a CONJECTURE only.

Local proofs: S015-122/123 (critical shift lemmas from S014-116; re-derive S014-117c). S014-111/112/113/116 were cold-challenged and reused. On all order-<=8 critical layers, H2r holds (receiver a largest pile) and global-Q maxima are AS; both statements are false universally because each implies ASH*.

Consequences: the S013/S014 universal-bridge routes cannot succeed universally; their scoped theorems stand. Trees (earlier TreeStack + S003 Thm 8), complete multipartite graphs, join classes and other proved classes still satisfy critical ASH*. Printed-form counterexamples are a separate earlier result. Bipartite critical ASH*-STACK remains open (no bipartite counterexample known). Critical ASH*-CLEAR remains OPEN (deferred this session).

## Campaigns and integrity

Plans: PLAN.md and PLAN_AMENDMENT_1..12, each hashed before execution, with addenda for deviations: aborted unrepresentative order-9 pilot (amendment 2), stopped S9 sample, Python order-8 third check stopped at 31 graphs by its time policy, chunk_00 restructuring (amendment 11), CAM91 checker crash on PB(4,4,4,1) from a cap/ulimit mismatch (tool failure, re-run per graph), operator stop of the CAM91 producer at n=14, a shell cwd race. CAM87 (heuristic search) and CAM88 (bipartite order 10) were registered but NOT executed; amendment 7's order-9 overflow fallback and Python sampling clauses are executed only as recorded in evidence/S015/cam85/summary.json. Evidence manifest: evidence/S015/HASHES.md (all S015 session/evidence/tool/research bytes). Large layer files are stored xz-compressed with digests of the decompressed producer/checker outputs recorded in the campaign summaries.

## Gates, permissions, integration

Phase 0 PASS; Phase 1 IN_PROGRESS (STACK component refuted at computed level, awaiting the S016 cold re-check and the rule-7 Lean proof; CLEAR open); phases 2-6 untouched; no Lean, Palomar, arXiv, publication or author contact. One atomic authored S015 commit on branch ccr-a9fdff28-6mqxx0 (harness-designated), ordinary PR and non-force merge if permitted; actual commit/PR/merge/hosted-job identifiers are recorded after creation in PR metadata, not in this file. The governance validator and hosted workflow are extended to the S015-closed state and replay both G9 certificate checkers.

The complete FUTURE/UNEXECUTED S016 handoff follows verbatim and is identical to authoritative/NEXT_SESSION_PROMPT.md.

# S016 - Cold re-check of the G9 STACK counterexample, then the critical CLEAR question

**FUTURE, UNEXECUTED.** Requires a fresh explicit owner invocation. Execute exactly S016 in https://github.com/jfairfaxball-348/Almost-Stacked-Proof. S015 is the last completed session. Stop before S017. No delegation of research judgement, Lean, registration, publication, manuscript/arXiv, Palomar or correspondence with the source authors is authorized by this handoff; each needs explicit owner authorization. This prospective handoff does not authorize execution.

## Where S015 left the problem

The target was the intended critical Almost Stacked Hypothesis, separately for STACK on finite connected simple graphs (n>=2) and CLEAR on connected non-bipartite graphs:

    L_all(G) <= L_AS(G)   (equivalently: some AS loser of size stack(G)-1).

S015 found that the STACK form is FALSE. On G9 = graph6 `HCQTaXi` (edges 0-3,0-5,0-6,1-4,1-7,1-8,2-6,2-8,3-5,3-6,4-7,4-8,5-7,6-8; two diamonds joined at both tip pairs, plus a vertex adjacent to one tip pair), stack(G9)=15, the ONLY losers of mass 14 are (0,0,1,0,0,5,0,8,0) and its automorphic image, and every AS configuration of mass 14 stacks: L_all=14 > L_AS=13. Evidence (research/S015_G9_COUNTEREXAMPLE.md, evidence/S015/counterexample): two independently written compiled loser-layer tools; a bare-definition brute force over all configurations of masses 1..16; closed reachable-set certificates (1974 states each); 6912 replayed AS winning sequences (masses 14-16); 490,314 replayed winning sequences covering EVERY mass-15 configuration; a human-readable proof of the non-stackability via the S014 boundary-tree characterization 111-113. Status: COMPUTED_EXACT, multiple checkers, LEAN_PENDING, INDEPENDENT_COLD_RECHECK_PENDING.

Complete atlases: every connected graph of order <=8 satisfies the STACK equality (dual compiled, byte-identical critical layers), so 9 is the minimum order of a counterexample. The order-9 atlas result and its exact completeness scope (including any capped/UNKNOWN graphs and trees covered only by EARLIER TreeStack) are recorded in research/S015_UNIVERSAL_RESEARCH.md section 2a. Families CAM90/91 add dual-verified counterexamples of orders 10-13 (including bridge-path graphs with L_all=30, L_AS=29); their exact scope is in the same report. H2r and global-Q AS selection, being sufficient for ASH*, are false in general; they hold on all order <=8 critical layers. S015 local items 122-123 (critical shift lemmas) are proved; S014 items 111-113 and 116 were cold-challenged in S015; other S014 items 71-121 keep LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING.

Earlier TreeStack (arXiv:2609.31811 and its registered package) remains credited prior work: trees satisfy critical ASH* (S003 Thm 8). The printed exact-layer counterexamples (S003/S004) are a different statement. Do not describe G9 as refuting TreeStack or any tree result.

## Entry and cold re-check (first milestone)

Read AGENTS.md, authoritative/START_HERE.md, STATE.json, docs/SESSION_PROTOCOL.md and RELEASE_PROTOCOL.md, research/ASH_SPEC.md, the catalogues, route/decision/failure/session/gate/search ledgers, sessions/S015/{INPUT,PLAN,PLAN_AMENDMENT_*,AUDIT,CLOSEOUT} and research/S015_*.md. Pin LIVE remote main and independently reconcile the actual S015 commit, PR, merge, hosted jobs and check-runs (recorded after creation in PR metadata; do not infer them from this frozen prompt).

Then cold re-check G9 as a fresh session, adversarially: (i) re-derive the definitions and threshold convention from the inspected source scope (S003 Thm 4, October Lemma 4.7, author-confirmed intended meaning), including the n=0/1 exclusions, exact-total versus at-least thresholds and AS meaning; (ii) re-read the human proof of non-stackability line by line, including every case of the padded trees and the reliance on 111-113 and the credited cancellation 47; (iii) write a NEW independent checker (different language or different algorithm, e.g. a SAT/BDD encoding or a bitset reachability engine) that re-verifies all of K1-K4, rather than only re-running S015 tools; (iv) re-run all S015 certificate checkers and compare digests. Any discrepancy suspends the counterexample status until resolved and is recorded without rewriting S015 bytes.

## Main research objective

With universal critical ASH*-STACK refuted (pending the gates above), the remaining universal question is **critical ASH*-CLEAR** on connected non-bipartite graphs. Pursue it with the same discipline: preregistered complete atlases of non-bipartite graphs of order 8 and 9 for CLEAR (CLEAR losing-layer recursion with its own candidate/termination lemmas re-proved for CLEAR, clear(G) conventions checked), a direct check of G9 and the CAM90/91 family for CLEAR, and a symbolic attempt to adapt the G9 mechanism (a parity marker whose neighbours lie far from two adjacent fuel piles) to CLEAR. Either a certified CLEAR counterexample, a proof for a substantial class, or an honest OPEN status with exact finite scope.

Secondary (only after the cold re-check passes): (a) clarify whether the G9 phenomenon yields an infinite family (e.g. even bridge lengths), by symbolic proof rather than extrapolation; (b) characterize which local structure forces L_AS < L_all, to state a corrected hypothesis that could be true (for example a bounded number of heavy sites), clearly labelled as a new conjecture, not the authors'.

## Gates and permissions

Phase 1 stays IN_PROGRESS until both the STACK refutation passes the independent cold re-check and the CLEAR question is resolved or the owner revises the plan. Phase 2 (novelty audit of the counterexample) and Phase 3 (Lean kernel proof of G9's K1-K4, which AGENTS.md rule 7 requires before the counterexample is final) need explicit owner authorization; propose them in the closeout if not authorized. Contacting Csernák/Soukup about the counterexample is owner-only; the existing reply draft remains NOT SENT.

## Computational discipline

Before any computation write and hash a bounded amendment: exact graph/input class, order/mass limits, caps, symmetry justification, two independently written validators, completeness and UNKNOWN policy, code/input/output hashes. Caps are UNKNOWN, never evidence. The S015 environment was a Linux container (4 cores, 15 GiB); state the actual environment. Preserve all S003-S015 immutable manifests, failed attempts, aborted pilots and UNKNOWNs.

## Closeout

One branch, one atomic authored session commit, ordinary PR, non-force merge if permitted; pin actual heads/trees/parents/hosted jobs/main after creation. Synchronize state, spec, catalogues, decision/route/failure/session/gate/search ledgers, campaign registry and evidence manifests. Prepare a complete FUTURE/UNEXECUTED S017 handoff. Avoid model/vendor names in repository files.
