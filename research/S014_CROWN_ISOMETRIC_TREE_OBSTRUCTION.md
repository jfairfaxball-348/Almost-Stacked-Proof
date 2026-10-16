# S014102: actual obstruction to an isometric-tree extremizer selection

Universal ASH*-STACK remains OPEN. This is a complete infinite-family
counterexample to a PROPOSED STRONGER SUPPORT SELECTION lemma, not ASH*.
Use earlier TreeStack and the source independent-set AS lower, not a new
tree theorem. Independent human/kernel and novelty review remain pending.

Let Cr_k have parts A={a_1,...,a_k}, B={b_1,...,b_k} and ALL cross edges
except a_i b_i, k>=3. It is connected bipartite. Same-part distinct vertices
have distance2, matched opposite vertices have distance3, and every other
opposite pair is adjacent. These distances follow by choosing distinct
indices (three indices suffice). No ambient loops or parallel edges.

**Proposition102.** The maximum earlier TreeStack threshold among ALL
nontrivial isometric subtrees T of Cr_k is

    R_k=max(3k-2,15).

For EVERY k>=5, R_k<3k+1<=stack(Cr_k). Therefore NO globally largest loser
of Cr_k has support contained in ANY isometric subtree, even though101
proves the full bridge for every input whose support does so. This refutes
universal isometric-tree support selection; it does NOT refute ASH*.

Proof. Isometry forces T to be INDUCED: any extra edge between its vertices
would have distance1 in Cr_k and thus also in T. If T uses a vertices of A,
b vertices of B and r matched index pairs, its edge count is ab-r. A tree
has a+b-1 edges, hence (a-1)(b-1)=r<=min(a,b). Both a,b are positive.
Assume a<=b. For a>=3, (a-1)(b-1)>= (a-1)^2>a, contradiction. If a1,
r0, and the tree is a star with at most k-1 leaves; its credited threshold
is at most3(k-1)+1=3k-2. If a2, b-1=r<=2, leaving only b2 or3 (b1
is a star under exchanging sides). For b2,r1 it is P4, threshold15.
For b3,r2 it is P5. Its two B endpoints have tree distance4 but ambient
distance2, so it is NOT isometric. No other shape is possible.

Both upper possibilities are attained: every full vertex neighborhood is an
isometric star with k-1 leaves. On {a_i,a_j,b_j,b_l} for three distinct
indices i,j,l, exactly the matched a_j b_j edge is missing, giving an
isometric P4 (the missing opposite pair really has ambient distance3).
Thus R_k is exact, including k3/4.

A whole independent part of size k supplies the earlier AS loser

    (2k+1)e_(a_1) + sum_(i=2..k) e_(a_i), mass3k.

The credited independent-set theorem proves its loss against EVERY ambient
root/move. Thus stack(Cr_k)>=3k+1, strictly greater than R_k for k>=5.
If a globally largest loser c were supported on an isometric T,101's exact
equivalence would imply |c|<=stack(T)-1<=R_k-1<3k. But the displayed AS
loser already forces its globally largest mass to be at least3k. This is
a contradiction. QED.

For k5, max isometric-tree threshold15 while stack>=16; the displayed AS
input has counts(11,1,1,1,1) on A and zeros on B. Its support cannot lie in
an isometric tree: a tree containing all A labels would need all their
pairwise distance2 paths, incompatible with the shape classification.
Actual graph/configuration, not abstract masks, defeats the shortcut.
CAM53 will separately check the retraction algorithm, exact subtree maxima
and one fresh general threshold at a frozen finite scope.

The universal proof still needs to dominate supports with this kind of
cyclic metric interaction. A restriction to isometric-tree-supported losers
cannot settle it. One might combine101 with other retract classes or prove
a different mass-preserving compression; neither is established here.
No CLEAR, later phase, session closeout or future session is executed.
