# S016 Gate 1 - independent cold re-check of the G9 STACK counterexample

Verdict: **COLD_RECHECK_PASS** (computational re-verification by two new tools in new languages and algorithms, all S015 checkers replayed with identical outputs, S015 manifest intact, hand proof correct after three editorial repairs recorded below). Status of the STACK refutation becomes COMPUTED_EXACT + COLD_RECHECK_PASS + human proof audited; **LEAN_PENDING** (AGENTS.md rule 7; Phase 3 needs explicit owner authorization). No S015 byte is rewritten.

## G1.1 Definitions and threshold convention

Re-derived from research/ASH_SPEC.md (October Def. 2.1/3.1 as transcribed in S003), research/S003_AS_GAP_AND_ATTACKS.md section 2 and SRC-0010:

- move u->v along an edge: c_u>=2, c_u-=2, c_v+=1 (mass drops by exactly 1); stackable: some legal sequence reaches a configuration with exactly one occupied vertex (any positive size); AS: at most one vertex holds more than one pebble;
- stack(G): G connected, n>=2, least t>=2 with every configuration of size exactly t stackable. S003 Lemma 1 (0/1 configurations of size 2..n are terminal AS losers) and Lemma 2 (= October Lemma 4.7, monotone above n, proof inspected in S003) give Proposition 3: losers exist at every size 2..stack-1 and none at or above stack, so the exact-layer and "every size >=t" readings coincide;
- intended critical ASH* (SRC-0010; S003 Theorem 4(ii)): ASLose(stack(G)-1) nonempty, equivalently L_AS = L_all.

On G9 the data give losers at every mass 2..14 (K4), none at 15 (K2) and hence none above (Lemma 2, 15>9), so stack(G9)=15 under every reading. AS losers exist at masses 2..13 (positive counts below) and none at 14 (K3), so ASLose(14) is empty: ASH*-STACK fails under (a) L_AS=L_all, (b) "least t0 such that every AS configuration of every size >=t0 is stackable" (t0=14, not 15), and incidentally under the already-refuted printed pointwise form (least t with every AS of size t stackable is 14). G9 is connected (the edge list contains the spanning path 2-6-0-3-5-7-1-4-8), n=9>=2, simple. Zero/one-vertex conventions are irrelevant here (n=9).

## G1.3 New independent checkers (preregistered, PLAN.md and PLAN_ADDENDA 1a)

1. tools/s016_g9_reverse.rs (Rust 1.97.1, rustc -O, msvc). Backward closure of all single piles under reverse moves, mass by mass, with each layer then enumerated by an independent odometer and its size asserted equal to C(m+8,8). Never evaluates a forward losing condition. Own graph6 decoder (asserts HCQTaXi = the stated edge list) and automorphism check. Output evidence/S016/gate1/reverse_rust.txt: per-mass losers 0,36,128,383,930,1862,2887,3280,2510,1301,473,124,21,2,0,0 (masses 1..16), AS losers 0,36,128,375,789,1185,1331,1116,734,391,177,60,10,0,0,0; mass-14 losers exactly (0,0,1,0,0,5,0,8,0) and (0,0,1,0,0,8,0,5,0), both non-AS; 21 mass-13 losers listed (10 AS). K1-K4 PASS, L_all=14, L_AS=13, `G9_REVERSE_OK`.
2. tools/s016_g9_forward.mjs (Node 24.18.0). Forward closure from both critical losers (1974 states each, closed, no single pile) and memoised forward win search with a separate legality replayer for all 2304 AS configurations of mass 14 and all 490,314 configurations of mass 15: 0 failures, `G9_FORWARD_OK` (evidence/S016/gate1/forward_node.txt).

## G1.4 Replay of every S015 checker

| check | result | comparison |
|---|---|---|
| tools/s015_cert_check.py G9_certificate.json | CERTIFICATE_OK (2 closed negatives of 1974 states, 11916 replayed sequences, 6912 AS coverage, 0 missing) | stdout identical to evidence/S015/counterexample/cert_check_log.txt |
| tools/s015_cert_full15_check.py | 490314 lines, 0 bad, FULL15_OK | identical to full15_check_log.txt |
| tools/s015_cert_brute.py 16 | per-mass table identical | log identical to brute_log.txt; JSON identical to brute_truth_table.json after CRLF->LF normalisation (Windows text-mode newline only) |
| tools/s015_validate.py on G9 | Lall 14 LAS 13 crit 2 critAS 0 FWD_OK ASH_FAIL | identical to python_layer_validator.txt |
| tools/s015_layers_v3.cpp, s015_check_v2.c (rebuilt, MSVC 14.44 cl /O2) | Lall 14, LAS 13, crit 2, maxlayer 3280, total 13937; checker fingerprint 6575d04037117c43; critical files byte-identical to each other | identical to the frozen S015 cam85 chunk_04 records except the wall-time field |
| tools/s015_author_check.py | NOT_RERUN | the authors' public code is not mirrored; fetching it was not needed for this gate and was not done (S015 result retained as recorded, external confirmation only) |
| evidence/S015/HASHES.md | 286/286 entries match, 0 missing | S015_MANIFEST_OK |

Build note: GCC `__builtin_popcount(l)` is unavailable in MSVC; a forced-include shim (evidence/S016/gate1/popcount_shim.h, mapping to `__popcnt`/`__popcnt64`, preserving LP64 semantics) was used without editing S015 sources. Windows `long` is 32-bit; all counts on G9 are far below 2^31.

## G1.2 Line-by-line audit of the human proof (S015_G9_COUNTEREXAMPLE.md section 5)

Dependencies re-derived. For the proof of K1 only these directions are used:
- 113, forward direction: a stacked pile k*e_r with k>=4 reaches (k-3)e_r (two moves r->s, one move s->r), so any stackable c reaches THREE, or pile 2 and then ONE; a ONE history at q, run with two extra untouched pebbles at q, gives THREE for c+2e_q. Hence STACK(c) implies T(c) or T(c+2e_q) for some q. The converse direction (which uses re-rooting and the credited cancellation 47) is NOT needed for K1.
- 111, history-to-tree direction: re-derived (ancestry of the three final pebbles; merge nodes labelled by source; deleting original-pebble leaves gives H with c_v = sum (3-deg_H x)).
- 112 normalisation: re-derived (two equal-label degree-2 vertices x,y: move x's off-path edge to y; tree, labels and boundary preserved). Leaf count a_v, marker count p_v, and B=A-2 branch nodes from the degree sum A+2P+3B=2(A+P+B-1).

For c*: A=6, P=2 (m2, m5), B=4; padded c*+2e_q: A=7, B=5. The argument is correct with three editorial repairs; none changes a conclusion.

(R1) Label-2 branch nodes. The text lists the possible labels of the further neighbours of x,y as N(6)\{2} and N(8)\{2} "since the only label-2 vertex is m2". Branch nodes may carry label 2. Correct statement: the only NON-branch vertex labelled 2 is m2 (c_2=1), which is already adjacent to x and y; so a further neighbour labelled 2 is a branch node and every conclusion "all are branch nodes" stands. Likewise in the padded case a z labelled 2 hosts no leaf or marker (N(2)={6,8}, no leaf or marker labelled 6/8 is available), so it needs two further branch neighbours and closes a cycle exactly as for labels 6/8; thus z labels lie in {0,1,3,4}. In the ell-adjacent-to-m2 case the z labels are N(6)={0,2,3,8} or N(8)={1,2,4,6}; a label-2 z hosts nothing and is admissible as a neighbour of neither m5 nor a 5-leaf, so every step of both sub-cases is unchanged.

(R2) Equal labels of x and y. The text writes "x at 6, y at 8". Both may carry the same label. The padded q not in {6,8} count is label-agnostic: it needs at least two z's labelled 1/4 and at least two labelled 0/3 among three z's. (If both are at 6 there is no z labelled 1/4; if both at 8 none labelled 0/3; either way the count fails even faster.) The unpadded count never used the labels.

(R3) Missing core-degree split in sub-case "y at 6", slot pattern (2,1,1). Core degrees w1=1, w2=2, m5=1 force core(z1)+core(z2)=4, which also allows (3,1) and (1,3), not only (2,2). (3,1): z2 (core 1) hosts both 5-leaves and so is labelled 0/3; z1 hosts nothing. The extra (non-y) core edges have degrees z1:2, w1:1, w2:2, m5:1, i.e. a path with ends w1, m5. m5's neighbour must be labelled in {0,3,7}; w2 is labelled in {1,4,5}, so m5~z1 (z1 at 0/3), the path is m5-z1-w2-w1, w2~z1 forces w2 at 5, and then w1 in N(5) intersect {1,4,5} is empty. (1,3) is symmetric. Impossible, as claimed.

All other steps were checked against the neighbourhood table N(0)={3,5,6}, N(1)={4,7,8}, N(2)={6,8}, N(3)={0,5,6}, N(4)={1,7,8}, N(5)={0,3,7}, N(6)={0,2,3,8}, N(7)={1,4,5}, N(8)={1,2,4,6}: leaf-hosting rules, the impossibility of leaf-leaf adjacency in trees of size >=3, the m5 single-leaf bound, the cycle arguments, (2,2,0), the y-at-8 cases (A1) and (A2) with their degree splits (2,1,1)/(1,2,1)/(1,1,2), and the q in {5,7} exclusion (ell must be one of the four further neighbours, so q is in {0,1,2,3,4}). The case list (q not in {6,8}; q in {6,8} with both m2-neighbours branch; q in {6,8} with ell adjacent to m2) is exhaustive because the only possible non-branch neighbour of m2 is ell.

Conclusion: K1 has a correct human proof (S015 section 5 plus R1-R3), independent of all computation, using only 111 (history-to-tree), 112 and the elementary direction of 113. K2-K4 are finite statements, now verified by five separately written programs in four languages and two algorithms (forward losing recursion; backward closure from single piles) plus explicit replayed certificates.

## Outcome

Gate 1 PASS. Per the handoff outcome rule S016 proceeds to Gate 2 (critical ASH*-CLEAR). Phase 3 Lean formalisation of G9 K1-K4 is proposed to the owner in the closeout; nothing Lean-related is started.
