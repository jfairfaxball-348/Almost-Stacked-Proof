# S01499: fair scheduling does not alter the mathematical predicate

Universal ASH*-STACK remains OPEN. This is a complete finite reduction/tool
argument, not the universal comparison. Credit90/94/95 and the earlier source
independent-set lower bound and legal-history semantics as in those reports.

Fix n>=2, M>=n+1. Let P be EVERY nonincreasing non-AS n-tuple of total M.
Use95's exact-one selectors s_p, graph variables, and conditional lex
representative restrictions. Let F be this fixed encoding plus independently
verified necessary graph/input clauses from literal histories, complete AS
negative closures at masses M..M+2, connected cuts and independent-set cuts.

**Proposition99.** For ANY order of visiting selectors and ANY native solver
answers during exploration, a fully independently checked unconditional
refutation of F excludes a mass-M loser above L_AS on ALL connected n-vertex
graphs. No other output of the schedule implies exclusion.

Proof. If (G,c) is a countermodel at this mass, sorting c and choosing the
lex-minimal graph under its count-preserving permutations gives a selector
p in the COMPLETE inventory and a graph satisfying F by94/95. This argument
does not inspect, trust or depend on the exploration schedule. Every graph
clause added during exploration is independently reverified as necessary
with its selector guard where applicable, so the implication survives every
addition. Closing p based on an assumption solve changes no formula: no
closed flag or negative selector literal is added as a clause.

When all patterns appear closed, a fresh solver on exactly F, with NO
assumptions or prior learned clauses, can produce a candidate refutation.
The exported CNF is compared exactly with the independently reconstructed
encoding and deduplicated graph clauses. Every retained proof addition is
then verified by a separate positive-clause-id RUP checker from these CNF
clauses, through the empty clause. This proves F inconsistent, contradicting
the assignment above. A native scheduling error can waste work or cause a
failed final solve; it cannot prove the checked formula inconsistent. QED.

Conversely, a scheduling cap, incomplete pattern visits, conditional UNSAT
answers or unchecked final proof supply no exclusion. Round-robin visitation
prevents phase preference alone from repeatedly selecting a single pattern,
but DOES NOT establish graph coverage or that any pattern is mathematically
closed. Only the complete unconditional proof establishes such a result.
This remains a finite reduction for each fixed(n,M), not a universal proof.
All independent human/kernel and novelty review remain pending; S014 ACTIVE.
