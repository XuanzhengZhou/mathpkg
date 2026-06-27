import Mathlib

/- Determination of F-automorphisms by generators -/
lemma determination_of_f_automorphisms_by_generators {F K : Type*} [Field F] [Field K] [Algebra F K]
    {X : Set K} (hgen : Algebra.adjoin F X = ⊤) (σ τ : K ≃ₐ[F] K) (h : ∀ x ∈ X, σ x = τ x) : σ = τ := by
  sorry
