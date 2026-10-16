# S01494: representative existence for input-fixed graph symmetry

This is elementary finite-orbit minimality and standard lex-leader symmetry
breaking, not a novelty or universal ASH* claim. All graph vertices remain
labeled. Let c be fixed on n>=2 sites; let Gamma be ALL permutations preserving
each c coordinate. It is a finite group. A graph edge vector is ordered by
the fixed lexicographic list of unordered vertex pairs, with bit0<bit1.

**Proposition94.** If a connected graph exists on which c loses and every AS
configuration at masses>=|c| wins, such a graph exists whose edge vector is
lexicographically no larger than its image under EACH of ANY specified finite
list of elements of Gamma. In particular the list may consist of adjacent
transpositions inside every equal-count label class.

Proof. Take a hypothesized graph G and its finite Gamma orbit. Choose a graph
H in that orbit with minimum edge vector. Every specified permutation sends
H to another graph in the same orbit, so its vector is no smaller than H's.
Relabeling preserves simplicity/connectivity and sends any legal consuming
history bijectively to a legal consuming history. It fixes c, and maps the
entire AS family at each mass bijectively to itself. Thus H retains precisely
the hypothesized original loss and universal AS-tail wins. QED.

No claim that the selected list eliminates every duplicate model is needed.
Its constraints need NOT hold for every labeled countermodel; their guarantee
is existence of a representative. Necessary graph-certificate clauses still
hold for H because they hold for EVERY original-class countermodel. Hence
UNSAT after adding the proved representative constraints excludes the whole
fixed-input graph class. This differs logically from claiming every symmetry
clause itself necessary on every labeling. Both validator flags are distinct.

## Exact local CNF extension, without constraining actual edge assignments

For one transposition pi (its inverse is itself), let a_i be edge bit i and
b_i its permuted edge bit. Introduce fresh prefix variables p_0,...,p_m.
Require p_0=true and for i=1,...,m:

    p_i <=> (p_(i-1) AND (a_i=b_i)),
    p_(i-1) => (a_i<=b_i).

For ANY assignment of actual graph edges, the equivalences determine a UNIQUE
prefix assignment, by induction. The guards hold iff at the first unequal
edge bit, a is0 and b is1, or no difference exists. Thus a prefix extension
exists iff a<=lex b. Different transpositions have disjoint fresh prefixes;
their simultaneous extension exists exactly when all required comparisons
hold. The group argument above supplies it for a representative countermodel.

One implementation uses the guard plus five clauses for each equivalence;
tautologies may be removed and literal repetitions contracted. The independent
checker does not trust that construction: for every local block it enumerates
EVERY valuation of its actual local variables (including any a_i=b_i alias),
and verifies its precise truth function equals the displayed equivalence and
guard. It independently checks the true initial prefix, disjoint fresh ids,
all pair/transposition mappings, complete block coverage and no extra clauses.
This local exhaustive truth table plus the written induction proves the
whole CNF existential extension. It is not a graph census or an assumed
symmetry heuristic. Complete independent UNSAT replay is still required.

Application remains restricted to fixed-input counterexample searches. Neither
the symmetry lemma nor an UNSAT result for a finite list of input types proves
L_all<=L_AS for arbitrary configurations/orders. S014 remains ACTIVE.
