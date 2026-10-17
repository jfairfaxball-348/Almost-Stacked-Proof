module

public import Mathlib.Order.Basic

/-!
# Binary search trees of natural numbers for kernel evaluation

`KTree` holds certificate data (codes of configurations). All traversals are written with the
recursor `KTree.rec` (no well-founded recursion), so that `decide +kernel` evaluates them by
plain iota reduction. `Contains` is the specification; `mem` is the search, correct on trees
satisfying `ordered`.
-/

@[expose] public section

namespace AlmostStacked

/-- A binary tree of natural-number keys. -/
inductive KTree where
  | nil : KTree
  | node (l : KTree) (k : ℕ) (r : KTree) : KTree

namespace KTree

theorem blt_true {a b : ℕ} : Nat.blt a b = true ↔ a < b := by simp [Nat.blt_eq]

theorem blt_false {a b : ℕ} : Nat.blt a b = false ↔ ¬ a < b := by
  rw [← Bool.not_eq_true, blt_true]

/-- Binary search for `k`. -/
noncomputable def mem (t : KTree) (k : ℕ) : Bool :=
  KTree.rec (motive := fun _ => Bool) false
    (fun _ x _ ml mr => bif Nat.blt k x then ml else bif Nat.blt x k then mr else true) t

/-- `p` holds at every key. -/
noncomputable def all (t : KTree) (p : ℕ → Bool) : Bool :=
  KTree.rec (motive := fun _ => Bool) true (fun _ x _ al ar => p x && (al && ar)) t

/-- Every key lies in `[lo, hi)` and the tree is a binary search tree. -/
noncomputable def ordered (t : KTree) : ℕ → ℕ → Bool :=
  KTree.rec (motive := fun _ => ℕ → ℕ → Bool) (fun _ _ => true)
    (fun _ x _ ol or lo hi => Nat.ble lo x && (Nat.blt x hi && (ol lo x && or (x + 1) hi))) t

/-- `k` is a key of `t`. -/
def Contains (t : KTree) (k : ℕ) : Prop :=
  KTree.rec (motive := fun _ => Prop) False (fun _ x _ pl pr => pl ∨ k = x ∨ pr) t

@[simp] theorem contains_nil (k : ℕ) : ¬ Contains nil k := id

@[simp] theorem contains_node (l r : KTree) (x k : ℕ) :
    Contains (node l x r) k ↔ Contains l k ∨ k = x ∨ Contains r k := Iff.rfl

@[simp] theorem mem_nil (k : ℕ) : mem nil k = false := rfl

theorem mem_node (l r : KTree) (x k : ℕ) :
    mem (node l x r) k = bif Nat.blt k x then mem l k else bif Nat.blt x k then mem r k else true :=
  rfl

@[simp] theorem all_nil (p : ℕ → Bool) : all nil p = true := rfl

@[simp] theorem all_node (l r : KTree) (x : ℕ) (p : ℕ → Bool) :
    all (node l x r) p = (p x && (all l p && all r p)) := rfl

@[simp] theorem ordered_nil (lo hi : ℕ) : ordered nil lo hi = true := rfl

@[simp] theorem ordered_node (l r : KTree) (x lo hi : ℕ) :
    ordered (node l x r) lo hi =
      (Nat.ble lo x && (Nat.blt x hi && (ordered l lo x && ordered r (x + 1) hi))) := rfl

theorem contains_of_mem {t : KTree} {k : ℕ} (h : mem t k = true) : Contains t k := by
  induction t with
  | nil => simp at h
  | node l x r ihl ihr =>
    rw [mem_node] at h
    simp only [contains_node]
    cases h1 : Nat.blt k x <;> cases h2 : Nat.blt x k <;> simp only [h1, h2, Bool.cond_true, Bool.cond_false] at h
    · rw [blt_false] at h1 h2; exact Or.inr (Or.inl (by omega))
    · exact Or.inr (Or.inr (ihr h))
    · exact Or.inl (ihl h)
    · exact Or.inl (ihl h)

theorem bounds_of_contains {t : KTree} {k lo hi : ℕ} (ho : ordered t lo hi = true)
    (h : Contains t k) : lo ≤ k ∧ k < hi := by
  induction t generalizing lo hi with
  | nil => exact absurd h (contains_nil k)
  | node l x r ihl ihr =>
    simp only [ordered_node, Bool.and_eq_true, Nat.ble_eq, Nat.blt_eq] at ho
    obtain ⟨h1, h2, h3, h4⟩ := ho
    rcases h with h | rfl | h
    · have := ihl h3 h; omega
    · omega
    · have := ihr h4 h; omega

theorem mem_of_contains {t : KTree} {k lo hi : ℕ} (ho : ordered t lo hi = true)
    (h : Contains t k) : mem t k = true := by
  induction t generalizing lo hi with
  | nil => exact absurd h (contains_nil k)
  | node l x r ihl ihr =>
    simp only [ordered_node, Bool.and_eq_true, Nat.ble_eq, Nat.blt_eq] at ho
    obtain ⟨h1, h2, h3, h4⟩ := ho
    rw [mem_node]
    rcases h with h | rfl | h
    · have := bounds_of_contains h3 h
      have hb : Nat.blt k x = true := blt_true.2 this.2
      simp [hb, ihl h3 h]
    · have : Nat.blt k k = false := blt_false.2 (Nat.lt_irrefl k)
      simp [this]
    · have := bounds_of_contains h4 h
      have hb : Nat.blt k x = false := blt_false.2 (by omega)
      have hb' : Nat.blt x k = true := blt_true.2 (by omega)
      simp [hb, hb', ihr h4 h]

theorem not_contains_of_mem_eq_false {t : KTree} {k lo hi : ℕ} (ho : ordered t lo hi = true)
    (h : mem t k = false) : ¬ Contains t k := fun hc => by
  rw [mem_of_contains ho hc] at h; exact Bool.noConfusion h

theorem of_all {t : KTree} {p : ℕ → Bool} (h : all t p = true) {k : ℕ} (hk : Contains t k) :
    p k = true := by
  induction t with
  | nil => exact absurd hk (contains_nil k)
  | node l x r ihl ihr =>
    simp only [all_node, Bool.and_eq_true] at h
    rcases hk with hk | rfl | hk
    · exact ihl h.2.1 hk
    · exact h.1
    · exact ihr h.2.2 hk

end KTree

end AlmostStacked
