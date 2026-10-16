# S015 research: complete low-order atlases, critical shift lemmas, and the G9 counterexample

**Headline (supersedes the working text below where they differ):** universal critical ASH*-STACK is **FALSE** at COMPUTED_EXACT level with multiple independent checkers: on the nine-vertex graph G9 = graph6 `HCQTaXi`, L_all=14 > L_AS=13 (research/S015_G9_COUNTEREXAMPLE.md). Lean and an independent cold re-check are pending. Every connected graph of order <=8 satisfies the STACK equality, so 9 is the minimum order. Universal CLEAR remains OPEN and was deferred. Earlier TreeStack (arXiv:2609.31811, registered package) is credited prior work; trees satisfy critical ASH* by S003 Thm 8 (TreeStack + October Thm 5.2), not by anything here. Printed-form S003 counterexamples (S004 cold audit PASS, Lean pending) are unchanged. No Lean, human, priority or novelty assurance is claimed for anything in this file.

## 0. Entry and cold challenge of the reused chain

Live main pinned at entry: 4200dc84be0bfd54e8573e7aa02dacea7ff8513c (tree 4f83e4b58baf55cc300aa6094d8c43b8ce556b2d), ordered parents 8ea5db20 (S013 merge) and cafa2f9a (S014 owner-authorized CI repair, child of S014 research commit 44a89726).

The S015 symbolic items reuse ONLY S014-116 and its chain 111 -> 112 -> 113 (with the credited occupied-root three-removal and the S013/S014 cold-challenged root-padding cancellation 47). Each was re-read line by line:

- 111 history->tree: merge vertices labelled by SOURCE have degree 3 (two consumed pebbles, one parent); original pebbles attach at their own label; the central vertex has three ports; deleting only original leaves leaves a tree H with |H|=(M-3)+1; boundary formula and the homomorphism property follow. Tree->history: after attaching 3-deg_H(x) leaves every vertex has degree 3; rooted at any vertex, each non-root has exactly two ports; postorder moves are legal because the two designated pebbles are present when the vertex fires. Single-vertex H = input 3e_v. PASS.
- 112 duplicate degree-2 labels: detaching x-z (the edge of x off the x..y path) and attaching y-z keeps a tree (the detached component contains neither x nor y), keeps label adjacency (f(x)=f(y)), keeps boundary 2+0=1+1. Count of degree-2 vertices drops by two. PASS.
- 113: reduction of a pile k>=4 to k-3 needs one neighbour (n>=2 connected): r->s, r->s, s->r. Pile 2 -> one move -> ONE. ONE at q pads to THREE at q. Converse uses rerooting at an H vertex labelled q (exists because the padded boundary at q is >=2) and credited cancellation 47. PASS at the stated scope (c nonempty, connected, n>=2).
- 116: the multioccupied hypothesis excludes zero-move THREE (|d|>=4 when T(d)); |d+2e_q|>=5 in the padded case; a w-leaf exists after 112 normalization because the boundary at w is >=2; deleting it gives the stated boundary including the single-vertex residual tree (degree 0 contributes 3 = 2+1). PASS.

Assurance: LOCAL_ADVERSARIAL_PASS (same programme, distinct session reading), INDEPENDENT_REVIEW_PENDING. Items 71-110 and 114-115, 117-121 are NOT reused in S015 and their pending status is unchanged.

## 1. S015-122 critical two-step shift (PROGRAMME_PROVED, local)

**Theorem 122.** Let G be finite, connected, simple, n>=3, M=L_all^STACK(G), and c a STACK loser with |c|=M. For every v with c_v>=1 and every w in N(v) there is x in N(w)\{v} with c-e_v+e_x STACK-winning. In particular every neighbour of an occupied vertex has degree >=2 (this re-derives S014-117c: critical losers vanish at neighbours of graph leaves, n>=3).

Proof. M>=n>=3, because the all-ones input (mass n, >=2 occupied, no legal move) loses. Put d=c-e_v+2e_w; |d|=M+1>L_all, so d wins, and d_w>=2. If d had one occupied vertex it is w and c=e_v+(M-1)e_w with M-1>=2; then c wins (w->v gives (M-3)e_w+2e_v, which is a single pile when M=3 and otherwise v->w gives (M-2)e_w), contradiction. So d is multioccupied and S014-116 gives u in N(w) with d-2e_w+e_u winning. If u=v this is c, a loser; hence u!=v, and d-2e_w+e_u=c-e_v+e_u. Take x=u. QED.

**Theorem 123 (one-step and prescribed-heavy shifts).** Same hypotheses. (a) For every v with c_v>=1 some u in N(v) has c-e_v+e_u winning. (b) For every heavy s (c_s>=2) and every vertex x, some u in N(s) has c+e_x-2e_s+e_u winning.

Proof. (a) d=c+e_v has mass M+1 and wins, d_v>=2, and d is multioccupied (otherwise c=Me_v would be a single pile). Apply 116 at v. (b) d=c+e_x wins, is multioccupied because c (a loser) has >=2 occupied sites, and d_s>=2. Apply 116 at s. QED.

These are necessary "fragility" conditions on the complete critical layer: every listed mass-M neighbour of c is outside it. They do not produce an AS loser and do not prove ASH*. Hostile finite challenge CAM84 (section 3) found zero violations (as it must if the proofs are right).

Hostile challenge (symbolic). Criticality is used ONLY through |d|=M+1>L_all; no below-critical input is covered (P4 mass 12 coordinatewise-maximal input shows local maximality is weaker). K2 is excluded (n>=3); the single-pile exceptional parents are handled explicitly; no adjacency v~x is claimed in 122 (x is at distance <=2 from v and may equal any vertex other than v, including heavy sites). x=w is impossible since x in N(w) and G is loopless.

## 2. Complete order <=9 STACK atlas (COMPUTED_EXACT, finite)

Method (CAM82/83/85, all preregistered with code hashes before execution). Exact loser-layer recursion: L_1 empty; for m>=2, c (|c|=m) loses iff >=2 occupied sites and EVERY legal successor lies in L_{m-1}. Candidate completeness: a loser without a move is 0/1; a loser with move u->v has losing successor s and c=s+2e_u-e_v (s_v>=1). Termination: L_m empty with m>=n forces all later layers empty. Within a graph NO symmetry reduction; one representative per isomorphism class (L_all, L_AS invariant).

Implementations: (A) C++ hash-set producer (v1/v2, 16-bit coordinates) and its packed-uint64 flat-hash version v3; (B) separately written C checker with sorted arrays, edge-list predecessor generation and binary search (12-bit __int128 version and uint64 radix-sort version); (C) pure-Python tuple/frozenset validator with independent forward closed-reachable-set re-proof of every critical non-AS loser and one AS witness per graph. Graph lists from nauty-geng 2.8.8, cross-checked for orders 5..8 against the repository's own S003 canonical generator (sets equal) and OEIS A001349 counts.

Results:
- Orders 2..7 (995 graphs): A and B critical layers byte-identical; C set-equal on all 995 with forward re-proofs; every graph has L_all=L_AS. Frozen S003 thresholds: 845 exact agreements + 8 S003-capped graphs consistent (order 7), 142 agreements (orders 2..6).
- Order 8 (11117 graphs): A(v1), A(v2) and B agree; A(v2)/B critical files byte-identical for all 11117; every graph has L_all=L_AS (critical ASH*-STACK holds on every connected graph of order 8). Frozen S003 partial order-8 atlas (cap 26): 10225 exact agreements, 892 capped-consistent, 0 mismatches. Largest L_all=254 (P8). C (Python) compared only on a 31-graph prefix (stopped by the preregistered time policy); the order-8 result is COMPILED-DUAL.
- Order 9 (261080 graphs): see section 2a.

### 2a. Order 9 (CAM85, amendments 4 and 11)

261,080 connected graphs (nauty-geng -c 9 = OEIS A001349). 261,008 dual-verified ASH_OK (byte-equal critical lines from both compiled tools), exactly ONE dual-verified failure, G9 = `HCQTaXi` (L_all=14, L_AS=13; see S015_G9_COUNTEREXAMPLE.md), and 71 UNKNOWN: 22 trees (critical ASH* holds for trees by the earlier credited TreeStack theorem + S003 Thm 8) and 49 non-tree graphs left unfinished when the owner requested closeout (names in evidence/S015/cam85/summary.json). The largest dual-verified L_all is 128. G9 is non-bipartite; no bipartite failure is known. The amendment-7 Python third check of order 9 was not executed. H2r/critical statistics were run only on order-9 chunks 06 and 07 (0 H2r failures there).

Interpretation: ASH*-STACK has no counterexample on <=8 vertices; on 9 vertices G9 is the only failure among the 261,008+1 dual-verified graphs (71 UNKNOWN). Finite statements only; nothing is extrapolated.

## 3. H2r, global-Q and critical structure on complete critical layers (finite evidence)

S014 hypothesis H2r (UNPROVED): every largest loser with >=2 heavy sites has distinct heavy s,t, r in {0,1}, k in {0,1,2}, a k-set U of empty sites with d=c-(c_s-r)e_s+(c_s-r-k)e_t+1_U losing. Its universal truth would imply ASH*-STACK (S014 conditional induction). Every candidate has mass exactly M, so on a complete critical layer the test is pure membership.

| order | graphs | graphs with non-AS critical loser | non-AS critical inputs | H2r fail | k=0 needed fail | Q-max non-AS graphs |
|---|---|---|---|---|---|---|
| 3-7 | 994 | 404 | 4835 | 0 | 20 | 0 |
| 8 | 11117 | 4858 | 69286 | 0 | 33 | 0 |

Additional observations (finite only): (i) the receiver t can always be taken to be a LARGEST heavy pile; (ii) "all pairs of s into t" (k=0, r=c_s mod 2) fails only in the listed k=0 cases, e.g. C5 (3,1,3) consecutive needs k=1; (iii) every global-Q-maximal critical loser is AS in every graph checked, i.e. the S014 global-Q selection statement survives; (iv) the two largest heavy sites are at distance 2 in 97.7% of order-8 non-AS critical inputs; (v) even heavy coordinates are rare: 1 order-7 and 10 order-8 non-AS critical inputs, all of the shape {4,5,1} (e.g. FCZTo (0,4,1,0,0,5,0)); critical core oddness is therefore FALSE as a universal statement, while S014-120 leaf oddness stands.

Interpretation: H2r and the global-Q selection survive every complete critical layer of order <=8, but both are FALSE universally: each implies ASH*-STACK (S014 conditional induction; global-Q maximum is a critical loser), and G9 has no AS critical loser at all. At order 9 the only failures of either statement are on the ASH*-failing graphs.

## 4. Consequences for the obligations

The universal SAME-GRAPH inequality L_all<=L_AS is false (G9), so the S014/S013 proof routes aimed at it (arbitrary-buffer domination, H2r, global-Q selection, B_odd as a route to bipartite ASH*, rescaled exchange as a route to AS selection) cannot succeed universally; their scoped theorems remain valid. Statements restricted to classes where ASH* is proved (trees, complete multipartite, join classes, triangle tails, isometric-tree-supported bipartite losers) are unaffected. G9 is non-bipartite and has an even critical heavy pile (8) adjacent to an odd one (5). Whether bipartite graphs satisfy critical ASH*-STACK remains OPEN (the only order-9 failure, G9, is non-bipartite). Critical ASH*-CLEAR remains OPEN.
