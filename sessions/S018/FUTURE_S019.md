# S019 - Sandboxed Comparator and hosted Lean CI for the G9 formalisation; owner-gated Phase 2 novelty audit

**FUTURE, UNEXECUTED.** Prepared at the S018 closeout (2026-10-17). Requires a fresh explicit owner invocation. Execute exactly S019 in https://github.com/jfairfaxball-348/Almost-Stacked-Proof. S018 is the last completed session. Stop before S020. This prospective handoff does not authorize execution. The owner's S017 authorisation of Phase 3 Lean work continues to cover Lean work here; it does NOT authorize any phase PASS, Palomar submission or registration, a manuscript/arXiv, publication or contact with the source authors (each needs separate explicit owner authorization). Reading public registry requirements is allowed.

## Where S018 left the problem

The intended critical Almost Stacked Hypothesis has a STACK clause (connected simple graphs, n>=2) and a CLEAR clause (connected non-bipartite graphs), each of the form

    L_all(G) <= L_AS(G)   (equivalently: some AS loser of size g(G)-1).

Both clauses fail on G9 = graph6 `HCQTaXi` (edges 0-3,0-5,0-6,1-4,1-7,1-8,2-6,2-8,3-5,3-6,4-7,4-8,5-7,6-8): stack=clear=15, the only size-14 losers in both games are (0,0,1,0,0,5,0,8,0) and its image (non-AS), L_all=14>L_AS=13. Computational status: STACK and CLEAR COLD_RECHECK_PASS (S016, S017).

Lean status after S018 (sessions/S018/LEAN_ASSURANCE.md, LEAN_COLD_RECHECK.md, SUBMISSION_PREP.md):
- S017 build reproduced from a clean `.lake/build` (staged, 829 s, 1201 jobs; axioms standard; scan PASS; 67/67 frozen hashes).
- `lake comparator` of the pinned toolchain (the tool Palomar judges with) on `leanexport` exports with Palomar's target list, UNSANDBOXED (`--inadvisably-no-sandbox`; Windows host, no bwrap): run 1 found F1 (universe parameter `u_2` vs `u_1` in three general lemmas of Challenge.lean, from a redundant `{V : Type*}` re-binding), fixed in Challenge.lean only; run 2: statement comparison and axiom check PASS for all 25 names, Lean kernel ACCEPT; nanoda and con-ron killed by the 12 GiB cap at Palomar's thread counts (UNKNOWN). Standalone single-thread replays of the same Solution export: nanoda ACCEPT, con-ron (verified) ACCEPT, lean4lean ACCEPT, leanchecker-paranoid ACCEPT, con-leche UNKNOWN (cap).
- Statement cold re-check of Challenge.lean against research/ASH_SPEC.md: PASS after F1.
- formal/formalization.yaml: DRAFT, NOT SUBMITTED; owner items in SUBMISSION_PREP.md (no repository LICENSE file; human author/maintainer fields; automation disclosure vs AGENTS.md rule 12; original-proof origin pending Phase 2; layout recommendation keep `formal/`).
- Not done: a sandboxed Comparator run with exit 0 including external kernels; hosted Lean CI (UNVERIFIED on hosted runners).
Other open items unchanged: bipartite critical ASH*-STACK OPEN; PB(4,4,2j,1) family a conjecture; order-9 CLEAR 53,286 graphs producer-only; S015 order-9 STACK UNKNOWN list not closed; S014 local items 71-110, 114-115, 117-121 review-pending. Earlier TreeStack (arXiv:2609.31811, registered package) remains credited prior work, not used.

## Entry

Read AGENTS.md, authoritative/START_HERE.md, STATE.json, docs/SESSION_PROTOCOL.md and RELEASE_PROTOCOL.md, formal/README.md, formal/FROZEN_MODULES.md, research/ASH_SPEC.md, the catalogues and all ledgers, sessions/S018/{INPUT,PLAN,PLAN_AMENDMENT_*,LEAN_ASSURANCE,LEAN_COLD_RECHECK,SUBMISSION_PREP,CLOSEOUT}. Pin LIVE remote main and reconcile the actual S018 commit/PR/merge and hosted runs (recorded in PR metadata). Record any owner decisions on the S018 gate proposals and owner items that the invocation contains; do not assume any.

## Milestone 1 (first): hosted Lean CI on a Linux runner

Add a GitHub Actions workflow (separate from governance.yml, or a separate job) that on a GitHub-hosted ubuntu runner installs the pinned elan (v4.2.3, checksum as Palomar uses) and the toolchain in formal/lean-toolchain, runs `lake exe cache get`, the staged build (tools/s018_staged_build.sh or a CI copy writing to a temporary directory), the axiom print and the placeholder scan. Hosted runners have about 16 GB RAM; build heavy modules one at a time. Record actual run IDs, job conclusions and timings from the GitHub API; a workflow file without a completed green run is UNVERIFIED. Do not weaken governance.yml.

## Milestone 2: sandboxed Comparator on Linux

In the same or a separate hosted job (manually dispatched if long): install bubblewrap (Palomar builds v0.12.0 from source; the distribution package is acceptable if recorded), export Challenge and Solution with `leanexport` and Palomar's target list (tools/s018_comparator.sh shows it), and run `lake comparator --config <cfg> --challenge-from-export ... --solution-from-export ...` WITHOUT `--inadvisably-no-sandbox`, with external kernels nanoda and con-ron as Palomar registers them. If the 16 GB runner cannot hold nanoda at 4 threads (S018 measured 14.6 GB+ before its cap), record that and run the external kernels standalone at 1 thread in the sandbox instead; a run killed by the runner is UNKNOWN, not a pass. Archive the full transcript and export hashes. Preregister caps before running.

## Milestone 3: owner-gated items (only those the invocation authorises)

- If authorised: the Phase 2 first novelty/prior-art audit of the G9 counterexample (timestamped queries, primary citations, closest results, explicit uncertainty; no worldwide priority claim).
- If the owner has chosen a licence and confirmed people fields: add the LICENSE file and complete formal/formalization.yaml (still no submission without separate explicit authorisation).
- Record any owner gate decisions (Phase 1, Phase 3) exactly as given.

## Lean build-efficiency discipline (binding)

Frozen modules are not edited (formal/FROZEN_MODULES.md; changes need a new module or an explicit un-freeze entry). Targeted builds; heavy kernel checks one at a time on hosts with <= 16 GB; full builds only at milestone ends and closeout, each recorded with command, wall time, peak memory and result. Record every failure honestly. No `sorry`, `admit`, unreviewed axioms or `native_decide` in anything called certified.

## Closeout

One branch, one atomic authored session commit, ordinary PR, non-force merge if permitted; pin actual heads/trees/parents/hosted jobs/main after creation. Synchronize state, spec, catalogues, decision/route/failure/session/gate/search ledgers, campaign registry, formal/README.md, formal/FROZEN_MODULES.md and evidence manifests. Prepare a complete FUTURE/UNEXECUTED S020 handoff. Do not claim L_all(G) <= L_AS(G) anywhere beyond computed or proved scopes. Avoid model/vendor names in repository files.

## Computational discipline

Before any computation (including CI kernel runs) write and hash a bounded amendment: exact scope, caps, validators, completeness and UNKNOWN policy, code/input/output hashes. Caps are UNKNOWN, never evidence. State the actual environment. Preserve all S003-S018 immutable manifests, failed attempts, protocol deviations and UNKNOWNs.
