import Mathlib

open IntermediateField

/--
  A field extension `K` of `F` is a *radical extension* if there exists a finite chain
  `F = F₀ ⊆ F₁ ⊆ ⋯ ⊆ Fᵣ = K` such that each step is obtained by adjoining an `n`-th root:
  `F_{i+1} = F_i(a_i)` where `a_i^{n_i} ∈ F_i` for some integer `n_i`.
-/
class IsRadicalExtension (F K : Type*) [Field F] [Field K] [Algebra F K] : Prop where
  exists_chain : ∃ (r : ℕ) (F_ : Fin (r+1) → IntermediateField F K) (a : Fin r → K) (n : Fin r → ℕ),
    F_ 0 = ⊥ ∧ F_ (Fin.last r) = ⊤ ∧
    (∀ i : Fin r, F_ i.succ = F_ (Fin.castSucc i) ⊔ adjoin F ({a i} : Set K) ∧ (a i) ^ (n i) ∈ (F_ (Fin.castSucc i) : Set K))

/--
  Transitivity of radical extensions: if K/F and L/K are radical
  field extensions, then L/F is also a radical extension.

  Here `F`, `K`, `L` are fields with algebra structures making them
  field extensions: `F ⊆ K ⊆ L`.  The predicate `IsRadicalExtension`
  asserts that the larger field is obtained from the smaller one
  by repeatedly adjoining radicals (n-th roots of elements).
-/
theorem transitivity_of_radical_extensions {F K L : Type*} [Field F] [Field K] [Field L]
    [Algebra F K] [Algebra K L] [Algebra F L] [IsScalarTower F K L]
    [IsRadicalExtension F K] [IsRadicalExtension K L] :
    IsRadicalExtension F L := by
  sorry
