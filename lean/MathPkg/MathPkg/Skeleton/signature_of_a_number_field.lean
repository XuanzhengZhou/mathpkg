import Mathlib

open scoped Classical

/-!
# Signature of a Number Field

The **signature** of a number field `K` is the ordered pair `(r₁, r₂)` where
* `r₁` is the number of real embeddings of `K` (i.e. embeddings `K → ℂ` whose image lies in `ℝ`)
* `r₂` is the number of pairs of complex conjugate non-real embeddings

Equivalently, `r₁ = nrRealPlaces K` (the number of real infinite places) and
`r₂ = nrComplexPlaces K` (the number of complex infinite places).

Key relation: `r₁ + 2r₂ = n` where `n = [K : ℚ]` is the degree of the number field.

## Special cases

* **Totally real**: `r₂ = 0`, all embeddings are real.
* **Totally complex**: `r₁ = 0`, no real embeddings; all embeddings come in complex conjugate pairs.

## References

* Mathlib4: `NumberField.InfinitePlace.nrRealPlaces`, `NumberField.InfinitePlace.nrComplexPlaces`
* Mathlib4: `NumberField.IsTotallyReal`, `NumberField.IsTotallyComplex`
-/

namespace NumberField

open InfinitePlace

/-! ### The Signature structure -/

/-- The signature of a number field, consisting of the pair `(r₁, r₂)` where
`r₁` is the number of real places and `r₂` is the number of complex places. -/
structure Signature where
  /-- Number of real embeddings / real infinite places -/
  r₁ : ℕ
  /-- Number of pairs of complex conjugate embeddings / complex infinite places -/
  r₂ : ℕ
  deriving Repr, DecidableEq, Inhabited

/-- The canonical signature of a number field `K`, given by
`(nrRealPlaces K, nrComplexPlaces K)`. -/
noncomputable def signature (K : Type*) [Field K] [NumberField K] : Signature where
  r₁ := nrRealPlaces K
  r₂ := nrComplexPlaces K

/-! ### Key relation: r₁ + 2r₂ = [K : ℚ] -/

/-- The fundamental relation satisfied by the signature:
`r₁ + 2·r₂ = [K : ℚ]`. -/
theorem signature_finrank_relation (K : Type*) [Field K] [NumberField K] :
    (signature K).r₁ + 2 * (signature K).r₂ = Module.finrank ℚ K := by
  sorry
