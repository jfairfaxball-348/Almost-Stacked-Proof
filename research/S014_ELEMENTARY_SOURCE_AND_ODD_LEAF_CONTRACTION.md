# S014118-120: independent source proof and odd-leaf contraction

Universal ASH*-STACK remains OPEN.118 independently proves116 using only
legal histories.119-120 use the already proved exact boundary trees111-113.
These are scoped whole-input results, not a new TreeStack theorem or an
independent human/kernel/priority audit. Frozen earlier files are unchanged.

## 118. An elementary source interchange proof and scheduling consequence

Take a winning history of a multioccupied d, and prescribe heavy w. If w
ever fires, commute its FIRST firing w->u to the beginning. All earlier
moves had sources different from w, and so remain legal: the early firing
decreases only w and increases u. None of those earlier sources is made
smaller. At the old position of the selected firing, omit it. The resulting
configuration equals the old history at that point, so the rest is valid
with exactly the same whole terminal pile. No move consumes an unused input.

If w never fires, its initially positive pile persists, so the terminal
root is w. Let its final size be k. Since d was multioccupied and d_w>=2,
k>=3. For k>=4, choose ANY neighbor u and fire w->u first. Simulate the
old history keeping that one new u pebble untouched; no original move has
source w. This leaves (k-2)e_w+e_u. The two true moves w->u then u->w leave
the positive pile (k-3)e_w, so this first source is also winning.

For k3, necessarily d_w2 and exactly ONE pebble arrives at w from all other
inputs. There is exactly one incoming w move, and it is the final move
z->w, z~w; otherwise a remaining off-w pebble would require another arrival.
Fire w->z first, then simulate the OLD prefix before its final move while
retaining the new z pebble. That prefix consumes all other inputs into2e_z,
so it now leaves3e_z and no pebbles elsewhere. This is a winning first move
at the prescribed w. Initial pure3 at w is the excluded one-site exception.
These cases independently prove116 without canonicalization or cancellation.

Consequently ANY adaptive policy that selects a heavy SOURCE while the
current configuration is not stacked admits destination choices that win
from every STACK-winning initial configuration.116 preserves winning after
each selected source; total mass decreases1 each step, so a nonstacked
stable state cannot be reached (it would lose). At most |d|-1 moves occur.
The policy must STOP upon reaching a pile; forcing pure3 to fire would fail.
This is an exact source-scheduling theorem, not arbitrary destination safety
or the missing mass-preserving AS concentration.

## 119. Odd graph-leaf contraction

Let w be a graph leaf, v its unique neighbor. Let x_w be ODD and x_v>=1.
If x has a THREE tree, then so does x-e_w-e_v.                      (119a)

Proof. The isolated mass3 tree cannot be this multioccupied x. Normalize by
112. Its unique degree2 w-marker has two DISTINCT v-labeled neighbors y,z.
If deg(y)+deg(z)<=5, contract the path y-w-z by identifying y,z and deleting
that w-marker. The result is a tree; the merged degree is deg(y)+deg(z)-2
and at most3. Its aggregate v boundary decreases1, and its w boundary
decreases1. All other labels and edges remain true. This includes a merged
isolated vertex of degree0, contributing3 rather than an empty tree.

If y,z both have degree3, x_v>=1 supplies some v-copy t of degree1 or2.
It is neither y nor z. Deleting the w-marker separates the y and z sides;
suppose t lies on the y side. At z choose an edge NOT toward the w-marker,
detach that branch and attach it to t instead. The detached component
contains neither t nor the marker, so this is a tree. Labels z=t=v make
the edge true. z becomes degree2 and t degree2 or3; total v boundary is
unchanged. The marker path can now be contracted as in the first case.
No requirement of canonicality after this operation is imposed. Other
w-copies (possible leaves/branches) stay in the tree and retain their
boundary.111 gives precisely x-e_w-e_v. QED.

If |x|>=3, the same implication holds for unrestricted STACK: by113 use
T(x) or T(x+2e_q); padding preserves the odd w-marker and positive v
boundary.119a gives T(x-e_w-e_v) or T(x-e_w-e_v+2e_q). The unpadded child is
nonempty, so113 applies. If x_v>=2, the converse is legal: v->w then w->v
produces exactly x-e_w-e_v. Therefore

    x_w odd>=1, x_v>=2: STACK(x) iff STACK(x-e_w-e_v).       (119b)

It is false to assert the converse with x_v1: three stable singleton inputs
can lose while their one-pebble remainder wins. Keep the parent>=2 gate.
No small or zero-input case is inferred by cancellation.

## 120. Any even heavy graph-leaf loser has a larger loser

For ANY connected simple G,n>=2, ANY STACK loser c, and ANY graph leaf w
with c_w=2a>=2,

    c+3e_w is also a STACK loser.                         (120a)

Proof.117's safe leaf-pair reduction sends c to a loser b with b_w0 and
b_v=c_v+a. The pure3 exception is impossible since c_w is even and c loses.
Now d=c+3e_w has leaf count2a+3.117's a+1 pair moves send d to z, where
z_w1 and z_v=c_v+a+1>=2. By119b, z has the same STACK status as
z-e_w-e_v=b. Hence d loses. All other input coordinates are retained;
the larger input is never the exceptional pure3 (c had multiple sites).
This proof does not delete a graph vertex or assume a threshold relation
between different graphs. QED.

Thus EVERY actual critical STACK loser on EVERY connected simple graph has
each graph-leaf coordinate either zero or ODD. Together with117c, at n>=3
all neighbors of graph leaves have zero coordinates. These are universal
critical restrictions, valid also on nonbipartite graphs, not absence of
all even heavy vertices in a graph core. The two-vertex critical input(1,1)
obeys the leaf-odd conclusion; the parent-zero restriction has its stated
K2 exception. No claim for zero/one vertex conventions is introduced.

This identifies an actual new ascent, rather than reviving the generic
some-neighbor ascent refuted by76. No universal AS selection follows: core
vertices and arbitrary buffers still require the same-graph comparison.
S014 stays ACTIVE; no closeout, later session or phase advancement.
