# S015: a nine-vertex counterexample to the critical Almost Stacked Hypothesis for STACKING

**Status.** COMPUTED_EXACT with multiple independently written checkers and explicit replayable certificates; the non-stackability of the critical input additionally has a human-readable proof below (via the S014 boundary-tree characterization 111-113, cold-challenged in S015). LEAN_PENDING and INDEPENDENT_COLD_RECHECK_PENDING: Phase 3 Lean work is not authorized in S015 and no human outside the programme has reviewed it. No contact with the source authors has been made (AGENTS.md rule 12). CLEAR is untouched: universal critical ASH*-CLEAR remains OPEN.

## 1. Statement checked

Definitions exactly as research/ASH_SPEC.md: a move removes two pebbles from a vertex u and adds one pebble to a neighbour v; a configuration is *stackable* if legal moves reach a configuration with exactly one occupied vertex; it is *almost stacked* (AS) if at most one vertex holds more than one pebble; stack(G) is the least t>=2 such that every configuration of size t is stackable. The intended critical form (author-confirmed, SRC-0010; S003 Theorem 4) is

    ASH*-STACK(G):  some AS configuration of size stack(G)-1 is not stackable,

equivalently L_AS(G) = L_all(G) where L_all, L_AS are the largest masses of a non-stackable configuration, respectively of a non-stackable AS configuration.

## 2. The graph G9

graph6 `HCQTaXi` (order 9, 14 edges, vertex connectivity 2 by nauty-countg). Labelled edge list (identical from the programme decoder and `nauty-listg -e`):

    0-3, 0-5, 0-6, 1-4, 1-7, 1-8, 2-6, 2-8, 3-5, 3-6, 4-7, 4-8, 5-7, 6-8.

Description: two diamonds (K4 minus an edge) D1={0,3,5,6} with non-adjacent tips 5,6 and D2={1,4,7,8} with tips 7,8; the tips are joined by the edges 5-7 and 6-8, and vertex 2 is adjacent to 6 and 8. The map 0<->1, 3<->4, 5<->7, 6<->8 (2 fixed) is an automorphism. Neighbourhoods: N(0)={3,5,6}, N(1)={4,7,8}, N(2)={6,8}, N(3)={0,5,6}, N(4)={1,7,8}, N(5)={0,3,7}, N(6)={0,2,3,8}, N(7)={1,4,5}, N(8)={1,2,4,6}.

## 3. Results

(K1) c* = (0,0,1,0,0,5,0,8,0) (one pebble on 2, five on 5, eight on 7; mass 14) is NOT stackable; nor is its automorphic image (0,0,1,0,0,8,0,5,0). These two are the ONLY non-stackable configurations of mass 14; neither is AS.

(K2) Every configuration of mass 15 is stackable. Since a configuration of mass m+1 > n=9 has a vertex with >=2 pebbles, it either is a single pile or has a legal move to a configuration of mass m; hence every configuration of every mass >=15 is stackable. With (K4) below, stack(G9)=15 and L_all(G9)=14.

(K3) Every AS configuration of mass 14 is stackable. With (K2), no AS configuration of size >=14 = stack(G9)-1 is non-stackable: L_AS(G9)=13 < 14 = L_all(G9). **The critical ASH*-STACK fails on G9.**

(K4) Every layer 2..14 contains a non-stackable configuration (per-mass loser counts from the brute force: 36, 128, 383, 930, 1862, 2887, 3280, 2510, 1301, 473, 124, 21, 2 for masses 2..14; 0 at 15 and 16). AS losers exist at mass 13, e.g. (0,0,1,0,1,11,0,0,0) and (1,0,1,0,0,0,0,11,0); 10 AS losers at mass 13 in total.

## 4. Verification record (CAM85, CAM89; preregistered amendments 4, 8 and addenda)

1. CAM85 producer (C++ hash-set loser-layer recursion, s015_layers_v3) and separately written checker (C sorted-array/binary-search recursion, s015_check_v2): identical critical layers {c*, image}, L_all=14, L_AS=13.
2. Bare-definition brute force (s015_cert_brute.py): every configuration of masses 1..16 (735,471 at mass 16) classified without any candidate lemma; same counts.
3. Explicit certificates (s015_cert_make.py) checked by a separately written verifier (s015_cert_check.py): closed forward reachable sets of both critical losers (1974 states each, every successor recomputed and inside, no single pile); legal winning sequences for all 2304 AS configurations at each of masses 14, 15, 16 (6912 replays, coverage enumerated independently).
4. Full mass-15 certificate (s015_cert_full15.py, checked by s015_cert_full15_check.py): a replay-verified winning move sequence for every one of the C(23,8)=490,314 configurations of mass 15.
5. Graph identity: nauty-listg decode equals the edge list; nauty-labelg canonical form equals that of the family member F(4,4,1).

## 5. Human-readable proof of (K1)

Tools (S014, re-checked in S015 section 0 of S015_UNIVERSAL_RESEARCH.md): **111** a configuration d of mass >=3 reaches exactly three pebbles on one vertex (THREE) iff there is a finite tree H of maximum degree <=3 with a graph homomorphism f:H->G such that d_v = sum over x with f(x)=v of (3-deg_H x); **112** for |d|>=4 the tree can be chosen with exactly floor(d_v/2) degree-1 vertices ("leaves") and (d_v mod 2) degree-2 vertices ("markers") labelled v, and any number of degree-3 vertices ("branch nodes"); a nontrivial canonical tree with A leaves has exactly A-2 branch nodes; **113** a nonempty d on a connected graph with n>=2 is stackable iff THREE(d) or THREE(d+2e_q) for some vertex q.

Adjacent tree vertices carry adjacent labels. A leaf labelled v is adjacent to exactly one tree vertex, whose label lies in N(v); a leaf is never adjacent to another leaf in a tree with >=3 vertices.

For c*: leaves 2 at vertex 5 and 4 at vertex 7; markers m5 (label 5) and m2 (label 2). Padding with 2e_q adds one leaf at q (parity unchanged). Write N(6)\{2}={0,3,8} and N(8)\{2}={1,4,6}.

**Unpadded, A=6, so 4 branch nodes.** The two tree-neighbours x,y of m2 have labels in {6,8}; no leaf or marker has label 6 or 8, so x,y are branch nodes. In a tree x,y are not adjacent and have no common neighbour other than m2, so their remaining 2+2 neighbours are four further distinct vertices, with labels in {0,3,8,1,4,6}; no leaf or marker carries such a label (the only label-2 vertex is m2), so all four are branch nodes: at least 6 > 4. Impossible.

**Padded, A=7, so 5 branch nodes.** Let ell be the extra leaf (label q).

Case q not in {6,8}. As above x,y are branch nodes and their four further neighbours have labels in {0,3,8,1,4,6}; the only non-branch vertex that can carry such a label is ell (possible only for q in {0,1,2,3,4}; label 2 is adjacent to 6 and 8). Hence at least three are branch nodes z1,z2,z3, and with x,y these are all 5 branch nodes; in particular q is not 5 or 7. No z has label 6 or 8: such a z could host no leaf or marker (none of 1,2,4 resp. 0,2,3 carries a remaining leaf, and 5 is not adjacent to 6 or 8), so it would need two further branch neighbours, but every other branch node is x, y or another z, and any such edge closes a cycle. So the z's have labels in {0,3} (neighbours of x at 6) or {1,4} (neighbours of y at 8). The four leaves at 7 need tree-neighbours with labels in N(7)={1,4,5}: z's with label 1 or 4, or m5. The marker m5 has two tree-neighbours with labels in {0,3,7}; label-7 vertices are leaves, and m5 cannot have two leaf neighbours (the tree would be the 3-vertex path), so m5 is adjacent to a z with label 0 or 3 and hosts at most one leaf at 7. The two leaves at 5 need neighbours with labels in N(5)={0,3,7}: z's with label 0 or 3. Every z has one edge to x or y, hence at most 2 further neighbours. Leaves at 7 then need at least 3 slots on z's labelled 1 or 4 (at least two such z's), and the two leaves at 5 plus m5 need 3 slots on z's labelled 0 or 3 (at least two such z's): at least 4 z's, but there are 3. Impossible.

Case q in {6,8}, both tree-neighbours of m2 branch nodes. Identical count: the four further neighbours of x,y include at most ell, the same three-z contradiction follows.

Case q in {6,8}, ell adjacent to m2. The other neighbour y of m2 is a branch node with label 6 or 8; its two further neighbours z1,z2 have labels in {0,3,8} or {1,4,6} and must be branch nodes. The remaining branch nodes are w1,w2. The non-leaf vertices m2,y,z1,z2,w1,w2,m5 form a subtree ("core") with 6 edges; m2 and y are saturated, so w1,w2,m5 attach through z1,z2. The six remaining leaves (4 at 7, 2 at 5) exactly fill the free degree of z1,z2,w1,w2,m5, so every vertex with free degree hosts leaves of an admissible label; no vertex hosts both a 5-leaf and a 7-leaf because N(5) and N(7) are disjoint.

Core-degree bookkeeping: core degrees of z1,z2,w1,w2,m5 sum to 2*6-1-3=8; the three core edges other than m2-y, y-z1, y-z2 carry "extra" degree 6. A label-6 vertex can host no leaf (N(6)={0,2,3,8}), nor a label-8 vertex (N(8)={1,2,4,6}); labels 0,3 host only 5-leaves; labels 1,4 and m5 host only 7-leaves; a w at 7 hosts only 5-leaves.

- y at 6 (z's in {0,3,8}). 7-leaves can sit only on w's labelled 1,4,5 (at most 2 each) and on m5 (at most 1, since m5 needs a core neighbour). Four 7-leaves force the 7-leaf slot counts (w1,w2,m5) to be (2,2,0), (2,1,1) or (1,2,1) with both w's labelled in {1,4,5} ((2,2,1) would leave a w-slot that can host nothing). (2,2,0): m5 has core degree 2 and its core neighbours must be labelled in {0,3,7}; the w's are not, so both are z's, closing the cycle m5-z1-y-z2-m5. (2,1,1): core degrees w1=1, w2=2, m5=1, so z1,z2 have core degree 2 and one free slot each, which must hold the two 5-leaves; thus both z's are labelled 0/3. m5 attaches to a z (its only admissible core neighbours); the remaining extra degrees w1=1, w2=2, other z=1 force the path w1-w2-z, so w2 is adjacent to a label-0/3 vertex, i.e. w2 at 5, and then w1 in N(5) intersected with {1,4,5} is empty. (1,2,1) is symmetric. Impossible.
- y at 8 (z's in {1,4,6}). The 5-leaves and the core neighbours of m5 must be w's labelled in {0,3,7}. (A1) One w, say w1, carries both 5-leaves (core degree 1). If w2 is not labelled in {0,3,7}, m5's only possible core neighbour is w1 and {w1,m5} is cut off from y. Otherwise w2 hosts nothing (0/3/7 host only 5-leaves) so has core degree 3, and all three extra edges are incident with w2: w2~w1, w2~m5, w2~z for one z. Adjacent labels in {0,3,7} are only {0,3}, so w2 is at 0 or 3 and the z adjacent to it is labelled 6; that z has core degree 2, hence a free slot that a label-6 vertex cannot fill. (A2) w1,w2 carry one 5-leaf each (core degree 2 each); then z1+z2+m5 core degrees total 4. Degrees (m5,z1,z2)=(2,1,1) disconnect {w1,w2,m5} from y; (1,2,1) forces the extra edges to form the path m5-w-w'-z1, so {w,w'}={0,3} and z1 is at 6 with a free slot it cannot fill; (1,1,2) is symmetric. Impossible.

Thus neither c* nor any c*+2e_q has a THREE tree; by 113, c* is not stackable. The image under the automorphism follows. QED (K1).

(K2)-(K4) are finite statements verified by the certificates and independent exhaustive programs listed in section 4; (K3) is 2304 explicit replayed winning sequences, (K2) 490,314.

## 6. Further counterexamples (CAM90, dual compiled only)

The same phenomenon occurs on 11 further graphs found in the preregistered family CAM90 (both compiled tools, byte-identical critical layers): eight one-vertex extensions of G9 (order 10; seven with L_all=14, L_AS=13 and one, X1_144, with 15/14), F(4,5,1) (order 10, 14/13), and the path-bridged P(4,2) (order 11) and P(5,2) (order 13), both with L_all=30, L_AS=29 and critical losers carrying piles 13 and 16 on the two adjacent internal bridge vertices plus one pebble on the vertex adjacent to both tips w1,w2. Bridge-length data (CAM91) are recorded in S015_UNIVERSAL_RESEARCH.md. These additional examples have NOT received the full brute-force/certificate treatment of G9; they are COMPUTED_EXACT (dual compiled) only.

## 7. Consequences and limits

- Universal critical ASH*-STACK is FALSE (subject to the Lean/cold re-check gates). The S014 sufficient routes H2r and global-Q AS selection are therefore false in general as well (each would imply ASH*): on G9 both critical losers are non-AS. H2r and global-Q survive only at the finite scopes recorded for orders <=8.
- The complete order-<=8 atlas shows G9's order 9 is the minimum possible order of a counterexample; the order-9 atlas (S015_UNIVERSAL_RESEARCH.md section 2a) records how many order-9 graphs fail.
- Printed-form S003 counterexamples, the S004 cold audit, the earlier TreeStack theorem (trees satisfy critical ASH* by S003 Thm 8) and all S014 local theorems are unaffected; theorems whose conclusion was ASH* for restricted classes remain valid on those classes.
- CLEAR: G9 is non-bipartite; its CLEAR behaviour has NOT been examined in S015 (CLEAR deferred). Universal critical ASH*-CLEAR remains OPEN.
- No novelty or priority claim is made; Phase 2 novelty audit is not started. No author/reviewer contact, no publication.
