# S014109: universal bipartite shell AS witnesses by full-history weight loss

Universal ASH*-STACK remains OPEN. This is a complete universal AS LOWER
witness theorem, not the missing general-loser upper comparison. It combines
the credited source valuation/signed invariant/ancestry/+3 operations and
earlier independent-set AS witness. At k1 it recovers the prior path-based
one-bit bound100; at distance2 it recovers the earlier independent-set AS
witness on source plus that shell. No new TreeStack, independent human/kernel
or worldwide-priority assurance is asserted; exact prior-art comparison remains
pending. Whole inputs and every possible final root are retained.

## A general three-output peak-valuation lemma

Let G be finite connected simple, s a vertex, U a nonempty set disjoint
from{s}. Let R:V->positive reals satisfy R(s)=1 and, on EVERY true edge,

    R(u)/2 <= R(v) <= 2R(u).

Assume every u in U is a strict peak: EVERY neighbor v of u has R(v)=R(u)/2.
Put r=min_(u in U)R(u). For x=N e_s+sum_(u in U)e_u, N>=1, any consuming
history reaching EXACTLY THREE pebbles at ANY root satisfies

    N >= (sum_(u in U)R(u)+3r)/2.                 (109a)

Proof. A move u->v loses exactly2R(u)-R(v)>=0 weight. It also loses at
least3(R(u)-R(v)), since the lower neighbor-ratio bound gives2R(v)>=R(u).
An initially singleton peak outside the final root must fire at least once
to empty, and each such peak firing loses exactly3R(u)/2.

If final root q belongs to U, select one firing for each OTHER peak.
Together with final weight3R(q), these disjoint contributions total at least
3/2 sum_U R +3/2 R(q)>=3/2 sum_U R +3r/2.

If q is outside U, every peak fires. Trace any ORIGINAL U input through
its actual ancestry to one of the three terminal q pebbles. Its label walk
has a LAST occurrence v in U. Select that actual v-exit occurrence as the
counted firing for v; select any firing for every other peak. The suffix
after this exit has NO U source label, so NONE of its move occurrences is
among the selected peak firings. Its starting neighbor has weight R(v)/2.
Telescoping the per-move bound gives suffix loss at least
3(R(v)/2-R(q)). Add all selected peak losses and final weight3R(q):
again total at least3/2 sum_U R +3R(v)/2>=3/2 sum_U R +3r/2.
The suffix bound may be negative, which only weakens the valid inequality;
all other actual moves have nonnegative loss. Repeated graph labels along
the spine are distinct production occurrences, so no counting is lost.

Initial weight is N+sum_U R. Subtracting establishes109a for both root
cases, all cyclic histories and all three terminal ancestry trees. QED.

## Universal shell witness, with exact parity and small cases

Let G be finite connected BIPARTITE, n>=2, s any vertex, ell>=1, and U ANY
nonempty k-element subset of vertices at exact distance ell from s. Set

    H=2^ell,
    B=2^(ell-1)*(k+3),
    N=B-3,
    c=N e_s+sum_(u in U)e_u.

**Theorem109b.** c is an AS STACK loser of mass

    (2^(ell-1)+1)*k +3*2^(ell-1)-3.              (109b)

Proof. N>=1: its minimum is1 at ell1,k1. Define the ACTUAL graph valuation

    R(v)=2^dist(s,v)  if dist(s,v)<=ell;
         2^(ell-1)   if dist(s,v)>ell.

Every edge changes actual distance by exactly1 in a bipartite graph. Thus
all neighbor ratios lie between1/2 and2. At a U vertex EVERY neighbor is
at level ell-1 or ell+1 and has weight H/2. Vertices farther than ell exist
without difficulty: their constant lower weight keeps ALL their edges legal
for the valuation. One must NOT use the untruncated distance valuation and
assume level-ell vertices cannot fire outward.

Choose bipartition sign+ at s. Each U vertex has sign(-1)^ell. Since
B=2^(ell-1)(k+3)=(-1)^(ell-1)k modulo3,

    I(c)=N+(-1)^ell*k=0 modulo3.

If c STACKed, its positive output would therefore be divisible by3. The
known occupied-root three-removal operation normalizes the WHOLE input
history to an exact three-output history (n>=2 ensures a true neighbor).
Lemma109a would force N>=H*(k+3)/2=B, whereas N=B-3. Contradiction.
Every original singleton and source input is included; a failed schedule,
fixed-root demand or unattained real relaxation is not used. QED.

For ell1,k1 c is simply two adjacent singleton inputs, a stable AS loser;
there is no vanished source or t1 exception. Zero/one vertex graphs have no
eligible shell and are excluded. The bipartite and strict-peak hypotheses are
essential: same-level edges or unrestricted terminal1/2 invalidate this proof.

## Consequences for the actual universal target

For each source s and every nonempty shell at distance ell, take U to be
the ENTIRE shell of size k_s,ell. Formula109b is a certified AS lower bound
for L_AS(G), so any bipartite universal counterexample must have L_all
STRICTLY ABOVE every one of these bounds. This is a necessary restriction,
not an upper theorem for general configurations or a replacement for ASH*.

FanoInc14 has four vertices at distance3 from source0. Thus N25 plus those
four singleton line inputs has mass29 and is SYMBOLICALLY losing against
all roots. This matches65's independently certified exact L_AS29, providing
a short analytic lower alongside its full computational upper. Q4 shells
at3/4 have k4/1, giving AS lower masses29/30, respectively.

Shell data alone are still insufficient as an upper: the previously checked
eight-vertex A182 cyclic-buffer example has AS critical mass41. Its different
distance buffers cannot be replaced by one shell without further proof.
No universal combined ceiling is inferred. The outstanding obligation is
still to dominate EVERY arbitrary-buffer largest loser by some actual AS
loser on the SAME graph. S014 remains ACTIVE.
