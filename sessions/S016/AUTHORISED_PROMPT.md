# S016 - Gate 1: cold re-check of the G9 STACK counterexample; Gate 2 (only if it survives): critical ASH*-CLEAR

**FUTURE, UNEXECUTED.** Owner-directed revision (2026-10-16) of the frozen S015 handoff sessions/S015/FUTURE_S016.md: "Rewrite the next session to first recheck stack and then move on to clear if it survives." Requires a fresh explicit owner invocation. Execute exactly S016 in https://github.com/jfairfaxball-348/Almost-Stacked-Proof. S015 is the last completed session. Stop before S017. No delegation of research judgement, Lean, registration, publication, manuscript/arXiv, Palomar or correspondence with the source authors is authorized; each needs explicit owner authorization. This prospective handoff does not authorize execution. The owner intends to spend several sessions on CLEAR; S016 is the first of them, conditional on Gate 1.

## Where S015 left the problem

The intended critical Almost Stacked Hypothesis has a STACK clause (finite connected simple graphs, n>=2) and a CLEAR clause (connected non-bipartite graphs), each of the form

    L_all(G) <= L_AS(G)   (equivalently: some AS loser of size g(G)-1).

S015 found the STACK clause FALSE, which refutes the combined hypothesis, subject to the gates below. On G9 = graph6 `HCQTaXi` (edges 0-3,0-5,0-6,1-4,1-7,1-8,2-6,2-8,3-5,3-6,4-7,4-8,5-7,6-8): stack(G9)=15; the only mass-14 losers are (0,0,1,0,0,5,0,8,0) and its automorphic image; every AS configuration of mass 14 stacks; L_all=14 > L_AS=13. Evidence: research/S015_G9_COUNTEREXAMPLE.md and evidence/S015/counterexample (two separately written compiled tools, bare-definition brute force over masses 1..16, closed-set certificates of 1974 states, 6912 replayed AS winning sequences, 490,314 replayed mass-15 winning sequences, Python validator, the source authors' own public code returning False, and a human proof of non-stackability via S014-111/112/113). Status: COMPUTED_EXACT, LEAN_PENDING, INDEPENDENT_COLD_RECHECK_PENDING.

Atlases: all connected graphs of order <=8 satisfy the STACK equality; order 9 has 261,008 dual-verified passes, exactly one failure (G9) and 71 UNKNOWN (22 trees covered by EARLIER TreeStack, 49 non-trees stopped at closeout). CAM90/91 families add counterexamples of orders 9-13; the even-bridge infinite family is a conjecture only. Earlier TreeStack (arXiv:2609.31811, registered package) remains credited prior work (trees satisfy critical ASH*, S003 Thm 8); S003/S004 printed-form counterexamples are a separate statement. S014 items 111-113 and 116 were cold-challenged in S015; other S014 items 71-121 remain LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING.

## Entry

Read AGENTS.md, authoritative/START_HERE.md, STATE.json, docs/SESSION_PROTOCOL.md and RELEASE_PROTOCOL.md, research/ASH_SPEC.md, the catalogues, the route/decision/failure/session/gate/search/handoff-revision ledgers, sessions/S015/{INPUT,PLAN,PLAN_AMENDMENT_*,AUDIT,CLOSEOUT,OWNER_CLOSEOUT} and research/S015_*.md. Pin LIVE remote main and independently reconcile the actual S015 commit, PR #18, merge, hosted jobs and check-runs, and this administrative revision's own commit/PR (recorded in PR metadata; do not infer them from this prompt). Note that PR #18 was merged at the owner's request while its hosted jobs were still queued: record their actual outcomes.

## Gate 1 (first milestone, mandatory): independent cold re-check of G9

Re-check the STACK counterexample adversarially as a fresh session before any CLEAR work:

1. Re-derive the definitions and threshold convention from the inspected source scope (S003 Thm 4, October Lemma 4.7, the author-confirmed intended meaning SRC-0010): moves, stackable, almost stacked, exact-layer versus at-least thresholds, n=0/1 exclusions.
2. Re-read the human non-stackability proof (S015_G9_COUNTEREXAMPLE.md section 5) line by line, every padded-tree case, and its dependencies 111-113 and the credited cancellation 47.
3. Write a NEW independent checker in a different style (for example a SAT/BDD encoding, a bitset reachability engine, or a different language) that re-verifies K1-K4 without reusing S015 code, and preregister it in a hashed plan before running.
4. Re-run every S015 certificate checker and compare all digests with evidence/S015/HASHES.md.

Outcome rule. If every check agrees, record STACK refutation COLD_RECHECK_PASS (Lean still pending; propose a Phase 3 Lean authorization to the owner in the closeout) and proceed to Gate 2. If any discrepancy appears, do NOT proceed to CLEAR: suspend the counterexample status, investigate to a definite diagnosis, record it without rewriting S015 bytes, and make that the session's work.

## Gate 2 (only if Gate 1 passes): critical ASH*-CLEAR

Main objective for the rest of S016 and the following sessions: prove or disprove the CLEAR clause on connected non-bipartite graphs, with all S015 discipline.

1. Re-state and re-prove for CLEAR the loser-layer candidate and termination lemmas (target: exactly one pebble remaining; clear(G) conventions and the bipartite exclusion checked against ASH_SPEC and S003-S007 CLEAR results).
2. Cheapest test first: check G9, the twelve CAM90 counterexamples and the PB(4,4,l,1) graphs for CLEAR.
3. Complete non-bipartite CLEAR atlases of order 8 and then 9 with two independently written tools, compared against the frozen S003/S004 order-7 CLEAR results (809 graphs); report exact UNKNOWN scopes.
4. If a CLEAR counterexample appears: certify it as G9 was (brute force, replayable certificates, the authors' clearing function, a hand proof of the non-clearable part). If none appears: use complete critical layers to seek a mechanism, test whether the G9 parity-marker mechanism can transfer to CLEAR or explain why it cannot, and pursue a symbolic proof for a substantial class. Keep OPEN status honest.

Secondary only after Gate 2 work is substantive: the even-bridge infinite STACK family by symbolic proof, and finishing the 49 UNKNOWN order-9 non-tree graphs under a new bounded plan.

## Gates and permissions

Phase 1 stays IN_PROGRESS until the STACK refutation passes the cold re-check and the CLEAR question is resolved, or the owner revises the plan. Phase 2 novelty audit and Phase 3 Lean (required by AGENTS.md rule 7 before a counterexample is final) need explicit owner authorization. Contacting Csernák/Soukup is owner-only; the existing reply draft remains NOT SENT.

## Computational discipline

Before any computation write and hash a bounded amendment: exact graph/input class, order/mass limits, caps, symmetry justification, two independently written validators, completeness and UNKNOWN policy, code/input/output hashes. Caps are UNKNOWN, never evidence. State the actual environment. Preserve all S003-S015 immutable manifests, failed attempts, aborted pilots and UNKNOWNs.

## Closeout

One branch, one atomic authored session commit, ordinary PR, non-force merge if permitted; pin actual heads/trees/parents/hosted jobs/main after creation. Synchronize state, spec, catalogues, decision/route/failure/session/gate/search ledgers, campaign registry and evidence manifests. Prepare a complete FUTURE/UNEXECUTED S017 handoff that continues the CLEAR programme (or, if Gate 1 failed, the investigation). Avoid model/vendor names in repository files.
