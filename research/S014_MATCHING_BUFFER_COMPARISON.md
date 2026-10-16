# S01480: matching buffers and the remaining universal obstruction

Status initially UNDER_ADVERSARIAL_CHECK. This is a candidate complete proof,
whose precise finite challenges are preregistered in CAM-S014-11. It is not a
universal ASH* conclusion, novelty verdict or kernel certification.

Let a,b>=1 and m>=2. G(a,b,m) has independent parts A,B of sizes a,b,
auxiliary pairs x_i y_i (1<=i<=m), all edges from B to A and every auxiliary
vertex, and exactly the m auxiliary edges besides these. Define

    T=max(3b+1,3a+4m+1).

**Candidate theorem80:** STACK=CLEAR=T, and both goals have an AS critical loser.
The m1 case is theorem79 with its potentially different CLEAR threshold. The
b1,m1 case retains S008 F_a attribution. The new argument below concerns m>=2.

## An all-target AS lower, with no unexplained impossibility claim

For the 3a+4m term, put 2a+2m+1 at r in A, one at each other A vertex and
every auxiliary vertex, zero at B. This is AS of total3a+4m. Collapse B to one
vertex z. This is an actual graph homomorphism, so a win would push to a win
in the quotient; only this lower-bound direction is used.

Give z weight1 and every other vertex weight2. Initial weight is6a+8m.
Leaf A firings and auxiliary-to-z firings lose3 weight; auxiliary internal
firings lose2; z firings lose0. These are exact additive losses on every legal
move. Every vertex outside the final pile must empty. In any complete history
the terminal root has incoming traffic if any input initially lies elsewhere:
otherwise its untouched pile is separate and the last token of the other
nonempty population could never disappear. This also follows by tracing the
ancestry of that population to the unique final pile.

Every initially odd A leaf that empties has odd incoming count, hence at least1.
If the terminal root is outside A, the sum of A firings is at least2a+m.
After these losses, weight budget is at most5m for all auxiliary losses and
the final pile. A pair initially (1,1) that empties costs at least5: if it has
an internal firing, that costs2 and its last exit to z costs3; if no internal
firing, each endpoint must fire to z, costing6. Extra arrivals only increase
these necessary counts. Terminal z is therefore impossible, since all m pairs
empty and a positive final weight remains.

For terminal q in an auxiliary pair, the other m-1 pairs cost at least5(m-1),
leaving at most5 for the active pair's losses and final weight2K. If K>=3
the final weight alone exceeds5. For K2, an internal firing costs2, already
exceeding the budget with final4; without one the other endpoint exits to z,
costing3. For K1 the terminal root has incoming, and therefore fires at least
once (its initial count is1). Two internal firings cost4, exceeding5 with the
final2. Exactly one internal firing requires an exit to z as well: if it
points to q, q's own firing must exit to z; if it points away, the other
endpoint must ultimately exit. These costs2+3+2 exceed5. With no internal
firings both endpoints fire to z, also exceeding5. All positive K are covered.

If the terminal root is an A leaf and its pile is K>=1, let delta=2 for odd K,
delta=1 for even K. Its incoming is at least delta, by parity and the preceding
incoming observation. Other A leaves each have incoming>=1. Consequently total
A firings are at least(4a+2m-1+delta-K)/2. After those losses and final weight2K,
the budget for the m emptied auxiliary pairs is at most

    5m+(3-3delta-K)/2 < 5m.

They cost at least5m, contradiction. This proves the proposed AS lower against
EVERY root and pile size with legal chronology, not merely a modular invariant.
The independent set B gives the credited AS loser of mass3b whenever b>=2.
For b1 that term is dominated and no singleton independence theorem is needed.
Use whichever of these two explicit AS losers has mass T-1. Thus STACK>=T and
CLEAR>=T, with an actual critical AS candidate if the upper is proved.

## Full two-heavy STACK construction

The only minimal open-neighborhood classes are A and B: every auxiliary
neighborhood contains N(A)=B properly. At any losing mass>=4,67/64 select a
GLOBAL Q then minimum degree P configuration with auxiliary counts0/1 and
at most one heavy vertex in each part. All coordinates and the original graph
remain; there is no graph compression of its threshold.

We prove EVERY configuration of this selected form and mass M>=T STACKs.
Choose r in A and t in B to carry the heavy site if present, otherwise an
occupied singleton if present, otherwise any vertex. Write their counts u,v;
p and q count other occupied A and B vertices, respectively; e counts occupied
auxiliaries, c counts fully occupied auxiliary pairs. Then

    p<=a-1, q<=b-1, e<=m+c, c<=m,
    M=u+v+p+q+e, rho=u mod2, sigma=v mod2.

T>n=a+b+2m: twice T is at least the sum of its two defining terms,
3a+3b+4m+2>2a+2b+4m. Thus these inputs cannot be entirely binary.

First suppose D=p+rho+e-q>=1. Transfer all floor(u/2) pairs r->t, leaving
singleton sets L of size p+rho+e and R of size q. All cross edges exist, and
t is adjacent to every L vertex. Put epsilon=min(c,D-1). Join epsilon of the
occupied auxiliary pairs into disjoint two-vertex blocks; treat other L sites
as singleton blocks. There are |L|-epsilon>=q+1 blocks. Alternate through all
q R sites using q+1 L blocks in one path, leaving other blocks as paths.
Expand blocks into their actual auxiliary edges. This partitions every
singleton into D-epsilon paths with L endpoints. Absorb each from t using the
explicit root/path/return operation of79, spending1 net at t. Final pile K is

    2K=M+v-3p+q-3e-3rho+2epsilon.

If epsilon=c, M>=3a+4m+1 gives2K>=m-c+1+v+q>=1. If epsilon=D-1<c,
there is just one path. Its starting root count R=v+floor(u/2) is at least2:
if v>=1 but R<=1, then v1,u<=1 and every site is binary, contradicting M>n;
if v0, the choice of t forces q0, and R<=1 forces u<=3, giving
M<=a+2m+2<3a+4m+1. Hence K=R-1>=1. The positive final base ensures every
path launch has its required2; no move consumes an unavailable pair.

Now D<=0. Transfer B pairs to r instead. The B singleton side then has
q+sigma sites versus p+e on the other side. Let E=q+sigma-p-e>=rho+sigma>=0.
If E>=1, use B-endpoint alternating paths, ignoring auxiliary internal edges.
They all have actual neighbor endpoints of r. The final pile satisfies

    2K=M+u+p+e-3q-3sigma >=1+u+p+e>=1,

because M>=3b+1 and q<=b-1. All path moves are therefore legal.

If E0, the inequalities force rho=sigma0 and q=p+e. If q0 only the adjacent
two root piles remain, which STACK at mass>=3 by the credited K2 result.
If q>0 and u>=2, transfer all but one A pair to t, retain2 at r, and launch
that pair into a B singleton. Walk one alternating path through ALL q B and
q other-side singletons, ending on the other side, and return to t. This
leaves v+u/2>0 at t, even if t was initially empty. If u0 then v>=2 (otherwise
all input would be binary). Reverse the roles: retain a B pair, transfer its
other pairs to r, launch into an other-side singleton, alternate through all
2q singletons ending in B, and return to r. Final pile v/2>0. These branches
cover both zero roots and the equal-side boundary without spending an absent
root pair. This proves the claimed full two-heavy STACK upper.

If stack(G)>T, choose a critical GLOBAL Q/P loser of mass>=T; it has exactly
the selected structure and the construction wins, contradiction. Thus
stack=T. The lower witnesses prove ASH*-STACK at T-1.

## CLEAR comparison for m>=2

The graph of nontriangular edges H is K(A,B) plus isolated auxiliary vertices;
every B and auxiliary vertex is triangular. If b>=a+2, theorem77 gives
CLEAR=STACK directly, independently of how many auxiliary edges occur.

Suppose b<=a+1. Now S=stack=T=3a+4m+1>=3a+9. If CLEAR>S, its mass-S
losing layer is nonempty by the established above-order threshold convention.
Select a GLOBAL Q/P loser there. It stacks, so55 confines its support to one
H component. An auxiliary singleton would be a pure triangular pile>=4 and
CLEAR, so all input lies in A union B. There is at most one heavy A and one
heavy B by64.

If a B vertex t has count>=4, remove and retain3 there. Remaining mass is
S-3>=3a+6, exceeding the complete-bipartite STACK bound on K(a,b), at most
3a+4 (K11 is smaller). The root t remains occupied, so73 CLEARs the original.
If t has2 or3, A must have a heavy site r with count>=4: otherwise total is
at most2a+5<S. Send one or two pairs r->t until t reaches4. At most2 moves
are needed and r has enough tokens. Retain3 at t, leaving mass at least
S-5>=3a+4, which stacks on K(a,b).73 again CLEARs the entire input after
prefixing those actual moves.

Finally if B has no heavy site, the selected input is AS at an A source,
with all auxiliaries0. Keep any one actual auxiliary pair; the input is an
instance of79's unbounded source-A CLEAR upper at mass S>=3a+9>3a+7. That
literal construction CLEARs it on a true subgraph. Every possible mass-S
loser is contradicted, so CLEAR=S. The STACK AS witness remains a CLEAR loser
at the same critical mass, giving ASH*-CLEAR. No use of55a's gap>=2 is needed.

## Scope and continued direction

The argument compares GLOBAL extrema after supplying a real same-input upper
for its residual class. The auxiliary matching changes the STACK threshold
and removes the one-edge CLEAR gap for m>=2. It does not supply a universal
threshold-preserving twin quotient or a theorem for arbitrary buffer graphs.
In particular an arbitrary auxiliary graph need not have its exact all-input
budget measured by an optimal disjoint path cover. Nonadjacent incomparable
minimal heavy neighborhoods, already present on P4, are outside this proof.
Universal STACK and CLEAR remain OPEN. Continue on these obstructions.
