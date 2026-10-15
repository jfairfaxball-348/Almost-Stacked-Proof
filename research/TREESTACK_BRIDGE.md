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


## S002 checked comparison
April arXiv:2604.22341v1 PDF p26 formula `sigma_T(r)=1+sum_{v=r OR deg(v)>1}deg(v)2^dist(r,v)` and `estim(T)=max_r(sigma_T(r)+leaf_T(r))` is exactly represented in `TreeStack/Estimator.lean` including root of degree one. Theorem `TreeStack.stack_eq_estim_of_two_le_card` in `TreeStack/Stacking.lean` uses least exact t≥2 and |V|≥2. `RootScore.lean`, `UpperBound.lean`, and `notes/defect-flow.md` inspected; no new Lean compilation. October full source not obtained, so equation-level comparison with *October* is still open. Its abstract's tree-conjecture restatement postdates the September 25 TreeStack publication, which proves the earlier source formula but NOT universal ASH. No attribution wrongdoing asserted.

## S003 checked comparison (October full text)
- October Def. 5.1 estim(T) = max{2, 1+max_r(ρ_T(r)+leaf_T(r))}, where ρ = σ−1. For |V|≥2 this is identical to the April formula and to `TreeStack/Estimator.lean`. October adds stack(K1)=2=estim(K1).
- October Conjecture 5.6 (stack(T)=estim(T) for finite trees) is the earlier TreeStack theorem for |V|≥2; the October paper does not cite arXiv:2609.31811. No inference about awareness or priority is made, and no contact.
- S003 consequence (credits TreeStack): with October Thm 5.2's almost-stacked witness of size estim−1 (proof checked in S003), the TreeStack theorem yields the **critical form ASH\* for every tree** (S003 Thm 8).
- The **printed** pointwise hypothesis fails on most trees: P4 is the smallest graph, and 77 of the 88 completed trees with n≤9 fail it. The TreeStack theorem itself is unaffected.
- No TreeStack Lean build was re-run in S003.

## S009 current primary refresh

arXiv2609.31811 now lists v1/v2. Currentv2 digest79f1d8e4ea707206e72fce3e43fabcf8803376987f6b4da6d5fa9b5a16b4b720,13pages, branch flux/scheduling/defect proof inspected. Nontrivial-tree equality and registered package are earlier work; no new build or registry audit. EMPTY versus zero, positive-before-debt tasks and ambient cancellation are explicitly attributed in S009. No universal ASH* inference.

## S010 boundary

Currentv2 unchanged; earlier nontrivial-tree equality/registered package credited, no build/registration. Generic grammar/ancestry primitives attributed; exact cyclic cancellation/selected-cost equivalence scoped/unresolved, no rediscovery or universal substitution.

## S011 boundary

TreeStack currentv2 digest unchanged and earlier nontrivial-tree equality/registered package credited; no Lean/registry build. Known exact ancestry/scheduling/last-move/+3 primitives remain prior. S011 exact terminal/cyclic transport is not a new tree estimator or universal ASH* proof. Precise equivalence uncertainty remains in the S011 primary report.

## S012 boundary

Earlier TreeStack2609.31811v2/registered package remains credited; selected current PDF digest unchanged, no new Lean/registry build.59-62 concern exact general-graph input language consequences and CLEAR restrictions, not a rediscovered tree estimator or universal ASH* proof. Precise equivalence uncertainty retained in S012 primary comparison.

## S013 boundary

Earlier TreeStack2609.31811v2 and registered package remain credited, selected current digest unchanged; no build/registry action.63-70 concern exact general-graph loss concentration/extremizers, not tree-estimator rediscovery or universal ASH* proof. Known scheduling/+3/homomorphism primitives attributed; exact equivalence/novelty uncertain.
