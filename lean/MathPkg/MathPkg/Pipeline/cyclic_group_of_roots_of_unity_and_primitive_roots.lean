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

/-- If `ζ` is a primitive `n`-th root of unity in `ℂ`, then `ζ ^ k` is also a
primitive `n`-th root if and only if `k` is coprime to `n`. -/
theorem isPrimitiveRoot_pow_iff_coprime {ζ : ℂˣ} (hζ : IsPrimitiveRoot ζ n) (k : ℕ) :
    IsPrimitiveRoot (ζ ^ k) n ↔ Nat.Coprime k n := by
  sorry
