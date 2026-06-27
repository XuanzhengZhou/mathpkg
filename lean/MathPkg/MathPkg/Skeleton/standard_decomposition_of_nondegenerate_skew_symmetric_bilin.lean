import Mathlib

open LinearMap (BilinForm)

/- Standard decomposition of nondegenerate skew-symmetric bilinear form -/

theorem standard_decomposition_of_nondegenerate_skew_symmetric_bilin
    (p : ℕ) [Fact p.Prime] (V : Type*) [AddCommGroup V] [Module (ZMod p) V] [FiniteDimensional (ZMod p) V]
    (f : BilinForm (ZMod p) V) (h_skew : f.IsAlt) (h_nondegen : f.Nondegenerate) :
    ∃ (n : ℕ) (u v : Fin n → V),
      (∀ i j, f (u i) (u j) = 0) ∧
      (∀ i j, f (v i) (v j) = 0) ∧
      (∀ i j, f (u i) (v j) = if i = j then 1 else 0) ∧
      Submodule.span (ZMod p) (Set.range u ∪ Set.range v) = ⊤ := by
  sorry
