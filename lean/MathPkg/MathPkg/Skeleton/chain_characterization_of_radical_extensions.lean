import Mathlib

open IntermediateField

/- Chain characterization of radical extensions -/

theorem chain_characterization_of_radical_extensions (F K : Type*) [Field F] [Field K] [Algebra F K] :
    solvableByRad F K = ⊤ ↔
    ∃ (r : ℕ) (E : ℕ → IntermediateField F K),
      E 0 = ⊥ ∧ E r = ⊤ ∧
      ∀ i, i < r → ∃ (a : K) (n : ℕ), a ^ n ∈ (E i : Set K) ∧
        E (i+1) = E i ⊔ adjoin F {a} := by
  sorry
