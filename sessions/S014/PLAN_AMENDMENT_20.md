# CAM-S014-20: out-of-sample smaller odd donor challenge, STACK only

Written BEFORE execution, 2026-10-15. Continue active S014, not S015.
Target the proposed sufficient step: for a STACK loser c with adjacent heavy
s,t, odd 3<=c(s)<=c(t), some EMPTY PRIVATE head v in N(s) minus N(t) minus{t}
gives a losing d=c-c(s)e_s+(c(s)-1)e_t+e_v. This assertion on arbitrary losers
is stronger than its critical/global-Q versions. Failure alone is not ASH*.

Exact graph generation: take G0 on 0..5 with edges01,05,14,23,24,25,34,35;
take G1 adding45. For EACH nonempty subset of vertices0..5 add vertex6
adjacent exactly to that subset (126 labeled graphs). Additionally take each
of those126 graphs and add vertex7 adjacent exactly to{2,6} (126 graphs).
Every graph is connected. No isomorphism quotient or symmetry reduction.
For each graph set c0=3, c1 in{3,5}, and independently c_i in{0,1} for
all i>=2. Thus n7 has64 and n8 has128 inputs per graph, total24192 inputs,
mass6..14. Inspect BOTH ordered pairs(0,1),(1,0), retaining only odd smaller
donors, and EVERY empty private true head. All other inputs remain untouched.
This deliberately tests arbitrary binary buffers; it does not cover arbitrary
heavy buffers, even donors, nonadjacent heavy pairs or unbounded graph sizes.

Producer: memoized full legal-move DFS, wins witnessed by literal full-input
STACK histories; losing states retain ALL children and have no pure terminal.
One shared cache per graph, cap300000 states per graph,600 seconds/2GiB per
process. Checker: no producer imports; decode all stored states, order by
total mass, independently enumerate every ordered pair of vertices and legal
edge, reconstruct exact all-root winning booleans from bottom up, verify all
generated input/pair/head keys and each Q identity. Hash exact input graphs,
code, plan, environment and output/log bytes. No cap increase. A graph hitting
a cap is UNKNOWN; do not count it as a passed assertion.

Keep the first FOUR failing input/pair rows in deterministic graph/input order
with complete reachable negative closures and positive transformed histories
in the shared state certificate. If failures exist, a separate bounded
amendment is required BEFORE computing critical layers or threshold status;
do not infer critical/global-Q status from an arbitrary losing input.

Symbolic follow-through: derive the exact count-change equation for a true-head
shift and identify when a normalized winning certificate of d can be rebuilt
on c. Follow any proof or failure toward the same-graph global inequality.
No CLEAR campaign, delegation, new session, phase/novelty/Lean/contact action.
