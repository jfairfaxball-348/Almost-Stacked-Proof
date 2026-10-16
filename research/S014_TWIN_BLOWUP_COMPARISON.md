# S01479: complete comparison for one-edge extensions of complete bipartite graphs

Status: PROGRAMME_PROVED at the explicit infinite-family scope below, with local adversarial review and bounded independent computational challenges. NOT a proof of unrestricted universal ASH*, a worldwide novelty verdict, or kernel certification. Earlier F_a, complete-bipartite and independence theorems retain their attribution. S014 remains ACTIVE.

## Statement and exact graph

For integers a,b>=1 let G(a,b) have disjoint sets A (size a), B (size b), and vertices x,y. Its edges are EVERY A-B edge, EVERY x-B/y-B edge, and xy, with NO others. Thus it is K(b,a+2) with exactly one edge added inside its larger named part; the part need not actually be larger. It is connected/nonbipartite and has n=a+b+2>=4. Moves consume TWO at a source and create ONE at a true neighbor. STACK consumes all inputs into a positive pile somewhere; CLEAR into exactly one. Thresholds are least exact t>=2, with known above-order monotonicity.

**Theorem79.** For ALL a,b>=1,

    stack(G(a,b)) = max(3b+1, 3a+5),
    clear(G(a,b)) = max(3b+1, 3a+7).

Both critical ASH* goals hold on this full two-parameter family, including ALL arbitrary buffers/roots/configurations, not just its AS inputs. The a=0 family is the already known complete multipartite K(b,1,1), separately credited; the displayed formula is not extended to a0,b1. The b=1 subfamily is precisely the earlier S008 F_a, whose result is USED, not rediscovered.

## Credited lower bounds and structural restrictions

Collapsing all false-twin vertices of B to the triangle root gives a TRUE simple-graph homomorphism onto F_a. No edge collapses to a loop. Winning inputs push forward, so the known F_a AS losing configurations lift to AS losing configurations on G(a,b):

* STACK: (2a+3)e_r + sum_{u in A minus{r}}e_u + e_x+e_y, mass3a+4;
* CLEAR: (2a+7)e_r + sum_{u in A minus{r}}e_u, mass3a+6.

All B counts are0. Their complete F_a weight/chronology proofs are S00836, freshly re-read here; this supplies the lower thresholds3a+5 and3a+7. The independent set B supplies the known AS losing witness(2b+1)e_t+sum_{u in B minus{t}}e_u, mass3b, whenever b>=2 (S00412/April independence bound). For b1 that lower term is dominated by the F_a bounds and is not invoked as a size-one independence theorem.

The only minimal open-neighborhood classes are A and B. Indeed N(A)=B and N(B)=A union{x,y}, while N(x)=B union{y} and N(y)=B union{x} properly contain N(A). Therefore67 selects any fixed-mass GLOBAL Q maximum with minimum degree P, at mass>=4, with NO heavy x/y and at most one heavy site in each of A and B. This preserves the original graph, mass, loss, all input coordinates and roots. It does not assert that arbitrary losers compress by a false-twin graph quotient.

Let H keep the ambient nontriangular edges. Here H is exactly K(A,B) plus the singleton components x,y. Every B vertex is triangular. In a stackable CLEAR loser,55 confines ALL input to one H component; its positive THREE witnesses use only H edges.55a additionally forbids heavy B when M-1>=stack(G).

## A complete path absorption operation

Suppose a heavy root z is adjacent to both endpoints of a path of singleton vertices, the path excludes z, and every singleton is a designated original input. Spend2 at z to create a pair at the first vertex, walk that pair along the path (each destination has its designated singleton), and move the last pair back to z. This consumes EVERY path input and has net cost1 at z. Other designated inputs are untouched. If c disjoint paths are processed and the final root count is K>=1, every operation is legal: before the final path at least K+1>=2 remain. This is the credited path/pullback idea used with explicit actual endpoints, not ordinary pebbling with leftovers.

For two vertex sets L,R with all cross edges, |L|>=|R|+1, there is a disjoint path cover with endpoints in L and exactly |L|-|R| paths: alternate through ALL R and |R|+1 selected L in one path, leave the other L as singleton paths. If x,y belong to L, xy is an edge and |L|-|R|>=2, regard xy as one two-vertex block. The same construction then has one fewer path. Expanding the block retains a simple real path and every original label exactly once.

## AS source-A uppers, with every buffer and parity

Assume b<=a+1, choose r in A, and let its source count be N while all other counts are0/1. Write p for occupied A minus{r}, q for occupied B, e for occupied{x,y}, and rho=N mod2. Thus p<=a-1,q<=a+1,e<=2 and M=N+p+q+e.

**STACK upper:** EVERY such input with M>=3a+5 STACKs, with no upper source cutoff. In particular N>=a+3>=4. If q>0 choose an occupied t in B, otherwise choose any t in B, and put delta=1 or0 accordingly. Sending all floor(N/2) source pairs to t leaves a singleton at r exactly when rho1. The new t count is R=floor(N/2)+delta. Remaining singleton neighbors of t number L=p+rho+e; remaining singleton B vertices number q-delta. Put D=L-q+delta.

If D>=1, use the preceding neighbor-endpoint path cover, with epsilon=1 when e2 and D>=2 (the xy block), otherwise epsilon0. Its path count is D-epsilon and final t pile is

    K=R-D+epsilon,
    2K=M-3p+q-3e-3rho+2epsilon.

For e0 the right side is>=5; for e1 it is>=2; for e2 with epsilon1 it is>=1. Since K is integral, each gives K>=1 and hence all path operations are legal. The remaining e2,D1 case has K=R-1>=1: D1 with e2 implies q>0, and N>=4 implies R>=3. Thus this entire branch ends in a positive pile, including empty residual source r.

If D<=0 and there is no singleton buffer, the input is already stacked. Otherwise q>0 and q>=p+e+rho+1. Keep the ORIGINAL source pile at r instead of performing the previous pair transfer. Cover the singleton buffer by B-endpoint alternating paths; the nonneighbor side has p+e vertices and q>=p+e+1. There are q-p-e paths, leaving

    K=N-(q-p-e)=M-2q >= a+3>=4

at r. Every input is consumed and the preserved positive base makes all path operations legal. This completes the unbounded AS STACK upper.

**CLEAR upper needed later:** EVERY source-A AS input with x=y=0 and M>=3a+7 CLEARs. Use the same construction with e0. In the B-root branch, 2K=M-3p+q-3rho>=7, so K>=4 at triangular t and CLEAR follows. In the A-root branch K=M-2q>=a+5. If K is nonzero modulo3, pure K at r CLEARs by occupied+3 reduction and the final2->one move. If K is divisible by3 and K>=9, complete every path except omit the last path's final return. This leaves(K-1)e_r+2e_t at an actual B endpoint t, total K+1>=10;76 CLEARs it.

The only remaining possibility K6 forces a1,b2,M10,q2,N8,p0. For B={t,w}, the following actual nine-move sequence CLEARs8e_r+e_t+e_w:

    r->t, t->x, r->w, r->w, r->w,
    w->y, w->x, x->y, y->w.

If the A-root branch has no buffer, pure N>=10 CLEARs by76 using any triangular B neighbor. This exhausts zero buffers, both source parities, all p/q counts and every possible final3 exception. No zero-source +3 rule is used.

## Global STACK upper: the actual extremal comparison

If b>=a+2, the spanning K(b,a+2) has STACK threshold3b+1; the independent B lower matches.77 gives CLEAR equality as well. Thus both formulas and AS witnesses are already proved in this range.

Now b<=a+1. Suppose stack(G)>3a+5 and select a critical STACK loser c by GLOBAL Q then minimum degree P. Its mass M>=3a+5. By the proved structural selection above, x/y are binary, A has at most one heavy site and B has at most one heavy site. If at most one of x,y is occupied, c lies on a complete bipartite subgraph with side sizes<=a+1,b. Its mass exceeds3(a+1)+1, so it STACKs by the known complete-bipartite theorem, contradiction.

Thus x=y=1. If a B vertex t is heavy, the two moves t->x,x->t empty x, retain positive input at t, and leave y1. The full resulting input lies on K(A union{y},B), has mass M-2>=3a+3, occupied-support independence<=a+1, and an ACTUAL occupied edge ty. The credited Proposition8.4 equality/edge case makes it STACKable. Prefixing the two moves contradicts c's loss.

Therefore no B site is heavy. The chosen c is AS at an A source, contradicting the complete AS STACK upper for ALL M>=3a+5. Hence stack<=3a+5. The lifted F_a AS loser proves equality and critical ASH*-STACK. This explicitly closes the global arbitrary-buffer comparison on this family; it is not an inference from a finite grammar or a local Q maximum.

## Global CLEAR upper and AS witness

For b<=a+1, STACK is now3a+5 and the lifted F_a CLEAR lower is3a+7. Suppose clear>3a+7 and choose a GLOBAL Q-maximal critical CLEAR loser. Its mass M>=3a+7 stacks.55 confines its support to H; an isolated x/y component would be a pure triangular pile of size>=4 and therefore CLEAR, so its support is in A union B. Since M-1>=stack,55a forbids EVERY heavy B site.64 permits at most one heavy A site because all A open neighborhoods agree. The input is thus AS at an A source, with x=y=0, contradicting the unbounded CLEAR upper just proved. Therefore clear<=3a+7. The lifted F_a AS loser gives equality and ASH*-CLEAR. Together with the already settled b>=a+2 range, this proves79.

## Local adversarial audit, attribution and bounded checks

The proof uses actual critical/global extrema only in the indicated branches; it does not assume every loser is AS, preserve fixed residues, or move graph thresholds through a quotient in the wrong direction. The quotient supplies LOWER bounds only. Equality/edge in Proposition8.4 is essential at M-2=3a+3 and ty is explicitly occupied. The AS upper keeps the root on the correct side, handles empty residual r, and never reduces3 at an empty source. Its positive tail argument covers ALL larger source counts, unlike the refuted printed exact-layer implication. CLEAR's K3 exception is explicitly repaired; the a1,b2 boundary is a literal full-input trace. All triangle repairs consume their whole frontier.

S00836's lower/upper proof and exact AS witnesses were freshly re-read, including the all-target weighted budget and final incoming leaf count. April8.4's exact statement/proof and its repaired STACK wording were inspected at the scope written in the S014 main report. The new proof's direct DAG is79<-S00836 lower lifts/S01049 pointwise push, S01364/67 selection, known complete-bipartite STACK/equality-edge theorem, explicit path absorption and76, with77 in the imbalanced range and55/55a in CLEAR. Earlier TreeStack is a separate credited theorem and not needed here. No Lean or registry build was run.

CAM09 certifies exact AS bounds on seven prescribed balanced examples using70 and TRUE checked source automorphisms, ALL binary buffers/roots/kinds and independent grammar inequalities/attaining DAGs. Its ten full general threshold comparisons on the first five examples agree with79, including the gap2 cases8/10,11/13,14/16. CAM10 independently validates7620 complete AS upper histories/92504 moves, all input keys and exact grammar predictions, including the one K6 boundary case and every path branch. These finite checks corroborate, not prove, the all-parameter theorem.

Novelty is qualified: the b1 case is S008 F_a; the a0 case is the prior complete-multipartite family; all numerical independence/complete-bipartite bounds and generic ancestry/path primitives are credited. Limited selected primary comparison did not identify this full one-edge formula, but no worldwide priority or equivalence verdict is claimed. Universal STACK/CLEAR for ARBITRARY connected graphs remains OPEN.

## Continued universal implication

This result removes an actual two-heavy arbitrary-buffer comparison on an unbounded family, and shows how GLOBAL Q/P can be used after the needed same-input reconstruction is supplied. The unrestricted residual still has incomparable minimal sites with neither this complete bipartite adjacency nor the fixed xy buffer edge. Even general joins replace that one edge by an arbitrary graph of binary buffers; arbitrary graphs may have NONADJACENT minimal heavy classes (P4 already does). Neither quotient equality nor the path cover supplies a universal domination theorem there. Continue S014 on those precise missing implications; this is not a session closeout.
