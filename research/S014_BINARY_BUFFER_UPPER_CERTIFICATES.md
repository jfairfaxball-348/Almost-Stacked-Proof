# S014105: positive-source binary-buffer ancestry upper certificates

Universal ASH*-STACK remains OPEN. This is a specialized SOUND certificate
scheme from the earlier exact S006/S009/S010 ancestry grammars, not a new
Parikh/TreeStack theorem or a claim that a producer is trustworthy. It checks
upper witnesses only. Failed or absent witnesses never certify a loser.

Fix connected G, source s, and a labeled set U of off-source vertices, each
with exactly one input. A tree certificate (U,q,N) consumes exactly N original
s inputs and every U singleton into one output at q. N can be zero ONLY for
the actual singleton tree U={q}; empty U with N0 is forbidden. A k-forest
certificate partitions the same complete inputs into k actual trees all
rooted at q, and consumes them into exactly kq. Below positive-source tree
labels have N>=1. Source-zero singleton trees remain SEPARATE objects.

Let P(q)=2^dist(s,q). A pure tree (empty U,q,P(q)) is realized by grouping
source pebbles and repeated pair moves along a shortest path. At q=s it is
the single actual source input. This is the earlier known distance witness.

The following certificate nodes are sound, retaining ALL input occurrences:

* **Tree split.** Proper disjoint nonempty A,B partition U. Two tree children
  at u, costs N_A,N_B, produce one output at q whenever u~q. Cost is their
  sum, which must be positive. Either child may be the SEPARATE zero-source
  singleton when its entire buffer is exactly{u}. Both cannot have source0
  because the two nonempty buffers are disjoint.
* **Pure sibling.** A positive-source tree for the SAME U at u, plus the pure
  P(u) source tree at u, merges along u~q. Cost N_child+P(u). This recurrence
  is well founded when child source cost is strictly smaller than the parent.
* **Zero singleton sibling.** For U={u}, its original singleton and a pure
  P(u) source tree merge along u~q, cost P(u)>0.
* **Two forest.** Concatenate two same-root trees with disjoint buffer parts,
  including a pure empty-buffer tree. Total source cost is positive. These
  are TWO terminal trees; no extra consuming move between them is invented.
* **Three forest.** Concatenate one tree and one two-forest at the SAME root,
  with disjoint buffer parts. Empty parts are genuine pure forests with
  costs P(q) or2P(q), never empty objects. Total source cost is positive.

Proof of soundness is simultaneous induction on buffer mask (proper masks
are smaller), then source cost for within-mask tree steps, then terminal
forest size. Execute the child histories on designated disjoint original
input groups, retaining other groups untouched. All child outputs and their
last merge are true graph moves. Forest concatenation preserves every output
at one root. Thus every node supplies an actual complete legal history,
including cyclic label repetitions and collisions of geometric paths.
Strict within-mask cost descent forbids cyclic evidence pointers. A local
checker must verify that descent and exact child costs, not merely equations.

For any checked positive-cost node N0 and desired source N>=N0 with
N-N0 divisible by3, erase triples at s while retaining the POSITIVE base N0,
then execute its whole-input witness. No rule erases down to a zero source.
Hence one verified one-/two-/three-forest node per residue, whose cost is at
most the desired N, certifies each positive-source AS input. These certificates
need not be minimal. Checking every proper-partition minimum or a native
optimizer is unnecessary for upper soundness. An unattained smaller label or
a cost above N supplies NO impossibility result.

On Q4 source0, store all32768 masks and16 roots for three positive types,
with uint32 costs and explicit split/neighbor provenance. Each mask has at
most48 nodes; proper split masks and within-mask strict cost descent make
an independent inductive replay finite. All16 XOR source maps are separately
verified. Complete witnesses at masses31/32/33 would prove the full AS upper
by90, and100's antipodal loser30 would make L_AS=30. A partial table, cap,
or missing upper witness leaves that statement UNKNOWN. CAM58 implements
this SOUND positive scheme; no producer optimality or universal cube formula
is promoted. S014 stays ACTIVE; general inputs still need separate work.
