# S019 Palomar packaging record

Plan: PLAN.md and PLAN_AMENDMENT_1.md (both hashed before the runs they govern). Environment: sessions/S019/INPUT.md. Memory sampled every 8 s (tools/s018_memsample.ps1); 12 GiB per-process watchdog every 2 s (tools/s018_memcap.ps1); no watchdog kill in any S019 build.

## Blockers and resolutions

| blocker | resolution |
|---|---|
| B1 research tree about 736 MiB > Palomar's 500 MiB cap | dedicated orphan branch `palomar/submission` with only the Lean project at its root: 876 KB tracked, 76 files |
| B2 non-module `.lean` files outside formal/ | not in the snapshot (68 `.lean` files there, all with the module header) |
| B3 `producer.dll` compiled artefacts in S014 evidence | not in the snapshot |
| B4 unstaged parallel `lake build` memory | 27 check modules and 27 data modules each gain one chaining import line (un-freeze entries in formal/FROZEN_MODULES.md; 54 rows re-frozen as S019) |

## M2 - memory-safe plain build (research repository, formal/)

- Run 1 (check modules chained only; evidence/S019/plain_build_1.txt, mem_plain_build_1.csv): rc 0, 758 s, heavy checks sequential, but peak total private memory 17.9 GB (data modules elaborating in parallel, about 1.2 GB each): preregistered criterion (< 13 GB) FAILED; kept, not relaxed.
- PLAN_AMENDMENT_1: data modules chained in the same order.
- Run 2 (evidence/S019/plain_build.txt, mem_plain_build.csv): plain `lake build` from a clean `.lake/build`, rc 0, 653 s, 1201 jobs, peak total 10.3 GB (9.3 GB in one process), minimum free physical memory 0.77 GB: criterion PASS.
- `#print axioms` output byte-identical to S018 (evidence/S019/axioms.txt); scan PASS (evidence/S019/lean_scan.txt).
- `leanexport` with Palomar's target list: Challenge.export sha256 5af8c78b6ba1cc9e5b50676bf51094f56b9331c587cd385baa3900f771e1930e and Solution.export 855ba7b9cf7a5e2557b3394d22ade3757eda04335f616ac5b0ab06f2cc628b3a, byte-identical to the S018 exports: the import chaining changes no exported declaration. `lake comparator --inadvisably-no-sandbox` with the committed comparator.json (no external kernels): **exit 0, "Your solution is okay!"**, 433 s (evidence/S019/comparator_s019.txt). Because the Solution export is byte-identical, the S018 standalone acceptances by nanoda, con-ron (verified), lean4lean and leanchecker-paranoid apply to these exact bytes.

## M3 - metadata and licence

- formal/formalization.yaml finalised (v0.4): name/description; authors and responsible maintainers John Fairfax-Ball (handoff default, no other name in the invocation); `license: Apache-2.0`; classification math.CO, MSC 05C57, 05C85; sources in original mode (an `original-proof` entry stating that no novelty audit was performed, by owner waiver, and that no priority is claimed; the two hypothesis papers as `background` with authors Tamás Csernák and Lajos Soukup, checked against the arXiv API listings of 2610.09650v1 and 2604.22341v1 on 2026-10-17); `author_endorsement: other` (deviation from the handoff default `not-contacted`, for accuracy: the authors were contacted by the owner on 2026-10-13 and an author reported the intended critical form; the counterexample itself has not been sent to them); TreeStack Palomar entry as an independent related formalisation; automation `agent` naming Claude and Codex (owner decision, limited to this field); review `agent-reviewed`; alignment of the two universal negations.
- Validation: the upstream JSON schema (mathlib-initiative/formalization.yaml commit 99c678e569c7c4c0772db297c5ddd5e4c9b6322e, schema sha256 22bd0b61631535fc68efbdf01e3013362437673ac836d721dfbdf80773244ec3) with jsonschema 4.26.0: 0 errors; Palomar's own loader `submission_contract.load_formalization_metadata` accepts it (below).
- LICENSE: canonical Apache License 2.0 text from https://www.apache.org/licenses/LICENSE-2.0.txt fetched 2026-10-17T10:22:03Z, sha256 cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30, placed only in the snapshot root (the research repository's own licensing is not changed). Palomar's licensee-based detector (scripts/detect_license.rb) was NOT run: no Ruby on this host; the file is the unmodified canonical text.

## M1 - snapshot

tools/s019_make_snapshot.py copied 73 files byte-identically from formal/ (lean-toolchain, lakefile.toml, lake-manifest.json, AlmostStacked.lean, AlmostStacked/**.lean, Challenge.lean, Solution.lean, comparator.json, formalization.yaml) and added LICENSE, README.md (tools/s019_snapshot_README.md) and `.gitignore` (`.lake/`); manifest with sha256 of all 76 files in evidence/S019/snapshot_manifest.txt (validate_governance.py re-checks the 73 copies against formal/). Orphan commit by John Fairfax-Ball; branch `palomar/submission` pushed to origin.

## M4 - pre-upload verification on a fresh clone from GitHub

Fresh `git clone --single-branch --branch palomar/submission` (no autocrlf) of the pushed commit:
- Palomar mechanical pre-checks (tools/s019_palomar_mech.py, calling PalomarSubmission's own functions at d4e41c1d: `tree_size`, `validate_preservable_git_checkout`, `source_requirements.inspect_lean_sources`, `submission_contract.load_formalization_metadata`, `repository_license_file`, `load_comparator_config`, `supported_toolchain`, plus the compiled-suffix list and Challenge limits): **MECH_PASS**, 10/10 (evidence/S019/palomar_mech_fresh_clone.txt). PalomarPolicy 96b034cc and PalomarSubmission d4e41c1d re-pinned 2026-10-17 (unchanged since S017).
- `lake exe cache get` (320 s, Mathlib cache) and plain `lake build` from nothing: rc 0, 677 s, 1201 jobs, peak total 10.3 GB, no kill (evidence/S019/fresh_clone_build.txt, mem_fresh_build.csv).
- Exports from the fresh clone: byte-identical to the research exports above.
- `lake comparator --inadvisably-no-sandbox` with the snapshot's comparator.json on the fresh-clone exports: **exit 0, "Your solution is okay!"**, 410 s (evidence/S019/comparator_fresh.txt).
- Standalone kernel replays of the fresh-clone Solution export (tools/s018_kernels.sh, one thread, 12 GiB cap, 2 h; evidence/S019/kernels_fresh.txt): nanoda ACCEPT (567 s), con-ron --verified ACCEPT, "accepted 6232 declarations" (319 s), lean4lean ACCEPT (514 s), leanchecker-paranoid ACCEPT (506 s); con-leche killed at the 12 GiB cap after 55 s: UNKNOWN (as in S018).

## Not done / limits

No sandboxed (bwrap) run and no Linux run: Palomar's own pipeline will be the first sandboxed run. No hosted Lean CI. Palomar's licence detector not run (no Ruby). Nothing submitted: the owner uploads.
