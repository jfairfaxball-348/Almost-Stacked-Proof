# S01487-88: exact true-head surgery and its signed obstruction

Active S014, STACK focus. Universal L_all<=L_AS remains OPEN. These are
complete local written arguments, not a kernel or independent human audit.
Known count reconstruction44, three-pile reflection50, signed invariant and
critical imbalance52 retain their existing source credit. No new threshold
or novelty claim is made.

## 87. Triplet donors: complete certificate reconstruction with the real cut

Let G be finite simple undirected, s~t and s~v, with s,t,v distinct. Let c be
nonnegative, h>=1, c_s>=3h, and set

    d=c-3h e_s+(3h-1)e_t+e_v.

No hypothesis on other counts, zero support, neighborhood inclusion,
bipartiteness or terminal root is required. Suppose a winning count
certificate m of d ends at positive pile k e_q and has at least h copies
of t->s. If q=t, OR there is a t-to-q positive directed path remaining after
removing h copies of t->s, then c stacks to the SAME k e_q.

Proof. Define actual nonnegative counts

    m'=m-h[t->s]+(h-1)[s->t]+[s->v].

With A(m)=2out-in, direct calculation gives

    A(m')-A(m)=3h e_s-(3h-1)e_t-e_v=c-d.

Hence c=k e_q+A(m'). Only outgoing t copies were removed. If q=t, choose
simple old paths to t; none uses outgoing t. Otherwise protect the stated
remaining t-to-q path. Any old path damaged by the removal reaches t before
its removed arc and can then use that protected path. Thus all old used
labels retain a path to q. Any newly used s reaches old occupied v by the
added true arc s->v; v is occupied in d, regardless of its input in c, so
has just been shown to retain a path to q. There are no other new labels.
Every original c input is among these labels. Exact connected reconstruction
44, via the credited reverse commutative grammar, gives the legal complete
history. No simultaneous scheduling or leftover relaxation is assumed. QED.

Consequently, if c is a STACK loser, EVERY winning certificate of d has

    m_ts <= h-1 if q=t;
    m_ts <= h   if q!=t.

In the second case equality forces every positive directed t-to-q path to
use the arc t->s: it is an essential cut for that actual certificate. If
m_ts>=h+1 the support still contains t->s after removal and all original
paths survive, which proves the asserted bound. These are multiplicity
constraints, not a bound on distinct heads or a common cut across winners.

This includes source sizes3,6,9,..., so includes EVEN donors. If c_s=3h,
c_v=0 and c_t>=2, the candidate has strictly higher concentration:

    Q(d)-Q(c)=2(3h-1)(c_t-1)>0.

Thus global Q maximality supplies a winner d and the stated necessary cuts.
It does not contradict them. The private-head hypothesis v notin N(t) is
unneeded for the reconstruction; that restriction belongs to the candidate
existence mechanism, not to87's proof. If no empty s-neighbor distinct from t
exists, this candidate does not even exist.

## 88. Non-triplet donors have a genuine signed barrier at critical mass

Let G be finite connected bipartite with n>=2, signs epsilon=+1/-1 on its
parts, and let c be ANY globally largest STACK loser. By52 its signed mass
I(c)=sum epsilon_x c_x is zero modulo3. For adjacent s,t, another s-neighbor
v!=t, and ANY integer a>=1 with c_s>=a, define

    d=c-a e_s+(a-1)e_t+e_v.

It has the same mass and is nonnegative. Since epsilon_t=epsilon_v=-epsilon_s,

    I(d)-I(c)=-2a epsilon_s = a epsilon_s (mod3).

If 3 does not divide a, d MUST stack: otherwise its same globally largest
mass would make it a critical loser with nonzero signed imbalance,
contradicting52. In particular all heads win for donor5/7 (and even2/4)
whenever such an input/head actually occurs. This is a conditional universal
obstruction to that mechanism, not an assertion that such a critical input
has been exhibited. It neither excludes the input nor refutes ASH*.

More basically, any integer change of actual directed move counts on a
bipartite G has signed A-value zero modulo3: each arc contributes
2epsilon_u-epsilon_v=3epsilon_u. Therefore when 3 does not divide a, c and d
cannot have certificates with the SAME root AND SAME terminal pile size.
The appealing donor3 count replacement cannot be extended to donor5 by
adjusting multiplicities alone while preserving that terminal. Any successful
proof in this case must change terminal type/root or construct a different
loser. It cannot infer loss from the shared descendant.

## Global follow-through and remaining obligation

87 supplies a valid even-donor reconstruction test and an exact all-winner
cut burden for entire triplet piles.88 sharply separates the non-triplet
critical bipartite cases. Neither supplies L_all<=L_AS. The outstanding task
is to combine actual consuming certificates with compatible roots/cuts, or
select a different same-mass AS loser, on the SAME graph. Nonadjacent heavy
sites, arbitrary heavy buffers, and all non-triplet residue classes remain.
Even in87's adjacent triplet class the cut constraints may all coexist;
no inconsistency across the whole winning family has been proved.

CAM20's distinct coordinate checker validates321804 state records including
184453 full negative states and603635 legal dependencies on252 prescribed
graphs/24192 inputs. All4080 eligible smaller-donor shifts have a losing
candidate. Its smaller donor is always3. This is bounded evidence only;
CAM21 separately challenges larger donors. Frozen execution artifacts and
resource logs are under evidence/S014/oddchallenge and oddlarge.

## Completed hostile follow-through: the arbitrary-loser shift is false

CAM21 v2 covers ALL3710 connected labeled six-vertex completions of01/02
with12 absent, and267120 registered inputs. The independent coordinate DAG
checker validates2129306 state records/3092719 legal dependencies. Of9484
eligible losing ordered pairs,583 have EVERY permitted private-head shift
winning. Donor sizes are3 (four failures),5 (342) and7 (237).259 failures
already satisfy70's minimal-heavy, distinct-neighborhood restriction;496
are bipartite. Thus neither smaller-donor selection nor70's residual domain
makes the assertion true for arbitrary losing mass. This is a precise failure
of that implication, not of ASH* or its critical weakening.

A particularly simple residual counterexample is the complete bipartite
graph with parts{0,3,4,5} and{1,2}, exactly edges

    01,02,13,14,15,23,24,25.

The input c=(3,3,0,1,1,1), mass9, loses; its complete negative legal closure
has126 states. Both heavy neighborhoods are minimal and incomparable. The
smaller/equal donor0, receiver1 has ONLY empty private head2. Its candidate
d=(0,5,1,1,1,1) stacks by the literal moves

    1->3, 1->4, 3->1, 1->5, 4->2, 2->5,

ending in3 at5. This witness has NO1->0 move, so87's necessary restriction
is fully consistent with it; no cross-winner contradiction follows. Its
signed mass is0 and its donor is3, so88 does not rule it out either.

CAM22/23 certify complete thresholds of the six preselected graph controls:
25,36,36,40,15,13. The displayed complete bipartite example has threshold13,
critical mass12 and losing-layer Qmax51 versus Q(c)21. All critical Q maxima
there are AS. Its critical AS witnesses include(9,0,0,1,1,1). The known
complete-bipartite result is credited; these examples claim no new threshold
theorem. Six extracted negative closures total1800 states, with56 literal
transformed winning moves checked separately. All selected failures are below
critical mass and below their own layer's GLOBAL Q maximum.

We did not extrapolate that last observation from six examples. CAM24
recomputes every complete STACK losing layer on ALL215 distinct labeled
graphs underlying the583 failures, comparing1878298 full losing states by
the two independent algorithms. EVERY failure is below critical mass and
below its losing-layer GLOBAL Q maximum. Every one of these graphs has
L_all=L_AS. The critical/global-Q weakening is therefore NOT refuted by
these failures, and remains UNPROVED universally. No candidate/state/time
or memory cap was hit in any completed CAM20-24 run.

The original CAM21 attempt was explicitly interrupted after209.672seconds
because its undrained progress pipe stalled execution. Its471 partial graph
certificates and unsuccessful log remain intact and UNVERIFIED as a campaign.
A separately frozen v2, reducing output frequency only and adding independent
input-list reconstruction, finishes in22.688/20.890seconds (producer/checker).
This implementation failure and repair are distinct from both mathematical
counterexamples and completed finite tests; see sessions/S014/REPAIR_21_1.md.

## Review boundary, with no universal inference

The failed general loss-preserving true-head implication has been followed
through its exact residual, critical and GLOBAL-Q quantifiers.87 handles
actual triplet/even-donor certificate surgery and88 proves the signed barrier
to extending it without changing terminal data. The remaining critical/global
version requires additional mathematics relating DIFFERENT actual winners;
neither the current cut bounds nor the signed calculation supplies it.
Repeating the now-tested local implication or enlarging finite agreement
cannot close that step. No complete new cross-winner proof is available at
this review boundary. This is an unresolved mathematical obligation, not an
owner-action blocker. Future work must seek that global argument or a weaker
same-mass AS existence construction and keep nonadjacent sites/arbitrary
heavy buffers/even non-triplet donors explicit.

CURRENT CONTINUATION SUPERSEDES THE EARLIER REVIEW-BOUNDARY NARRATIVE: S014 remains ACTIVE, owner explicitly prohibits closeout before proof/counterexample. CAM25/26 now refute the critical private-head input-existence strengthening too; GLOBAL-Q-only remains unproved. Read research/S014_CRITICAL_HEAVY_ELIMINATION.md. All earlier scoped proofs/evidence preserved.
