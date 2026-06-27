import Mathlib

/-!
# Divisibility Notations

This file defines common divisibility notations used in elementary number theory.

## Standard notation (provided by Mathlib4)

- `d ∣ n` : `d` divides `n`. This is the standard `Dvd.dvd` from the `Div` typeclass,
  available for `Nat`, `Int`, and any `CommSemiring`.

## Coprime divisibility (defined here)

- `CoprimeDiv d n` : notation `d ∥ n`, meaning `d ∣ n` and `Nat.Coprime d (n / d)`.
  This says that `d` is a *unitary divisor* of `n`: it divides `n` and is coprime
  to the cofactor `n / d`. In traditional number theory, this is written `d ‖ n`.

## Exact power divisibility (provided by Mathlib4)

- `padicValNat p n = a` : for a prime `p`, the exponent `a` is the highest power such that
  `p^a ∣ n`. In traditional notation this is written `p^a ‖ n`.

  Key theorems in Mathlib4:
  * `pow_padicValNat_dvd` : `p ^ padicValNat p n ∣ n`
  * `pow_dvd_iff_le_padicValNat` : `p^k ∣ n ↔ k ≤ padicValNat p n` (for `p ≠ 1`, `n ≠ 0`)

## References

- `padicValNat` : `Mathlib/Data/Nat/MaxPowDiv.lean`
- `Nat.Coprime` : `Mathlib/Data/Nat/GCD/Basic.lean`
- `Dvd.dvd`   : `Mathlib/Algebra/Div/Basic.lean`
-/

open Nat

/-- `CoprimeDiv d n` means `d` divides `n` and `d` is coprime with `n / d`.
This is the condition that `d` is a *unitary divisor* of `n`.
In traditional number theory notation, this is written `d ‖ n`. -/
def CoprimeDiv (d n : ℕ) : Prop :=
  d ∣ n ∧ Nat.Coprime d (n / d)

/-- Notation `d ∥ n` for `CoprimeDiv d n`: `d` divides `n` and `gcd(d, n/d) = 1`.
Use `open scoped Divides` to enable this notation. -/
scoped[Divides] infix:50 " ∥ " => CoprimeDiv

/-- `ExactPowDiv p a n` means `p^a` is the highest power of `p` dividing `n`.
In Mathlib4 this is equivalent to `padicValNat p n = a`.
Traditional notation: `p^a ‖ n`. -/
abbrev ExactPowDiv (p a n : ℕ) : Prop :=
  padicValNat p n = a

-- Example: standard divisibility `∣` is already available
example (d n : ℕ) : (d ∣ n) ↔ ∃ k, n = d * k := by
  exact (Nat.dvd_iff_exists_eq_mul_of_dvd_dvd (by simp) (by simp)).trans
    ⟨fun ⟨k, h⟩ => ⟨k, h⟩, fun ⟨k, h⟩ => ⟨k, h⟩⟩

/-- Example: 3 is a coprime divisor of 12, since 3 ∣ 12 and gcd(3, 4) = 1. -/
example : CoprimeDiv 3 12 := by
  dsimp [CoprimeDiv]
  constructor
  · exact by decide
  · native_decide

/-- Example: 2 is NOT a coprime divisor of 12, since gcd(2, 6) = 2 ≠ 1. -/
example : ¬ CoprimeDiv 2 12 := by
  dsimp [CoprimeDiv]
  native_decide

/-- Example: 4 is a coprime divisor of 12, since 4 ∣ 12 and gcd(4, 3) = 1. -/
example : CoprimeDiv 4 12 := by
  dsimp [CoprimeDiv]
  native_decide

/-- Example: 6 is NOT a coprime divisor of 12, since gcd(6, 2) = 2 ≠ 1. -/
example : ¬ CoprimeDiv 6 12 := by
  dsimp [CoprimeDiv]
  native_decide

/-- Example: 1 is always a coprime divisor of any n, since 1 ∣ n and gcd(1, n) = 1. -/
example (n : ℕ) : CoprimeDiv 1 n := by
  dsimp [CoprimeDiv]
  constructor
  · exact Nat.one_dvd _
  · simp [Nat.coprime_one_left]

/-- Example: `n` is a coprime divisor of itself iff n = 1, since gcd(n, 1) = 1 always,
but for n > 1, we need gcd(n, n/n) = gcd(n, 1) = 1, which is always true.
Wait: if n > 0, n/n = 1, so gcd(n, 1) = 1 always. So n ∥ n is always true for n > 0.
Actually n ∣ n always, and n/n = 1 for n > 0 (0/0 is 0).
For n = 0: 0 ∣ 0 is true, 0/0 = 0, gcd(0,0) = 0 ≠ 1. So 0 ∥ 0 is false. -/
example : CoprimeDiv 5 5 := by
  dsimp [CoprimeDiv]
  constructor
  · exact dvd_refl 5
  · native_decide

/-- Example: 0 ∥ 0 is false because gcd(0, 0/0) = gcd(0, 0) = 0 ≠ 1. -/
example : ¬ CoprimeDiv 0 0 := by
  dsimp [CoprimeDiv]
  native_decide

/-- Example: Using `padicValNat` to express `p^a ‖ n`. For p=2, n=24=2^3·3,
the highest power of 2 dividing 24 is 2^3. So `padicValNat 2 24 = 3`. -/
example : padicValNat 2 24 = 3 := by
  native_decide

/-- Example: `padicValNat 2 12 = 2` because 12 = 2^2·3. -/
example : padicValNat 2 12 = 2 := by
  native_decide

/-- Example: `padicValNat 3 12 = 1` because 12 = 3·4. -/
example : padicValNat 3 12 = 1 := by
  native_decide

/-- Example: `padicValNat 5 12 = 0` because 5 does not divide 12. -/
example : padicValNat 5 12 = 0 := by
  native_decide

/-- Example: For n = 0, `padicValNat p 0 = 0` for any p. -/
example (p : ℕ) : padicValNat p 0 = 0 := by
  simp [padicValNat]

/-- Example: `ExactPowDiv` expresses that `p^a` is the exact power of `p` dividing `n`,
i.e., `padicValNat p n = a`. -/
example : ExactPowDiv 2 3 24 := by
  dsimp [ExactPowDiv]
  native_decide

/-- Example: `¬ ExactPowDiv 2 2 24` because the highest power of 2 in 24 is 3, not 2. -/
example : ¬ ExactPowDiv 2 2 24 := by
  dsimp [ExactPowDiv]
  native_decide

/-- Example: For a prime p, `ExactPowDiv p a n` implies `p^a ∣ n`. -/
example (p a n : ℕ) (h : ExactPowDiv p a n) : p ^ a ∣ n := by
  dsimp [ExactPowDiv] at h
  -- h : padicValNat p n = a
  -- We know pow_padicValNat_dvd : p ^ padicValNat p n ∣ n
  have h_dvd := pow_padicValNat_dvd (p := p) (n := n)
  rw [h] at h_dvd
  exact h_dvd
