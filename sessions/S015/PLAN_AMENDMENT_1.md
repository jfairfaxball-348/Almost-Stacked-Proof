# S015 amendment 1 - CAM-S015-83: critical layers, H2r challenge, order-9 atlas

2026-10-16, BEFORE any CAM83 execution. CAM82 (PLAN.md) continues unchanged; its v1 order<=7 producer/validator comparison found ZERO numeric disagreements (L_all, L_AS, critical count, AS critical count, non-AS existence, forward re-proofs) on 995 graphs, and 845+8(capped-consistent) agreement with frozen S003 T2b order-7 thresholds. The v1 "min non-AS representative" column is NOT comparable (producer string order versus validator tuple order); this is a reporting artefact, recorded, not a mathematical disagreement. Order-8 v1 run in progress.

New tools (sha256 before execution):
- tools/s015_layers_v2.cpp 271ef91a4f5792740069b475d1223d2295b7af4fd9c86a88197e2b32f977b526 (v1 recursion + full critical-layer output + per-graph wall/total caps)
- tools/s015_check.c (second compiled checker; sorted __int128 arrays, edge-list predecessor generation, binary search; separately written) sha256 listed in AMENDMENT_1.sha256 companion line below
- tools/s015_validate_v2.py 6e91fe856298a2e075519feaec53fde4e18a96791e5c7f177d2200ea58ddb576 (Python v1 recursion; compares FULL critical-layer SETS with producer)
- tools/s015_h2r.py 92a9d7741d5fab7647ac079ee61a4089ff612463693c6f057957bc3aaa1cfe92 (S014 H2r and k=0 variant, by membership in the complete critical layer; valid because every H2r candidate has mass exactly M)
- tools/s015_compare.py (frozen S003 comparison)

Stage A (orders 2..8): producer v2 with critical files; compiled checker with critical files; byte comparison of the two critical files; Python v2 set comparison for orders 2..8 (order 8 only if wall time per batch <=3600 s; otherwise the uncompared remainder is recorded as compiled-dual-only). Frozen S003 A3 order-8 partial atlas (cap_t 26) compared by canonical form.

Stage B (H2r on complete layers): run s015_h2r.py on every complete critical layer of orders 2..8 (and order 9 from Stage C). A failure refutes H2r only (not ASH*) and is recorded with full graph and input; H2r survival is finite evidence only.

Stage C (order 9): all 261080 connected graphs from `nauty-geng -c 9`, decoded by s015_graphs.py; cross-check count against OEIS A001349 (261080). Producer v2 caps per graph: 120 s wall, 20,000,000 losers per layer, 2,000,000,000 cumulative states; children ulimit -v 4 GiB, at most 3 concurrent. Compiled checker on every graph: caps 150,000,000 candidate slots and 240 s; critical files compared byte-for-byte with the producer's. Any capped/OVER graph is UNKNOWN; trees among them are additionally covered by EARLIER credited TreeStack (no new claim). Python validator: a deterministic sample (every 50th graph in geng order) plus every graph whose critical layer contains a non-AS loser with minimum heavy count >=2 (i.e. every ASH_FAIL candidate). Symmetry: one isomorphism-class representative per graph; no within-graph reduction.

Outcome policy: a graph is ASH_OK_DUAL when producer and checker agree on the full critical layer and it contains an AS loser. ASH_FAIL requires agreement plus Python forward re-proof, then becomes a candidate counterexample for separate certification (all-AS inputs at mass >= L_all must lose-check exhaustively, adjacency/configuration published, Lean later gated). UNKNOWN for any cap. No extrapolation beyond the literal order-9 list.

Stage D: if a pilot of the first 5000 order-9 graphs projects total wall >8 h at 3 workers, the remaining graphs are restricted by a further PRIOR amendment; nothing beyond the pilot is run without it.

Environment as PLAN.md. Outputs under evidence/S015/cam83/ with SHA256 manifest.
d453037cac32fd362a591c4f17f5d88cef2b7e3d72b0df3a8971f8d15ff144ba  tools/s015_check.c
