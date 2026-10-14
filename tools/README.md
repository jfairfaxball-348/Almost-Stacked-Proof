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

## S004

- `s004_cold.py`: fresh full reverse-winning DP and forward closure; printed audit, boundaries and n<=4 minimality.
- `s004_frontier.py`: all-parent sparse losing recurrence, preregistered21-case campaign.
- `s004_verify_frontier.py --check-only`: independent packed canonical-parent complete replay of all21 compressed certificates; no producer import.
- `s004_check_base.py --check-only`: cold full reverse-winning DP base-layer comparison for all21 cases.
- `s004_structure.py --check-only`: original sequence/closure replay and complete n<=5 structural extrema.
- `s004_witness_tests.py --check-only`: every independent set/root on connected n<=5 (233 tests).

Run from repository root. `--check-only` avoids rewriting evidence; regeneration without it creates runtime timing fields. Mathematical proofs in research/S004_ASHSTAR_ATTACK.md. No external packages required.

S005: s005_sparse.cpp complete all-parent packed losing recurrence; s005_campaign.py exact graph inputs, caps and certificate serialization; s005_verify.py independent canonical-parent set equality and full reverse-winning bases; s005_geodesic.py bounded BFS witness challenge; s005_pure.py pure-pile theorem prediction; s005_check_traces.py independent arithmetic replay. See S005 PLAN/amendments for exact scopes. Binary certificate format is little-endian mass/count then uint128 states with8-bit coordinates; raw decoded hashes in summaries. No state symmetry and no Lean certification.

S005 additional streamed checker: s005_stream_check.cpp uses decoded coordinate arrays and canonical candidates, streaming one layer at a time; s005_stream_verify.py verifies hashes/per-layer extrema and independently recomputes winning base layers. It reduces replay memory without weakening full-set completeness. PLAN_AMENDMENT_7 records the implementation change; original Python replay remains in the evidence.

## S006 exact rooted interfaces (local and hosted replay)

`python tools/s006_grammar.py` creates pure/buffer minimum-source certificates; `python tools/s006_verify.py --check-only` independently checks every local inequality, infinity and attaining legal tree. `python tools/s006_stack.py` creates the separate forest certificate; `python tools/s006_stack_verify.py --check-only` independently checks forests and full dual rooted-stacking layers. `python tools/s006_challenges.py --check-only` replays registered full forward/reverse rooted-clearing masks; `python tools/s006_extrema.py --check-only` challenges inherited critical support/residue classes; `python tools/s006_obstruction_verify.py --check-only` checks complete auxiliary closures/traces. Check-only commands preserve evidence. Exact scopes/cutoff in S006 AUDIT; none is a universal ASH* or Lean test.

## S007

`python tools/s007_provenance.py` reads entry APIs/current primary digests and hashes (entry-specific, not for repinning later sessions). `python tools/s007_tail.py` generates CAM-S007-01 full forward layers and selected-ancestry traces; `--stack` selects CAM-S007-02. `python tools/s007_tail_verify.py --check-only` recomputes complete independent reverse layers and every legal trace; `--stack` for the separate goal. No producer import. Symbolic proof in S007 report; finite scope l=0,1,2 only.

## S008

`python tools/s008_tip.py` generates registered l0..8 named-buffer tree/forest certificates. `python tools/s008_tip_verify.py --check-only` checks every optimality inequality/attaining tree/forest and complete candidate closures l0..3; imports the independent S006 tree checker, no optimizer import. `python tools/s008_symbolic.py --check-only` verifies universally nonnegative linear production differences by exact integer coefficients/domains, not sampled graph lengths. `python tools/s008_branches.py` generates registered F_k k1..3 forward layers/constructive traces; `python tools/s008_branches_verify.py --check-only` recomputes full reverse sets and literal legal trace arithmetic. All check-only commands preserve stored evidence. `s008_provenance.py` is pinned entry-specific, not a future repinner. No universal ASH*/Lean/novelty test.
