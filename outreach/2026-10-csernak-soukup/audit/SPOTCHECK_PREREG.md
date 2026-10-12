# Pre-registration: fresh spot-check of evidence/S003/T2b_analysis.json (written before running)

- **Population:** the 853 records in `evidence/S003/T2b_analysis.json` (all connected 7-vertex graphs; S003 cap t ≤ 55).
- **Sampling:** a uniformly random permutation from `random.Random(20261012).sample(range(853), 853)`, processed in order.
- **Full verification:** a graph is fully verified if every relevant goal has a recorded threshold g and C(g_max+6, 6) ≤ 1,500,000, where g_max is the largest threshold over stacking and, for non-bipartite graphs, clearing.
  - The fresh layered DP (`verify_fresh.py`, sizes 2..g+1, stacking and, for non-bipartite graphs, clearing separately) recomputes five quantities: the threshold, the literal AS threshold, whether an AS loser exists at g−1 (ASH*), the literal gap sizes in (n, g), and the literal-ASH verdict.
  - Each is compared with the record. Bipartiteness is recomputed too.
- **Skipped graphs:** graphs over the cap or undecided in S003 are recorded as SKIPPED and not counted.
- **Stopping rule:** stop after 20 fully verified graphs.
- **Pass criterion:** zero disagreements, and an AS loser at g−1 for every fully verified graph and goal. Any disagreement means the email's evidence claim is weakened or removed, and the discrepancy is reported.
- **Completeness scope:** a sample check only. It does not re-establish the full n=7 census.

## Addendum (written after the T2b run and before this run): full fresh re-check of evidence/S003/T2_analysis.json
- **Population:** all 143 records (connected graphs with 1 ≤ n ≤ 6), in the same seeded order. The layer cap is raised to 5,000,000, so every decided graph is fully verified.
- **Quantities and pass criterion:** as above. The one-vertex graph K1 is expected to have no AS loser at size g−1 = 1. That is the |V| ≥ 2 boundary case and not a disagreement, because its threshold form ASH* holds trivially.
- **Scope:** complete for n ≤ 6, a census re-check by a fresh implementation. Command: `python3 verify_fresh.py spot ../../../evidence/S003/T2_analysis.json 143 recheck_T2_n_le_6.json 5000000`.
