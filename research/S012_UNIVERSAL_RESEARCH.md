# S012: reciprocal insertion languages and losing-history barriers

Universal critical ASH* remains OPEN for STACK and CLEAR separately. Graphs here are finite simple undirected; threshold claims require connected n>=2, and CLEAR additionally non-bipartite. A move removes TWO at its source and creates ONE at a true neighbor. Every successful history below consumes every original input, with positive final stack or exactly one final pebble. AS means at most one coordinate greater than one. Printed-form refutations/PASS and earlier TreeStack arXiv:2609.31811/registered package remain separate credited results.

This session first cold-challenged S01153-58 and their S010 dependencies. They survive at their stated scopes; twelve check-only replays pass with historical bytes unchanged. Original SRC-0036 ordering2.7, BOTH cases including the pending-multiplicity split, and2.8-2.10 were re-read before reuse. Terminal forests must be nonempty, all used labels reach the terminal SET, forward moves consume two, and reverse grammar consumes one variable. S01155a still needs gap>=2; S01157 still needs its donor-root/output assumptions. This is local hostile review plus independently written computational checks, not independent human or kernel certification.

Write x -> kq for an exact history ending in k pebbles at q; write R_k(x) for all such roots. Root-padding cancellation S01047 and full three-output deletion reflection S01050 have their audited original hypotheses. They retain cycles, repeated labels and all unmarked trees.

## 1. Exact reciprocal insertion languages

**Theorem59 (marked-input reciprocity).** Let x>=0, x(w)>=1, q any vertex, and k in {1,2}. Then

    x -> kq  iff  x-e_w+(3-k)e_q -> 2w.

Proof. From x -> kq, leave the added 3-k pebbles at q untouched during that history, obtaining exactly3q from x+(3-k)e_q. Delete ONE designated original w input and apply S01050 to this entire forest. This yields exactly2w from x-e_w+(3-k)e_q, consuming all its inputs. Conversely, pad the displayed TWO history with one original w to obtain3w from x+(3-k)e_q. There is at least one original q input in this padded configuration because 3-k>=1. Reflect after deleting one q: x+(2-k)e_q ->2q. Cancel p=2-k root inputs from pile2 using S01047; 2>p, and the result is exactly kq from x. This also handles w=q, zero-length marked walks and repeated labels. There is no assertion for k=3 via an empty terminal vector. QED.

For ANY base c>=0, including c=0, define D_c(w)=R_2(c+e_w). Applying59 to the inserted input gives

    q in D_c(w) iff w in D_c(q),
    q in R_1(c+e_w) iff w in R_2(c+2e_q).

Thus D is an ACTUAL symmetric relation on the same base input, not arbitrary independently assigned masks. If c is a CLEAR loser, D has no loop: c+e_w ->2w would cancel to c ->1w. A critical STACK loser supplies nonempty D at every site by S01158, so D is the adjacency relation of an undirected loopless graph without isolated vertices. The bipartite part restrictions from S01156 remain.

**Corollary59a (protected TWO normal form, exact zero bit).** For c!=0,

    R_2(c+2e_q) = union_{z adjacent q} D_c(z).

Every positive membership has a history beginning by moving the TWO added q inputs to one neighbor z, then consuming exactly c+e_z. For c=0 the answer is {q}; in a formula valid for all c, add the separate term {q} if c=0 and the empty set otherwise.

Proof. For any proposed output w, reciprocity says c+2q ->2w iff c+w ->1q. When c!=0 this last input has mass>=2, so its last move is z->q with the entire preceding configuration exactly2z. Thus z belongs to D_c(w). Symmetry gives w in D_c(z), establishing the equality and the claimed first-move history. If c=0, input2q already realizes the TWO goal without a move, and any move lowers its mass, so no other TWO root exists. QED.

The first computational run exposed precisely this zero-base exception in a draft that omitted it. The failure and original preflight are retained; amendment3 corrects both independently written implementations before rerun. No incorrect normal form was accepted as a theorem. Neither the exception nor the corrected equality is ASH* evidence.

**Corollary59b (symmetry alone remains insufficient).** On abstract labelled G=C6, assign D the matching01,23,45, put C_w=N_G(D_w), S_w=D_w union C_w. D is symmetric, loopless, has no isolates, respects opposite-part TWO typing, and every w lies in C_w. Nevertheless intersection_w S_w is empty. For example S_0={0,1,2}, S_1={5,0,1}, S_2={2,3,4}, and intersecting all six gives empty. This is an assigned-set proof, NOT a realization by insertions of one configuration. It rejects inference from symmetry/typing/self-root tests alone. S011's directed assigned C5 pattern is now excluded by reciprocity, but that does not prove common roots for actual inputs.

## 2. Exact donor exceptions as original-input identities

**Theorem60 (donor-one/two root languages).** Fix s!=t and c>=0. All displayed goals are exact and rooted. For c(s)>=1 and d=c-e_s+e_t,

    d ->1s iff c+e_s ->2t,
    d ->2s iff c ->2t.

For c(s)>=2 and d=c-2e_s+2e_t,

    d ->1s iff c ->1t,
    d ->2s iff c-e_s ->1t.

No adjacency assumption is needed for these four identities.

Proof. In each d, designate one receiver input at t; it exists even when t was empty in c. Theorem59 gives d ->ks iff d-e_t+(3-k)e_s ->2t. For a=1, k1 gives c+e_s, and k2 gives c. For a=2, k1 gives c+e_t, whose TWO-at-t history is equivalent to c ->1t by root-padding cancellation and its converse padding. For a=2,k2 it gives c-e_s+e_t, whose TWO-at-t history similarly cancels to c-e_s ->1t. All subtracted inputs are present, every final root is positive, and no isolated component or original input is dropped. QED.

For a STACK loser c, the unit donor-TWO and double donor-CLEAR outcomes are impossible. Its unit donor-CLEAR exception is exactly the actual D_c edge st; its double donor-TWO exception is exactly receiver-root CLEAR membership of c-e_s. If st is an edge, S01157 excludes every other donor pile after reduction to1/2/3. For separated sites the mixed terminal demand remains real and cannot be treated as an adjacent pair. These identities sharpen the older conditional transport to exact SAME-input language comparisons; they do not provide the missing donor-root certificate for an unrooted winner.

Actual diagnostic: C5 edges01,12,23,34,04, c=(0,1,0,3,3) is a non-AS critical STACK loser of mass7, with stack(C5)=8. With s3,t4 the unit transfer d1=(0,1,0,2,4) CLEARs at3. The double transfer d2=(0,1,0,1,5) wins elsewhere and has NO donor-root ONE/TWO/THREE output. Both transfers increase Q. Complete negative closures and literal positive histories are retained in CAM03. This c has Q19, below the whole-layer Q maximum27 attained by AS inputs. It refutes a criticality-only donor-root availability shortcut, not a global-Q theorem or ASH*. A premature draft/commentary claimed the double transfer had the donor-TWO exception; the actual complete masks refute that claim, which is corrected and retained as a draft failure. No double-donor-TWO instance occurs among CAM03's42 transfers. The old same-layer compression failure FL0015 is not revived as a proposed route.

## 3. CLEAR: a whole-history escape barrier

Let c be stackable but not clearable and put S=R_3(c). S01154/55 give nonempty S, supp(c) subset S, connected G[S], every used label in every THREE witness inside S, and no triangular edge in any such witness when |c|>=4. Call an edge occurrence u->v forbidden if uv lies in an ambient triangle OR v is outside the ORIGINAL S.

**Theorem61 (first escape forces STACK loss).** If ANY history from c uses a forbidden occurrence, its configuration immediately after that occurrence is NOT stackable. Every later descendant also is not stackable. Consequently, writing s=stack(G), M=|c|, a forbidden occurrence at step ell satisfies

    M-ell < s.

When M>=s, every prefix of length ell<=M-s stays stackable, does not clear, and uses no forbidden occurrence. All THREE root sets of such descendants are subsets of the original S.

Proof. Suppose the descendant immediately after a forbidden occurrence stacks. It cannot clear, since prefixing its CLEAR history would clear c. It therefore reaches exactly3 at some root by the credited positive-pile +3 reduction. Prefixing gives a complete THREE history for c containing that occurrence. If its target is outside S, S01154 re-roots that very certificate to the outside label, contradicting the definition of S. If it is triangular, S01154 exposes exactly2u+2v and the known October6.4 three-move repair clears c, again a contradiction. The only stackable CLEAR loser of mass3 is a pure3 pile: a complete THREE history at that mass has no moves; any of its first moves produces two separated singletons and is nonstackable directly. Thus this boundary also satisfies the claim. STACK loss persists forward by prefixing any proposed later win. All masses>=s stack by above-order threshold monotonicity, so the nonstackable descendant has mass<s. The assertions about prefixes and root subsets follow respectively from that inequality and prefixing a THREE history. QED.

At a critical stackable CLEAR loser M=clear-1 write delta=clear-stack. If tau is the shortest first-forbidden-occurrence length (infinity if none), then

    delta <= tau.

For delta>=2 every first move is safe: each heavy vertex has ALL neighbors in S and lies on NO triangle. For delta=1 a forbidden first move is allowed, but its successor is an exact critical STACK loser of mass stack-1. This identifies the precise boundary problem; it does not solve it. For delta=0 only critical CLEAR losers that actually stack are covered.

**Corollary61a (explicit fuel bounds).** Suppose c is critical, stackable, CLEAR-losing and v is an input site. For a simple path of length d from v to a triangular vertex u, if c(v)>=2^(d+1), partial transport followed by a triangular move gives

    delta <= 2^(d+1)-1.

For a simple path of length d>=1 from v to w outside S, if c(v)>=2^d, then delta<=2^d-1.

Proof. Designate exactly the stated number of ORIGINAL source tokens and keep every other input untouched. To bring TWO to u, on path edge i=0,...,d-1 perform 2^(d-i) moves; append one triangular move. There are 2^(d+1)-2+1 moves. To bring ONE outside, perform 2^(d-i-1) moves on edge i; there are 2^d-1 moves. These sequences are legal on the designated tokens with nonnegative untouched buffer. They use a forbidden occurrence, so their full descendants are nonstackable by61; compare mass with s. d0 in the triangle case is one move using two original tokens. An earlier forbidden occurrence only strengthens the barrier, and later descendants remain nonstackable. No inputs need be consumed during the partial transport; the contradiction would prefix a complete consuming STACK history. QED.

These are exact history/fuel restrictions, not a universal odd-cycle bound. On the checked critical inputs, C5/F2 have tau3 while delta2, and triangle_tail2 has tau7 while delta6. Even the shortest escape leaves a gap; equality is not inferred.

**Corollary61b (componentwise conditional AS selection).** Delete triangular edges ONLY to define H. Suppose each component of H contains at most one vertex lying on no ambient triangle. If clear>=stack+2, EVERY critical CLEAR loser is AS.

Proof. Every such input stacks. S01155 puts its full initial support in ONE component of H; S01155a puts its heavy sites among nontriangular vertices. There is at most one such vertex in that component. QED. This improves the earlier global at-most-one condition to a componentwise one, but retains gap>=2. H is not substituted for G and its threshold is not used. In particular no statement about gap1 or arbitrary triangle-free graphs follows. When every edge is triangular the equality clear=stack is already SOURCE_STATED/credited October6.4, not a new result here.

## 4. Exact port implications without graph surgery

**Theorem62 (distinguished-output permutation).** Fix ANY base b>=0 and a nonempty LIST of labels l_1,...,l_m, allowing repetitions. The predicate

    b + sum_{j!=i} e_(l_j) ->2(l_i)

is independent of the chosen distinguished index i.

Proof. For i!=k the input has a designated original occurrence at l_k. Apply59 with k(output pile)=2 and w=l_k. It removes that ONE occurrence and adds one original l_i, producing exactly the input with index k distinguished and output2 at l_k. Reverse by the same equivalence. Repeated labels and m1 are included; occurrences, not distinct vertices, specify removed inputs. QED.

This is exact compatibility between boundary-input occurrences and a TWO output at the same port on the ORIGINAL graph. It remains valid with cycles/returns and arbitrary fixed internal inputs. Its complete derivations use full input partitions. It is not a homomorphism, deletion, contraction, gluing or threshold comparison. S01049 still requires a genuine simple quotient with established threshold equality; S01045 still retains singleton/TWO/separated output demand. Nothing here permits substituting a scalar port value, independently chosen rooted witnesses, or an abstract symmetric D for actual consuming forests. No new general threshold/AS-preserving gluing theorem was obtained.

## 5. Registered validation and exact universal obligations

CAM01: ten fixed labelled boxes, 175359 configurations, all four full root masks agree under forward versus separately written reverse propagation. It checks16394311 reciprocal/normal-form/donor identities,714 literal traces/5484 moves and69 complete critical negative closures. Two new fixed controls have exact stack=clear=8 (triangular prism) and12 (two triangles joined by edge23); both full boxes stop at14, every earlier t>=2 has a loser and the first winning layers are above n. These are COMPUTED_EXACT, not new general graph-family theorems or an atlas extension. No gap1 example was found in these two controls.

CAM02:435 complete one-step forbidden checks;15 stackable critical CLEAR inputs,1177 full closure states,78 partial-fuel witnesses/338 literal moves. Independent finite-DAG minimum-cost checking agrees with BFS on every tau and full closure. All15 have finite tau. The general theorem is symbolic; these finite checks do not prove it by extrapolation.

CAM03:42 concentrating transfers from actual critical non-AS STACK inputs,18 donor-root traces/116 moves,26 complete control negative closures/1177 states. Four transfers remain losing,38 win. Eighteen whole critical-layer graph/goal extrema have AS Q maxima and no non-AS ties; this remains finite support for a stronger conjecture. The actual local example combines a unit donor-CLEAR exception with a double-transfer win at other roots. It is not a global-Q counterexample.

All campaigns were separately preregistered and hashed, with <=600s/2GB process caps and <=300000 states per layer/input; all final runs pass without caps. The draft zero-base failure and console encoding display failure are retained. Historical cutoffs/hashes remain unchanged. Fresh local review/different algorithms are not independent human/kernel proof, and new statements await fresh S013 cold challenge.

Route A now has a true SAME-input symmetric insertion relation and higher occurrence-permutation law, but needs a theorem using their full base-input dependencies to select an AS largest loser. Symmetry/typed/self-root constraints alone fail abstractly. Route B has exact donor exception identities, but at a GLOBAL Q maximum one must force an admissible root/output/leaf partition or produce another same-mass loser; the criticality-only shortcut is disproved by actual C5. Arbitrary-buffer min-root integer-hole domination, all support/zero/positive representative/carry cases, remains unproved. Route C now has full-prefix confinement and componentwise conditional AS selection, but gap1 and general triangle-free regions survive. Route D has exact occurrence symmetry at fixed graph/inputs, not threshold/AS-preserving substitution; well-founded quotient minimality cannot discard strict threshold drops.

The missing universal implication is explicit: for a hypothetical non-AS global largest Q-maximal loser, prove the simultaneous exact insertion/transfer languages cannot realize only exceptional donors and essential cuts, OR build an AS loser of the same mass by another justified construction. For already-stackable CLEAR inputs this must preserve the whole cyclic defect and handle the first escape at gap1. None of59-62 proves this implication. No universal proof or certified ASH* counterexample was obtained; Phase1 remains IN_PROGRESS, phases2-6 unchanged/deferred.

## Dependency DAG and distinct hostile pass

59 <- audited S01047 root cancellation + S01050 full three-output reflection;59a <-59 + exact last move with mass>=2;59b <-explicit finite sets.60 <-59 + root cancellation/padding, no adjacency.61 <-S01154/55 + known +3/triangle repair + above-order threshold monotonicity, with mass3 handled directly.61a <-61 + literal binary partial transport.61b <-S01155/55a, no new threshold comparison.62 <-59 with designated repeated input occurrences. The inherited chain47/50 <- exact ancestry and SRC0036 count reconstruction is audited; earlier TreeStack is credited in inherited controls, not a hidden proof of these statements.

Hostile questions checked separately: Does reciprocity add/delete an absent token? No, all marked inputs are explicitly present; its converse adds3-k>=1 original q inputs. Is cancellation at k=p used? No, only2>2-k and2>1. Does normal form include a zero-move TWO terminal? Yes, only base0 adds {q}. Does a nonadjacent transfer produce an automatic unrooted win? No. Does a forbidden prefix need its original input to be threshold-critical? No, only the numerical gap comparison uses criticality. Is S recomputed after each move? No, confinement uses the ORIGINAL root region. Does H-edge deletion preserve loss? No such claim. Does escape-length equality or the gap1 solution follow? No. Do arbitrary symmetric masks realize input languages or imply AS? No. Entire universal DAG is still open; no human/kernel or worldwide-priority assurance is asserted.
