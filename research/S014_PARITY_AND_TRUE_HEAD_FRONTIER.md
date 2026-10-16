# S01485-86: actual critical barriers and a parity-changing frontier

ACTIVE continuation, locally complete proofs at the stated scopes. No
unrestricted ASH* proof/disproof, formal certification or priority claim.
This follows81-84 back to incomparable and partial neighborhoods rather than
stopping at the arbitrary-buffer join class.

## New complete residual controls, outside the join comparison

CAM15 independently certifies ALL unbounded AS source rays for every source,
every binary buffer and every root, then EVERY general losing layer through
the first winning layer. Q3plus03 (cube plus edge03) has STACK=CLEAR15;
Wagner8 has STACK=CLEAR11; Petersen10 has STACK=CLEAR15. All their open
neighborhoods are minimal. All six critical Q/Q-P selected sets are AS.
Wagner has32 critical losers for each goal, only16 AS. CAM16 checks ALL256
parity-concentrated candidates for its32 non-AS goal/input pairs, including
empty receivers, with1716 literal winning moves. Each has some AS loser of
the same parity. This finite positive pattern is not a universal theorem.

CAM17 challenges it on the fixed343 archived goal cases, ALL1043 non-AS
critical inputs. Two cases refute the ALL-receiver fixed-parity assertion;
eight refute its original-heavy-receiver version (including the already
known C5 donor-root obstruction). Initial CAM17 attempt failed with a
metadata KeyError at the new nested summaries. Original code/preflight/log
are preserved. The separate v2 schema-only repair and independent checker
pass; no certificate, cutoff, goal or case was changed. That failure is not
a mathematical UNKNOWN or a silently discarded test.

## Complete exact counterexamples to critical fixed-parity compression

Let G0 have vertices0..5 and exactly edges

    01,05,14,23,24,25,34,35.

Let G1 add edge45. Both have STACK threshold9. Their ENTIRE critical losing
layer is the following three inputs, each of mass8:

    c =(3,3,1,1,0,0),
    a0=(5,0,1,1,1,0),
    a1=(0,5,1,1,0,1).

Thus ASH*-STACK HOLDS on both graphs. However c's parity vector is111100,
and its SIX possible AS inputs of mass8 with that parity are

    (5,1,1,1,0,0), (1,5,1,1,0,0),
    (1,1,5,1,0,0), (1,1,1,5,0,0),
    (1,1,1,1,4,0), (1,1,1,1,0,4).

Every one STACKs. CAM18 recomputes ALL general losing layers1..9 by the two
independent algorithms, compares every decoded state with the old full
certificate, constructs complete forward negative closures for c and a1,
and literal winning histories for all twelve parity-class candidates.
The independent closure/move checker verifies161 negative states/72 moves,
not a failed move sequence. The named graphs are S005 atlas inputs; their
existence/threshold is not claimed new. The newly isolated failure is the
same-parity strengthening at ACTUAL critical mass.

All three critical inputs are isolated under ANY unit mass redistribution
c-e_s+e_t, including nonedges. In particular c is a non-AS local Q maximum
among such losing neighbors (there are none), yet global Q28 belongs to a0/a1,
above Q(c)20. One cannot replace GLOBAL maximality by a greedy one-step local
maximum, even at critical mass. No chain of losing unit redistributions
connects c to an AS input. The true jump must change parity and several
coordinates simultaneously. A continuous/simplex or fixed-parity argument
cannot be imported merely from the extremal formulation.

## 85. What extremizer selection really retains inside a parity class

Fix any finite simple connected eligible graph, either goal, and a NONEMPTY
losing layer of exact mass M>=4 with a prescribed parity vector. Select c
maximizing Q within that class, then minimizing P=sum deg(v)c(v).

**Proposition85.** No two heavy sites of c have comparable/equal open
neighborhoods. If a heavy s has a strictly smaller neighborhood N(t) subset
N(s), then c_s is ODD and c_t=0. This conclusion holds for EVERY such t.
It does not force all heavy neighborhoods minimal inside a parity class.

Proof. The even exchanges66 preserve the parity vector. If a comparable
heavy receiver exists, transferring every even pair gives the same strictly
positive Q change as64, contradicting maximality. For strict N(t) subset
N(s), c_t>=2 is already excluded. For c_t1, transferring h=c_s-(c_s mod2)
preserves loss/parity and has Q change2h(1-(c_s mod2)). This is positive
if c_s even; otherwise Q stays equal and P strictly decreases. For c_t0
and c_s EVEN, transfer the entire EVEN source pile by66. Q is unchanged,
P strictly decreases. Only c_s odd and c_t0 escapes these arguments. The
mass>=4 hypothesis excludes66's genuine STACK mass3 exception. QED.

Original67 removes this remaining case by moving the ENTIRE odd source pile
to the empty smaller-neighborhood site using a true endomorphism; that move
CHANGES parity. Hence67 is correct globally and cannot silently be reused
as minimal-neighborhood selection inside a prescribed parity simplex.
The counterexamples above are stronger still: their relevant heavy sites
already have minimal, incomparable neighborhoods. Repairing the parity-local
selection alone would not make fixed-parity critical compression true.

## 86. Why a same-graph endomorphic AS lift cannot repair these inputs

**Proposition86.** For any finite simple G and endomorphism f:G->G, if d is
AS then f_*d has at most one coordinate strictly greater than alpha(G).
Every fiber of f is independent, since an edge cannot collapse to a loop.
All fibers avoiding d's unique possible heavy input have only0/1 inputs,
so their sums are at most their fiber sizes, hence at most alpha(G). Only
the fiber containing that heavy input can exceed alpha. This also covers
an entirely binary d. QED. This uses the elementary known independent-fiber
fact, not an assertion of a new general homomorphism theorem.

Both G0/G1 have alpha2, independently verified by exhaustive subsets in
CAM18 (the complement has no triangle and a nonedge exists). Their c has
TWO coordinates3>2. It therefore cannot be the pushforward of ANY AS input
under ANY same-graph endomorphism. So 'lift this critical loser to AS by an
endomorphism' is false as a universal compression mechanism. Threshold
equality under a different quotient remains separately unproved; this does
not contradict the correct one-direction quotient restriction49.

## A genuine parity-changing candidate, not an accepted universal lemma

The actual AS losers are simultaneous odd/even redistributions:

    a1=c-3e_0+2e_1+e_5,
    a0=c-3e_1+2e_0+e_4.

For an odd heavy s adjacent to heavy t and an EMPTY v in N(s) minus{t}, put

    d=c-c_s e_s+(c_s-1)e_t+e_v.

It changes only the s/v parity bits and strictly increases Q by
2(c_s-1)(c_t-1). If some such d loses, a GLOBAL-Q non-AS c is excluded.
It is not itself a legal mass-preserving pebbling move, and a common losing
successor does NOT prove either parent losing. For the examples, c and a1
share the losing successor c-2e_0+e_5, reached respectively by0->5 and1->0;
that diamond alone is insufficient as a universal proof.

CAM19 registers exactly this diagnostic on the same343 archived critical
layers.34 true-head transformations over14 eligible critical inputs give28
losing outputs. EVERY one of those14 inputs has a losing output, but six
ORDERED heavy-pair versions fail. For example A7_0019, STACK11, critical
(1,1,5,3,0,0,0), source2/receiver3 has its only candidate
(1,1,0,7,0,0,1) WINNING; changing which heavy is the receiver repairs the
tested input. Thus the unrestricted ordered-pair statement is not proved.
Filtering the already generated data by smaller donor c_s<=c_t leaves22
eligible ordered pairs, all with a losing PRIVATE-head transform. This is
explicitly a DATA-DERIVED finite hypothesis, not a preregistered universal
theorem, and needs an out-of-sample challenge before proof extrapolation.

The universal step is still missing. One must justify a genuine true-head
reconstruction for a suitable parity-changing transform using the ENTIRE
winning family, or produce a same-graph AS loser by another mechanism.
71's even donor matching does not carry the removed odd original input;
81's binary-region traffic bound does not align the terminal roots or all
actual head copies.59's reciprocal TWO insertion relation is symmetric but
does not by itself supply the required same-input/root compatibility. The
published finite failures of weaker root availability remain in force.

S014 is still active. These are concrete new results, counterexamples to
stronger routes, and a sharply stated unproved next implication. They do
not close the universal programme, license later gates, or constitute an
owner-action blocker.
