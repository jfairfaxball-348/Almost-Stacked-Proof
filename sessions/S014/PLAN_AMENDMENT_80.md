# CAM-S014-80: odd-leaf contraction and even-leaf +3 ascent

2026-10-16 BEFORE execution. Use exactly ALL142 connected graph cases
through order6 and their complete saved losing sets S, no bipartite filter.
Challenge119b by BOTH losing ends: for EVERY x in S with an odd graph-leaf
count and parent>=2, x-e_w-e_v must be in S; for EVERY y in S with even
leaf count and parent>=1, y+e_w+e_v must be in S. This covers every possible
failing equivalence on each fixed graph because one end of a failure loses.
Challenge120a for EVERY saved loser with positive even graph-leaf count:
c+3e_w must be in S. Check all critical leaf counts are zero or odd.
Include leaf0 in119b's reverse direction, odd leaf>1, parent1/2, empty
leaves and nonbipartite cases. No false inverse with parent1 in119b.

Producer packed-state adjacency versus independent tuple incidence checker,
equal complete configuration/leaf/direction inventory and every membership.
Both use old exact certificates/thresholds, not a new capped reachability
claim. Freeze118-120 and dependencies before execution; derived results
before independent verification. Bounds1M old states/layer,2M total saved
states,2M records,540sec internal/600sec external/2GiB per child. ONE math
child at a time. Caps UNKNOWN. No extrapolation to new graph orders.
This tests actual universal scoped proofs but does not establish ASH*.
No CLEAR/delegation/closeout/commit/PR/Lean/phase/contact/future session.
