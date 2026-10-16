# S014108: complete losing layers modulo true graph automorphisms

Universal ASH*-STACK remains OPEN. This is the earlier exact all-predecessor
and canonical-first-move recurrence, specialized to107's exact Q_d translation
orbits. It is not a new general ancestry/TreeStack theorem or a conclusion
from samples. A compiled producer is UNTRUSTED until independent replay.

Fix Q_d, d>=1, n=2^d, count coordinates<256 in16-byte states (d<=4 here).
Let C(x) be the greatest packed integer under all n XOR translations. This
is a different total order from107's tuple order, equally valid. It fixes a
unique representative VALUE of every full labeled configuration orbit;
different shifts attaining it do not give different states.

For mass m, given the COMPLETE orbit representatives L_(m-1) of previous
losers, generate every inverse d+2e_u-e_v for d in L_(m-1), true edge u~v
and d_v>=1, then canonicalize. Add every canonical binary stable input of
mass m (when m<=n). Discard positive one-site goals. A candidate loses iff
EVERY true legal successor's canonical representative belongs to L_(m-1).

Completeness proof. Every nonterminal loser c either has no legal move, in
which case it is a binary stable input with at least two occupied sites, or
has a legal move c->z into the previous COMPLETE losing layer. Translate z
to its representative d; the same automorphism sends c to an actual inverse
of d along a true edge. Thus C(c) is generated. All its successors lose iff
the input loses, since mass falls1 and the graph/action preserve goals.
This is an induction on mass, with mass1 goals excluded and binary seeds
reintroduced at every appropriate mass. No upward monotonicity is assumed
from the mass1 empty losing layer. Only an EMPTY layer ABOVE n invokes the
earlier exact-threshold/above-order source convention.

Independent checker generation can instead take EVERY labeled translate z
of each previous representative and invert ONLY the deterministic first move
of a proposed canonical parent c: its lowest heavy source u and lowest true
neighbor v. Require the parent already canonical. Every canonical loser has
that actual first successor in some previous orbit, so it is generated in
this independent recurrence. Its candidate set need not equal the producer's
larger all-inverse candidate set; their COMPLETE losing sets must coincide.
Stable binary parents and positive terminal goals remain separate.

Checking each complete labeled-orbit set and all its negative successors,
plus this independent complete parent inventory, certifies winners as the
complement as well as actual losers. An exact AS oracle may accelerate an
AS candidate's yes/no test only after106's whole proof chain passes; the
independent recurrence does not rely on native producer decisions. Missing
or capped layers never establish a threshold. A mass31 Q4 loser, with exact
L_AS30, would require a fresh cold counterexample audit. An empty mass31
layer would prove stack(Q4)=31 and ASH* on Q4 ONLY, not universally.

CAM63 first compiles/controls Q1 and Q3, then attempts full Q4 through31,
with fresh per-layer process/resource bounds and Python complete replay.
No independent human/kernel/novelty or later-phase assurance is claimed.
