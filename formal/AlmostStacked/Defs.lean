module

public import Mathlib.Algebra.BigOperators.Fin
public import Mathlib.Combinatorics.SimpleGraph.Basic
public import Mathlib.Logic.Relation
public import Mathlib.Order.Bounds.Defs
public import Mathlib.Data.Fin.VecNotation

/-!
# The pebbling model (definitions only)

These definitions are repeated verbatim in `Challenge.lean`; the Solution proves the
statements about the definitions of this module. Conventions follow `research/ASH_SPEC.md`:

* a configuration on a finite vertex type `V` is a function `c : V → ℕ`, of size
  `∑ v, c v`;
* a move `u ⇒ v` along an edge needs `c u ≥ 2` and replaces `c u` by `c u - 2` and `c v`
  by `c v + 1`;
* `c` is *stackable* if a sequence of moves reaches a configuration with exactly one
  occupied vertex, and *clearable* if it reaches a configuration of total size exactly `1`;
* `stack(G)` (resp. `clear(G)`) is the least `t ≥ 2` such that every configuration of size
  exactly `t` is stackable (resp. clearable);
* `c` is *almost stacked* if some vertex `v₀` has `c u ≤ 1` for every `u ≠ v₀`.
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

end AlmostStacked
