# S006 — exact rooted buffer conductors and the remaining extremal gap

**Universal critical ASH*: OPEN for stacking and clearing.** This session proves an exact finite interface for a variable pile at a specified vertex, with arbitrary fixed pebbles elsewhere and a specified final root. Clearing uses binary ancestry trees; stacking uses nonempty forests. It closes the chronology/target gap for that interface, but does not compare the largest general loser with the largest almost-stacked loser. No infinite triangle-tail threshold formula, novelty, Lean or universal ASH* success is claimed.

Throughout G is finite, simple, connected, n>=2. Moves remove two pebbles and place one at an adjacent vertex. Rooted clearing ends at exactly e_q; rooted stacking ends at k e_q for some k>=1, consuming every initial pebble. Empty configurations are neither goal. General clearing thresholds require non-bipartiteness; individual rooted reachability on bipartite graphs is still meaningful. The source's least exact threshold t>=2 and monotonicity above n are retained.

## 1. Cold audit and attribution

The S005 Theorem19 proof survives the cold challenge. For source s, distance levels differ by at most one across an edge. If no equal-level edge exists, distance parity is a bipartition. A shortest odd closed walk has an equal-level edge, and every vertex on a length 2k+1 closed walk is at distance at most k. Conversely paths to the endpoints of a first equal-level edge at height h give an odd closed walk of length 2h+1, even if the paths overlap. Hence odd(s,G)=2h+1.

In a pure-source clearing ancestry tree, any subtree ending at v uses at least 2^dist(s,v) leaves, by induction on its last merge. A subtree without an equal-level merge has leaf count congruent to (-1)^dist(s,v) mod3. If the whole tree has leaf count divisible by3, take an equal-level merge with no such merge below it. Its children have the same nonzero residue, so the selected merge cannot itself be the final root. Its two children and its parent's other child are disjoint and each require at least 2^h leaves. Thus N>=3*2^h, regardless of the final vertex or subsequent cyclic moves. On bipartite graphs the residue obstruction holds throughout. The three-group construction along shortest paths to an equal-level edge consumes all labelled leaves; overlaps do not invalidate designated moves. The +3 reduction preserves a positive base and is legal even for base1 (the first pile is4).

Therefore the exact unrooted classification is retained: N e_s clears iff N%3!=0 or N>=3*2^h for non-bipartite G; bipartite multiples3 do not clear. This is a **clearing** obstruction only. The lower bound is already SRC-0002, April Theorem6.1; the reduction is SRC-0001, October equation4.10. Source versions freshly fetched on 2026-10-14 remain v1 with the same PDF hashes. Relevant statement/proof portions were re-read, not inferred from abstracts. Private correspondence SRC-0010 remains owner-supplied provenance, not a public erratum.

The S004 independent-set witness, its complete multipartite consequences using source equalities, and earlier TreeStack arXiv:2609.31811/registered package remain credited. Its rooted tree messages already retain debt and schedule; no rediscovery claim is made here. No TreeStack kernel build or registry audit was run. The fresh tree source files read are hashed in source_refresh.json.

## 2. Exact rooted pure-pile theorem

Fix source s. For v in V and r in {0,1,2}, define A(v,r) to be the smallest positive N with N congruent to r mod3 and N e_s legally clearable to e_v, or infinity if none.

**Theorem23.** These 3n numbers are exactly the minima of the finite grammar

- base: (s,1) has weight1;
- for each edge uv and residues a,b, two derivations at (u,a),(u,b) combine to a derivation at (v,a+b mod3), with weight the sum of their weights.

For every N>=1, N e_s clears to e_q iff A(q,N mod3) is finite and N>=A(q,N mod3). All finite minima admit ancestry witnesses. All minima, including infinities, can be certified by attaining trees plus the base and every production inequality. At most 3n-1 synchronous production rounds after the base suffice; hence O(n|E|) min-plus operations with O(n)-bit finite values suffice for one source.

Proof. Every clearing sequence gives exactly such a tree by following the two ancestors of each output pebble. All leaves are s. Conversely evaluate two designated child trees independently and then their legal merge along the edge. Every initial pebble is used, including when paths/vertices recur. This is the exact ancestry equivalence of S004 Proposition17, now restricted to pure input and optimized by source count.

Every tree weight in class (q,r) is at least the minimum A. A tree attaining A gives the upper bound. If labels L satisfy L(s,1)<=1 and L(v,a+b)<=L(u,a)+L(u,b) for every production with finite children, tree induction proves weight>=L for every possible derivation. A parent labelled infinity may not have finite children producing it. Attaining trees then prove L=A; this certifies infinity as well as finite values. No finite search cutoff is used to prove a minimum.

Choose a minimum-weight derivation. No root-to-leaf path repeats a (vertex,residue): replacing the higher occurrence by the lower subtree would preserve the root state and strictly reduce leaf count, a contradiction. Thus its height is at most 3n-1 and its weight at most 2^(3n-1). Finite synchronous relaxation through that height finds it, and the remaining states are unreachable. Each round examines nine residue pairs per oriented edge. Integer bit length is at most 3n. Finally a winning input A e_s can be preceded by the legal +3 reduction at the occupied source to clear every (A+3j)e_s. These are exactly all larger positive integers of that residue. QED.

**Bipartite case.** If d=dist(s,q), the signed mod3 invariant requires N congruent to (-1)^d. Every ancestry tree requires at least 2^d leaves; a shortest-path tree attains 2^d. Thus that residue has A=2^d and the other two have A=infinity. This is rooted clearing reachability, not an eligible clearing number.

**Non-bipartite case.** Every A(q,r) is finite. There are walks of both parities from s to any vertex: insert an odd closed walk into an ordinary walk. A walk of length L realizes 2^L e_s -> e_q. Opposite parities supply residues1 and2. To realize residue0 at q, take opposite-parity walk trees ending at a neighbour u, evaluate both, and merge their two outputs u->q. The sum of their leaf counts is0 mod3. This proves finiteness without a numerical threshold guess.

For the labelled triangle with source0 the exact rows (residues0,1,2) are

| Final root | Minima |
|---|---|
| 0 | (6,1,8) |
| 1 | (6,4,2) |
| 2 | (6,4,2) |

In particular 5e0 clears somewhere but cannot clear to e0. The complete forward closure independently proves that exclusion; it is not a failed selected move sequence. This disproves importing an unrooted clearing threshold as a prescribed-boundary threshold. The grammar allows directed cycles: K3 at6e0 is retained, while terminal all ones still cannot make a first move.

## 3. Arbitrary fixed off-source piles: necessary and sufficient interface

Fix s, a vector b on V minus {s}, and final root q. For each positive residue r let C(s,b,q,r) be the minimum positive N such that b+N e_s clears to e_q, or infinity. Record separately the Boolean Z(s,b,q) for whether b alone clears to e_q. The zero-source case is not residue0 with a zero minimum.

**Theorem24 (exact clearing buffer interface).** This four-part interface determines rooted clearing for every N>=0: at N=0 use Z; at N>0 use C(s,b,q,N mod3)<=N. It is exactly computable by a finite grammar on states

    (final vertex v, off-source vector d with 0<=d<=b,
     source kind: exactly zero, or positive with residue0/1/2).

Base leaves are e_s (positive source count1) and e_w for each permitted off-source vertex w (source count zero). A merge across u-v adds the two off-source vectors exactly, adds source counts, and keeps the zero kind only when both counts are zero. There are K=4n product_w(b(w)+1) states. Minimize source count and retain attaining trees; exclude the empty input.

Proof of exactness. A clearing ancestry tree for b+N e_s has every subtree's off-source vector <=b, so it is a derivation of this finite grammar. Conversely every grammar derivation realizes exactly its stated vector by legal postorder moves; addition of off-source vectors forbids discarding or duplicating an initial pebble. Minima and infinity are certified by the same induction inequalities and attaining trees as Theorem23, now for every allowed split d=d1+d2 and every source kind.

For positive N, legal +3 at s fills the corresponding class above its minimum and cannot create a smaller winning count. At N=0 this closure has no justification because the source is empty; hence the separate bit. A minimum-source derivation can be chosen with no repeated state on a path: equal off-source vectors at an ancestor and descendant force every intervening sibling's off-source vector to be zero; a nonempty sibling then contributes positive source count, strictly improving N if removed. For zero-source states repetition is impossible for the same reason. Thus a minimum has height at most K-1. Exhaustive finite relaxation terminates with every exact minimum; this is not a relaxed integer firing-balance certificate. QED.

**Theorem25 (exact stacking buffer interface).** Replace clearing trees by nonempty forests of clearing trees with common output root q. Keep the same positive residue minima S(s,b,q,r) and separate zero-source bit. Seed a forest with any clearing tree and concatenate two forests at the same root, adding their input vectors/source counts. This finite grammar computes the exact rooted stacking interface; at positive N, rooted stacking holds iff N>=S of that residue.

Proof. Following each surviving pebble of a final stack partitions all initial pebbles into clearing trees with root q. Conversely evaluate those trees on disjoint designated inputs, leaving a positive number of pebbles at q. Concatenation does **not** merge two stacks as if they were single pebbles. Every forest has a finite binary concatenation parse. With clearing/forest types separated there are at most 2K states; the same minimal repeated-state argument and production inequalities apply. The +3 reduction preserves the entire input before running the forest, so positive-source threshold tails follow. Zero remains separate. QED.

These are exact whole-graph buffer interfaces, with an input-dependent finite state space. They retain arbitrary targets, initial residues, excursions and cycles. They do not prove a fixed-size scalar block message that can be composed independently of every possible external history; nor do they supply a symbolic infinite triangle-tail threshold upper bound.

## 4. Constructive finiteness and bounds, separately for each goal

For w!=s put d_w=dist(s,w) and

    D(s,b)=sum_w b(w) (2^(d_w+1)-3).

**Lemma26 (absorbing fixed pebbles).** For every L>=1,

    b + (D+L)e_s -> L e_s.

Proof. For one designated pebble at w, supply one additional pebble at w and one at each internal vertex of a shortest s-w path, using only designated source pebbles. This costs p=2^d+sum_(i=1..d-1)2^i=2^(d+1)-2 at s. The backwards cascade consumes all path pebbles and returns one pebble to s, a net source cost p-1=2^(d+1)-3. Other designated inputs are untouched, even on overlapping paths. Repeat for every off-source pebble. Before each task, source count is at least its cost plus1 because L>=1; therefore its p source pebbles are available. The final count is exactly L and every off-source pebble was consumed. QED. This uses the source pullback operation (October Lemma4.8); no priority claim.

For non-bipartite G all three C minima are finite, since

    C(s,b,q,r) <= D + A(q,(r-D) mod3),

using Theorem23 with source s. For stacking on every connected G, put d=dist(s,q). For the unique k in {1,2,3} satisfying D+k*2^d congruent to r, k shortest-path trees show

    S(s,b,q,r) <= D + k*2^d.

These bounds are sufficient constructions; they need not be exact minima. The clearing argument is not applied to bipartite graphs.

**Corollary27 (finite rooted conductor bound).** Fix q and an eligible goal: stacking on connected G or clearing on connected non-bipartite G. Let B be the maximum positive-source minimum over all sources s, residues, and off-source representatives b in {0,1,2,3}^(V minus s). Every configuration with a coordinate >=B wins at q. Consequently every configuration of total >n(B-1) wins at q.

Proof. Choose a coordinate s with count N>=B. Replace each other positive count by its representative in {1,2,3}; retain every zero. The resulting b+N e_s wins at q by its exact interface minimum. Restore the removed multiples of3 at occupied off-source vertices using positive-support +3 closure. This recovers the original configuration as a winner. If all coordinates are <B, their sum is at most n(B-1). Finiteness of B follows from Lemma26 and the separate pure constructions. QED.

This independently establishes a finite exact-algorithm domain for rooted thresholds. It does not say the bound is sharp or that its extremizers are AS. Bipartite clearing is explicitly excluded. For n=1 there are no moves, positive configurations are already stacked, only size1 clears, and the source threshold convention gives stack(K1)=2. None of the +3/conductor statements above is applied there; the zero graph is outside the target.

## 5. Exact AS rays and the first unsolved universal implication

For eligible G, let B(s,b,r) be the minimum over final roots of the corresponding interface minimum, with b binary off s. Let r_+=3,1,2 for r=0,1,2 respectively. The exact largest losing mass among positive AS configurations is

    L_AS(G) = max { |b|+B(s,b,r)-3 : B(s,b,r)-3 >= r_+ }.

Every positive AS configuration occurs on one of these rays by choosing its heavy vertex, or an occupied vertex if there is no heavy pile. On each positive residue ray all winners start at B, so its last loser is B-3 if positive. The all-ones terminal configuration shows L_AS>=n. Thus this is a finite exact computation from binary off-source grammars, including arbitrary pile sizes; it is not a search extrapolation.

ASH* is precisely the assertion that **every configuration of mass L_AS(G)+1 wins**, for every eligible G, separately for the two goals. Such a theorem would give g=L_AS+1 by monotonicity above n and the AS loser. Theorems24-27 do not compare interfaces with b(w)>=2 to the binary b interfaces; their finite bound B generally uses representatives2 and3. Removing those representatives while preserving the global largest-hole comparison is the first unsolved implication. No finite test here supplies it.

## 6. Route A: fixed-residue concentration fails at the critical layer

The exact grammar gives useful production inequalities, but they compare **winning** derivations at different masses/roots. They do not reverse to loss-preserving concentration at fixed mass. Support/residue closure cannot cross from a class with two residues2 or3 into an AS configuration: those two coordinates remain heavy.

Cold analysis of all 257 inherited n=2..6 graph/goal critical layers found618 non-AS class square maximizers. The first is P3, edges0-2,1-2, critical mass6, c=(3,3,0). Its positive-support/residue class has only that critical loser, Q=18, whereas the global AS maximizer (1,5,0) has Q=26. No sequence staying in this class can reach any larger-Q critical loser. An independent eight-state legal closure proves c non-stackable. The global critical Q maxima in all257 cases remain AS, consistent with S005; this is finite evidence, not a proof of global Q selection or ASH*.

Logical distinctions remain: every global Q maximizer AS implies existence of an AS Q maximizer, which implies ASH*. Mixed ties disprove only the strongest assertion. A component/class maximum is not a global maximum. The explicit P3 obstruction rejects the proposed fixed-residue route, not the unproved cross-class theorem.

## 7. Route B: scalar leaf elimination fails in both directions

Take triangle0-1-2-0 with leaf3 at0. The naive rule replaces an even leaf m by m/2 at0, an odd leaf by (m-3)/2, rejects a negative core, and asks only whether the adjusted triangle clears somewhere.

- False positive: c=(0,1,0,3). Its only move gives (1,1,0,1), terminal and not cleared. The adjusted core is (0,1,0), already cleared, so the scalar rule incorrectly accepts. It has lost the required boundary credit.
- False negative: c=(0,0,4,1). The adjusted core has -1 at0, so the scalar rule rejects. A legal trace is 2->0 twice,0->3,3->0, ending at e0. The negative debt can be paid later.
- Even the zero-move boundary matters: a single pebble at leaf3 is already cleared and must not be forced to the core. The first bounded false negative is exactly that case.

Independent closure certificates and traces are retained; no failed selected move sequence is used as an impossibility argument. The precise interface from Theorems24-25 handles these cases, but its size grows with the fixed off-source data. An upper bound for all distributions on every length-l triangle tail remains unproved. S005's numerical family pattern and its tail6 cutoffs remain unchanged; this session did not relabel them as exact thresholds.

## 8. Computation, independent verification and limits

All experiments were registered and hashed before execution (PLAN and Amendments1-3). No new atlas census or threshold frontier was run. Optimizer certificates cover137 source/graph cases from every connected n=2..5 inherited catalogue graph, plus15 source/graph cases on triangle tails of lengths1..3. The independent verifier checks all local production inequalities, all infinity cases, and actual legal postorder realizations:153 clearing certificates including one arbitrary-buffer box,2145 finite attaining trees and30347 production inequalities. Pure tables have1788 finite entries. Unrooted minima agree with cold Theorem19 in every case; bipartite root residues/minima also agree.

The triangle-leaf buffer box {0,1,2}^3 at source0 has432 clearing cells,357 finite. Its separate stacking forest has367 finite cells, all legally replayed, plus9161 checked concatenation inequalities. The forest checker includes the clear-to-forest bounds and independently verifies the clearing seed certificate. No optimizer import is used by either proof checker.

Independent full forward-successor and reverse-predecessor rooted-mask algorithms agree on all3155536 labelled configurations in531 complete layers across35 graphs. There are11750 pure source/target/size comparisons with exact grammar predictions and1508 clearing-buffer comparisons. A separate pair of rooted-stacking traversals adds1508 buffer comparisons through mass16 and full dictionary equality on those16 layers. Zero-source inputs are included separately; the empty configuration is explicitly not a goal.

The root-layer graph scopes are every connected n=2..5 inherited graph, the three named tails, canonical triangle, and length4 tail. Caps are exactly in rooted_challenges.json. The length3 tail stops after mass29 because the next layer has324632 configurations, over the registered300000 limit; it carries no layer30 claim. Length4 tail only through10. No threshold or completeness beyond these caps is asserted. The whole registered rooted challenge took32.203s, extrema3.313s, grammar optimization0.078s; all within budgets. No field packing, coordinate overflow, stochastic sampling or state symmetry is used.

Scalar tests are complete within the registered mass bounds: lengths1,2,3 through16 and length4 through10. Counts are in rooted_challenges.json; failures are auxiliary-rule failures, never ASH* counterexamples. Complete membership sets are compared in memory; deterministic per-layer hashes preserve the replay log. The universal interface proofs use induction and attaining grammar certificates, not an inference from those hashes.

## 9. Dependency and exit audit

Exact ancestry equivalence (S004 Proposition17) -> rooted min-plus optimization (Theorem23) -> finite off-source grammar (Theorem24) -> forests (Theorem25). Source pullback and explicit shortest-path trees -> Lemma26 -> finite rooted conductor bound (Corollary27). Positive-support source +3 -> threshold tails. Binary off-source specialization -> exact L_AS formula. **There is no proved arrow from these statements to the comparison of general and binary off-source holes.**

Universal Phase1 remains IN_PROGRESS. Printed-form mathematics PASS remains separate, Lean pending. No first novelty audit, Lean, Palomar, paper, author contact or submission. A fresh cold audit of the full new interface proof belongs in the FUTURE S007 handoff; different checker implementations are not a separate human mathematical review. The original universal objective has not been achieved, and no gate is advanced.
