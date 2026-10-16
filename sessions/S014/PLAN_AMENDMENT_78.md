# CAM-S014-78: all-graph challenge of117's full leaf-neighbor ascent

2026-10-16 BEFORE execution. Use ALL142 fixed connected graph cases through
order6 and their complete saved labeled losing sets, with NO bipartite
filter. For EVERY nonempty loser c, EVERY graph leaf w and its neighbor v
with c_v>=1, independently check d=c-e_v+2e_w is losing, except precisely
c=e_v+e_w. Check ALL such exceptions really give the pure3 winning input,
and EVERY critical losing input of every graph n>=3 has c_v=0 at all leaf
neighbors. This tests117, a written universal scoped proof, not ASH*.

Producer packed integers and graph adjacency versus independently written
tuple validator reconstructing incidence degrees directly. Require equal
complete original input/leaf/source inventory and every losing membership.
Old exact thresholds make above-threshold nonmembership decisive. Include
nonbipartite graphs, parent pile1, odd heavy parents, empty leaves and both
directions in K2. No new graph/reachability search or invented completeness.

Bounds1M old states/layer,2M total parsed saved states,2M extension records,
540sec internal/600sec external/2GiB per child. One mathematical child at
a time. Cap UNKNOWN; no truncated computation called complete. Freeze old
certificates,111-117 proofs, code and plan before producer; derived output
before independent checker. No CLEAR/delegation/Lean/closeout/commit/PR/
phase/contact/future session. New source-first challenge gets its own plan.
