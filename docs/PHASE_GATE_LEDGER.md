# Phase gates

| Phase | Status at S001 | Exact exit condition |
|---|---|---|
| 0. Bootstrap | **PASS — 2026-10-12** | Core authority, protocol, catalogues, provenance bridge, routes, ledger, S001 closeout and future S002 |
| 1. Mathematics | **IN_PROGRESS** | Unconditional complete ASH proof OR fully certified finite counterexample; independent proof audit before 2 |
| 2. First novelty check | NOT_STARTED | Written primary-source search/equivalence classification for exact result and dependencies |
| 3. Lean | NOT_STARTED | Kernel-checked theorem/certificate with pinned dependency closure, actual reproducible build |
| 4. Final comprehensive novelty | NOT_STARTED | Fresh broad primary and alternative-formulation audit of final exact theorem |
| 5. Palomar | OWNER_GATED | Explicit approval, frozen verified commit, policy/current preflight, registry entry verified |
| 6. arXiv | OWNER_GATED | Authorised source-ready paper, references, reproducible bundle, current submission preflight |

Bootstrap PASS is **administrative**, not mathematical success. In particular ASH, cycle equalities under ASH, and pre-existing TreeStack statements must remain distinct.

S002 review (2026-10-12): Phase 0 PASS inherited. Phase 1 IN_PROGRESS: no unconditional universal proof or certified counterexample; October PDF exact source gate PARTIAL. 1,918,566 bounded computations and two full independent cold checks are not a Phase 1 completion. Phases 2–6 NOT STARTED/OWNER_GATED, no promotion.

S003 review (2026-10-12): Phase 0 PASS inherited. **Phase 1 IN_PROGRESS — literal-form exit candidate.**
- Achieved: the printed ASH (October Hypothesis 3.2 = April 9.1) is refuted by certified finite counterexamples for both halves. Stack fails on P4 at t=12; clear fails on the bull graph at t=12. Finite certificates were checked by five (P4) / four (bull) independent tools; a human-checkable proof is in `research/S003_AS_GAP_AND_ATTACKS.md`.
- Missing before PASS: the gate's own "independent proof audit before 2" (a cold re-check by a fresh session), scheduled for S004. Rule 7's Lean kernel proof belongs to Phase 3.
- The critical form ASH* is OPEN.
- Phases 2–6: NOT STARTED/OWNER_GATED; no promotion.

2026-10-13 correspondence update (NOT a research session): Tamás Csernák confirms ASH* is the intended conjecture; the printed statement is stronger and false. **No phase advancement**. The independent cold audit and any printed-form Phase 1 exit decision remain S004 responsibilities; ASH* universal proof/counterexample remains open under Phase 1. Author's n<=7 report is SOURCE_STATED, not a completed independent rerun. Phases 2–6 unchanged.
