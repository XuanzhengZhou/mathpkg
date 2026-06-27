import Mathlib

/-!
# Zero Divisors and Cancellation Laws

A ring `R` has no zero divisors if and only if the right and left cancellation laws hold:
for all `a`, `b`, `c` in `R` with `a ≠ 0`, `ab = ac ⇒ b = c` and `ba = ca ⇒ b = c`.
-/

variable {R : Type*} [Ring R]

/-- A ring `R` has no zero divisors if and only if the right and left cancellation laws hold. -/
theorem zero_divisors_and_cancellation_laws : NoZeroDivisors R ↔ IsCancelMulZero R := by
  sorry
