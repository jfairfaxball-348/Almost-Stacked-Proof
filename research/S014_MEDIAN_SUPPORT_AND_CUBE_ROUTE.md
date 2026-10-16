# S014104: triple-median supports and the hypercube residual domain

Universal ASH*-STACK remains OPEN. This is a complete consequence of101 and
the EARLIER TreeStack formula, source homomorphism/path/AS bounds and ordinary
graph metric facts. No new TreeStack theorem, human/kernel or priority claim.

Let G be finite connected bipartite. A median of three vertices a,b,c means
a vertex m satisfying d(a,b)=d(a,m)+d(m,b), and the other TWO analogous
equalities. Multiple medians are allowed. Call G modular here if EVERY triple
has at least one median; no unproved structural characterization is used.

**104a.** Any input whose positive support consists of at most three vertices
and whose three labels admit a median satisfies the bridge

    c loses ==> |c|<=L_AS(G).

For support2 use101's geodesic. For three distinct labels take shortest paths
from m to each. Two arms cannot meet beyond m: such a common vertex would
give a shorter path between the corresponding terminals than their median
equality permits. The union is a tree, possibly a path if m is a terminal.
Each arm is geodesic. Any ambient shortcut between points on different arms
would, by adjoining the two remaining terminal segments, shorten the relevant
terminal-to-terminal distance, again violating a median equality. Thus the
union is an ISOMETRIC subtree containing the whole support. Apply101,
retaining arbitrary coefficients and every original input. A nonzero one-site
input is already stacked; mass0 obeys the numeric inequality trivially.
Consequently EVERY loser supported on at most THREE sites obeys the bridge
on EVERY modular bipartite graph. Larger supports are not covered.

**104b.** On the d-dimensional cube Q_d, d>=1, every loser supported on at most
three sites has mass<=2^(d+1)-2. This mass is attained by an AS one-bit loser
on antipodes by100/earlier source path lower, so it is an actual domination
result with the correct unrestricted root quantifier.

Proof. Vertices are binary d-tuples, true edges differ in ONE coordinate,
and graph distance is Hamming distance. Bitwise majority is a median of any
triple: in each coordinate the minority terminal differs from the majority,
giving exactly the pairwise distance decompositions. The isometric tripod
in104a has at most d edges. More generally ANY isometric subtree of Q_d has
at most d edges: two distinct tree edges lie together on some tree path;
if their cube-coordinate labels repeated, that path's endpoint Hamming
distance would be strictly smaller than its tree length. Hence all tree
edges use distinct cube coordinates.

The earlier tree estimator on any m-vertex tree has maximum at most2^m-1,
with equality for P_m. Here is a complete elementary bound from its formula,
not a new proof of stack=estim. For a chosen root, if a vertex x has at least
two children, move one whole child subtree B from x to a leaf z in another
child subtree. The root score rho+leaf changes at x by -2^depth(x), at z
from off-root leaf contribution1 to2*2^depth(z), and at each weighted
internal B vertex by a nonnegative increase from its larger depth. All B
leaves remain leaves and their contribution1 is unchanged; the parent
replacement leaves B's vertex degrees unchanged. Root x is always counted,
even if it becomes a one-child root; a nonroot branching x remains internal.
Thus the score strictly increases because depth(z)>depth(x). A maximum
rooted score among finitely many rooted m-vertex trees can have no such
branch and must be a path rooted at an endpoint. Direct substitution in
the credited formula gives threshold2^m-1. This covers m2 and all larger m.

Every relevant cube subtree has m<=d+1, so its largest losing mass is at
most2^(d+1)-2. 101 transfers this bound to any supported input in the whole
cube. The antipodal AS loser has source2^(d+1)-3 and one opposite pebble,
mass2^(d+1)-2, including d1's two singleton inputs. QED.

## Why Q4 is a precise remaining challenge

For Q4, n16, all two-/three-site inputs of mass>=31 therefore STACK. The
distance AS lower is30. The general statement stack(Q_d)=2^(d+1)-1 remains
UNPROVED here beyond previously certified small cases; it is not inferred
from104b or finite cube3 agreement. On Q4 a completely certified AS tail
31/32/33 would give L_AS30. Any freshly certified general loser of mass>=31
would then be an actual universal ASH* counterexample. Such an input would
necessarily occupy at least FOUR sites. Conversely a finite sample of
winning larger-support inputs would not prove the general upper.

CAM57 first preregisters the complete AS-tail test with explicit cube
automorphisms. General-input search requires a separate written plan after
that exact tail status is known. No partial tail or failed schedule is an
ASH* result. S014 stays ACTIVE, CLEAR deferred and all later phases gated.
