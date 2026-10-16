# S015 amendment 7 - CAM-S015-88: complete connected BIPARTITE graphs of order 10; overflow fallback; Python third checks

2026-10-16, BEFORE execution. Runs after the CAM85 order-9 processes release cores.

Tools (sha256; each reproduced v3/v2 critical files byte-identically on the 27-graph S9 test prefix):
- tools/s015_layers_v4.cpp ea0f3ec54155f28c651f18f9c6ad600ab7c34d77440e4d69bb072464ad5d4110 (v3 with unsigned __int128 keys, B=min(16,floor(128/n)); 12 bits at n=10)
- tools/s015_check_v3.c c2e3fe20a7c5d1136b6f73913e89df47783675b4a804b7894df4237dcb275092 (separately written sorted-array checker, __int128, B as above, LSD radix sort)

(1) CAM88 scope: ALL connected bipartite graphs of order 10 from `nauty-geng -c -b 10` (4032 graphs, nauty count). Producer cap 1800 s wall / 4e9 cumulative states per graph; checker cap 400M candidate slots / 1800 s; ulimit -v 6 GiB; at most 4 processes. Critical files compared byte-for-byte. Capped/overflow => UNKNOWN; trees (106 of them) additionally covered by earlier credited TreeStack/S003 Thm 8. Analyses: s015_h2r.py, s015_shift.py, s015_crit_stats.py by membership.

(2) Overflow/cap fallback for CAM85 order 9: any order-9 graph with OVERFLOW/CAPPED/OVER in either v3/check_v2 is rerun with v4 and check_v3 (16 bits at n=9 is not available; B=14 at n=9) with caps 3600 s; still capped => UNKNOWN.

(3) Python third check (s015_validate_v2.py): order 8 graphs whose producer cumulative state count is <= 100000, and order 9 every 100th graph with cumulative states <= 100000 plus EVERY order-9 graph whose critical layer contains a non-AS loser and has cumulative states <= 100000. Wall budget 2 h total at <=2 processes; remainder recorded as compiled-dual only.

No other change. Outcome policy as amendment 1.
