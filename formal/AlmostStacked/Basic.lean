module

public import AlmostStacked.Defs
public import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-!
# General lemmas about the pebbling model

* `wins_iff`: one-step characterisation of reaching a goal;
* `size_of_move`: a move lowers the size by exactly one;
* `isStacked_iff`: a configuration is stacked iff one vertex carries the whole (nonzero) size;
* `clearable_stackable` (T1 of `research/S016_CLEAR.md`): clearable implies stackable;
* `wins_of_wins_succ` / `wins_above`: monotonicity above the order of the graph
  (October Lemma 4.7, S003 Lemma 2) for graphs without isolated vertices.
-/

@[expose] public section

namespace AlmostStacked

open Finset

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Reaching a configuration satisfying `P` by a finite sequence of moves. -/
def Wins (G : SimpleGraph V) (P : (V → ℕ) → Prop) (c : V → ℕ) : Prop :=
  ∃ d, Relation.ReflTransGen (Move G) c d ∧ P d

omit [Fintype V] in
theorem stackable_iff_wins (G : SimpleGraph V) (c : V → ℕ) :
    Stackable G c ↔ Wins G IsStacked c := Iff.rfl

theorem clearable_iff_wins (G : SimpleGraph V) (c : V → ℕ) :
    Clearable G c ↔ Wins G (fun d => size d = 1) c := Iff.rfl

omit [Fintype V] in
theorem wins_iff {G : SimpleGraph V} {P : (V → ℕ) → Prop} {c : V → ℕ} :
    Wins G P c ↔ P c ∨ ∃ d, Move G c d ∧ Wins G P d := by
  constructor
  · rintro ⟨d, h, hd⟩
    rcases h.cases_head with rfl | ⟨e, he, hed⟩
    · exact Or.inl hd
    · exact Or.inr ⟨e, he, d, hed, hd⟩
  · rintro (h | ⟨d, hm, e, he, hP⟩)
    · exact ⟨c, Relation.ReflTransGen.refl, h⟩
    · exact ⟨e, Relation.ReflTransGen.head hm he, hP⟩

/-- Changing one value of `f` changes a weighted sum by the difference of the weights. -/
theorem sum_update_add (F : V → ℕ → ℕ) (f : V → ℕ) (i : V) (b : ℕ) :
    (∑ x, F x (Function.update f i b x)) + F i (f i) = (∑ x, F x (f x)) + F i b := by
  have h1 := Finset.add_sum_erase univ (fun x => F x (Function.update f i b x)) (mem_univ i)
  have h2 := Finset.add_sum_erase univ (fun x => F x (f x)) (mem_univ i)
  have h3 : ∑ x ∈ univ.erase i, F x (Function.update f i b x) = ∑ x ∈ univ.erase i, F x (f x) :=
    Finset.sum_congr rfl fun x hx => by rw [Function.update_of_ne (Finset.ne_of_mem_erase hx)]
  simp only [Function.update_self] at h1
  omega

omit [Fintype V] in
/-- The configuration after the move `u ⇒ v`. -/
theorem move_iff {G : SimpleGraph V} {c d : V → ℕ} :
    Move G c d ↔ ∃ u v, G.Adj u v ∧ 2 ≤ c u ∧
      d = Function.update (Function.update c u (c u - 2)) v (c v + 1) := Iff.rfl

theorem size_update (f : V → ℕ) (i : V) (b : ℕ) :
    size (Function.update f i b) + f i = size f + b :=
  sum_update_add (fun _ y => y) f i b

/-- A move lowers the size by exactly one. -/
theorem size_of_move {G : SimpleGraph V} {c d : V → ℕ} (h : Move G c d) :
    size d + 1 = size c := by
  obtain ⟨u, v, huv, hu, rfl⟩ := h
  have hne : u ≠ v := G.ne_of_adj huv
  have h1 := size_update c u (c u - 2)
  have h2 := size_update (Function.update c u (c u - 2)) v (c v + 1)
  rw [Function.update_of_ne hne.symm] at h2
  omega

omit [DecidableEq V] in
theorem le_size (c : V → ℕ) (v : V) : c v ≤ size c :=
  Finset.single_le_sum (f := c) (fun _ _ => Nat.zero_le _) (mem_univ v)

theorem add_le_size (c : V → ℕ) {v w : V} (h : v ≠ w) : c v + c w ≤ size c := by
  have := Finset.sum_le_sum_of_subset (f := c) (subset_univ {v, w})
  rwa [Finset.sum_pair h] at this

/-- A configuration is stacked iff one vertex carries its whole, nonzero, size. -/
theorem isStacked_iff (c : V → ℕ) : IsStacked c ↔ ∃ v, c v = size c ∧ size c ≠ 0 := by
  constructor
  · rintro ⟨v, hv⟩
    have hs : size c = c v := by
      unfold size
      exact Finset.sum_eq_single v (fun b _ hb => by_contra fun h => hb ((hv b).1 h))
        (fun h => absurd (mem_univ v) h)
    refine ⟨v, hs.symm, ?_⟩
    rw [hs]; exact (hv v).2 rfl
  · rintro ⟨v, hv, h0⟩
    refine ⟨v, fun w => ⟨fun hw => ?_, fun hw => ?_⟩⟩
    · by_contra hne
      have := add_le_size c (Ne.symm hne)
      omega
    · subst hw; omega

/-- T1: a configuration of size exactly one is stacked, so clearable implies stackable. -/
theorem isStacked_of_size_one {c : V → ℕ} (h : size c = 1) : IsStacked c := by
  rw [isStacked_iff]
  by_contra hno
  push Not at hno
  have hall : ∀ v, c v = 0 := by
    intro v
    have := le_size c v
    have := hno v
    omega
  have : size c = 0 := Finset.sum_eq_zero fun v _ => hall v
  omega

theorem clearable_stackable (G : SimpleGraph V) (c : V → ℕ) (h : Clearable G c) :
    Stackable G c := by
  obtain ⟨d, hd, h1⟩ := h
  exact ⟨d, hd, isStacked_of_size_one h1⟩

omit [DecidableEq V] in
/-- A configuration of size larger than the number of vertices has a vertex with at least two
pebbles. -/
theorem exists_two_le {c : V → ℕ} (h : Fintype.card V < size c) : ∃ u, 2 ≤ c u := by
  by_contra hno
  push Not at hno
  have : size c ≤ ∑ _v : V, 1 := Finset.sum_le_sum fun v _ => by have := hno v; omega
  simp at this
  omega

omit [Fintype V] in
/-- The move `u ⇒ v`. -/
theorem move_of {G : SimpleGraph V} {c : V → ℕ} {u v : V} (huv : G.Adj u v) (hu : 2 ≤ c u) :
    Move G c (Function.update (Function.update c u (c u - 2)) v (c v + 1)) :=
  ⟨u, v, huv, hu, rfl⟩

/-- Monotonicity step above the order (October Lemma 4.7 / S003 Lemma 2). -/
theorem wins_of_wins_succ {G : SimpleGraph V} {P : (V → ℕ) → Prop}
    (hiso : ∀ u, ∃ v, G.Adj u v) {t : ℕ} (ht : Fintype.card V ≤ t)
    (h : ∀ c : V → ℕ, size c = t → Wins G P c) :
    ∀ c : V → ℕ, size c = t + 1 → Wins G P c := by
  intro c hc
  obtain ⟨u, hu⟩ := exists_two_le (c := c) (by omega)
  obtain ⟨v, huv⟩ := hiso u
  have hm := move_of huv hu
  refine wins_iff.2 (Or.inr ⟨_, hm, h _ ?_⟩)
  have := size_of_move hm
  omega

theorem wins_above {G : SimpleGraph V} {P : (V → ℕ) → Prop}
    (hiso : ∀ u, ∃ v, G.Adj u v) {t : ℕ} (ht : Fintype.card V ≤ t)
    (h : ∀ c : V → ℕ, size c = t → Wins G P c) :
    ∀ s, t ≤ s → ∀ c : V → ℕ, size c = s → Wins G P c := by
  intro s hs
  induction s, hs using Nat.le_induction with
  | base => exact h
  | succ s hs ih => exact wins_of_wins_succ hiso (le_trans ht hs) ih

end AlmostStacked
