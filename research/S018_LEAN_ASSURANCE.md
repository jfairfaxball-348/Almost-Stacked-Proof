# S018 - Lean assurance of the G9 refutation of critical ASH*

Session records: sessions/S018/LEAN_ASSURANCE.md (build, Comparator, kernels), LEAN_COLD_RECHECK.md (statements), SUBMISSION_PREP.md (draft metadata, owner items, gate proposals).

## Result

The Lean development in formal/ (S017) proving that the critical Almost Stacked Hypothesis ASH* fails in both clauses on G9 = graph6 `HCQTaXi` was (1) rebuilt from a clean state with the same outcome; (2) checked by the pinned toolchain's `lake comparator`, which, after a fix of finding F1 in Challenge.lean, finds all 25 Solution statements identical to the Challenge and only the axioms propext, Quot.sound, Classical.choice; (3) replayed by Lean's kernel and, standalone at one thread, by the independent kernels nanoda and con-ron (verified mode) and by lean4lean and leanchecker-paranoid, all accepting; con-leche did not finish within 12 GiB (UNKNOWN); (4) its statements were re-checked line by line against research/ASH_SPEC.md (PASS).

## Scope and limits

- LOCAL and UNSANDBOXED: Windows host without bwrap; Palomar runs the same tool sandboxed on a 32 GB Linux runner. No single comparator invocation with exit 0 including external kernels exists yet; hosted Lean CI does not exist yet (S019 proposal).
- F1 was a universe-parameter name (`u_2` vs `u_1`) in three general lemmas of Challenge.lean, not a mathematical difference; fixed on the Challenge side; no frozen module changed.
- Nothing new is claimed mathematically: universal critical ASH* is FALSE in both clauses (G9), the printed form is FALSE (S003/S004); universal L_all(G) <= L_AS(G) is not claimed. TreeStack (arXiv:2609.31811) is earlier, credited, unused work.
- No submission, registration, publication or contact; formal/formalization.yaml is a draft with owner fields open and no repository licence yet.
