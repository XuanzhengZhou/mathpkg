import Mathlib

open IntermediateField

/- Intermediate fields of cyclic Kummer extensions -/
theorem intermediate_fields_of_cyclic_kummer_extensions
    (F K : Type*) [Field F] [Field K] [Algebra F K] [FiniteDimensional F K]
    (n : ℕ) (a : F) (ζ : F)
    (h_primitive_root : IsPrimitiveRoot ζ n)
    (h_galois : IsGalois F K)
    (h_cyclic : IsCyclic (K ≃ₐ[F] K))
    (h_finrank : Module.finrank F K = n)
    (h_generated : ∃ (α : K), α ^ n = algebraMap F K a ∧ adjoin F {α} = ⊤) :
    ∀ (L : IntermediateField F K), ∃ (m : ℕ), m ∣ n ∧
      ∃ (β : K), β ∈ L ∧ β ^ m = algebraMap F K a ∧ adjoin F {β} = L := by
  sorry
