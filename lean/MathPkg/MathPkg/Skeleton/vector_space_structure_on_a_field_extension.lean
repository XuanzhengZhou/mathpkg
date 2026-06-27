import Mathlib

/-!
# Vector Space Structure on a Field Extension

For a field extension `F ⊆ K`, `K` is made into an `F`-vector space by defining
scalar multiplication for `α ∈ F` and `a ∈ K` as `α · a = α * a` (multiplication in `K`).

In Mathlib4, this is captured by the typeclass `Algebra F K`, which provides the
`Module F K` instance, giving `K` the structure of an `F`-vector space.
-/

/-- For a field extension `K/F`, the scalar multiplication `α • a` for `α : F` and `a : K`
coincides with ordinary multiplication in `K` via the algebra map. -/
theorem vector_space_structure_on_a_field_extension (F K : Type*) [Field F] [Field K] [Algebra F K]
    (a : F) (b : K) : a • b = (algebraMap F K a) * b := by
  sorry
