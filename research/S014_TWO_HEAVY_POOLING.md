# S014 continued: explicit two-donor pooling at an arbitrary receiving site

Universal STACK remains OPEN. This is a new UNPROVED sufficient hypothesis,
chosen AFTER CAM69's unconditional heavy-receiver restriction failed. It is
not a repair of69's frozen scope or a consequence of positive finite tests.

For ANY actual loser c with h(c)>=2, choose two distinct heavy sites s,t,
arbitrary receiving q (including either donor, another heavy, a singleton
or an empty site), residuals r_s,r_t in{0,1}, and up to2 initially empty
sites U excluding q. Put k=|U|, F=c_s-r_s+c_t-r_t and require F>=k.
First replace both donor counts by their residuals, then add F-k+delta at q,
and one at each U, with delta in{0,1,2}. Denote the whole result d.

Candidate H_pool2: SOME such choice is losing, for EVERY c and G in scope.
There is no adjacency, root, fixed parity, fixed support or criticality
assumption; arbitrary untouched buffers remain. No assertion of truth yet.

If true universally, this would prove the actual universal comparison:
mass(d)=mass(c)+delta, and h(d)<=h(c)-1. Indeed both old donors become bits
unless one is q, and the ONLY possibly new heavy is q. Existing other heavy
sites cannot multiply; U is binary. Pooling at a donor keeps it heavy and
eliminates the other. Pooling elsewhere eliminates both and creates at most
one. At least one heavy disappears in every case, including F=k and a binary
receiver. Repeat at most h(c)-1 times to an actual AS loser of mass>=mass(c)
on the SAME G. Apply to a global maximum: all deltas must then be0. This
conditional induction covers even/nonadjacent piles, all buffers and roots;
the unproved ingredient is the actual existence of a LOSING pool result.

This is strictly a finite local candidate family, not the statement that
some unrelated larger AS loser exists. CAM70 preregisters its first complete
all-layer challenge. Any failure leaves ASH* open; agreement is not proof.
This remains focused on the universal heavy-elimination bridge, with no
new family-threshold programme. No closure or later-phase authorization.
