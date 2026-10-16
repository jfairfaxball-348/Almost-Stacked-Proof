# CAM-S014-76: some-neighbor ascent beyond graph leaves

2026-10-16 BEFORE execution. This challenges an UNPROVED strengthening of114b:
for every bipartite signed-zero STACK loser c and every positive EVEN c_v,
there exists w adjacent to v for which c-e_v+2e_w also loses. No graph-leaf
restriction. A failure refutes this auxiliary statement, not ASH* or114b.

Use exactly ALL142 fixed graph cases/certificates of CAM75, independently
filter bipartite graphs, enumerate ALL saved labeled signed-zero losers and
ALL eligible v. Compare EVERY adjacent w, not a chosen failed move. Complete
old thresholds make membership in the saved losing set decisive for these
inputs. No new reachability search, graph enumeration or threshold inference.
Retain complete inventory even after failures. Record first ten failures,
including graph, configuration, threshold and ALL transformed memberships.
Producer packed integers/BFS versus independently written tuple/parity-union
find validator. Require exact input/v/w inventory and memberships equality.
Optional summaries distinguish c_v=2, actual criticality and minimum degree.

Bounds:1M saved states/layer,2M total saved states,1M input-v records,
5M adjacent extensions,540sec internal/600sec external/2GiB per child.
Use only ONE mathematical child at a time following the owner's report of
unexpected app exits. Code/input/proof111-114/plans and old certificates
hashed before producer; output hashed before independent checker. Caps
UNKNOWN. No CLEAR/delegation/Lean/phase/closeout/commit/PR/future session.
