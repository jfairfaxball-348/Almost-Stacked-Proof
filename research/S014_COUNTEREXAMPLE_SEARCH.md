# S014 ACTIVE: continued universal counterexample attack through CAM45

The universal target is still L_all(G)<=L_AS(G), with complete original
input consumption and unrestricted terminal root. No proof or counterexample
of that implication has been found. S014 remains open by owner instruction.

CAM33 completes120 exact comparisons on the prescribed circulants n11..14;
all unrestricted thresholds match largest AS mass+1. CAM34 checks7510 fixed
lifts of actual losing configurations:7261 original winners and249 losers
with an AS loser at at least the same mass, no unknown/potential. CAM35
refutes the proposed singleton-to-two monotonicity with90 old full-table
failures; do not use it in the no-two question. CAM36 completes120 greedy
edge saturations and literal missing-edge winning traces, all checked. A
noncritical seed's saturation is not a critical-threshold certificate.

## Fixed inputs, all graph edges variable

CAM37's native SAT variables are ALL unordered graph edges. Lazy connectivity
cuts are necessary for every connected graph. A complete c-winning literal
history forces at least one of its used edges absent in a countermodel. A
certified AS loser d on a supergraph H forces at least one edge outside H:
otherwise d would remain losing. Each clause is therefore necessary for a
connected graph on which c loses and ALL AS inputs of mass>=|c| win.90 makes
that tail exactly testable at three layers. This is actual move reachability,
not a balance relaxation or mere failure to find a history.

CAM38 adds clause images under permutations fixing c, independently expanding
every recorded base/permutation pair. It does not quotient graphs or assume
unproved symmetry. CAM41 uses a smaller explicit valid permutation family.
CAM43 strengthens C10's imported negative clauses by minimizing their real
winning supports and retaining independently replayed literal histories.

The following fixed inputs are excluded across ALL connected labeled graphs
of their displayed orders, hence also after simultaneous relabeling of input
and graph:

| Case | c | Exact accepted proof |
|---|---|---|
| C6 | (3,3,1,1,0,0) | CAM37/38 full RUP plus CAM45 independent hinted replay |
| C9a | (3,3,1,1,0,0,1,1,1) | CAM42 full smaller-core RUP and CAM45 original-formula hinted replay |
| C9b | (3,3,3,1,1,1,0,0,0) | CAM45 original-formula hinted replay |
| E8 | (2,2,1,1,1,1,1,1) | CAM42 full RUP replay |
| M9 | (2,3,1,1,1,1,1,0,0) | CAM42 full RUP replay |

For each such c, if c loses then there EXISTS an AS loser with mass>=|c|.
This does not assert c is never critical; a critical c can coexist with an AS
critical loser. It does not cover arbitrary c, order or graph classes with
unbounded binary buffers. No universal ASH* inference follows.

The final accepted proof chain has literal graph certificate replay,
independent clause/permutation necessity, a native refutation as untrusted
certificate producer, and a separate Python verification of every retained
RUP addition ending in empty. CAM45's native LRAT conversion supplies only
clause-id hints; Python checks the actual unit implications, deletions and
fresh identifiers against the exact frozen original CNF. Native VERIFIED is
not the sole evidence. The official DRAT-trim documentation/CLI has stable
SRC0060 attribution. This is computational certification, without claiming a
formal kernel or independent human audit.

Preserve all earlier bounded failures: original CAM38 C9a was explicitly
interrupted after its oversized stdout blocked the pipe; separate v2 keeps
compact output. The original/simple whole-formula proof scans, occurrence
checker39 and core scans40 hit fixed limits on some proofs. CAM42's C9b core
proof also hit500000000 watched visits. Those ATTEMPTS remain UNKNOWN even
though a different complete proof now certifies their original input class.
CAM40 C10's500000-clause partial formula is SAT, not a counterexample: the
remaining reachability/AS conditions were not all met. CAM43 then imported
minimized traces and learned1000 further clauses; its class remains UNKNOWN.
E9,E10,M10,F9,T10,T12 likewise remain UNKNOWN after1000 CAM41 iterations.

## Universal proof follow-through

90 supplies the exact three-layer AS tail,92 supplies a simultaneous extremal
graph/input normal form, and93 supplies actual EVERY-root neutral count
certificates at bipartite criticality. CAM44 checks638 already independently
certified full critical sets,20231 inputs and17940 non-AS inputs. None of
those non-AS inputs has a pile2; their only four even-heavy inputs are
nonbipartite. Universal no-two and bipartite odd-heavy assertions remain
unproved. A proposed hub/branch obstruction has not been proved critical and
is not a disproof of either assertion. H2r remains a sufficient unproved
induction toward the actual universal comparison, including nonadjacent
heavy sites, arbitrary buffers, changed roots and even/non-triplet donors.

Continue in S014. No authored commit, PR, merge, closeout, S015 handoff, Lean,
phase/novelty promotion, registration, publication or correspondence occurred.

CURRENT S014 ACTIVE through CAM50: proofs71-99 at exact scopes. Fixed-input F9/E9 graph classes now independently excluded, joining C6/C9a/C9b/E8/M9; other fixed-input caps remain UNKNOWN. CAM48 all five ALL-pattern fixed(n,M) searches ended at caps UNKNOWN; inventory/formula/certificate verification PASS is not exclusion. CAM49 refutes generic even-pair extension; CAM50 independently certifies P4 d=(9,0,0,3), mass12, ALL positive coordinate extensions win, actual every-root neutral histories, minimum-heavy/global-Q/P properties, but L_all=L_AS14. Thus even these joint local properties cannot replace global largest losing mass. H2r/no-two/bipartite odd-heavy UNPROVED. CAM51 fair-selector control PASS, real cases NOT_YET_EXECUTED at this checkpoint. Universal STACK/CLEAR OPEN; CLEAR deferred. Continue until proof/counterexample; no closeout/commit/PR/S015.

CURRENT S014 ACTIVE through CAM55, local items71-103. All six CAM51 fair all-pattern real cases capped UNKNOWN, no full exclusion/counterexample.100 exact bipartite one-bit conductors retains earlier April7.3 path/zero-imbalance credit.101 proves the universal bridge for EVERY losing input supported on an isometric subtree of a bipartite graph, using the EARLIER TreeStack theorem.102 crowns Cr_k(k>=5) refute stronger universal tree-support selection.103/CAM54-55 refute the combined n/independence/isometric-tree ceiling: actual bipartite A182 threshold42>bound40, with AS critical loser(39,1,0,0,0,1,0,0), fresh10988-state complete negative closure and independent full threshold42/AS maximum41. These are auxiliary shortcut failures, not ASH*. H2r/no-two/bipartite odd-heavy remain UNPROVED. Universal STACK/CLEAR OPEN; CLEAR deferred. Continue proof/counterexample work, no closeout/commit/PR/S015.

CURRENT S014 ACTIVE through CAM62/local items71-108. CAM56 independently excludes ALL32 sorted non-AS order8/mass10 input classes across all connected graphs; finite only.104 covers all triple-median supports with arbitrary coefficients, including <=3 occupied sites on Q4. CAM57 forward AS-tail cap remains UNKNOWN; CAM58 v2 checks ALL1572864 attaining nodes/98304 upper queries and CAM59 ALL803538796 lower inequalities, exact Q4 L_AS30 and exact whole-AS oracle.58 original checker negative-shift failure preserved/repaired separately. CAM60/61 capped general prefixes remain UNKNOWN; CAM62 exact XOR quotient verifies ALL9783 fixed general inputs at31/32/33 as winners,872261 states, no potential. These samples do NOT prove full Q4/universal threshold. CAM63 compiled untrusted producer and independent complete controls Q1=3/Q3=15 PASS; full Q4 layers1..31 NOT_YET_EXECUTED at this checkpoint. Universal STACK/CLEAR OPEN; CLEAR deferred. Continue, no closeout/commit/PR/S015/later-phase action.

CURRENT S014 ACTIVE through CAM63. Full compiled/Python Q4 orbit layers1..13 independently agree; mass14 reaches its2M candidate cap, general threshold UNKNOWN. Earlier exact Q4 AS max30, whole-AS oracle and9783 verified general winners retained at their exact scopes. Source-integrity recovery: CAM56 filename collision with frozen CAM06 checker detected by failed scope62 validation; original CAM06 bytes recovered to exact73a042ac... digest from its original tool record, CAM56 byte-identical de2b450e... checker archived under distinct mass-split name. All33 independent replays preserve output bytes; old preflights/logs remain unchanged, exact path/digest archive alias reconciles provenance. Never rerun historical CAM56 split_generate/prepare/run scripts that name the old path; use mass_split_replay for existing data. No mathematical claim changed by this repair. Universal STACK/CLEAR OPEN; continue research, no closeout/commit/PR/S015/phase advance.

CURRENT S014 ACTIVE throughCAM67/local items71-109. Independent COMPLETE losing layers establish Q4 stack31=L_AS30+1 and FanoInc14 stack30=L_AS29+1; every critical loser in each is AS. Symbolic109 gives universal bipartite distance-shell AS lower witnesses with actual all-edge truncated valuation/all-root full-history proof. CAM67 checks501 shell instances,106 exact-AS oracle comparisons and350 fresh complete negative closures/22920 states. Original65 producer-width failure and separate passing repair preserved, all older caps/failures unchanged. Universal SAME-GRAPH STACK comparison OPEN; CLEAR deferred. Continue, no closeout/commit/PR/S015/later phase.

CURRENT S014 ACTIVE throughCAM71/local items71-110. CAM68 independently excludes ALL44 non-AS order8 mass11 patterns across all connected graphs,64781 RUP additions/1461399 hints. CAM71 independently excludes8 specified multiheavy classes at masses16/18/20 on orders8/9, with no cap or potential. CAM69/70 refute unconditional mass-slack elimination/pooling at precise below-critical five-vertex inputs: original heavy receivers fail12 complete candidates; arbitrary receivers/two donors fail60. Remaining respective12/9 graph cases UNEXECUTED after decisive auxiliary failures. Critical H2r and universal SAME-GRAPH STACK remain OPEN; full buffer/actual criticality cannot be dropped. Symbolic110 gives Q5 AS lower66 and stack>=67, invalidating cube diameter/product doubling shortcuts; no exact Q5 threshold or ASH* failure. All earlier exact/capped scopes preserved. Continue S014, no closeout/commit/PR/S015/later phase; CLEAR deferred.

CURRENT S014 ACTIVE through completedCAM76/registeredCAM77/local proofs71-115.111 gives exact whole-input subcubic boundary trees;112 canonical unique parity markers;113 exact STACK iff THREE(c) or some THREE(c+2e_q);114 actual losing mass ascent at even heavy sites adjacent to graph leaves.75 independently checks33188 extensions including3104 empty leaves.76 refutes unrestricted some-neighbor ascent below criticality with515 failures; critical bipartite oddness remains UNPROVED.72 checks14814 non-AS bipartite critical inputs/203673 parity candidates.73 plus74 support only finite B_odd:13297 small plus1598711 larger inputs,18 larger completed cases through order14 and3 prior-size UNKNOWN cases A171/A181/A184.115 exactly reduces pair-fuel2 THREE to a marker path, general STACK additionally to a three-arm tree; old independence witness already dominates all such bipartite inputs for n>=8.77 is a registered fixed-pattern search, no result inferred. Universal SAME-GRAPH STACK OPEN; CLEAR deferred. Continue S014, no closeout/commit/PR/S015/Lean/phase/contact.

CURRENT S014 ACTIVE completedCAM1-76,78-80;77 still in progress,81 registered UNEXECUTED. Local proofs71-121.116/118 prove any prescribed heavy source has a winning first move from any multioccupied STACK winner, independently by tree normalization and elementary history interchange.117 proves graph-leaf safe firing except pure3 and all critical neighbors of graph leaves zero for n>=3.119 proves odd-leaf/positive-parent boundary contraction, with exact STACK equivalence when parent>=2.120 proves ANY even-heavy graph-leaf loser remains losing after +3 at that leaf; hence critical graph-leaf counts are zero or odd, ALL graphs.78 passes160579 inverse extensions;79 independently checks598867 predecessors/437350 multioccupied winners/1211093 heavy sources/2538712 child memberships;80 passes54686 each of both odd-leaf contraction directions and even-leaf +3 extensions.121 explicitly refutes generic jump-system/M-convex exchange of the all-odd THREE language on P3 by mod3 charge; this is NOT a STACK/ASH* counterexample. Core even-heavy/global arbitrary-buffer bridge remains UNPROVED. Universal SAME-GRAPH STACK OPEN; CLEAR deferred. Continue S014, no closeout/commit/PR/S015/Lean/phase/contact.

CURRENT S014 ACTIVE through completed/registeredCAM81, local proofs71-121. CAM77 independently excludes ONLY full-buffer two-pile3 order8/mass12 class F8 (1365 RUP additions/40162 hints); order9/10 iteration caps and order12 time cap remain UNKNOWN. CAM81 all30 fixed graphs through order5, bipartite filter,2490 mod3-residue groups/57060 memberships/560 nontrivial pair-source exchange checks complete with no failure; rescaled-sector M-convexity remains UNPROVED globally.116/118 prescribed-source theorem,117 critical graph-leaf neighbor zeros,119 odd-leaf contraction and120 even-leaf +3 ascent/critical leaf oddness remain complete scoped proofs with finite independent challenges78-80.121 refutes direct unit exchange of THREE by charge, not rescaled exchange or ASH*. Universal SAME-GRAPH STACK comparison OPEN; arbitrary buffers/graph cores remain. Continue S014; no closeout/commit/PR/S015/Lean/phase/contact, CLEAR deferred.

## Final S014 authority - owner-requested closeout, 2026-10-16

The owner's later explicit request, `Can you commit and close out this session`, supersedes all earlier S014 keep-going/no-closeout instructions in this file. Those earlier checkpoint paragraphs are historical. S014 is COMPLETED at the administrative session boundary; universal critical STACK and CLEAR remain OPEN. Phase1 remains IN_PROGRESS; phases2-6, Lean, registration, publication and contact are unchanged and unexecuted. S015 is strictly FUTURE, UNEXECUTED; its complete prompt is sessions/S014/FUTURE_S015.md and authoritative/NEXT_SESSION_PROMPT.md.

S014 preserves 81 preregistered bounded campaigns and local proof items71-121, at their exact scopes and LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING assurance. Main advances include arbitrary-buffer join-class ASH*, exact Q4 stack31/L_AS30 and FanoInc14 stack30/L_AS29, subcubic boundary-tree and unique-marker characterizations, prescribed-heavy-source first-move existence, safe graph-leaf firing, odd-leaf contraction and critical leaf/neighbor restrictions. None proves universal SAME-GRAPH L_all(G)<=L_AS(G). Earlier TreeStack is credited prior work. Direct unit exchange is false; rescaled-sector exchange, H2r, critical core oddness and arbitrary-buffer domination remain unproved. All caps, prior-scope UNKNOWNs, unexecuted suffixes, mathematical failures and separate repairs remain archived. CAM77 excludes only F8; F9/F10/F12 remain UNKNOWN. See CLOSEOUT for the exact final synthesis.

Final governance/provenance validation and immutable hashes are required before the one atomic authored commit, ordinary PR and non-force two-parent merge. Actual outgoing head/tree/parents, hosted jobs and final main are verified after creation and recorded in PR metadata, without circular self-SHA claims in this commit. Administrative memory failures are retained separately under evidence/S014/admin_recovery; no resource failure becomes a mathematical conclusion.
