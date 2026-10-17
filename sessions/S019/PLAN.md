# S019 plan - full Palomar packaging

2026-10-17. Written and hashed (PLAN.sha256) before any build, export or checker run. Authority: AUTHORISED_PROMPT.md (owner-revised; decisions: Apache-2.0, Claude and Codex named only in formalization.yaml automation metadata, novelty audits OWNER_WAIVED, author/maintainer John Fairfax-Ball). Stop before S020. No submission.

## M2 (first) - memory-safe plain `lake build` (blocker B4)

Change: serialise the 28 heavy kernel-evaluation modules by ONE linear import chain, adding exactly one line `public import AlmostStacked.G9.<previous>` to each of CheckStack3..15 (previous = CheckStack(t-1)), CheckClear2 (previous = CheckStack15) and CheckClear3..15 (previous = CheckClear(t-1)). No other byte of any module changes; theorem statements and proofs unchanged. These 27 modules are frozen: un-freeze entries (old hash, reason B4) are written in formal/FROZEN_MODULES.md before the edit, and the new hashes are re-frozen after the build passes. Lake schedules by imports, so no two heavy evaluations can run concurrently in a plain `lake build`; cheap data modules may still run in parallel.
Acceptance test (caps): on this 16 GB host, after moving `.lake/build` aside, plain `lake build` (no staged script) completes; wall cap 2 h; peak total private memory of Lean processes sampled every 8 s (tools/s018_memsample.ps1) below 13 GB; the 12 GiB per-process watchdog (tools/s018_memcap.ps1) runs throughout (a kill is a FAIL of the acceptance test, not a pass). Then axioms (tools/s017_print_axioms.py) identical to evidence/S018/axioms.txt, scan PASS, Comparator statement check re-run unsandboxed (tools/s018_comparator.sh) with expected verdict as S018 run 2.

## M3 - formalization.yaml final and LICENSE

Finalize per the handoff (Apache-2.0; authors/maintainers John Fairfax-Ball; automation methods naming Claude and Codex; original-proof origin with novelty waiver stated; source author lists checked against arXiv listings; author_endorsement not-contacted). LICENSE: canonical Apache License 2.0 text fetched from https://www.apache.org/licenses/LICENSE-2.0.txt (URL, time, sha256 recorded). Validate the YAML against the upstream schema (mathlib-initiative/formalization.yaml, commit recorded) with a JSON-schema validator, and Palomar taxonomy snapshots.

## M1 - snapshot

Orphan branch palomar/submission in this repository; root layout = byte-identical copies of formal/{lean-toolchain, lakefile.toml, lake-manifest.json, AlmostStacked.lean, AlmostStacked/, Challenge.lean, Solution.lean, comparator.json, formalization.yaml}, plus LICENSE, README.md (snapshot-specific) and .gitignore (`.lake/`). Copies are hashed against the research commit. Built by tools/s019_make_snapshot.py into a separate worktree.

## M4 - pre-upload verification on a fresh clone of the snapshot commit

Re-read PalomarPolicy/PalomarSubmission HEADs. Mechanical checks (tools/s019_palomar_mech.py, written from the policy text, plus any PalomarSubmission script runnable without submitting): tree size < 500 MiB, no symlinks/submodules/LFS, no compiled-artefact suffix, every .lean has the module header and <= 10,000 lines, Challenge <= 1,000 lines and 100 KiB, exactly one licence file and SPDX = project.license, comparator.json keys/allowlist, toolchain >= minimum and = Mathlib's lean-toolchain, committed manifest, formalization.yaml schema-valid. Then `lake exe cache get`, plain `lake build` from clean (M2 acceptance caps), exports + `lake comparator` unsandboxed (verdict expected as S018 run 2), nanoda and con-ron standalone at one thread (12 GiB, 2 h each). Caps are UNKNOWN, never passes. Any failure: fix in the snapshot, new commit, re-verify.

## Closeout

Research repo: one atomic session commit, PR, non-force merge. Snapshot branch pushed separately (it is the upload target, not a research-session commit; its SHA and tree recorded). S020 placeholder only.
