# S008 — hostile audit, exact cyclic families and universal obligations

Universal critical ASH* remains OPEN, stacking and clearing separately. The S007 audit passes at the stated scopes. New complete family results below do not resolve the universal target and have no novelty or kernel certification. All graphs are finite simple; thresholds are least exact t>=2. Connected stacking and connected non-bipartite clearing are separate. Zero/one vertex graphs are not extended by these theorems. Prior TreeStack arXiv:2609.31811 and its registered package remain earlier work, not a universal ASH* proof.

## 1. Hostile S007 verdicts

| Result | Verdict | Adversarial examination and exact dependency |
|---|---|---|
| Lemma28 | PROVED | Tree edges always decrease depth; ancestry leaves at depth d have height <=h-d even if moves are interleaved. Failure tokens partition ALL original inputs. Extract exactly two disjoint root histories and replay those histories only; each costs <=2^h, actual losses K-2. Unused greedy histories are not charged. |
| Lemma29 | PROVED | Exact2g+2 has even mass. Leaf odd>=5 self-supplies two root tokens and leaves core (t+a-3)/2>=g because a is odd>=1. Leaf1/3 invoke strict M<2g and selected K<=g+1, then debt loses exactly one further core pebble. No rooted clearing threshold is imported from an unrooted one. |
| Theorem30 | PROVED | All four K3 mass4 shapes have legal three-move clears. Broom height l+1, M=4*2^l, g=6*2^l-2 meet both leaf inequalities including l=0. Prior April6.1/S005 pure-tip lower matches; monotonicity above order and terminal layers exclude every smaller exact threshold. |
| Lemma31 | PROVED | Odd leaf/core-singleton uses a positive reserve in credited pullback, net cost <=2g-3. For leaf3 preserve/select the newly supplied root singleton (cost one); other root tree costs <=2^h, giving K<=g-1. Leaf1 and even cases are separately valid. |
| Corollary32 | PROVED UPPER ONLY in S007 | The inequalities M=g<2g-2, 2^(h+1)=g hold at every step. Finite4/8/16 did not prove an infinite lower. A matching lower is newly established by Theorem35 below. |
| Theorem33 | CONDITIONALLY PROVED | Exact core clearing, root odd walk2h+1, spanning height h and M<2g are explicit hypotheses, not conclusions. New-tip odd walk increases2; M'=M+2^(h+1), g'=2g+2 preserve credit conditions. No arbitrary cactus claim. |

No substantial S007 theorem was refuted or downgraded. This is a fresh-session adversarial rederivation and distinct-code replay, not an independent human reviewer or Lean kernel audit. In Lemma31, a simulation that consumes root tokens would break the cost-one argument; the actual inward-only simulation never uses its root as a source. All original K3 traces, selected productions and debt arithmetic were rechecked. S006 Theorems23-27 were rederived as dependencies: exact labelled trees/nonempty forests, input partition, positive versus zero source, no repeated minimum state, all infinity inequalities, positive-only +3, and reserve-inclusive pullback. Five S006 and two S007 check-only replays passed. Original evidence/cutoffs remain intact.

## 2. A universal-in-length ancestry dual for the stacking gap

For triangle-tail G_l, write A=2^l. The source s is the tail tip (0 when l=0); the only other inputs are singletons at triangle vertices1,2. For a subtree/forest let B be its subset of these two singleton inputs, N its source count, and r=N mod3 when N>0. A zero-source kind is separate. Define lower labels C for a single clearing ancestry tree and S for a nonempty forest ending at a common vertex. They are lower bounds, not asserted exact minima.

Every tail vertex including0 has distance d from s, 0<=d<=l; put t=2^d. At triangle endpoints1/2 use the separate endpoint row. In each positive residue row, k is the unique element of the stated set giving the specified residue. Infinity means there is no such zero-source derivation.

| Inputs/type | Tail vertex, including0 | Triangle endpoint |
|---|---|---|
| B empty, C | t if r=t mod3; otherwise6A | 6A if r=0; 2A if r=2A mod3; 4A for the other nonzero residue |
| B empty, S | kt, k in {1,2,3}, kt=r mod3 | 2kA, k in {1,2,3}, 2kA=r mod3 |
| B nonempty, either C or S | 4A-kt, k in {0,1,2}, 4A-kt=r mod3 | (4-k)A, k in {0,1,2}, (4-k)A=r mod3 |
| N=0, either type | infinity | zero only for B={endpoint itself}; infinity otherwise |

**Lemma34 (symbolic ancestry lower certificate).** Every such tree/forest has N at least its finite label; a kind labelled infinity is impossible. This holds for every integer l>=0 and every possible final vertex.

Proof. The source base leaf has N=1 and label1 (at d=0; for l=0 at0,A=1). Each singleton base has zero label at its own endpoint. There are no other base leaves. We verify C(parent)<=C(child1)+C(child2) for every legal tree merge on an edge, S<=C for every forest seed, and S(parent)<=S(child1)+S(child2) for concatenation at one vertex. The off-source subsets must be disjoint; two positive/zero source kinds combine by their encoded residues, with zero retained only when both are zero. This is sufficient by structural induction on the exact labelled ancestry tree/forest, with no legality relaxation.

Here are the complete inequality cases. For empty B in C, the good-residue cost is t on the tail. Merging two good costs on adjacent tail levels gives2t and the good residue at either neighbour (the inward required cost is t/2, outward2t). If either child is a bad/zero-residue positive tree, its cost6A bounds every tail parent label; two such children also suffice. Across0--endpoint, two good A-cost children give the good2A endpoint cost. Every other pair costs at least7A or12A, exceeding the endpoint's maximum6A. Conversely at an endpoint, the costs2A,4A,6A obey: 2A+2A produces core good residue with costA or the other endpoint cost4A; 2A+4A produces residue0,cost6A; 4A+4A covers every resulting parent. A6A child covers all remaining pairs. These enumerate the pure tree rules on every edge.

For nonempty B and two nonempty children, each cost is >=2A at any vertex, so their sum>=4A bounds every positive parent label. For one nonempty child and a pure child on the tail, a bad pure child costs6A and suffices. For a good pure child of cost t, write the nonempty cost4A-kt with k=0,1,2. The sum is4A+(1-k)t. At either neighbour the new coefficient is k'=2(k-1) mod3 in {0,1,2}, namely1,0,2 respectively. With inward unit t/2 or outward unit2t, each required label is <=that sum. At0--endpoint, the corresponding good pure costA gives sums5A,4A,3A and required endpoint costs2A,4A,3A. In the other direction a pure endpoint costs >=2A, so any nonempty pair totals>=4A. Equal-endpoint edges obey the same bound. A zero-source singleton tree can merge only at its own endpoint; with a pure endpoint child the required nonempty label is <=2A/4A/6A as appropriate, while with the other singleton's positive tree the required label is unchanged. Two zero-source trees cannot merge with disjoint permitted inputs at the same vertex. Thus no finite children produce an infinity-labelled kind.

For forest seeds the displayed S label is <=C: pure tail S costs at most3t<=3A versus bad C6A; pure endpoints have equal or smaller costs; nonempty/zero labels coincide. Pure forest concatenation uses the least positive representative k=1,2,3, hence the required cost is no greater than the sum. At a tail vertex one nonempty child4A-kt and a pure forest child jt (j=1,2,3) require4A-k't where k'=(k-j) mod3 in {0,1,2}; k'>=k-j, giving the inequality. At an endpoint the pure forest costs at least2A, so the total is >=4A. Two nonempty forests again total>=4A. Concatenating a zero singleton to a pure endpoint forest gives required costs2A/4A/3A versus supplied2A/4A/6A; concatenating it to the other singleton's positive forest leaves the bound unchanged. No two disjoint zero singleton forests share a root. These exhaust all bases, merges, seeds and concatenations. Structural induction proves both labels and all infinity exclusions. QED.

The independent algebra checker enumerates4376 encoded production cases (including both parities) and proves each difference alpha*A+beta*t nonnegative by alpha>=0 and ratio*alpha+beta>=0 for A>=ratio*t>0. Internal edges use ratio2; single-vertex forest rules ratio1. Core edges use multiples of A. This is a finite check of universal symbolic inequalities, not checking4376 graph sizes. The complete written case argument above is the proof; no unexplained evaluator/native theorem is used.

**Theorem35 (exact triangle-tail stacking).** For every l>=0,

    stack(G_l)=4*2^l,

and ASH*-stack holds on this family.

Proof. The new AS configuration c_l=(4A-3)e_s+e_1+e_2 has total4A-1 and positive source residue4A mod3. Any stacking sequence consumes every input in a nonempty common-root forest. Its subset B is {1,2}; for this residue Lemma34 has k=0 at EVERY final vertex, so it requires at least4A source pebbles. But c_l has4A-3. Thus c_l is non-stackable, including cyclic schedules and arbitrary final roots. S007 Corollary32 gives the all-configuration upper4A. This exceeds order l+3; source monotonicity above order and terminal AS configurations at sizes2..order exclude every earlier exact threshold. The matching AS loser proves critical ASH*. QED.

This is not the refuted distance-only two-site assertion: both core singleton labels and all final forest roots are retained. Pure piles are already stacked. CAM-S008-01 independently certifies the exact named buffer for l0..8, and complete candidate closures for l0..3; those are support checks, distinct from the all-length proof.

## 3. A broader branching class with sharp distinct thresholds

Let F_k, k>=1, have triangle0/1/2 and leaves3,...,k+2, each adjacent0. No other edges. Its order is k+3. This branching family is different from a length-k tail; it does not assume sharp odd-bound clearing or Theorem33's hypotheses.

**Theorem36.** For every k>=1,

    stack(F_k)=3k+5,    clear(F_k)=3k+7,

with AS critical losers for both goals.

Upper proof. Fix exact mass t=3k+5 (stack) or3k+7 (clear). First send pairs from1 and2 to0, leaving epsilon_1,epsilon_2 in {0,1}. For a leaf count m define phi(m)=m/2 when even and (m-3)/2 when odd. Eliminate all even leaves by outward pairs to0. Eliminate odd m>=5 by pairs leaving one, then the two moves0->leaf,leaf->0; the two required root pebbles are supplied by that leaf itself. These operations add phi(m)>=0 to0. Next handle m=3 by its first outward pair and the same two-move cycle (net0), and m=1 by that cycle (net-1). The latter operations need root count >=1 and>=2 respectively.

The final root count prescribed by this normalization is

    B=c(0)+floor(c(1)/2)+floor(c(2)/2)+sum_leaves phi(m)
     =(t+c(0)-epsilon_1-epsilon_2-3o)/2,

where o<=k is the number of odd leaves. In stacking B>=(5-2)/2, hence integral B>=2. In clearing B>=(7-2)/2, hence B>=3, and final core mass B+epsilon_1+epsilon_2=(t+c(0)+epsilon_1+epsilon_2-3o)/2>=7/2, hence>=4. Before paying the negative m=1 debts the root count is B plus their number; paying any debt leaves at least B>=2. The m=3 operations have enough root credit and net0. Thus the entire specified normalization is legal, never merely a balance equation.

For clearing, K3's mass>=4 theorem completes. For stacking, the core (B,epsilon_1,epsilon_2) is already stacked if both epsilons vanish; with B=2 and exactly one epsilon it stacks by0->that endpoint; every other non-stacked case has core mass>=4 and clears using K3. Monotonicity above order gives both at-least uppers.

Lower proof uses R(0)=1 and R(v)=2 for all other vertices. A move out of0 preserves weight; a leaf or triangle-endpoint move into0 loses3; a1--2 move loses2. All weights are nonnegative and every legal move is accounted for. This is a graph-specific weight-loss/chronology argument, not the scalar separation scheme refuted in S007.

Clearing candidate: (2k+7)e_3 + sum_{v=4..k+2}e_v, mass3k+6. All k leaf counts are odd, initial weight6k+12, triangle empty. If final singleton is outside the leaves, each leaf must receive an odd number b_i>=1 from0 and emit f_i=(m_i+b_i)/2, so sum f_i>=2k+3, losing at least6k+9. At most weight3 remains for other losses plus the goal. The star without1--2 is bipartite; its signed mod3 invariant initially0 cannot become a singleton, so at least one1--2 move is required. If the goal is1/2, its weight2 plus this loss2 exceed3. If the goal is0, an equal-edge output must eventually return from the triangle to0, losing another3; its total costs plus final weight exceed3. If final singleton is a leaf x, the other leaves need b_i>=1, and b_x is even>=0; sum f_i>=(3k+6-1+k-1)/2=2k+2. Thus weight<=6 remains. Again a1--2 move is required, and the triangle must subsequently send a pebble to0 to empty itself. Losses2+3 plus final leaf weight2 exceed6. All targets are excluded.

Stacking candidate: (2k+3)e_3 + sum_{v=4..k+2}e_v + e_1+e_2, mass3k+4. Initial weight6k+8, total leaf mass3k+2, all leaf counts odd. Any stacking sequence has a final move into its final vertex, because its initial support has at least three vertices; therefore the final vertex receives at least one incoming pebble.

If the final vertex is0 or a triangle endpoint, leaves all empty and sum leaf emissions>=2k+1, costing6k+3; only weight5 remains. To finish at0, both triangle endpoints must empty: without an equal-edge move each emits to0, loss>=6; with one there is still a last triangle move into0, loss>=2+3=5, and positive final weight makes the budget impossible. To finish at an endpoint q, let j be the number of equal-edge moves and K its final pile. If j>=2 their loss leaves weight<=1<2K. If j=1, weight congruence gives2K=2-2j=0 mod3, so K>=3, but available weight<=3. If j=0,2K=2 mod3 and2K<=5 imply K=1. At q its initial count1 and an incoming star pebble force at least one q->0 move (count equation1+b-2f=1, b>=1). The other endpoint also emits to0 to empty, giving loss>=6, again above5.

If the final vertex is a leaf x with pile K>=1, its incoming count b_x>=1 has parity K-1: b_x>=2 for odd K and>=1 for even K. Write delta=2 or1 accordingly. Other leaves have incoming count>=1. The total leaf emissions are >=(4k+1+delta-K)/2. After these losses and final weight2K, the remaining budget for triangle losses is <=(13-3delta-K)/2, which is <=3 for odd K and<=4 for even K. Emptying the two triangle endpoints costs at least6 without an equal-edge move, or at least5 with one and a final endpoint->0 move. Impossible in both cases. Every stacking target is excluded.

Both candidates are AS and have the upper minus one mass. The uppers exceed order; monotonicity and terminal low layers give the exact least thresholds and both critical ASH* assertions. QED.

For k>=2, the clearing value3k+7 strictly exceeds both the odd-walk lower10 and independence lower3(k+1)+1=3k+4. Thus arbitrary branch composition cannot be reduced to the maximum rooted odd-walk invariant. The source odd-walk lower and independent-set bound remain credited; this theorem supplies the separate all-distribution upper and matching AS obstructions. Novelty is NOT_AUDITED; S009 must compare the exact result and proof to prior art.

## 4. Continued universal research: exact algebra and simultaneous tightness

The universal conductor comparison is still

    |b|+U_goal(s,b,r)-3 <= L_AS(G)

for every positive last-losing ray, with minimum over ALL final roots. S006 gives exact interfaces but no such domination. The new tip dual is a lower bound for one binary buffer; it cannot prove an upper comparison for all arbitrary buffers. The branching theorem also shows why maximum odd-walk height alone cannot supply the required clearing upper.

**Proposition37 (finite support-residue ideal and critical tightness).** Fix an eligible goal and finite G,n>=2. For a nonempty support S choose rho(v) in {1,2,3} on S, zero elsewhere. Write every configuration in that support/residue class uniquely as rho+3x, x in N^S. The winning exponent set is upward closed, has finite complement, and is exactly the monomials of an ideal J_goal,rho with finitely many componentwise-minimal generators. Rooted winning ideals have the same properties; the unrooted ideal is the sum of the rooted ideals. If c is a global largest-mass loser L, then for EVERY occupied s,

    U_goal(s,c off s,c(s) mod3)=c(s)+3.

Proof. At every occupied site the credited +3 operation reduces c+3e_v to c without disturbing designated other pebbles. Iterating gives exponent upward closure for each fixed goal/root. S006 Corollary27 supplies a finite rooted bound B: any coordinate >=B wins at a prescribed root. Hence a losing exponent has rho(v)+3x(v)<B for each occupied v. Its exponent lies in a finite box; the complement is finite. A minimal winning exponent cannot have a coordinate above the corresponding first sure-winning pure-axis exponent, because it would then dominate a smaller winning exponent. Thus generators are finite without invoking an unproved algebraic finiteness theorem. Upward closure makes their monomial ideal exact. A monomial belongs to the sum of rooted monomial ideals iff one root's generator divides it, exactly the existential final-root predicate. For global largest loser c, c+3e_s wins by finite maximality. Its exact positive ray minimum cannot be <=c(s), or c would win; the next positive number of that residue is c(s)+3, so the minimum equals it. QED.

This reformulation retains support: adding3 at a zero coordinate changes the class and is NOT licensed by the occupied-site closure. Almost-stacked exponents require rho(v)<=1 and x(v)=0 off one distinguished vertex. Every class contributes its largest standard-monomial mass |rho|+3 degree(x); the universal conjecture asserts that the maximum across all classes is attained in that AS subcollection. Simultaneous tightness is a necessary condition for a critical non-AS counterexample, not a sufficient criticality certificate.

The graph ancestry imposes cross-class carries: when two input vectors rho_a+3x_a and rho_b+3x_b combine, rho_new is the positive representative1/2/3 of rho_a+rho_b at each occupied coordinate (zero only at an empty coordinate), and

    x_new=x_a+x_b+(rho_a+rho_b-rho_new)/3.

The carry is0 or1 componentwise. Clearing combines TWO trees at the SAME child vertex and moves their outputs across an edge; stacking concatenates forests only at a COMMON final root. These are the precise extra graph constraints that a universal ideal theorem would have to use. Dropping the carry, the positive/zero distinction, or the root type destroys exact input consumption. No cross-class comparison follows merely from the ideals being finite.

We attempted three universal steps and did not silently treat them as proved:

1. **Axis extremality from upward closure.** False as a logical inference: the abstract ideal (X^3,Y^3) has largest standard monomial X^2Y^2 of degree4, while either axis reaches degree2. Even symmetry and finite complement do not fix this. This is NOT a graph counterexample; realizing such incompatible holes with all actual ancestry productions is the missing disproof obligation.
2. **Rooted winning concatenation gives hole domination.** It gives constructions for stacking inputs whose common-root forests can be joined. It supplies an upper bound on a sum of fuel requirements, not the needed maximum-hole inequality. In clearing two root outputs do not clear at the same vertex; they must merge across an edge. Replacing minimum-over-roots by a prescribed root already fails on K3 pure5. The obstruction is both the carry/class change and final-root alignment.
3. **Surplus-token surgery at a Q-maximal critical loser.** Proposition37 gives winning trees/forests for c+3e_s at every occupied s. Removing those three input leaves can affect as many as three distinct forest components and leave multiple unmatched roots; the +3 operation only removes surplus at its original occupied vertex. A mass-preserving transfer between two heavy sites therefore needs a new legal reconstruction lemma. P3 fixed-residue classes, the C5 same-layer compression failure and terminal K3 rule out assuming a simple local version. Every-global-Q-maximizer-AS, existence-of-an-AS-Q-maximizer and ASH* remain distinct; none is newly proved.

The next useful universal lemma is now precise: use the full carry-sensitive ancestry relations to prove that a largest standard-monomial mass across ALL support/residue ideals has an AS representative, or construct a graph where it does not. An upper proof must provide attaining legal trees/forests for the required arbitrary-buffer conductors, not merely lower dual labels. A disproof may use production lower certificates for a non-AS ray plus complete binary-buffer upper certificates, but must still establish the exact global threshold and critical AS layer with two independent validators under rule7.

## 5. Broader clearing and counterexample priorities

Theorem33 additionally applies to already threshold-certified C5 and C7 cores: their cited computed exact clearing values10 and22, root shortest odd walks5 and7, and the spanning two-arm tree with height2/3, M=10/22<2g meet every hypothesis. Thus pendant l-edge extensions have exact clearing12*2^l-2 or24*2^l-2, with the prior pure-tip AS lower. This is a proved consequence conditional on the retained finite core certificates, not an unconditional all-odd-cycle core theorem. It uses no expansion of old computational cutoffs. The new F_k theorem settles simultaneous branches at a triangle root even where sharp-odd transfer is inapplicable; paths and branches are genuinely different boundary demands.

General cactus/odd-cycle upper proofs still need exact root-target/residue/credit interfaces through which outside schedules may return. A whole-graph box grammar is not yet a fixed-size block interface. S007's sufficient selected-credit condition can prove uppers when its inequalities hold, but cannot certify that other configurations lose. The F_k weight proof succeeds because every non-root is adjacent0 and only one peripheral edge has nonzero same-level loss. A second cyclic block breaks that small loss accounting; that is a research lead, not a proved minimal-counterexample exclusion.

Ranked routes after S008:

| Priority | Proof/disproof route | First unresolved obligation |
|---|---|---|
| 1 | Carry-sensitive exact ancestry/conductor extremal comparison | A global across-class maximum-hole theorem or graph-realized separation, retaining all final roots and zero kinds |
| 2 | Global critical Q/lex extremizer with simultaneous tight rays | Legal surplus-tree surgery proving existence of an AS extremizer; no local convexity assumption |
| 3 | Compositional cyclic boundary certificates / minimal non-tree counterexample | Uniform rooted tree/forest message that covers excursions, credit and ancestry consumption; general cactus and odd-cycle uppers remain open |
| 4 | Proof-derived counterexample challenges in overlapping cycle/branch obstructions | A preregistered specific failed inequality with exact non-AS loser AND complete AS/global threshold certification; no new blanket census |

The priority-one PRIMARY-SOURCE originality investigation in S009 comes before all four research routes, to determine which of these mechanisms and surviving theorems are known/equivalent. This is foundational work authorized by the owner, not advancement to publication. No route is declared solved or universally promising by finite agreement alone.

## 6. Evidence, assurance and dependencies

Dependency DAG: exact labelled ancestry (S004 Proposition17/S00623-25) -> Lemma34 production lower labels -> Theorem35 lower; S00731/32 -> its upper. Selected-credit28 -> leaf29/31 -> S00730/33. Explicit K3 base -> Theorem36 normalization upper; exact signed mod3/weight loss and final-move chronology -> its independent lower. Positive-only +3 and S006 finite rooted bound -> Proposition37; its missing cross-class extremal step remains unproved. Prior April6.1 supplies clearing odd-walk lower in S00730/33 and their C5/C7 extension consequences. TreeStack is a credited separate prior theorem.

CAM-S008-01: nine exact named-buffer grammar/forest certificates l0..8, all production/infinity/attaining input/legality checks;774 finite forest witnesses. Complete forward reachable closures and independent reverse goal recurrence for c_l at l0..3 have1/14/101/891 states and no stacking goal. They do not claim all configurations or larger closures. Symbolic certificate checks4376 universally nonnegative linear differences and all bases; infinite theorem relies on the written proof.

CAM-S008-02: only F_k,k1..3, both goals.72 complete labelled layers,127799 configurations;36173 constructive threshold traces and479591 legal moves independently checked. Full forward/reverse ordered set hashes/counts agree and both registered AS critical losers occur in losing layers. No symmetry or stochastic search. Code/environment/input/output/plans are hashed; raw evidence and failures are retained. This does not extrapolate thresholds to larger k; Theorem36 is symbolic.

All inherited S005 A8/tail6 and S006 mask cutoffs remain unchanged. S007's triangle-tail6 clearing382 and S008 stacking256 are symbolic results, not completion of those truncated certificates. Primary October/April remain v1 with the same PDF hashes; selected definitions, monotonicity, pullback/+3 and April6.1 proofs were inspected again, not inferred from abstracts. No source paper is mirrored. Earlier TreeStack conventions/credit and owner-supplied correspondence provenance remain separate. No comprehensive prior-art or priority verdict was performed in S008. No Lean, registration, manuscript, submission or contact. Universal Phase1 IN_PROGRESS; S009 strictly FUTURE/UNEXECUTED.
