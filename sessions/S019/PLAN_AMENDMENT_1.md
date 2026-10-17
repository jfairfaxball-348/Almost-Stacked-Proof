# S019 PLAN_AMENDMENT_1 - chain the certificate-data modules too

Written after plain-build run 1 and before any further build. Hash in PLAN_AMENDMENT_1.sha256.

Run 1 (check modules chained, data modules not): plain `lake build` from clean completed, rc 0, 758 s, 1201 jobs, no watchdog kill; heavy checks strictly sequential (peak 9.3 GB in one process, 10.3 GB total at that moment, 0.6 GB free physical memory at the minimum). But the preregistered acceptance criterion (peak total private memory below 13 GB) FAILED: 17.9 GB at 10:22:54Z, when about 15 certificate-data modules (`AlmostStacked.Data.G9*`, about 1.2 GB each during elaboration) built in parallel (evidence/S019/plain_build_1.txt, mem_plain_build_1.csv). On Palomar's 16-core runner this phase could reach about 19 GB alone; the criterion is kept, not relaxed.

Change: chain the 28 data modules by one more import line each, in the same order as the checks: `Data.G9Stack3` imports `Data.G9Stack2`, ..., `Data.G9Stack15`; `Data.G9Clear2` imports `Data.G9Stack15`; `Data.G9Clear3..15` import their predecessor. Exactly one line `public import AlmostStacked.Data.<previous>` after `public import AlmostStacked.KTree`; nothing else changes. Un-freeze entries first (old hashes, reason B4), re-freeze after a passing run.

Run 2: identical acceptance test to PLAN.md M2 (clean `.lake/build` moved aside; plain `lake build`; 2 h; sampler and 12 GiB watchdog; peak total private memory below 13 GB; then axioms identical, scan PASS, Comparator statement check). If run 2 fails the criterion, record it and stop changing modules; report to the owner.
