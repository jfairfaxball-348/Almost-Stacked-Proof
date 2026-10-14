# S005 — global extrema, exact pure-pile clearing, and the remaining ASH* gap

**Universal critical ASH*: OPEN**, separately for stacking and clearing. No universal proof or counterexample is claimed. The printed pointwise form remains independently refuted, with its earlier certificates unchanged. The symbolic advance is an exact classification of clearing for a pile at any root of any connected graph, with a complete ancestry proof of necessity. Its lower half is already the rooted odd-walk obstruction in Csernák–Soukup April Theorem6.1; the nonzero residues and three-pebble reduction are also source observations. We claim a proved synthesis and matching construction, not unaudited novelty.

## 1. Cold challenge of S004

The independent-set witness proof was rederived without using its finite tests as proof. For I independent, k>=2, r in I, weights1 at r,4 on J=I minus r,2 on A=V minus I give initial weight6k-3. Allowed losses are0,3,0,6,2 for r-to-A, A-to-r, A-to-J, J-to-A, A-to-A. If the final root is in A, forced J firings leave final weight at most3, and final one pebble requires an impossible extra loss1. If root is in J, final two pebbles similarly require loss1; final one requires extra loss5 and prevents any firing/arrival at that untouched singleton. Its positive complement cannot disappear. If root is r, final mass1 or3 forbids A-to-r and any second J firing; the last unique J firing leaves positive mass in A which neither internal moves nor forbidden later J arrivals can erase. Mass2 requires loss1. k=2, isolated vertices, arbitrary edges within A, untouched singleton, positive residual A mass and extra firings all covered. No gap found.

Complete S004 layers were replayed by its independent canonical-parent verifier, alongside full reverse-winning base checks and printed-form cold audit. These are repetitions of independent algorithms, not a new author's testimony or Lean build. The mathematical dependencies are still source threshold equalities and earlier TreeStack where explicitly cited.

## 2. Exact clearing of a pile at a root

Let G be a finite connected simple graph with at least two vertices, r a vertex, and d(v)=dist(r,v). For a non-bipartite G define

h(r) = min {d(u) : uv is an edge and d(u)=d(v)}.

Such an edge exists: otherwise distance parity gives a bipartition. h>=1 since the graph is simple. Let odd(r,G) be the shortest odd closed walk through r, as defined in April Section6.

**Lemma18.** odd(r,G)=2h(r)+1.

Proof. Shortest paths to the endpoints of an equal-level edge at height h, with that edge between them, give an odd closed walk of length2h+1. Conversely an odd closed walk has an equal-level edge: if each step changed the distance parity, an odd number of steps could not return to r. On an odd closed walk of length2k+1, every visited vertex has distance at most k, by taking the shorter direction around the walk. Thus that equal-level edge has height at most k, so h<=k. These two inequalities give equality. Paths may share vertices; a closed walk, not a simple cycle, is the stated object. QED.

**Theorem19 (exact pure-pile clearing).** For every integer N>=1:
- on bipartite G, N e_r is clearable iff N is not divisible by3;
- on non-bipartite G, N e_r is clearable iff N is not divisible by3, or N>=3*2^h(r).

Thus the largest losing positive pure pile at r in the non-bipartite case is (3*2^h(r)-3)e_r. This is an almost-stacked *clearing* loser and is already stacked; it supplies no stacking obstruction.

**Construction for residues1,2.** On any incident edge r-x, four pebbles at r undergo r-to-x twice followed by x-to-r, becoming one at r while restoring x's old pile. This removes three pebbles while retaining a positive base. For N=3q+1 repeat to1 at r. For N=3q+2 repeat to2 and make one move to x. All moves are legal; N=1,2 are included.

**Matching construction at M=3*2^h.** Choose an equal-level edge u-v at height h. A pile of2^h at r can be consumed completely to one pebble at u by successive pair moves along a shortest r-u path; the same holds for v. Partition the M initial labelled pebbles into three disjoint groups of size2^h. Evaluate two groups to two pebbles at u, then move u-to-v. Evaluate the third group to one pebble at v, then move v-to-u. This leaves exactly one pebble. Shortest paths may overlap: evaluate labelled groups separately, as in the exact ancestry grammar; other groups' pebbles do not invalidate a designated move. No residual pebble is discarded. For N=M+3q first remove3q at r retaining M, then apply this construction.

**Necessity, independent ancestry proof.** By S004 Proposition17, clearing a pure pile gives a full binary ancestry tree whose leaves all have label r. Every internal node has two children with the same label u and a parent label v adjacent to u. The node represents a legal u-to-v merge.

First, every such subtree with root label v contains at least2^d(v) leaves. Induct on the tree. A leaf is labelled r and has1 leaf. For an internal parent v with both child roots u, each child has at least2^d(u) leaves, and d(u)>=d(v)-1; hence their sum is at least2^d(v).

Second, a subtree containing no equal-level merge has leaf count congruent to (-1)^d(v) modulo3. At a leaf this is1. For a parent v whose children are both u, consecutive distance levels have opposite parity, and twice (-1)^d(u) is (-1)^d(v) modulo3. Induction proves the claim. In particular such a subtree never has leaf count divisible by3.

Now suppose the entire clearing tree has N divisible by3. It must contain an equal-level merge. Choose one with no equal-level merge strictly below it. Its two child subtrees, rooted at u, each have leaf count congruent to (-1)^d(u); their sum is nonzero modulo3. Therefore this chosen node cannot be the root of the whole tree. Write a=d(u)=d(v)>=h for its equal-level edge u-v. Each child has at least2^a leaves. The node has a parent in the tree, whose other child is also rooted at v and has at least2^a leaves. These three subtrees have disjoint leaves, so N>=3*2^a>=3*2^h. This covers arbitrary extra firings, overlapping graph paths, every final vertex and all later ancestry merges. QED.

For a bipartite graph no equal-level edge exists. The residue induction holds throughout the tree, so a multiple of3 cannot clear. Equivalently use the source's signed bipartite mod3 invariant.

**Attribution and scope.** April Theorem6.1's internal claim already proves the necessary rooted bound in terms of odd(r,G); its full proof was freshly inspected in this session. October equation4.10 already proves the residue1/2 construction and adding-three operation. The equal-level matching construction completes an exact single-pile classification; no comprehensive novelty search has been conducted. The ancestry argument is a programme proof of the necessity, not an assertion that the numerical lower bound was previously unknown.

**Corollary20.** Put H=max_r h(r). Every eligible G satisfies clear(G)>=3*2^H-2. If equality holds, its critical layer contains the AS pure loser (3*2^H-3)e_r, and ASH*-clear holds. This is the source's odd(G) lower bound plus its existing AS witness, now with exact pure-pile interpretation. It does not prove equality on arbitrary graphs. A graph with clearing threshold strictly larger needs singleton-bearing AS witnesses or a different argument.

On C_(2k+1), h(r)=k at every root, recovering the source lower bound3*2^k-2. This does not independently prove the conditional upper bound or solve ASH* on all odd cycles. On a triangle with a tail of l edges and root at its tip, h=l+1, so the pure-pile critical candidate is (3*2^(l+1)-3)e_tip. Finite complete thresholds may corroborate equality but do not prove the infinite family.

## 3. Rooted transfer and a failed geodesic witness

Attempted two-site obstruction:
(2^(dist(r,s)+1)-3)e_r+e_s should be non-stackable.
It holds on the tree paths motivating it but is false on cyclic graphs. A complete BFS test on every ordered pair in every connected graph n=2..5 found3 failures among506 tests. No failure occurred at smaller graph orders.

First stored failure: vertices0..4, edges0-3,1-2,1-4,2-4,3-4. This is triangle1-2-4 with tail4-3-0. Root1, singleton0, distance3, configuration(1,13,0,0,0), mass14. It stacks by:
1-to-2 four times; 2-to-1; 1-to-4 three times; 2-to-4; 4-to-3 twice; 3-to-0.
The final configuration is(2,0,0,0,0). Every step and intermediate state are archived in geodesic_tests.json. A same-level detour changes the residues while respecting graph distances. Consequently shortest distance alone cannot give this stronger stacking obstruction. This is a failed auxiliary lemma, not an ASH* counterexample.

For a leaf x adjacent to u, eliminating an even pile m at x sends m/2 to u. Eliminating an odd pile needs one u-to-x move and then (m+1)/2 x-to-u moves, net (m-3)/2 at u. The odd formula requires two available pebbles at u at the appropriate time. Treating a negative boundary balance as an impossible ordinary configuration loses legal cases: on pathx-u-y, (1,0,4) clears at u by y-to-u twice, u-to-x, x-to-u. Deleting x first would record -1 at u. Thus an exact leaf/block interface must represent deferred debt, chronology and target location. No general signed normalization or cactus/unicyclic threshold upper theorem was obtained.

## 4. Exact consumption forces cyclic schedules

**Lemma21 (acyclic balance is sufficient).** Given nonnegative integer counts a_uv of oriented moves, if their positive-support directed graph is acyclic and the final balance
f(v)=c(v)+sum_u a_uv-2 sum_w a_vw
is nonnegative at every vertex, all counted moves can be legally scheduled to produce f.

Proof. Process vertices in a topological order. When v is processed, every incoming counted move has already occurred. Its current pile is c(v)+sum_u a_uv, at least twice its total outgoing count by f(v)>=0. Execute its outgoing moves in any order. Earlier source vertices receive no later counted moves. This gives all counts legally and leaves exactly f. Zero counts/vertices cause no issue. QED.

Necessity of an acyclic certificate is false even for AS input6e0 on K3. A legal clearing trace is
(6,0,0) -> (4,1,0) -> (2,2,0) -> (2,0,1) -> (0,0,2) -> (0,1,0),
using0-to-1,0-to-1,1-to-2,0-to-2,2-to-1. Its support contains the directed1-2 cycle.

There is no acyclic balance certificate clearing this input. Any vertex other than0 with no incoming positive count has no pebbles and cannot have outgoing counts by nonnegative balance. Hence every used vertex is reachable from0 in the support DAG. If final root is0, it has no incoming count, so6-2*out(0)=1 is impossible. Otherwise call the target b and the third vertex a. The target is a sink: if it had an outgoing edge it would have a downstream vertex that must retain nonnegative mass, and following the DAG to a last downstream vertex gives a positive final pile away from the target. More directly each non-target sink with positive incoming has positive final balance, impossible. Thus any third intermediate a may only send to b. Source0 emits3 moves; if k of them go to a then 0<=k<=3 and balance at a requires k even with out(a)=k/2. Final mass at b is3-k+k/2=3-k/2; equality1 would require k=4, impossible. If a is unused the same formula withk=0 applies. All orientations covered.

This is a decisive obstruction to a no-cycle exact-consumption reduction. Usual cycle deletion raises balances and may leave extra support; it does not preserve clearing or exact stacking. The terminal all-ones K3 integer-balance example from S004 remains a separate failure of unrestricted balance sufficiency.

## 5. Three-pebble closure and the precise extremal-hole problem

**Lemma22 (support-preserving +3 closure).** If c is stackable or clearable and c(w)>=1 at a vertex w with a neighbour, then c+3e_w has the same property. Apply the three-move reduction at w to return exactly to c, then its winning sequence. For a losing c with c(w)>=4, contrapositive implies c-3e_w is losing. Neither assertion allows deletion of the last pebble or creation of a new support vertex without qualification. This is the source's equation4.10 operation, applied before a general configuration's winning sequence.

Fix a support S and positive residue representatives b_v in{1,2,3} at v in S, with b_v=0 elsewhere. Every configuration in that support/residue class is b+3z, z in N^S. Winning z form an upper set; losing z form a lower set. For an eligible goal their losing set is finite, because a finite threshold exists. The union over finitely many support/residue classes exactly represents all positive losing configurations.

This reformulates ASH* as a maximum-degree hole question comparing these finite lower sets across *different* classes: can their overall largest mass always be attained with all but one positive coordinates equal1? Three-pebble closure alone does not answer it. A lower set with z1,z2<=1 has its largest total degree at(1,1), larger than on either coordinate axis. This is an abstract obstruction to the proposed order-theoretic proof, not a graph example; the exact graph grammar/recurrence must supply additional constraints.

The remaining first implication is now explicit: a graph-generated family of these residue lower sets, with the exact stack/clear ancestry grammar and all-successor recurrence, must have a largest hole on an AS ray. Neither acyclic move counts, shortest-path weights, support minimization nor closure under3 proves this.

## 6. Global square extrema

Select over the entire certified critical losing layer. The assertion that every Q(c)=sum c(v)^2 maximizer is AS is stronger than ASH*. If at least one AS Q-maximizer exists, ASH* follows; if all Q-maximizers were non-AS that would refute the existential square selection, but not necessarily ASH*. A mixed AS/non-AS tie refutes only the strongest assertion. The lexicographic sorted-pile maximum is another stronger selection, tested separately.

Whole-layer producers and independent replayers calculate the exact maximum and count of non-AS maximizers, not local maxima or sampled states. Completed/cutoff scopes and counts are in campaign_summary.json and verification.json. No proof of global square selection was obtained. The old P3 local convexity failure remains relevant and is not bypassed by finite success.

## 7. Assurance and exit

Numeric details and final campaign counts are consolidated in sessions/S005/AUDIT.md after all replay completes. Binary certificates encode complete labelled losing layers, not orbit representatives. The independent checker regenerates canonical-parent candidates and compares full sets, exact masses, AS counts, Q maxima and reverse-winning base layers. Cutoff certificates certify only completed layers. Every headline numerical claim requires that replay; producer-only observations are provisional until then.

Pure-pile theorem checks, geodesic traces, exact graph inputs, code/environment metadata and evidence hashes are retained. Source current versions were v1 and unchanged on the original S005 fetch; fresh continuation inspection read April Theorem6.1 and October4.10 proof text. Private correspondence remains an attributed owner-supplied summary, not a published erratum.

Phase1 universal stays IN_PROGRESS. Printed-form Phase1 PASS remains separate. No first novelty audit, Lean, Palomar, manuscript or author contact began. Next S006 must be complete and strictly FUTURE/UNEXECUTED, aimed at the universal hole-selection theorem and legal rooted debt interfaces.
