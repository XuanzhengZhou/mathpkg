import Mathlib

open IntermediateField

/- radical extensions are n-radical -/

/-- A field extension K/F is radical if every element of K is solvable by radicals over F. -/
abbrev radical_extensions_are_n_radical_IsRadicalExtension (F K : Type*) [Field F] [Field K] [Algebra F K] : Prop :=
  solvableByRad F K = ⊤

/-- K/F is an n-radical extension if there exists a chain
    F = F₀ ⊂ ⋯ ⊂ Fᵣ = K where F_{i+1} = F_i(a_i) and a_i^n ∈ F_i. -/
class IsNRadicalExtension (F K : Type*) [Field F] [Field K] [Algebra F K] (n : ℕ) : Prop where
  exists_chain : ∃ (r : ℕ) (F_ : Fin (r+1) → IntermediateField F K) (a : Fin r → K),
    F_ 0 = ⊥ ∧ F_ (Fin.last r) = ⊤ ∧
    (∀ i : Fin r, F_ i.succ = adjoin F ({a i} : Set K) ⊔ F_ (i.castSucc) ∧ (a i)^n ∈ (F_ (i.castSucc) : Set K))

theorem radical_extensions_are_n_radical {F K : Type*} [Field F] [Field K] [Algebra F K]
    (h : radical_extensions_are_n_radical_IsRadicalExtension F K) : ∃ n : ℕ, IsNRadicalExtension F K n := by
  sorry
