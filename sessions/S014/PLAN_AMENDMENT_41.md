# CAM-S014-41: fixed inputs with two-pebble and mixed heavy sites

2026-10-15 BEFORE execution. Continue direct STACK counterexample search on
the residual input domain, especially size-two heavies; no universal no-two
lemma is assumed. Exact eight fixed inputs (n=length, T=sum) in order:

    E8: [2,2,1,1,1,1,1,1]
    E9: [2,2,1,1,1,1,1,1,1]
    E10:[2,2,1,1,1,1,1,1,1,1]
    M9: [2,3,1,1,1,1,1,0,0]
    M10:[2,4,1,1,1,1,1,1,0,0]
    F9: [4,4,1,1,1,0,0,0,0]
    T10:[2,2,3,1,1,1,1,1,0,0]
    T12:[3,3,3,1,1,1,1,0,0,0,0,0]

All have T>=n+1. Search ALL connected labeled graphs at that fixed input,
using the CAM37 certified necessary-clause rules and exact three-AS-layer
tail90. There are no fixed seed edges or assumed graph isomorphism classes.
For each equal-input class list its labels increasingly; choose all cyclic
rotations within each class, and additionally their compositions with the
simultaneous reversal of all classes. Deduplicate these explicit permutations.
They all fix c, so their clause images are necessary. This limited family
adds valid clauses; it does not restrict graphs to representatives, and does
not claim to enumerate the full input stabilizer. No imported CAM37 clauses.
Start with degree cuts, close each new certificate clause under this family,
and minimize each positive c history's used-edge support as CAM38.

PRIOR caps as CAM38:1000 iterations,500000 necessary clauses,300000 oracle
states per graph,540seconds internal/600seconds external/2GiB per process.
One producer/checker at a time within this campaign; at most2 mathematical
children with CAM40. Freeze exact list/permutations/code/plan/runtime before
producer. Freeze all derived clauses/CNF/certificates before independent
CAM37 base-certificate and literal permutation checking. Fresh native DRUP
only provisional; full independent proof replay needed for any exclusion.
Any cap/SAT without potential/unsupported proof is UNKNOWN. A potential must
have complete original negative and ALL three AS-layer positive dependencies,
independently checked and followed by a separately bounded cold threshold
audit before mathematical promotion. No counterexample from a failed move.
No CLEAR, delegation, closeout, next session or external/later-stage action.
