# S014100: exact all-root one-bit STACK conductors on bipartite graphs

Universal ASH*-STACK remains OPEN. This is a complete scoped argument using
the credited ancestry, pure distance lower bound, signed invariant and
occupied-source +3 operation (S005/S006/S010 and original source attribution).
It repairs the precise BIPARTITE restriction missing from S005's refuted
distance-only proposal. No priority, independent human or kernel claim.

Let G be finite connected bipartite simple, s!=t, d=dist(s,t)>=1. A move
consumes TWO at a vertex and creates ONE at a neighbor. For N>=1 put
x=N e_s+e_t. Define A=2^d, B=3*2^(d-1), C=2^(d+1), and a=(-1)^d mod3.

**Theorem100.** For unrestricted final positive pile and unrestricted root,
x STACKs EXACTLY in the following cases:

| Source residue | Necessary and sufficient lower cutoff |
|---|---|
| N=a (mod3) | N>=A |
| N=0 (mod3) | N>=B |
| N=-a (mod3) | N>=C |

The table concerns POSITIVE N. N=0 is a separate initially stacked singleton
at t. No zero-source +3 reduction or zero-output cancellation is used.

## Ancestry lower bounds for every chronology, root and pile

A pure-source ancestry tree producing one pebble at v uses at least
2^dist(s,v) source leaves. At a last move u->v its TWO child subtrees each
end at u; induction and dist(s,u)>=dist(s,v)-1 prove the bound. A source
leaf is at s and has cost1, including zero-length pure histories.

Normalize any winning whole-input pile to k=1,2 or3 by the known positive
three-removal operation. This remains a complete legal forest on ALL original
inputs. Exactly ONE final ancestry tree contains the unique original t
pebble. Its marked leaf-to-root WALK is v_0=t,...,v_l=q. Its sibling trees
at v_i (0<=i<l) are all pure-source trees. The remaining k-1 final trees at
q are pure-source too. These disjoint trees partition EVERY source input,
so, with j_i=dist(s,v_i) and h=dist(s,q),

    N >= sum_{i<l} 2^j_i + (k-1)*2^h.                 (1)

Repeated labels/walk vertices do not identify leaves or invalidate this sum.
If l>=1 its first sibling alone costs A. If l=0 and N>0, some other final
tree must exist and costs A. Thus EVERY positive winning N is at least A.
This proves the first row's necessary bound, without imposing a root.

Choose bipartition sign+ at s; then sign(t)=a. The conserved signed residue
of x is N+a, and that of the normalized output is k*sign(q).

If N=-a modulo3, this residue is zero, forcing k=3. Every actual arc along
the walk satisfies j_(i+1)>=j_i-1, hence

    2^j_i >= 2^(j_i+1)-2^(j_(i+1)+1).

Summing telescopes to sum 2^j_i >=2^(d+1)-2^(h+1).
In (1), the two additional pure trees cost at least2*2^h, so N>=C.
This covers l=0 and every choice of q as well. No lower bound on distance
along the marked walk is substituted for the actual graph distance.

If N=0 modulo3, the output residue is a, so k is1 or2.
For k1, q is in t's part. The marked walk has EVEN length; length0 would
give N0 because there are no other final trees. Thus l>=2, whose first two
siblings cost at least2^d+2^(d-1)=B. For k2, q lies in the OPPOSITE part,
so l is odd. If l>=3 the same first-two bound suffices. If l1, (1) includes
the first sibling at t and an additional pure final tree at its neighbor q,
whose distance from s is at least d-1. Again N>=B. This proves the middle
row, including d1 and all possible normalized final roots. Signed parity
is used only where the graph is actually bipartite.

## Matching legal constructions and the unbounded tail

Fix a shortest s-to-t path, with penultimate vertex u at distance d-1.
Designated disjoint groups of 2^dist(s,v) source inputs produce one pebble
at v by repeated pair moves along their path. Overlap of graph vertices is
harmless: execute on the designated tokens, leaving other tokens untouched.

At N=A produce ONE new pebble at t from all source inputs; it joins the
original t singleton to give exactly2 at t.

At N=B partition the source inputs into groups A and2^(d-1). Produce one
pebble at t and one at u, preserving the original singleton at t. Move the
resulting pair t->u. The exact final pile is2 at u and no other input remains.
For d1 the second group is the one reserved original s pebble; u=s is valid.

At N=C produce TWO new pebbles at t, each using A source inputs. Together
with the original t singleton they give exactly3 at t.

These counts have the residues in the table, since A=a, B0, C=-a modulo3.
For any larger N in the same row, erase successive triples at the occupied
source s, retaining its positive base A/B/C, then execute the relevant
construction. Each erased triple is consumed by the known three-move
operation at a true neighbor; no surplus input is ignored. This proves every
sufficiency assertion at unbounded N. QED.

## Exact universal use and its remaining limit

The largest losing source count is C-3. The other two rows have smaller
last losers (or none positive), because C>=B>=A and d>=1. Thus

    max{N+1 : N>=1, N e_s+e_t loses}=2^(d+1)-2.

For d1 this is the two-singleton loser; the input is still AS, with no heavy
site. Taking diametral s,t gives the universal bipartite AS lower

    L_AS(G)>=2^(diam(G)+1)-2,
    stack(G)>=2^(diam(G)+1)-1.

Together with the earlier all-ones and independent-set AS witnesses, EVERY
bipartite ASH* counterexample must have

    stack(G)>max(n+1,3*alpha(G)+1,2^(diam(G)+1)-1)

when alpha>=2 (K2 separately has stack3). This is a necessary restriction,
not the missing upper inequality. A proof that the displayed maximum always
equals stack would be FALSE on trees with more elaborate branching; no such
upper is claimed. Earlier TreeStack arXiv:2609.31811/registered package and
the source tree estimator remain credited and are not rediscovered here.

The nonbipartite S005 counterexample remains valid: its same-level detour
changes the signed-residue argument and defeats that unrestricted statement.
No extension to nonbipartite graphs or arbitrary binary buffers is inferred.
CAM52 is a separately preregistered bounded challenge, not this proof.
S014 remains ACTIVE; universal comparison and human/kernel review are open.
