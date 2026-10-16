# S014 local proof adjudication and continuing universal obligations

Current ACTIVE status, 2026-10-15. This document supersedes the initial
UNDER_ADVERSARIAL_CHECK/candidate labels in the preregistration-time proof
texts, whose bytes remain unchanged because their execution preflights pin
them. The accepted statements are at their EXACT scopes below. PROGRAMME_PROVED
means a complete local written proof, not independent human or kernel review.
Universal STACK/CLEAR remain OPEN. No S014 closeout, commit, PR or S015 handoff.

## Accepted local proof chain

71: protected capacitated multiple-donor reconstruction, with EVERY donor-subset
Hall inequality, true-edge assignments, simple reserved root path and exact
grammar realization. Its consequence for GLOBAL Q losers is a family of
necessary deficiencies, not that the deficiencies are inconsistent.

72: every adjacent1/2 transfer from a stackable CLEAR loser CLEARs, while its
THREE output set remains empty by69. This proves the opposite of the proposed
TR shortcut and is not a loss-preserving concentration theorem.

73: retain3 at an occupied triangular root; if the remainder STACKs, the whole
input CLEARs.74: complete-bipartite input with every initial heavy site triangular
CLEARs at mass>=3alpha(occupied support)+4.75: if all vertices are triangular
and every nontrivial nontriangle-edge component is complete bipartite, then
CLEAR=STACK.76: mass>=10 on adjacent sites, one triangular, CLEARs.77: the
specified imbalanced complete-bipartite components with one actual external
common neighbor also imply CLEAR=STACK.78: the stated K(k,3)+one-edge family,
k>=3, has both thresholds3k+1 and the credited independence AS witness.

79: for a,b>=1, G(a,b) one-edge buffer join has
STACK=max(3b+1,3a+5), CLEAR=max(3b+1,3a+7), both ASH*.80: m>=2 disjoint-edge
buffers have both thresholds max(3b+1,3a+4m+1), both ASH*. These are superseded
as class results by82, while their literal constructions remain dependencies.

81: first-firing extraction proves theta(U)<=2I-O for an emptied initially
binary region, and theta(U)<=2I-O-1 for a single terminal pile whose root
starts empty or has incoming.82: for the exact arbitrary buffer join J(a,b,F),
a,b>=1, F nonempty/no isolates, n=a+b+|F| and W=max_U(|U|+2theta(F[U])),

    STACK=S=max(n+1,3b+1,3a+W+1),
    CLEAR=max(S,3a+7),

and both critical ASH* statements hold with explicit all-target AS losers.
These are complete infinite CLASS comparisons, not universal ASH*.

## Hostile boundaries that were actually checked

81's first incoming precedes the first firing of an initially occupied site;
its internal parent has already fired. Thus selected U arcs are acyclic even
when a parent fires repeatedly. Only the first incoming at each target is
selected; one firing produces only one token. Deleting all but one selected
outgoing arc at each parent costs at most sum(k_v-1) over fired U sites.
Initially empty sites cost their FULL k_v, not just a distinct-site count.
The root that never fires is the only exception: it must have K>=2 if it
starts1 and has incoming. Adding its selected parent cannot form a cycle
because it has no outgoing firing. The algebra changes by+1 precisely there.
An untouched initial singleton is excluded only from the strict terminal
assertion. These facts prove the all-history lemma independently of the finite
representative histories used to corroborate it.

82's lower uses a TRUE B-to-hub homomorphism, LOWER direction only. All A
inputs are odd. The terminal A incoming parity is checked for every K, and a
maximizing U is nonempty. The initially empty F vertices remain in81; no
induced-support approximation discards their use. Terminal F needs incoming
because original A input is nonzero. For CLEAR, the leaf loss leaves budget3,
and internal F firings cost2 modulo3: final weight2 requires at least two;
final hub weight1 requires at least one and a real exit from F. This proves
the3a+6 AS CLEAR lower for every F, rather than assuming the F_a loser survives
an arbitrary edge addition.

For82's upper, n+1 is an actual separate lower term. Without it, a large
clique buffer and many B singletons would invalidate the 'some heavy site'
argument. W>=|F|+2 handles the zero B-root case. Arbitrary path-cover blocks
can be cut to ANY required number of retained edges, then expanded into real
simple paths. Source-even equal-side cases retain a real pair rather than
spending a zero root. All root/pile parities and empty buffers are included.
The B-heavy CLEAR branch needs only one actual move into F followed by STACK
on K(A+x,B), whose threshold is explicitly paid; it uses neither55a's gap>=2
nor a threshold after deleting graph edges. With B binary,79 supplies the
actual full-input CLEAR sequence on any chosen edge of F.

## Source reconciliation and exact assurance

An execution-time citation typo in the82 candidate text calls October's
Hamiltonian necessity6.5. The original2610.09650v1 statement/proof is
**Proposition6.2**, not6.5 (which is the perfect-pebblability corollary).
Definition6.7/Lemma6.8 is the path-cover absorption sufficient condition.
April's concluding Hamiltonian iff is on its original page27. These selected
proofs were freshly read. They supply precedents and credited primitives;
neither quoted statement gives81's arbitrary boundary traffic/empty-site
necessity or82's full exact join formula. No worldwide novelty/equivalence
claim is made. Earlier TreeStack and its registered package remain credited
and separate. No PDF was mirrored and no Lean/registration/publication ran.

CAM11's two full threshold algorithms agree on14 cases, all matching formulas;
66144 separate literal STACK histories/552534 moves and both explicit lower
witness types pass. CAM12's independent W algorithms agree on50 prescribed
labeled F graphs, producing146 join graphs and292 full goal comparisons;
all146 STACK endpoints match82,286 cases finish exactly, six CLEAR cases are
initially incomplete. CAM13 preserves every prior complete layer and finishes
those six at10/10/13 for edge buffers and10/10/13 for triangle buffers. It
checks228 explicit W/independence/order AS witnesses in the old full critical
STACK sets. All146 prescribed graphs now have both thresholds and AS witnesses
checked by complete independent algorithms.

CAM13 separately compares ALL66642 reachable boundary cells by BFS versus a
whole coordinate-box predecessor DP on10 fixed F graphs, all binary inputs
and I<=3. It replays11625 terminal histories and extracts10033 true path covers
in the claimed empty/strict cases. CAM14 independently checks198320 complete
general-buffer STACK constructions/2046597 moves; the n16 K10-buffer case
alone has180224 histories and1896493 moves, with order bound17 strictly
dominating the two other terms16. No resource/candidate/layer/trace cap hit.
Finite checks corroborate the all-parameter written proofs and do not replace
them. Fresh session-external/human/kernel cold review of the new results is
still pending; no formal certification or universal gate promotion.

## 83. Universal rooted AS necessity and the exact universal-hub case

For ANY finite simple graph G of order>=2, source r, U subset V(G) minus{r}, and N>=1,
if N e_r+sum_{u in U}e_u STACKs then N>=theta(G[U])+1.
Proof: put F=G-r. Its I arrivals/O exits are exactly firings from/to r. If
the final positive pile K is at r, root conservation gives2I-O=N-K, and81
gives theta<=N-K<=N-1. If the final pile lies in F, root conservation gives
2I-O=N. Its root starts empty or must receive some of the original r input,
so81's strict inequality gives theta<=N-1. No adjacency completion is used.
For U empty the inequality is just N>=1. N0 is deliberately excluded: an
untouched single original U pebble is already stacked.

If r is UNIVERSAL, the converse holds: choose a minimum path cover of G[U],
absorb each actual path from/to r at net cost1, retaining positive final pile
N-theta. Thus for every N>=1 the exact all-root AS criterion is

    N e_r+1_U STACKable iff N>=theta(G[U])+1.

Consequently the largest root-r AS losing mass is
max_U(|U|+theta(G[U])). Root-zero binary inputs do not enlarge it, since taking
all n-1 off-root vertices gives at least n, while their mass is at most n-1.
This is a ROOTED AS statement, not the full graph threshold or ASH*. Even a
star with k>=2 leaves has universal-center AS maximum2k but credited full
STACK critical mass3k at a leaf. Without a universal root the converse fails:
P4 with edges01,12,23 and input(2,0,0,1) has theta({3})1,N2, yet its only
first move gives(0,1,0,1), a stable non-goal. This exact two-state impossibility
requires no search and is not a critical ASH* counterexample.

## 84. Exact positive-gap classification INSIDE the join class

Within82, CLEAR>STACK iff b<=a+1 and F=K2 or K3. For K2 the gap is2; for K3
it is1. Proof: a positive gap requires W<=5 because S>=3a+W+1 and C=max(S,3a+7).
W>=|F|+2 forces |F|<=3. A no-isolate two-vertex F is K2 (W4); the only
three-vertex no-isolate types are P3 with W6 (its independent pair attains6),
and K3 with W5. Substitution into82 gives the two claimed gaps exactly when
b<=a+1. This gives an infinite genuine gap1 control family beyond a finite
atlas; it does not prove C14 on arbitrary graphs. In these positive-gap
families, ALL critical CLEAR losers have nontriangular heavy support:55
confines them to A-B or a pure F site; the latter CLEARs at these masses.
If B is heavy, its one move into F STACKs on K(A+x,B) already at critical
mass (at least3a+4 after the move), hence CLEARs by55, contradiction.
Thus heavy sites lie only in nontriangular A, without invoking gap>=2.

## What remains and what these results cannot supply

71 constrains each actual concentrating certificate.81 constrains every
initially binary region's traffic.82 discharges the global comparison when
its required paths have the actual neighbor endpoints;83 exposes this as
the exact missing geometric condition, not an abstract integer-balance issue.
An arbitrary connected graph has neither a universal root nor the join's two
complete adjacent minimal classes. Connecting partial/private neighborhoods
can require initially empty intermediate sites and repeated traffic, and
different concentrating winners need not share their deficient subset or root.
P4's simple rooted failure illustrates why completing the graph or suppressing
zeros is invalid. No theorem equates its original threshold with that of a
join, and no contradiction among all71 deficiencies has been proved.

Continue the active S014 universal attack on these precise interface costs:
can criticality force a full true-head assignment across the entire family,
or can a weighted first-firing/path extraction yield a SAME-GRAPH AS loser
whose mass dominates the original arbitrary-buffer loser? The unweighted83
lower alone is too weak on long empty routes and does not make either arrow.
This mathematical gap is not an owner-action blocker or a session closeout.
