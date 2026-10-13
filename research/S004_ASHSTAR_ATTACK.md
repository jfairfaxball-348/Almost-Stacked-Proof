# S004 — independent-set AS witnesses, exact losing frontiers, and the universal obstruction

**Universal ASH*: OPEN for stacking and clearing.** No universal proof or counterexample was obtained. The printed form's separate cold audit passes. The main symbolic result is a universal *lower-bound witness* theorem: it puts the known independence obstruction in almost-stacked form even on graphs with odd cycles. Together with the source's exact thresholds it settles ASH* for all complete multipartite graphs. No priority claim or Lean certification is made.

## 1. Exact losing recurrence and complete sparse certificates

Fix a connected simple graph of order n>=2 and one goal. For clearing require non-bipartiteness when discussing its threshold. Let B_t be the exact mass-t losing set. A state is losing iff it is not already a goal and every legal successor lies in B_(t-1). This includes the empty successor set: non-goal terminal states lose. Every move decreases mass by one, so induction on mass proves the recurrence, without fairness or a search heuristic.

Let P(B) be the union of inverse legal moves of states in B. For t>=1, let T_t be the terminal 0/1 states of mass t that are not goals. Then

**Theorem 11 (complete sparse recurrence).**

`B_t = {c in P(B_(t-1)) union T_t : c is not a goal and all legal successors are in B_(t-1)}`.

Proof: a nonterminal loser has a legal successor, which is losing by the preceding identity, so it lies in P(B_(t-1)). Terminal losers are exactly T_t. Conversely the non-goal and all-successor conditions imply loss. B_0 consists of the zero state, but it has no predecessors; the implementations omit B_0 and seed T_1 before rejecting its singleton goals, which gives the identical B_1=empty. For t>n, T_t is empty because a heavy vertex has a neighbour. The first empty layer above n is the threshold, since terminal losers cover 2<=t<=n and the all-configuration monotonicity covers every higher layer. QED.

The primary implementation takes **all** inverse moves of previous losers, then filters every legal successor. The independently written packed-state checker enumerates inverses only of the deterministic move from the least heavy vertex to its least neighbour. Every nonterminal loser has this successor in the previous losing set, so this smaller candidate set is still complete. The checker verifies exact equality of each supplied layer with the expected set, not just closure of the supplied set. Terminal states are seeded separately; both goals and exact masses are checked. No configuration symmetry is used. This is an induction certificate of all winners as the complements of the supplied complete losing sets, as well as of all losers.

An empty layer proves the complete threshold; it is **not** enough to show some AS winners. Every completed critical layer is replayed and contains an explicit AS loser. None is an ASH* counterexample. Cutoff layers yield lower bounds only. See `evidence/S004/frontier_summary.json`, `frontier_verification.json`, compressed layers and hashes.

## 2. A universal almost-stacked independence obstruction

**Theorem 12.** Let G be any finite simple graph. Let I be an independent set with k=|I|>=2 and let r in I. Then

`c = (2k+1)e_r + sum_{x in I\{r}} e_x`

is not stackable. Its mass is 3k and it is almost stacked. Therefore it is also not clearable. Connectivity is needed for threshold conclusions, not for this obstruction.

**Proof.** Put J=I\{r}, A=V\I. Assign weights R(r)=1, R(J)=4, R(A)=2. The initial weighted mass is 6k-3. Independence of I gives the complete list of possible move losses `2R(u)-R(v)`:

| Move type | r to A | A to r | A to J | J to A | A to A |
|---|---:|---:|---:|---:|---:|
| Weight lost | 0 | 3 | 0 | 6 | 2 |

All losses are nonnegative. The new point beyond S003 Theorem 10 is to allow the loss-2 moves inside A; a mod-3 invariant cannot be assumed. Suppose a sequence ends in h e_s, h>=1.

**s in A.** Each x in J starts with one pebble and ends with none, so it must fire at least once, costing at least 6(k-1). The final weighted mass 2h is at most 3. Thus h=1, leaving exactly one unit of additional weight loss beyond these forced firings. All additional losses are sums of 2,3,6, so one is impossible.

**s in J.** The other k-2 vertices of J must each fire at least once. The final weight 4h is at most 9. If h=2, the additional loss is one, impossible. If h>=3, weight exceeds 9. If h=1, additional loss is five. In particular the target s cannot fire, since that alone would lose six; neither can any other J vertex fire a second time. Since s starts and ends with exactly one pebble and never fires, it receives no pebble either. Hence all moves avoid s. Initially the complement of s has positive mass. A legal move wholly within that complement decreases its positive mass by one and leaves it positive: it requires at least two pebbles and produces one. It can never become empty. Contradiction.

**s=r.** All k-1 vertices of J must fire. Final weight h is at most 3. h=2 leaves additional loss one, impossible. h=3 leaves additional loss zero and h=1 leaves additional loss two. In either remaining case there are no A-to-r moves, and each J vertex fires exactly once. The balance at x in J is `0=1+arrivals(x)-2`, so each receives exactly one pebble, before its unique firing. Choose the last firing by a vertex of J; it creates a pebble in A. After that time there can be no A-to-J move (its recipient has already had its unique arrival/firing and must finish empty), nor any A-to-r move. Internal A-to-A moves cannot empty a positive mass in A, by the same last-pebble argument. Thus A remains nonempty at the purported final stack. Contradiction. J is nonempty because k>=2. If an isolated vertex prevents a required firing, that case is already impossible. This exhausts target locations and proves the claim. QED.

**Independent challenge.** The statement was tested on every independent set of size >=2 and every root of each such set on every connected graph with 2<=n<=5: 233 labelled witnesses on 30 graph isomorphism classes, all losing under the cold full winning-set DP. The proof was also audited for k=2, isolated vertices, target untouched, extra firings, and internal A moves. The finite tests corroborate but do not prove the theorem. The numeric independence lower bound itself is prior work (April Theorem 5.1 uses three pebbles at every independent-set vertex). This result supplies a different AS witness; novelty remains unaudited.

**Corollary 13 (threshold saturation).** For either eligible goal, if g(G)=3alpha(G)+1 with alpha>=2, Theorem 12 at a maximum independent set gives an AS loser at g-1. Thus ASH* holds. If g(G)=n+1, the all-ones state gives the same conclusion independently. Consequently any universal counterexample must have `g(G)>max(n+1,3alpha(G)+1)` (K2 handled separately).

**Corollary 14 (complete multipartite graphs).** ASH* holds for stacking on every connected complete multipartite graph with n>=2, and for clearing on every such non-bipartite graph. Complete graphs use g=n+1; K2 uses the two-singleton loser. For two nonempty parts and n>=3, April Theorem 8.2 gives stack=3alpha+1. For at least three nonempty parts, April Theorem 8.3 gives stack=clear=max(n+1,3alpha+1). Apply Corollary 13 in each case. The threshold equalities are **cited source theorems**, not newly proved here. Theorem 8.3 statement and proof ending were inspected; its full technical Proposition 8.5 proof was not independently audited, so no stronger source access is inferred. S003 already settled the bipartite subfamily. The extension to three or more parts is a genuine family consequence in this programme, not a universal solution.

## 3. Route A — extremal selection, with a precise remaining gap

Select a last-layer loser maximizing Q(c)=sum c(v)^2. This is an existential selection across **the entire** last losing set, unlike the refuted operation that must compress every loser within its own connected transfer component. Every Q-maximizer was AS in all 50 completed graph/goal pairs with 2<=n<=5, and in all 19 threshold-complete S004 frontier cases. These finite observations support only a **HEURISTIC conjecture**:

`Every maximizer of Q on B_(g-1) is almost stacked.`

It implies ASH*, but has no proof. The proposed local convexity argument fails already on P3: with centre 0, c=(0,3,3) is a critical loser (stack=7), while the one-unit transfers (0,4,2),(0,2,4) are winning. The more distant (0,5,1) is losing. Thus loss is not interval-convex along pair transfers, and a local optimum need not be the global maximum. Minimum support is likewise insufficient: P3 has minimum critical support two but both AS (0,5,1) and non-AS (0,3,3) minimizers. All graphs of smaller order were checked, so this is a smallest-order checked support-selection failure. Do not assert an improvement step from an arbitrary critical loser.

The exact missing theorem is a global argument ruling out a non-AS Q-maximizer when B_g is empty. The recurrence supplies only lower-layer universal loss, whereas mass-preserving transfers have the same mass and generally no legal path between them.

## 4. Route B — blocks, bridges and pointwise stack/clear transfer

Block threshold numbers alone do not determine the union threshold. Identify one vertex of P3 with a vertex of K3. Attaching at the middle of P3 gives the triangle with two leaves at the same triangle vertex, edges 0-1,0-2,0-3,0-4,1-2: stack=11, clear=13. Attaching at an endpoint gives the triangle with a pendant path of length two: stack=16, clear=22. Both have the same unrooted block list K3,K2,K2. The cold n<=5 computation checks these exact thresholds. A block rule must retain rooted interface information, not just component thresholds. A minimal counterexample cannot currently be reduced merely by knowing ASH* of its blocks. Trees remain prior TreeStack work.

**Proposition 15 (pointwise triangulated transfer).** If G is connected and every edge lies in a triangle, then every configuration of mass >=4 is stackable iff clearable. Thus the two ASH* questions are equivalent on this graph class.

Proof: clearing implies stacking. Given a stacked pile of mass >=4, the moves u-to-v twice and v-to-u reduce it by three. Repeating leaves a pile of size 1,2,3; size 2 clears by one move. If size 3 remains, the sequence from the original configuration of mass >=4 contains a last move to 3e_v; immediately before it the configuration is 2e_u+2e_v on an edge. A common neighbour w permits u-to-w, v-to-w, w-to-u, clearing it. This proof also covers an initially stacked pile: the reduction sequence supplies that last move. It is the pointwise strengthening of the source's October Lemma 6.4 argument, properly credited. For n>=4 the critical mass is >=4 and losing sets coincide there. For n=3 the class is K3, whose critical layer is the all-ones loser. QED.

More generally any stackable but nonclearable configuration of mass >=4 can reach 2e_u+2e_v on an **untriangulated** edge. This necessary interface obstruction follows from the same final-three argument. It is not sufficient for original loss: an alternative sequence may clear. At mass four exactly, 2e_u+2e_v is clearable iff u and v have a common neighbour, by examining the first move. No bridge elimination theorem preserving the critical level was proved.

## 5. Route C — global additive certificates and cycle corrections

**Proposition 16 (classification of additive move invariants).** On a connected simple graph with an edge, assign weights a_v in any abelian group so that sum c(v)a_v is unchanged by every oriented legal move. Then every weight is 3-torsion and adjacent weights are negatives of each other. For a bipartite graph the assignments are a on one part and -a on the other, with 3a=0. On a non-bipartite graph the only assignment is zero.

Proof: both directions of an edge give a_v=2a_u and a_u=2a_v, hence 3a_u=0 and a_v=-a_u. Connectivity propagates. An odd cycle yields a=-a, so 2a=0; together with 3a=0 this gives a=0. Conversely the bipartite assignments satisfy every move equation. QED.

Thus a nonzero mod-3 invariant for arbitrary connected non-bipartite clearing cannot extend the rooted tree invariant directly. Rooted distance weights 2^dist have nonnegative legal-move losses because adjacent distances differ by at most one, but same-level edges have loss 2^dist, generally not divisible by three. Necessity of these weighted obstructions was not proved. Theorem 12 succeeds by budgeting the loss-2 terms and retaining chronology; it does not need an invariant modulo three. Beyond the independence threshold, the exact necessary certificate remains open.

## 6. Route D — direct contradiction and exact ancestry languages

For each root v, define C_v as the least family of configuration vectors containing e_v and closed under: if c,d in C_u and uv is an edge, then c+d in C_v. Define S_v as the set of all nonempty finite sums of members of C_v.

**Proposition 17 (exact ancestry certificate).** A configuration is clearable at v iff it lies in C_v; it is stackable at v iff it lies in S_v.

Proof: label every initial pebble by its own leaf. Each move joins the two ancestry trees at its source under a parent at its destination. A final single pebble supplies exactly the binary tree described by the recursive C_v grammar, and a stack supplies a forest with all roots v. Conversely evaluate a grammar tree from leaves upward; evaluate two subtrees separately using their designated pebbles, then merge their two outputs along the edge. Extra pebbles designated for other subtrees do not invalidate a move. A forest is evaluated componentwise, leaving all outputs at v. Every initial pebble belongs to exactly one tree, so there is no implicit discard and the final support is exact. QED.

This converts a universal counterexample into an extremal hole of a union of rooted additive monoids (stack) or rooted tree languages (clear). The positive-demand cover-pebbling theorem cannot be substituted: these languages consume **all** initial pebbles and permit no unaccounted residual pebbles. No theorem forces their largest hole to lie on the AS boundary. This is the direct-contradiction route's first unsolved obstruction.

Dropping chronology also fails. On K3, c=(1,1,1) is terminal and losing, yet formal move counts one each for 0-to-1 and 1-to-0 balance it to e_2. Neither move can legally start. Therefore nonnegative integer firing counts plus final nonnegative balance are not a sufficient reachability certificate. K2 at (1,1) would balance to zero, which is not a goal; K1 has no moves. The checked three-vertex example demonstrates the issue without asserting exhaustive minimality for every possible firing relaxation. No global flow-duality theorem was obtained.

## 7. Exact campaign outcome and scope

All eight previously cutoff n=7 stacking cases and all three clearing cases now have independently verified complete thresholds. This closes the S003 finite atlas coverage to 853/853 stacking and 809/809 clearing for order seven (combined with inherited S003 agreeing full-layer data on the other cases). ASH* holds on every one. This is now independent programme computation rather than solely author testimony; the earlier author claim retains SOURCE_STATED provenance.

Selected new larger values: C9 stack=37, clear=46; triangle with a length-five tail stack=128; two triangles joined by a length-three path stack=clear=36. These refer to the explicit labelled edges in the evidence, with path length counted in edges. C8 stack=31 and C8 chord 0-4 23/23 are replicated. C10 stopped before completing mass 17 (candidate limit); exact completed layers end at 16. The triangle-tail clearing computation stopped at mass 140 with 739 losers, so clear>140 and there is no ASH* verdict for it. No extrapolation to cycles or sparse families of arbitrary order.

## 8. Gate and next theorem to attack

The printed-form cold audit is **Phase 1 PASS for that separate result only**. Universal ASH* remains Phase 1 IN_PROGRESS; novelty/Lean/Palomar/arXiv stages have not started. Main dependency chain: complete recurrence -> finite layer certificates; independent-set weighted budget -> saturation corollary -> complete multipartite ASH* using cited exact thresholds. No arrow leads from any finite census or special family to universal ASH*.

The first unsolved obstruction is a graph with g>max(n+1,3alpha+1): prove that a last-layer loser can be selected AS without assuming within-layer compression or necessary linear potentials. The global square-maximizer assertion and the exact ancestry language offer precise, competing formulations for S005, together with rooted block interfaces and sparse unexplored graphs.
