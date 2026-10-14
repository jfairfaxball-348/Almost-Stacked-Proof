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
