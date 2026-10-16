# CAM-S014-79: complete finite prescribed-source challenge

2026-10-16 BEFORE execution. Challenge116 on ALL142 connected graph cases
through order6 with their complete saved losing sets S. Generate ALL legal
predecessors x+2e_u-e_v of ALL x in S, across ALL true arcs and x_v>=1.
For EACH predecessor c not in S with at least two occupied sites, check
EVERY heavy source w has SOME neighbor destination with a child outside S.
Retain all actual outgoing child memberships, not merely one witness move.

This covers every possible failing winning input on these graphs at ANY
mass: a failure's prescribed heavy source has a losing legal child, hence
that input is among the enumerated predecessors. Its mass is at most the
old exact threshold. Single-pile winning terminals are separately counted
and excluded from116, especially pure3. No claim about graphs outside the
registered142 cases or arbitrary new graph sizes.

Producer packed states/bitmask arcs versus independently written tuple
predecessors/membership with full input-set and ALL arc-mask equality.
Binary records24bytes:16-byte input plus8-byte ordered-arc winning mask.
Each case stored separately, full derived result provenance before validator.
No new reachability solver or bare heuristic classification. Old thresholds
and complete negative sets are frozen, not enlarged or inferred anew.

Bounds:1M saved states/layer,2M total saved states,2M candidate predecessors
per graph,5M total distinct predecessors,20M legal child membership tests,
540sec internal/600sec external/2GiB each. ONE mathematical child at a time.
Caps UNKNOWN and stop, with no passing completeness claim. Freeze111-117,
old graph/certificate inputs, plan and exact code before producer; freeze
result inventory and binary records before independently regenerating.
Any discrepancy halts the symbolic route. No CLEAR/delegation/closeout/
commit/PR/Lean/phase/contact/future session; universal ASH* remains OPEN.
