# CAM-S014-58: compact Q4 AS upper DAG, preserving CAM57's state-cap UNKNOWN

2026-10-16 BEFORE execution. CAM57 independently checked16931 completed
queries/2000000 states, but full AS tail UNKNOWN. New method, same Q4 and
exact98304 AS inputs at31/32/33; source0/all32768 masks plus16 XOR maps.
Use105's shared positive-source tree/two-/three-forest ancestry nodes.
No larger forward-state cap and no reinterpretation of57 as a full result.

Pure trees have source cost2^popcount(q). Source0 positive tree node table
enumerates all proper buffer splits then shortest positive pure-sibling
walks. Two-/three-forest nodes retain exact disjoint buffer splits and SAME
root. A separate zero-cost singleton child is permitted ONLY for U={q}.
Any selected final AS witness MUST have positive source cost, at most its
actual source count and matching residue modulo3. All surplus source inputs
are consumed by occupied +3 reduction, not omitted.

Producer stores at most32768*16*3=1572864 nodes (<2000000), uint32 cost+
uint8 kind/neighbor+uint16 splitmask (8 bytes/node), cost cap1024. No zero-
source tree is silently represented by a positive node. Within-mask tree
steps must strictly decrease source cost. Independent verifier checks EVERY
node's actual ancestry production, exact costs, root/edge, disjoint input
partition, positive-source/zero singleton distinction and well-foundedness.
It imports no producer code/optimizer. It checks EVERY AS source-count query
at31/32/33 against an attaining positive node and ALL16 XOR maps.

Verifier proves sound upper witnesses only; no independently unchecked
producer minimum is used for a negative claim. If a query has no affordable
certified node, return UPPER_WITNESS_MISSING_UNKNOWN, not a losing input.
If all98304 queries pass, exact L_AS30 follows from90/100. This still gives
NO full general threshold or universal ASH* result. General-input search
requires a separate preregistered plan AFTER this tail's actual verified
status. Prefix/time/cost failures remain UNKNOWN with preserved tables.

Producer and checker internal540seconds, external600seconds/2GiB each,
at mostTWO mathematical children overall. Freeze graph/query spec,105,
plan, all code and dependencies before producer; derived node/choice/result
files frozen before independent replay. No CLEAR/delegation/Lean/phase,
closeout/future session/contact/publication. Continue S014.
