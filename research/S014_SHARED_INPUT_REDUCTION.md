# S01495: exact finite mass-layer reduction, with shared graph obstructions

Universal ASH*-STACK remains OPEN.95 is an elementary finite selection/CNF
reduction, not an unbounded graph theorem or a claimed new SAT principle.
The credited independent-set AS witness12 and AS-tail90 are used at their
actual scopes. No later phase or independent human/kernel assurance inferred.

Fix integers n>=2 and M>=n+1. Let P be EVERY nonincreasing nonnegative
n-tuple of sum M having at least two heavy coordinates. Select exactly one
p in P. All unordered graph edges are Boolean variables. For the selected p
add the exact necessary graph clauses from literal p-winning histories,
complete AS-negative supergraphs, and proper connectivity cuts. A p-winning
clause is guarded by 'p is not selected'; AS/cut clauses apply globally.
Comparison constraints under any finite list of permutations fixing p may
be imposed conditional on p, using94's exact prefix extension. Auxiliary
equivalences may be unconditional: every edge assignment has their unique
extension, even for unselected comparisons. Only their lex guards restrict
the selected case. Exactly-one selection has its literal standard CNF.

**Proposition95.** If a connected graph on n vertices has a mass-M loser c
and EVERY AS input of mass>=M wins, the resulting finite necessary-clause CNF
has a satisfying assignment. This remains true for ANY finite set of the
stated sound certificate clauses.

Proof. c cannot be AS, since it has mass M. Permute its labels into the
nonincreasing tuple p in P, carrying its graph along. Then choose a graph
representative in the full group of permutations fixing p by94. It still
has p losing and all AS masses>=M winning. Thus all graph-global AS and cut
clauses hold, as do every p-guarded winning clause: an actual winning history
whose every edge was present would contradict p's loss. Clauses guarded by
unselected patterns hold automatically. Its graph representative has the
required lex comparisons for p. Prefix equivalences for every pattern have
a unique extension, so they introduce no additional constraint on unselected
cases. The selected representative extends to a full satisfying assignment.
This proves the implication without claiming that every labeled countermodel
obeys the symmetry clauses. QED.

Consequently a COMPLETE independently verified UNSAT proof excludes exactly
that finite (n,M) countermodel class. By90 any actual potential is tested by
all AS layers M,M+1,M+2, with full consuming certificates. Neither outcome at
one (n,M), nor any finite list of such pairs, proves universal ASH*. A SAT
model of NECESSARY clauses is not itself a counterexample until its selected
input loss and entire AS tail have been independently established.

## A theorem-derived initial family of graph clauses

Set k=ceil(M/3), assume2<=k<=n. If U has k vertices and no edge inside it,
the audited AS independent-set witness from S00412 has(2k+1) at one U vertex,
one at each other U vertex, and zero elsewhere. Its mass is3k>=M. It loses
on ANY simple graph in which U is independent, including arbitrary edges
outside U. Hence every countermodel must have at least one actual edge in
EVERY k-subset. These global positive clauses need no fresh negative DAG:
their mathematical justification is that complete credited universal proof.
The independent checker verifies each finite instantiation, not a solver's
claim that U was independent. At the chosen k,3k<=M+2, so the witness is
within the same three-layer tail90. Other k outside the stated range are not
silently instantiated. This lower bound is prior work and not rediscovered.

## Complete finite validation obligations

The producer enumerates P recursively by descending parts. The separate
checker constructs the same finite set by a partition/multiplicity dynamic
program; equality and uniqueness establish complete pattern coverage, not
sampled representatives. It verifies each selected history at its exact
pattern and every graph-clause literal, full AS closures, independent-set
instances and cuts. It independently checks selector allocation/exactly-one
CNF, every local conditional-prefix truth table, disjoint fresh variables,
complete full CNF coverage and the explicit existential-extension flag.
Finally a separate pure clause-id RUP checker replays every retained hinted
addition to empty. Native hints and native UNSAT are untrusted. Bounds and
UNKNOWN remain explicit. No proof replaces the actual universal implication.
