# CAM-S014-43: smaller certified trace supports for the unresolved C10 class

2026-10-15 BEFORE execution. Exact C10 input [1,0,0,0,0,0,7,7,1,1],
n10,M17, all connected labeled graphs. CAM37 hit its iteration bound; CAM38
hit its clause bound and CAM40 found that partial formula SAT. All UNKNOWN.
Continue the SAME class, with independently certified stronger trace clauses,
not a claimed exclusion from any of those caps.

Import the50010? NO: use EXACT records in frozen
`evidence/S014/cegis/C10/constraints.jsonl` (the actual recorded5010 clauses;
do not infer a count from this prose). For every c-winning trace, take its
used-edge graph and greedily remove an edge whenever exact legal recursion
still wins c; retain the final literal history. Each new negative clause is
independently justified by that history and may be stronger than the old one.
Cache identical original supports; do not rely on old UNSAT or core results.
All cut/AS-negative records remain with their original certificate paths.

Use exactly the limited permutation family from CAM41 (within-count cyclic
rotations plus simultaneous reversal),60 distinct maps, every one fixing c.
Import all base records first at identity, then add these valid clause images.
Continue at most1000 fresh CEGIS iterations with the SAME c-winning trace,
AS-negative-supergraph and lazy connectivity rules; all new winning traces
also minimized. No graph isomorphism quotient and no pre-fixed edges.

PRIOR caps500000 necessary clauses,300000 oracle states/tested graph,
540seconds internal/600seconds external/2GiB per process; at most2 mathematical
children with CAM42. Freeze old original certificates/code/input/environment
and new code/plan before producer; freeze derived outputs before independent
base-certificate and literal permutation replay. If UNSAT, invoke the fully
separate CAM42 watched RUP checker on THIS frozen formula/proof at its SAME
500000-line/500000000-visit/540s caps; this paragraph explicitly extends its
input list to this case, with every clause already independently justified.
If potential, full negative/ALL3AS-layer DAG independent replay then separately
registered exact-threshold/cold audit. Any cap/SAT incomplete proof UNKNOWN.
No universal inference, CLEAR, delegation, closeout or external/later-stage work.
