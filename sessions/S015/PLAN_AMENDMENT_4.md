# S015 amendment 4 - CAM-S015-85: full order-9 STACK atlas with faster dual compiled tools

2026-10-16, BEFORE execution. Amendment-2 S9 sample (v2 producer, 60 s cap) was stopped by the operator once the timing estimate was available: 1481 of 2611 S9 graphs completed ASH_OK single-implementation, 1 CAPPED (H?ABAqW, 60 s, contention), rest unexecuted. Archived as evidence/S015/cam83/prod_S9_part*.txt / crit_prod_S9_part*.txt; superseded by this campaign; no claim from S9 alone.

New tools (sha256 before execution; tested only on 27 S9 graphs where both reproduced v2 totals/critical layers byte-identically):
- tools/s015_layers_v3.cpp b0ca2180db9b2da9c5934742c2946ad87ec2632ba0c87daec525ee1b0736ab94: identical recursion, uint64 packing (B=floor(64/n), 7 bits at n=9), flat open addressing, per-layer seen-table. OVERFLOW if a coordinate would reach 2^B-1.
- tools/s015_check_v2.c 88a9402279b2be74ddace21de0733c702a36a3faab4774bd9606361b3faafce8: the separately written sorted-array checker with uint64 keys and LSD radix sort; OVERFLOW likewise.
Build: g++/gcc 13.3.0 -O3 -march=native.

Scope: ALL 261080 lines of evidence/S015/cam83/graphs_9.txt (nauty-geng -c 9, count = OEIS A001349). Producer caps 300 s wall/2e9 cumulative states per graph; checker caps 150M candidate slots/300 s CPU per graph; ulimit -v 4 GiB; 4 producer-or-checker processes at once (4 cores). Work split into 8 contiguous chunks; producer and checker critical files compared byte-for-byte per chunk.

Fallback: graphs reported OVERFLOW or CAPPED/OVER by either tool are rerun by v2 producer (16-bit coordinates, 3600 s) and v1 checker (12-bit, 3600 s); still capped => UNKNOWN (trees additionally covered by earlier credited TreeStack + October Thm 5.2 witness, S003 Thm 8).

Third check: Python v2 set-validator on every 100th graph plus every graph with a non-AS critical loser of heavy count >= 2 among those with producer total states <= 300000 (otherwise recorded as compiled-dual only).

Analyses on the complete order-9 critical files (membership only): s015_h2r.py, s015_shift.py (items 122/123), even-heavy tallies.

Outcome classes and policies as amendment 1 (ASH_OK_DUAL / ASH_FAIL candidate -> certification / UNKNOWN). No extrapolation beyond order 9.
