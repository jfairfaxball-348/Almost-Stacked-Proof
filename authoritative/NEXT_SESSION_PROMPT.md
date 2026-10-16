# S017 - long ambitious session: cold re-check of the G9 CLEAR counterexample, local Lean setup, formalisation plan, and as much Lean formalisation as the session can carry

**FUTURE, UNEXECUTED.** Owner-directed revision (2026-10-16) of the frozen S016 handoff sessions/S016/FUTURE_S017.md; the owner's request is archived verbatim in authoritative/handoffs/S017_OWNER_REQUEST_2026-10-16.txt. Requires a fresh explicit owner invocation. Execute exactly S017 in https://github.com/jfairfaxball-348/Almost-Stacked-Proof. S016 is the last completed session. Stop before S018. This is a LONG, AMBITIOUS session: do not stop at the first milestone; continue until the context budget makes a clean closeout and handover the better choice, then close out properly (never mid-step, never with an unrecorded build state). This prospective handoff does not itself authorize execution.

**Owner authorization carried by this revision.** The owner explicitly asks S017 to set up a local Lean environment and to BEGIN Lean formalisation (Phase 3 work) of the G9 counterexample. This is an owner-authorised revision of the AGENTS.md rule-10 stage order: Lean work may start before the Phase 2 novelty audit. Record it as such in the decision and phase-gate ledgers. It does NOT mark Phase 1, 2 or 3 PASS; it does not authorize Palomar submission or registration, a manuscript/arXiv, publication or any contact with the source authors (each still needs separate explicit owner authorization). Reading the public Palomar registry requirements is allowed; submitting anything to it is not.

## Where S016 left the problem

The intended critical Almost Stacked Hypothesis has a STACK clause (connected simple graphs, n>=2) and a CLEAR clause (connected non-bipartite graphs), each of the form

    L_all(G) <= L_AS(G)   (equivalently: some AS loser of size g(G)-1).

On G9 = graph6 `HCQTaXi` (edges 0-3,0-5,0-6,1-4,1-7,1-8,2-6,2-8,3-5,3-6,4-7,4-8,5-7,6-8; non-bipartite via triangle 0-3-5) both clauses fail:
- STACK: stack=15, L_all=14>L_AS=13 (S015); S016 Gate 1 COLD_RECHECK_PASS (sessions/S016/GATE1_AUDIT.md, hand-proof repairs R1-R3). LEAN_PENDING.
- CLEAR (S016, research/S016_CLEAR.md): clear=15; the only mass-14 non-clearable configurations are the two STACK critical losers (0,0,1,0,0,5,0,8,0) and image, neither AS; every AS configuration of mass 14 and every configuration of mass 15 clears; L_all=14>L_AS=13. COMPUTED_EXACT (bare-definition backward closure from mass-1 configurations, 492,618 replayed clearing sequences with a separate verifier, closures without mass-1 states, dual layer tools; hand proof of non-clearability via T1: clearable implies stackable). INDEPENDENT_COLD_RECHECK_PENDING, LEAN_PENDING. The authors' public clearing code was not run.
- Atlases: all non-bipartite connected graphs of order <=8 satisfy CLEAR (dual), so 9 is minimal; order 9 producer-complete with G9 unique, dual for 207,794 graphs (53,286 producer-only). S014 local items 71-110, 114-115 and 117-121 remain review-pending (not needed for G9). Earlier TreeStack (arXiv:2609.31811, registered package) remains credited prior work; S003/S004 printed-form counterexamples are a separate statement.

## Entry

Read AGENTS.md, authoritative/START_HERE.md, STATE.json, docs/SESSION_PROTOCOL.md and RELEASE_PROTOCOL.md, formal/README.md, research/ASH_SPEC.md, the catalogues and all ledgers (including docs/HANDOFF_REVISION_LEDGER.md and authoritative/HANDOFF_REVISION_S017.json), sessions/S016/{INPUT,PLAN,PLAN_AMENDMENT_*,GATE1_AUDIT,AUDIT,CLOSEOUT}, research/S015_G9_COUNTEREXAMPLE.md and research/S016_CLEAR.md. Pin LIVE remote main and reconcile the actual S016 commit 19537a9e / PR #20 / merge 378652c7, the hosted run on that merge push, and this revision's own commit/PR (recorded in PR metadata). Push note: on this host git defaults to a gh credential without write access; push with the stored owner account credential (as done for PR #20).

## Milestone 1 (mandatory, first): independent cold re-check of the G9 CLEAR counterexample

1. Re-derive the CLEAR definitions and threshold convention (S003 Lemma 1/2, Prop. 3, Thm 4 with g=clear; October Lemma 4.7; terminal = total mass exactly 1; bipartite exclusion) and check C1-C7 and T1-T3 of research/S016_CLEAR.md line by line.
2. Write a NEW checker in a style not used in S015/S016 (for example a SAT/BDD encoding of K2c/K3c, an exact layer computation in another language with a different data structure, or — efficiently combined with Milestone 3 — a Lean-evaluated checker), preregister it in a hashed plan, and re-verify K1c-K4c.
3. Replay the S016 CLEAR checkers and compare with evidence/S016/HASHES.md.
4. Outcome rule: all agree => CLEAR refutation COLD_RECHECK_PASS; any discrepancy => suspend the CLEAR status, diagnose definitively, record without rewriting S016 bytes, and make that the session's work (Lean work then waits).

## Milestone 2: local Lean environment aligned with the Palomar registry

1. Read the CURRENT public Palomar registry requirements (accepted Lean/toolchain versions, Mathlib pinning, project layout such as any formalization manifest, comparator/challenge conventions, forbidden axioms/`sorry`/`native_decide` rules, CI expectations). Record exact URLs, access timestamps and the requirement text you rely on (SOURCE catalogue entry; do not copy another project's manifest blindly — RELEASE_PROTOCOL step 5).
2. Install elan locally (official installer, user-level), then pin `lean-toolchain` to a Lean 4 release that BOTH the Palomar requirements accept AND a released Mathlib tag supports; pin Mathlib in `lakefile` and commit `lake-manifest.json`. Record `lean --version`, `lake --version`, the Mathlib commit, OS and disk/RAM. If the registry requirements and the latest stable Mathlib conflict, prefer the registry-accepted version and record the reason. If the requirements cannot be read, record UNVERIFIED and choose the most recent stable Lean/Mathlib pair, flagging it for re-alignment before any submission.
3. Use the Mathlib binary cache (`lake exe cache get`); never compile Mathlib from source unless the cache is unavailable (then record it). Verify the setup with a trivial module before real work.
4. Consider reuse of the earlier TreeStack Lean package (TreeStack/PebblingMove.lean, Stacking.lean) only after a licence, version and definition-equivalence audit; credit it if reused.

## Milestone 3: formalisation plan (written and hashed before substantive Lean work)

Target statements (definitions in separate model modules; a standalone Challenge file stating the theorems from the definitions only; Solution proofs separately):
- Model: finite simple graph on Fin n (G9 as an explicit decidable adjacency), configurations as Fin n -> Nat, the move relation, stackable (some reachable configuration has exactly one occupied vertex), clearable (reachable total mass exactly 1), AS, stack/clear thresholds as in research/ASH_SPEC.md (least t>=2 with every size-t configuration g-able), L_all/L_AS.
- Theorems: G9 STACK K1-K4 and CLEAR K1c-K4c, hence stack(G9)=clear(G9)=15 and the failure of the critical ASH* clause for each game exactly as stated in research/ASH_SPEC.md (critical form), plus the general lemmas used (monotonicity above n = October Lemma 4.7 / S003 Lemma 2; T1 clearable => stackable).
- Proof strategy must be chosen for KERNEL EFFICIENCY. Evaluate and record the trade-offs before committing to one: (a) a reflective checker proved sound in Lean and evaluated by `decide`/kernel reduction (no `native_decide` in certified theorems, AGENTS.md rule 9); (b) prefer the exact losing-layer recursion (candidate completeness C5 + termination C6) over replaying 490k winning sequences: the G9 losing layers total about 14k configurations, so verifying "Lose(15) is empty", "Lose(14) = {c*, image}" and the AS conditions through a verified layer checker is orders of magnitude cheaper than per-configuration certificates; (c) compact encodings (Nat-packed configurations, sorted arrays/RBSets with proved lemmas) and kernel-friendly recursion (well-founded recursion avoided in evaluated code; structural recursion on fuel). Benchmark a small instance (e.g. P4 stack 15, bull clear 15) before scaling to G9.
- Non-stackability of c* may alternatively be formalised from the human proof (S015 section 5 with S016 repairs R1-R3) — record whether this is attempted or left to the certificate.

## Lean build-efficiency discipline (binding for this and later sessions)

- **Freeze green modules.** One lemma group per module. When a module compiles with no `sorry`/`admit`/new axioms (checked by `#print axioms` on its main declarations), record it in a frozen-module ledger (formal/FROZEN_MODULES.md: module path, source sha256, toolchain, Mathlib commit, axioms printed, date, session). A frozen module is not edited; changes require a new module or an explicit un-freeze entry.
- **Build only what changed.** Use targeted `lake build <Module>` or `lake env lean <file>` for the module under work; do NOT run a full `lake build` after every edit. Frozen modules are rebuilt only when they are dependencies of the target being built (lake's incremental build handles this) and for the full final build.
- **Full builds are milestone events**: at most at the end of each major milestone and at closeout, each recorded with command, wall time, peak memory and result. Keep expensive kernel evaluations in their own modules so they are not re-elaborated by unrelated edits.
- Record every build failure honestly (FAILURE ledger); a failed build is not a result. No `sorry`, `admit`, unreviewed axioms or unexplained `native_decide` in anything called certified.

## Milestone 4: begin the formalisation

Implement as much of the plan as the session can carry: model definitions, the general lemmas, the verified checker, and then the G9 STACK and CLEAR statements, freezing each green module as it lands. Keep the Challenge statement faithful to research/ASH_SPEC.md and reviewable by a human; any mismatch between the Lean model and the paper's conventions (t>=2, exact layer versus at least, n=0/1 exclusions, bipartite exclusion for CLEAR) must be resolved explicitly and recorded.

## Closeout and handover

Close when context is genuinely running low or a natural boundary is reached, not at the first milestone. Before closing: run one full `lake build` of the formal project (recorded), the forbidden-placeholder scan and `#print axioms` for every completed theorem; update formal/README.md, formal/FROZEN_MODULES.md, state, spec, catalogues, decision/route/failure/session/gate/search ledgers, campaign registry and evidence manifests. One branch, one atomic authored session commit, ordinary PR, non-force merge if permitted; pin actual heads/trees/parents/hosted jobs/main after creation. Hosted CI should check the Lean project only if it can do so within reasonable time (use the Mathlib cache); otherwise record that Lean CI is local-only and UNVERIFIED on hosted runners. Prepare a complete FUTURE/UNEXECUTED S018 handoff that continues the formalisation exactly where it stopped (frozen modules, open goals, next module, measured build costs). Do not claim L_all(G) <= L_AS(G) anywhere beyond computed or proved scopes. Avoid model/vendor names in repository files.

## Computational discipline

Before any computation (including Lean kernel evaluations at scale) write and hash a bounded amendment: exact scope, caps, two independent validators where applicable, completeness and UNKNOWN policy, code/input/output hashes. Caps are UNKNOWN, never evidence. State the actual environment. Preserve all S003-S016 immutable manifests, failed attempts, protocol deviations and UNKNOWNs.
