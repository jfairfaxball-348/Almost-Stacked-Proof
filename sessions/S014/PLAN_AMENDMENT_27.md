# CAM-S014-27: a weaker all-root heavy-elimination implication

2026-10-15 BEFORE computation. S014 remains ACTIVE. Critical local odd private
heads fail in CAM25/26. Test a weaker, fully stated implication rather than
repairing its ordered-pair quantifier silently:

H2: for EVERY general critical STACK loser c with at least two heavy sites,
there exist distinct heavy s,t, k in{0,1,2} with k<=c_s, and a k-element subset
U of initially EMPTY sites, such that d=c-c_s*s+(c_s-k)*t+1_U loses.
No edge, parity, smaller-donor, support-preserving or root restriction.
All untouched heavy buffers retained. Every such d has exactly one fewer
heavy site, so H2 for ALL graphs/critical inputs would prove universal ASH*
by finite induction on the number of heavy sites, at the SAME largest mass.
This implication does not rely on Q increasing; for c_s=2,k2 it can decrease.
It includes even and nonadjacent heavy sites. It is UNPROVED, not assumed.

Fixed finite test cases: ALL STACK cases in parity_archive/inputs.json with
complete registered critical layers, plus ALL252 headcritical cases. Keep
duplicates as labeled repeated controls, no new graph/threshold expansion.
For EVERY non-AS critical input enumerate ALL ordered heavy pairs and ALL
eligible k/U exactly as above, none filtered by observed outcomes. Maximum
300000 generated candidates per input;600seconds/2GiB per process. Cap means
UNKNOWN. Producer packed membership versus separate tuple-coordinate
enumeration, exact full keys/outcomes and one-heavy decrease verified.
Freeze original complete certificate digests, code/input/plan/environment.

Record input-existence failures and first FOUR deterministic actual examples.
They refute H2 only if every candidate is independently certified winning;
the complete layer checks establish membership, and fresh histories require
another bounded plan. No ASH* refutation if other AS critical losers remain.
Follow a surviving H2 symbolically toward its stated induction, or pivot to
a weaker same-mass AS construction if H2 fails. No CLEAR/session closeout.
