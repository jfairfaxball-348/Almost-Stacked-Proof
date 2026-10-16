# CAM-S014-12: arbitrary binary buffer graph versus path covers

2026-10-15, prior to all computation. Test a proposed EXTENSION, not a theorem.
Let J(A,B,F) be the join of independent B with disjoint independent A and F.
a,b>=1; F has no isolated vertices. All A-B and F-B edges, only F's own
internal edges otherwise. Test every LABELED simple F of order2,3,4 with no
isolates, each (a,b)=(1,1),(1,2),(2,2), plus F=P5,C5,K1,4,K5, each (1,1),(1,3).
No isomorphism/symmetry reduction. Record labeled adjacency exactly.

For each occupied subset U of F let theta(U) be its minimum number of disjoint
simple paths covering every U vertex, singleton paths allowed, theta(empty)=0.
Compute W=max_U(|U|+2theta(U)) by Hamiltonian subset DP; independently verify by
enumerating EVERY edge subset whose degrees<=2 and which is acyclic. These are
distinct complete algorithms on these fixed size<=5 F inputs.

Candidate STACK upper/equality T=max(n+1,3b+1,3a+W+1). n+1 is essential: a
large dense F with many B singletons need not satisfy the former matching-only
T>n argument. Replacing the matching by arbitrary F may make this upper
nonsharp; do not use a path cover as a necessary condition without proof.

For both goals compute EVERY general losing layer1..T via unchanged packed
all-predecessor implementation. Independent unchanged tuple canonical-parent
checker compares each full losing set and all roots/AS/Q. Its wrapper removes
ONLY the former proposed-AS-bound inequality and expected-equality assertion
L_AS=proposed_T-1, so an earlier threshold, smaller AS bound, or a CLEAR AS loser
at the last registered layer is recorded rather than rejected as an expectation.
It retains exact layer completeness, exact threshold and independently observed
AS max. CLEAR may not reach an empty layer by T: explicitly UNKNOWN beyond T.
Caps5M candidate,1M loser per layer,600s/2GiB per process, n<16,mass<256.
First replay and compare both W computations before threshold execution.

Freeze all plans/inputs/code/import/runtime hashes. Retain exact full losing
sets, logs and all mismatch cases. Any g_STACK<T refutes the proposed exact
path-cover formula, not ASH*. Equality on this finite set is not an all-F proof.
No expansion beyond these graphs, novelty, session closeout or later gate.
