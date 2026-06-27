import Mathlib

/- Translation of: Preservation of Discreteness under Finite Extensions

Let E be a finite extension of K, v a valuation on K, and w a valuation on E
extending v. If v is discrete, then w is discrete.

Mathlib4 references:
- `Valuation.IsRankOneDiscrete v` : the valuation v is discrete (has a generator < 1)
- `Valuation.HasExtension v w` : w is an extension of v (v is equivalent to the
  comap of w along algebraMap K E)
- `FiniteDimensional K E` : E is finite-dimensional as a K-vector space (i.e., a
  finite extension)
-/

theorem preservation_of_discreteness_under_finite_extensions
  {K E : Type*} [Field K] [Field E] [Algebra K E] [FiniteDimensional K E]
  {ΓK ΓE : Type*} [LinearOrderedCommGroupWithZero ΓK] [LinearOrderedCommGroupWithZero ΓE]
  (v : Valuation K ΓK) (w : Valuation E ΓE)
  [hw_ext : v.HasExtension w] [hv : v.IsRankOneDiscrete] : w.IsRankOneDiscrete := by
  sorry
