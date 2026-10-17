module

public import AlmostStacked.Checker
public import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
public import Mathlib.Combinatorics.SimpleGraph.Coloring.Vertex

/-!
# The graph `G9`: adjacency data, connectivity, non-bipartiteness
-/

@[expose] public section

namespace AlmostStacked

instance : DecidableRel G9.Adj := fun a b =>
  decidable_of_iff _ (SimpleGraph.fromRel_adj (fun a b : Fin 9 => ((a : ℕ), (b : ℕ)) ∈ g9Edges) a b).symm

namespace G9Data

/-- Both orientations of every edge of `G9`. -/
def g9Adj : List (ℕ × ℕ) :=
  [(0, 3), (0, 5), (0, 6), (1, 4), (1, 7), (1, 8), (2, 6), (2, 8), (3, 5), (3, 6), (4, 7),
    (4, 8), (5, 7), (6, 8), (3, 0), (5, 0), (6, 0), (4, 1), (7, 1), (8, 1), (6, 2), (8, 2),
    (5, 3), (6, 3), (7, 4), (8, 4), (7, 5), (8, 6)]

theorem adj_iff : ∀ u v : Fin 9, G9.Adj u v ↔ ((u : ℕ), (v : ℕ)) ∈ g9Adj := by decide

theorem iso : ∀ u : Fin 9, ∃ v, G9.Adj u v := by decide

theorem setup : Setup 9 G9 g9Adj where
  adj := adj_iff
  edges_lt := by decide +kernel
  iso := iso

end G9Data

open G9Data

theorem g9_adj (u v : Fin 9) (h : ((u : ℕ), (v : ℕ)) ∈ g9Adj := by decide) : G9.Adj u v :=
  (adj_iff u v).2 h

theorem G9_connected : G9.Connected := by
  have h0 : ∀ v : Fin 9, G9.Reachable 0 v := by
    have r3 : G9.Reachable 0 3 := (g9_adj 0 3).reachable
    have r5 : G9.Reachable 0 5 := (g9_adj 0 5).reachable
    have r6 : G9.Reachable 0 6 := (g9_adj 0 6).reachable
    have r2 : G9.Reachable 0 2 := r6.trans (g9_adj 6 2).reachable
    have r8 : G9.Reachable 0 8 := r6.trans (g9_adj 6 8).reachable
    have r1 : G9.Reachable 0 1 := r8.trans (g9_adj 8 1).reachable
    have r4 : G9.Reachable 0 4 := r8.trans (g9_adj 8 4).reachable
    have r7 : G9.Reachable 0 7 := r5.trans (g9_adj 5 7).reachable
    intro v
    fin_cases v
    · exact SimpleGraph.Reachable.refl _
    all_goals assumption
  exact ⟨fun u v => (h0 u).symm.trans (h0 v)⟩

/-- `G9` contains the triangle `0, 3, 5`, so it is not bipartite. -/
theorem G9_not_bipartite : ¬ G9.Colorable 2 := by
  rintro ⟨C⟩
  have h03 := C.valid (g9_adj 0 3)
  have h05 := C.valid (g9_adj 0 5)
  have h35 := C.valid (g9_adj 3 5)
  generalize C 0 = a at *
  generalize C 3 = b at *
  generalize C 5 = c at *
  revert a b c
  decide

end AlmostStacked
