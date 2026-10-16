# S014111: exact trivalent boundary trees and a remaining bipartite comparison

Universal ASH*-STACK remains OPEN.111 is an exact reformulation and gluing
lemma from the credited whole-input ancestry/THREE transport, not an extremal
selection proof. It does NOT use the earlier TreeStack equality on a new
graph. The tree below is an ancestry object with REPEATED graph labels;
it is not a subtree/retract/quotient of G. No priority/human/kernel claim.

## Exact boundary characterization

For finite simple G and nonnegative input c of mass M>=3, c can consume into
EXACTLY THREE at some vertex iff there is a nonempty finite tree H, maximum
degree<=3, with a TRUE graph homomorphism f:H->G and

    c_v=sum_(x in H: f(x)=v) (3-deg_H(x)).                (111a)

Necessarily |H|=M-2. All copies, including copies with zero contribution,
are retained. For a one-vertex H, degree0 contributes3, not a discarded
empty tree. Adjacent copies may not have equal labels in a loopless G.

Proof from a history. Its consuming forest has three roots at q. Each move
is a binary merge at its source u, followed by its output edge u->v.
Introduce one central vertex labeled q and attach the three ancestry trees.
Represent every merge by a vertex labeled its SOURCE; an edge to its parent
merge/central vertex joins adjacent labels because its output was consumed
there. An original input leaf joins its next merge at its OWN label, or
joins the central vertex directly for a zero-move terminal pebble. Every
merge vertex and the central vertex has degree3 in this unrooted full tree.
Remove ONLY original input leaves. The remaining internal tree H has
M-3 merge vertices and one central vertex. A vertex loses exactly3-deg_H(x)
original leaves, all carrying f(x), proving111a and |H|=M-2.

Conversely attach3-deg_H(x) distinct original leaf inputs of label f(x) to
each H vertex. Choose ANY H vertex as central. Away from it each vertex
has exactly two descendant ports (H branches or attached inputs). Evaluate
these two subtrees into two pebbles at its own graph label and move them
along the true edge to its parent's label. Disjoint designated inputs make
every postorder move legal even with repeated graph labels. The central
vertex receives/retains exactly three pebbles, consuming ALL original inputs.
This also reproves the already known THREE rerooting at every used label.
Finally sum111a:3|H|-2(|H|-1)=|H|+2=M. QED.

On bipartite G, nonempty signed-zero c STACKs iff it has such an H: any
stacked output has positive size divisible3 and normalizes to3 by the known
occupied-root three-removal. For M<3 a nonempty signed-zero input consists
of two opposite-part singleton pebbles and loses; no empty H is admitted.
Nonzero signed inputs may STACK into1/2 and are outside this equivalence.

## A genuine whole-input gluing consequence

If a and b each have THREE witnesses, a_u>=1, b_v>=1 and u~v in G, then

    a+b-e_u-e_v -> THREE somewhere.                      (111b)

Choose one actual leaf port labeled u in H_a and one labeled v in H_b.
Delete those two INPUT leaves and join their incident internal vertices
by the new true u-v edge. The two internal trees form one tree, maximum
degree remains3, and111a's boundary becomes exactly the displayed input.
Postorder gives a legal consuming certificate for it. This retains all
other inputs; it neither glues independent roots without an edge nor
deduces that a common losing child makes either parent lose.

For bipartite signs+, -, write C_+,C_- for original input totals and A_+,
A_- for numbers of H vertices in the two parts. Every internal edge crosses
parts, so111a gives C_+=3A_+-(M-3), C_-=3A_--(M-3). These are necessary
EXACT integer color counts; they do not ensure a tree with those labels.
For |H|>=2, parity(c_v) is the parity of the NUMBER of degree2 H vertices
labeled v (degree1 contributes2, degree3 contributes0). Degree2 vertices
can repeat labels; replacing them by one binary vertex is NOT proved.

## The precise remaining selection question

CAM72 rechecks ALL638 existing critical graph cases, filters48 bipartite
cases independently, and tests every source for ALL14814 non-AS critical
inputs,203673 candidates. Every one has a same-mass same-parity AS loser,
even at some initially heavy receiver. This is bounded evidence only.
The old all-graph assertion stays FALSE on nonbipartite G0/G1 by17/18.

For bipartite c=p+2a with p binary, concentrating all pair fuel at q yields
d=p+2|a|e_q. If c has signed zero, a necessary condition for d to be a
critical loser is a_- divisible3 when q is positive-part, or a_+ divisible3
when q is negative-part. This follows by subtracting the signed invariants:
I(d)-I(c)=4a_- or -4a_+, respectively. No universal critical divisibility
theorem follows just from72's finite memberships.

An unconditional fixed-parity rule is false even in bipartite graphs:
(2,0,0,2) on P4 loses, but every same-parity AS input is already a single
pile and hence wins at ANY positive mass. Thus critical oddness and/or a
valid parity change cannot be omitted. Critical bipartite odd-heavy remains
UNPROVED. A narrower prospective hypothesis B_odd is: any signed-zero
bipartite loser with ALL positive coordinates ODD and>=2 heavy sites has a
same-parity AS loser at one of masses M,M+2,M+4. It is UNPROVED and selected
after the failures above. If true together with critical bipartite oddness,
it would imply bipartite ASH*: the critical application permits only mass M.
It would still leave nonbipartite ASH* open. CAM73 tests this before proof work.

The hard step is now explicit in111a: make actual same-graph boundary
nonrepresentability concentrate at one label WITHOUT dropping leaf ports,
changing mass downward, identifying graph labels, or assuming a missing
tree from a failed construction.111b supplies positive constructions only;
it does not prove the required maximum-hole comparison.

## Primary-source cross-check for the algebraic lead

SRC-0070: Elduque-Labra, Evolution algebras and graphs, arXiv:1312.4685v1,
Definition2.1/2.2 and Theorem3.4 proof pp2,6-7 inspected through the primary
PDF (https://arxiv.org/pdf/1312.4685); no PDF mirrored. The standard algebra
e_i e_j=0 for i!=j and e_i^2=sum_(j~i)e_j encodes a consuming ONE tree by
positivity over rationals. Its no-directed-cycle nilpotency theorem concerns
all algebra elements/products, and does not supply a largest missing input
comparison; every nontrivial undirected graph has directed2-cycles anyway.
The elementary ancestry correspondence does not claim a new evolution
algebra.111's full boundary proof above is local, and this literature lead
does not establish ASH* or a novelty verdict. Continue S014, no closeout.
