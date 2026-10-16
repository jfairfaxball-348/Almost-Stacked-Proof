# CAM-S014-11: matching-buffer comparison, before computation

2026-10-15. Continue active S014, without closing the session or promoting the
universal headline. Proposed G(a,b,m): independent A of size a, independent B of
size b, and m disjoint auxiliary edges; every B vertex joins every A/auxiliary
vertex. Integers a,b>=1,m>=2. Candidate STACK=CLEAR=max(3b+1,3a+4m+1), both ASH*.
The proof under adversarial check uses GLOBAL Q/P minimal-neighborhood selection,
two possibly heavy roots, explicit parity/path constructions, and an all-target
weighted lower on the quotient with one B vertex. No generic quotient equality.

Fixed graphs (a,b,m): (1,1,2),(1,2,2),(2,2,2),(2,3,2),(1,4,2),(1,1,3),
(1,2,3). Orders6..9. Full general STACK and CLEAR losing layers from1 through
T=max(3b+1,3a+4m+1), with all roots and every nonnegative configuration. No
symmetry reduction. Reuse unchanged independently written packed predecessor and
tuple canonical-parent checkers, through new directory-only wrappers. Each
checker compares the entire losing set, exact critical AS maximum and empty
first winning layer. Candidate/layer caps5M/1M,600s/2GiB per process; any cap
remains UNKNOWN, never a theorem. n<16 and mass<256 explicitly checked.

Literal STACK challenge: the same seven graphs, every configuration with at most
one heavy A and at most one heavy B, all auxiliary coordinates binary, totals
T,T+1,T+2. Count cap300000 per graph; exceeding it records UNKNOWN rather than
sampling. Enumerate one chosen heavy root per part (first occupied otherwise),
both parities, every binary buffer and every nonnegative split between the two
roots. Deduplicate full configurations. Producer uses the symbolic path formula,
never move search. Independent checker regenerates all keys by a distinct
whole-composition recursion, verifies the structural restriction, every actual
edge and two-source availability, and exact positive final pile. Replay the
proposed lower witness by the complete full losing sets, not a failed history.
Retain branch counts, exact full certificates and hashes; preflight freezes
plan, graph inputs, new wrappers, imported unchanged implementations and runtime.

Finite agreement corroborates only these seven cases. The all-parameter proof
requires its own complete inequalities, root/zero/parity/target cases. Earlier
F_a, independence/complete-bipartite theorems and path primitives stay credited.
