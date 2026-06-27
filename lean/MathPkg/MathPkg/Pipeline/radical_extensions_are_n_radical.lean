import Mathlib

/- radical extensions are n-radical -/

/-- K/F is an n-radical extension if there exists a chain
    F = F₀ ⊂ ⋯ ⊂ Fᵣ = K where F_{i+1} = F_i(a_i) and a_i^n ∈ F_i. -/
class IsNRadicalExtension (F K : Type*) [Field F] [Field K] [Algebra F K] (n : ℕ) : Prop where
  exists_chain : ∃ (r : ℕ) (F_ : Fin (r+1) → IntermediateField F K) (a : Fin r → K),
    F_ 0 = ⊥ ∧ F_ (Fin.last r) = ⊤ ∧
    (∀ i : Fin r, F_ i.succ = (F_ i).adjoin ({a i} : Set K) ∧ (a i)^n ∈ (F_ i : Set K))

theorem radical_extensions_are_n_radical {F K : Type*} [Field F] [Field K] [Algebra F K]
    [h : IsRadicalExtension F K] : ∃ n : ℕ, IsNRadicalExtension F K n := by
  sorry
