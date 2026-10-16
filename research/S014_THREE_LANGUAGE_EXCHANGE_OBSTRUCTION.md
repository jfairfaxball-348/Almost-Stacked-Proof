# S014121: the all-odd THREE language is not a jump system

Universal ASH*-STACK remains OPEN. This is a symbolic obstruction to a
generic exchange/convexity shortcut, not a losing STACK configuration or
ASH* counterexample. No search or uninspected matching-factor theorem is
used. The proposed comparison must respect the mod3 charge sectors.

Use the path/star P3 with center0 and leaves1,2, edges01,02, and p=(1,1,1).
Let W_p={a>=0 : p+2a consumes into THREE}. Every positive input count in
this representation is ODD, so the all-odd restriction does not fix the
obstruction. The two fuel vectors

    a=(5,0,0), b=(2,3,0)

both belong to W_p and have the same total fuel5 (input mass13).
For a the input(11,1,1) consumes each leaf singleton via0->i,i->0 for i1,2,
leaving9 at0; twice use0->1,0->1,1->0 to leave3 at0. For b the input(5,7,1)
uses1->0 three times, leaving(8,1,1). Consume the two singleton leaves by
the same two cycles to leave6 at0, then one three-removal cycle leaves3.
All moves consume exactly2 and produce1; both histories have10 moves and
consume the entire input. No threshold is used to certify these positives.

Take the unit step s=-e_0 from a toward b, giving(4,0,0). The ONLY possible
second unit steps toward b give(3,0,0) or(4,1,0). Their actual inputs are

    (9,1,1), (7,1,1), (9,3,1), respectively.

With the bipartite charge I(c)=c_0-c_1-c_2 modulo3, these have charges1,2,2.
Every true move preserves this charge, whereas THREE at any root has charge0.
Thus none of these three fuel vectors belongs to W_p. The usual two-step
jump-system axiom fails. The fixed-total slice sum a=5 also fails ordinary
unit exchange: a_0>b_0 and the only deficit coordinate is1, but
a-e_0+e_1=(4,1,0) is absent. Hence no unproved M-convex base-set property
may be used to concentrate this THREE language.

SRC-0073: Norito Minamikawa, arXiv:2206.10439v1, Section2.1 p3's precise
(J-EXC) definition and inc(x,y) were inspected in the primary author paper
https://arxiv.org/pdf/2206.10439. Access STATEMENT_INSPECTED for that definition,
not the paper's algorithm proofs. Murota DOI10.1137/040618710 was inspected
only at its publisher abstract; matching/factor degree-sequence results are
not silently applied to these connected homomorphic ancestry trees. No PDF
is mirrored. The counterexample above is proved directly from the axiom.

All three negative THREE inputs nevertheless STACK (P3 threshold7 is earlier
work, not needed here). This distinction is essential: this disproves a
generic THREE-language exchange route, not B_odd or universal ASH*. A
different rescaled mod3-sector exchange remains a separate UNPROVED idea.
