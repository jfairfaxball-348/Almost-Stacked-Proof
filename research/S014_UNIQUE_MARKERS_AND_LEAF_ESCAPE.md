# S014112-114: unique parity markers and a bipartite critical leaf exclusion

Universal ASH*-STACK remains OPEN. The arguments below retain whole inputs,
every possible root, true edges and repeated graph labels. They use111's
proved boundary-tree equivalence and the credited ancestry/THREE operations;
no new TreeStack equality, independent human/kernel or priority assurance.
This is an actual local mass-ascent theorem as well as a representation,
not the missing full even-heavy/global comparison.

## 112. Normalize all repeated degree-two labels

Let c have mass>=4 and put p_v=c_v mod2, a_v=(c_v-p_v)/2. Then c reaches
THREE somewhere iff111's tree can be chosen with EXACTLY

    a_v degree1 vertices labeled v,
    p_v degree2 vertices labeled v,
    any nonnegative number of degree3 vertices labeled v.          (112)

In particular degree2 labels never repeat. The one-vertex mass3 boundary
3e_v is a SEPARATE base; do not call it a leaf/marker instance of112.

Proof. In any nontrivial H, degree1 contributes2 original inputs, degree2
contributes1 and degree3 contributes0. If two degree2 vertices x,y have
the same label v, take the UNIQUE H path from x to y. Exactly one of x's
two incident edges is outside this path, say x-z. Remove x-z and attach
y-z instead. Its detached component does not contain y, so the result is
still a simple tree; x has degree1 and y degree3. The new graph-label edge
is true because f(x)=f(y). Other degrees/labels stay fixed, and the total
boundary at v stays1+1=2+0. No input is dropped or extra edge in G assumed.
The operation removes two degree2 occurrences. Finite iteration terminates
with0/1 at each label, necessarily p_v by parity. The remaining leaf count
is exactly a_v by111a. Conversely the displayed counts give boundary c,
so111 reconstructs a whole legal THREE history. QED.

Write A=sum a_v and P=sum p_v. A nontrivial canonical H has A leaves,
P markers and A-2 branches; hence A>=2 and |H|=2A+P-2=|c|-2. This is an
exact count identity, not sufficient existence on an arbitrary graph.
All-positive-odd inputs have every leaf label also represented by a marker;
even heavy sites have leaf copies without that marker. This is the actual
distinction in the surviving UNPROVED B_odd route, not an oddness theorem.

## 113. Separate exact THREE from unrestricted STACK at all parities

For finite connected G,n>=2, define T(c) to mean a THREE boundary tree exists
(false for |c|<3). Then for EVERY nonempty c,

    STACK(c) iff T(c) OR (there exists q: T(c+2e_q)).                 (113)

Proof. Normalize a stacked positive pile by occupied-root three-removal to
1,2 or3. A pile2 can make one true move into ONE because its root has a
neighbor. Thus the history gives THREE or ONE. A ONE history at q becomes
THREE on c+2e_q by retaining two extra designated q inputs untouched.
Conversely T(c) is already a stack. If T(c+2e_q), q is an original used
label;111 reroots the three outputs to q, and the credited root-padding
cancellation47 subtracts two original q inputs and outputs (3>2), yielding
c->e_q. No equality cancellation to the empty terminal is used. QED.

Equivalently set W_p={a>=0:T(p+2a)}. A nonempty fixed-parity input p+2a
loses STACK exactly when a AND EVERY a+e_q are outside W_p. These are SET
memberships; W_p is not asserted upward closed under unit increments.
On bipartite G with I(c)=0, all neighbors c+2e_q have nonzero signed charge
and cannot reach THREE, so STACK(c) iff T(c). Nonbipartite graphs require
the entire extra family in113. This explains why a fixed-parity THREE
comparison alone would not settle the full all-graph STACK problem.

## 114. A genuine inverse extension at a graph leaf

First a local witness fact. Let d_v be ODD, d_w>=2, v!=w. If a canonical
THREE tree for d has a degree1 w-labeled vertex y whose neighbor x is
v-labeled, then

    c=d+e_v-2e_w reaches THREE.                              (114a)

Because d_v is odd there is one v-marker z. If x=z it is already adjacent
to y. Otherwise x cannot have degree1: x-y would then be the entire tree,
contradicting the v-marker's existence elsewhere. Nor can x have degree2,
since the unique v-marker is z. Thus x has degree3. Of its three incident
edges, one is x-y and one begins the path to z; these are distinct because
y is a leaf and z is not y. Detach the remaining branch x-b and attach
z-b. The detached component contains neither y nor z, so this preserves
the tree and x-y. Labels at x,z both equal v, so its new edge is true.
Now x is the unique v-marker and z a v-branch. Delete ONLY the w-leaf y.
Then x becomes a v-leaf: its boundary rises from1 to2, and w's boundary
falls by2. Every other boundary contribution is unchanged.111 reconstructs
exactly c into THREE. The mass3 isolated base cannot meet d_v odd>=1 and
d_w>=2 at distinct sites while already reaching THREE, so no base is lost.
This proves114a at unrestricted roots. QED.

**Theorem114b.** Let G be finite connected BIPARTITE,n>=2, c any STACK loser
with signed I(c)=0. If c_v is positive EVEN and w is a graph leaf adjacent
to v, then the whole input

    d=c-e_v+2e_w

also loses, and has mass |c|+1. No requirement c_w>0 or c_v=2 is needed.

Proof. d is nonnegative, d_v odd, d_w>=2 and
I(d)=I(c)-epsilon_v+2epsilon_w=-3epsilon_v=0. If d stacked it would have
a THREE tree by111/113. Its mass3 base cannot apply to these two occupied
sites. Normalize by112. At least one w-leaf exists because floor(d_w/2)>=1.
EVERY w-copy's graph neighbor is v, so that H leaf has a v-labeled neighbor.
114a then reconstructs c into THREE, contradicting its actual loss. Thus d
loses at the larger mass, against EVERY possible final root. QED.

Consequently NO bipartite critical loser has an even heavy vertex adjacent
to any graph leaf, including an initially empty leaf. This is a strict
necessary critical restriction, not universal absence of even heavy sites.
Graphs with minimum degree>=2 remain eligible; no silent core deletion or
threshold-preserving leaf reduction is inferred.

For the already independently negative printed P4 input(9,2,0,1), take v1
and leaf w0.114b yields the actual AS loser(11,1,0,1) of mass13. The four
different even-pair extensions rejected in CAM49 do not include this input;
that old auxiliary failure remains unchanged. Actual P4 L_AS=L_all=14 is
credited separately. This example illustrates the new ascent, not ASH*.

In a hypothetical vertex-minimal universal counterexample,92's leaf
positivity is compatible with this stronger exclusion, but neither supplies
the missing even-heavy argument in a core. The full outstanding tasks are
to extend an actual mass-ascent/compression to core sites and arbitrary
buffers, or certify a genuine counterexample. B_odd and critical oddness
are still UNPROVED globally. S014 remains ACTIVE; no closeout/later gates.
