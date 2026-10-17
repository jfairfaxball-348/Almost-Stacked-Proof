# S018 Lean assurance record (Milestones 1 and 2)

Plan: PLAN.md, PLAN_AMENDMENT_1.md (finding F1), PLAN_AMENDMENT_2.md (single-thread kernel replays), each hashed before the runs it governs. Environment: sessions/S018/INPUT.md (Windows 11, i7-11800H 16 threads, 16 GB RAM of which about 9 GB free, Lean 4.35.0 commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc, Mathlib 56a00585). Memory: sampled every 8 s (tools/s018_memsample.ps1, evidence/S018/mem_*.csv; sampled peaks understate true peaks); 12 GiB per-process cap enforced every 2 s by tools/s018_memcap.ps1 (kills in evidence/S018/memcap_kills.txt).

## M1 - reproduction of the S017 build: PASS

- formal/.lake/build moved aside (kept, not deleted); `lake exe cache get` (Mathlib cache already present, nothing downloaded); clean staged build with tools/s018_staged_build.sh (a copy of the S017 script writing to evidence/S018): STAGED_BUILD_OK, 30 steps, total 829 s, final `lake build` 1201 jobs (evidence/S018/staged_build.txt, evidence/S018/staged/). Heavy checks 53-72 s each (Stack8-10, Clear8-10), in line with S017. Peak sampled memory 10.3 GB total, 9.3 GB in one `lean` process, 0.8 GB free physical memory at that moment.
- `#print axioms` (tools/s017_print_axioms.py, unchanged): 59 declarations; 31 depend on exactly [propext, Classical.choice, Quot.sound], the 28 kernel-evaluated layer checks on no axioms; no sorryAx or Lean.ofReduceBool (evidence/S018/axioms.txt; identical again at closeout, axioms_closeout.txt).
- tools/s017_lean_scan.py: SCAN_PASS (evidence/S018/lean_scan.txt).
- Re-hash of every frozen module: 67/67 match formal/FROZEN_MODULES.md (evidence/S018/frozen_rehash.txt).

## M2 - Comparator and independent kernels

What Palomar runs (PLAN.md, read 2026-10-17T06:19Z): the `lake comparator` of the submitted toolchain on `leanexport` exports, with external kernels nanoda (`nanoda_bin`) and con-ron (`con-ron --jobs=2`), inside bwrap. This host has no bwrap and no WSL, so every run here used `--inadvisably-no-sandbox`. That is a DEVIATION from Palomar's execution: it removes isolation of the code being judged (here our own), and does not change any check; the tool prints "WARNING: Sandbox disabled, this run is not trustworthy." The verdicts below are therefore LOCAL_UNSANDBOXED.

Exports (tools/s018_comparator.sh; target list = Quot, Quot.mk, Quot.lift, Quot.ind, the 25 theorem names, the three permitted axioms, and the 26 `primitiveTargets` of Lake/CLI/Check.lean at v4.35.0). Exports are not committed (size); hashes:

| run | Challenge.export sha256 | Solution.export sha256 |
|---|---|---|
| 1 (S017 Challenge) | 934eaa13a42ad61c8051d6158953b562e0e572dbb2cc6a4ea4434f5959456a3d (8,971,223 B) | 855ba7b9cf7a5e2557b3394d22ade3757eda04335f616ac5b0ab06f2cc628b3a (30,377,549 B) |
| 2 (F1-fixed Challenge) | 5af8c78b6ba1cc9e5b50676bf51094f56b9331c587cd385baa3900f771e1930e (8,970,562 B) | 855ba7b9cf7a5e2557b3394d22ade3757eda04335f616ac5b0ab06f2cc628b3a (same) |

Run 1 (evidence/S018/comparator_run1.txt): exit 1, "Challenge and solution theorem statement do not match: 'AlmostStacked.clearable_stackable'". Finding F1, diagnosed with tools/s018_export_diff.py (evidence/S018/f1_diagnosis.txt): the S017 Challenge gave `clearable_stackable`, `stackable_above` and `clearable_above` the universe parameter `u_2` (a redundant `{V : Type*}` re-binding inside a section with the same `variable`), the Solution `u_1`; nothing else differs (`#check` with `pp.all` prints identical statements because the universe is renamed for display: evidence/S018/diagall_*.txt). Fixed in Challenge.lean only (PLAN_AMENDMENT_1); no frozen module changed; `lake build Challenge` 8 s.

Run 2 (evidence/S018/comparator_run2.txt, flags: none besides the sandbox switch; 549 s): no statement or axiom error, i.e. `compareAt` (all 25 statements identical, transitive constant closure identical, primitives) and `checkAxioms` (only propext, Quot.sound, Classical.choice) PASSED; Lean's own kernel (`leanchecker --silent --from-export`) accepted the Solution export. The two external kernels were killed by the 12 GiB cap (con-ron at 12,376 MB with 2 jobs; nanoda_bin at 14,655 MB with 4 threads) and therefore reported as "rejected"; overall exit 1. Under the plan these two are UNKNOWN (cap), not rejections.

Standalone replays (PLAN_AMENDMENT_2, tools/s018_kernels.sh, evidence/S018/kernels.txt and kernels/; same Solution export 855ba7b9..., sequential, 12 GiB cap, 2 h each):

| checker | command | result | wall | sampled peak |
|---|---|---|---|---|
| nanoda (independent Rust kernel; Palomar-registered) | `nanoda_bin cfg` with num_threads 1 | exit 0: ACCEPT | 585 s | 8.3 GB |
| con-ron (Palomar-registered; verified mode) | `con-ron --jobs=1` | exit 0: "accepted 6232 declarations (--verified)" | 343 s | 8.8 GB |
| lean4lean | `lean4lean --import` | exit 0: ACCEPT | 545 s | 8.0 GB |
| leanchecker-paranoid | `--silent --from-export` | exit 0: ACCEPT | 535 s | 9.9 GB |
| con-leche | `con-leche` | killed at the 12 GiB cap after 41 s: UNKNOWN | 41 s | >12 GB |

## Verdicts

- M1: S017_BUILD_REPRODUCED.
- M2: COMPARATOR statement and axiom check PASS_LOCAL_UNSANDBOXED (after F1); Lean kernel ACCEPT; independent kernels nanoda ACCEPT and con-ron ACCEPT (both at one thread, standalone, outside lake comparator), lean4lean and leanchecker-paranoid ACCEPT; con-leche UNKNOWN (cap). Not established: a single `lake comparator` run with exit 0 including the external kernels (on this host they exceed the cap at Palomar's thread counts; Palomar's default runner has 32 GB), a sandboxed run, and hosted Lean CI.
- The S017 stand-in tools/s017_challenge_bridge.py could not detect F1 (it re-elaborates statements); it remains a sanity check only.
