# S016 plan amendment 1 - CAM-S016-01..04: CLEAR layer computations (Gate 2)

Written after Gate 1 PASS (GATE1_AUDIT.md) and after the CLEAR lemmas C1-C7 (research/S016_CLEAR.md section 2).

## Protocol deviation recorded before this amendment

While developing the two CLEAR tools below, a 5-graph smoke test (G9, P4, bull, C7, K3; both tools; modes stack and clear) was run BEFORE this amendment was written and hashed. It is archived unchanged in evidence/S016/gate2/smoke_pre_amendment/. It showed G9 ASH_FAIL for CLEAR (L_all=14, L_AS=13, critical layer = the two STACK critical losers). PLAN.md required a hashed amendment before any CLEAR computation, so this is a protocol deviation (recorded in docs/FAILURE_AND_LESSON_LEDGER.md). The smoke result is NOT evidence; every claim below is re-derived by the preregistered runs.

## Tools (frozen for this amendment)

- Producer tools/s016_clear_layers.rs, sha256 51104fabc8c2d2df0b8d06662bd2c5a83d66cf0d79b8e544c8cd1e713a62ca7a, rustc 1.97.1 -O (msvc): hash-set recursion C4-C6, u128 packing w=floor(128/n) bits, OVERFLOW guard, BFS 2-colouring.
- Independent checker tools/s016_clear_check.mjs, sha256 88f2e3db2237a48b69525d1a9c8a9f0ad8db81bbe7709bc6cc25d8ab9f8fd103, Node 24.18.0: separately written (string keys, recursive 0/1 base, receiver-first predecessor generation, double-cover non-bipartiteness test), full critical-layer list.
- Comparators (written after this amendment, hashed in PLAN_AMENDMENT_1_ADDENDA before use): tools/s016_clear_compare.py (producer vs checker, per graph: status, L_all, L_AS, |crit|, critAS and the exact critical-layer list) and tools/s016_frozen_compare.py (producer vs frozen S003 T2/T2b and S004 A7_0025/0252/0506 clear summaries: threshold = L_all+1 and the AS-at-threshold-1 flag).

## Runs

CAM-S016-01 (controls). (a) STACK mode, both tools, on G9: must reproduce S015 (L_all 14, L_AS 13, the two critical losers). (b) CLEAR mode, both tools, on every graph of evidence/S003/T2_analysis.json (orders 1..6) and T2b_analysis.json (all 853 order-7 graphs) using their own labelled edge lists; all non-bipartite results compared with the frozen clear thresholds/ASH flags; the three S003-UNKNOWN order-7 clear graphs compared with the S004 summaries. Any disagreement stops the campaign for diagnosis.

CAM-S016-02 (cheapest test). CLEAR mode, both tools: G9; all 559 graphs of evidence/S015/cam90/family.txt; all 29 graphs of evidence/S015/cam91/family2.txt.

CAM-S016-03 (complete order 8). CLEAR mode, both tools, on all 11117 connected order-8 graphs of evidence/S015/cam82/graphs_8.txt.xz (the frozen S015 nauty-geng list, cross-checked in S015 against the repository's own generator and OEIS A001349; nauty is not available on this host, so the frozen list is used and its sha256 re-checked from evidence/S015/HASHES.md). Bipartite graphs are skipped by both tools independently and the two skip sets must agree. Also orders 2..7 from cam82 graphs_N.txt as a second control set.

CAM-S016-04 (certification, only if an ASH_FAIL appears). For a failing graph, at least: (i) bare-definition CLEAR truth table for every configuration up to mass L_all+2 by a reverse closure from the mass-1 configurations (new tool, separate amendment addendum with hash); (ii) explicit clearing sequences for every AS configuration of mass L_all and every configuration of mass L_all+1, replayed by a separate verifier; (iii) a human proof of non-clearability of the critical witness; (iv) where the authors' public code is unavailable locally it is recorded NOT_RUN.

Caps: producer 8 threads, 3600 s per graph, 5,000,000 states per layer; checker 8 processes, 3600 s per graph, 2,000,000 states per layer. Peak memory is monitored; total resident memory is kept below 12 GiB. CAP/OVERFLOW = UNKNOWN, never ASH_OK; a graph is ASH_OK/ASH_FAIL only when both tools agree on everything compared. Completeness scope: exactly the listed graphs. No extrapolation.

Artefacts: evidence/S016/gate2/cam01..cam04 (inputs, both outputs, critical lists, comparisons, summary JSON), and SHA256 manifest evidence/S016/HASHES.md at closeout.
