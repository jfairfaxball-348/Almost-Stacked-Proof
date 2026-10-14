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
| FL-0025 | Distance-only two-site AS stacking witness ignores cyclic residue adjustments | Triangle1-2-4 tail4-3-0 stacks(1,13,0,0,0); independent legal trace, 506 bounded pair tests. Auxiliary failure, not ASH*. |
| FL-0026 | Deleting an odd leaf with negative boundary score can reject a legal clearing state | Path(1,0,4) clears; retain deferred debt and schedule, not nonnegative-only normalization. |
| FL-0027 | Erasing directed move cycles may destroy exact consumption and final singleton support | K3 pure6 clears but no acyclic balance certificate; cyclic grammar essential. |
| FL-0028 | Treating a pure pile as a stacking obstruction, or the rooted odd-walk lower bound as new | Pure pile is already stacked; April Thm6.1 lower bound and October4.10 already known. Exact classification has no priority claim. |
| FL-0029 | Three-pebble monotonicity alone cannot force AS extreme holes | Fixed support/residue lower sets need cross-class graph constraints; general lower sets can have interior degree maxima. |
| FL-0030 | Interrupted scratch producer outputs are not complete certificate pairs | Continuation reruns invalid/unfinished jobs; preserve valid pairs, exclude orphan raw files and empty summaries. |
| FL-0031 | C8 plus a leaf remains bipartite; named both-goals plan overlooked clearing eligibility | Correct before its run: treat clear as bounded reachability sanity check only, never clear threshold or ASH* verdict; exclude from eligible counts. |

| FL-0032 | Unrooted clearing does not supply a prescribed final boundary vertex | K3 pure5 clears somewhere but cannot finish at its source; exact rooted residue minima required. |
| FL-0033 | Scalar leaf net plus unrooted core clearing loses legal credit/target and can fail in both directions | Triangle-leaf (0,1,0,3) false positive, (0,0,4,1) false negative; use exact tree/forest input-dependent interface. |
| FL-0034 | Zero source count is not the positive residue0 class and +3 cannot be applied to an empty site | Keep a distinct zero-source bit in every buffer grammar and validator. |
| FL-0035 | Exact AS-ray conductor computation or coarse global finiteness is not ASH* | Prove general-versus-binary maximum-mass domination separately. |
| FL-0036 | Windows CRLF checkout changes bytes of hashed historical evidence | Enforce canonical LF text and binary exclusions; verify manifests on committed bytes. |

| FL-0037 | Entire greedy production can spend extra mass in unused residual histories beyond selected K-2 | Extract and replay only two disjoint selected ancestry trees; final S007 proof/producer agree |
| FL-0038 | A scalar move-monotone weight dual cannot separate all exact-clearing losers | K3 pure3 exact three-state closure; richer chronology/residue certificates needed |
| FL-0039 | New symbolic threshold does not complete an old truncated certificate | S007 proves triangle-tail6 clear382, old S005 certificate still stops at47 |
| FL-0040 | Triangle-tail stacking upper does not imply exact formula or ASH*-stack | S007 <=4*2^l; matching AS lower remains future |

| FL-0041 | A binary-buffer lower dual or a finite-complement ideal does not establish arbitrary-buffer upper domination | S00834 solves one buffer; abstract (X^3,Y^3) axis inference fails, with no graph counterexample inferred |
| FL-0042 | Simultaneous U=c(s)+3 tightness is necessary for largest losers, not a sufficient global threshold certificate | Keep exact threshold/critical AS layer verification separate |
| FL-0043 | Theorem33 cannot extend sharp odd-bound clearing to arbitrary simultaneous branches | F_k clear3k+7 exceeds odd-walk10 and independence3k+4 for k>=2; separate weight/credit proof needed |
| FL-0044 | Historical manifests also hash mutable mirrors in S007 | Freeze21 pinned S007 byte snapshots and explicitly remap only these paths; never rewrite old digests |
| FL-0045 | PowerShell/Python nested quote escaping can truncate a code-generation command | Initial provenance-copy command failed before creating any script; replaced by literal here-string, no mathematical result affected |


Closeout administrative correction: implicit Windows cp1252 reads failed on UTF-8 text, interrupting CLM-0068 Markdown update and check-log collection. Governance failed closed on the missing claim mirror. Explicit UTF-8 reads/output capture repaired both; mathematical checks had passed, failures retained in evidence/S008/administrative_failures.json.

| FL-0046 | Calling exact ancestry/token values new ignores direct April4.3/Sjostrand precedents | S009 per-result primary table separates known theorem/mechanism from possible new consequences |
| FL-0047 | Ordinary target/cover/no-cycle/lex results allow leftovers and fixed demands | Preserve exact consuming labels, all root minima, zero support and forest reconstruction |
| FL-0048 | Rootwise conductor domination is stronger and false | K3 pure5 fails root0 while clearing elsewhere; rooted minimum8/last5 versus unrooted AS maximum3 |
| FL-0049 | Three removed inputs assumed to damage at most two stack components | Explicit labeled critical P3 extension has three affected final trees; arbitrary-length frontiers require full reconstruction |
| FL-0050 | Protecting an odd-path credit export before completing its launch can make the construction illegal | Retained producer failure; protect completed path-return output or even export; independent full traces then PASS |
| FL-0051 | A first-return port hole treated as free or a standalone boundary base | Least nonempty substitution, even holes and actual e_a input separately; complete318-case challenge |
| FL-0052 | Pre-registration labels accidentally overlap source or fail universal-port assumption | Both corrected/rehashed before computation, initial text/digests retained; no scope expansion |
