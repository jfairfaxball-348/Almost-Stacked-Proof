# S014116-117: a prescribed heavy source and the full graph-leaf restriction

Universal ASH*-STACK remains OPEN. These proofs strengthen114; its oddness
and bipartite assumptions were sufficient but unnecessary for the leaf
consequence. The earlier proof's marker relocation is not needed when the
resulting boundary tree need not already be canonical. Frozen111-115 remain
unchanged. Every statement uses whole inputs, true edges and all roots.
No new TreeStack equality, independent human/kernel or priority claim.

## 116. A winning first move can use any prescribed heavy vertex

Let G be finite connected simple with n>=2. If a nonempty configuration d
is STACK winning and has at least TWO occupied vertices, then for EVERY
vertex w with d_w>=2 there exists u adjacent to w such that

    d-2e_w+e_u is STACK winning.                         (116)

Proof.113 supplies either T(d), or T(d+2e_q) for some q, where T means an
exact THREE boundary tree111. In the first case |d|>=4: mass3 reaching3
uses zero moves, so would have been a single pile, contrary to the two-site
hypothesis.112 therefore normalizes the witness to have floor(d_w/2)>=1
w-labeled LEAF. Delete that leaf alone, and call its parent label u. Its
edge is true, u~w. The nonempty remaining tree has maximum degree<=3.
At w its boundary drops2; the parent's degree drops1 so its boundary rises
exactly1 at u. This remains true if the remaining tree is a SINGLE vertex:
its degree0 boundary is3, replacing the old degree1 boundary2. All other
boundary contributions are identical.111 gives T(d-2e_w+e_u).

In the second case |d+2e_q|>=5 because d has a heavy site AND another
occupied vertex. Normalize this padded witness by112. It has at least one
w-leaf, including when q=w, since the original d_w>=2. Deleting one such
leaf gives T(d-2e_w+e_u+2e_q) at the SAME padding label q.113 implies STACK
of the unpadded child. The child is nonempty and nonnegative. This argument
does not designate an added pebble as an original one, or cancel equal
input/output mass:113 already proves precisely the needed positive root
cancellation. The two cases cover all winning d. QED.

The converse is always true: a winning legal child gives a winning parent.
Thus for any NONSTACKED input with some heavy vertex, its STACK decision
can inspect only outgoing moves at ANY chosen heavy source. Stable inputs
with two or more singleton sites lose; one-site inputs win immediately.
This is an exact decision equivalence, not deterministic destination
independence, a bound on the number of configurations, or an AS theorem.

The multioccupied hypothesis is essential at d=3e_w: any move gives two
adjacent singletons, which lose. For a single pile k e_w with k>=2, k!=3,
EVERY neighbor move is winning. For k2 it gives one pebble; for k4 or k5,
the child consumes along that edge into a pile (k4: one more forward move;
k5: forward then backward); k6 child(4,1) gives3 at the neighbor by two
forward moves. For k>=7 the child reduces three untouched w pebbles to the
k-3 case using the known occupied-source +3 operation. The child w count
after reduction is k-5>=2, so the operation retains a positive base and
is legal. These bases and induction cover all k>=2 except3. No exceptional
pure3 is hidden.

## 117. Exact graph-leaf safety and critical neighbor zeros

Let w be a GRAPH LEAF with unique neighbor v. For every nonempty d with
d_w>=2 and d!=3e_w,

    STACK(d) iff STACK(d-2e_w+e_v).                       (117a)

Proof. For multioccupied d apply116, whose only possible destination is v.
For single-pile d use116's explicit k2/k4/k5/k6 and induction cases. The
other implication is the displayed true legal move. At the omitted pure3
input the parent wins and its two-singleton child loses. QED.

Consequently, if c is ANY STACK loser with c_v>=1, then

    c-e_v+2e_w loses and has mass |c|+1,                  (117b)

EXCEPT when c=e_v+e_w. To prove it, call the larger input d. If d STACKed,
117a would make its child c STACK, unless d=3e_w, which is exactly the
listed c. No parity/bipartiteness or positive c_w hypothesis is needed.
The child c is nonempty by assumption; the exceptional c really is two
adjacent singleton pebbles and loses.

**Critical restriction117c.** On EVERY finite connected simple graph of
order n>=3, EVERY actual critical STACK loser c has c_v=0 whenever v is
adjacent to any graph leaf w. If c_v>=1 and |c|>=3,117b produces a loser at
strictly larger mass, contradicting global last loss. The exceptional mass2
cannot be critical here: the all-ones input at n>=3 is a losing stable
configuration. K2 has critical input(1,1), so n>=3 is necessary. Zero/one
vertex graphs have no eligible statement. This is strictly stronger than
114b's even-heavy bipartite exclusion, with no threshold convention change.

For an arbitrary d other than3e_w, repeated117a also gives exact leaf-pair
reduction: move floor(d_w/2) pairs off w, leaving d_w mod2 there and adding
floor(d_w/2) at v. After the first move v is positive and never decreases
during these leaf-only moves, so the exceptional pure3 cannot appear later.
The final configuration has the same STACK status as d; a remaining leaf
singleton is retained, not silently discarded. This is an exact local
algorithm, not a block threshold formula or a universal extremal proof.

The universal gap remains in graphs with minimum degree>=2 and in the
comparison of all general losers with same-graph AS losers.117 supplies
neither critical global oddness nor heavy elimination H2r. Continue S014.
