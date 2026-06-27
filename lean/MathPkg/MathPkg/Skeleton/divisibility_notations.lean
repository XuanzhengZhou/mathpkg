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
def CoprimeDiv (d n : ℕ) : Prop := by
  sorry
