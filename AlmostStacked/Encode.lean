module

public import AlmostStacked.Basic
public import Mathlib.Tactic.Ring
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.IntervalCases

/-!
# Coding configurations on `Fin n` as natural numbers

`enc c = ∑ i, c i * 32 ^ i`. For configurations of size below `32` every entry is a base-32
digit of the code, so the code determines the configuration (`dig_enc`, `enc_injective`), and a
move changes the code by `+ 32 ^ v - 2 * 32 ^ u` (`enc_move`). The kernel-evaluated functions
(`dig`, `mass`, `zeroOne`, ...) are defined with `Nat.rec` and explicit `Nat` operations.
-/

@[expose] public section

namespace AlmostStacked

open Finset

/-- The code of a configuration on `Fin n`. -/
def enc {n : ℕ} (c : Fin n → ℕ) : ℕ := ∑ i, c i * 32 ^ (i : ℕ)

/-- `32 ^ i`, written for kernel evaluation. -/
def pw (i : ℕ) : ℕ := Nat.pow 32 i

/-- The `i`-th base-32 digit. -/
def dig (k i : ℕ) : ℕ := Nat.mod (Nat.div k (pw i)) 32

/-- The sum of the first `n` digits. -/
noncomputable def mass (n k : ℕ) : ℕ := Nat.rec (motive := fun _ => ℕ) 0 (fun i s => Nat.add (dig k i) s) n

/-- Codes of all `0/1` configurations on `n` vertices. -/
noncomputable def zeroOne (n : ℕ) : List ℕ :=
  Nat.rec (motive := fun _ => List ℕ) [0]
    (fun _ l => List.flatMap (fun k => [Nat.mul 32 k, Nat.add (Nat.mul 32 k) 1]) l) n

theorem pw_eq (i : ℕ) : pw i = 32 ^ i := Nat.pow_eq

theorem dig_eq (k i : ℕ) : dig k i = k / 32 ^ i % 32 := by
  simp only [dig, pw_eq]; rfl

theorem mass_zero (k : ℕ) : mass 0 k = 0 := rfl

theorem mass_succ (n k : ℕ) : mass (n + 1) k = dig k n + mass n k := rfl

theorem mass_eq (n k : ℕ) : mass n k = ∑ i ∈ range n, dig k i := by
  induction n with
  | zero => rfl
  | succ n ih => rw [mass_succ, ih, sum_range_succ, Nat.add_comm]

theorem zeroOne_zero : zeroOne 0 = [0] := rfl

theorem zeroOne_succ (n : ℕ) :
    zeroOne (n + 1) = (zeroOne n).flatMap (fun k => [32 * k, 32 * k + 1]) := rfl

theorem enc_succ {n : ℕ} (c : Fin (n + 1) → ℕ) :
    enc c = c 0 + 32 * enc (fun i : Fin n => c i.succ) := by
  simp only [enc, Fin.sum_univ_succ, Fin.val_zero, pow_zero, mul_one, Fin.val_succ, pow_succ,
    Finset.mul_sum]
  congr 1
  exact Finset.sum_congr rfl fun i _ => by ring

theorem dig_enc {n : ℕ} (c : Fin n → ℕ) (hc : ∀ i, c i < 32) (i : Fin n) :
    dig (enc c) i = c i := by
  rw [dig_eq]
  induction n with
  | zero => exact i.elim0
  | succ n ih =>
    rw [enc_succ]
    have h0 := hc 0
    refine Fin.cases ?_ (fun j => ?_) i
    · simp only [Fin.val_zero, pow_zero, Nat.div_one]; omega
    · rw [Fin.val_succ, pow_succ', ← Nat.div_div_eq_div_mul,
        Nat.add_mul_div_left _ _ (by norm_num : 0 < 32), Nat.div_eq_of_lt h0, Nat.zero_add]
      exact ih (fun i => c i.succ) (fun i => hc i.succ) j

theorem lt_of_size_lt {n : ℕ} {c : Fin n → ℕ} (h : size c < 32) (i : Fin n) : c i < 32 :=
  lt_of_le_of_lt (le_size c i) h

theorem enc_injective {n : ℕ} {c d : Fin n → ℕ} (hc : size c < 32) (hd : size d < 32)
    (h : enc c = enc d) : c = d := by
  funext i
  rw [← dig_enc c (lt_of_size_lt hc) i, ← dig_enc d (lt_of_size_lt hd) i, h]

theorem mass_enc {n : ℕ} (c : Fin n → ℕ) (hc : size c < 32) : mass n (enc c) = size c := by
  rw [mass_eq, ← Fin.sum_univ_eq_sum_range (fun i => dig (enc c) i) n]
  exact Finset.sum_congr rfl fun i _ => dig_enc c (lt_of_size_lt hc) i

theorem enc_update {n : ℕ} (c : Fin n → ℕ) (u : Fin n) (b : ℕ) :
    enc (Function.update c u b) + c u * 32 ^ (u : ℕ) = enc c + b * 32 ^ (u : ℕ) :=
  sum_update_add (V := Fin n) (fun x y => y * 32 ^ (x : ℕ)) c u b

/-- A move `u ⇒ v` changes the code by `+ 32 ^ v - 2 * 32 ^ u`. -/
theorem enc_move {n : ℕ} (c : Fin n → ℕ) {u v : Fin n} (huv : u ≠ v) (hu : 2 ≤ c u) :
    enc (Function.update (Function.update c u (c u - 2)) v (c v + 1)) + 2 * 32 ^ (u : ℕ) =
      enc c + 32 ^ (v : ℕ) := by
  have h1 := enc_update c u (c u - 2)
  have h2 := enc_update (Function.update c u (c u - 2)) v (c v + 1)
  rw [Function.update_of_ne huv.symm] at h2
  have h3 : c u * 32 ^ (u : ℕ) = (c u - 2) * 32 ^ (u : ℕ) + 2 * 32 ^ (u : ℕ) := by
    rw [← Nat.add_mul, Nat.sub_add_cancel hu]
  have h4 : (c v + 1) * 32 ^ (v : ℕ) = c v * 32 ^ (v : ℕ) + 32 ^ (v : ℕ) := by ring
  omega

theorem enc_mem_zeroOne {n : ℕ} (c : Fin n → ℕ) (hc : ∀ i, c i ≤ 1) : enc c ∈ zeroOne n := by
  induction n with
  | zero => simp [enc, zeroOne_zero]
  | succ n ih =>
    rw [zeroOne_succ, List.mem_flatMap, enc_succ]
    refine ⟨_, ih (fun i => c i.succ) (fun i => hc i.succ), ?_⟩
    have := hc 0
    interval_cases h : c 0 <;> simp [Nat.add_comm]

end AlmostStacked
