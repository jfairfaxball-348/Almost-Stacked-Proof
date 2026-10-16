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
