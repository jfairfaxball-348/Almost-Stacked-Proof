module

public import Mathlib.Algebra.BigOperators.Fin
public import Mathlib.Combinatorics.SimpleGraph.Basic
public import Mathlib.Logic.Relation
public import Mathlib.Order.Bounds.Defs
public import Mathlib.Data.Fin.VecNotation
public import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
public import Mathlib.Combinatorics.SimpleGraph.Coloring.Vertex

/-!
# The critical Almost Stacked Hypothesis fails on a nine-vertex graph: statements

This file states, with deliberate `sorry`, the results proved in `Solution.lean` (through
`AlmostStacked/Main.lean`). It imports Mathlib only. The definitions below are repeated
verbatim from `AlmostStacked/Defs.lean`.

Sources: the Almost Stacked Hypothesis (October arXiv:2610.09650v1, Hypothesis 3.2 = April
arXiv:2604.22341v1, Hypothesis 9.1) in its critical (monotone) form ASH*, as reported by an
author to be the intended meaning; the definitions and conventions are those of
`research/ASH_SPEC.md` of this repository. The stacking threshold of trees, `stack(T) =
estim(T)`, is an earlier result (arXiv:2609.31811) and is not used here.

## What is claimed

`G9` is the graph on `Fin 9` with edges 0-3, 0-5, 0-6, 1-4, 1-7, 1-8, 2-6, 2-8, 3-5, 3-6,
4-7, 4-8, 5-7, 6-8 (graph6 `HCQTaXi`). It is connected and not bipartite. For both games
(stacking and clearing): every configuration of size at least `15` wins, the only losing
configurations of size `14` are `cStar = (0,0,1,0,0,5,0,8,0)` and its image, neither almost
stacked, and losing configurations exist in every size `2..14`, with an almost stacked one in
size `13`. Hence `stack(G9) = clear(G9) = 15` while every almost stacked configuration of every
size `≥ 14` is stackable and clearable: the critical hypothesis ASH* fails for `G9` in both
clauses, so neither clause holds for all finite connected (resp. connected non-bipartite)
graphs.
-/

@[expose] public section

namespace AlmostStacked

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- The size of a configuration: its total number of pebbles. -/
def size (c : V → ℕ) : ℕ := ∑ v, c v

/-- `Move G c d`: `d` arises from `c` by one pebbling move `u ⇒ v` along an edge `u v` of
`G`: two pebbles are removed from `u` (which must hold at least two) and one is added at
`v`. -/
def Move (G : SimpleGraph V) (c d : V → ℕ) : Prop :=
  ∃ u v, G.Adj u v ∧ 2 ≤ c u ∧
    d = Function.update (Function.update c u (c u - 2)) v (c v + 1)

/-- A configuration is stacked if exactly one vertex is occupied. -/
def IsStacked (c : V → ℕ) : Prop := ∃ v, ∀ w, c w ≠ 0 ↔ w = v

/-- `c` is stackable in `G`: some finite sequence of moves (possibly empty) reaches a stacked
configuration. -/
def Stackable (G : SimpleGraph V) (c : V → ℕ) : Prop :=
  ∃ d, Relation.ReflTransGen (Move G) c d ∧ IsStacked d

/-- `c` is clearable in `G`: some finite sequence of moves (possibly empty) reaches a
configuration of size exactly `1`. -/
def Clearable (G : SimpleGraph V) (c : V → ℕ) : Prop :=
  ∃ d, Relation.ReflTransGen (Move G) c d ∧ size d = 1

/-- `c` is almost stacked: some vertex `v₀` carries any number of pebbles and every other
vertex at most one. -/
def IsAlmostStacked (c : V → ℕ) : Prop := ∃ v₀, ∀ u, u ≠ v₀ → c u ≤ 1

/-- `t = stack(G)`: `t` is the least integer `t ≥ 2` such that every configuration of size
exactly `t` is stackable. -/
def IsStackNumber (G : SimpleGraph V) (t : ℕ) : Prop :=
  IsLeast {s | 2 ≤ s ∧ ∀ c : V → ℕ, size c = s → Stackable G c} t

/-- `t = clear(G)`: `t` is the least integer `t ≥ 2` such that every configuration of size
exactly `t` is clearable. -/
def IsClearNumber (G : SimpleGraph V) (t : ℕ) : Prop :=
  IsLeast {s | 2 ≤ s ∧ ∀ c : V → ℕ, size c = s → Clearable G c} t

/-- The critical (monotone) form ASH* of the stacking clause of the Almost Stacked
Hypothesis for `G`: `stack(G)` is the least `t₀ ≥ 2` such that every almost stacked
configuration of every size `s ≥ t₀` is stackable. -/
def ASHStarStack (G : SimpleGraph V) : Prop :=
  ∀ t, IsStackNumber G t →
    IsLeast {t₀ | 2 ≤ t₀ ∧ ∀ s, t₀ ≤ s → ∀ c : V → ℕ, size c = s → IsAlmostStacked c →
      Stackable G c} t

/-- The critical (monotone) form ASH* of the clearing clause of the Almost Stacked
Hypothesis for `G`: `clear(G)` is the least `t₀ ≥ 2` such that every almost stacked
configuration of every size `s ≥ t₀` is clearable. -/
def ASHStarClear (G : SimpleGraph V) : Prop :=
  ∀ t, IsClearNumber G t →
    IsLeast {t₀ | 2 ≤ t₀ ∧ ∀ s, t₀ ≤ s → ∀ c : V → ℕ, size c = s → IsAlmostStacked c →
      Clearable G c} t

/-- The edge list of the nine-vertex graph `G9` (graph6 `HCQTaXi`). -/
def g9Edges : List (ℕ × ℕ) :=
  [(0, 3), (0, 5), (0, 6), (1, 4), (1, 7), (1, 8), (2, 6), (2, 8), (3, 5), (3, 6), (4, 7),
    (4, 8), (5, 7), (6, 8)]

/-- The graph `G9` on `Fin 9` with the fourteen edges of `g9Edges`. -/
def G9 : SimpleGraph (Fin 9) :=
  SimpleGraph.fromRel fun a b => ((a : ℕ), (b : ℕ)) ∈ g9Edges

/-- The critical loser `c* = (0,0,1,0,0,5,0,8,0)`. -/
def cStar : Fin 9 → ℕ := ![0, 0, 1, 0, 0, 5, 0, 8, 0]

/-- Its image `(0,0,1,0,0,8,0,5,0)` under the automorphism `0↔1, 3↔4, 5↔7, 6↔8`. -/
def cStarImage : Fin 9 → ℕ := ![0, 0, 1, 0, 0, 8, 0, 5, 0]


/-! ## The graph -/

theorem G9_connected : G9.Connected := sorry

theorem G9_not_bipartite : ¬ G9.Colorable 2 := sorry

/-! ## Stacking -/

theorem G9_stack_14 (c : Fin 9 → ℕ) (hc : size c = 14) :
    ¬ Stackable G9 c ↔ c = cStar ∨ c = cStarImage := sorry

theorem cStar_not_AS : ¬ IsAlmostStacked cStar := sorry

theorem cStarImage_not_AS : ¬ IsAlmostStacked cStarImage := sorry

theorem G9_stack_large : ∀ s, 15 ≤ s → ∀ c : Fin 9 → ℕ, size c = s → Stackable G9 c := sorry

theorem G9_stack_losers : ∀ t, 2 ≤ t → t ≤ 14 → ∃ c : Fin 9 → ℕ, size c = t ∧ ¬ Stackable G9 c :=
  sorry

theorem G9_stackNumber : IsStackNumber G9 15 := sorry

theorem G9_stack_AS_threshold :
    IsLeast {t₀ | 2 ≤ t₀ ∧ ∀ s, t₀ ≤ s → ∀ c : Fin 9 → ℕ, size c = s → IsAlmostStacked c →
      Stackable G9 c} 14 := sorry

theorem G9_stack_Lall :
    IsGreatest {t | 2 ≤ t ∧ ∃ c : Fin 9 → ℕ, size c = t ∧ ¬ Stackable G9 c} 14 := sorry

theorem G9_stack_LAS :
    IsGreatest {t | 2 ≤ t ∧ ∃ c : Fin 9 → ℕ, size c = t ∧ IsAlmostStacked c ∧ ¬ Stackable G9 c}
      13 := sorry

theorem G9_not_ASHStarStack : ¬ ASHStarStack G9 := sorry

theorem not_forall_ASHStarStack :
    ¬ ∀ (n : ℕ) (G : SimpleGraph (Fin n)), 2 ≤ n → G.Connected → ASHStarStack G := sorry

/-! ## Clearing -/

theorem G9_clear_14 (c : Fin 9 → ℕ) (hc : size c = 14) :
    ¬ Clearable G9 c ↔ c = cStar ∨ c = cStarImage := sorry

theorem G9_clear_large : ∀ s, 15 ≤ s → ∀ c : Fin 9 → ℕ, size c = s → Clearable G9 c := sorry

theorem G9_clear_losers : ∀ t, 2 ≤ t → t ≤ 14 → ∃ c : Fin 9 → ℕ, size c = t ∧ ¬ Clearable G9 c :=
  sorry

theorem G9_clearNumber : IsClearNumber G9 15 := sorry

theorem G9_clear_AS_threshold :
    IsLeast {t₀ | 2 ≤ t₀ ∧ ∀ s, t₀ ≤ s → ∀ c : Fin 9 → ℕ, size c = s → IsAlmostStacked c →
      Clearable G9 c} 14 := sorry

theorem G9_clear_Lall :
    IsGreatest {t | 2 ≤ t ∧ ∃ c : Fin 9 → ℕ, size c = t ∧ ¬ Clearable G9 c} 14 := sorry

theorem G9_clear_LAS :
    IsGreatest {t | 2 ≤ t ∧ ∃ c : Fin 9 → ℕ, size c = t ∧ IsAlmostStacked c ∧ ¬ Clearable G9 c}
      13 := sorry

theorem G9_not_ASHStarClear : ¬ ASHStarClear G9 := sorry

theorem not_forall_ASHStarClear :
    ¬ ∀ (n : ℕ) (G : SimpleGraph (Fin n)), G.Connected → ¬ G.Colorable 2 → ASHStarClear G :=
  sorry

/-! ## General lemmas -/

/-- T1: clearable implies stackable. -/
theorem clearable_stackable {V : Type*} [Fintype V] [DecidableEq V] (G : SimpleGraph V)
    (c : V → ℕ) (h : Clearable G c) : Stackable G c := sorry

/-- Monotonicity above the order for stacking (October Lemma 4.7 / S003 Lemma 2). -/
theorem stackable_above {V : Type*} [Fintype V] [DecidableEq V] (G : SimpleGraph V)
    (hiso : ∀ u, ∃ v, G.Adj u v) (t : ℕ) (ht : Fintype.card V ≤ t)
    (h : ∀ c : V → ℕ, size c = t → Stackable G c) :
    ∀ s, t ≤ s → ∀ c : V → ℕ, size c = s → Stackable G c := sorry

/-- Monotonicity above the order for clearing (October Lemma 4.7 / S003 Lemma 2). -/
theorem clearable_above {V : Type*} [Fintype V] [DecidableEq V] (G : SimpleGraph V)
    (hiso : ∀ u, ∃ v, G.Adj u v) (t : ℕ) (ht : Fintype.card V ≤ t)
    (h : ∀ c : V → ℕ, size c = t → Clearable G c) :
    ∀ s, t ≤ s → ∀ c : V → ℕ, size c = s → Clearable G c := sorry

end AlmostStacked
