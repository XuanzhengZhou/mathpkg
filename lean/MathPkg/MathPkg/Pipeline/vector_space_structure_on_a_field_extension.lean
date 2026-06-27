import Mathlib

open scoped Classical

/-!
# Vector Space Structure on a Field Extension

For a field extension `F ⊆ K`, we make `K` into an `F`-vector space by defining
scalar multiplication for `α ∈ F` and `a ∈ K` as `α · a = α * a` (multiplication in `K`).

In Mathlib4, this is captured by the typeclass `Algebra F K`, which provides:
- An embedding `algebraMap F K : F →+* K` (the natural inclusion)
- Scalar multiplication `(•) : F → K → K` defined by `α • a = algebraMap F K α * a`

Since `algebraMap` for fields is the inclusion map, this reduces to `α • a = α * a` in `K`.
The `Algebra` structure automatically extends `SMul`, `MulAction`, `DistribMulAction`,
and `Module`, giving `K` the full structure of an `F`-vector space.

This is the same construction used throughout Mathlib4's `FieldTheory` and `Algebra` libraries.
-/

section vector_space_structure_on_a_field_extension

/-! ### Core definition -/

variable (F K : Type*) [Field F] [Field K]

/-- Given a field extension `K/F`, `Algebra F K` provides `K` with the structure of an
`F`-vector space. The scalar multiplication `α • a` for `α : F` and `a : K` is defined as
`algebraMap F K α * a`, which reduces to ordinary multiplication in `K`.

We provide two convenience abbreviations:

* `FieldExtVectorSpace F K` — a shorthand for the full set of assumptions needed.
* `fieldExtVectorSpace` — a type alias making the vector space structure explicit.

In practice, one should use `Algebra F K` directly, since Mathlib4's typeclass system
automatically provides all `Module` and `VectorSpace` instances from an `Algebra` instance. -/
class FieldExtVectorSpace (F K : Type*) [Field F] [Field K] extends Algebra F K : Type _ where

/-- For a field extension `F ⊆ K`, we automatically have `Algebra F K`.
This instance is typically provided when we know that `F` embeds into `K` as a subfield. -/
instance [Algebra F K] : FieldExtVectorSpace F K where
  __ := ‹_›

/-- The vector space structure ensures that scalar multiplication for `α : F` and `a : K`
coincides with ordinary multiplication in `K`. -/
example [Algebra F K] (α : F) (a : K) : α • a = (algebraMap F K α) * a := by
  rfl

/-- When `F` is a subfield of `K` (e.g., `ℚ` in `ℝ`), the `algebraMap` is the inclusion,
so `α • a = α * a`. -/
example [Algebra F K] (α : F) (a : K) : α • a = (algebraMap F K α) * a :=
  rfl

end vector_space_structure_on_a_field_extension

/-! ### Examples -/

section examples

/-- Example 1: `ℚ ⊆ ℝ` as a ℚ-vector space.
Since `ℝ` is a ℚ-algebra (via `algebraMap ℚ ℝ` sending rationals to reals),
`ℝ` is automatically a ℚ-vector space. -/
example : FieldExtVectorSpace ℚ ℝ := by
  infer_instance

/-- Example 2: `ℝ ⊆ ℂ` as an ℝ-vector space.
`ℂ` is an ℝ-algebra, hence an ℝ-vector space. -/
example : FieldExtVectorSpace ℝ ℂ := by
  infer_instance

/-- Example 3: When `α : ℚ` and `a : ℝ`, scalar multiplication `α • a` equals
ordinary multiplication `α * a` in `ℝ`. -/
example (α : ℚ) (a : ℝ) : α • a = (α : ℝ) * a := by
  rfl

/-- Example 4: `K` is an `F`-module (hence an `F`-vector space).
The `[Algebra F K]` argument gives `K` all `R`-module structure. -/
example [Algebra F K] : Module F K := by
  infer_instance

/-- Example 5: Generic field extension `F ⊆ K`.
Once `[Algebra F K]` is available, vector space operations work directly. -/
example [Algebra F K] (α β : F) (a b : K) : (α + β) • a = α • a + β • a := by
  exact add_smul α β a

/-- Example 6: For a number field `K/ℚ`, the ring of integers `𝓞 K` is a ℤ-module,
but `K` itself is a ℚ-vector space via `Algebra ℚ K`. -/
example (K : Type*) [Field K] [Algebra ℚ K] : Module ℚ K := by
  infer_instance

/-- Example 7: Scalar multiplication is compatible with the `algebraMap`.
This follows from the `smul_def'` field of the `Algebra` class. -/
example [Algebra F K] (r : F) (x : K) : r • x = (algebraMap F K r) * x :=
  Algebra.smul_def' r x

end examples
