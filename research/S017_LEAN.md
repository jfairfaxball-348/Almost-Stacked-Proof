# S017: Lean formalisation of the G9 counterexamples (both clauses of critical ASH*)

Status: Lean 4 / Mathlib development in `formal/`, built locally with the kernel (no `sorry`, no `native_decide`, standard axioms only). This is Phase 3 WORK, owner-authorised before the Phase 2 novelty audit; Phase 3 is NOT passed: no Comparator run, no independent-kernel check (a same-kernel `leanchecker` replay passed), no fresh-session cold re-check of the Lean development, no hosted Lean CI, no submission. Records: `sessions/S017/LEAN_RECORD.md`, `formal/README.md`, `formal/FROZEN_MODULES.md`.

## 1. Statements (formal/Challenge.lean)

Definitions (`AlmostStacked/Defs.lean`, repeated verbatim in the Challenge): configurations `V → ℕ` on a finite type, `size`, `Move` (u ⇒ v along an edge, `c u ≥ 2`), `IsStacked` (exactly one occupied vertex), `Stackable`/`Clearable` (reflexive-transitive closure of `Move` reaches a stacked configuration / a configuration of size exactly 1), `IsAlmostStacked` (some `v₀` with `c u ≤ 1` for all `u ≠ v₀`), `IsStackNumber G t` / `IsClearNumber G t` (`t` is the least `t ≥ 2` such that every configuration of size exactly `t` wins: Mathlib `IsLeast`), `ASHStarStack G` / `ASHStarClear G` (for the stacking/clearing number `t`, `t` is also the least `t₀ ≥ 2` such that every almost stacked configuration of every size `≥ t₀` wins), `G9` on `Fin 9` via `SimpleGraph.fromRel` of the 14-edge list, `cStar`, `cStarImage`.

Theorems (25): `G9_connected`; `G9_not_bipartite` (`¬ G9.Colorable 2`); for STACK and CLEAR separately: the size-14 characterisation (K1/K1c), `cStar_not_AS`, `cStarImage_not_AS`, all sizes `≥ 15` win (K2/K2c), losers in every size 2..14 (K4/K4c), `IsStackNumber G9 15` / `IsClearNumber G9 15`, the almost-stacked threshold is 14 (`IsLeast`, which contains K3/K3c and the AS loser of size 13), `L_all = 14` and `L_AS = 13` (`IsGreatest`), `¬ ASHStarStack G9` / `¬ ASHStarClear G9`, and the universal negations `¬ ∀ n (G : SimpleGraph (Fin n)), 2 ≤ n → G.Connected → ASHStarStack G` and `¬ ∀ n G, G.Connected → ¬ G.Colorable 2 → ASHStarClear G`; general lemmas `clearable_stackable` (T1), `stackable_above`, `clearable_above` (monotonicity above the order, October Lemma 4.7 / S003 Lemma 2, for graphs without isolated vertices).

Convention check: `t ≥ 2` is built into both thresholds; sizes are exact (`size c = t`), not "at least"; the zero configuration and size 1 never enter the thresholds; the bipartite exclusion appears as the hypothesis `¬ G.Colorable 2` of the CLEAR universal statement; STACK uses `2 ≤ n` (n = 9 for G9). The universal statements quantify over graphs on `Fin n`, which represent every finite graph up to isomorphism. These match research/ASH_SPEC.md (critical form) and the S003 conventions.

## 2. Proof architecture

- `Basic`: `Wins G P c` (generic reachability of a goal), the one-step characterisation `wins_iff`, `size_of_move`, `isStacked_iff` (stacked iff one vertex carries the whole nonzero size), T1, pigeonhole and monotonicity above the order.
- `Encode`: `enc c = Σ c_i 32^i`; for size < 32 each `c_i` is the i-th base-32 digit (`dig_enc`), `enc` is injective, `mass (enc c) = size c`, a move changes the code by `+32^v − 2·32^u` (`enc_move`), and 0/1 configurations are enumerated by `zeroOne`.
- `KTree`: binary search trees with recursor-defined `mem`, `all`, `ordered`; search correctness on ordered trees.
- `Checker`: Boolean `layerB` = order ∧ soundness ∧ candidate completeness (C5) ∧ terminal 0/1 configurations; `layer_step` proves exactness of layer `t` from exactness of layer `t − 1` (induction step of C4); `layer_one` is the base (size 1 always wins).
- `Data/` (generated, untrusted): claimed losing layers of masses 2..15 for each game; `G9/Check*` evaluate `layerB` with `decide +kernel`, one module per layer; `G9/*Layers` chain the 14 steps.
- `Main`: the statements above from the exact layers 13, 14, 15, explicit witnesses for sizes 2..12, and `wins_above` for sizes > 15.

No step uses the S015 human proof; the non-stackability of `cStar` comes from the kernel-checked layers. The CLEAR clause is obtained independently of the STACK layers (its own certificate), so T1 is stated and proved but not needed for the G9 results.

## 3. Assurance and limits

- Trusted: Lean 4.35.0 kernel, Mathlib v4.35.0 (Challenge imports only Mathlib), the three standard axioms. The certificate data and its generator are NOT trusted.
- Done: `leanchecker` replay of all 67 non-root modules, 67/67 OK (same kernel implementation). Not yet done (S018): Comparator run against `comparator.json`; an independent-kernel check (the toolchain ships `lean4lean`, `leanexport` and `nanoda_bin`); hosted Lean CI; independent fresh-session review of the Challenge statements; `formalization.yaml`. A local stand-in (`tools/s017_challenge_bridge.py`) checks that the Challenge definitions are byte-identical to `Defs.lean` and that every Challenge statement is closed by the Solution theorem of the same name.
- Scope: one graph, G9. Nothing here proves or claims `L_all(G) <= L_AS(G)` for any graph class; the universal positive hypothesis is refuted, not restricted.
- Credit: TreeStack (arXiv:2609.31811, registered package) is earlier, separate work on trees and is not used.
