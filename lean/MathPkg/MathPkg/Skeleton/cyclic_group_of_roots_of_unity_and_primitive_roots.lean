import Mathlib

/-!
# Cyclic Group of Roots of Unity and Primitive Roots

The complex `n`-th roots of unity form a cyclic group.
If `ζ` is a primitive `n`-th root of unity, then `ζ ^ k` generates
the group if and only if `gcd(k, n) = 1`.
-/

open scoped Classical

/-- The complex `n`-th roots of unity form a cyclic group. -/
theorem rootsOfUnity_isCyclic (n : ℕ) (hn : 0 < n) : IsCyclic (rootsOfUnity n ℂ) := by
  sorry
