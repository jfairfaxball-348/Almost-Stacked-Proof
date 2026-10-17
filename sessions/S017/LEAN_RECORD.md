# S017 Lean record (Milestones 2-4)

Plan: sessions/S017/PLAN_AMENDMENT_1.md (hashed before substantive Lean work). Project: formal/ (README there).

## Environment

Windows 11 Home 10.0.26300; Intel i7-11800H, 16 logical CPUs; 16,086 MB RAM (about 6-7 GB in use by other processes during the builds); 131 GB free disk. elan 4.2.3 (already installed, user level). `lean --version`: Lean (version 4.35.0, x86_64-w64-windows-gnu, commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc, Release). `lake --version`: see evidence/S017/lake_version.txt. Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679 (tag v4.35.0; its lean-toolchain is leanprover/lean4:v4.35.0); Mathlib cache: 9031 files downloaded by `lake exe cache get`, nothing compiled from source.

## Build events (chronological; every failure recorded)

1. Smoke module (trivial theorem): PASS (16 s); deleted after use.
2. `AlmostStacked.Defs` with `import Mathlib`: PASS but 3 min per file (whole-Mathlib load); switched to targeted Mathlib imports (6 s).
3. `Basic`: first build failed (missing order-big-operators import; deprecated `push_neg`), fixed; PASS.
4. `KTree`: failed (recursor-defined functions are not compilable: marked `noncomputable`, kernel-only; two proof steps), fixed; PASS.
5. `Encode`: failed (missing tactic imports; a rewrite direction; an elaboration hint), fixed; PASS.
6. `Checker`: failed (Bool/Nat lemma names; pair projections before `omega`), fixed; PASS.
7. `G9.Graph`: PASS first time.
8. Data modules: failed with `maxRecDepth` during elaboration of the nested tree literals; generator adds `set_option maxRecDepth 100000 in`; PASS.
9. `G9.CheckStack8` alone: PASS (62 s incl. data).
10. `G9.StackLayers` (14 STACK checks, Lake-parallel): PASS, 3 min 08 s wall, peak total lean working set about 11.3 GB (evidence/S017/build_stack_layers.txt).
11. `G9.ClearLayers` (14 CLEAR checks, Lake-parallel): PASS, 13 min 15 s wall; CLEAR checks 6-10 took 10-13 min each under contention (evidence/S017/build_clear_layers.txt).
12. `AlmostStacked.Main`: PASS first time (all 25 statements and lemmas).
13. Linter clean-up of `Basic` (`omit ... in` for unused instance arguments) forced a rebuild of all dependants.
14. First full `lake build`: ABORTED by the session after the machine thrashed (all 28 heavy checks scheduled at once; about 100 MB free RAM); log evidence/S017/full_build_1_aborted_thrashing.txt. Not a result.
15. Staged build v1 (batches of up to 14 checks): ABORTED for the same reason (each heavy check process commits about 7 GB private memory); log evidence/S017/staged_stack_aborted_parallel.txt. Not a result.
16. Staged build v2 (tools/s017_staged_build.sh: one heavy check per Lake invocation, then `lake build`): see the table below.

## Final staged build (milestone/closeout build)

Command: `bash tools/s017_staged_build.sh` (log evidence/S017/staged_build.txt, per-step Lake output in evidence/S017/staged/). Result: **STAGED_BUILD_OK**; the final `lake build` (default targets AlmostStacked, Challenge, Solution) reports `Build completed successfully (1201 jobs)`. Peak private memory of lean processes during this build: about 9.3 GB (one heavy check at a time; sampled every 8 s). Steps whose module had already been compiled by an aborted run (identical sources) show only a replay time of 2-3 s; the times of the heavy modules compiled in this run are their isolated costs.

| step | rc | wall s |
|---|---|---|
| base | 0 | 10 |
| checkStack2 | 0 | 3 |
| checkStack3 | 0 | 2 |
| checkStack4 | 0 | 3 |
| checkStack5 | 0 | 3 |
| checkStack6 | 0 | 24 |
| checkStack7 | 0 | 38 |
| checkStack8 | 0 | 62 |
| checkStack9 | 0 | 73 |
| checkStack10 | 0 | 57 |
| checkStack11 | 0 | 2 |
| checkStack12 | 0 | 3 |
| checkStack13 | 0 | 3 |
| checkStack14 | 0 | 2 |
| checkStack15 | 0 | 3 |
| checkClear2 | 0 | 8 |
| checkClear3 | 0 | 10 |
| checkClear4 | 0 | 10 |
| checkClear5 | 0 | 2 |
| checkClear6 | 0 | 19 |
| checkClear7 | 0 | 33 |
| checkClear8 | 0 | 54 |
| checkClear9 | 0 | 65 |
| checkClear10 | 0 | 2 |
| checkClear11 | 0 | 28 |
| checkClear12 | 0 | 2 |
| checkClear13 | 0 | 3 |
| checkClear14 | 0 | 2 |
| checkClear15 | 0 | 9 |
| full | 0 | 23 |


## Axioms, scan, stand-in comparison, freeze

`tools/s017_print_axioms.py` + `lake env lean` (output evidence/S017/axioms.txt): 59 declarations printed: the 25 compared theorems, `layer_step`, `layer_one` and four layer lemmas depend on exactly [propext, Classical.choice, Quot.sound]; the 28 kernel-evaluated layer checks (`stack_check_t`, `clear_check_t`) depend on no axioms. No `sorryAx`, no `Lean.ofReduceBool`. `tools/s017_lean_scan.py formal`: SCAN_PASS (68 .lean files, module headers, <= 10,000 lines each, no sorry/admit/native_decide/axiom/ofReduceBool/implemented_by/extern outside the deliberate `sorry` of Challenge.lean, Challenge 197 lines). `tools/s017_challenge_bridge.py`: Challenge definitions byte-identical to Defs.lean; all 25 Challenge statements re-stated against the Solution and closed by the Solution theorems (evidence/S017/bridge.txt). This is a local stand-in, NOT Comparator.

Frozen: 67 modules (all except Challenge.lean), formal/FROZEN_MODULES.md.

Kernel replay (PLAN_AMENDMENT_2 with addendum 2-i): `tools/s017_leanchecker.sh` v2 replayed every module except the root `AlmostStacked` (which declares nothing) with the toolchain's `leanchecker`, one process at a time: **LEANCHECKER modules=67 ok=67** (evidence/S017/leanchecker.txt); heavy layer modules 40-80 s and up to about 10 GB each. The first driver run (root module first) exceeded the 12 GiB cap and was killed (UNKNOWN, evidence/S017/leanchecker_run1_aborted.txt). This replay uses the same kernel implementation; it is not an independent kernel and not Comparator.

## Kernel-cost observations for S018

- Kernel time per declaration grows with earlier heavy declarations in the same file; keep one heavy check per module.
- A heavy layer check commits several GB; Lake runs independent modules in parallel with no job limit flag, so on a 16 GB host build them one at a time (staged script).
- In isolation CLEAR and STACK layer checks cost about the same (CheckClear8 54 s, CheckStack8 62 s); the 10-13 min CLEAR times of event 11 were contention/paging, not intrinsic cost.
