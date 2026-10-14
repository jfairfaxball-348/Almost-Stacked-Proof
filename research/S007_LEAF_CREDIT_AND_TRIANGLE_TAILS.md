# S007 — legal leaf credit and exact triangle-tail clearing

**Universal critical ASH*: OPEN, stacking and clearing separately.** A complete infinite-family result is obtained: if G_l is a triangle with a pendant path of l edges, then clear(G_l)=6*2^l-2 for every integer l>=0. Its critical pure-pile AS witness is the prior April Theorem6.1 obstruction, not a new lower bound. The upper is proved here for all configurations, without assuming ASH*. No novelty or formal-certification claim. Also proved: stack(G_l)<=4*2^l, without an infinite matching stacking lower claim.

Label G_l by vertices0,1,2 forming a triangle and vertices3,...,l+2 on the path0-3-4-...-(l+2). The tip is0 when l=0 and l+2 otherwise. Graphs are finite, simple, connected and non-bipartite. A legal u->v removes2 at u and adds1 at adjacent v. Clearing ends at one pebble anywhere; stacking ends at a positive pile anywhere. No pebble may be discarded. Exact thresholds are least t>=2; source monotonicity applies only above order. No zero/one-vertex extension.

## 1. Fresh cold audit of S006

Theorems23-25 survive the following independent rederivation. Following each final pebble partitions all original labelled pebbles into exact binary ancestry trees. Two children have the same vertex label and their parent an adjacent label. Postorder evaluation on designated inputs is legal even with overlapping graph paths and other piles. A clearing goal is one such tree, a stacking goal a nonempty forest; concatenation leaves all outputs at their common root and never merges arbitrary stacks as single pebbles.

For a fixed off-source vector, every subtree uses a componentwise subvector. An ancestor/descendant repetition of the full state fixes that vector and the zero/positive source kind and residue. All intervening siblings have zero off-source vector and are nonempty, hence contribute positive source count. Replacing the ancestor subtree by the descendant strictly decreases that count in the same residue state. Zero-source repetition cannot occur. This justifies the minimal-tree height bound; forest types must be separate. The pure case minimizes positive leaf count and has3n states. Infinity certificates require that no production from finite children has an infinite parent; finite attaining trees plus all inequalities prove exact minima, rather than the optimizer merely stabilizing.

The +3 reduction begins with at least4 source pebbles to preserve a positive base; it never fills a zero-source cell. Non-bipartite opposite-parity walks realize residues1/2 at a neighbour, whose merge gives residue0 at the prescribed root. Bipartite rooted clearing retains its signed residue restriction. Lemma26 costs p=2^(d+1)-2 designated source pebbles, returns1, and therefore has net cost p-1, including d=1. At each successive absorption the remaining L>=1 reserve provides the extra credit. Other piles and shared path vertices are untouched as designated inputs. Corollary27 restores multiples3 only on occupied support. The AS-ray last loser uses the positive residue starts3,1,2. All ones supplies L_AS>=n. None of these establishes general-versus-binary extremal domination.

All five S006 check-only tools and the inherited geodesic/pure6/deferred-debt trace checker passed in this fresh session. This is a fresh-session mathematical audit and distinct implementation replay, not a separate human review or Lean kernel proof. Previously retained scopes/cutoffs are unchanged. The primary sources remain v1 with unchanged PDF hashes; April6.1 and October Lemma4.7/pullback/+3 proof portions were re-inspected. Private correspondence remains owner-supplied, not a public correction. Earlier TreeStack arXiv:2609.31811 and registered package remain earlier results; no new build.

## 2. Route A: derive the comparison, and expose a dual obstruction

For goal g in {stack,clear} with its eligible graph class, define U_g(s,b,r) as the minimum positive source count, minimized over final roots, from S006's exact interface. A general positive loser c=b+N e_s in residue r satisfies N<=U_g(s,b,r)-3. The universal sufficient comparison would be

    |b|+U_g(s,b,r)-3 <= L_AS(G)

for every off-source b and every positive last loser. Proving it would bound every general loser, hence give ASH*. It is also necessary for ASH*, since each such last loser exists by exact interface tails. Thus this is an exact missing inequality, not merely a suggestive conductor reformulation.

An attempted route uses nonnegative additive potentials that do not increase along any move: w(v)<=2w(u) for every oriented edge. To certify inability to clear anywhere one would need w.c<min_q w(q). This cannot even separate the losing K3 input3e0: 3w(0)>=min_q w(q) for every nonnegative w. Restricting to positive weights does not repair it; allowing arbitrary signed weights also gives 3w(0)>=min w when w(0)>=0, while move-monotonicity in both edge directions forces w>=0 (w(v)<=2w(u)<=4w(v) implies w(v)>=0). Thus **this entire scalar monotone linear separation scheme is insufficient**, with a precise graph loser, not an abstract lower-set counterexample. K3 at3e0 has only the initial state and (1,1,0)/(1,0,1) reachable; all are non-goals. No independent computation is needed for this three-state proof.

For rooted stacking, forest concatenation supplies a subadditive winning construction across off-source sums and residues. It does not give the required maximum-hole comparison: splitting a general vector into binary pieces adds their separate fuel penalties and may produce several roots. For clearing two outputs must be combined through an edge with their target labels retained; ordinary subadditivity at a root is unavailable. Neither inequality reverses to a loss-preserving concentration. The P3 fixed-residue class failure is retained, as is the cyclic geodesic witness failure. This rejects the proposed scalar dual, not all dual certificates or ASH*.

The Q-selection quantifiers remain distinct: every global Q maximizer being AS implies some AS Q maximizer, which implies ASH*. A mixed tie rejects only the strongest claim; a fixed-support/residue maximum says nothing about global maximization. None of these auxiliary selection assertions is newly proved by the leaf credit construction.

## 3. Route B: a uniform boundary resource theorem

**Lemma28 (selected ancestry credit).** Let T be a finite rooted spanning tree of H, root u, height h>=0, depth d(v). Put

    M(T,u)=sum_v 2^(h-d(v)).

Any configuration on H of mass>M(T,u) can produce two designated pebbles at u using at most2^(h+1) original pebbles. All remaining original pebbles are untouched in that selected schedule.

Proof. Ignore non-tree edges and repeatedly move pairs from a non-root vertex to its parent until at least two pebbles occur at u, or until no non-root pair remains. Total mass decreases at every move, so this terminates. Track each pebble's disjoint original ancestry tree. Every edge strictly reduces depth. A token at vertex v has ancestry height at most h-d(v), hence at most2^(h-d(v)) original leaves. If production fails, root has at most1 token and each non-root at most1. Since these tokens partition every original pebble, initial mass is at most M, contrary to hypothesis. Choose two root tokens. Each has at most2^h leaves. Evaluate only their disjoint ancestry trees from the initial configuration, in postorder. Omit all simulated moves whose descendants are not selected. These trees consume K<=2^(h+1) labelled original pebbles and leave2 at u, so their actual move count is exactly K-2. Other pebbles never enter the designated moves. Initial root pebbles may be selected as leaf trees. QED.

The omission of unused simulated histories is essential: executing an entire greedy simulation can lose additional pebbles in unrelated residual trees. The complete proof and final implementation replay only the two selected trees; initial bounded traces of the unselected greedy procedure also passed, but do not justify the claimed symbolic credit bound.

**Lemma29 (one-leaf clearing extension).** Suppose H is finite connected non-bipartite of order n, every configuration of mass>=g clears, and g>n. Attach a new leaf x at u. If a rooted spanning tree (T,u) of height h satisfies M(T,u)<2g and 2^(h+1)<=g+1, then every configuration on H+x of mass>=2g+2 clears.

Proof. It suffices to treat exact mass t=2g+2, which exceeds order n+1; larger configurations can be reduced by legal moves to this layer (October Lemma4.7). Write m=c(x).

- If m is even, m/2 moves x->u remove the leaf. Remaining core mass is t-m/2>=t/2=g+1.
- If m is odd and m>=5, first make (m-1)/2 moves x->u, leaving1 at x and at least2 newly supplied at u. Then u->x and x->u empty x. The core mass is t-(m+3)/2. Since t is even and m odd, the original core has odd mass a=t-m>=1, so this is (t+a-3)/2>=g. No external credit was assumed.
- If m=1, the core has mass2g+1>M. Lemma28 produces two pebbles at u with K<=g+1 designated inputs and K-2 moves. Perform u->x and x->u, emptying x and leaving a core of mass (2g+1)-(K-2)-1=2g+2-K>=g+1.
- If m=3, first x->u leaves1 at x and a core of mass2g>M. Produce the two selected pebbles as above, then use the same two-move debt cycle. Core mass is 2g-(K-2)-1=2g+1-K>=g.

In every case the core is nonnegative, has mass>=g, and all off-core pebbles were legally consumed, so its clearing sequence finishes the proof. Its final root may be anywhere in H; we never imported an unrooted threshold as a rooted boundary threshold. A leaf-target win at small mass is neither needed nor rejected by this sufficient large-mass theorem. QED.

## 4. Sharp infinite cyclic family

**Theorem30.** For every integer l>=0, clear(G_l)=6*2^l-2, and ASH*-clear holds on G_l.

Proof of upper. For K3 every mass4 configuration clears. Up to permutation the four shapes and complete reductions are: (4,0,0)->(2,1,0)->(0,2,0)->(1,0,0); (3,1,0)->(1,2,0)->(2,0,0)->(0,0,1); (2,2,0)->(0,2,1)->(0,0,2)->(1,0,0); (2,1,1)->(0,2,1)->(0,0,2)->(1,0,0). These use actual triangle edges and end with one pebble. Larger masses reduce to4 by monotonicity.

For the step, root a spanning tree of G_l at its tip, deleting triangle edge1-2. Its height is h=l+1. There is one vertex at each depth0,...,l and two at depth l+1, hence

    M=sum_(i=0..l)2^(l+1-i)+2=2^(l+2)=4*2^l.

Set g=6*2^l-2. Then M<2g and 2^(h+1)=4*2^l<=g+1, including l=0; also g>l+3. Lemma29 gives the upper 2g+2=6*2^(l+1)-2 on G_(l+1). Induction and monotonicity prove every mass at or above the claimed bound wins.

Proof of matching lower. The tip's shortest odd closed walk traverses the tail to the triangle, takes its3-cycle, and returns: length2l+3. Any odd closed walk must include a triangle edge between the two equal distance-level vertices, so it cannot be shorter. Equivalently S005 h(tip)=l+1. April Theorem6.1, cold-rederived in S005/S006, gives the nonclearable pure pile (3*2^(l+1)-3)e_tip=(6*2^l-3)e_tip. It is AS, of mass g-1. Since g>order, any smaller exact threshold would by monotonicity make this pile clearable; sizes2..order also have terminal AS losers. Thus the exact least threshold is g and the critical AS witness proves this family's ASH*-clear. QED.

For l>=1 this exact threshold is strictly above both the order bound n+1 and the independence bound3alpha+1. Indeed alpha(G_l)<=l+1 (at most one triangle vertex and at most l path vertices), so 3alpha+1<=3l+4<6*2^l-2; the latter inequality holds at l=1 and its positive difference strictly increases. The lower bound is exponential and is explicitly prior source work; the advance is the unconditional matching upper for the entire infinite family.

## 5. Separate stacking extension

**Lemma31.** Suppose H is finite connected, every mass>=g stacks, g>order(H), g>=4. Root a spanning tree at u with height h, and assume M(T,u)<2g-2 and 2^(h+1)<=g. Then attaching one leaf at u gives stack(H+x)<=2g.

Proof. Work at exact mass2g and write a for the original core mass. Even leaf piles eliminate directly, leaving at least g. For odd m>=5 and a>=3 the self-credit elimination in Lemma29 leaves (2g+a-3)/2>=g in H. When a=1 (the only other odd value), the initial input is (2g-1)e_x+e_w for a single core vertex w. Tree distance x-w is at most h+1. S006 Lemma26 absorbs e_w to x with net source cost D=2^(dist(x,w)+1)-3<=2^(h+2)-3<=2g-3, leaving at least2 at x. This is already stacked and consumes exactly every input; it asserts a winning construction, not the previously refuted distance-only losing witness.

For m=1 the core mass is2g-1>M. Select two ancestry outputs with K<=2^(h+1)<=g, then the two-move debt cycle leaves total2g-K>=g on H. For m=3 first x->u leaves a core of mass2g-2>M and one at x. This core has an initial pebble at u. In the ancestry simulation preserve/select that pebble as one of the two final root tokens; only the other needs production. Thus K<=1+2^h<=g-1, the last inequality following from g>=4 and 2^(h+1)<=g. The debt cycle leaves core mass2g-1-K>=g. Use H's stacking sequence in all remaining cases. Exact2g exceeds order(H+x), so monotonicity handles larger masses. QED.

**Corollary32.** For all l>=0, stack(G_l)<=4*2^l. The base K3 upper4 follows from its clearing construction. On G_l's spanning broom M=4*2^l=g, height l+1, so M<2g-2 and 2^(h+1)=g. Lemma31 doubles the upper. This is not an infinite exact stacking formula or ASH*-stack proof: an infinite matching AS stacking lower remains unproved here. Pure piles are already stacked and cannot supply that lower. The finite exact stack4/8/16 checks do not fill this gap.

## 6. Route C: closure of sharp odd-bound cores under pendant paths

**Theorem33.** Let H be finite simple connected non-bipartite, root u, and integer h>=1. Assume its shortest odd closed walk at u has length2h+1, clear(H)=g=3*2^h-2>order(H), and there exists a rooted spanning tree of height h with M(T,u)<2g. Attach a pendant path of l edges at u, obtaining H_l. Then for every l>=0,

    clear(H_l)=3*2^(h+l)-2,

with a critical pure-pile AS loser at the new tip (at u when l=0). In particular ASH*-clear holds throughout this entire class.

Proof. The old source lower guarantees no vertex of H has a shorter-odd-walk maximum greater than2h+1: otherwise clear(H)>g. Adding a leaf cannot create a new odd cycle or shorten an old odd closed walk. The shortest odd closed walk at the new tip is exactly the old root walk plus the outward/returning new edge, hence increases by2 at each step. Its prior pure-pile lower is therefore3*2^(h+l)-2.

For the upper apply Lemma29 inductively. Initially 2^(h+1)<=3*2^h-1=g+1. After one attachment, root the extended tree at the new leaf; its height is h+1 and

    M'=M+2^(h+1)<2g+2^(h+1)<2(2g+2),

where the last inequality follows from2^(h+1)<2g+4=6*2^h. Its new candidate g'=2g+2=3*2^(h+1)-2 exceeds its order and satisfies2^(h+2)<=g'+1. These hypotheses repeat at every step. The upper and the tip lower match; monotonicity above order and terminal lower layers give the exact least threshold. The pure loser is AS, yielding critical ASH*. QED.

This is a conditional family-transfer theorem whose hypotheses are exact independently proved facts about H, not an assumption of universal ASH*. It specializes to H=K3, h=1, g=4 and M=4<8, so Theorem30 is unconditional. It also pinpoints why arbitrary cactus blocks are not yet solved: a block may lack a sharp clearing threshold or a height-h boundary spanning tree satisfying M<2g. We do not replace these requirements by an unrooted clearing number alone.

## 7. Remaining universal implication and assurance

Dependency DAG: exact labelled ancestry (S004 Proposition17) -> Lemma28 selected credit -> Lemmas29/31 leaf extensions. Explicit K3 base + Lemma29 -> Theorem30 upper; April6.1/S005 ancestry lower -> its matching AS witness. Lemma31 -> Corollary32 stacking upper only. Lemma29 + a sharp independently known core + prior odd-walk lower -> Theorem33. None of these arrows proves Route A's general/binary inequality on all graphs.

The independent forward-successor and reverse-predecessor algorithms recompute complete labelled layers on exactly the registered l=0,1,2 graphs. Clearing:36 layers,81763 configurations,15251 constructed traces,316569 legal moves, thresholds4/10/22. Stacking:28 layers,20876 configurations,5025 traces,73132 moves, thresholds4/8/16. The trace checker imports no producer code. Reverse checks compare canonical hashes/counts of full sets, not sampled configurations; hash equality is the retained finite-comparison evidence, distinct from the symbolic universal-family proof. Critical pure AS witnesses are checked for clearing; stacking finite first-empty layers do not certify its infinite lower. Computation took seconds within the preregistered budgets. No symmetry, random inputs, new atlas or larger cutoff extension.

Theorem30 proves the numerical value382 for length6 symbolically. The old S005 length6 clearing certificate still ends at47 and its old stacking/A8 cutoffs remain unchanged: a new proof does not retroactively complete a truncated computational certificate. Likewise the S006 rooted-mask caps29/10 remain historical caps. Novelty is NOT_AUDITED; Lean NOT_STARTED; universal Phase1 IN_PROGRESS; printed mathematics PASS separate. A fresh S008 audit of the new full symbolic proof is future and unexecuted.
