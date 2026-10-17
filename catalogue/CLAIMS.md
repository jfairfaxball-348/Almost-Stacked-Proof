# Claim catalogue - current after S013

Universal STACK/CLEAR OPEN; symbolic proof, finite computation, source and novelty assurance separate.

| ID | Status | Claim | Sources |
|---|---|---|---|
| CLM-0001 | SOURCE_STATED | October Hypothesis 3.2 (v1, STATEMENT_INSPECTED in S003) has the same content as April Hypothesis 9.1: least exact t>=2 such that every almost-stacked configuration of size t is stackable (connected G) / clearable (connected non-bipartite G) | SRC-0001, SRC-0002 |
| CLM-0002 | SOURCE_STATED | Even-cycle almost-stacked stackability for all sizes >= 2^(n+1)-1 (October Thm 4.10) and conditional equality (Thm 4.12); the conditional equality also follows from the critical form ASH* | SRC-0001, SRC-0002 |
| CLM-0003 | SOURCE_STATED | Odd-cycle almost-stacked clearability for all sizes >= 3*2^n-2 (October Thm 4.11) and conditional equality (Thm 4.13); also follows from ASH* | SRC-0001, SRC-0002 |
| CLM-0004 | SOURCE_STATED | Tree lower bound stack(T)>=estim(T) unconditional (October Thm 5.2, proof inspected S003), upper bound under ASH (Thm 5.4); the earlier TreeStack theorem already proves equality for \|V\|>=2 | SRC-0001 |
| CLM-0005 | SOURCE_STATED | Earlier TreeStack published/formalized tree estimator equality on nontrivial finite trees | SRC-0003 |
| CLM-0006 | SOURCE_STATED | TreeStack recorded arXiv and Palomar status | SRC-0003, SRC-0004 |
| CLM-0007 | SOURCE_STATED | Authors' atlas reports 995/995 stack and 924/924 clear passes for connected graphs 2<=n<=7; S003 inspected the public code: it tests the critical form (AS witness at level g(G)-1), not the printed least-t statement | SRC-0002, SRC-0007 |
| CLM-0008 | INHERITED_UNVERIFIED | Universal ASH true (open target record): the printed/literal form is refuted (CLM-0016, CLM-0017); the critical form ASH* remains open (CLM-0020) |  |
| CLM-0009 | PROGRAMME_PROVED | ASH false via finite counterexample: achieved for the printed (literal) form, both halves; see CLM-0016/CLM-0017 (Lean pending; S004 cold audit PASS) | SRC-0009 |
| CLM-0010 | SOURCE_STATED | Original April Hypothesis 9.1 exact universal stack connected and clear connected non-bipartite formulation; least exact t>=2 | SRC-0002 |
| CLM-0011 | COMPUTED_EXACT | W8 with center 0 and 7-cycle has stack=clear=11; every exact mass t=2..14 exhaustively checked by two distinct full-layer algorithms | SRC-0008 |
| CLM-0012 | COMPUTED_EXACT | Two disjoint K4 graphs joined by 3-4 bridge have stack=clear=13; every exact mass t=2..14 independently checked | SRC-0008 |
| CLM-0013 | PROGRAMME_PROVED | P4 c=(2,0,0,2) is nonstackable, but graph after adding edge 0-3 stacks c; arbitrary loss-preserving pile merge/general spanning-tree scoring fails |  |
| CLM-0014 | COMPUTED_EXACT | Six labeled connected eight-vertex graphs, exact masses 2..14: no literal gap within that bounded scope; S003 corrects S002: C8+chord 0-4 is non-bipartite (stack=clear=23) | SRC-0008, SRC-0009 |
| CLM-0015 | PROGRAMME_PROVED | AS-gap reformulation (S003 Thm 4): for connected G with n>=2, literal ASH_g(G) iff an AS non-g-able configuration exists at every size t with n<t<g(G); critical ASH*_g(G) iff one exists at size g(G)-1; literal implies critical | SRC-0009 |
| CLM-0016 | PROGRAMME_PROVED | Printed ASH stacking half is false: on P4 (0-1-2-3) every one of the 32 AS configurations of size 12 is stackable while (1,0,2,9) is not, so least AS threshold <=12 < stack(P4)=15; finite certificate evidence/S003/cert_P4_stack_t12.json checked by independent tools (Lean pending; S004 cold audit PASS) | SRC-0009 |
| CLM-0017 | PROGRAMME_PROVED | Printed ASH clearing half is false: on the non-bipartite bull graph (triangle 2-3-4, pendants 1-3, 0-4) every one of the 80 AS configurations of size 12 is clearable while (1,9,0,2,0) is not, so least AS threshold <=12 < clear=15; certificate evidence/S003/cert_bull_clear_t12.json (Lean pending; S004 cold audit PASS) | SRC-0009 |
| CLM-0018 | COMPUTED_EXACT | Atlas of all connected graphs with n<=6 (143; 115 non-bipartite), exact thresholds by forward and independent reverse solvers: literal stack ASH fails on 21, literal clear ASH on 19; critical form holds on all; smallest literal failures P4 (stack, n=4) and three 5-vertex graphs (clear) | SRC-0009 |
| CLM-0019 | PROGRAMME_PROVED | Critical form ASH*-stack holds for every finite tree with >=2 vertices: TreeStack theorem stack=estim (cited, formally certified in its own repository) plus October Thm 5.2 AS witness of size estim-1 (proof inspected S003) | SRC-0001, SRC-0003 |
| CLM-0020 | INHERITED_UNVERIFIED | Critical (monotone) form ASH*: for every connected G (non-bipartite for clear) the largest non-g-able size is attained by an almost-stacked configuration -- OPEN target |  |
| CLM-0021 | COMPUTED_EXACT | Exact thresholds with three agreeing solvers and no literal or critical gap: stack C6=15, C7=17, clear C7=22, stack C8=31, C8+{0,4} stack=clear=23, C8+{0,2},{4,6} 19/19, K2,6 stack=19, W8 11/11, W9 13/13 | SRC-0009 |
| CLM-0022 | COMPUTED_EXACT | Critical-layer compression fails: the 5-cycle (0-3-2-1-4-0) at t=7 has critical loser (0,0,3,3,1) not connected to an AS loser by same-mass pair transfers or even-pile merges; critical losers on n<=6 carry up to 5 heavy piles; ASH* itself still holds there | SRC-0009 |
| CLM-0023 | HEURISTIC | October Section 6 results (Cor 6.6, Thms 6.9, 6.11, 6.13) use AS stackability only at size n+1; they follow from the refuted printed form but not directly from ASH*; their conclusions are neither confirmed nor refuted here | SRC-0001 |
| CLM-0024 | HEURISTIC | Conjecture from data (P4..P8): for every n>=4 every AS configuration of size 2^n-4 on P_n is stackable, giving an infinite family of printed-ASH failures; unproved | SRC-0009 |
| CLM-0025 | PROGRAMME_PROVED | Critical form ASH*-stack holds for every complete bipartite K_{a,b} with a+b>=3: the AS configuration (2alpha+1)e_w + sum of e_x over the other vertices of the larger part has size 3alpha and is non-stackable (S003 Thm 10, mod-3 weight + ordering argument; checked exhaustively for 24 cases), combined with April Thm 8.2 stack=3alpha+1 (cited, proof not inspected) | SRC-0002, SRC-0009 |
| CLM-0026 | COMPUTED_EXACT | All 853 connected 7-vertex graphs, exact layers t<=55, forward and independent reverse solvers agreeing on every graph: stack threshold found for 845 (8 cutoff), clear for 806 of 809 non-bipartite (3 cutoff); critical form ASH* holds for every graph whose threshold was found; printed form fails on 112 (stack) and 123 (clear) -- independent replication of the authors' n<=7 atlas claim under its critical reading Historical S003 cutoff; S004 independently completes the remaining 8/3 cases (CLM-0033). | SRC-0009 |
| CLM-0027 | COMPUTED_EXACT | All 11117 connected 8-vertex graphs, exact layers t<=26: stack threshold found for 10225 (892 cutoff), clear for 10052 of 10935 non-bipartite (883 cutoff), reverse solver agreeing on every graph whose threshold was found; ASH* (stack and clear) holds on all of them; printed form fails on 613 (stack) and 612 (clear) of them, plus literal gaps inside 166/169 cutoff graphs; no claim for thresholds above 26 | SRC-0009 |
| CLM-0028 | SOURCE_STATED | Owner-supplied 2026-10-13 message from Tamás Csernák (cc Lajos Soukup) confirms intended statement is critical form ASH* at largest bad layer, stronger printed pointwise claim false, and describes upward losing-layer propagation; not a public erratum, universal theorem, or independent certificate verification | SRC-0010 |
| CLM-0029 | SOURCE_STATED | Tamás Csernák reports complete n<=7 computations and ASH* holding (SOURCE_STATED). S004 separately independently completes S003's missing 8 stack/3 clear cases, so combined programme order-seven coverage is now 853/853 and 809/809; author testimony is not itself the computation. | SRC-0010, SRC-0007, SRC-0009 |
| CLM-0030 | PROGRAMME_PROVED | Complete sparse losing recurrence: inverse predecessors plus terminal 0/1 seeds, filtered by non-goal and all-successor loss, certify every exact layer and its first empty threshold (S004 Theorem11). | SRC-0011 |
| CLM-0031 | PROGRAMME_PROVED | For any finite simple graph and independent I of size k>=2, (2k+1)e_r + sum_{x in I minus r}e_x is almost stacked of size3k and non-stackable, including graphs with internal edges outside I (S004 Theorem12; no novelty or Lean claim). | SRC-0012 |
| CLM-0032 | PROGRAMME_PROVED | ASH* holds for all connected complete multipartite graphs for stack and all non-bipartite such graphs for clear; S004 AS witness plus cited April Thms8.1-8.3 exact thresholds. More generally g=n+1 or g=3alpha+1 gives ASH* (Corollaries13-14). | SRC-0012, SRC-0002 |
| CLM-0033 | COMPUTED_EXACT | S004 complete certificates close all eight missing n7 stack and three clear thresholds; combined S003+S004 order-seven coverage 853/853 stack and 809/809 clear, AS critical losers throughout. No universal extrapolation. | SRC-0011, SRC-0009 |
| CLM-0034 | COMPUTED_EXACT | Selected labelled larger graphs: C9 stack37 clear46; triangle with length-five tail stack128; two triangles joined by length-three path stack=clear36. C10 cutoff after exact t16, triangle-tail clear>140 but undetermined. All completed layers independently replayed. Historical S004 cutoff C10 and triangle-tail clear completed independently in S005; see CLM-0046/AUDIT. | SRC-0011 |
| CLM-0035 | HEURISTIC | Global critical-layer square-potential selection is unproved: every Q maximizer AS survived S004 and completed S005 finite challenges, including every connected n<=6 graph. Strongest, existential and mixed-tie variants distinguished; ASH* itself OPEN. | SRC-0011, SRC-0012, SRC-0014 |
| CLM-0036 | PROGRAMME_PROVED | On connected edge-triangulated graphs, every mass>=4 configuration is stackable iff clearable; hence the two ASH* questions are equivalent there. Pointwise form of credited October Lemma6.4 proof (S004 Proposition15). | SRC-0012, SRC-0001 |
| CLM-0037 | PROGRAMME_PROVED | Additive legal-move invariants on connected graphs with edges are signed 3-torsion bipartite weights and are trivial on non-bipartite graphs (S004 Proposition16). | SRC-0012 |
| CLM-0038 | PROGRAMME_PROVED | Rooted clear configurations are exactly binary ancestry-language vectors; rooted stack configurations are finite nonempty sums of them, with legal postorder realization (S004 Proposition17). Balance equations alone are insufficient (K3 terminal all ones). | SRC-0012 |
| CLM-0039 | PROGRAMME_PROVED | Exact pure-pile clearing: on connected non-bipartite G, N e_r clears iff N%3!=0 or N>=3*2^h(r), first equal-distance edge height h. Prior rooted odd-walk lower bound credited; matching path/edge ancestry construction; no novelty/Lean claim. Bipartite multiples3 never clear. | SRC-0001, SRC-0002, SRC-0013 |
| CLM-0040 | PROGRAMME_PROVED | First equal-distance edge height h(r) satisfies odd(r,G)=2h(r)+1; ASH*-clear holds when the cited odd-walk lower bound clear=3*2^max(h)-2 is attained. No arbitrary upper bound or odd-cycle equality inferred. | SRC-0002, SRC-0013 |
| CLM-0041 | PROGRAMME_PROVED | Nonnegative integer move balance with acyclic support is legally schedulable, but acyclic certificates are not necessary for exact clearing: K3 at6e0 clears and admits no such balance certificate. | SRC-0013, SRC-0014 |
| CLM-0042 | PROGRAMME_PROVED | Two-site geodesic stacking obstruction is false: triangle1-2-4 with tail4-3-0 stacks (1,13,0,0,0), distance(root1,singleton0)=3; legal trace independently replayed. Bounded test506 ordered pairs n<=5 found3 failures, none at smaller orders; not ASH* counterexamples. | SRC-0013, SRC-0014 |
| CLM-0043 | PROGRAMME_PROVED | Support-preserving +3 closure: winning c with c(w)>=1 implies winning c+3e_w via source equation4.10; fixed positive support/residue losing sets are finite lower sets. This alone does not force AS extreme holes. | SRC-0001, SRC-0013 |
| CLM-0044 | COMPUTED_EXACT | Complete S005 critical-layer square/sorted-pile extremum tests on every connected n=2..6 graph and the explicitly completed larger sample; all Q maximizers and lexicographic pile maxima AS. Finite scope only; conjecture HEURISTIC. | SRC-0014 |
| CLM-0045 | COMPUTED_EXACT | Independently replayed finite S005 pure-pile clearing tests: 8619 piles on665 root/graph cases, all agree with theorem prediction; this supports but does not prove the universal classification. | SRC-0014 |
| CLM-0046 | COMPUTED_EXACT | Exact S005 C10 stack63; triangle-tail5 clear190; tail4 64/94; C5-tail3 64/94; two-triangles-path4 68/68; C8-leaf stack63. 337 threshold-complete cases, three eligible cutoffs and one ineligible bipartite sanity run; complete labelled layers independently replayed; no Lean/universal certification. | SRC-0014 |
| CLM-0047 | PROGRAMME_PROVED | Exact rooted pure-pile clearing is determined by three residue minima of a binary min-plus grammar, with attaining trees/all-production inequalities and at most3n-1 production height. Bipartite parity minimum2^distance; all residues finite on non-bipartite graphs. | SRC-0015, SRC-0012, SRC-0001 |
| CLM-0048 | PROGRAMME_PROVED | For arbitrary fixed off-source configuration, exact rooted clearing is a finite tree grammar and exact rooted stacking a nonempty forest grammar. Three positive-source minima plus separate zero-source bit determine every source pile. No scalar block-composition theorem claimed. | SRC-0015, SRC-0012, SRC-0001 |
| CLM-0049 | PROGRAMME_PROVED | Constructive pullback debt D=sum b(w)(2^(dist+1)-3) proves all rooted buffer residues finite for eligible goals; finite representative0/1/2/3 interfaces give a coarse universal rooted mass bound. No sharp threshold or ASH* conclusion. | SRC-0015, SRC-0001 |
| CLM-0050 | PROGRAMME_PROVED | Exact largest positive AS losing mass is max(\|b\|+min_q A(s,b,q,r)-3) over binary off-source b and positive last losers. Universal ASH* is precisely the still-unproved winning upper at L_AS+1, not a consequence of computing the formula. | SRC-0015 |
| CLM-0051 | PROGRAMME_PROVED | Scalar leaf net plus unrooted core clearing is false in both directions on triangle0-1-2-0 with leaf3 at0: (0,1,0,3) falsely accepted, (0,0,4,1) falsely rejected. K3 pure5 clears somewhere but cannot finish at its source. Complete closures/traces checked. | SRC-0015, SRC-0016 |
| CLM-0052 | COMPUTED_EXACT | S006 independent optimum/legality checks:153 clearing certificates,2145 attaining trees,30347 production inequalities;367 finite stacking forest cells and9161 concatenation inequalities; scopes in AUDIT, no Lean. | SRC-0016 |
| CLM-0053 | COMPUTED_EXACT | Full independent forward/reverse rooted masks agree on3155536 labelled configurations in531 layers/35 graphs;11750 pure and1508 clear-buffer comparisons plus1508 stack-buffer comparisons. Tail3 state cutoff after29, tail4 cap10; no new global threshold claims. | SRC-0016 |
| CLM-0054 | COMPUTED_EXACT | 257 inherited n<=6 critical sets have618 non-AS support/residue-class Q maxima, first P3(3,3,0) Q18 vs global AS Q26. Fixed-residue concentration fails; all global Q maxima remain AS in this finite scope only. | SRC-0016, SRC-0014 |
| CLM-0055 | PROGRAMME_PROVED | Rooted spanning-tree selected ancestry credit: mass>M=sum 2^(h-depth) produces two root pebbles from K<=2^(h+1) designated inputs; replay only chosen trees, leaving other inputs untouched. S007 Lemma28. | SRC-0017, SRC-0012 |
| CLM-0056 | PROGRAMME_PROVED | Legal leaf clearing/stacking extension bounds under explicit rooted-tree credit/M/g hypotheses; separate odd self-credit, leaf1/3 debt and core-singleton winning pullback. S007 Lemmas29/31. | SRC-0017, SRC-0015, SRC-0001 |
| CLM-0057 | PROGRAMME_PROVED | For every l>=0, triangle with pendant l-edge path has clear=6*2^l-2 and an AS pure tip loser at the critical layer; prior April6.1 lower credited, complete unconditional all-configuration upper. S007 Theorem30. | SRC-0017, SRC-0002, SRC-0013 |
| CLM-0058 | PROGRAMME_PROVED | For every l>=0, triangle-tail stack<=4*2^l; infinite matching stacking lower/ASHstar-stack remains unproved. S007 Corollary32. Historical S007 scope; S008 Theorem35 independently adds a matching all-length AS lower (CLM-0063). | SRC-0017, SRC-0015 |
| CLM-0059 | PROGRAMME_PROVED | Sharp odd-bound non-bipartite cores with boundary spanning height h and M<2g retain exact clear=3*2^(h+l)-2 under pendant path extension; explicit conditional hypotheses in S007 Theorem33. | SRC-0017, SRC-0002 |
| CLM-0060 | COMPUTED_EXACT | Independent S007 full layer hashes/counts: clear l0..2 thresholds4/10/22,81763 states/36 layers; stack4/8/16,20876 states/28 layers.15251 clear and5025 stack traces,316569/73132 moves legally replayed. Finite only. | SRC-0018 |
| CLM-0061 | PROGRAMME_PROVED | Move-monotone additive scalar weights cannot separate the K3 pure3 clearing loser; exact three-state closure nonclearing. Universal general/binary conductor inequality remains unproved. | SRC-0017 |
| CLM-0062 | PROGRAMME_PROVED | For every triangle-tail length l>=0, the explicit tree/forest lower labels for a tip pile and two core singleton inputs satisfy all bases/productions, including zero kind and every final root; S008 Lemma34, no novelty/kernel claim. | SRC-0019, SRC-0012, SRC-0015 |
| CLM-0063 | PROGRAMME_PROVED | Exact stack(G_l)=4*2^l for every triangle-tail l>=0: S007 upper plus S008 AS loser (4*2^l-3)e_tip+e1+e2, ruled out at every final forest root by Lemma34. ASH*-stack holds for this family only. | SRC-0019, SRC-0017 |
| CLM-0064 | PROGRAMME_PROVED | For triangle F_k with k>=1 leaves all attached at vertex0, stack=3k+5 and clear=3k+7; complete separate legal normalization uppers and weight/mod3/chronology AS critical lowers. S008 Theorem36, universal ASH* OPEN. | SRC-0019 |
| CLM-0065 | PROGRAMME_PROVED | Winning configurations in each fixed nonempty support/residue class form a finite-complement monomial ideal via occupied +3; rooted ideals sum for unrooted goals; every globally largest loser has U=c(s)+3 at every occupied s. S008 Proposition37, no cross-class AS domination proved. | SRC-0019, SRC-0015, SRC-0001 |
| CLM-0066 | COMPUTED_EXACT | S008 registered named-buffer l0..8 optimality/legality certificates,774 finite forest witnesses; complete candidate closures l0..3 with1/14/101/891 states;4376 universally nonnegative symbolic production differences. No whole-graph threshold census or universal ASH* certificate. | SRC-0020 |
| CLM-0067 | COMPUTED_EXACT | S008 F_k,k1..3 only, both goals:72 complete labelled layers/127799 states; full forward/reverse set hashes/counts agree;36173 upper traces/479591 legal moves independently replayed and both critical AS patterns checked. Infinite Theorem36 rests on written proof. | SRC-0020 |
| CLM-0068 | PROGRAMME_PROVED | Conditional consequence of audited S007 Theorem33 and retained COMPUTED_EXACT core thresholds: C5 and C7 with a pendant l-edge path have clear=12*2^l-2 and24*2^l-2, respectively, for l>=0, with prior pure-tip AS lower. Not an all-odd-cycle core theorem; finite core dependencies remain explicit. | SRC-0019, SRC-0017, SRC-0009 |
| CLM-0069 | HEURISTIC | Foundational S004-S008 originality/dependency classifications: known mechanisms and elementary encodings attributed, precise possible-new results/equivalence uncertainty retained; no worldwide priority or Phase2 promotion. | SRC-0033 |
| CLM-0070 | COMPUTED_EXACT | S009 fifteen inherited cold check-only commands PASS at old scopes; all S003-S008 manifests verify with frozen S006/S007 indexes; new challenge is not a human/kernel audit. | SRC-0035, SRC-0020 |
| CLM-0071 | PROGRAMME_PROVED | Exact first-return ancestry composition at any distinguished vertex: least finite substitution of consuming fragments, actual boundary singleton distinct from holes, even holes, arbitrary excursions and all rooted goals; nonempty common-root forest sum for stack. S009 Thm38. | SRC-0034, SRC-0012, SRC-0002 |
| CLM-0072 | PROGRAMME_PROVED | One-pebble insertion gives a marked walk, full sibling-input partition and unmarked final forest; every-site insertion for global largest losers. Marked deletion damages <=p final trees but can expose arbitrarily many frontier siblings. S009 Lemmas39-40, no AS selection implication. | SRC-0034, SRC-0002 |
| CLM-0073 | PROGRAMME_PROVED | At-most-two-component reconstruction shortcut refuted: critical P3 center0 loser(0,3,3) extends to(0,6,3), legally stacks into three distinct root trees each using a different marked extra input. Removing three marks damages three components. Not Q-maximal or ASH* counterexample. | SRC-0034, SRC-0035 |
| CLM-0074 | PROGRAMME_PROVED | For universal vertex a, B=c(a)+sum floor(c(v)/2)-theta((G-a)[odd])>0 gives legal rooted stack of exactlyB, by positive credit then zero/negative path tasks; sufficient only. Thus stack<=1+max_O(\|O\|+2theta). S009 Prop41. | SRC-0034, SRC-0001, SRC-0003 |
| CLM-0075 | PROGRAMME_PROVED | Dominated nonbipartite n>=4 graphs have stack<=3n-4/clear<=3n-2 via spanning S008F; if G-a has >=2 edges, stack<=3n-5 and clear<=3n-3. Sharpness/class scopes separate; n3 K3=4. S009 Cor42/Prop43. | SRC-0034, SRC-0019 |
| CLM-0076 | PROGRAMME_PROVED | If G has universal a and G-a is a star with >=2 edges plus isolates, alpha=n-2 and stack=3n-5, with S004 AS independent-set critical witness. ASH*-stack saturation subcase only; no universal or new clear equality. | SRC-0034, SRC-0012, SRC-0002 |
| CLM-0077 | PROGRAMME_PROVED | For universal a with neighbor graphH containing an edge and r isolates, clear<=max(D(H)+3,3r+7), D=max_O(\|O\|+2theta(H[O])); B3 case needs completed/protected triangular output and exact disjoint final-forest repair. S009 Prop43, cold audit S010 PASS at stated scope. | SRC-0034, SRC-0001, SRC-0003 |
| CLM-0078 | COMPUTED_EXACT | CAM-S009-01:318 registered vectors n<=5 mass<=18,53924 closure states/max3409,1694 rooted traces; exact fragment versus full forward/reverse membership agrees. CAM02:33 full layers/13088 states,3860 upper traces/41800 legal moves/795 protectedB3 ancestry partitions pass. No new exact threshold or universal claim. | SRC-0035 |
| CLM-0079 | PROGRAMME_PROVED | Correct direction of surjective simple-graph homomorphism threshold comparison is g(G0)>=g(G1), via arbitrary configuration lift and pushed legal sequences; April7.1(2) prints the reversed inequality while Cor7.5 uses the correct lower direction. This is programme reconciliation, not a posted erratum. | SRC-0033, SRC-0002 |
| CLM-0080 | COMPUTED_EXACT | S01019 inherited check-only commands PASS at unchanged scopes and S003-S009 manifests pass with frozen indexes; hostile S00938-43 audit survives. Not human/kernel certification. | SRC-0040, SRC-0034 |
| CLM-0081 | PROGRAMME_PROVED | S01044: prescribed q,k>=1,m legally realizes c to k e_q with exactly those counts iff c=k e_q+2out-in and every used vertex reaches q on positive arcs. Known one-input grammar theorem in reverse ancestry, not bare forward balance. | SRC-0038, SRC-0036, SRC-0002 |
| CLM-0082 | PROGRAMME_PROVED | S01045 finite graph-dependent arithmetic predicates describe exact first-return/interior fragments at ALL masses with paired holes/actual singleton distinct and both-direction reconstruction. Credited Parikh alternative; no constant-scalar/extremal theorem. | SRC-0038, SRC-0036, SRC-0037, SRC-0034 |
| CLM-0083 | PROGRAMME_PROVED | S01046 rooted winners exactly equal arborescence-seeded integer cone unions with nonnegative input/positive pile; root existential outside whole certificate. Maximum-hole AS selection remains open. | SRC-0038, SRC-0036 |
| CLM-0084 | PROGRAMME_PROVED | S01047-48 root padding k>p cancellation and available3-token path reversals with exact root connection; Q thin-cut/no-return and anti-excision restrictions. Donor2/root alignment/three-mark reconstruction unresolved. | SRC-0038, SRC-0036, SRC-0001 |
| CLM-0085 | PROGRAMME_PROVED | S01049 equal-threshold eligible simple homomorphic quotient AS critical loser lifts; vertex-minimal counterexample strictly drops threshold at every proper nonadjacent quotient. Contraction/deletion/attachment not licensed. | SRC-0038, SRC-0002, SRC-0033 |
| CLM-0086 | PROGRAMME_PROVED | S01050: on ANY finite undirected graph, if d reaches3e_r, EVERY occupied-site deletion d-e_w reaches exactly2e_w consuming all remaining labels. Full marked reflection and distinct connected-count derivation; no human/kernel claim. | SRC-0038, SRC-0002, SRC-0036 |
| CLM-0087 | PROGRAMME_PROVED | S01051: for a STACK loser c on connected n>=2 G, every stackable one-insertion c+e_w clears; EVERY critical STACK insertion has a consuming TREE. Individual bipartite clearing only; no fixed root, clearing threshold or three-mark inference. | SRC-0038, SRC-0001 |
| CLM-0088 | PROGRAMME_PROVED | S01052 bipartite STACK loser with nonzero signed3 admits a larger losing insertion; every global critical STACK loser signed0 and opposite-part unit transfers at its mass win. No AS selection/non-bipartite sign inference. | SRC-0038, SRC-0002 |
| CLM-0089 | COMPUTED_EXACT | CAM-S010-01 complete six-graph count sum<=5/root/pile1..4 box:37556 certificates/26274 exact legal traces/3856 weak-connectivity failures; independent fixed-count chronology/full closures. No threshold/universal claim. | SRC-0040 |
| CLM-0090 | COMPUTED_EXACT | CAM-S010-02 eight labelled graphs/fourteen inherited goal baselines:136 complete rooted layers/125481 inputs/930 insertion-root traces/7703 moves, independently forward/reverse equal. C5 no graph-wide STACK root at g8; not ASH* failure. | SRC-0040 |
| CLM-0091 | COMPUTED_EXACT | CAM-S010-03 all7289 k3 traces/all21707 occupied markings from frozen01:98878 reflected moves/2642 empty paths,1447 deleted inputs/60868 complete closure states/max122; full independent partition/count/root/literal checks. | SRC-0040 |
| CLM-0092 | HEURISTIC | Common insertion root and occupied self-site tests pass every critical loser in fourteen registered cases, including non-AS examples; universal compatibility/AS selection unproved. Graph-wide fixed-root replacement separately refuted. | SRC-0038, SRC-0040 |
| CLM-0093 | COMPUTED_EXACT | S011 cold challenge S01044-52 survives stated scopes; all25 unchanged check-only commands and historical manifests PASS. Fresh local review/replay is not independent human/kernel certification. | SRC-0041, SRC-0043 |
| CLM-0094 | PROGRAMME_PROVED | S01153 prescribed nonempty terminal vector f: exact count chronology iff c=f+2out-in and every used label reaches supp(f). Direct known reverse-grammar arbitrary-pending specialization; no rootless forest. | SRC-0041, SRC-0036 |
| CLM-0095 | PROGRAMME_PROVED | S01154 a3-output certificate re-roots to EVERY used label by simple positive path reversal, including empty transit sites; ANY positive used edge can be exposed as exact terminal2u+2v with all inputs consumed. | SRC-0041, SRC-0036 |
| CLM-0096 | PROGRAMME_PROVED | S01155/55a: stackable CLEAR loser has all occupied deletions reaching2 at their sites and every3-witness avoids ambient triangular edges. If clear>=stack+2, critical heavy sites lie on no triangle; if every vertex lies on a triangle, clear<=stack+1. With<=1 nontriangular vertex and gap>=2 ASH*-CLEAR follows conditionally. Gap1/general target open. | SRC-0041, SRC-0001 |
| CLM-0097 | PROGRAMME_PROVED | S01156 bipartite critical STACK insertion CLEAR roots lie in the insertion part, hence common CLEAR root over ALL sites impossible, including non-AS inputs/empty sites. Common STACK roots remain separate; no bipartite CLEAR threshold. | SRC-0041, SRC-0002 |
| CLM-0098 | PROGRAMME_PROVED | S01157 d=c-ae_s+ae_t reaching k at donor s gives c->(k+a-3)s+(3-a)t for a1/2,k+a>=3 via exact path reversal. Adjacent STACK criterion excludes a1k1 and a2k2; donor2/changing terminal types handled conditionally, unrooted root coverage open. | SRC-0041, SRC-0036 |
| CLM-0099 | PROGRAMME_PROVED | S01158 mass>=2 exact CLEAR roots=N(exactTWO roots), STACK roots=R1 unionR2 unionR3. Winning STACK-loser insertion has nonempty D_w=R2 excluding w,R3 empty,C_w=N(D_w),S_w=D_w unionC_w. Actual input compatibility not encoded by assigned root sets. | SRC-0041, SRC-0001 |
| CLM-0100 | COMPUTED_EXACT | CAM-S011-01 all90 layers/97839 explicit inputs;3416 winning insertions/4418 occupied deletions;4883 literal traces/43286 moves/15 selected negative closures.884 noncritical own-root failures each goal,3 critical common CLEAR root failures,10 C5 nonbipartiteR3 CLEAR losers; no ASH* failure. | SRC-0043 |
| CLM-0101 | COMPUTED_EXACT | CAM-S011-02 all116401 exact terminal transport certificates/507217 moves,65164 adjacent pair checks/6978 exceptional(1,1) outcomes,24894 triangle repairs/12 critical CLEAR cuts. Actual C5 odd-cycle3-support c=(4,1,1,1,1) has70-state closed CLEAR-negative reachability and all3 roots. Not critical ASH* failure. | SRC-0043 |
| CLM-0102 | COMPUTED_EXACT | CAM-S011-03 all97798 mass>=2 root identities/120 critical STACK insertion root families/23 critical CLEAR cases(15 stackable)/10 bipartite checks. Explicit abstract C5 typed/self-root family has empty common STACK intersection, NOT claimed graph/configuration realization. | SRC-0043 |
| CLM-0103 | COMPUTED_EXACT | S012 cold challenge S01153-58 and needed dependencies survives stated scopes;12 unchanged check-only replays and S003-S011 frozen manifests pass. Fresh local audit/replay is not human/kernel certification. | SRC-0044, SRC-0046 |
| CLM-0104 | PROGRAMME_PROVED | S01259 exact marked-input reciprocity x->kq iff x-e_w+(3-k)e_q->2w, x(w)>=1,k1/2; SAME-base TWO insertion D is symmetric, critical STACK D loopless/nonempty. No AS selection. | SRC-0044 |
| CLM-0105 | PROGRAMME_PROVED | S01259a for NONZERO c exact R2(c+2q)=union over z~q R2(c+z), realized by moving the TWO inserted q tokens first. c=0 has separate terminal{q}. Initial omitted zero bit corrected, failed run retained. | SRC-0044 |
| CLM-0106 | PROGRAMME_PROVED | S01260 exact unit/double donor languages: d1->1s iff c+s->2t;d1->2s iff c->2t;d2->1s iff c->1t;d2->2s iff c-s->1t. No adjacency needed for these ROOTED identities; no unrooted donor availability. | SRC-0044 |
| CLM-0107 | PROGRAMME_PROVED | S01261 stackable CLEAR-loser history using ambient triangular edge or landing outside ORIGINAL R3 immediately becomes nonstackable. At criticality gap<=shortest forbidden length; gap1 allowed first move lands at critical STACK loser. | SRC-0044, SRC-0001 |
| CLM-0108 | PROGRAMME_PROVED | S01261a exact partial path fuel bounds gap<=2^(d+1)-1 toward triangular site or2^d-1 outside originalR3 under stated source-fuel hypotheses;61b if gap>=2 and each triangle-edge-deleted component has<=1 nontriangular vertex, EVERY critical CLEAR loser is AS. Gap1/general target OPEN. | SRC-0044, SRC-0001 |
| CLM-0109 | PROGRAMME_PROVED | S01262 for base b and nonempty LIST l_i with repeated labels allowed, exact predicate b+sum_{j!=i}e_lj->2l_i is independent of distinguished index. Fixed-graph occurrence symmetry, NOT threshold/AS-preserving gluing. | SRC-0044 |
| CLM-0110 | COMPUTED_EXACT | CAM-S012-01 ten fixed boxes/175359 full configurations/16394311 exact relations;714 traces/5484 moves/69 full critical negative closures. Fixed triangular prism stack=clear8 and bridged_triangles12 through mass14, both independently full-mask checked; no atlas/universal claim. | SRC-0046 |
| CLM-0111 | COMPUTED_EXACT | CAM-S012-02 all435 one-step barriers/15 critical inputs/1177 closure states/78 partial-fuel witnesses/338 moves. BFS/full-DAG exact tau agree; C5/F2 tau3>gap2 and triangle_tail2 tau7>gap6, no equality inferred. | SRC-0046 |
| CLM-0112 | COMPUTED_EXACT | CAM-S012-03 all42 concentrating transfers,18 donor traces/116 moves,26 complete control negative closures/1177 states and18 whole-layer extrema.4 transfers lose/38 win; actual critical C5 unit donor CLEAR but double wins at OTHER roots, no double donor TWO in this sample. All bounded Q maxima AS, not universal. | SRC-0046 |
| CLM-0113 | PROGRAMME_PROVED | S01259b assigned abstract C6 matching D01,23,45 satisfies actual-style symmetry/typing/self-root rules but empty common STACK intersection. NOT a graph/configuration realization; no ASH* evidence. | SRC-0044 |
| CLM-0114 | COMPUTED_EXACT | S013 cold challenge59-62 and needed44/47/50/53-58 chain survives stated scopes;18 unchanged check-only replays and S003-S012 manifests PASS. Local audit is not human/kernel proof. | SRC-0047, SRC-0049 |
| CLM-0115 | PROGRAMME_PROVED | S01363 N(t) subset N(s),c(t)>=2,even concentration2a froms tot: winning concentrated input implies original wins for STACK/CLEAR, arbitrary buffer/root, protected full count path. Hence loss preserved. | SRC-0047 |
| CLM-0116 | PROGRAMME_PROVED | S01364 GLOBAL fixed-mass Q maximum has pairwise incomparable heavy open neighborhoods, at most one heavy per false-twin class; no receiver>=donor assumption. | SRC-0047 |
| CLM-0117 | PROGRAMME_PROVED | S01365 every normalized winning full concentration from a GLOBAL Q-maximal loser has common-exit count<=a-1 at root t or<=a otherwise, protected private-path exclusion and precise private multiplicity bounds. No distinct-neighbor bound. | SRC-0047 |
| CLM-0118 | PROGRAMME_PROVED | S01366 even open-neighborhood exchange permits arbitrary0/1 receiver: CLEAR always, STACK except exactly c=2s+t,a1; thus STACK safe at mass>=4. Zero disappearance/unique-incoming THREE re-root retain complete input. | SRC-0047 |
| CLM-0119 | PROGRAMME_PROVED | S01367 at any nonempty losing layer mass>=4 choose GLOBAL Q maximum then minimum degree-weight P: heavy sites have minimal open neighborhoods among ALL vertices and no comparable/equal pair. Graph/threshold unchanged. | SRC-0047 |
| CLM-0120 | PROGRAMME_PROVED | S01368 gap>=2 and componentwise neighborhood comparability of nontriangle vertices implies ASH*-CLEAR; also a largest loser with a heavy-set neighborhood minimum concentrates to an AS loser of same mass. No gap1/general comparison. | SRC-0047 |
| CLM-0121 | PROGRAMME_PROVED | S01369 adjacent1/2 transfer from any CLEAR loser has no THREE root anywhere; any resulting STACK win clears, with ONE/TWO root unspecified. Applies also to STACK losers. | SRC-0047 |
| CLM-0122 | PROGRAMME_PROVED | S01370 n>=4: L_all equals max losing mass with heavy sites only minimal open neighborhoods/one per false-twin class; L_AS equals restricted minimal-heavy-source AS maximum. Exact reduction of both maxima, residual inequality OPEN. | SRC-0047 |
| CLM-0123 | COMPUTED_EXACT | CAM-S013-02/03 freshly exact A7_0036 stack12/clear13; all six critical CLEAR losers(a,12-a,0,...),a odd1..11 have EVERY first move STACK-winning. Six full negative closures and20 literal successor traces; first-step gap1 shadow criterion false. | SRC-0047, SRC-0049 |
| CLM-0124 | COMPUTED_EXACT | CAM-S013-05 all189 exact historical STACK critical sets/1028 losers contain eight adjacent transfer pairs on A6_0076/A7_0019. Selected losses have complete81/101-state closures. A6 pair both GLOBAL Q52 and AS refutes threshold/global-Q deletion independence, not ASH*. | SRC-0047, SRC-0049 |
| CLM-0125 | COMPUTED_EXACT | CAM-S013-03/04 validate313052/370252 exact open exchange implications,3437/12239 modified-count chronologies,1872 adjacent CLOSED-extension failures and13 precise small STACK exceptions/no CLEAR exception. Finite scope only. | SRC-0047, SRC-0049 |
| CLM-0126 | COMPUTED_EXACT | CAM-S013-01 historical11970 n7/n8 records:10858 both-exact pairs,1112 unknown/ineligible pairs retained,114 genuine gap1 pairs. No new threshold/atlas/global inference. | SRC-0047, SRC-0049 |
| CLM-0127 | COMPUTED_EXACT | CAM-S013-05 independently validates12345 private-exit certificates/111047 literal moves and85604 adjacent small-transfer THREE exclusions on eleven complete boxes; no universal inference. | SRC-0047, SRC-0049 |
| CLM-0128 | COMPUTED_EXACT | CAM-S013-06 all134 losing layers>=4/614 Q-P extremizers/17 exact restricted-max comparisons agree; conditional68 applies to F2 in this finite box. Universal STACK/CLEAR remain OPEN. | SRC-0047, SRC-0049 |

| CLM-0129 | COMPUTED_EXACT | CAM-S014-01 two independent complete diagnostics agree on full GLOBAL Q/Q-P selected sets from44 positive-gap historical critical CLEAR layers plus four existing controls: every selected maximizer has no heavy triangular vertex and is AS. No new threshold or universal inference; gap1 candidate C14 UNPROVED. | SRC-0051 |

| CLM-0130 | COMPUTED_EXACT | S014 stated-scope cold challenge63-70 and required dependency chain survives;24 unchanged inherited check-only replays PASS and historical bytes preserved. Local mathematical review and finite algorithms are not human/kernel certification. | SRC-0051, SRC-0047 |

| CLM-0131 | PROGRAMME_PROVED | S01471: Protected capacitated multiple-donor reconstruction is equivalent to EVERY donor-subset Hall inequality on true heads, with a reserved simple root path. GLOBAL Q losers force deficiencies, not a universal contradiction. | SRC-0052 |

| CLM-0132 | PROGRAMME_PROVED | S01472: Every adjacent1/2 transfer from a stackable CLEAR loser CLEARs; its THREE roots remain absent. The proposed triangular loss-transfer shortcut is false. | SRC-0052 |

| CLM-0133 | PROGRAMME_PROVED | S01473: If retaining3 at an occupied triangular root leaves a whole input that STACKs, the original input CLEARs. | SRC-0052 |

| CLM-0134 | PROGRAMME_PROVED | S01474: Input on a complete-bipartite subgraph with all initial heavy sites ambient-triangular CLEARs at mass>=3alpha(occupied support)+4, by a complete all-input case proof. | SRC-0052 |

| CLM-0135 | PROGRAMME_PROVED | S01475: If every vertex is triangular and every nontrivial nontriangle-edge component is complete bipartite, CLEAR=STACK. A same-graph STACK AS witness transfers if available. | SRC-0052 |

| CLM-0136 | PROGRAMME_PROVED | S01476: Every input of mass>=10 on adjacent sites, at least one triangular, CLEARs, with all parities and zero-root cases covered. | SRC-0052 |

| CLM-0137 | PROGRAMME_PROVED | S01477: CLEAR=STACK when each nontrivial nontriangle-edge component satisfies75 or is K(a,b), b>=a+2, with an actual external common neighbor of B; A need not be triangular. | SRC-0052 |

| CLM-0138 | PROGRAMME_PROVED | S01478: K(k,3) plus one edge in the size-three part has both thresholds3k+1 and both ASH* for all k>=3, using the credited independent-set AS witness. | SRC-0052 |

| CLM-0139 | PROGRAMME_PROVED | S01479: For a,b>=1 the exact one-edge buffer join has STACK=max(3b+1,3a+5), CLEAR=max(3b+1,3a+7), both ASH*. Earlier F_a and known bounds/primitives retain credit. | SRC-0052 |

| CLM-0140 | PROGRAMME_PROVED | S01480: For a,b>=1,m>=2 the matching-buffer join has STACK=CLEAR=max(3b+1,3a+4m+1), with explicit all-target AS critical witnesses and both ASH*. | SRC-0052 |

| CLM-0141 | PROGRAMME_PROVED | S01481: An initially binary region U with I single arrivals/O pair exits satisfies theta(U)<=2I-O if emptied, and <=2I-O-1 for one terminal pile whose root starts empty or has incoming. Complete causal first-firing proof includes repeated/zero sites. | SRC-0052 |

| CLM-0142 | PROGRAMME_PROVED | S01482: For J(a,b,F), a,b>=1,F nonempty/no isolates, n=a+b+|F|,W=max_U(|U|+2theta(F[U])), STACK=S=max(n+1,3b+1,3a+W+1), CLEAR=max(S,3a+7). Both ASH* on this full arbitrary-buffer join class, not arbitrary graphs. | SRC-0052 |

| CLM-0143 | PROGRAMME_PROVED | S01483: For ANY finite simple graph of order>=2,N>=1, STACKability of N at r plus binary U implies N>=theta(G[U])+1. With UNIVERSAL r this is iff, giving rooted AS maximum max_U(|U|+theta(G[U])), not full graph threshold. | SRC-0052 |

| CLM-0144 | PROGRAMME_PROVED | S01484: Inside82, positive CLEAR-STACK gap occurs exactly for b<=a+1,F=K2 (gap2) or K3 (gap1); ALL critical CLEAR losers there have only nontriangular heavy sites. Universal gap1 C14 remains unproved. | SRC-0052 |

| CLM-0145 | COMPUTED_EXACT | CAM02: 2087 matching cases/2210 reservations/114 complete reconstructions;127 of127 triangular loss-transfer tests fail, with independently checked selected negative closures. Proper-subset Hall obstructions retained. No universal extrapolation. | SRC-0053 |

| CLM-0146 | COMPUTED_EXACT | CAM03-04: Complete unbounded binary source rays plus independent full general losing layers certify theta334 STACK25/CLEAR27 and barbell55 STACK48/CLEAR48. All critical losers on these four cases AS; mixed source boxes remain limited. No universal extrapolation. | SRC-0053 |

| CLM-0147 | COMPUTED_EXACT | CAM05-06: Whole-pile swaps fail1846 of10240 tests, including71 GLOBAL-Q CLEAR cases; triangular split fails3 of176 tests. Selected complete negative closures and winning traces independently checked; weaker critical variants unproved. No universal extrapolation. | SRC-0053 |

| CLM-0148 | COMPUTED_EXACT | CAM07-10: Seven complete-bipartite triangular construction challenges, four book examples, seven balanced exact AS ray examples/ten general thresholds and7620 literal one-edge AS histories all pass at their fixed scopes. No universal extrapolation. | SRC-0053 |

| CLM-0149 | COMPUTED_EXACT | CAM11: Fourteen matching-buffer full threshold comparisons,66144 literal STACK histories/552534 moves and explicit AS witnesses pass independently. No universal extrapolation. | SRC-0053 |

| CLM-0150 | COMPUTED_EXACT | CAM12: Two full W/path-cover algorithms agree on50 prescribed labeled F graphs, giving146 join graphs/292 goal comparisons:146 exact STACK endpoints match82;286 goal endpoints exact, six CLEAR initially incomplete at STACK cutoff. No universal extrapolation. | SRC-0053 |

| CLM-0151 | COMPUTED_EXACT | CAM13: All66642 boundary cells/11625 terminal histories/10033 true path covers agree independently; six earlier CLEAR cutoffs separately completed with old layers unchanged;228 explicit STACK AS witnesses checked across146 graphs. No universal extrapolation. | SRC-0053 |

| CLM-0152 | COMPUTED_EXACT | CAM14: All198320 arbitrary-buffer literal STACK histories/2046597 moves pass independently, including180224 n16 histories with order bound17 strictly dominating both other lower terms16. No universal extrapolation. | SRC-0053 |

| CLM-0153 | PROGRAMME_PROVED | S01485: Inside a fixed-parity losing layer of mass>=4, Q/P-selected heavies have incomparable open neighborhoods; any strictly nonminimal heavy must be ODD and every smaller-neighborhood site EMPTY. Global67 can change parity and cannot be silently reused in that simplex. | SRC-0054 |

| CLM-0154 | PROGRAMME_PROVED | S01486: An AS input pushed through any same-graph endomorphism has at most one coordinate>alpha(G), since all other fibers are independent binary sets. Thus the two alpha2 critical examples with two3-piles admit no endomorphic AS lift. | SRC-0054 |

| CLM-0155 | COMPUTED_EXACT | CAM15: ALL26 source rays/six general comparisons certify Q3plus03 thresholds15/15, Wagner8 11/11, Petersen10 15/15; every open neighborhood minimal, every critical Q/Q-P maximum AS. No universal extrapolation. | SRC-0054 |

| CLM-0156 | COMPUTED_EXACT | CAM16: All256 parity-preserving AS candidates for32 non-AS Wagner goal/input pairs checked,1716 literal winning moves; every input has a related parity-class AS loser. Bounded positive pattern only. No universal extrapolation. | SRC-0054 |

| CLM-0157 | COMPUTED_EXACT | CAM17: Fixed343 goal cases/1043 non-AS critical inputs: two ALL-receiver fixed-parity failures and eight heavy-receiver failures. Original schema KeyError/code/log preserved; separate hashed v2 metadata-only repair passes. No universal extrapolation. | SRC-0054 |

| CLM-0158 | COMPUTED_EXACT | CAM18: Two exact critical parity obstructions independently recomputed through threshold9, every old layer preserved;161 complete negative states/12 same-parity AS winners/72 moves checked. Critical non-AS loser isolated under every unit redistribution; alpha2 blocks endomorphic AS lift. No universal extrapolation. | SRC-0054 |

| CLM-0159 | COMPUTED_EXACT | CAM19: Fixed343-case odd-shift diagnostic:34 true-head transforms/14 eligible critical inputs,28 losing outputs. Each input has some losing output; six ORDERED-pair variants fail. Smaller-donor22-pair filter is post-data finite support, not a universal theorem. No universal extrapolation. | SRC-0054 |

| CLM-0160 | PROGRAMME_PROVED | S01487: For d=c-3h*s+(3h-1)*t+v on true edges st,sv, a winning m with h copies t->s reconstructs c by replacing those with(h-1)s->t and s->v if q=t or a t-to-q path survives. Loss forces multiplicity/essential-cut bounds; includes even donor6, no global AS conclusion. | SRC-0055 |

| CLM-0161 | PROGRAMME_PROVED | S01488: Bipartite globally largest STACK losers have signed mass0; an a-donor true-head shift changes it by a*epsilon_s mod3. If3 does not divide a, every such shift wins whenever its critical input exists. Same-root/same-pile count surgery is impossible in those residues; no existence or ASH* refutation claimed. | SRC-0055 |

| CLM-0162 | COMPUTED_EXACT | CAM20:252 labeled graphs/24192 inputs,4080 eligible smaller donor3 pairs all have a losing shift. Independent DAG checker validates321804 states/184453 full negative states/603635 legal dependencies. No universal extrapolation. | SRC-0056 |

| CLM-0163 | COMPUTED_EXACT | CAM21 v2:3710 labeled connected n6 graphs/267120 inputs,9484 eligible losing pairs,583 all-shift-winning failures. Independent DAG checker validates2129306 states/3092719 dependencies. Generic smaller-odd-donor loss preservation false; original pipe interruption and passing repair retained. | SRC-0056 |

| CLM-0164 | COMPUTED_EXACT | CAM22/23: six preselected graph controls have exact STACK thresholds25,36,36,40,15,13; independent full sets and1800 negative-closure states/56 transformed winning moves checked.259 of583 failures satisfy minimal-heavy residual restriction; all selected failures below critical/global-layer Q. | SRC-0056 |

| CLM-0165 | COMPUTED_EXACT | CAM24: independently compared1878298 full losing states on ALL215 labeled graphs underlying583 head-shift failures. NONE is critical or layer-global Q; every graph has L_all=L_AS. The universal critical/global-Q weakening remains unproved. | SRC-0056 |

| CLM-0166 | PROGRAMME_PROVED | S01489: minimize heavy count first, then maximize Q/minimize degree P on a losing layer M>=4; selected heavy neighborhoods are minimal and incomparable. Zero relocation uses the correct endomorphism direction d->c. Fewer-heavy same-mass candidates must win at a hypothetical counterexample; no universal AS selection proved. | SRC-0057 |

| CLM-0167 | COMPUTED_EXACT | CAM25:252 full general threshold comparisons,508929 losing states;4 ordered-pair failures at2 actual critical inputs refute smaller odd private-head input existence. All graph AS comparisons hold; no non-AS global Q critical maximum. | SRC-0057 |

| CLM-0168 | COMPUTED_EXACT | CAM26: fresh complete negative closures for2 critical inputs and2 AS critical witnesses,2556 states;52 literal transformed winning moves. Critical private-head failure is not ASH* failure. | SRC-0057 |

| CLM-0169 | HEURISTIC | H2r: every critical non-AS STACK loser has a losing elimination to one fewer heavy site retaining source residual0/1 and adding at most2 binary bits at initially empty sites. Complete conditional induction would imply ASH*, but universal hypothesis remains UNPROVED. | SRC-0057 |

| CLM-0170 | COMPUTED_EXACT | CAM27: entire-source H2 fails1124 of1230 critical non-AS inputs, already P3(3,3,0); source residual must not be silently forbidden. Failed H2 records retained. | SRC-0057 |

| CLM-0171 | COMPUTED_EXACT | CAM28:444 fixed STACK cases/1230 non-AS critical inputs/45804 full residual H2r candidates, zero failures. Bounded support only. | SRC-0057 |

| CLM-0172 | COMPUTED_EXACT | CAM29:72 new cycle/matching/chord graphs n8/9/10,1545176 complete losing states,227 non-AS critical inputs/11632 H2r candidates, zero failures. All AS comparisons hold; no universal extrapolation. | SRC-0057 |

| CLM-0173 | COMPUTED_EXACT | CAM30:252 coupled n12 gadget inputs at mass16,108 lose/144 win;617212 state records/1799764 legal dependencies checked, no cap hit. Two strongest cross-edge survivors selected by prior rule; not ASH* counterexamples by themselves. | SRC-0057 |

| CLM-0174 | COMPUTED_EXACT | CAM31: complete unbounded source/binary-buffer STACK rays on C00_51/C00_60; explicit automorphisms cover all12 sources using reps0/2/4. Exact L_AS18/24. Thus fixed mass16 holes do not refute ASH*. General thresholds tested separately in CAM32. | SRC-0057 |

| CLM-0175 | COMPUTED_EXACT | CAM32: exact general STACK thresholds19/25 on C00_51/C00_60, independently compared348930/587258 full losing states; exact AS maxima18/24 match. Every critical loser is AS, H2r scope there vacuous. No unrestricted ASH* inference. | SRC-0057 |

| CLM-0176 | PROGRAMME_PROVED | 90: for T>=n+1 all AS inputs at T,T+1,T+2 win iff all AS masses>=T win; exact occupied source three-removal, no general AS implication. | SRC-0058 |

| CLM-0177 | PROGRAMME_PROVED | 91: a critical loser surviving an edge addition preserves the exact STACK threshold; greedy saturation of an arbitrary loser only proves that narrower loss/maximality condition. | SRC-0058 |

| CLM-0178 | PROGRAMME_PROVED | 92: minimum-vertex/MAX-edge hypothetical counterexample has simultaneous minimum-heavy/Q/P structure, every nonedge cures its whole critical layer, strict proper quotient drops, and all dominated-neighborhood vertices positive in EVERY critical loser. Universal comparison still missing. | SRC-0058 |

| CLM-0179 | PROGRAMME_PROVED | 93: for every bipartite globally largest STACK loser c, every site s including empty ones and every k>=1, c+k*s consumes to k*s. Actual root-connected neutral counts at every root; no universal AS selection follows. | SRC-0058 |

| CLM-0180 | COMPUTED_EXACT | CAM33:120 fixed circulant graphs n11..14 have independently equal complete general losing layers and L_all=L_AS; no universal extrapolation. | SRC-0059 |

| CLM-0181 | COMPUTED_EXACT | CAM34:7510 prescribed lifted graph/inputs, no potential counterexample or unknown; every original loser has an independently certified AS loser at at least its mass. Winners have literal dependencies. | SRC-0059 |

| CLM-0182 | COMPUTED_EXACT | CAM35: singleton-to-two STACK monotonicity is FALSE,90 exact old-table failures in11 fixed boxes; no critical-layer extension inferred. | SRC-0059 |

| CLM-0183 | COMPUTED_EXACT | CAM36:120 greedy loser-preserving edge saturations,2189 independently checked missing-edge winning histories/28257 moves plus1912482-state complete original/AS screen DAGs; no potential or unknown, not automatically actual criticality. | SRC-0059 |

| CLM-0184 | COMPUTED_EXACT | CAM37-45: across ALL connected labeled graphs at each fixed input, losing c implies an AS loser of mass>=|c| for C6(3,3,1,1,0,0), C9a(3,3,1,1,0,0,1,1,1), C9b(3,3,3,1,1,1,0,0,0), E8(2,2,1,1,1,1,1,1), M9(2,3,1,1,1,1,1,0,0). Literal graph certificates and necessary-clause images plus independent complete RUP/LRAT refutations. Fixed finite input classes only; not universal ASH*. | SRC-0059 |

| CLM-0185 | COMPUTED_EXACT | CAM43 preserves UNKNOWN for C10 after1000 new iterations,91566 necessary clauses,1452478 AS-negative closure states checked; earlier C9a/C9b proof-scan caps stay UNKNOWN as attempts despite later successful separate proofs. No exclusion from any cap. | SRC-0059 |

| CLM-0186 | COMPUTED_EXACT | CAM44:638 full labeled critical sets,20231 critical inputs,17940 non-AS, zero non-AS coordinate2; four non-AS even-heavy inputs, all nonbipartite. Complete packed/coordinate and BFS/parity-union-find selections agree. Finite evidence only. | SRC-0059 |

| CLM-0187 | HEURISTIC | Universal no-two: a non-AS largest STACK loser has no pile2. UNPROVED; finite CAM44 agreement and fixed-input CEGIS exclusions are not a proof. Likewise odd-heavy restrictions on bipartite non-AS critical inputs remain unproved. | SRC-0059 |

| CLM-0188 | PROGRAMME_PROVED | 94: every fixed-input countergraph orbit has a lex-minimal representative under input-preserving permutations, with unique prefix extension; comparison clauses need not hold for every labeling. | SRC-0061 |

| CLM-0189 | PROGRAMME_PROVED | 95: complete sorted fixed-mass non-AS inventory, exactly-one guarded graph clauses and AS-tail cuts yield a finite necessary countermodel formula; independent full UNSAT would exclude only that(n,M). | SRC-0061 |

| CLM-0190 | PROGRAMME_PROVED | 96: even-pair loss-extension E0 is FALSE on noncritical P4(9,2,0,1), mass12: replacing its2 by3 at any vertex wins. No critical no-two/ASH* refutation. | SRC-0062 |

| CLM-0191 | PROGRAMME_PROVED | 97: actual P4(9,0,0,3), mass12, jointly has every-root neutral histories, minimum-heavy/global-Q/P selection and stated neighborhood/edge/quotient restrictions, yet all AS inputs of its mass win. Its mass is not globally largest. | SRC-0062 |

| CLM-0192 | PROGRAMME_PROVED | 98: EVERY proper coordinatewise positive extension of P4(9,0,0,3) wins, although L_all=L_AS14 is larger than12. Complete local addition maximality does not replace largest losing mass. | SRC-0062 |

| CLM-0193 | PROGRAMME_PROVED | 99: fair selector assumptions/closed flags affect only untrusted scheduling. A fresh unconditional exported-formula refutation independently replayed to empty is required for each complete finite(n,M) exclusion. | SRC-0061 |

| CLM-0194 | COMPUTED_EXACT | CAM46/47: F9(4,4,1,1,1,0,0,0,0) and E9(2,2,1,1,1,1,1,1,1) independently excluded as counterinputs across ALL connected graphs at their fixed orders. Exact necessary-clause/LRAT proof chains, not universal ASH*. | SRC-0059 |

| CLM-0195 | COMPUTED_EXACT | CAM48: complete fixed-mass inventories have45/65/257/88/212 patterns on(9,11)/(10,12)/(10,17)/(12,13)/(12,16). All graph records and encodings independently checked, but searches capped UNKNOWN; no full exclusion or actual counterexample. | SRC-0061 |

| CLM-0196 | COMPUTED_EXACT | CAM50: fresh full thresholds15/8/7/8 for P4 and its3 edge additions; full mass12 losing layer4 inputs, minimumheavy2, Q90/P12. Independent56-state negative closure and18 literal histories/202 moves cover14 insertions and4 exact neutral roots. Scoped actual obstruction only. | SRC-0062 |

| CLM-0197 | COMPUTED_EXACT | CAM49 repaired separate version: P4(9,2,0,1) full negative50-state closure and44 literal positive moves verify all4 even-pair extensions win. Original tuple/list predicate failure preserved, not mathematical evidence. | SRC-0062 |

| CLM-0198 | PROGRAMME_PROVED | 100: for connected bipartite G, distinct s/t at distance d, positive N at s plus singleton t STACKs iff N reaches residue cutoff2^d,3*2^(d-1),2^(d+1) respectively. Zero source separate. Path zero-imbalance lower already April7.3; no novelty claim. | SRC-0063, SRC-0002, SRC-0003 |

| CLM-0199 | PROGRAMME_PROVED | 101: every nontrivial isometric subtree of bipartite G is a true loopless retract, by explicit colored Helly-ball extension. EVERY loser supported there has mass<=L_AS(G), using EARLIER TreeStack. Includes all two-site inputs, not arbitrary supports. | SRC-0063, SRC-0002, SRC-0003 |

| CLM-0200 | PROGRAMME_PROVED | 102: Cr_k(k>=3) has maximum isometric-tree threshold max(3k-2,15). For k>=5 this is below known independent-set AS lower3k+1, so NO critical loser has isometric-tree-contained support. Refutes stronger support-selection only, not ASH*. | SRC-0063 |

| CLM-0201 | COMPUTED_EXACT | CAM51: all six complete all-pattern fixed(n,M) fair-selector searches ended iteration-bound UNKNOWN. Independent inventory/formula/graph-certificate checks PASS, but no unconditional real-case refutation, exclusion or actual counterexample. Control only independently refuted. | SRC-0063 |

| CLM-0202 | COMPUTED_EXACT | CAM52:27 fixed bipartite graphs,654 ordered pairs,5260 queries/44991 dependency states and1962 literal minimum constructions/9228 moves match100; finite negative queries only d<=3, universal theorem is symbolic. | SRC-0063 |

| CLM-0203 | COMPUTED_EXACT | CAM53:31 fixed graphs,2279 complete isometric subtree sets and65648 true ambient edge maps/earlier root scores agree. Crown5/6/7 maxima15/16/19. Fresh full crown5 threshold16/AS maximum15,28880 complete losing states; ASH* agreement. | SRC-0063 |

| CLM-0204 | COMPUTED_EXACT | CAM54:49 existing complete bipartite graphs,6415 complete isometric trees/full alpha maximum sets/root scores independently compared;48 combined-ceiling equalities and one strict gap42>40. Proposed universal combined ceiling is FALSE, not supported by a finite majority. | SRC-0063 |

| CLM-0205 | COMPUTED_EXACT | 103/CAM55: bipartite A182 edges07,16,26,27,35,37,45,46 has fresh exact STACK threshold42/AS maximum41 while combined n/alpha/isometric-tree bound40. AS loser(39,1,0,0,0,1,0,0) has complete independent10988-state closure/50423 legal dependencies. Actual auxiliary ceiling counterexample, not ASH*. | SRC-0063 |

| CLM-0206 | PROGRAMME_PROVED | 104: every loser supported on at most3 median-admitting vertices of a bipartite graph lies in an isometric tripod and satisfies |c|<=L_AS. All modular triple supports covered; on Q_d their mass<=2^(d+1)-2. Larger supports remain open; EARLIER TreeStack used. | SRC-0066 |

| CLM-0207 | PROGRAMME_PROVED | 105: exact labeled binary-buffer positive ancestry upper DAG is sound with separate actual zero singleton, positive pure siblings, proper partitions, same-root forests and strict cost descent. Affordable positive node plus occupied+3 gives a full input win; missing node supplies no loss. | SRC-0066 |

| CLM-0208 | PROGRAMME_PROVED | 106: checking EVERY proper partition/edge/pure/forest inequality and all signed residues supplies complete lower annotations for binary-buffer one/two/three-root forests. Together with105 attaining nodes this gives exact AS residue conductors, not arbitrary multiheavy classification. | SRC-0066 |

| CLM-0209 | COMPUTED_EXACT | CAM56 all32 non-AS sorted n8 mass10 patterns independently excluded across ALL connected graphs, exact inventory and4468 retained RUP additions/108581 hints. Finite(n8,M10) complete exclusion only; no full order8/universal ASH* claim. | SRC-0067 |

| CLM-0210 | COMPUTED_EXACT | CAM57 preserves STATE_CAP_UNKNOWN after16931 complete AS queries/2000000 states;12551572 dependencies checked, full tail NOT proved by that attempt. | SRC-0066 |

| CLM-0211 | COMPUTED_EXACT | CAM58 separately repaired v2 checks ALL1572864 positive ancestry nodes/98304 Q4 AS inputs31/32/33 and16 XOR maps. Exact L_AS30 follows with prior antipodal lower; original negative-shift checker failure preserved, no full general threshold. | SRC-0066 |

| CLM-0212 | COMPUTED_EXACT | CAM59 independently checks ALL803538796 lower inequalities/7141686 unordered proper partitions, exact minima/residues. Exact whole-Q4 AS oracle all source counts; only source0 critical AS is29 at0 plus one at15. Full general domain still open. | SRC-0066 |

| CLM-0213 | COMPUTED_EXACT | CAM60 general Q4 search reaches2M-state cap after2157 winners/one UNKNOWN query; completed DAG and14409950 legal dependencies checked, rest unexecuted. No actual counterexample or threshold. | SRC-0066 |

| CLM-0214 | COMPUTED_EXACT | CAM61 two pointwise shards cap at8M cumulative states each;1093/1300 literal winners plus one UNKNOWN each,69638 literal moves. Overlaps60, do not add prefixes across campaigns as distinct inputs. No full threshold or counterexample. | SRC-0066 |

| CLM-0215 | PROGRAMME_PROVED | 107: exact XOR translation canonicalization preserves whole-input consuming answers; negative orbit nodes check every legal canonical child, positive edges/macros lift by actual automorphism, mass descends. Candidate-list completeness and threshold do not follow. | SRC-0066 |

| CLM-0216 | COMPUTED_EXACT | CAM62 all9783 frozen Q4 general inputs31/32/33 independently WIN,872261 canonical states/7653737 dependencies, no unknown or potential. Exact AS oracle/literal anchors retained. Winning finite matrix does not prove general Q4 threshold or universal ASH*. | SRC-0066 |

| CLM-0217 | PROGRAMME_PROVED | 108: full inverse-orbit losing recurrence plus stable binary seeds and independent canonical-first-parent over ALL labeled translates certifies whole losing layers. Empty layer only above order can establish threshold; partial/capped sets cannot. | SRC-0066 |

| CLM-0218 | COMPUTED_EXACT | CAM63 controls: untrusted compiled producer and independent full canonical-first-parent layer replay certify Q1 threshold3 and Q3 threshold15. Compilation alone proves nothing; full Q4 run not yet executed at this checkpoint. | SRC-0066 |

| CLM-0219 | COMPUTED_EXACT | CAM63 full general Q4 orbit layers1..13 independently agree under native all-inverse and Python canonical-first-parent algorithms; mass14 candidate cap2M, threshold UNKNOWN. Q1/Q3 controls exact3/15. Source56 collision exactly recovered/versioned with33 unchanged replays; no mathematical promotion from repair. | SRC-0066 |

| CLM-0220 | COMPUTED_EXACT | CAM64 COMPLETE Q4 all general layers1..31, exact stack31 matching AS max30, only one mass30 orbit and all critical losers AS. Earlier63 cap unchanged. | SRC-0068 |

| CLM-0221 | COMPUTED_EXACT | CAM65 independently exact FanoInc14 AS max29/all source counts;344064 nodes,66961563 inequalities. Source0 critical AS25 plus four distance3 bits. Original failed producer-width run preserved with separate repair. | SRC-0068 |

| CLM-0222 | COMPUTED_EXACT | CAM66 COMPLETE FanoInc14 all general layers1..30, exact stack30 matching AS max29, one mass29 orbit/all critical losers AS. Independent336-map group and Q1/Q3 controls. | SRC-0068 |

| CLM-0223 | PROGRAMME_PROVED | 109 universal bipartite shell AS lower: nonempty k vertices at distance ell give losing source2^(ell-1)*(k+3)-3 plus those k singleton bits. All true edges, all final roots/chronologies, exact signed0 and output3 retained. No arbitrary-buffer upper/universal ASH* conclusion. | SRC-0068 |

| CLM-0224 | COMPUTED_EXACT | CAM67 ALL501 shell hypotheses on30 fixed bipartite graphs pass;106 exact-AS oracle checks;350 complete fresh negative closures/22920 states/53775 dependencies, no unknown. Finite challenge does not prove109 or universal ASH*. | SRC-0068 |

| CLM-0225 | COMPUTED_EXACT | CAM68 complete all44 sorted non-AS order8 mass11 classes independently excluded over ALL connected graphs;31824 labeled compositions audited,64781 RUP additions/1461399 hint visits. Finite scope only. | SRC-0069 |

| CLM-0226 | COMPUTED_EXACT | CAM69 H_up2 is FALSE: graph03,12,14,24,34 input(1,2,2,1,1), mass7 below true critical15; all12 prescribed mass-slack candidates win.2946-input/18-case complete prefix, remaining12 cases unexecuted. | SRC-0069 |

| CLM-0227 | COMPUTED_EXACT | CAM70 H_pool2 is FALSE despite arbitrary receiving site: graph04,13,23,24,34 input(3,3,1,1,1), mass9 below true critical14; all60 two-donor pooling candidates win.3097-input/21-case complete prefix, remaining9 cases unexecuted. Criticality/full buffer restriction remains essential. | SRC-0069 |

| CLM-0228 | PROGRAMME_PROVED | 110: Q5 AS input61 at0 plus bits15,23,27,29,30 loses by109, so L_AS>=66 and stack>=67. No critical loser supported on<=3 vertices/isometric subtree by104. Diameter-only cube equality and general product doubling upper are false (product comparison uses exact Q4 stack31). No exact Q5 threshold or ASH* failure. | SRC-0069 |

| CLM-0229 | COMPUTED_EXACT | CAM71 ALL8 specified high-pile patterns at masses16/18/20 on orders8/9 independently excluded across all connected graphs, full literal/CNF/LRAT chains and fresh control. Not complete coverage of those orders/masses; universal ASH* OPEN. | SRC-0069 |

| CLM-0230 | PROGRAMME_PROVED | 111: exact THREE boundary tree H->G with c_v=sum(3-deg H), |H|=|c|-2; true repeated labels, all original ports, mass3 base. Actual input-port edge gluing111b. Not a graph subtree/retract or extremal selection. | SRC-0071,SRC-0070 |

| CLM-0231 | COMPUTED_EXACT | CAM72 complete14814 non-AS critical inputs across48 bipartite cases,203673 parity-AS candidates: no all-source/heavy-source failure. B_par remains unproved globally. | SRC-0071 |

| CLM-0232 | COMPUTED_EXACT | CAM73 all27 bipartite cases among142 fixed graphs through order6;13297 odd-positive signed-zero multiheavy losers have a tested same-parity AS loser within mass+0/2/4. Finite only. | SRC-0071 |

| CLM-0233 | COMPUTED_EXACT | CAM74 independently completes18 selected larger bipartite cases through order14,1598711 eligible inputs with zero B_odd failures. A171/A181/A184 prior-scope UNKNOWN, not executed or extrapolated. | SRC-0071 |

| CLM-0234 | PROGRAMME_PROVED | 112: exact THREE trees canonicalize to floor(c_v/2) leaf copies, c_v mod2 unique degree2 markers, arbitrary degree3 branches; pair-fuel A>=2, branches A-2. Mass3 separate. | SRC-0071 |

| CLM-0235 | PROGRAMME_PROVED | 113: any connected simple n>=2 nonempty c STACKs iff THREE(c) or some THREE(c+2e_q), by whole-input reroot/cancellation. Signed-zero bipartite case uses only THREE(c); W_p not claimed a unit-upward ideal. | SRC-0071 |

| CLM-0236 | PROGRAMME_PROVED | 114: actual canonical w-leaf/v-marker pruning; if bipartite signed-zero loser c has positive even c_v adjacent to graph-leaf w, c-e_v+2e_w loses at mass+1 including c_w=0. Thus no critical such even heavy adjacent to a graph leaf. Core case unproved. | SRC-0071 |

| CLM-0237 | COMPUTED_EXACT | CAM75 all33188 eligible leaf inverse extensions across27 bipartite fixed graphs/102483 saved states lose;3104 initially empty leaf extensions. Finite challenge of114, not universal comparison. | SRC-0071 |

| CLM-0238 | COMPUTED_EXACT | CAM76 unconditional EVERY-even-vertex SOME-neighbor inverse ascent is FALSE below criticality:515 failed input/vertex pairs,74 at pile2,0 actual-critical failures; full83376 pair/145073 extension inventory independently checked.114 remains intact. | SRC-0071 |

| CLM-0239 | PROGRAMME_PROVED | 115: pair-fuel2 THREE exactly a true-edge path with prescribed leaf endpoint labels and all unique parity markers; unrestricted STACK additionally permits pair-fuel3 single-branch three-arm trees after padding2 at some label. Old independent-set witness dominates EVERY pair-fuel2 bipartite loser of order>=8. No all-graph extremal theorem. | SRC-0071 |

| CLM-0240 | PROGRAMME_PROVED | 116: every multioccupied STACK-winning input admits a winning first move at ANY prescribed heavy source; exact tree deletion handles arbitrary roots/padding. Pure3 one-site terminal is excluded. | SRC-0072 |

| CLM-0241 | PROGRAMME_PROVED | 117: firing a graph leaf with>=2 pebbles preserves STACK status except pure3 there. Every actual critical STACK loser on any connected graph n>=3 has zero pebbles at ALL neighbors of graph leaves. K2 exception explicit. | SRC-0072 |

| CLM-0242 | COMPUTED_EXACT | CAM78 complete160579 eligible all-graph inverse extensions across142 connected cases/order<=6,167713 saved states,22440 empty-leaf extensions; zero failure, exact two-singleton exceptions and all critical parent-zero checks. | SRC-0072 |

| CLM-0243 | PROGRAMME_PROVED | 118: independent elementary proof of116 by first-source commutation, positive edge reduction and final-arrival reversal; any adaptive heavy-source policy before reaching a pile admits winning destination choices. | SRC-0072 |

| CLM-0244 | COMPUTED_EXACT | CAM79 complete598867 legal predecessors of all167713 saved losers on142 fixed graphs,437350 multioccupied winning inputs,1211093 heavy sources,2538712 exact child-membership tests; every source has a winning destination.809 pure3 terminal predecessors excluded exactly. | SRC-0072 |

| CLM-0245 | PROGRAMME_PROVED | 119: odd graph-leaf/positive-parent THREE boundary contraction subtracts one input at each endpoint. For parent>=2 this is an exact STACK equivalence, with both legal converse moves and positive-root padding. Parent1 converse is not asserted. | SRC-0072 |

| CLM-0246 | PROGRAMME_PROVED | 120: on any connected simple graph, every losing input with positive EVEN graph-leaf count remains losing after +3 at that leaf. Hence all actual critical graph-leaf counts are zero or ODD. No claim that all core heavy counts are odd. | SRC-0072 |

| CLM-0247 | COMPUTED_EXACT | CAM80 complete164058 two-direction contraction/+3 checks across142 fixed cases:54686 in each direction and54686 even-heavy leaf+3 extensions; zero discrepancies or critical even leafs. Universal proof is119-120, not extrapolated computation. | SRC-0072 |

| CLM-0248 | PROGRAMME_PROVED | 121: the fixed-parity all-positive-odd THREE language W_p need not be a jump system or unit M-convex base set. Explicit P3 p111, fuel(5,0,0)/(2,3,0), two full consuming histories, all failed two-step exchanges excluded by signed mod3 invariant. All example inputs STACK; no ASH* counterexample. | SRC-0072,SRC-0073 |

| CLM-0249 | COMPUTED_EXACT | CAM77 ONLY specified F8 c=(1,1,1,1,1,1,3,3),mass12 on order8 independently excluded across ALL connected graphs with full necessary-CNF/LRAT chain. F9/F10 iteration bounds and F12 time bound UNKNOWN; no larger-pattern inference. | SRC-0072 |

| CLM-0250 | COMPUTED_EXACT | CAM81 finite complete charge-sector exchange challenge on bipartite fixed graphs through order5:2490 residue/fuel groups,57060 membership queries,560 nontrivial ordered pair/source checks, all matched independently. Rescaled-sector M-convexity remains UNPROVED universally; direct unscaled W_p exchange stays false by121. | SRC-0072 |

S014 final scope: owner-requested closeout; CLM-0129 through CLM-0250 retain their existing mathematical/finite statuses. Local proof assurance remains independent-review pending; universal STACK/CLEAR OPEN. No status is promoted by closeout.

## S015 final - critical ASH*-STACK counterexample G9 (2026-10-16)

| CLM-0251 | COMPUTED_EXACT | CAM82/83 complete STACK atlas: every connected graph of order 2..8 (995+11117 graphs, nauty-geng lists cross-checked with the S003 generator) has L_all=L_AS (critical ASH*-STACK holds); two separately written compiled loser-layer tools give byte-identical complete critical layers; orders<=7 also Python set-validated. Finite scope only. | SRC-0074,SRC-0075 |

| CLM-0252 | COMPUTED_EXACT | CAM85 order-9 STACK atlas with dual compiled tools: order 9: 261080 graphs; ASH_OK dual 261008; ASH_FAIL 1 (HCQTaXi); UNKNOWN/uncompared 71. Exact completeness scope and any UNKNOWN graphs listed in evidence/S015/cam85/summary.json. | SRC-0074,SRC-0075 |

| CLM-0253 | PROGRAMME_PROVED | S015-122/123 critical shift lemmas: for a largest STACK loser c on connected G (n>=3), every occupied v and w~v admit x in N(w)\{v} with c-e_v+e_x winning; every occupied v admits u~v with c-e_v+e_u winning; every heavy s and any x admit u~s with c+e_x-2e_s+e_u winning. Uses S014-116 only. Re-derives S014-117c. | SRC-0074,SRC-0072 |

| CLM-0254 | COMPUTED_EXACT | G9 = graph6 HCQTaXi (edges 0-3,0-5,0-6,1-4,1-7,1-8,2-6,2-8,3-5,3-6,4-7,4-8,5-7,6-8): stack(G9)=15, the only mass-14 losers are (0,0,1,0,0,5,0,8,0) and its automorphic image, every AS configuration of mass 14 stacks; hence L_all=14>L_AS=13 and critical ASH*-STACK FAILS. Verified by two compiled tools, a bare-definition brute force over all configurations of masses 1..16, closed-set and 6912 AS winning-sequence certificates, 490314 replayed mass-15 winning sequences, a Python layer validator and the source authors own public atlas code (is_critical_stacked_almost_stacked False). LEAN_PENDING, INDEPENDENT_COLD_RECHECK_PENDING. | SRC-0074,SRC-0075,SRC-0076 |

| CLM-0255 | PROGRAMME_PROVED | Human-readable proof that (0,0,1,0,0,5,0,8,0) is not stackable on G9: by S014-111/112/113 no subcubic boundary tree exists for c* or any c*+2e_q (branch-node counting around the unique parity marker at vertex 2 and label constraints of the fuel leaves). | SRC-0074,SRC-0071 |

| CLM-0256 | COMPUTED_EXACT | CAM90/91 families around G9 (dual compiled where both tools completed; see summaries): 12 CAM90 graphs of orders 9-13 with L_AS<L_all, including F(4,5,1) and bridge-path P(4,2), P(5,2) (L_all=30, L_AS=29); CAM91 producer gives PB(4,4,l,1) failures at l=0,2,4 (L_all=14,30,62; L_AS one less) and successes at l=1,3. Infinite-family behaviour is a CONJECTURE only. | SRC-0074,SRC-0075 |

| CLM-0257 | COMPUTED_EXACT | On every complete order<=8 critical layer (74121 non-AS critical inputs) S014 H2r holds (receiver can be a largest heavy pile) and every global-Q-maximal critical loser is AS; 11 even-heavy critical non-AS inputs, all of shape {4,5,1}. Both H2r and global-Q AS selection are FALSE universally because they would imply ASH* (CLM-0254). | SRC-0074 |

S015 final scope: CLM-0251..0257 added; earlier claims keep their statuses (claims whose conclusion is ASH* only for restricted classes remain valid on those classes). No FORMALLY_CERTIFIED status is assigned.

| CLM-0258 | COMPUTED_EXACT | S016 Gate 1 independent cold re-check of CLM-0254 (G9 STACK): new Rust backward-closure tool and Node forward/certificate tool reproduce K1-K4 exactly; all S015 G9 checkers replayed with identical outputs (two compiled tools rebuilt with MSVC); 286/286 S015 manifest hashes match; hand proof of K1 correct after editorial repairs R1-R3. COLD_RECHECK_PASS, LEAN_PENDING. | SRC-0077,SRC-0074 |

| CLM-0259 | PROGRAMME_PROVED | CLEAR losing-layer recursion C4-C6 (candidate completeness, termination above n) and STACK-to-CLEAR transfer T1-T3: every clearable configuration is stackable, so Lose_STACK(t) is contained in Lose_CLEAR(t) and stack(G)<=clear(G) on connected non-bipartite G; a pile k*e_r with 3 not dividing k clears; ASH*-CLEAR fails whenever Lose_CLEAR(L+1) is empty and no AS lies in Lose_CLEAR(L), L=L_all^STACK. | SRC-0077 |

| CLM-0260 | COMPUTED_EXACT | G9 = graph6 HCQTaXi: clear(G9)=15; the only mass-14 non-clearable configurations are (0,0,1,0,0,5,0,8,0) and its image (non-AS, non-clearable by CLM-0259 T1 and CLM-0254); every AS configuration of mass 14 and every configuration of mass 15 clears; L_all=14>L_AS=13, so critical ASH*-CLEAR FAILS. Bare-definition backward closure, 492618 replayed clearing sequences with a separate verifier, closures without mass-1 states, dual layer tools. INDEPENDENT_COLD_RECHECK_PENDING, LEAN_PENDING; authors code not run. | SRC-0077,SRC-0074 |

| CLM-0261 | COMPUTED_EXACT | CAM-S016-01/03 CLEAR atlas, dual tools: every connected non-bipartite graph of order 2..8 (924 + 10935) satisfies critical ASH*-CLEAR, matching frozen S003/S004 order<=7 thresholds; minimum order of a CLEAR counterexample is 9. | SRC-0077,SRC-0075 |

| CLM-0262 | COMPUTED_EXACT | CAM-S016-05 order-9 CLEAR: producer complete over 261080 graphs, G9 the unique failure among 260350 non-bipartite graphs; independent checker stopped at owner request after 207794 graphs, all agreeing; 53286 graphs producer-only (single implementation). | SRC-0077,SRC-0075 |

| CLM-0263 | COMPUTED_EXACT | CAM-S016-02: on G9 and the S015 CAM90/91 families, 17 graphs fail critical ASH*-CLEAR (dual), exactly the completed STACK failures; STACK and CLEAR verdicts coincide wherever both are known; 11 family graphs UNKNOWN at caps. CAM-S016-06: 69 of 71 S015 order-9 STACK UNKNOWN graphs ASH_OK by the producer (9 dual), 2 capped. | SRC-0077 |

S016 final scope: CLM-0258..0263 added; CLM-0254 (G9 STACK) is now cold-rechecked (CLM-0258). No FORMALLY_CERTIFIED status is assigned.

| CLM-0264 | COMPUTED_EXACT | S017 Milestone 1 independent cold re-check of CLM-0260 (G9 CLEAR): a new dense forward dynamic programme over all 2,042,975 configurations of masses 0..16 (Lean 4 program, rank-indexed arrays) reproduces K1c-K4c and K1-K4 exactly; every S016 CLEAR checker replayed with identical outputs (one CRLF-only difference), 91/91 S016 hashes; lemmas C1-C7 and T1-T3 re-checked line by line. Status COLD_RECHECK_PASS. | SRC-0079,SRC-0077 |

| CLM-0265 | FORMALLY_CERTIFIED | Lean 4 kernel proof (local build; Lean 4.35.0, Mathlib v4.35.0; standard axioms only; no sorry/native_decide): for G9 = graph6 HCQTaXi, the size-14 non-stackable configurations are exactly (0,0,1,0,0,5,0,8,0) and its image, neither almost stacked; every configuration of size >=15 is stackable; IsStackNumber G9 15; the AS threshold is 14; L_all=14, L_AS=13; not ASHStarStack G9; hence critical ASH*-STACK fails for some connected graph. A same-kernel leanchecker replay of all modules passed; Comparator, an independent-kernel check, hosted Lean CI and a fresh-session Lean cold re-check are pending. | SRC-0079 |

| CLM-0266 | FORMALLY_CERTIFIED | Lean 4 kernel proof (local build, same pins and limits as CLM-0265): G9 is connected and not 2-colourable; the size-14 non-clearable configurations are exactly (0,0,1,0,0,5,0,8,0) and its image; every configuration of size >=15 is clearable; IsClearNumber G9 15; the AS threshold is 14; L_all=14, L_AS=13; not ASHStarClear G9; hence critical ASH*-CLEAR fails for some connected non-bipartite graph. | SRC-0079 |

| CLM-0267 | FORMALLY_CERTIFIED | Lean 4 kernel proof (local build): clearable implies stackable (T1) on every finite graph; monotonicity above the order (October Lemma 4.7 / S003 Lemma 2) for stacking and clearing on finite graphs without isolated vertices; soundness of the exact losing-layer checker (layer_step: order, soundness, candidate completeness C5 and terminal 0/1 checks imply exactness of the next layer). | SRC-0079 |

S017 final scope: CLM-0264..0267 added. CLM-0260 (G9 CLEAR) is now cold-rechecked (CLM-0264). CLM-0265..0267 are the first FORMALLY_CERTIFIED claims; their scope is a LOCAL kernel build plus a same-kernel leanchecker replay (Comparator, independent-kernel check, hosted Lean CI and fresh-session cold re-check pending). No universal positive claim.

| CLM-0268 | FORMALLY_CERTIFIED | S018 Lean assurance of CLM-0265..0267: the pinned toolchain's lake comparator (unsandboxed, Windows host) finds the 25 Solution statements identical to formal/Challenge.lean (after fixing finding F1, a universe-parameter name in three Challenge lemmas) using only propext, Quot.sound, Classical.choice; Lean's kernel accepts the Solution export, and standalone replays are accepted by nanoda, con-ron (verified mode), lean4lean and leanchecker-paranoid; con-leche UNKNOWN (memory cap). Not established: a sandboxed comparator run with exit 0 including external kernels; hosted Lean CI. | SRC-0079, SRC-0080, SRC-0081 |

S018 final scope: CLM-0268 added (assurance of CLM-0265..0267). No claim promoted beyond its scope; universal L_all(G) <= L_AS(G) is not claimed.
