# Tools and checks

S002: `cam_s002_01.py` (forward recursion, six 8-vertex graphs) and `reverse_cold_check.py`.

S003 (CAM-S003-01; preregistered in `sessions/S003/PLAN.md` and `PLAN_AMENDMENT_1.md`):

| File | Role | Independence |
|---|---|---|
| `cam_s003_fwd.c` | Forward layered exact DP over all compositions of each size, both goals, per-layer counts and order-free fingerprints of the losing sets | primary solver |
| `cam_s003_rev.c` | Reverse predecessor propagation (W_t = goal_t ∪ parents(W_{t−1})) with lexicographic ranking from a recurrence table | written separately; no shared code |
| `cam_s003_pyrev.py` | Pure-Python set-based reverse fixpoint (generalises S002 checker), layers ≤ 5M | third implementation |
| `cam_s003_as.c` | Per-configuration memoised exact search over AS configurations below a known stacking number (trees) | used for T3 only |
| `cam_s003_cert.py` | Builds and checks literal AS-gap certificates: replays a winning move sequence for every AS configuration of size t and recomputes the loser's full, closed, goal-free reachable set | shares no code with the C tools |
| `cam_s003_graphs.py` | Named graphs; self-generated atlas (counts asserted against OEIS A000088/A001349) and AHU-coded trees (A000055) | — |
| `cam_s003_run.py`, `cam_s003_trees.py` | Drivers and AS-gap analysis (S003 Thm 4) | — |

Build and reproduce (Python ≥3.11, gcc with OpenMP):
```
gcc -O2 -fopenmp -o fwd tools/cam_s003_fwd.c && gcc -O2 -o rev tools/cam_s003_rev.c && gcc -O2 -o as tools/cam_s003_as.c
python3 tools/cam_s003_run.py T2 . out_T2          # tiers T1, T4, T2, T2b, A3
python3 tools/cam_s003_trees.py ./as T3.json 9 300 out_T2/summary_T2.json
python3 tools/cam_s003_cert.py check evidence/S003/cert_P4_stack_t12.json
```
The certificate checks also run in hosted CI (`.github/workflows/governance.yml`).
