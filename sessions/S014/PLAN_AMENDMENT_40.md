# CAM-S014-40: small necessary-clause cores with fresh independently replayed proofs

2026-10-15 BEFORE execution. CAM38 C9a/C9b are solver-UNSAT but independent
full proof replay hit its explicit scan caps; neither is an accepted exclusion.
CAM39 C9a also hit its occurrence cap. Preserve these UNKNOWN outcomes. CAM38
C10 hit its clause cap before solving its sound partial expanded formula.

Exact inputs: the four CAM38 v2 fixed cases and their independently validated
expanded formulas, including C10's partial sound clause set. First solve the
frozen formula. If SAT record UNKNOWN (no graph oracle/model promotion here).
If UNSAT, use one selector per original clause and assumption-core extraction
only as a heuristic to select a smaller subset of the original necessary
clauses. At most128 additional native calls for chunk deletion/core tightening.
Native core validity is NOT trusted: save explicit original clause indices,
and fresh proof-logging solve the final selected formula. Independently check
EVERY selected clause matches its frozen original index and original necessity
pass, then replay EVERY fresh DRUP step via the separate CAM39 pure-Python
occurrence checker, with no native calls in that verifier. Any subset of
necessary clauses suffices if its UNSAT is independently certified.

PRIOR bounds:500000 input clauses,128 tightening calls,500000 proof lines,
540seconds internal/600seconds external/2GiB per producer or checker;
500000000 active occurrence visits as CAM39. No cap increase on the failed
proofs. At most2 mathematical children; these four cases run sequentially.
Freeze code/plan/input-original digests before producer and derived subset,
indices/proof/digests before independent checkers. SAT/resource/proof failure
is UNKNOWN. Scope remains ONLY each fixed-c graph-class exclusion, not the
universal ASH*, all configurations, CLEAR or a session completion. No later
stage action or correspondence.
