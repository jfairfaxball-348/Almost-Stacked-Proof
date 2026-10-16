# S014101: all isometric-tree-supported inputs satisfy the bipartite bridge

Universal ASH*-STACK remains OPEN. TreeStack arXiv:2609.31811 and its
registered package are the EARLIER theorem stack(T)=estim(T), used below,
not rediscovered. Graph retraction/Helly facts are established graph theory;
Bandelt, Absolute retracts of bipartite graphs (1987), DOI
10.1016/0166-218X(87)90058-8, abstract inspected, is a primary background
trail, NOT a whole-paper proof audit. Complete elementary proof is supplied.
All human/kernel and worldwide novelty review remain pending.

## Source correction and the geodesic specialization of100

The current April primary text (SRC0002), SHA256
e28470bb90f082f8cf92fc08ea810e3f34a5f7c119dee31d4d0ce1dad595c89d,
was re-inspected at Definition7.2/Theorem7.3 and Theorem7.4 lower proof.
7.3 ALREADY states that N at one endpoint and one at the other on P_(d+1)
loses when N<2^(d+1), N=2^(d+1) modulo3. Thus100's zero-imbalance row on
paths and its extremal endpoint witness are SOURCE-STATED earlier results.
100 supplies a separate ancestry proof and all three positive-source residue
cutoffs on arbitrary bipartite graphs. No unqualified new-result claim.
April7.1(1)'s move pushforward is valid; the printed threshold direction
in7.1(2) is reversed, as already corrected in S009/S01049. We use the
move pushforward and the CORRECT direction stack(G)>=stack(H).

If P is any geodesic s-to-t path of length d in connected bipartite G,
let j(v)=dist_G(s,v), and define

 f(v)= j(v) if j(v)<=d; otherwise d-((j(v)-d) mod2).

Regard f(v) as the vertex at that index on P. Adjacent G vertices have
distance levels differing EXACTLY1, so their images are consecutive path
vertices, including the folded tail. Along the chosen geodesic, j is the
path index, so f FIXES P pointwise. No adjacent vertices collapse to a loop.
This is a retraction. Any whole-input win supported on P pushes to the
identical path input; conversely a path win runs inside G. This proves the
exact all-input equivalence, not merely a lower bound for one special input.

##101. The same bridge for every isometric subtree

Let T be a nontrivial isometric subtree of finite connected bipartite G:
dist_T(u,v)=dist_G(u,v) for all u,v in T. Then T is a RETRACT of G. For ANY
input c supported on T, with arbitrary nonnegative counts and arbitrary
heavy/binary buffers, c STACKs in G iff it STACKs in T. Consequently

    c loses in G ==> |c|<=L_all(T)=L_AS(T)<=L_AS(G).       (101)

The middle equality is earlier TreeStack, with its exact n>=2 threshold
convention. This is the desired universal inequality on a precisely stated
UNBOUNDED input subdomain; it does not cover arbitrary supports.

Proof of retraction. Fix a root of T and align its bipartition with G.
Initially f is identity on T, a color-preserving1-Lipschitz map by isometry.
Extend f one G vertex x at a time, maintaining

    dist_T(f(u),f(v))<=dist_G(u,v)

for ALL already mapped u,v, not just neighbors. For every mapped u form
the integer-radius tree ball K_u=B_T(f(u),dist_G(x,u)). These balls pairwise
intersect: their center distance is at most dist_G(u,v), which is at most
dist_G(x,u)+dist_G(x,v), and the integer tree path meets the two balls.

Finite connected subtrees of a tree have the Helly property. For completeness,
root T; let p_K be the vertex of a subtree K nearest the root. Choose K with
p_K deepest. For any other subtree L choose z in K intersect L. Both p_K
and p_L lie on the root-to-z path, with p_K between p_L and z. The path
inside L therefore contains p_K. Hence p_K lies in EVERY subtree. Applying
this to the balls gives a common vertex y.

If y has x's required bipartition color, take f(x)=y. Otherwise for EVERY
mapped u, the integer dist_T(y,f(u)) has the OPPOSITE parity from
dist_G(x,u), because f preserves color. It is therefore at most the latter
radius MINUS1. Any true T-neighbor z of y belongs to all these balls by
the triangle inequality and has the required color. Such a neighbor exists
because T is nontrivial and connected. Take f(x)=z. In either case all old
distance inequalities and colors are preserved. Finite induction extends
to all G. Adjacent G vertices map to distinct opposite-color vertices at
distance at most1, hence to a TRUE edge of T. Identity on T persists, proving
retraction with no loops or relaxed one-token deletion.

Push any G winning history of c along f. Its initial vector is unchanged,
and every legal move and final positive pile pushes correctly, even if
intermediate G labels lie outside T or merge under f. This gives a T win;
inclusion gives the converse. If c loses, its mass is at most the exact
largest tree losing mass. Lift a TreeStack critical AS witness from T to G
by setting all other sites zero. A G win would push to the forbidden T win,
so it is still AS and losing in G. This proves (101). QED.

## Exact remaining obligation, including an immediate adversarial warning

Any critical loser with support in an isometric subtree proves ASH*-STACK
on its ambient bipartite graph. In particular every TWO-site loser satisfies
the bridge, since a shortest path joins its support. A bipartite counterexample
cannot have ANY critical loser with such support, not just the chosen Q/P one.

This is not a spanning-tree upper theorem: arbitrary spanning trees are
usually not isometric, and inputs cannot be discarded outside T. Nor can one
assume a critical support lies in an isometric subtree. The crown graphs in
102 actually refute that stronger selection assertion. Thus101 must be used
as a reduction with its remaining cyclic/branching support domain intact.
The one-bit diameter lower in100 is also a direct SOURCE-based corollary of
the geodesic retraction and April7.3; it is not evidence of new priority.

As a small exact consequence, bipartite graphs with stack<=15 satisfy ASH*:
if the graph is not complete bipartite, a missing opposite-part edge has
distance>=3, so100 gives L_AS>=14. With L_all<=14 equality follows whenever
L_all14; if L_all<14 the lower is impossible. Complete bipartite graphs use
the prior source threshold/independence result. This bounded-threshold
criterion is not a universal bound on stack. S014 remains ACTIVE.
