# S015 amendment 8 - CAM-S015-89: certification of candidate ASH*-STACK counterexample G9 = HCQTaXi

2026-10-16, BEFORE any certification computation. CAM85 (order-9 atlas) reported ONE graph with L_all != L_AS so far: graph6 `HCQTaXi`, both compiled tools agreeing (L_all=14, L_AS=13, critical layer exactly {(0,0,1,0,0,5,0,8,0),(0,0,1,0,0,8,0,5,0)}, zero AS critical losers). Until certified this is a CANDIDATE only.

Labelled graph (decoded from graph6, vertices 0..8), 14 edges:
0-3, 1-4, 0-5, 3-5, 0-6, 2-6, 3-6, 1-7, 4-7, 5-7, 1-8, 2-8, 4-8, 6-8.

Claims to certify:
(K1) c*=(0,0,1,0,0,5,0,8,0) (mass 14) is NOT stackable; likewise its image (0,0,1,0,0,8,0,5,0).
(K2) EVERY configuration of mass 15 is stackable; hence (termination lemma = October Lemma 4.7 monotonicity above n) every configuration of every mass >=15 is stackable and stack(G9)=15 = L_all+1.
(K3) EVERY almost-stacked configuration of mass 14 is stackable; with (K2), no AS configuration of size >=14 = stack(G9)-1 is non-stackable, i.e. the critical form ASH*-STACK FAILS on G9 (ASH* <=> some AS configuration of size g(G)-1 is not stackable, S003 Thm 4 / ASH_SPEC).
(K4) Supporting: every layer 2..14 is nonempty (no exact-layer gap), and L_AS=13 exactly.

Independent methods (in addition to the two compiled CAM85 tools):
(M1) tools/s015_cert_brute.py: complete truth table of STACK for EVERY configuration of masses 1..16 on G9 by the bare definition (single pile, or some legal move to a winner), masses processed in increasing order over explicit composition enumeration (itertools); no candidate lemma, no loser-layer recursion. Outputs per-mass loser counts, AS loser counts, all losers at masses >=10, and digests.
(M2) tools/s015_cert_make.py: explicit certificates: (a) complete forward closed reachable sets from both critical losers, with every successor listed and no single-pile state; (b) for EVERY AS configuration of masses 14,15,16 an explicit legal move sequence ending in a single pile; (c) for a deterministic 5000-configuration sample of mass 15 (every 98th in lexicographic composition order) explicit winning sequences.
(M3) tools/s015_cert_check.py: separately written verifier that re-derives G9 from the edge list, replays every certificate move (legality: >=2 at source, true edge), checks closure of the negative sets (recomputing all successors itself) and that every AS configuration of masses 14..16 is covered.
Also: nauty independent decode of the graph6 string (nauty-listg -e) cross-checked against the edge list; connectivity and simplicity checked.

Resources: one process at a time, <=3600 s, ulimit -v 8 GiB. Outputs: evidence/S015/counterexample/. Outcome policy: if ALL of K1-K4 hold under M1 and M3 and both compiled tools, G9 is recorded as COMPUTED_EXACT counterexample to critical ASH*-STACK with multiple independent checkers; status remains LEAN_PENDING / COLD_RECHECK_PENDING (Phase 3 Lean is NOT authorized in S015). Any disagreement => record, no claim, investigate.
