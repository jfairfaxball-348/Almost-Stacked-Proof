# Failures, traps and lessons

| ID | Hazard | Response |
|---|---|---|
| FL-0001 | Treating a consequence of ASH as equivalent to ASH | Tree equality is independently settled by TreeStack; do not infer universal ASH |
| FL-0002 | Turning source abstract into an exact quantified hypothesis | Record ABSTRACT_INSPECTED until exact PDF theorem statement and numbering are read |
| FL-0003 | Missing a counterexample because a greedy solver reports failure | Require complete reachability or invariant/nonreachability certificate, not a particular move sequence |
| FL-0004 | Unjustified extrapolation from graph atlas n≤7 | Finite verification bounds are finite only; source's atlas is SOURCE_STATED |
| FL-0005 | Crossing stack/clear or bipartite boundaries | Track connected vs non-bipartite hypotheses and exact definition of cleared |
| FL-0006 | Assuming small-tree theorem or historical tree conjecture remains open | Preserve TreeStack public theorem arXiv:2609.31811 and exact Lean declaration |
| FL-0007 | Mistaking absent GitHub Actions runs for CI green | Inspect runs/jobs/check-runs/status contexts; record missing separately |
| FL-0008 | Granting Palomar or arXiv status before registration/submission | Owner gated and immutable public evidence required |
| FL-0009 | Arbitrary mass-preserving pile consolidation can change a losing state into a winning state | Explicit P4 c=(2,0,0,2) losing, (4,0,0,0) winning; loss-preserving *existential* ASH reduction still open |
| FL-0010 | Tree-only incident branches overlap around cycles, destroying independent root-task execution | P4 + edge 0-3 changes same c from losing to winning; cyclic correction required |
| FL-0011 | Confuse verified April Hypothesis 9.1 with unread October paper | Keep October ABSTRACT_INSPECTED, label April version, reopen October full-source gate in S003 |
| FL-0012 | Infer universal ASH from finite order-8 evidence or one solver | Complete cutoffs only, independent inverse-DP and BFS checks, no universal claim |
| FL-0013 | S002 labelled C8 + chord 0–4 "bipartite" by inspection; the chord closes a 5-cycle | Bipartiteness is now computed by BFS 2-colouring in every solver and asserted against the catalogue; exact stack=clear=23 recorded (S003 errata) |
| FL-0014 | Testing only the critical layer g(G)−1 (as the authors' atlas code and S002's framing did) cannot detect failures of the *printed* pointwise least-t hypothesis, because AS-stackability is not monotone in t | Check every t in (n, g(G)); distinguish printed (literal) ASH from the critical form ASH* in every claim (S003 Thm 4) |
| FL-0015 | Route B on the critical layer: same-mass pair transfers / even-pile merges between critical losers do not reach an AS loser in general | Smallest counterexample: the 5-cycle at t=7, loser (0,0,3,3,1); ASH* still holds there. Do not base an ASH* proof on critical-layer compression |
| FL-0016 | Explicit-state AS memo search blows up on long paths (P9 with estim 511 exceeded 300 s / 3 GiB) | Report such trees as incomplete; never extrapolate from completed sizes |
| FL-0017 | Treating a conditional theorem whose hypothesis is now known false as refuted | October §6 conclusions are "unsupported", not "false"; §4–5 conclusions survive under ASH* |

| FL-0018 | Mistaking a privately reported author acknowledgement for a posted correction, a validation of particular counterexample certificate files, or a universal proof | Record as SRC-0010 SOURCE_STATED with provenance and no raw email; require new paper version and independent S004 cold audit separately |
| FL-0019 | Misusing the bad-layer predecessor recurrence as an ASH* proof, or overlooking terminal no-move configurations | Include `c not goal` and the universal quantifier over all legal successors; for t<=n handle 0/1 terminal losers explicitly; demonstrate any proposed extremal structural theorem independently |

| FL-0020 | Selecting minimum critical support need not select AS; pair-direction loss is not interval-convex | P3 centre0 c=(0,3,3) critical loser, (0,4,2)/(0,2,4) winners, (0,5,1) loser; global square-extremal conjecture remains open |
| FL-0021 | Unrooted block thresholds/list do not determine union threshold | K3 with two K2 blocks arranged as same-vertex leaves gives11/13, as length2 tail gives16/22; rooted interfaces essential |
| FL-0022 | Nonzero additive/mod3 invariant cannot persist on a connected non-bipartite graph | both edge directions force3-torsion, odd cycle also2-torsion, hencezero; weight-loss budget plus chronology needed |
| FL-0023 | Nonnegative integer firing balance does not ensure a legal schedule | terminal K3 (1,1,1) balances formally to e2 by a two-cycle but cannot move |
| FL-0024 | Sparse candidate explosion or mass cutoff is not an exact threshold | C10 completed only through16; triangle-tail clear>140; no ASH* verdict for these cases |
