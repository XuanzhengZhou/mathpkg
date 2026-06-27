import Mathlib

example {α : Type} [Monoid α] (u : αˣ) : ((u * u⁻¹ : αˣ) : α) = (1 : α) := by
  simpa using congrArg Units.val (u.mul_inv)
