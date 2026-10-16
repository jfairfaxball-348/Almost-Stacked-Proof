# S014 continued: an unconditional elimination candidate with mass slack

Universal STACK remains OPEN. This records a precisely UNPROVED sufficient
lemma. It is not another assertion that a local move preserves all losing
layers. H2r remains the earlier critical-only, exactly mass-preserving route.

For a loser c with at least two heavy sites, choose distinct heavy s,t,
r in{0,1}, k in{0,1,2}, r+k<=c_s, a k-subset U of initially EMPTY sites,
and delta in{0,1,2}. Form the whole same-graph input

    d=c-(c_s-r)e_s+(c_s-r-k+delta)e_t+1_U.

Candidate H_up2: EVERY such c has SOME choice giving a loser d. There is no
criticality, fixed root, sign, adjacency, smaller-donor or fixed-support
hypothesis. Untouched buffers are arbitrary. The proposed family is explicit
and finite; it is stronger than ASH*, not an accepted generic theorem.

If universally true, it proves the requested universal comparison directly:
|d|=|c|+delta>=|c|, s becomes0/1, t stays heavy, U becomes binary, so h(d)=
h(c)-1 exactly. Repeat finitely to an actual AS loser on the SAME G with
mass at least |c|. Applying to a global maximum c forces every encountered
delta=0 and recovers the required largest AS loser. All input occurrences
are retained in each new input definition, with explicit mass addition;
no input-winning history is mistaken for an impossible original history.

Unlike exact-layer elimination, this candidate permits repairing an interior
hole by finding an AS loser at a LARGER mass. On the earlier printed P4
example(9,2,0,1), eliminating the2 into the9 and adding delta2 gives the
known critical AS loser(13,0,0,1), mass14. This is an illustration only;
universal existence needs proof, and a finite failure would refute H_up2
while leaving ASH* open. At actual criticality the family is exactly H2r,
because no larger loser exists. Thus the global critical gap is not removed
merely by changing the formulation.

CAM69 challenges this new sufficient lemma on complete previously checked
losing sets, including ALL lower layers. This is aimed at finding a proof
mechanism which need not assume criticality, or a precise barrier before
investing in that argument. S014 remains IN_PROGRESS, CLEAR deferred.
