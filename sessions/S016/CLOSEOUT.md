# S016 closeout

S016 executed under the owner invocation `run next session` (later in-session owner messages: a withdrawn "Run next session", then "Wait ignore that, continue and closeout when appropriate", then "Yeah no need to keep checking other graphs.. if we have the counterexample then let's finish up", which stopped the remaining cross-checks).

## Result

- **Gate 1 PASS.** The S015 counterexample G9 = graph6 `HCQTaXi` to critical ASH*-STACK survives an independent cold re-check: new Rust and Node checkers with a different algorithm, every S015 checker replayed with identical output, the full S015 manifest intact, hand proof audited (repairs R1-R3). sessions/S016/GATE1_AUDIT.md. Status COLD_RECHECK_PASS, LEAN_PENDING.
- **Critical ASH*-CLEAR is FALSE, on the same graph G9.** clear(G9)=15; the only mass-14 non-clearable configurations are the two STACK critical losers (0,0,1,0,0,5,0,8,0) and image, neither AS; every AS configuration of mass 14 and every configuration of mass 15 clears; L_all^CLEAR=14>L_AS^CLEAR=13. Non-clearability is proved by hand (clearable implies stackable); the finite facts are certified by a bare-definition backward closure, 492,618 replayed clearing sequences and dual layer tools. COMPUTED_EXACT, INDEPENDENT_COLD_RECHECK_PENDING, LEAN_PENDING. research/S016_CLEAR.md.
- Both clauses of the intended critical Almost Stacked Hypothesis are therefore refuted by one nine-vertex graph.
- CLEAR atlases: all non-bipartite connected graphs of order <=8 satisfy CLEAR (dual; frozen order<=7 values reproduced), so 9 is the minimum order; order 9 producer-complete with G9 unique, dual for 207,794 graphs (checker stopped at owner request). S015 families: 17 dual CLEAR failures, coinciding with the STACK failures.

## Campaigns

CAM-S016-01..06 (PLAN.md, PLAN_AMENDMENT_1/2, addenda). Protocol deviation: pre-amendment smoke test (archived, excluded). Comparator defect fixed before use. CAM05/CAM06 checkers stopped at owner request; their unchecked graphs are producer-only.

## Gate decision

Phase 1 remains IN_PROGRESS: the STACK refutation has passed the cold re-check; the CLEAR refutation awaits the S017 fresh-session cold re-check. AGENTS.md rule 7 requires Lean kernel proofs for both. **Proposal to the owner (not executed): authorise Phase 3 Lean formalisation of G9 K1-K4 for STACK and K1c-K4c for CLEAR after the S017 re-check, and decide the Phase 1 gate.** Phases 2-6 unchanged; no Lean, Palomar, arXiv, publication or author contact. The draft reply to the authors remains NOT SENT.

## Integration

One branch session/S016-g9-recheck-and-clear, one atomic authored commit, ordinary PR, non-force merge if permitted; actual head/tree/parents, hosted jobs and final main are recorded after creation in PR metadata (no circular self-SHA claims here).

## FUTURE S017 handoff (identical to sessions/S016/FUTURE_S017.md and authoritative/NEXT_SESSION_PROMPT.md)

# S017 - cold re-check of the G9 CLEAR counterexample, then consolidation of the double refutation

**FUTURE, UNEXECUTED.** Prepared at the S016 closeout (2026-10-16). Requires a fresh explicit owner invocation. Execute exactly S017 in https://github.com/jfairfaxball-348/Almost-Stacked-Proof. S016 is the last completed session. Stop before S018. No delegation of research judgement, Lean, registration, publication, manuscript/arXiv, Palomar or correspondence with the source authors is authorized; each needs explicit owner authorization. This prospective handoff does not authorize execution.

## Where S016 left the problem

The intended critical Almost Stacked Hypothesis has a STACK clause (connected simple graphs, n>=2) and a CLEAR clause (connected non-bipartite graphs), each of the form

    L_all(G) <= L_AS(G)   (equivalently: some AS loser of size g(G)-1).

On G9 = graph6 `HCQTaXi` (edges 0-3,0-5,0-6,1-4,1-7,1-8,2-6,2-8,3-5,3-6,4-7,4-8,5-7,6-8; non-bipartite via triangle 0-3-5):
- STACK: stack=15, L_all=14>L_AS=13 (S015). S016 Gate 1 COLD_RECHECK_PASS (sessions/S016/GATE1_AUDIT.md): new Rust backward-closure and Node forward checkers, every S015 checker replayed with identical outputs, 286/286 S015 manifest hashes, hand proof audited with three editorial repairs R1-R3. LEAN_PENDING.
- CLEAR (S016, research/S016_CLEAR.md): clear=15, the only mass-14 non-clearable configurations are the same two STACK critical losers (0,0,1,0,0,5,0,8,0) and image, no AS non-clearable configuration of mass 14, none of mass 15: L_all^CLEAR=14>L_AS^CLEAR=13. Evidence: two independently written layer tools, a bare-definition backward closure from the mass-1 configurations, 492,618 replayed clearing sequences (every AS configuration of mass 14 and every configuration of mass 15) with a separate Python verifier, closed reachable sets without a mass-1 state, and a human proof of non-clearability through the elementary loser-inclusion T1 (clearable implies stackable). Status COMPUTED_EXACT, INDEPENDENT_COLD_RECHECK_PENDING, LEAN_PENDING. The authors' public clearing code was not run in S016.
- Atlases (S016, dual tools): every non-bipartite connected graph of order <=8 satisfies ASH*-CLEAR (924 of orders 2..7 matching frozen S003/S004 values, 10,935 of order 8), so 9 is the minimum order of a CLEAR counterexample. Order 9: the producer completed all 261,080 graphs (730 bipartite skipped) and finds G9 the UNIQUE CLEAR failure; the independent checker was stopped at the owner's request after 207,794 graphs (all agreeing), so 53,286 order-9 graphs are producer-only (evidence/S016/gate2/cam05/summary.json). All 17 S015 STACK-failure family members that completed also fail CLEAR (dual), and on the S015 families the STACK and CLEAR verdicts coincide wherever both are known. The S015 order-9 STACK UNKNOWN list (71) was re-run: 69 producer ASH_OK, 2 capped, only 9 dual-verified (cam06).

Both clauses of the intended hypothesis are therefore refuted at COMPUTED_EXACT level; the CLEAR refutation has NOT had a fresh-session cold re-check. S014 local items 71-110, 114-115 and 117-121 remain LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING (111-113 and 116 cold-challenged in S015). Earlier TreeStack (arXiv:2609.31811, registered package) remains credited prior work; S003/S004 printed-form counterexamples are a separate statement.

## Entry

Read AGENTS.md, authoritative/START_HERE.md, STATE.json, docs/SESSION_PROTOCOL.md and RELEASE_PROTOCOL.md, research/ASH_SPEC.md, the catalogues, the route/decision/failure/session/gate/search/handoff-revision ledgers, sessions/S016/{INPUT,PLAN,PLAN_AMENDMENT_*,GATE1_AUDIT,AUDIT,CLOSEOUT} and research/S016_CLEAR.md. Pin LIVE remote main and independently reconcile the actual S016 commit, PR, merge, hosted jobs and check-runs (recorded in PR metadata; do not infer them from this prompt).

## Gate 1 (mandatory): independent cold re-check of the G9 CLEAR counterexample

1. Re-derive the CLEAR definitions and threshold convention (S003 Lemma 1/2, Prop. 3, Thm 4 with g=clear; October Lemma 4.7; exactly-one-pebble terminal; bipartite exclusion) and check T1-T3 of research/S016_CLEAR.md line by line.
2. Write a NEW checker in a style not used in S015/S016 (for example a SAT/BDD encoding of K2c/K3c, or an exact integer-programming/parity argument, or a different language), preregister it in a hashed plan, and re-verify K1c-K4c.
3. Replay every S016 checker and compare with evidence/S016/HASHES.md.
4. Outcome rule: all agree => CLEAR refutation COLD_RECHECK_PASS; then propose to the owner a Phase 1 gate decision (both clauses refuted, Lean pending) and a Phase 3 Lean authorization covering G9 STACK and CLEAR. Any discrepancy => suspend the CLEAR status, diagnose definitively, record without rewriting S016 bytes.

## After Gate 1 (only if it passes)

Substantive, in this order of priority: (a) a structural explanation of the G9 mechanism for both clauses (why every mass-15 configuration clears; which stackable-but-not-clearable configurations exist near the threshold; T3 as a general transfer criterion); (b) a symbolic proof for the PB(4,4,2j,1) even-bridge family (STACK and CLEAR), currently a conjecture with computed members j=0,1 (j=2 STACK producer-only, CLEAR capped in S016); (c) bipartite critical ASH*-STACK (no bipartite counterexample known); (d) any remaining UNKNOWN order-9 graphs under a new bounded plan. A corrected or weakened hypothesis may be formulated only as a clearly labelled NEW statement, never as the authors'.

## Gates and permissions

Phase 1 stays IN_PROGRESS until the owner records a gate decision. Phase 2 novelty audit and Phase 3 Lean (AGENTS.md rule 7) need explicit owner authorization. Contacting Csernak/Soukup is owner-only; the existing reply draft remains NOT SENT.

## Computational discipline

Before any computation write and hash a bounded amendment: exact graph/input class, order/mass limits, caps, symmetry justification, two independently written validators, completeness and UNKNOWN policy, code/input/output hashes. Caps are UNKNOWN, never evidence. State the actual environment. Preserve all S003-S016 immutable manifests, failed attempts, aborted pilots, protocol deviations and UNKNOWNs. Do not claim L_all(G) <= L_AS(G) anywhere beyond computed or proved scopes.

## Closeout

One branch, one atomic authored session commit, ordinary PR, non-force merge if permitted; pin actual heads/trees/parents/hosted jobs/main after creation. Synchronize state, spec, catalogues, decision/route/failure/session/gate/search ledgers, campaign registry and evidence manifests. Prepare a complete FUTURE/UNEXECUTED S018 handoff. Avoid model/vendor names in repository files.
