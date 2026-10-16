# ACTIVE S01492: compatible extremal graph and input normal form

Universal ASH*-STACK remains OPEN. This is a complete conditional structural
reduction, not an unrestricted proof or counterexample. Known graph/pointwise
homomorphism monotonicity,49 and66 retain credit; no priority/kernel claim.

Assume a STACK ASH* counterexample exists. Choose one G of MINIMUM vertex
count n, then MAXIMUM edge count among counterexamples of that order. Both
choices exist: natural n is well ordered and finitely many simple graphs have
that fixed order. Let M=L_all(G), A=L_AS(G)<M and d=M-A>=1. Earlier exact
small cases exclude n2/3, so n>=4 and M>=n>=4. Choose c of mass M first with
minimum heavy count, then maximum Q, then minimum degree-weight P as in89.

**Proposition92.** All the following hold SIMULTANEOUSLY for that actual pair:

1. c has at least two heavy sites with distinct, incomparable inclusion-minimal
   open neighborhoods. Every fewer-heavy input of mass M wins on G, including
   all H2r candidates, even those decreasing Q.
2. EVERY proper edge supergraph H on the same vertices satisfies ASH*-STACK,
   and stack(H)<=A+1=stack(G)-d. Thus adding ANY missing edge lowers the actual
   threshold by at least d and makes EVERY mass-M input win, including the
   ENTIRE critical losing layer of G, not just c.
3. Every eligible proper homomorphic vertex quotient has strictly smaller
   threshold (the established49 consequence of vertex minimality).
4. Every critical loser x has x_v>0 whenever N(v) subseteq N(w) for some
   distinct w. Hence every zero site has an inclusion-MAXIMAL neighborhood
   and no false twin. In particular every member of a nonsingleton false-twin
   class is positive; c has at most one heavy there and ALL others exactly1.

Proof of1. A largest AS loser does not have mass M by the assumed counterexample,
so minimum heavy count is>=2. Proposition89 proves the neighborhood statements.
Any same-mass input with fewer heavies would contradict the minimum. This is
not a choice of independently assigned winner/root sets.

Proof of2. H is connected and has more edges with the same n, so it cannot
be a counterexample by the MAXIMUM-edge choice of G. Its ASH* is a logical
minimality consequence, not an independent literature theorem or computation.
Every H loser, including every AS loser, also loses on G because a G winning
history remains legal in H. Hence L_AS(H)<=A. ASH* for H gives
stack(H)=L_AS(H)+1<=A+1. Since stack(G)=M+1, the drop is at least d. Every
mass-M H input wins by exact-layer/above-threshold monotonicity. QED2.

Proof of3. H has fewer vertices and satisfies its goal by vertex minimality.
Established49 gives stack(G)>=stack(H), with equality lifting a critical AS
loser upstairs and contradicting the assumed failure. Hence strict drop.
This does not assert arbitrary deletion or contraction preserves the model.

Proof of4. Suppose a critical loser x has x_v=0 and N(v) subseteq N(w) for
distinct w. These vertices are automatically nonadjacent: otherwise
w in N(v) would force the forbidden loop w in N(w). Delete v to obtain H.
It is connected: replace any path segment u-v-z by u-w-z and remove repeated
vertices; neighborhood inclusion makes the replacement true. Its order
remains>=2. The map f(v)=w
fixing other labels is a surjective TRUE simple-graph homomorphism G->H.
Since x_v=0, its pushforward is exactly the same input on the remaining
vertices, with no pile changed at w. If that H input stacked, the literal
history would also be legal on G leaving v empty, contradicting x's loss.
Thus H has a mass-M loser, so stack(H)>=M+1. The homomorphic threshold
inequality gives stack(H)<=stack(G)=M+1. Equality contradicts3. This proves
positivity for ALL critical x. The contrapositive makes every zero neighborhood
maximal and unique. Combining it with1's at most one heavy per equal-neighborhood
class leaves every other member exactly1. QED.

There is no assumption that a fixed c remains P-selected when edges are
added: degrees and P can change. For clarity about91's conservative warning,
if a chosen minimum-heavy/Q-maximal critical c DOES survive an edge addition,
its minimum heavy count and Q extremality actually persist, because the
losing set only shrinks and c remains in it. P-minimality need not persist.
The global min-vertex/MAX-edge selection above avoids that issue entirely
and gives the stronger ALL-critical-layer conclusion in2.

## How this advances the actual proof obligation

The empty coordinate supplies a genuine exact threshold equality for every
one-vertex open-neighborhood retraction, not just identical twins. In the
selected c, heavy sites are neighborhood MINIMA, zero sites are unique MAXIMA,
and every vertex strictly between comparable neighborhoods is a singleton.
Repeated false-twin binary buffers must all be actual singleton inputs.
Primitive regular graphs with all neighborhoods
minimal remain fully eligible, so this is not a complete reduction to joins,
trees or one cyclic family.

The remaining task is to prove the ALL-root/ALL-critical-layer witness family
in1-2 incompatible with c's loss, or find a genuine graph realizing it with
no AS critical loser. Individual private-exit deficiencies/essential cuts
still do not provide that contradiction. Computations which saturate one
arbitrary-layer loser certify only that narrower property until actual
criticality/full threshold is independently established. S014 remains ACTIVE.
