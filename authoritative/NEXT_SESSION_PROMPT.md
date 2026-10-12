# S004 — Independent cold audit of the printed-ASH counterexamples, Phase 1 gate decision, and the critical-form ASH* attack (FUTURE, UNEXECUTED IN S003)

**This is a complete future handoff only. It is NOT permission to execute during S003.** One fresh, explicit owner invocation is required.

Execute ONE serious session in https://github.com/jfairfaxball-348/Almost-Stacked-Proof. Do not execute S005, contact the authors or anyone else, start Lean or Palomar, submit anywhere, or write solved claims beyond audited evidence.

## Where S003 left the programme
The printed hypothesis (October 2610.09650v1 Hypothesis 3.2 = April 2604.22341v1 Hypothesis 9.1: "g(G) is the least t≥2 such that every almost-stacked configuration of exact size t is g-able") was refuted by S003 with finite certificates:
- **stack:** P4 (0-1-2-3) at t=12 — all 32 AS configurations stackable, (1,0,2,9) not, stack(P4)=15;
- **clear:** the bull graph (edges 0-4, 1-3, 2-3, 2-4, 3-4) at t=12 — all 80 AS configurations clearable, (1,9,0,2,0) not, clear=15.

S003 also established:
- The AS-gap reformulation (S003 Thm 4) and the observation that the authors' public atlas code (`lajossoukup/pebbling@701cdd93`) tests the **critical form ASH\***: an AS configuration attains the largest non-g-able size, i.e. one exists at size g(G)−1.
- ASH\* is OPEN. It is true for:
  - all trees (TreeStack theorem plus October Thm 5.2);
  - every graph with g(G)=n+1;
  - every connected graph with n≤7 whose threshold S003 found (independent replication);
  - the selected n=8–10 graphs computed.
- Critical-layer compression is refuted as a proof route (5-cycle, t=7).

Read: `research/S003_AS_GAP_AND_ATTACKS.md`, `research/S003_SOURCE_RECONCILIATION.md`, `research/ASH_SPEC.md/.json`, `evidence/S003/*`, `sessions/S003/*`, and all ledgers and catalogues.

## Entry (mandatory)
1. Independently fetch LIVE remote main. Pin from GitHub, never from closeout strings:
   - S003's actual session commit, its parent and tree, the S003 PR and its non-force merge commit;
   - post-merge main and its parents.
2. Reconcile any other commits, PRs and branches.
3. Audit workflow definitions and real Actions runs/jobs/check-runs on the S003 PR head and post-merge main. Since S003, the workflow also replays the certificates. Absent checks are not a PASS.
4. Check arXiv for any new version of 2610.09650 (or 2604.22341). If the printed hypothesis changed, transcribe the new wording exactly and reconcile every S003 statement against it before any gate decision.
5. Archive the owner invocation, without inventing a hash. Preregister the S004 plan and budget, and hash the plan before computation.

## Task 1 — Independent cold audit (gate-critical)
Without reading S003's solver or checker source first, write a fresh minimal checker (different language or different algorithm; e.g. explicit reachable-set enumeration with a different state encoding, or a SAT/ILP-free exhaustive search). Use it to re-verify:
- (a) every AS configuration of size 12 on P4 is stackable, and (1,0,2,9) is not;
- (b) the same for the bull graph, for clearing and for stacking;
- (c) stack(P4)=15 and clear(bull)=15 exactly — not needed for the refutation, but recorded;
- (d) minimality:
  - no connected graph with ≤3 vertices fails the printed form;
  - among 4-vertex graphs only P4 fails (stack);
  - no non-bipartite graph with ≤4 vertices fails clear.

Re-derive by hand, and cold-check, the proofs of S003 Lemma 1, Lemma 2 (October Lemma 4.7), Proposition 3, Theorem 4 and Corollary 5. Pay attention to: n=1 and n=2, t≥2, exact versus at-least sizes, and that stack is defined only for connected graphs and clear only for non-bipartite ones. Also re-read S003's quantifier transcription against the PDF text.

Record the outcome in a new audit file. Only then decide the Phase 1 gate for the **printed form** explicitly (PASS / FAIL / PARTIAL), with scope wording that distinguishes the printed form from ASH\*. Lean remains Phase 3. If the audit finds any defect, fix it or downgrade claims everywhere (catalogues, STATE, ASH_SPEC, README).

## Task 2 — Critical form ASH\* (proof-first, separately for stack and clear)
Aim for an unconditional proof, or a fully certified counterexample, of ASH\*. Suggested routes, each with explicit falsification gates and smallest counterexamples for failed lemmas:
- (A) Global obstruction certificates. Generalise the mod-3 weight argument of October Thm 5.2 and April Lemma 2.5 to graphs with cycles (spanning-tree weights with cycle corrections). Look for an extremal non-g-able configuration that can be chosen AS. Do not compress within the critical layer (FL-0015).
- (B) Block/bridge and pendant-tree decomposition: graphs = blocks + trees; trees are settled.
- (C) Cycles: ASH\*(C₂ₙ) ⇔ stack(C₂ₙ)=2^{n+1}−1 together with an AS loser of size 2^{n+1}−2. Identify whether April Corollary 7.5's witness is AS.
- (D) Bounded exact search for ASH\* counterexamples where g(G) is computable but large (sparse n=8 graphs beyond the S003 cap; selected n=9/10 unicyclic/bicyclic graphs). Use symmetry reduction only with a written orbit argument, and two independent exact solvers. Any candidate needs labeled adjacency, exact g(G), all AS configurations at g(G)−1 certified g-able (replayable sequences), and one general loser certified at g(G)−1 by two independent checkers. Otherwise CANDIDATE ONLY.

Optional, if time remains: attempt a proof of CLM-0024 — for every n≥4, every AS configuration of size 2ⁿ−4 on P_n is stackable, giving an infinite printed-form family.

## Stage-2 boundary
If and only if Task 1 records a Phase 1 PASS for the printed form in this session, S004 may begin a bounded **first novelty check** (Phase 2) for that exact counterexample:
- timestamped primary-source queries;
- citations of 2610.09650 and any errata or new versions;
- equivalent formulations;
- the closest prior statements.

There is no worldwide-priority claim and no contact. Otherwise leave Phase 2 NOT_STARTED. Notifying the authors is owner-gated; record it as a possible owner decision only.

## Exit
- Write S004 INPUT, plan (with hash), audit report, ASH\* research report, and machine-readable records with hashes.
- Update ASH_SPEC and its JSON, the catalogues and JSON mirrors, all ledgers, STATE, the validator, and the closeout.
- Write ONE complete strictly FUTURE S005 handoff.
- State explicitly:
  - printed-form status (stack, clear);
  - ASH\* status (stack, clear);
  - audit outcome;
  - source access level;
  - the first remaining obstruction;
  - the Phase 1 decision.
- One atomic authored session commit, an ordinary PR, a non-force merge. Independently verify post-merge main and the hosted checks. STOP; do not execute S005.
