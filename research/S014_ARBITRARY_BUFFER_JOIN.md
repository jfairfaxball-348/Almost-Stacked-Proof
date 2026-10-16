# S01481-82: causal path covers and arbitrary buffer joins

Status: complete candidate proof UNDER_ADVERSARIAL_CHECK, followed through from
the matching proof rather than inferred from finite data. Universal ASH* for
arbitrary connected graphs remains OPEN. No worldwide priority/kernel verdict.

## 81. A necessary path-cover inequality from first firings

Let F be any finite simple graph, initially ONE token on each vertex of U and
zero elsewhere. Allow internal legal moves2u->v along F, external arrivals of
ONE token at any vertex (I in total), and external exits removing TWO tokens
at any vertex (O in total). Count every operation, including visits to initially
empty vertices and repeated firings. Let k_v be the number of firings at v,
counting both internal moves and external exits. Histories are finite and legal.
theta(U) denotes the minimum disjoint simple path cover of F[U], zero if empty.

If F ends empty, then

    theta(U) <= 2I-O.

If F ends in a single pile K>=1, and its root q either starts empty or has
incoming traffic, then

    theta(U) <= 2I-O-1.

The incoming proviso is essential: an untouched initial singleton is not the
conclusion of the nontrivial all-input histories where the lemma is used.

Proof. Write e=|U|. Each internal firing decreases F's mass1, each exit2, each
arrival increases it1. Thus the total number of firings is e+I-O-K, with K0
for an empty end. Every initial U vertex that empties fires at least once.
For each such vertex select its FIRST incoming token before its first firing;
it exists because its initial count is1. An internal parent u has already
fired before the child's first firing, so the selected arcs between U vertices
are acyclic. Every selected target has indegree at most1. At most I selections
come from the exterior, and at most sum_{v outside U}k_v come from initially
empty vertices. A U vertex is the selected parent of at most k_v targets,
because each firing produces at most one token. Delete excess outgoing arcs,
at most sum_{v in U}(k_v-1). The remaining arcs form disjoint simple directed
paths on U, including isolated vertices, and therefore a genuine path cover
in F[U]. Parallel arcs cannot share a target, and directed chronological
acyclicity plus indegree/outdegree<=1 also forbids undirected cycles.

For an empty end, the total deletion allowance beyond the I external parents
is sum_{U}(k_v-1)+sum_{outside U}k_v=I-O. At least e-2I+O arcs remain,
proving theta<=2I-O. If all initial U sites fire and final K>=1, the same
calculation gives allowance I-O-K, and theta<=2I-O-K<=2I-O-1.

Only one exception to 'all U fire' is possible: q in U may never fire. The
incoming condition then forces K>=2. Select one incoming parent for q as well;
q has no outgoing firing, so adding it cannot create a cycle. Every other U
site fires. The deletion allowance is now I-O-K+1, giving
theta<=2I-O-K+1<=2I-O-1. This covers root in/outside U, every K, repeated
visits, arbitrary zero sites and arbitrary temporal interleaving. QED.

Equivalently, give F vertices weight2 and its exterior hub weight1. Internal
firings cost2 weight, exits cost3, arrivals cost0. If J is the number of
internal firings, conservation gives J=e+I-2O-K, hence

    loss_inside_F + final_F_weight = 2J+3O+2K = 2e+2I-O.

This is at least2e+theta(U) for an empty end, and STRICTLY larger for a single
terminal pile under the incoming condition. This necessity is the missing
direction; a path-absorption upper alone did not justify it. The extraction
uses actual legal first firings, not balance-only satisfiability.

## 82. Exact thresholds on an arbitrary buffer join

Let a,b>=1 and F any nonempty finite simple graph with NO isolated vertices,
order s>=2. J(a,b,F) has disjoint independent A (a vertices), independent B
(b vertices), and F. Every B vertex joins every vertex of A and F. There are
no A-F edges. This graph is connected and nonbipartite. Put n=a+b+s and

    W(F)=max_{U subset V(F)} (|U|+2theta(F[U])),
    S=max(n+1,3b+1,3a+W(F)+1),
    C=max(S,3a+7).

**Candidate theorem82:** stack(J)=S, clear(J)=C, and BOTH critical ASH* goals
hold, with explicit AS losers at their respective critical masses. Isolates
in F may instead be placed in A before applying the theorem; this statement
assumes a>=1 and does not claim the a0 case. Arbitrary connected graphs are
not of this form, and threshold-preserving completion to this form is unproved.

### STACK lower and every terminal root

The all-ones configuration is a stable AS loser of mass n. B is independent,
giving the credited AS loser of mass3b when b>=2; for b1 that term is dominated.
For W choose a maximizing U, set e=|U|, h=theta(U), and put

    (2a+2h+1)e_r + sum_{v in A minus{r}}e_v + sum_{v in U}e_v.

Its mass is3a+e+2h=3a+W. Collapse B to one actual hub z, a true simple-graph
homomorphism, so a win would push to a win in the quotient. No loop is
collapsed. Assign weight1 to z and2 to all other vertices. Initial weight is
6a+4h+2e. Every A leaf starts odd, and the A leaf input total is3a+2h.
An emptied A leaf needs odd incoming>=1. Thus if the final root is outside A,
the total A firings are at least2a+h, costing6a+3h. Only2e+h weight remains.
For terminal z,81 makes the emptied F cost at least2e+h, leaving no positive
terminal weight. For terminal F, its incoming is necessary because initial
input in A must reach the unique final pile.81 makes its losses plus final
weight STRICTLY exceed2e+h. Both are impossible.

For terminal A pile K, let delta2 for odd K and delta1 for even K. The terminal
root has incoming because some initial U input lies elsewhere; U is nonempty
for a maximizing W since F is nonempty. Parity gives incoming>=delta. The
other a-1 leaves have incoming>=1. Total leaf firings are at least
(4a+2h-1+delta-K)/2. After those losses and terminal weight2K, F's budget is

    2e+h+(3-3delta-K)/2 < 2e+h,

contradicting81 for the empty F. This proves the AS lower at3a+W for every
root/pile/chronology, including initially empty F vertices. Taking the largest
of the three AS witnesses proves stack>=S and supplies its critical candidate.

### STACK upper: the original-input extremal comparison

The minimal open-neighborhood classes are exactly A and B. Every F vertex has
neighborhood B union N_F(v), a proper superset of N(A)=B.67/64 select a
GLOBAL Q then minimum-degree P loser with at most one heavy A site and one
heavy B site and every F count binary. Select roots r,t as in80 and use its
u,v,p,q,rho,sigma notation; U is the occupied F set and e=|U|. At mass M>=S,
M>n ensures an actual heavy site. The inequalities p<=a-1,q<=b-1 persist.

The two-heavy construction80 applies verbatim EXCEPT its matching blocks:
take an actual optimal disjoint path cover of F[U], h paths and e-h edges.
In the B-root branch D=p+rho+e-q>=1, retain epsilon=min(e-h,D-1) of those
edges, breaking paths as necessary. The resulting blocks give exactly
D-epsilon alternating L-endpoint paths through every original singleton.
All moves are true edges and consume every input. The final pile satisfies

    2K=M+v-3p+q-3e-3rho+2epsilon.

If epsilon=e-h, the bound e+2h<=W makes this at least1+v+q. Otherwise only
one absorbing path remains and its root R=v+floor(u/2)>=2: with v>=1, failure
would make all input binary; with v0 the choice of root forces q0 and u<=3,
so M<=a+s+2<3a+W+1, using W>=s+2. Thus K>=1 in every B-root branch.

For D<=0, the A-root alternating paths ignore all F edges and use only the
complete B-to-(A,F) join. Their bound2K=M+u+p+e-3q-3sigma>=1+u+p+e uses
M>=3b+1. If both singleton sides have equal size and the roots are even,
retain one root pair and walk the single balanced alternating path exactly
as80, handling zero roots and an empty buffer separately. No source+3 rule
is applied at zero, and no input is discarded.80's full boundary argument
therefore proves EVERY selected input of mass>=S STACKs. A critical GLOBAL
Q/P loser at mass>=S would contradict that construction. Hence stack=S and
the explicit AS lower proves ASH*-STACK.

### CLEAR lower independent of the complexity of F

STACK supplies C>=S. The additional AS input

    (2a+7)e_r + sum_{v in A minus{r}}e_v, mass3a+6,

is a CLEAR loser for ANY F. Again collapse B to hub z and use weights1/2.
Initial weight6a+12 is0 modulo3. If the terminal root is not in A, odd
emptied leaves force at least2a+3 A firings. For terminal A singleton, that
root has positive EVEN incoming, at least2; the same2a+3 bound holds. Their
loss leaves budget at most3 for all F losses and terminal weight.

Only F-internal firings change weight modulo3, costing2 each. If the final
singleton is outside z it has weight2, so their count is2 modulo3 and at
least2, costing4 already. If it is at z, their count is1 modulo3 and at
least1. F starts and ends empty, so an internal firing also requires at least
one later exit to z; that costs an additional3. Total cost>=5 plus final1
cannot fit in3. All terminal roots are impossible. Thus clear>=3a+7 with
the stated AS lower; this extends the S008 F_a LOWER argument, not its
whole-graph upper or a threshold equality after adding edges.

### CLEAR upper and the gap-one branch

The nontriangular-edge graph H is K(A,B) plus isolated F vertices. Every B
and F vertex lies on a triangle, because F has no isolates. If b>=a+2,
77 gives CLEAR=STACK; S>=3b+1>=3a+7 makes C=S as required.

Suppose b<=a+1 and CLEAR>C. The nonempty mass-C losing layer exists by the
established above-order threshold convention. Select a GLOBAL Q/P loser c.
It stacks since C>=S, so55 confines its support to one H component. A pure
F vertex at mass C>=4 CLEARs, leaving support in A union B. At most one
heavy site occurs in each part. If some B site t is heavy, fire t->x for
any x in F. The result has mass C-1>=3a+6 and lies on the ACTUAL complete
bipartite subgraph K(A union{x},B), whose threshold is at most3a+4. It STACKs.
It has positive x input and positive remaining core input, in distinct H
components.55 therefore forces it to CLEAR. Prefixing the move CLEARs c.

If B is binary, c is AS at an A source with F empty. Keep any actual edge
xy of F and use79's complete source-A CLEAR construction at mass C>=3a+7.
This consumes its entire input on a true subgraph. Both cases contradict
loss, proving CLEAR<=C. If C=S, its STACK AS loser remains CLEAR-losing. If
C>S, the explicit3a+6 CLEAR AS loser has mass C-1. Both ASH* goals follow.
This handles the W5 gap-one cases without an unjustified55a gap>=2 step.

## Attribution, assurance and further universal work

The independence/complete-bipartite bounds, root/path absorption, +3 and
triangle repairs are credited earlier primitives. Selected original October
Hamiltonian necessity6.5 and path-cover absorption6.8, April Hamiltonian
necessity and complete-bipartite8.4 are re-inspected;81 must be compared at
its full boundary/root/empty-vertex scope, not claimed new from a term search.
Limited primary comparison is not a worldwide priority/equivalence verdict.

CAM12 independently computes W by TWO complete algorithms and all general
losing layers on146 fixed graphs. All146 STACK thresholds match S;286 of292
goal cases reach an exact threshold, while six CLEAR cases remain incomplete
at their registered STACK cutoff.
Those six are UNKNOWN beyond that cutoff until separately registered work.
These finite checks do not prove82;81 and the full all-parameter proof do.

Continue S014 toward the universal extremal comparison:82 pays every buffer
and root cost for two ADJACENT minimal heavy classes with this complete join.
Arbitrary connected graphs have nonadjacent incomparable minimal classes and
partial/private neighborhoods. Completing them to a join adds winning moves
and cannot justify an upper for the original graph. Neither a threshold-
preserving completion nor a universal loss-preserving concentration is proved.
