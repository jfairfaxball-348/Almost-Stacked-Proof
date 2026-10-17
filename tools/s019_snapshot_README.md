# The critical Almost Stacked Hypothesis fails on a nine-vertex graph (Lean 4)

This repository snapshot is a self-contained Lean 4 project (Lean `leanprover/lean4:v4.35.0`, Mathlib tag `v4.35.0`) prepared for the Palomar registry. It proves that the critical (monotone) form of the Almost Stacked Hypothesis (T. Csernák and L. Soukup, arXiv:2610.09650, Hypothesis 3.2; arXiv:2604.22341, Hypothesis 9.1) fails in both of its clauses, stacking and clearing.

## What is proved

For the graph `G9` on nine vertices (graph6 `HCQTaXi`; edges 0-3, 0-5, 0-6, 1-4, 1-7, 1-8, 2-6, 2-8, 3-5, 3-6, 4-7, 4-8, 5-7, 6-8), which is connected and not bipartite:

- `stack(G9) = clear(G9) = 15`;
- the only non-stackable (and the only non-clearable) configurations of size 14 are `(0,0,1,0,0,5,0,8,0)` and its automorphic image, neither of which is almost stacked;
- every almost stacked configuration of every size at least 14 is stackable and clearable;
- hence the critical hypothesis fails for `G9`, so neither clause holds for all finite connected (respectively connected non-bipartite) graphs.

General lemmas (clearable implies stackable; monotonicity above the order) are also proved. The statements are in `Challenge.lean` (the 25 names in `comparator.json`); `Solution.lean` exports the proofs from `AlmostStacked/`.

## How

`AlmostStacked/Checker.lean` defines a Boolean exact losing-layer checker and proves it sound and complete (`layer_step`). The certificate data in `AlmostStacked/Data/` (claimed losing layers of sizes 2..15, untrusted) are checked by kernel evaluation (`decide +kernel`) in `AlmostStacked/G9/Check*.lean`, one layer per module. The check modules, and separately the data modules, are each chained by imports, so a plain `lake build` evaluates one heavy layer check at a time (each needs up to about 10 GB of memory; a full build takes about 13 minutes on an 8-core laptop). No `sorry` outside `Challenge.lean`, no `native_decide`, no custom axioms; the compared theorems use only `propext`, `Classical.choice` and `Quot.sound`.

## Build

```
lake exe cache get
lake build
```

## Provenance

The research record (computations, independent cold re-checks, certificate generator `tools/s017_gen_layers.py`, assurance runs) is in https://github.com/jfairfaxball-348/Almost-Stacked-Proof; this snapshot's Lean files are byte-identical copies of its `formal/` directory at the commit named in that repository's session S019 record. An earlier, separate result, the stacking number of trees (arXiv:2609.31811), is credited prior work and is not used here.

Licence: Apache-2.0 (`LICENSE`).
