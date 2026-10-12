# S003 closeout — 2026-10-12

## Required explicit statements
- **Universal ASH, stacking — printed form (October Hyp. 3.2(1) = April Hyp. 9.1(1)): FALSE.**
  - Certified finite counterexample on P4 (0-1-2-3) at t=12. All 32 almost-stacked configurations of size 12 are stackable; (1,0,2,9) is not; stack(P4)=15.
  - Certificate: `evidence/S003/cert_P4_stack_t12.json`.
  - Lean proof: NOT started (Phase 3). Independent cold audit: scheduled for S004.
- **Universal ASH, clearing — printed form (Hyp. 3.2(2) = 9.1(2)): FALSE.**
  - Certified on the non-bipartite bull graph (edges 0-4, 1-3, 2-3, 2-4, 3-4) at t=12. All 80 AS configurations of size 12 are clearable; (1,9,0,2,0) is not; clear=15.
  - Certificate: `evidence/S003/cert_bull_clear_t12.json`.
- **Critical form ASH\* (what the authors' atlas code tests): OPEN for both stacking and clearing.**
  - Proved for all trees (earlier TreeStack theorem + October Thm 5.2) and for complete bipartite graphs (S003 Thm 10 + April Thm 8.2).
  - Computed true on every connected graph with n≤7 whose threshold was found, and on every connected 8-vertex graph with threshold ≤26.
- **Certified counterexample status:**
  - Printed form: certified, with five independent tools for P4 and four for the bull graph, human-checkable finite certificates, and a replay in hosted CI.
  - Critical form: none found.
- **Source access level:**
  - October 2610.09650v1: STATEMENT_INSPECTED (full text; Lemma 4.7 and Thm 5.2 PROOF_INSPECTED).
  - April 2604.22341v1: STATEMENT_INSPECTED.
  - Authors' atlas code: inspected at `701cdd93`.
  - Source gate for statements: PASS.
- **First serious remaining obstruction.** Prove or refute ASH\*: that the largest size of a non-stackable (non-clearable) configuration is attained by an almost-stacked one. Critical-layer compression is refuted as a route (5-cycle, t=7). A global obstruction certificate generalising the mod-3 weight arguments (October Thm 5.2; S003 Thm 10) is the leading idea.
- **Phase 1:** NOT passed in S003. It is an exit candidate for the printed form, pending the gate's independent proof audit (S004). Phase 1 stays IN_PROGRESS, Phases 2–6 are untouched, and nothing was silently advanced.

## What was done
1. Entry pins are recorded in `INPUT.md`. The preregistered plan was hashed before any run (`PLAN.md`), and amendment 1 was hashed before its runs.
2. Source gate: the October v1 PDF was read in full and reconciled line by line with April (`research/S003_SOURCE_RECONCILIATION.md`). The hypothesis content is identical. estim is identical for |V|≥2; October adds K1.
3. Mathematics (`research/S003_AS_GAP_AND_ATTACKS.md`), all with complete proofs:
   - the AS-gap reformulation (Thm 4) and the counterexample certificate shape (Cor 5);
   - the printed-form counterexamples (Thms 6, 7);
   - ASH\* for trees (Thm 8);
   - the trivial case g=n+1 (Thm 9);
   - complete bipartite graphs (Thm 10);
   - the consequences for the source's conditional theorems: §4–5 survive under ASH\*, while §6 is now unsupported (not refuted).
4. CAM-S003-01, using the forward C DP, an independent reverse C solver, a Python reverse fixpoint, an AS memo solver and an independent certificate checker. Every layer comparison agreed.
   - T1: C6–C8 and the S002 graphs (exact stack(C8)=31).
   - T2: the n≤6 atlas.
   - T2b: the n=7 atlas.
   - T3: trees with n≤9.
   - T4: W9, C9+chord and the Petersen graph.
   - A3: the n=8 atlas with t≤26.
5. S002 erratum: C8+chord{0,4} is non-bipartite; stack=clear=23 (FL-0013).
6. Atlas provenance: the authors' `is_critical_stacked_almost_stacked` tests the critical form, which explains why their atlas did not detect the printed-form failures. No wrongdoing is asserted and there was no contact.
7. The hosted workflow now also replays the three certificates, and the validator re-verifies the evidence hashes.

## Honest limits
- No Lean proof, and no novelty or priority audit.
- Graphs above their caps carry no verdict, and six order-9 trees were not completed. There is no claim beyond the enumerated graphs.
- April Thm 8.2 is cited, not proof-inspected. The TreeStack theorem is cited, not re-built.
- The source is an arXiv preprint; a later version may change the printed statement, and S004 must check this.

## Git/PR
- One atomic authored session commit on the harness-designated development branch, then an ordinary PR to main and a non-force merge.
- The actual commit, PR number, merge commit and post-merge main SHA must be read from GitHub after the merge. They are deliberately not embedded here, to avoid speculative SHAs.

## Next
The complete strictly FUTURE S004 handoff is in `authoritative/NEXT_SESSION_PROMPT.md`: independent cold audit, the Phase 1 gate decision, and the ASH\* attack. **S004 is UNEXECUTED and requires a fresh owner invocation.**

An owner decision (not a blocker): whether to notify the authors of the printed-form discrepancy. This is owner-gated and not done.
