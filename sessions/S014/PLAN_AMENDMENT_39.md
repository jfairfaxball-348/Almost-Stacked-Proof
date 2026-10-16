# CAM-S014-39: independently indexed DRUP replay of the frozen CAM38 CNF

2026-10-15 BEFORE execution. CAM38 C6 replay passes. C9a provenance passes,
but the original simple whole-formula RUP scanner is still running. A solver
UNSAT remains provisional. This amendment changes only independent proof
verification on the exact CAM38 v2 outputs, not the graph/input class or clauses.

For each of its four fixed cases whose producer reports UNSAT and whose base
and orbit necessity checks pass, hash-freeze inputs, formula, clause provenance,
proof and necessity result before replay. Implement a distinct pure-Python
literal-occurrence RUP checker, with no native SAT calls, producer oracle or
graph-state routine. Clauses carry occurrence lists and independent deletion
identities. Each proposed clause must follow by unit contradiction after
assuming its negation. Lazy stamped residual counts/XORs record precisely the
not-yet-processed false literals. Units and empty clauses are handled explicitly;
duplicate/deleted clauses preserve their multiplicity. Every added clause,
including final empty, must pass. Compare C6 with the original independent
scanner's accepted output as a control. Do not reinterpret an old cap as success.

PRIOR caps:500000 proof lines,500000000 active literal-occurrence visits,
540seconds internal/600seconds external/2GiB per case, at most2 mathematical
children total alongside CAM38. Any resource/unsupported-proof outcome is
UNKNOWN. Freeze code/plan plus each derived input before replay. Successful
proof certifies ONLY the exact fixed-c graph-class exclusion, never universal
ASH*. No CLEAR, delegation, closeout, future handoff or later-stage action.
