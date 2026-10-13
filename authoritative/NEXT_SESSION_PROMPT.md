# S004 — Cold-audit the printed form, then attack the **intended universal ASH*** via losing-layer structure

**FUTURE, UNEXECUTED.** This update was prepared outside any numbered research session after author correspondence on 2026-10-13. Execute **exactly one** S004 on a **fresh explicit owner invocation**. No S005 execution, unsolicited author contact, Lean, Palomar, arXiv submission or publication.

Repository: https://github.com/jfairfaxball-348/Almost-Stacked-Proof

## Headline objective — solve the intended conjecture, not just a printed-form discrepancy

The authors' 2026-10-13 message (recipient-supplied summary in `outreach/2026-10-csernak-soukup/2026-10-13_AUTHOR_REPLY.md`) **explicitly confirms** that their intended hypothesis is **ASH***: the largest losing (non-stackable or non-clearable) size has an **almost-stacked losing witness**. The **stronger pointwise 'least exact t' hypothesis as printed** is false; the author acknowledges the wording is too strong. This is a report of their intent, not a revised arXiv text nor an independent proof.

Formulate ASH* precisely: for every finite connected simple `G` with `|V|>=2`, some almost-stacked configuration of size `stack(G)-1` is not stackable; separately for connected non-bipartite `G`, some almost-stacked configuration of size `clear(G)-1` is not clearable. By S003 Thm 4 it is equivalent to the monotone **all t>=t0** formulation. K1 must be treated separately. Do **not** replace this with the already refuted printed statement or an already proved tree theorem.

**Mathematical ambition:** attempt the full proof or a fully certified counterexample in this session. Allocate serious effort to multiple genuinely competing approaches, pursue an actual theorem rather than merely listing lemmas, and record failed proof routes with smallest valid counterexamples. Do not overstate progress.

## Entry and authoritative evidence

1. Pin LIVE remote main commit, parent(s), tree, recent PRs and branch activity; independently verify S003 PR#3 and correspondence PR#4, and reconcile every intervening commit or competing S004 branch. Inspect accessible Actions workflow/runs/jobs/status/check-runs and branch rules. CI ABSENT != PASS; inaccessible protection = UNKNOWN. One branch, atomic commit, normal PR, non-force merge, independent main re-pin.
2. Read `AGENTS.md`, `authoritative/START_HERE.md`, `STATE.json`, `docs/SESSION_PROTOCOL.md`, `PHASE_GATE_LEDGER.md`, ledgers, claim/source registers, `research/S003_AS_GAP_AND_ATTACKS.md`, `S003_SOURCE_RECONCILIATION.md`, `ASH_SPEC.md/.json`, `ASHSTAR_ATTACK_BRIEF.md`, `evidence/S003/*`, S003 closeout, and the full correspondence summary. Note the owner says the initial email was sent, but the exact outgoing headers/time are **not independently verified**. S004 has not been executed by the 2026-10-13 admin update.
3. Recheck the *current* October and April arXiv version lists, actual PDFs and any errata/author corrections; if text changed, cite exact version and reconcile. The author email is **SRC-0010 / SOURCE_STATED**, not an arXiv erratum. Their report of complete n<=7 threshold computations is author-reported; our own n=7 845/853 stack and 806/809 clear cases below t<=55 are independent and bounded.
4. Archive the actual owner S004 invocation as received (or explicitly label a summary when exact text unavailable). Preregister full S004 plan before mathematics/compute: proof goals, independent falsification checks, precise finite-search cutoffs, resource budget, data/code hashes and rollback criteria. Hash the preregistration.

## Task 1 — Gate-critical independent **cold audit** of the printed counterexamples

Without first reading or copying S003 solver/checker source, implement a different minimal independent checker or mathematically distinct certificate verification; use it to verify:
- P4 (0-1-2-3): exactly **32** AS configurations at t=12 and every one stackable; (1,0,2,9) has a complete closed, goal-free reachable set; true stack(P4)=15.
- Bull graph edges (0,4),(1,3),(2,3),(2,4),(3,4): exactly **80** AS configurations at t=12, all clearable (and all stackable); (1,9,0,2,0) has a closed, goal-free reachable set; true clear(bull)=15. Check non-bipartiteness and vertex renamings.
- Check pointwise minimality of a printed-form failure among graph orders <=3 and <=4 where relevant, and check boundary n=1,2, exact masses, thresholds and trivial goals.
- Re-derive S003 Lemmas 1,2, Proposition 3, Theorem 4, Corollary 5 and original source quantifiers. Compare original file hashes with fresh results.
- State the **Phase 1 decision for the printed-form result alone** (PASS/PARTIAL/FAIL with evidence); **ASH*** remains OPEN unless separately proved or refuted. Lean is Phase 3; no phase promotion by inference. If defect found, downgrade all mirrors and explain it.

## Task 2 — Serious proof-first universal **ASH*** attack, both goals separately

Begin from the author's algorithmic observation, made precise **as a definition-level recurrence**. For goal g, let `B_t(G)` be all losing configurations of exact mass t, `AS_t` the almost-stacked ones, and `M(c)` all one-move successors. At mass t>=2:

`c ∈ B_t  iff  c is not already a goal and M(c) ⊆ B_(t−1)`.

When t>|V| every configuration has a move (connected nontrivial graph). Non-moving 0/1 states at lower masses must be handled. ASH* is `B_(g(G)-1) ∩ AS_(g(G)-1) ≠ ∅`. The recurrence **does not itself prove** this, and membership of AS losers need not be monotone.

Pursue at least these **competing routes**, dropping a route only after an explicit mathematical obstruction or meaningful experiment:

**A. Last-layer inverse-shadow extremal theorem.** Select an extremal losing configuration at critical mass by a rigorously chosen potential/support/heavy-pile statistic and ask why an AS representative must exist. Try a minimal bad-layer obstruction or injection argument; verify necessity, not just sufficiency. **Do not** assume all losers can be compressed within the critical layer: C5, t=7 refutes this specific route (FL-0015).

**B. Graph-structural reduction.** Attempt to exclude a minimal counterexample with cut-vertices/bridges or establish transfer rules for block sums/cactus/unicyclic graphs. Trees are settled (TreeStack + source Thm 5.2) and not a new headline. Edge addition can change winners, so prove each reduction.

**C. Necessary global obstruction certificates.** Try mod-3 parity/weight arguments, cycle-corrected rooted potentials, dual-set descriptions, invariants that can certify critical bad configurations; check the legal-move inequality in both stack and clear formulations. Identify exact point where a sufficient condition is falsely treated as necessary.

**D. Direct contradiction from no AS critical loser.** Assume every AS configuration at g−1 wins but at least one general loser exists. Using exact loss recurrence derive a forbidden combinatorial configuration, threshold contradiction, or infinite descent. Check `n>=2`, non-bipartite clear, and special goal states explicitly. If a candidate structural lemma is false, provide a *smallest checked* counterexample.

**E. Bounded exact attack** only after a written, hashed plan. Prioritise S003 n=7 uncovered 8 stack/3 clear threshold cases and selected sparse n=8+ hard cases. Two **independent** complete algorithms and certificate replay are required. A genuine ASH* counterexample must specify graph adjacency; exact threshold `g(G)`; a losing general configuration at mass `g−1` with closed reachable-set certificate; and a legal winning sequence for *every* almost-stacked configuration at that mass, with independent checkers. No result for undetermined thresholds.

Plan freely allows a major universal proof or definitive counterexample to displace subordinate tasks after recording why. Preserve the source statements, proof gaps, failed assumptions, machine evidence and completeness scope. Optional infinite non-tree family only if it advances the universal target substantially.

## Phase / outside-contact boundaries

The earlier printed formulation being false does **not** settle ASH*. If Task 1 yields a documented Phase 1 PASS for the printed result, a bounded preliminary Phase 2 novelty inspection **of that exact printed counterexample only** may begin; it must not be labelled a novelty review of a universal ASH* theorem not yet obtained. No formalisation until the appropriate stage and authority. No emailing the authors, proposed collaboration, erratum submission, Palomar, or arXiv action in S004 without a separate explicit owner instruction.

## S004 exit — required

Write `sessions/S004/INPUT.md`, preregistered `PLAN.md` (+ hashes), cold `AUDIT.md`, substantial `research/S004_ASHSTAR_ATTACK.md`, any experiments/code/certificates and hashes, truthful `CLOSEOUT.md`, mirror updates (STATE, decision/gate/session/failure/source/claim ledgers, machine JSON, ASH_SPEC, README, validator), and **one ambitious, complete, strictly FUTURE S005 handoff**. Clearly state printed stack/clear status, ASH* stack/clear status, full audit result, source access, phase decision, first unsolved obstruction, what was disproved, and evidence level.

One atomic authored S004 commit on a fresh branch, ordinary PR, non-force merge, verify final live main and actual hosted checks. **STOP before executing S005.**
