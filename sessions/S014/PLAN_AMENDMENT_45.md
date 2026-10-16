# CAM-S014-45: hinted RUP proof replay with untrusted native LRAT generation

2026-10-15 BEFORE execution. C9a already has a complete CAM42 independent
proof pass, but C9b's watched replay is still running and prior slower proof
attempts were UNKNOWN. Do not raise their caps. Use an independently checkable
hinted certificate on the ORIGINAL CAM38-v2 formulas/proofs for C6,C9a,C9b.
No graph/input/clause changes. All original clauses already have full separate
graph certificate and literal-permutation necessity passes.

An existing local DRAT-trim binary is read-only tooling, not research on its
host repository: C:/Earth-Moon-problem/artifacts/tmp/S004/drat-trim-mingw.exe,
SHA256970caaea97a15c8a27d4747e0e92e058ac1b1d9d4e04a95e3fc58b069ed4c03e.
Its actual help lists uppercase -L for LRAT output and -U for RUP only.
Official implementation/documentation: https://github.com/marijnheule/drat-trim .
No files in that other repository are edited. Record binary digest before and
after; save native command/log/resource outcome. Native output is UNTRUSTED
hint generation; its VERIFIED string alone is not the accepted proof.

Separate pure-Python checker loads the frozen CNF clauses with exact original
indices. For every LRAT addition, assume its negated literals, then replay the
positive clause-id hints: each can derive only a unit whose other literals
are false, or an actual all-false contradiction. Satisfied hints may be skipped;
an unexplained non-unit hint fails. Require contradiction for EVERY added
clause, then store it under a fresh id. Apply explicit deletions, prohibit id
reuse, and require a verified EMPTY addition. Negative RAT hints are unsupported
and UNKNOWN. No native solver imports, graph oracle or searching in this checker.

PRIOR caps500000 input clauses,500000 addition lines/1000000 total LRAT lines,
100000000 hint visits,540seconds internal/600seconds external/2GiB per native
or Python process. At most2 mathematical children with CAM43/44; wait for a
slot. Native -t540 plus external wall/memory supervision. Freeze code/input/
plan/binary metadata before native, then LRAT/output digests before independent
checker. Any cap, malformed or unsupported proof UNKNOWN. Scope ONLY those
fixed-c graph classes; universal ASH* OPEN, no closeout or external/later stage.
