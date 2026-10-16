# S014115: two units of pair fuel give an exact path obstruction

Universal ASH*-STACK remains OPEN. This is a complete structural consequence
of111-113, not an extremal comparison, new TreeStack result or novelty claim.
It retains ALL binary buffer vertices. Let G be finite connected simple,
n>=2, c=p+2a nonempty with binary p, A=sum a and P=sum p. Here A=2.
Write a=e_q+e_r, allowing q=r. Then |c|=P+4>=4.

**115a.** c reaches exactly THREE iff its p-support U admits an ordering
(v_1,...,v_P), each vertex appearing exactly once, such that

    q ~ v_1 ~ ... ~ v_P ~ r.

For P=0 this means simply the true edge q~r. Equal consecutive labels are
forbidden in a loopless graph, even when an endpoint also belongs to U.

Proof.112 forces A=2 leaves, P degree-two markers, and A-2=0 branches.
Thus its canonical ancestry tree is a path. The leaves have labels q,r,
and its internal vertices are precisely the distinct labels U. Conversely
such a path is the exact boundary tree112, and111 reconstructs THREE with
every original pebble consumed. No Hamiltonian path in G is claimed when
U omits vertices or q/r repeat a marker label. QED.

**115b.** On bipartite G with signed I(c)=0 this is also equivalent to STACK,
by111's signed-zero reduction. On an arbitrary connected graph one must
add113's alternative: for SOME s, the input c+2e_s has a THREE witness.
Its canonical tree has THREE leaves labeled q,r,s, exactly ONE degree-three
branch with any graph label, and the SAME unique degree-two marker set U.
Consequently it is a three-arm subdivided star with those exact labels and
true graph edges. The branch label can coincide with any marker/leaf label;
no unwarranted injectivity restriction is imposed on that branch. This is
an exact STACK criterion: path OR one of these three-arm trees. QED.

For c having two piles3 and one pebble everywhere else, U=V. The internal
marker path in115a is a spanning path, with extra endpoint labels q,r.
For AS concentration a=2e_s the endpoints both equal s. A missing such
spanning walk only excludes THREE; on a nonbipartite graph115b's three-arm
alternative must ALSO be excluded before claiming loss. This distinction
is material for the next fixed-input search.

The old independent-set AS witness (S004 Theorem12, numerical bound credited
to the primary paper) already supplies L_AS>=3alpha when alpha>=2. Thus any
such input of mass<=3alpha is automatically dominated by an AS loser on
the SAME graph, irrespective of its path obstruction. In particular, in a
bipartite graph of order n>=8, |c|<=n+4<=3ceil(n/2)<=3alpha; hence no A=2
input on such a graph can violate the global comparison. This is an exact
restricted domination statement, NOT a bipartite universal upper theorem.
For lower orders use their existing separate exact coverage or proofs;
no uninspected source completeness is inserted here.

The potentially relevant fixed-input search on orders8-12 must therefore
allow nonbipartite graphs and retain115b, full AS tail and exact threshold
conditions. Bounded failure to find a graph gives no universal theorem.
S014 remains IN_PROGRESS, with no closeout/phase/Lean/future session.
