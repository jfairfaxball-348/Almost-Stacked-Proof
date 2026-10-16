# CAM-S014-42: two-watched-literal independent DRUP verification

2026-10-15 BEFORE execution. Earlier bounded independent RUP scans remain
UNKNOWN when capped. The clause sets already have separate literal graph
certificate provenance. Implement another pure-Python unit-propagation replay
using exactly two watched literals per non-unit clause, explicit units and
empty clauses, full assumption reset for EACH proposed step, persistent legal
watch positions, and active multiplicity-aware deletion. No native solver,
producer oracle or graph enumeration in this verifier. A watch can move only
to a literal not currently false. Without such a replacement, its other watch
is forced, or an all-false clause certifies contradiction. Thus every accepted
proof addition is RUP, including the final empty clause. This is an ordinary
verification algorithm, with no claimed novelty or independent human audit.

Inputs ONLY completed frozen CAM38-v2, CAM40-core and CAM41 fixed cases whose
formula has the separate necessary-clause pass and status solver-UNSAT.
Freeze exact formula/proof/necessity/code/plan digests before each replay.
C6 original proof is the first control: agree with BOTH prior independent
replayers on all37 added steps and final empty. For other inputs require every
proof addition, including empty, checked; never infer validity from a matching
step count or native UNSAT. No partial proof promotion.

PRIOR caps500000 proof lines,500000000 active watched-clause visits,
540seconds internal/600seconds external/2GiB per process. At most2 concurrent
mathematical children with CAM40/41; wait for a slot. All caps UNKNOWN. Keep
earlier failed/capped attempts intact. Accepted results exclude ONLY their
fixed-c graph class, not universal STACK/CLEAR. No closeout or later-stage action.
