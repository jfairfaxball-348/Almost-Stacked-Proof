# Registered mathematical campaigns

**No active campaign in S001.** R-E in research/ROUTES.md is a *proposal*, not an authorised computation.

Proposals must specify: CAM identifier, theorem statement, graph model and atlas source, graph-size and pebble-mass range, enumerator and completeness proof, isomorphism/canonical-labelling assumptions, legal-move state solver, genuinely independent verifier, log/raw data location, expected hash and stopping rule. Search output cannot be promoted to a certified counterexample until exact ASH threshold equivalence is checked.

## CAM-S002-01 — COMPLETED within preregistered cutoff (2026-10-12)
Six specified labeled simple connected order-8 graphs, all exact configuration sizes t=2,...,14, with no graph-symmetry quotient (1,918,566 labeled configurations). Preregistered plan SHA256 `a1403026ddc36fed628ac4e7ef6ce633c7d4dfbd240d87315e17509a2da115fd`. Forward exhaustive legal-move dynamic recursion plus 420 independent BFS samples; full-layer independent inverse-DP on W8 and bridged K4s; no mismatches. Sources tools/cam_s002_01.py and tools/reverse_cold_check.py, report research/S002_ASH_FOUNDATION_AND_ATTACK.md. Raw output checksum `a437a59259b0a3b28f883cd92405ee7d270823d95f5c59a0fc60815566017515`. Exact W8 threshold 11 and bridged-K4 threshold 13 for both stack and clear. Remaining four graphs >14 within measured cutoff. NOT complete n=8 atlas, NOT ASH proof, and no plausible counterexample. Full raw files attached to session conversation as S002_research_evidence.zip.

## CAM-S003-01 — COMPLETED within preregistered caps (2026-10-12)
- Plan SHA-256 `8e8bc65d0cf3a0392ebb19dba4176975dfc14ae3d6a96196bb128c1765afe084`, hashed before any run. Amendment 1 SHA-256 `6ce55071e5f9a75b323a76a8517e7b1245ceaf61ab31a3a19a9e57d5590433c2`, hashed before the amendment runs.
- Tiers:
  - T1: C6, C7, C8, C8+{0,4}, C8+{0,2},{4,6}, triangular ladder, K2,6, W8.
  - T2: all connected graphs with n≤6.
  - T2b: all 853 connected graphs with n=7, t≤55.
  - T3: trees 2≤n≤9, AS-only below the known stack=estim.
  - T4: W9, C9+{0,4}, Petersen.
  - A1: certificates.
  - A3: n=8 atlas capped at t≤26, run if within budget.
- Solvers: forward C DP, independent reverse C solver (all graphs), Python reverse fixpoint (T1/T4 layers ≤5M) and an independent certificate checker. Every layer comparison agreed. Results and hashes: `evidence/S003/`. Analysis: `research/S003_AS_GAP_AND_ATTACKS.md`.
- Headline: the printed ASH fails (stack on P4 at t=12; clear on the bull graph at t=12). The critical form ASH* holds on every graph whose threshold was found.
- Not claimed: no statement beyond the enumerated graphs and caps; graphs over their cap are cutoff only.
- A3 outcome: completed in full for all 11117 graphs (≈34 min). Thresholds ≤26 were found for 10225 (stack) and 10052 (clear) graphs, the reverse solver agreed on all of them, and there were zero ASH* failures. Totals used ≈71 min of the 180-min budget.

## CAM-S004-01 — completed within registered cutoffs

Plan sessions/S004/PLAN.md (hash in PLAN.sha256), 21 graph/goal runs, no configuration symmetry. All 8 stack/3 clear unresolved n7 cases exact; selected larger graphs completed in19/21 runs. C10 candidate cutoff before t17, triangle-tail clear mass cutoff140. Primary tuple all-predecessor losing recurrence; independent packed canonical-first-parent complete layer replay; cold full reverse-winning base DP on all21 cases. Evidence hashes in evidence/S004/HASHES.md. Total producer computation137.1s excluding serialization; resources stayed within per-case/campaign bounds. Cold audit n<=4 and structural n<=5 campaigns also completed; 233 independent-set witness challenges. No universal verdict.

## CAM-S005-01 — completed within documented scopes
2026-10-13/14, PLAN plus seven hashed amendments; 341 exact labelled graph/goal certificate pairs, 340 eligible, 337 thresholds, three eligible cutoffs and one ineligible bipartite sanity run. All connected n=2..6 plus explicit selected sparse n7/n8/named graphs. Full all-parent C++ losing recurrence; independent canonical-parent Python/streamed coordinate-array complete set equality and reverse-winning bases. No state symmetry. 133,405,188 certified losing states; AS critical witnesses and all Q/lex maximizers AS throughout completed thresholds. Finite scope only. Timer layer-boundary overshoot5.635s and continuation/eligibility/representation/replay changes in AUDIT. Hashes and exact inputs in evidence/S005. Universal ASH* OPEN; S006 strictly future.

## CAM-S006-01 — completed exact interface challenges, explicit state cutoff

PLAN and three hashed amendments, local Windows, no new atlas census/threshold frontier. 152 pure source cases plus one buffer box, all grammar production/infinity/attaining-tree checks; separate stacking forest box. 35 graphs/531 full rooted layers/3155536 labelled configurations compared by independently written forward/reverse traversals, no symmetry;11750 pure and1508 clear/1508 stack comparisons. Tail3 stops at29 before324632-state next layer; tail4 cap10. Existing257 n<=6 critical sets challenge fixed-residue concentration. Scalar closures/traces independently checked. Full scope/hashes in evidence/S006 and AUDIT. No new global threshold or ASH* certificate.

## CAM-S007-01/02 — complete registered small family challenges

S007 PLAN and Amendments1-2 hashed before execution. Triangle-tail l=0,1,2 only, labelled/no symmetry. Clearing masses1..4/10/22; stacking1..4/8/16. Independent forward/reverse full set hashes/counts plus literal constructive trace arithmetic; counts in S007 AUDIT/evidence. No larger atlas/cutoff expansion. Infinite clearing rests on symbolic proof, not extrapolation.

## CAM-S008-01/02 — complete registered scopes

S008 PLAN and Amendments1-2 hashed before runs. Tip-source two-singleton exact tree/forest buffer certificates l0..8,774 finite forest witnesses, independent optimality/legality; full candidate closures l0..3 with1/14/101/891 states. Symbolic universal algebra4376 production inequalities (not graph-size sampling). F_k k1..3, both goals,72 full layers/127799 configurations,36173 constructive traces/479591 legal moves; independent forward/reverse hashes/counts and literal replay. No symmetry/stochastic/atlas/cutoff expansion. Infinite theorems are written proofs. Scope/code/input/output hashes in evidence/S008; universal target OPEN.

## CAM-S009-01/02 — completed registered precision challenges

PLAN and Amendments1–2 hashed BEFORE computation; initial P3 buffer/diamond labeling corrected beforehand with old text/digests retained. CAM01 exact first-return fragments versus independent complete forward closures/reverse rooted recurrence on318 named vectors/n<=5/mass<=18:53924 total closure states/max3409,1694 literal rooted traces; three affected P3 forest components independently checked. CAM02 three fixed dominated graphs at upper masses9/12/12:33 complete reverse layers/13088 configurations,3860 every-upper-input traces/41800 literal moves/795 B3 protected trees. No symmetry/new threshold/atlas/cutoff expansion. Retained implementation failure logs precede corrected successful runs. All executions below600s/300000 states/2GB; code/input/output/environment hashes in S009 manifest. Symbolic proofs and universal OPEN scope are separate.

## CAM-S010-01/02/03

Prior-hashed PLAN/Amendments1-3/code/input preflights; no symmetry,600s/300000 states/2GB caps.01 six-graph count<=5/root/pile1..4 box37556 certificates/26274 traces/3856 weak failures; separate chronology and closures.02 eight-graph/fourteen-goal136 full rooted layers/125481 inputs/930 traces/7703 moves; full independent masks; C5 graph-wide root STACK false.03 frozen01's7289 k3 traces/all21707 occupied marks/98878 reflections/2642 empty paths, full partitions/count/root/literal checks and1447 deleted-input complete closures/60868 states/max122. No new atlas/cutoff/universal/kernel claim. Plans/code/inputs/outputs/logs/environment in immutable S010 manifest.

## CAM-S011-01/02/03 - completed within exact registered scopes

PLAN and Amendments1-3 hashed BEFORE computation, independent forward/reverse/count chronology validators, no symmetry,600s/300000-state/2GB caps.01 eight fixed graphs at inherited maximal masses:90 layers/97839 inputs/3416 winning insertions/4418 deletion checks,4883 traces/43286 moves/15 selected complete negative closures.02 frozen S010 count traces plus one explicit C5 cycle:116401 terminal certificates/507217 moves/65164 adjacent pair checks/6978 exceptional(1,1) outcomes/24894 triangle repairs/12 critical CLEAR cuts; C5 negative closure70 states.03 frozen01 layers:97798 mass>=2 root identities/120 critical insertions/23 CLEAR critical cases(15 stackable)/10 bipartite checks, assigned abstract C5 obstruction expressly NOT graph-realized. No new threshold/universal/human/kernel claim or old cutoff expansion. Exact plans/code/input/output/environment/log hashes in S011 immutable manifest.

## CAM-S012-01/02/03 - complete at registered exact scopes

PLAN and amendments1-5 frozen before dependent computation; no symmetry,600s/2GB/300000-state limits.01 original eight boxes plus FIXED prism/bridged triangles masses0..14:175359 configurations/16394311 exact relations,714 traces/5484 moves/69 complete critical closures; full independent forward/reverse masks, exact8/8 and12/12 controls only. Initial zero-base omission failed and was corrected under amendment3; original preflight/log retained.02 same boxes:435 one-step barriers/15 critical full closures1177 states/78 fuel witnesses338 moves, independent BFS/DAG tau.03 same critical layers:42 transfers/18 traces116 moves/26 negative closures1177 states/18 whole-layer Q extrema, no nonAS Q maximum in bounded sample. No resource cutoff, old cutoff expansion, universal/human/kernel assurance or ASH* counterexample. Actual C5 double donor output absent; no false exception claim retained as result.

## CAM-S013-01 through06 - complete within prior-hashed exact scopes

PLAN/amendments1-6 and code/input/environment preflights frozen before dependent computation.01 historical11970 graph records/10858 both-exact pairs/114 gap1.02 eleven fixed labelled boxes incl selected gap1 A7_0036 through14:291639 configurations, complete independent four-mask forward/reverse equality and exact12/13.03 open exchange313052 implications/3437 modified-count histories,1872 closed-extension failures, six full negative gap1 inputs/20 first successors.04 arbitrary low receivers370252 implications/12239 histories,13 precise STACK exceptions/no CLEAR failure, complete global Q/P selection.05 all189 exact historical STACK critical sets/1028 losers/eight adjacent pairs and fresh selected negative closures;12345 private certificates111047 literal moves/85604 adjacent small transfers.06 all134 losing layers>=4/614 selected extremizers/17 restricted maxima comparisons. No symmetry,600s/2GiB/300000 states per layer/input, no caps hit or old cutoff changes; distinct complete checkers and hashes in S013 evidence. Universal and kernel assurance remain separate.

## CAM-S014-01 - completed bounded diagnostic in ACTIVE S014

Prior-hashed amendment1 fixes148 historical exact CLEAR inputs and paired STACK summaries, plus existing eleven precision boxes.44 positive-gap archive cases and four positive-gap controls: independent integer/neighborhood versus streamed-byte/triple diagnostics agree on ALL labeled Q/Q-P maximizers and predicates. Every tested selected maximum AS and no heavy triangular vertex; no universal inference/new threshold/closure/old-cutoff expansion.600s/2GiB/300000-state caps, no caps hit. S014 itself remains IN_PROGRESS.

## S014 CAM02 completed within ACTIVE session

2087 matching cases/2210 reservations/114 complete reconstructions;127 of127 triangular loss-transfer tests fail, with independently checked selected negative closures. Proper-subset Hall obstructions retained. Prior-hashed plans, frozen preflights, separate producer/checker logs and full certificates under sessions/S014/evidence/S014. No caps hit or universal/session promotion.

## S014 CAM03-04 completed within ACTIVE session

Complete unbounded binary source rays plus independent full general losing layers certify theta334 STACK25/CLEAR27 and barbell55 STACK48/CLEAR48. All critical losers on these four cases AS; mixed source boxes remain limited. Prior-hashed plans, frozen preflights, separate producer/checker logs and full certificates under sessions/S014/evidence/S014. No caps hit or universal/session promotion.

## S014 CAM05-06 completed within ACTIVE session

Whole-pile swaps fail1846 of10240 tests, including71 GLOBAL-Q CLEAR cases; triangular split fails3 of176 tests. Selected complete negative closures and winning traces independently checked; weaker critical variants unproved. Prior-hashed plans, frozen preflights, separate producer/checker logs and full certificates under sessions/S014/evidence/S014. No caps hit or universal/session promotion.

## S014 CAM07-10 completed within ACTIVE session

Seven complete-bipartite triangular construction challenges, four book examples, seven balanced exact AS ray examples/ten general thresholds and7620 literal one-edge AS histories all pass at their fixed scopes. Prior-hashed plans, frozen preflights, separate producer/checker logs and full certificates under sessions/S014/evidence/S014. No caps hit or universal/session promotion.

## S014 CAM11 completed within ACTIVE session

Fourteen matching-buffer full threshold comparisons,66144 literal STACK histories/552534 moves and explicit AS witnesses pass independently. Prior-hashed plans, frozen preflights, separate producer/checker logs and full certificates under sessions/S014/evidence/S014. No caps hit or universal/session promotion.

## S014 CAM12 completed within ACTIVE session

Two full W/path-cover algorithms agree on50 prescribed labeled F graphs, giving146 join graphs/292 goal comparisons:146 exact STACK endpoints match82;286 goal endpoints exact, six CLEAR initially incomplete at STACK cutoff. Prior-hashed plans, frozen preflights, separate producer/checker logs and full certificates under sessions/S014/evidence/S014. No caps hit or universal/session promotion.

## S014 CAM13 completed within ACTIVE session

All66642 boundary cells/11625 terminal histories/10033 true path covers agree independently; six earlier CLEAR cutoffs separately completed with old layers unchanged;228 explicit STACK AS witnesses checked across146 graphs. Prior-hashed plans, frozen preflights, separate producer/checker logs and full certificates under sessions/S014/evidence/S014. No caps hit or universal/session promotion.

## S014 CAM14 completed within ACTIVE session

All198320 arbitrary-buffer literal STACK histories/2046597 moves pass independently, including180224 n16 histories with order bound17 strictly dominating both other lower terms16. Prior-hashed plans, frozen preflights, separate producer/checker logs and full certificates under sessions/S014/evidence/S014. No caps hit or universal/session promotion.

## S014 CAM15 completed within ACTIVE session

ALL26 source rays/six general comparisons certify Q3plus03 thresholds15/15, Wagner8 11/11, Petersen10 15/15; every open neighborhood minimal, every critical Q/Q-P maximum AS. Prior-hashed plans, frozen preflights, separate producer/checker logs and full certificates under sessions/S014/evidence/S014. No caps hit or universal/session promotion.

## S014 CAM16 completed within ACTIVE session

All256 parity-preserving AS candidates for32 non-AS Wagner goal/input pairs checked,1716 literal winning moves; every input has a related parity-class AS loser. Bounded positive pattern only. Prior-hashed plans, frozen preflights, separate producer/checker logs and full certificates under sessions/S014/evidence/S014. No caps hit or universal/session promotion.

## S014 CAM17 completed within ACTIVE session

Fixed343 goal cases/1043 non-AS critical inputs: two ALL-receiver fixed-parity failures and eight heavy-receiver failures. Original schema KeyError/code/log preserved; separate hashed v2 metadata-only repair passes. Prior-hashed plans, frozen preflights, separate producer/checker logs and full certificates under sessions/S014/evidence/S014. No caps hit or universal/session promotion.

## S014 CAM18 completed within ACTIVE session

Two exact critical parity obstructions independently recomputed through threshold9, every old layer preserved;161 complete negative states/12 same-parity AS winners/72 moves checked. Critical non-AS loser isolated under every unit redistribution; alpha2 blocks endomorphic AS lift. Prior-hashed plans, frozen preflights, separate producer/checker logs and full certificates under sessions/S014/evidence/S014. No caps hit or universal/session promotion.

## S014 CAM19 completed within ACTIVE session

Fixed343-case odd-shift diagnostic:34 true-head transforms/14 eligible critical inputs,28 losing outputs. Each input has some losing output; six ORDERED-pair variants fail. Smaller-donor22-pair filter is post-data finite support, not a universal theorem. Prior-hashed plans, frozen preflights, separate producer/checker logs and full certificates under sessions/S014/evidence/S014. No caps hit or universal/session promotion.

## S014 completed continuation CLM-0162

CAM20:252 labeled graphs/24192 inputs,4080 eligible smaller donor3 pairs all have a losing shift. Independent DAG checker validates321804 states/184453 full negative states/603635 legal dependencies. No universal extrapolation. Prior-hashed amendments20-24, separate preflights/full outputs/checks under evidence/S014. No universal or phase promotion.

## S014 completed continuation CLM-0163

CAM21 v2:3710 labeled connected n6 graphs/267120 inputs,9484 eligible losing pairs,583 all-shift-winning failures. Independent DAG checker validates2129306 states/3092719 dependencies. Generic smaller-odd-donor loss preservation false; original pipe interruption and passing repair retained. Prior-hashed amendments20-24, separate preflights/full outputs/checks under evidence/S014. No universal or phase promotion.

## S014 completed continuation CLM-0164

CAM22/23: six preselected graph controls have exact STACK thresholds25,36,36,40,15,13; independent full sets and1800 negative-closure states/56 transformed winning moves checked.259 of583 failures satisfy minimal-heavy residual restriction; all selected failures below critical/global-layer Q. Prior-hashed amendments20-24, separate preflights/full outputs/checks under evidence/S014. No universal or phase promotion.

## S014 completed continuation CLM-0165

CAM24: independently compared1878298 full losing states on ALL215 labeled graphs underlying583 head-shift failures. NONE is critical or layer-global Q; every graph has L_all=L_AS. The universal critical/global-Q weakening remains unproved. Prior-hashed amendments20-24, separate preflights/full outputs/checks under evidence/S014. No universal or phase promotion.

## S014 active CLM-0167

CAM25:252 full general threshold comparisons,508929 losing states;4 ordered-pair failures at2 actual critical inputs refute smaller odd private-head input existence. All graph AS comparisons hold; no non-AS global Q critical maximum. Prior-hashed plan and independent complete code/certificates/logs under sessions/S014/evidence/S014. No session or phase promotion.

## S014 active CLM-0168

CAM26: fresh complete negative closures for2 critical inputs and2 AS critical witnesses,2556 states;52 literal transformed winning moves. Critical private-head failure is not ASH* failure. Prior-hashed plan and independent complete code/certificates/logs under sessions/S014/evidence/S014. No session or phase promotion.

## S014 active CLM-0170

CAM27: entire-source H2 fails1124 of1230 critical non-AS inputs, already P3(3,3,0); source residual must not be silently forbidden. Failed H2 records retained. Prior-hashed plan and independent complete code/certificates/logs under sessions/S014/evidence/S014. No session or phase promotion.

## S014 active CLM-0171

CAM28:444 fixed STACK cases/1230 non-AS critical inputs/45804 full residual H2r candidates, zero failures. Bounded support only. Prior-hashed plan and independent complete code/certificates/logs under sessions/S014/evidence/S014. No session or phase promotion.

## S014 active CLM-0172

CAM29:72 new cycle/matching/chord graphs n8/9/10,1545176 complete losing states,227 non-AS critical inputs/11632 H2r candidates, zero failures. All AS comparisons hold; no universal extrapolation. Prior-hashed plan and independent complete code/certificates/logs under sessions/S014/evidence/S014. No session or phase promotion.

## S014 active CLM-0173

CAM30:252 coupled n12 gadget inputs at mass16,108 lose/144 win;617212 state records/1799764 legal dependencies checked, no cap hit. Two strongest cross-edge survivors selected by prior rule; not ASH* counterexamples by themselves. Prior-hashed plan and independent complete code/certificates/logs under sessions/S014/evidence/S014. No session or phase promotion.

## S014 active CLM-0174

CAM31: complete unbounded source/binary-buffer STACK rays on C00_51/C00_60; explicit automorphisms cover all12 sources using reps0/2/4. Exact L_AS18/24. Thus fixed mass16 holes do not refute ASH*. General thresholds tested separately in CAM32. Prior-hashed plan and independent complete code/certificates/logs under sessions/S014/evidence/S014. No session or phase promotion.

## S014 active CLM-0175

CAM32: exact general STACK thresholds19/25 on C00_51/C00_60, independently compared348930/587258 full losing states; exact AS maxima18/24 match. Every critical loser is AS, H2r scope there vacuous. No unrestricted ASH* inference. Prior-hashed plan and independent complete code/certificates/logs under sessions/S014/evidence/S014. No session or phase promotion.

CURRENT S014 ACTIVE through CAM45: local proofs71-93, including exact AS-tail90, extremal graph/input normal form92 and bipartite every-root neutral catalysis93. Fixed-input exclusions C6/C9a/C9b/E8/M9 independently certified; C10/E9/E10/M10/F9/T10/T12 UNKNOWN. CAM44 checks638 complete critical sets/20231 inputs/17940 non-AS, none with pile2; four even-heavy inputs all nonbipartite. Universal no-two and H2r UNPROVED. Universal STACK/CLEAR OPEN; CLEAR deferred. Continue until proof/counterexample, no session closeout/commit/PR/S015 handoff. See research/S014_COUNTEREXAMPLE_SEARCH.md and hashed PLAN_AMENDMENT_33..45 for exact scopes, successful independent proofs and all preserved UNKNOWN attempts.

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
