# S017 closeout

S017 executed under the owner invocation `run next session` (owner-revised long-session handoff; Lean work authorised before the Phase 2 novelty audit).

## Result

- **Milestone 1 PASS: the G9 CLEAR counterexample survives an independent cold re-check.** A new checker in a new language and style (tools/s017_g9_dense.lean: a Lean 4 program computing a dense forward dynamic programme over all 2,042,975 configurations of masses 0..16, rank-indexed arrays, no hash set, no candidate generation) reproduces K1c-K4c and K1-K4 exactly; every S016 CLEAR checker re-ran with identical output (one CRLF-only difference); 91/91 S016 hashes match; lemmas C1-C7 and T1-T3 re-checked line by line with no gap. sessions/S017/CLEAR_RECHECK.md. Status: COLD_RECHECK_PASS.
- **Milestone 2: Lean environment.** formal/ with `leanprover/lean4:v4.35.0` and Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679 (tag v4.35.0, exact toolchain match), chosen against the Palomar policy read on 2026-10-16 (minimum v4.35.0-rc2; module system; per-file 10,000-line cap; TOML lakefile; committed manifest; Challenge/Solution/comparator.json). Mathlib from the binary cache only.
- **Milestones 3-4: Lean proofs of both refutations (local kernel build).** Hashed plan PLAN_AMENDMENT_1. A verified exact losing-layer checker (AlmostStacked/Checker.lean, `layer_step`) is evaluated by the kernel (`decide +kernel`) on untrusted certificate layers, one module per layer, and yields the 25 statements of formal/Challenge.lean: G9 connected and not 2-colourable; for STACK and CLEAR separately the size-14 characterisation (only c* and its image, neither AS), every size >= 15 wins, losers in sizes 2..14, stack(G9)=clear(G9)=15, AS thresholds 14, L_all=14, L_AS=13, not ASH*(G9), and the universal negations; general lemmas T1 and monotonicity above the order. Standard axioms only; no sorry, admit or native_decide. Details: sessions/S017/LEAN_RECORD.md, research/S017_LEAN.md, formal/README.md, formal/FROZEN_MODULES.md.
- **Kernel replay:** `leanchecker` (same kernel) replayed all 67 non-root modules, 67/67 OK (PLAN_AMENDMENT_2).
- **Not done (S018):** Comparator run, independent-kernel check (lean4lean / leanexport + nanoda ship with the toolchain), hosted Lean CI (Lean CI is local-only, UNVERIFIED on hosted runners), fresh-session Lean cold re-check, formalization.yaml. No submission.

## Protocol deviations and failures

Pre-amendment kernel benchmark (pilot, not evidence); M1 checker first-run assertion abort (edge order, fixed before any result); two aborted full builds that thrashed the host (archived, not results); a first leanchecker driver run that exceeded its memory cap on the root module (killed, UNKNOWN; addendum 2-i); several ordinary compile failures fixed during development (LEAN_RECORD). All in docs/FAILURE_AND_LESSON_LEDGER.md.

## Gate decision

Phase 1 remains IN_PROGRESS: both clauses are refuted, both cold-rechecked, and both now have local Lean proofs; the owner's gate decision is pending. Phase 3 is IN_PROGRESS (owner-authorised start before Phase 2), NOT passed. **Proposals to the owner (not executed):** (1) record the Phase 1 gate decision; (2) authorise the Phase 2 novelty audit; (3) S018 Lean assurance (Comparator, independent kernel replay, Lean cold re-check) toward a Phase 3 gate. Palomar, arXiv, publication and author contact remain owner-gated; the reply draft to the authors remains NOT SENT.

## Integration

One branch session/S017-clear-recheck-and-lean, one atomic authored commit, ordinary PR, non-force merge if permitted; actual head/tree/parents, hosted jobs and final main are recorded after creation in PR metadata (no circular self-SHA claims here).

## FUTURE S018 handoff (identical to sessions/S017/FUTURE_S018.md and authoritative/NEXT_SESSION_PROMPT.md)

# S018 - Lean assurance for the G9 formalisation: Comparator, independent kernel replay, Lean cold re-check, then submission preparation (owner-gated)

**FUTURE, UNEXECUTED.** Prepared at the S017 closeout (2026-10-17). Requires a fresh explicit owner invocation. Execute exactly S018 in https://github.com/jfairfaxball-348/Almost-Stacked-Proof. S017 is the last completed session. Stop before S019. This prospective handoff does not authorize execution. The owner's S017 authorisation of Phase 3 Lean work (begun before the Phase 2 novelty audit) continues to cover Lean work here; it does NOT authorize any phase PASS, Palomar submission or registration, a manuscript/arXiv, publication or contact with the source authors (each needs separate explicit owner authorization). Reading public registry requirements is allowed.

## Where S017 left the problem

The intended critical Almost Stacked Hypothesis has a STACK clause (connected simple graphs, n>=2) and a CLEAR clause (connected non-bipartite graphs), each of the form

    L_all(G) <= L_AS(G)   (equivalently: some AS loser of size g(G)-1).

Both clauses fail on G9 = graph6 `HCQTaXi` (edges 0-3,0-5,0-6,1-4,1-7,1-8,2-6,2-8,3-5,3-6,4-7,4-8,5-7,6-8): stack=clear=15, the only size-14 losers in both games are (0,0,1,0,0,5,0,8,0) and its image (non-AS), L_all=14>L_AS=13.
- Computational status: STACK COLD_RECHECK_PASS (S016 Gate 1); CLEAR COLD_RECHECK_PASS (S017 Milestone 1: new dense forward DP over all 2,042,975 configurations of masses 0..16 written as a Lean 4 program, all S016 CLEAR checkers replayed identically, 91/91 S016 hashes, C1-C7/T1-T3 re-checked). sessions/S017/CLEAR_RECHECK.md.
- Lean status (S017): `formal/` (Lean `leanprover/lean4:v4.35.0`, Mathlib `56a005855ea17e0b0958f73ec801ae140b0a1679` = tag v4.35.0, module system, TOML lakefile, committed manifest) proves, with standard axioms only and no `sorry`/`native_decide`, the 25 statements of `formal/Challenge.lean` (listed in `formal/comparator.json`): G9 connected and not 2-colourable; for each game the size-14 characterisation, all sizes >=15 win, losers in sizes 2..14, `IsStackNumber G9 15` / `IsClearNumber G9 15`, AS thresholds 14, `L_all=14`, `L_AS=13` (IsGreatest), `¬ ASHStarStack G9`, `¬ ASHStarClear G9`, the universal negations, and the general lemmas T1 (clearable implies stackable) and monotonicity above the order. Proof: a verified exact losing-layer checker (`AlmostStacked/Checker.lean`, theorem `layer_step`) evaluated by `decide +kernel` on untrusted certificate layers (`AlmostStacked/Data/`), one module per layer. Frozen modules: formal/FROZEN_MODULES.md. Measured costs: sessions/S017/LEAN_RECORD.md (each heavy layer check commits up to about 7-9 GB; Lake runs independent modules in parallel, so unstaged full builds on this 16 GB host thrashed and were aborted; the sequential staged build `tools/s017_staged_build.sh` completes, heavy checks 19-73 s each, final `lake build` 1201 jobs; `leanchecker` replay per PLAN_AMENDMENT_2 recorded there).
- Done in S017: a same-kernel `leanchecker` replay of all 67 non-root modules, 67/67 OK (PLAN_AMENDMENT_2; note that leanchecker treats its argument as a module-name prefix, so never pass the root `AlmostStacked`). NOT done: Comparator run; an independent-kernel check (`lean4lean`, `leanexport` + `nanoda_bin` ship with the toolchain); hosted Lean CI (local-only, UNVERIFIED on hosted runners); fresh-session Lean cold re-check of the Challenge statements against research/ASH_SPEC.md; `formalization.yaml`; human-proof formalisation of K1 (not needed: the certificate proves it).
- Other open items unchanged: bipartite critical ASH*-STACK OPEN (no bipartite counterexample known); PB(4,4,2j,1) family a conjecture; order-9 CLEAR 53,286 graphs producer-only; S015 order-9 STACK UNKNOWN list not closed; S014 local items 71-110, 114-115, 117-121 review-pending. Earlier TreeStack (arXiv:2609.31811, registered package) remains credited prior work, not used.

## Entry

Read AGENTS.md, authoritative/START_HERE.md, STATE.json, docs/SESSION_PROTOCOL.md and RELEASE_PROTOCOL.md, formal/README.md, formal/FROZEN_MODULES.md, research/ASH_SPEC.md, research/S017_LEAN.md, the catalogues and all ledgers, sessions/S017/{INPUT,PLAN,PLAN_AMENDMENT_*,CLEAR_RECHECK,LEAN_RECORD,CLOSEOUT}. Pin LIVE remote main and reconcile the actual S017 commit/PR/merge and hosted runs (recorded in PR metadata). Push note: on this host git defaults to a gh credential without write access; push with the stored owner account credential.

## Milestone 1 (mandatory, first): reproduce the S017 Lean build

`cd formal; lake exe cache get`, then the staged build (`bash tools/s017_staged_build.sh`), then `#print axioms` for every compared theorem (`tools/s017_print_axioms.py`) and the forbidden-placeholder scan (`tools/s017_lean_scan.py`). Re-hash every frozen module. Any failure suspends the Lean status: diagnose and record, do not edit frozen modules silently.

## Milestone 2: Comparator and independent kernel replay

1. Build the leanprover/comparator tool at the version Palomar pins (read the current Palomar policy first; record URL/time/commit) and run it on formal/comparator.json; record the full output. If Comparator cannot be built here, record NOT_RUN with the reason (do not substitute the S017 stand-in `tools/s017_challenge_bridge.py`, which is only a local sanity check).
2. Independent kernel check: an export with `leanexport` checked by `nanoda_bin` (an independent kernel implementation) and/or `lean4lean`, each preregistered with caps (memory 12 GiB, wall 2 h per run) and recorded; UNKNOWN at a cap is not a pass.
3. Optionally reduce per-process kernel memory (a heavy layer check commits several GB; e.g. split soundness/completeness into separate modules) so that parallel builds fit 16 GB; any change to a frozen module requires an explicit un-freeze entry and a new full staged build. In isolation STACK and CLEAR checks cost about the same (S017).

## Milestone 3: Lean cold re-check of the statements

Line-by-line review of formal/Challenge.lean against research/ASH_SPEC.md (critical form; t>=2; exact sizes; n=0/1 cases; bipartite exclusion as `¬ G.Colorable 2`; `Fin n` universality), recorded in sessions/S018/LEAN_COLD_RECHECK.md. Any mismatch is a finding: fix in a new module and re-freeze, never silently.

## Milestone 4 (only if 1-3 pass): submission preparation, not submission

Draft `formal/formalization.yaml` (v0.4, in the shape the current Palomar policy asks for; author/maintainer fields left for the owner to confirm), decide with the owner whether the Lean project stays at `formal/` (Palomar section 6.1) or moves to the repository root, and propose to the owner a Phase 1 gate decision (both clauses refuted with Lean proofs), a Phase 2 novelty audit, and the Phase 3 gate. No submission, registration, publication or contact.

## Lean build-efficiency discipline (binding)

Freeze green modules (formal/FROZEN_MODULES.md; frozen modules are not edited; changes need a new module or an explicit un-freeze entry). Build only what changed with targeted `lake build <Module>`; heavy kernel checks in their own modules; full builds only at milestone ends and closeout, STAGED (tools/s017_staged_build.sh) on hosts with <= 16 GB RAM, each recorded with command, wall time, peak memory and result. Record every build failure honestly. No `sorry`, `admit`, unreviewed axioms or `native_decide` in anything called certified.

## Closeout

One branch, one atomic authored session commit, ordinary PR, non-force merge if permitted; pin actual heads/trees/parents/hosted jobs/main after creation. Synchronize state, spec, catalogues, decision/route/failure/session/gate/search ledgers, campaign registry, formal/README.md, formal/FROZEN_MODULES.md and evidence manifests. Prepare a complete FUTURE/UNEXECUTED S019 handoff. Do not claim L_all(G) <= L_AS(G) anywhere beyond computed or proved scopes. Avoid model/vendor names in repository files.

## Computational discipline

Before any computation (including kernel evaluations and external checkers at scale) write and hash a bounded amendment: exact scope, caps, validators, completeness and UNKNOWN policy, code/input/output hashes. Caps are UNKNOWN, never evidence. State the actual environment. Preserve all S003-S017 immutable manifests, failed attempts, protocol deviations and UNKNOWNs.
