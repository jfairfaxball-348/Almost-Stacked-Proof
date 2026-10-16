# CAM-S014-47: proved representative symmetry plus coupled-hole synthesis

2026-10-15 BEFORE execution. Use the exact finite-orbit proposition94 and
independently checked local prefix CNF extension to search fixed-input graph
classes more efficiently. Symmetry is proved representative existence, NOT
claimed necessary for every labeled countermodel. No unsupported graph quotient.

Cases in order: E9 and E10 from CAM41; C10 from CAM43; T12 from CAM41; and
NEW D12 input (3,3,1,1,0,0,3,3,1,1,0,0),n12,M16. D12 tests arbitrary graph
couplings of the two earlier parity-hole inputs, with ALL66 edges variable,
not just CAM30's matching links. All c have M>=n+1. Import every already frozen
base record/certificate for the first four cases; D12 begins only with degree
cuts. No imported assumption of criticality or AS failure. Use identity clause
images only; no factorial clause closure. Instead add lex<= constraints for
each adjacent transposition inside each equal-count label class, as94.

Continue exact necessary-clause CEGIS: c-positive literal histories, AS-negative
supergraph complete closures, lazy connectivity, exact ALL3 AS layers90.
Minimize each new winning edge support. Save the exact queried graph/input
on an oracle state cap for a separately bounded follow-up; it remains UNKNOWN,
never a negative certificate or actual counterexample. A query graph can be
a temporary support subgraph, so do not assert it is itself a SAT model.

PRIOR limits10000 iterations,50000 graph-certificate clauses,300000 oracle
states/query graph,540seconds internal/600seconds external/2GiB per process;
500000 native DRUP lines. Graph clauses and lex clauses saved separately, full
CNF is their exact concatenation. Independently replay EVERY graph base clause
via CAM37, compare deduplicated graph clauses, independently check each true
prefix and ALL local block truth tables plus complete variable/permutation
allocation. Produce explicit `counterexample_exists_implies_formula_satisfiable`
and `all_graph_clauses_necessary` flags, NEVER the false claim that each lex
clause holds for every labeling. The mathematical orbit/extension proof94 is
part of the frozen preflight. All variables/hypotheses/quantifiers retained.

If UNSAT, frozen fresh native proof then CAM45's native untrusted LRAT hints
and separate Python clause-id RUP replay, with unchanged500000 additions/
1000000 lines/100000000 hints/540s caps. A dedicated verifier copy accepts ONLY
the explicit representative-reduction flag instead of the all-labeled-clauses
flag; unit proof semantics unchanged. A potential gets full c-negative/ALL3AS
positive coordinate replay then separately registered threshold/cold audit.
Any cap/partial/proof failure UNKNOWN. Every imported/new artifact and code
hashed before use, derived outputs frozen before checkers. Two sequential-case
shards (even/odd indices), max2 mathematical children TOTAL; launch only when
CAM46 releases slots. Shared potential flag stops next cases. No CLEAR,
delegation, session closeout, next session, later stage or external action.
