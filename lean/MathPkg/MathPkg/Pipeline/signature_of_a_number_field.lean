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
    (signature K).r₁ + 2 * (signature K).r₂ = finrank ℚ K := by
  dsimp [signature]
  exact card_add_two_mul_card_eq_rank K

/-! ### Totally real fields (r₂ = 0) -/

/-- A number field is totally real iff its signature has `r₂ = 0`. -/
theorem signature_totally_real_iff (K : Type*) [Field K] [NumberField K] :
    (signature K).r₂ = 0 ↔ IsTotallyReal K :=
  nrComplexPlaces_eq_zero_iff

/-- In a totally real field, the signature is `(n, 0)` where `n = [K : ℚ]`. -/
theorem signature_of_totally_real (K : Type*) [Field K] [NumberField K] [IsTotallyReal K] :
    signature K = { r₁ := finrank ℚ K, r₂ := 0 } := by
  have hr₂ : (signature K).r₂ = 0 := (signature_totally_real_iff K).mpr inferInstance
  have hrank : (signature K).r₁ + 2 * (signature K).r₂ = finrank ℚ K :=
    signature_finrank_relation K
  rw [hr₂, mul_zero, add_zero] at hrank
  ext <;> dsimp
  · exact hrank
  · exact hr₂

/-! ### Totally complex fields (r₁ = 0) -/

/-- A number field is totally complex iff its signature has `r₁ = 0`. -/
theorem signature_totally_complex_iff (K : Type*) [Field K] [NumberField K] :
    (signature K).r₁ = 0 ↔ IsTotallyComplex K :=
  nrRealPlaces_eq_zero_iff

/-- In a totally complex field, the signature is `(0, n/2)` where `n = [K : ℚ]`
(so `n` must be even). -/
theorem signature_of_totally_complex (K : Type*) [Field K] [NumberField K] [IsTotallyComplex K] :
    signature K = { r₁ := 0, r₂ := (finrank ℚ K) / 2 } := by
  have hr₁ : (signature K).r₁ = 0 := (signature_totally_complex_iff K).mpr inferInstance
  have hrank : (signature K).r₁ + 2 * (signature K).r₂ = finrank ℚ K :=
    signature_finrank_relation K
  rw [hr₁, zero_add] at hrank
  have hfinrank_even : 2 ∣ finrank ℚ K := by
    rw [← hrank]
    exact ⟨(signature K).r₂, by ring⟩
  have hdiv : 2 * (signature K).r₂ / 2 = (signature K).r₂ := by
    omega
  rw [hrank] at hdiv
  ext <;> dsimp
  · exact hr₁
  · omega

end NumberField

/-! ### Examples -/

section examples

open NumberField

/-- ℚ has signature (1, 0): one real embedding, no complex ones. Totally real. -/
example : signature ℚ = { r₁ := 1, r₂ := 0 } := by
  have hrank : finrank ℚ ℚ = 1 := by
    exact FiniteDimensional.finrank_self ℚ
  have htot : IsTotallyReal ℚ := by infer_instance
  rw [signature_of_totally_real ℚ, hrank]

/-- ℚ(√2) has signature (2, 0): two real embeddings (√2 ↦ √2, √2 ↦ -√2),
both lie in ℝ. Totally real. -/
example : IsTotallyReal ℚ := by
  infer_instance

/-- ℚ(√-1) = ℚ(i) has signature (0, 1): one pair of complex conjugate
embeddings (i ↦ i, i ↦ -i). Totally complex, degree 2. -/
example (K : Type*) [Field K] [NumberField K] [IsTotallyComplex K] (hfinrank : finrank ℚ K = 2) :
    signature K = { r₁ := 0, r₂ := 1 } := by
  rw [signature_of_totally_complex K]
  rw [hfinrank]
  rfl

/-- The fundamental relation r₁ + 2r₂ = [K:ℚ] holds for any number field ℚ. -/
example : (signature ℚ).r₁ + 2 * (signature ℚ).r₂ = finrank ℚ ℚ :=
  signature_finrank_relation ℚ

/-- The signature of a totally real cubic field is (3, 0). -/
example (K : Type*) [Field K] [NumberField K] [IsTotallyReal K] (hfinrank : finrank ℚ K = 3) :
    signature K = { r₁ := 3, r₂ := 0 } := by
  rw [signature_of_totally_real K, hfinrank]

/-- A mixed-signature cubic field has signature (1, 1):
one real embedding, one pair of complex conjugate embeddings. -/
example (K : Type*) [Field K] [NumberField K]
    (hr₁ : nrRealPlaces K = 1) (hr₂ : nrComplexPlaces K = 1) :
    signature K = { r₁ := 1, r₂ := 1 } := by
  have hfinrank : finrank ℚ K = 3 := by
    have h := card_add_two_mul_card_eq_rank K
    rw [hr₁, hr₂] at h
    omega
  unfold signature
  rw [hr₁, hr₂]
  rfl

end examples
