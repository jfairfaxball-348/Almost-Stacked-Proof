# CAM-S014-14: general-buffer upper, including order-bound dominance

2026-10-15 before execution. Challenge82's explicit two-heavy STACK construction,
not another threshold inference. Fixed F=P3,K3,2K2,K1,3,C4,K4,P5,C5,K1,4,K5,
each a=b=1; additionally F=P5,a2,b3; and F=K10,a1,b5. The last has n16,
W12, S17=n+1 strictly greater than both other lower terms16.

For the first eleven graphs test EVERY binary off-root vector and EVERY split
between fixed roots r=0 in A,t=a in B at totals S,S+1,S+2. For K10 test
EVERY such vector/split at total17 (no residue-tail completeness claim).
Other A/B sites are binary; all F sites are binary. Root permutations within
A/B are true checked automorphisms, so these are ALL selected-form inputs
up to those explicit source permutations, not random buffer sampling.

Producer computes Hamiltonian subset paths then optimal path covers of F[U]
by a finite complete subset DP, using the required prefix of cover edges as
blocks. It constructs actual moves via82/80; no pebbling move search. Retain
complete histories, all branches, every original input and final positive pile
as compressed JSONL streamed per graph. Independent checker enumerates all
keys via combinations, checks minimal classes and source automorphisms,
replays every true-edge/source-availability move and exact final pile. Per
graph cap1000000 traces,600s/2GiB per process; a cap is UNKNOWN, no sampling.

Independently check n16 all-ones as the explicit critical AS loser (no legal
move) and S=max(n+1,3b+1,3a+W+1), with W(K10)=12 from Hamiltonian paths on
every nonempty clique subset. No infeasible full threshold enumeration on n16
and no claim finite traces alone prove the unbounded theorem. All code/input/
plan/import/runtime hashes frozen first. S014 continues, headline OPEN.
