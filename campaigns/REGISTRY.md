# Registered mathematical campaigns

**No active campaign in S001.** R-E in research/ROUTES.md is a *proposal*, not an authorised computation.

Proposals must specify: CAM identifier, theorem statement, graph model and atlas source, graph-size and pebble-mass range, enumerator and completeness proof, isomorphism/canonical-labelling assumptions, legal-move state solver, genuinely independent verifier, log/raw data location, expected hash and stopping rule. Search output cannot be promoted to a certified counterexample until exact ASH threshold equivalence is checked.

## CAM-S002-01 — COMPLETED within preregistered cutoff (2026-10-12)
Six specified labeled simple connected order-8 graphs, all exact configuration sizes t=2,...,14, with no graph-symmetry quotient (1,918,566 labeled configurations). Preregistered plan SHA256 `a1403026ddc36fed628ac4e7ef6ce633c7d4dfbd240d87315e17509a2da115fd`. Forward exhaustive legal-move dynamic recursion plus 420 independent BFS samples; full-layer independent inverse-DP on W8 and bridged K4s; no mismatches. Sources tools/cam_s002_01.py and tools/reverse_cold_check.py, report research/S002_ASH_FOUNDATION_AND_ATTACK.md. Raw output checksum `a437a59259b0a3b28f883cd92405ee7d270823d95f5c59a0fc60815566017515`. Exact W8 threshold 11 and bridged-K4 threshold 13 for both stack and clear. Remaining four graphs >14 within measured cutoff. NOT complete n=8 atlas, NOT ASH proof, and no plausible counterexample. Full raw files attached to session conversation as S002_research_evidence.zip.
