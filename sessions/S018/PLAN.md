# S018 plan - Lean assurance for the G9 formalisation

2026-10-17. Written and hashed (PLAN.sha256) before any S018 build, export or checker run. Authority: sessions/S018/AUTHORISED_PROMPT.md. Stop before S019. No submission, registration, publication or contact.

## Palomar policy read (Milestone 2 prerequisite)

Read 2026-10-17T06:19Z (UTC) via the GitHub API and fresh clones: PalomarRegistry/PalomarPolicy HEAD 96b034cc31a72a63d4f4041911dce337a85c9a04 (unchanged since S017) and PalomarRegistry/PalomarSubmission HEAD d4e41c1d5b0d114c4859e6e5831dc6d3ad1d0d44 (unchanged since S017); toolchains.json minimum v4.35.0-rc2; verification-profile.json palomar-standard-v1; formalization-profile.json schema_version 4. Facts relied on (paraphrased from .github/workflows/submission.yml, scripts/verify_submission.py and docs/comparator-declaration-closure.md at that HEAD):
- Palomar judges with the `lake comparator` of the SUBMITTED toolchain (no separate leanprover/comparator build; the standalone repository leanprover/comparator, HEAD 865edc14486c3388e9225daa971da8e157488c3e, is not what Palomar runs). Its `leanexport` exports the Challenge and the built Solution, and the judge runs `lake comparator --config <protected config> --challenge-from-export <C> --solution-from-export <S>` inside bwrap.
- The protected configuration registers two external kernels bundled with the toolchain: `nanoda` = `nanoda_bin` and `con-ron` = `con-ron --jobs=2`; Lean's own kernel and `leanchecker` also replay the Solution export.
- Export targets, in order: Quot, Quot.mk, Quot.lift, Quot.ind (as Quot.sound is permitted), the theorem_names, the permitted axioms, the toolchain's `primitiveTargets` (read from the toolchain's Lake source), then definition_names.
So "the version Palomar pins" for Comparator is the one in leanprover/lean4:v4.35.0, already pinned by formal/lean-toolchain.

## M1 Reproduce the S017 build (mandatory, first)

Clean reproduction: move formal/.lake/build aside (renamed, not deleted; Mathlib packages kept), `lake exe cache get`, then the staged build with a copy of the S017 script writing to evidence/S018/ (tools/s018_staged_build.sh; the S017 script writes into evidence/S017 and is not run, to keep S017 evidence immutable). Record wall time per step and peak memory. Then `#print axioms` (tools/s017_print_axioms.py, unchanged), forbidden-placeholder scan (tools/s017_lean_scan.py, unchanged), and re-hash every frozen module against formal/FROZEN_MODULES.md. Caps: staged build 2 h wall; one heavy module at a time. Outcome: all green => M1 REPRODUCED; any failure suspends the Lean status (diagnose, record, no edit of frozen modules).

## M2 Comparator and independent kernels

M2.1 Exports (tools/s018_comparator.sh): with the toolchain `leanexport`, export module `Challenge` and module `Solution` with the Palomar target list (above; primitiveTargets read from the installed toolchain's Lake source and recorded). Hash both exports.
M2.2 `lake comparator --config <config> --challenge-from-export --solution-from-export --inadvisably-no-sandbox`, with a config = formal/comparator.json plus `external_kernels` {nanoda: [nanoda_bin], con-ron: [con-ron, --jobs=2]} (Palomar's protected set). The sandbox is disabled because bwrap does not exist on Windows: a recorded DEVIATION from Palomar's execution (it weakens isolation of untrusted code, which here is our own; it does not change the checks). Full output archived. Exit 0 => COMPARATOR_PASS_LOCAL_UNSANDBOXED; exit 1 => finding (diagnose); exit 2 => NOT_RUN with reason.
M2.3 Also, separately, `--paranoid` (all five bundled external checkers: leanchecker-paranoid, lean4lean, nanoda, con-leche, con-ron) on the same exports, if M2.2 passes; each checker failure recorded individually.
M2.4 Independent kernels standalone if comparator cannot run them: `nanoda_bin` and/or `lean4lean` directly on the Solution export.
Caps (every run): one process at a time, 12 GiB memory (sampled; a run exceeding it is killed), 2 h wall. A cap or crash is UNKNOWN, never a pass. These are kernel replays of the whole Solution closure, including the 28 heavy `decide +kernel` layer checks.
M2.5 (optional) memory reduction of heavy modules: NOT planned unless a cap forces it; any such change needs an un-freeze entry and a new full staged build.

## M3 Lean cold re-check of the statements

Line-by-line review of formal/Challenge.lean against research/ASH_SPEC.md (critical form; t>=2; exact sizes; n=0/1 cases; bipartite exclusion as `¬ G.Colorable 2`; `Fin n` universality; legal moves; terminal definitions for STACK and CLEAR; AS definition; stack/clear numbers; L_all and L_AS as stated), recorded in sessions/S018/LEAN_COLD_RECHECK.md. Any mismatch is a finding, fixed only in a new module with re-freeze, never silently. The S017 bridge script is not relied on (the Comparator is the statement check; M3 is the human semantic check).

## M4 Submission preparation (only if M1-M3 pass)

Draft formal/formalization.yaml against the PalomarPolicy schema v0.4 at the HEAD above, with owner-confirmation placeholders for people fields; record the layout question (formal/ vs root) and Phase 1/2/3 gate proposals for the owner. No submission.

## Closeout

Per AGENTS.md and the handoff: one branch, one atomic session commit, ordinary PR, non-force merge; all ledgers/catalogues/state; FUTURE S019 handoff. No claim of L_all <= L_AS beyond proved/computed scopes.
