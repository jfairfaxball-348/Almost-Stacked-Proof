module

public import AlmostStacked.Encode
public import AlmostStacked.KTree

/-!
# A verified checker for exact losing layers

Fix a graph `G` on `Fin n` given by a list `edges` of ordered pairs, and a goal predicate `Pg`
(stacked, or of size one) computed on codes by `good`. A *layer certificate* for mass `t` is a
tree `C` of codes, checked against the tree `P` of mass `t - 1` by `layerB`:

* `C` is a binary search tree of codes below `32 ^ n`;
* soundness: no key of `C` is a goal and every legal successor of a key of `C` is in `P`;
* candidate completeness (lemma C5 of `research/S016_CLEAR.md`): every predecessor
  `s + 2 e_u - e_v` of a key `s` of `P` is in `C`, or is a goal, or has a legal successor
  outside `P`;
* terminal configurations: every `0/1` configuration of mass `t` that is not a goal is in `C`.

`layer_step` proves that if `P` is exactly the set of codes of non-winning configurations of
size `t - 1`, then `C` is exactly that set for size `t` (for `2 ≤ t < 32`).
-/

@[expose] public section

namespace AlmostStacked

open Finset

/-- `p` holds on every element of a list (kernel-friendly). -/
noncomputable def lall {α : Type} (l : List α) (p : α → Bool) : Bool :=
  List.rec (motive := fun _ => Bool) true (fun a _ ih => p a && ih) l

/-- `p` holds on some element of a list (kernel-friendly). -/
noncomputable def lany {α : Type} (l : List α) (p : α → Bool) : Bool :=
  List.rec (motive := fun _ => Bool) false (fun a _ ih => p a || ih) l

/-- `p i` holds for some `i < n` (kernel-friendly). -/
noncomputable def nany (n : ℕ) (p : ℕ → Bool) : Bool :=
  Nat.rec (motive := fun _ => Bool) false (fun i ih => p i || ih) n

theorem lall_iff {α : Type} (l : List α) (p : α → Bool) :
    lall l p = true ↔ ∀ a ∈ l, p a = true := by
  induction l with
  | nil => simp [lall]
  | cons a l ih =>
    change (p a && lall l p) = true ↔ _
    simp [ih]

theorem lany_iff {α : Type} (l : List α) (p : α → Bool) :
    lany l p = true ↔ ∃ a ∈ l, p a = true := by
  induction l with
  | nil => simp [lany]
  | cons a l ih =>
    change (p a || lany l p) = true ↔ _
    simp [ih]

theorem nany_iff (n : ℕ) (p : ℕ → Bool) : nany n p = true ↔ ∃ i < n, p i = true := by
  induction n with
  | zero => simp [nany]
  | succ n ih =>
    change (p n || nany n p) = true ↔ _
    rw [Bool.or_eq_true, ih]
    constructor
    · rintro (h | ⟨i, hi, h⟩)
      · exact ⟨n, Nat.lt_succ_self n, h⟩
      · exact ⟨i, Nat.lt_succ_of_lt hi, h⟩
    · rintro ⟨i, hi, h⟩
      rcases Nat.lt_succ_iff_lt_or_eq.1 hi with hi | rfl
      · exact Or.inr ⟨i, hi, h⟩
      · exact Or.inl h

theorem beq_true {a b : ℕ} : Nat.beq a b = true ↔ a = b := by simp [Nat.beq_eq]

theorem beq_false {a b : ℕ} : Nat.beq a b = false ↔ a ≠ b := by
  rw [← Bool.not_eq_true, beq_true]

/-- Code after the move `u ⇒ v`. -/
def succC (k u v : ℕ) : ℕ := Nat.sub (Nat.add k (pw v)) (Nat.mul 2 (pw u))

/-- Code before the move `u ⇒ v`. -/
def predC (k u v : ℕ) : ℕ := Nat.sub (Nat.add k (Nat.mul 2 (pw u))) (pw v)

theorem succC_eq (k u v : ℕ) : succC k u v = k + 32 ^ v - 2 * 32 ^ u := by
  simp only [succC, pw_eq]; rfl

theorem predC_eq (k u v : ℕ) : predC k u v = k + 2 * 32 ^ u - 32 ^ v := by
  simp only [predC, pw_eq]; rfl

/-- The stacking goal on codes: one digit equals the (nonzero) mass. -/
noncomputable def goodStack (n k : ℕ) : Bool :=
  nany n (fun i => Nat.beq (dig k i) (mass n k)) && !(Nat.beq (mass n k) 0)

/-- The clearing goal on codes: mass one. -/
noncomputable def goodClear (n k : ℕ) : Bool := Nat.beq (mass n k) 1

/-- Soundness of a layer `C` against the previous layer `P`. -/
noncomputable def soundB (edges : List (ℕ × ℕ)) (good : ℕ → Bool) (P C : KTree) : Bool :=
  C.all fun k => !(good k) && lall edges fun e => Nat.blt (dig k e.1) 2 || P.mem (succC k e.1 e.2)

/-- A candidate is in `C`, or a goal, or has a legal successor outside `P`. -/
noncomputable def candOk (edges : List (ℕ × ℕ)) (good : ℕ → Bool) (P C : KTree) (c : ℕ) : Bool :=
  C.mem c || (good c || lany edges fun e => !(Nat.blt (dig c e.1) 2) && !(P.mem (succC c e.1 e.2)))

/-- Candidate completeness of `C` against `P`. -/
noncomputable def completeB (edges : List (ℕ × ℕ)) (good : ℕ → Bool) (P C : KTree) : Bool :=
  P.all fun k => lall edges fun e => Nat.beq (dig k e.2) 0 || candOk edges good P C (predC k e.1 e.2)

/-- Every non-goal `0/1` configuration of mass `t` is in `C`. -/
noncomputable def termB (n : ℕ) (good : ℕ → Bool) (t : ℕ) (C : KTree) : Bool :=
  lall (zeroOne n) fun k => !(Nat.beq (mass n k) t) || (good k || C.mem k)

/-- The complete check of layer `t`. -/
noncomputable def layerB (n : ℕ) (edges : List (ℕ × ℕ)) (good : ℕ → Bool) (t : ℕ) (P C : KTree) :
    Bool :=
  C.ordered 0 (pw n) && (soundB edges good P C && (completeB edges good P C && termB n good t C))

/-- All edge endpoints are vertices. -/
noncomputable def edgesB (n : ℕ) (edges : List (ℕ × ℕ)) : Bool :=
  lall edges fun e => Nat.blt e.1 n && Nat.blt e.2 n

/-- The graph data the checker relies on. -/
structure Setup (n : ℕ) (G : SimpleGraph (Fin n)) (edges : List (ℕ × ℕ)) : Prop where
  adj : ∀ u v : Fin n, G.Adj u v ↔ ((u : ℕ), (v : ℕ)) ∈ edges
  edges_lt : edgesB n edges = true
  iso : ∀ u, ∃ v, G.Adj u v

/-- `good` computes the goal predicate on codes of configurations of size below `32`. -/
def GoodSpec (n : ℕ) (Pg : (Fin n → ℕ) → Prop) (good : ℕ → Bool) : Prop :=
  ∀ c : Fin n → ℕ, size c < 32 → (Pg c ↔ good (enc c) = true)

theorem goodStack_spec (n : ℕ) : GoodSpec n IsStacked (goodStack n) := by
  intro c hc
  rw [isStacked_iff, goodStack, Bool.and_eq_true, nany_iff, mass_enc c hc]
  constructor
  · rintro ⟨v, hv, h0⟩
    refine ⟨⟨v, v.2, ?_⟩, ?_⟩
    · rw [dig_enc c (lt_of_size_lt hc) v, hv]; exact beq_true.2 rfl
    · rw [Bool.not_eq_true']; exact beq_false.2 h0
  · rintro ⟨⟨i, hi, h⟩, h0⟩
    rw [Bool.not_eq_true'] at h0
    refine ⟨⟨i, hi⟩, ?_, beq_false.1 h0⟩
    have := dig_enc c (lt_of_size_lt hc) ⟨i, hi⟩
    rw [beq_true] at h
    rw [← this]; exact h

theorem goodClear_spec (n : ℕ) : GoodSpec n (fun c => size c = 1) (goodClear n) := by
  intro c hc
  rw [goodClear, mass_enc c hc]
  simp

section

variable {n : ℕ} {G : SimpleGraph (Fin n)} {edges : List (ℕ × ℕ)}

theorem Setup.mem_lt (S : Setup n G edges) {e : ℕ × ℕ} (he : e ∈ edges) :
    e.1 < n ∧ e.2 < n := by
  have := (lall_iff _ _).1 S.edges_lt e he
  simpa [Bool.and_eq_true, KTree.blt_true] using this

/-- A move, read on codes. -/
theorem Setup.move_code (S : Setup n G edges) {c d : Fin n → ℕ} (hc : size c < 32)
    (h : Move G c d) :
    ∃ e ∈ edges, 2 ≤ dig (enc c) e.1 ∧ enc d = succC (enc c) e.1 e.2 ∧
      1 ≤ dig (enc d) e.2 ∧ enc c = predC (enc d) e.1 e.2 := by
  have hsize := size_of_move h
  obtain ⟨u, v, huv, hu, rfl⟩ := h
  have hne : u ≠ v := G.ne_of_adj huv
  have hm := enc_move c hne hu
  have hd : size (Function.update (Function.update c u (c u - 2)) v (c v + 1)) < 32 := by
    omega
  refine ⟨((u : ℕ), (v : ℕ)), (S.adj u v).1 huv, ?_, ?_, ?_, ?_⟩
  · rw [dig_enc c (lt_of_size_lt hc) u]; exact hu
  · rw [succC_eq]; dsimp only; omega
  · rw [dig_enc _ (lt_of_size_lt hd) v, Function.update_self]; omega
  · rw [predC_eq]; dsimp only; omega

/-- A code-level legal move is a move. -/
theorem Setup.code_move (S : Setup n G edges) {c : Fin n → ℕ} (hc : size c < 32)
    {e : ℕ × ℕ} (he : e ∈ edges) (h2 : 2 ≤ dig (enc c) e.1) :
    ∃ d, Move G c d ∧ enc d = succC (enc c) e.1 e.2 := by
  obtain ⟨h1, h2'⟩ := S.mem_lt he
  set u : Fin n := ⟨e.1, h1⟩
  set v : Fin n := ⟨e.2, h2'⟩
  have huv : G.Adj u v := (S.adj u v).2 (by simpa [u, v] using he)
  have hu : 2 ≤ c u := by rw [← dig_enc c (lt_of_size_lt hc) u]; exact h2
  refine ⟨_, move_of huv hu, ?_⟩
  have hm := enc_move c (G.ne_of_adj huv) hu
  rw [succC_eq]
  change _ = enc c + 32 ^ (v : ℕ) - 2 * 32 ^ (u : ℕ)
  omega

/-- No legal move means every vertex holds at most one pebble. -/
theorem Setup.le_one_of_no_move (S : Setup n G edges) {c : Fin n → ℕ}
    (h : ¬ ∃ d, Move G c d) (u : Fin n) : c u ≤ 1 := by
  by_contra hu
  obtain ⟨v, huv⟩ := S.iso u
  exact h ⟨_, move_of huv (by omega)⟩

/-- One exact layer step. -/
theorem layer_step (S : Setup n G edges) {Pg : (Fin n → ℕ) → Prop} {good : ℕ → Bool}
    (hgood : GoodSpec n Pg good) {t : ℕ} (ht : 2 ≤ t) (ht32 : t < 32) {P C : KTree}
    (hPo : P.ordered 0 (pw n) = true)
    (hP : ∀ c : Fin n → ℕ, size c = t - 1 → (P.Contains (enc c) ↔ ¬ Wins G Pg c))
    (hchk : layerB n edges good t P C = true) :
    ∀ c : Fin n → ℕ, size c = t → (C.Contains (enc c) ↔ ¬ Wins G Pg c) := by
  simp only [layerB, Bool.and_eq_true] at hchk
  obtain ⟨_, hsound, hcomp, hterm⟩ := hchk
  intro c hc
  have hc32 : size c < 32 := by omega
  constructor
  · -- soundness
    intro hmem hwin
    have hk := KTree.of_all hsound hmem
    simp only [Bool.and_eq_true, Bool.not_eq_true'] at hk
    obtain ⟨hng, hall⟩ := hk
    rcases wins_iff.1 hwin with hgoal | ⟨d, hm, hd⟩
    · rw [(hgood c hc32).1 hgoal] at hng; exact Bool.noConfusion hng
    · obtain ⟨e, he, h2, hed, -, -⟩ := S.move_code hc32 hm
      have := (lall_iff _ _).1 hall e he
      rw [Bool.or_eq_true] at this
      rcases this with hlt | hpm
      · rw [KTree.blt_true] at hlt; omega
      · rw [← hed] at hpm
        have hsd := size_of_move hm
        exact (hP d (by omega)).1 (KTree.contains_of_mem hpm) hd
  · -- completeness
    intro hnw
    by_cases hmove : ∃ d, Move G c d
    · obtain ⟨d, hm⟩ := hmove
      have hsd := size_of_move hm
      have hnd : ¬ Wins G Pg d := fun hw => hnw (wins_iff.2 (Or.inr ⟨d, hm, hw⟩))
      have hdP := (hP d (by omega)).2 hnd
      obtain ⟨e, he, -, -, h1, hce⟩ := S.move_code hc32 hm
      have := (lall_iff _ _).1 (KTree.of_all hcomp hdP) e he
      rw [Bool.or_eq_true, beq_true] at this
      rcases this with h0 | hok
      · omega
      rw [← hce, candOk, Bool.or_eq_true, Bool.or_eq_true] at hok
      rcases hok with hmem | hg | hany
      · exact KTree.contains_of_mem hmem
      · exact absurd (wins_iff.2 (Or.inl ((hgood c hc32).2 hg))) hnw
      · obtain ⟨e', he', hx⟩ := (lany_iff _ _).1 hany
        simp only [Bool.and_eq_true, Bool.not_eq_true'] at hx
        obtain ⟨hx2, hxP⟩ := hx
        have h2 : 2 ≤ dig (enc c) e'.1 := by
          rw [KTree.blt_false] at hx2; omega
        obtain ⟨d', hm', hd'⟩ := S.code_move hc32 he' h2
        rw [← hd'] at hxP
        have hsd' := size_of_move hm'
        have : Wins G Pg d' := by
          by_contra hn
          exact KTree.not_contains_of_mem_eq_false hPo hxP ((hP d' (by omega)).2 hn)
        exact absurd (wins_iff.2 (Or.inr ⟨d', hm', this⟩)) hnw
    · have hle := S.le_one_of_no_move hmove
      have hz := enc_mem_zeroOne c hle
      have := (lall_iff _ _).1 hterm _ hz
      rw [mass_enc c hc32, hc, Bool.or_eq_true, Bool.or_eq_true] at this
      rcases this with h | hg | hmem
      · simp at h
      · exact absurd (wins_iff.2 (Or.inl ((hgood c hc32).2 hg))) hnw
      · exact KTree.contains_of_mem hmem

/-- The base layer `t = 1`: every configuration of size one is a goal. -/
theorem layer_one {Pg : (Fin n → ℕ) → Prop} (h1 : ∀ c : Fin n → ℕ, size c = 1 → Pg c) :
    ∀ c : Fin n → ℕ, size c = 1 → (KTree.nil.Contains (enc c) ↔ ¬ Wins G Pg c) := by
  intro c hc
  simp only [KTree.contains_nil, false_iff, not_not]
  exact wins_iff.2 (Or.inl (h1 c hc))

end

end AlmostStacked
