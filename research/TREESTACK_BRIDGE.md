# Separate earlier theorem: TreeStack boundary and chronology

**Not a new target.** [TreeStack-Structural-Certificates-for-Stacking-on-Trees](https://github.com/jfairfaxball-348/TreeStack-Structural-Certificates-for-Stacking-on-Trees) reports the corrected nontrivial-tree result
`|V(T)|≥2 => stack(T)=estim(T)`, the exact rooted message theorem, the zero-score obstruction, and the arbitrary-defect upper certificate. It gives the checked Lean declaration:

```lean
TreeStack.stack_eq_estim_of_two_le_card :
  2 ≤ Fintype.card V → TreeStack.stack T = TreeStack.estim T
```

The project records the publicly posted paper [*The stacking number of a tree*, arXiv:2609.31811](https://arxiv.org/abs/2609.31811), v1 submitted 2026-09-25, and [Palomar PALOMAR-2026-09-25-000010 v1](https://palomar-registry.org/entry.html?id=PALOMAR-2026-09-25-000010&version=1). Its README and repository source listing were inspected during ASH S001; no new end-to-end compilation or Palomar registry audit was run.

The [Csernák–Soukup October 2026 ASH preprint](https://arxiv.org/abs/2610.09650) reports the tree estimator equality as conjectured unconditionally and deduces it under ASH. Because the TreeStack public release precedes the October paper's listed 2026-10-07 submission, this is a **notable public-record overlap**, **not a claim of copying, awareness, priority adjudication or a refutation**. Preserve courteous attribution; do not contact its authors without owner authorisation.

S002 shall perform an equation-by-equation source audit of both papers' `estim`, `stack`, threshold conventions, tree size restriction and revisions; check whether its exact named conjecture is indeed identical or needs a qualified comparison. Investigate whether the TreeStack branch-message or generalized-flow method yields an ASH proof for graphs with cycles, noting precisely which acyclic steps fail. No silent import of TreeStack Lean theorem into a general graph theorem, and no duplicate paper claim.
