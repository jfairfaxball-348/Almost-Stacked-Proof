# S018 PLAN_AMENDMENT_2 - standalone external-kernel replays at one thread (PLAN.md M2.4)

Written after Comparator run 2 and before any further kernel run. Hash in PLAN_AMENDMENT_2.sha256.

Comparator run 2 (evidence/S018/comparator_run2.txt): statement comparison and axiom check passed (lake comparator reaches the kernel stage only after `compareAt` and `checkAxioms` succeed, Lake/CLI/Check.lean `verifyMatch`); Lean's own kernel (`leanchecker --silent --from-export`) accepted the Solution export; `con-ron --jobs=2` and `nanoda_bin` (num_threads 4, set by lake comparator) were killed by the preregistered 12 GiB watchdog (tools/s018_memcap.ps1; evidence/S018/memcap_kills.txt: con-ron 12,376 MB, nanoda_bin 14,655 MB), which lake comparator reports as "rejected" and as exit 4294967295. Under PLAN.md these two are UNKNOWN (cap), not rejections and not passes; the overall exit is 1.

Standalone replays (sequential, one process at a time, same Solution export exports2/Solution.export sha256 855ba7b9cf7a5e2557b3394d22ade3757eda04335f616ac5b0ab06f2cc628b3a), each with the 12 GiB watchdog and a 2 h wall cap, driver tools/s018_kernels.sh, log evidence/S018/kernels.txt:
1. `nanoda_bin <cfg>` with the same JSON configuration lake comparator writes (permitted_axioms propext, Quot.sound, Classical.choice; unpermitted_axiom_hard_error false; nat_extension and string_extension true) but num_threads 1.
2. `con-ron --jobs=1 <export>` (default --verified mode).
3. `lean4lean --import <export>` (the bundled paranoid command form).
4. `leanchecker-paranoid --silent --from-export <export>`.
5. `con-leche <export>`.
Outcome per checker: exit 0 => ACCEPT; nonzero exit without cap kill => REJECT (a finding: diagnose); cap kill or timeout => UNKNOWN. Exit 0 of a checker is recorded as that checker's acceptance of the whole Solution closure (including the 28 kernel-evaluated layer checks). Nothing here changes formal/.
