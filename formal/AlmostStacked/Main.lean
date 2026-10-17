module

public import AlmostStacked.G9.StackLayers
public import AlmostStacked.G9.ClearLayers

/-!
# The G9 counterexamples to the critical Almost Stacked Hypothesis

From the exact losing layers of `G9` (`G9.StackLayers`, `G9.ClearLayers`):

* K1 / K1c: the non-stackable (non-clearable) configurations of size 14 are exactly `cStar`
  and `cStarImage`, neither almost stacked;
* K2 / K2c: every configuration of every size `≥ 15` is stackable (clearable);
* K3 / K3c: every almost stacked configuration of size 14 is stackable (clearable);
* K4 / K4c: for every `t ∈ [2, 14]` some configuration of size `t` is not stackable
  (clearable), and some almost stacked configuration of size 13 is not;
* hence `stack(G9) = clear(G9) = 15`, the almost-stacked thresholds are `14`, `L_all = 14`,
  `L_AS = 13`, and the critical hypothesis fails in both clauses.
-/

@[expose] public section

namespace AlmostStacked

open G9Data

theorem enc9 (a b c d e f g h i : ℕ) : enc ![a, b, c, d, e, f, g, h, i] =
    a + 32 * b + 1024 * c + 32768 * d + 1048576 * e + 33554432 * f + 1073741824 * g +
      34359738368 * h + 1099511627776 * i := by
  simp [enc, Fin.sum_univ_succ]; ring

theorem size9 (a b c d e f g h i : ℕ) : size ![a, b, c, d, e, f, g, h, i] =
    a + b + c + d + e + f + g + h + i := by
  simp [size, Fin.sum_univ_succ]; ring

theorem not_wins_of_mem {P : (Fin 9 → ℕ) → Prop} {T : KTree} {t : ℕ}
    (hl : ∀ c : Fin 9 → ℕ, size c = t → (T.Contains (enc c) ↔ ¬ Wins G9 P c))
    (c : Fin 9 → ℕ) (hs : size c = t) (hm : T.mem (enc c) = true) : ¬ Wins G9 P c :=
  (hl c hs).1 (KTree.contains_of_mem hm)

theorem size_cStar : size cStar = 14 := by rw [cStar, size9]

theorem size_cStarImage : size cStarImage = 14 := by rw [cStarImage, size9]

theorem enc_cStar : enc cStar = 275045680128 := by rw [cStar, enc9]

theorem enc_cStarImage : enc cStarImage = 172067128320 := by rw [cStarImage, enc9]

theorem cStar_not_AS : ¬ IsAlmostStacked cStar := by
  rintro ⟨v, hv⟩
  by_cases h : v = 5
  · subst h
    have := hv 7 (by decide)
    simp [cStar] at this
  · have := hv 5 (Ne.symm h)
    simp [cStar] at this

theorem cStarImage_not_AS : ¬ IsAlmostStacked cStarImage := by
  rintro ⟨v, hv⟩
  by_cases h : v = 5
  · subst h
    have := hv 7 (by decide)
    simp [cStarImage] at this
  · have := hv 5 (Ne.symm h)
    simp [cStarImage] at this

/-- An almost stacked configuration of size 13 that is neither stackable nor clearable. -/
def w13 : Fin 9 → ℕ := ![0, 0, 1, 0, 1, 11, 0, 0, 0]

theorem w13_AS : IsAlmostStacked w13 := ⟨5, by decide⟩

theorem size_w13 : size w13 = 13 := by rw [w13, size9]

/-- The two critical configurations are the only size-14 keys. -/
theorem crit_of_contains {T : KTree}
    (hT : T = .node (.node .nil 172067128320 .nil) 275045680128 .nil) {c : Fin 9 → ℕ}
    (hc : size c = 14) (h : T.Contains (enc c)) : c = cStar ∨ c = cStarImage := by
  subst hT
  simp only [KTree.contains_node, KTree.contains_nil, false_or, or_false] at h
  rcases h with h | h
  · right
    exact enc_injective (by omega) (by rw [size_cStarImage]; norm_num) (h.trans enc_cStarImage.symm)
  · left
    exact enc_injective (by omega) (by rw [size_cStar]; norm_num) (h.trans enc_cStar.symm)

/-! ## Stacking -/

theorem G9_stack_14 (c : Fin 9 → ℕ) (hc : size c = 14) :
    ¬ Stackable G9 c ↔ c = cStar ∨ c = cStarImage := by
  constructor
  · intro h
    exact crit_of_contains rfl hc ((stack_layer_14 c hc).2 h)
  · rintro (rfl | rfl)
    · exact not_wins_of_mem stack_layer_14 _ size_cStar (by rw [enc_cStar]; decide +kernel)
    · exact not_wins_of_mem stack_layer_14 _ size_cStarImage
        (by rw [enc_cStarImage]; decide +kernel)

theorem G9_stack_15 (c : Fin 9 → ℕ) (hc : size c = 15) : Stackable G9 c := by
  by_contra h
  have := (stack_layer_15 c hc).2 h
  simp [Data.G9Stack15] at this

theorem G9_stack_large : ∀ s, 15 ≤ s → ∀ c : Fin 9 → ℕ, size c = s → Stackable G9 c :=
  wins_above setup.iso (by simp) G9_stack_15

theorem G9_stack_AS_14 (c : Fin 9 → ℕ) (hc : size c = 14) (ha : IsAlmostStacked c) :
    Stackable G9 c := by
  by_contra h
  rcases (G9_stack_14 c hc).1 h with rfl | rfl
  · exact cStar_not_AS ha
  · exact cStarImage_not_AS ha

theorem G9_stack_w13 : ¬ Stackable G9 w13 :=
  not_wins_of_mem stack_layer_13 _ size_w13 (by rw [w13, enc9]; decide +kernel)

theorem G9_stack_losers : ∀ t, 2 ≤ t → t ≤ 14 → ∃ c : Fin 9 → ℕ, size c = t ∧ ¬ Stackable G9 c := by
  intro t h2 h14
  interval_cases t
  · exact ⟨![0, 0, 0, 0, 0, 0, 0, 1, 1], by rw [size9], not_wins_of_mem stack_layer_2 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 0, 1, 2], by rw [size9], not_wins_of_mem stack_layer_3 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 0, 1, 3], by rw [size9], not_wins_of_mem stack_layer_4 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 1, 1, 3], by rw [size9], not_wins_of_mem stack_layer_5 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 0, 1, 5], by rw [size9], not_wins_of_mem stack_layer_6 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 1, 5, 1], by rw [size9], not_wins_of_mem stack_layer_7 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 1, 1, 6], by rw [size9], not_wins_of_mem stack_layer_8 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 3, 5, 1], by rw [size9], not_wins_of_mem stack_layer_9 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 1, 9, 0], by rw [size9], not_wins_of_mem stack_layer_10 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 1, 0, 0, 0, 1, 9, 0], by rw [size9], not_wins_of_mem stack_layer_11 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 1, 0, 0, 1, 0, 10, 0], by rw [size9], not_wins_of_mem stack_layer_12 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨w13, size_w13, G9_stack_w13⟩
  · exact ⟨cStar, size_cStar, (G9_stack_14 cStar size_cStar).2 (Or.inl rfl)⟩

theorem G9_stackNumber : IsStackNumber G9 15 := by
  refine ⟨⟨by norm_num, G9_stack_15⟩, fun s ⟨hs2, hall⟩ => ?_⟩
  by_contra hlt
  obtain ⟨c, hc, hn⟩ := G9_stack_losers s hs2 (by omega)
  exact hn (hall c hc)

theorem G9_stack_AS_threshold :
    IsLeast {t₀ | 2 ≤ t₀ ∧ ∀ s, t₀ ≤ s → ∀ c : Fin 9 → ℕ, size c = s → IsAlmostStacked c →
      Stackable G9 c} 14 := by
  refine ⟨⟨by norm_num, fun s hs c hc ha => ?_⟩, fun t₀ ⟨_, hall⟩ => ?_⟩
  · rcases Nat.lt_or_ge s 15 with h | h
    · exact G9_stack_AS_14 c (by omega) ha
    · exact G9_stack_large s h c hc
  · by_contra hlt
    exact G9_stack_w13 (hall 13 (by omega) w13 size_w13 w13_AS)

theorem G9_stack_Lall :
    IsGreatest {t | 2 ≤ t ∧ ∃ c : Fin 9 → ℕ, size c = t ∧ ¬ Stackable G9 c} 14 := by
  refine ⟨⟨by norm_num, cStar, size_cStar, (G9_stack_14 cStar size_cStar).2 (Or.inl rfl)⟩,
    fun t ⟨_, c, hc, hn⟩ => ?_⟩
  by_contra hlt
  exact hn (G9_stack_large t (by omega) c hc)

theorem G9_stack_LAS :
    IsGreatest {t | 2 ≤ t ∧ ∃ c : Fin 9 → ℕ, size c = t ∧ IsAlmostStacked c ∧ ¬ Stackable G9 c}
      13 := by
  refine ⟨⟨by norm_num, w13, size_w13, w13_AS, G9_stack_w13⟩, fun t ⟨_, c, hc, ha, hn⟩ => ?_⟩
  by_contra hlt
  rcases Nat.lt_or_ge t 15 with h | h
  · exact hn (G9_stack_AS_14 c (by omega) ha)
  · exact hn (G9_stack_large t h c hc)

theorem G9_not_ASHStarStack : ¬ ASHStarStack G9 := fun h =>
  absurd ((h 15 G9_stackNumber).unique G9_stack_AS_threshold) (by norm_num)

theorem not_forall_ASHStarStack :
    ¬ ∀ (n : ℕ) (G : SimpleGraph (Fin n)), 2 ≤ n → G.Connected → ASHStarStack G := fun h =>
  G9_not_ASHStarStack (h 9 G9 (by norm_num) G9_connected)

/-! ## Clearing -/

theorem G9_clear_14 (c : Fin 9 → ℕ) (hc : size c = 14) :
    ¬ Clearable G9 c ↔ c = cStar ∨ c = cStarImage := by
  constructor
  · intro h
    exact crit_of_contains rfl hc ((clear_layer_14 c hc).2 h)
  · rintro (rfl | rfl)
    · exact not_wins_of_mem clear_layer_14 _ size_cStar (by rw [enc_cStar]; decide +kernel)
    · exact not_wins_of_mem clear_layer_14 _ size_cStarImage
        (by rw [enc_cStarImage]; decide +kernel)

theorem G9_clear_15 (c : Fin 9 → ℕ) (hc : size c = 15) : Clearable G9 c := by
  by_contra h
  have := (clear_layer_15 c hc).2 h
  simp [Data.G9Clear15] at this

theorem G9_clear_large : ∀ s, 15 ≤ s → ∀ c : Fin 9 → ℕ, size c = s → Clearable G9 c :=
  wins_above setup.iso (by simp) G9_clear_15

theorem G9_clear_AS_14 (c : Fin 9 → ℕ) (hc : size c = 14) (ha : IsAlmostStacked c) :
    Clearable G9 c := by
  by_contra h
  rcases (G9_clear_14 c hc).1 h with rfl | rfl
  · exact cStar_not_AS ha
  · exact cStarImage_not_AS ha

theorem G9_clear_w13 : ¬ Clearable G9 w13 :=
  not_wins_of_mem clear_layer_13 _ size_w13 (by rw [w13, enc9]; decide +kernel)

theorem G9_clear_losers : ∀ t, 2 ≤ t → t ≤ 14 → ∃ c : Fin 9 → ℕ, size c = t ∧ ¬ Clearable G9 c := by
  intro t h2 h14
  interval_cases t
  · exact ⟨![0, 0, 0, 0, 0, 0, 0, 1, 1], by rw [size9], not_wins_of_mem clear_layer_2 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 0, 0, 3], by rw [size9], not_wins_of_mem clear_layer_3 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 0, 1, 3], by rw [size9], not_wins_of_mem clear_layer_4 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 1, 1, 3], by rw [size9], not_wins_of_mem clear_layer_5 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 0, 1, 5], by rw [size9], not_wins_of_mem clear_layer_6 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 1, 5, 1], by rw [size9], not_wins_of_mem clear_layer_7 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 1, 1, 6], by rw [size9], not_wins_of_mem clear_layer_8 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 3, 5, 1], by rw [size9], not_wins_of_mem clear_layer_9 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 0, 0, 0, 0, 1, 9, 0], by rw [size9], not_wins_of_mem clear_layer_10 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 1, 0, 0, 0, 1, 9, 0], by rw [size9], not_wins_of_mem clear_layer_11 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨![0, 0, 1, 0, 0, 1, 0, 10, 0], by rw [size9], not_wins_of_mem clear_layer_12 _
      (by rw [size9]) (by rw [enc9]; decide +kernel)⟩
  · exact ⟨w13, size_w13, G9_clear_w13⟩
  · exact ⟨cStar, size_cStar, (G9_clear_14 cStar size_cStar).2 (Or.inl rfl)⟩

theorem G9_clearNumber : IsClearNumber G9 15 := by
  refine ⟨⟨by norm_num, G9_clear_15⟩, fun s ⟨hs2, hall⟩ => ?_⟩
  by_contra hlt
  obtain ⟨c, hc, hn⟩ := G9_clear_losers s hs2 (by omega)
  exact hn (hall c hc)

theorem G9_clear_AS_threshold :
    IsLeast {t₀ | 2 ≤ t₀ ∧ ∀ s, t₀ ≤ s → ∀ c : Fin 9 → ℕ, size c = s → IsAlmostStacked c →
      Clearable G9 c} 14 := by
  refine ⟨⟨by norm_num, fun s hs c hc ha => ?_⟩, fun t₀ ⟨_, hall⟩ => ?_⟩
  · rcases Nat.lt_or_ge s 15 with h | h
    · exact G9_clear_AS_14 c (by omega) ha
    · exact G9_clear_large s h c hc
  · by_contra hlt
    exact G9_clear_w13 (hall 13 (by omega) w13 size_w13 w13_AS)

theorem G9_clear_Lall :
    IsGreatest {t | 2 ≤ t ∧ ∃ c : Fin 9 → ℕ, size c = t ∧ ¬ Clearable G9 c} 14 := by
  refine ⟨⟨by norm_num, cStar, size_cStar, (G9_clear_14 cStar size_cStar).2 (Or.inl rfl)⟩,
    fun t ⟨_, c, hc, hn⟩ => ?_⟩
  by_contra hlt
  exact hn (G9_clear_large t (by omega) c hc)

theorem G9_clear_LAS :
    IsGreatest {t | 2 ≤ t ∧ ∃ c : Fin 9 → ℕ, size c = t ∧ IsAlmostStacked c ∧ ¬ Clearable G9 c}
      13 := by
  refine ⟨⟨by norm_num, w13, size_w13, w13_AS, G9_clear_w13⟩, fun t ⟨_, c, hc, ha, hn⟩ => ?_⟩
  by_contra hlt
  rcases Nat.lt_or_ge t 15 with h | h
  · exact hn (G9_clear_AS_14 c (by omega) ha)
  · exact hn (G9_clear_large t h c hc)

theorem G9_not_ASHStarClear : ¬ ASHStarClear G9 := fun h =>
  absurd ((h 15 G9_clearNumber).unique G9_clear_AS_threshold) (by norm_num)

theorem not_forall_ASHStarClear :
    ¬ ∀ (n : ℕ) (G : SimpleGraph (Fin n)), G.Connected → ¬ G.Colorable 2 → ASHStarClear G :=
  fun h => G9_not_ASHStarClear (h 9 G9 G9_connected G9_not_bipartite)

/-! ## General lemmas used -/

/-- Monotonicity above the order for stacking (October Lemma 4.7 / S003 Lemma 2). -/
theorem stackable_above {V : Type*} [Fintype V] [DecidableEq V] (G : SimpleGraph V)
    (hiso : ∀ u, ∃ v, G.Adj u v) (t : ℕ) (ht : Fintype.card V ≤ t)
    (h : ∀ c : V → ℕ, size c = t → Stackable G c) :
    ∀ s, t ≤ s → ∀ c : V → ℕ, size c = s → Stackable G c :=
  wins_above hiso ht h

/-- Monotonicity above the order for clearing (October Lemma 4.7 / S003 Lemma 2). -/
theorem clearable_above {V : Type*} [Fintype V] [DecidableEq V] (G : SimpleGraph V)
    (hiso : ∀ u, ∃ v, G.Adj u v) (t : ℕ) (ht : Fintype.card V ≤ t)
    (h : ∀ c : V → ℕ, size c = t → Clearable G c) :
    ∀ s, t ≤ s → ∀ c : V → ℕ, size c = s → Clearable G c :=
  wins_above hiso ht h

end AlmostStacked
