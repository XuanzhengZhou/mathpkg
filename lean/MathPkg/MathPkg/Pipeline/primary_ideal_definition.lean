import Mathlib

open scoped Classical

/-!
# Primary Ideal Definition

An ideal `P` in a ring `R` is called **primary** if whenever
`a * b ∈ P` and `a ∉ P`, there exists a positive integer `n` such that `b ^ n ∈ P`.

Mathlib4 already defines `Ideal.IsPrimary` as an abbreviation for `Submodule.IsPrimary`,
and provides `Ideal.isPrimary_iff` which gives the equivalent multiplicative formulation.
-/

/-! ### Using the existing Mathlib4 definition -/

section primary_ideal_basics

variable {R : Type*} [CommSemiring R]

/-- Mathlib4's definition: `Ideal.IsPrimary I` iff `I ≠ ⊤` and
  `x * y ∈ I → x ∈ I ∨ y ∈ radical I`. -/
example (I : Ideal R) : I.IsPrimary ↔ I ≠ ⊤ ∧ ∀ {x y : R}, x * y ∈ I → x ∈ I ∨ y ∈ I.radical :=
  Ideal.isPrimary_iff

/-- The concept's formulation: whenever `a * b ∈ P` and `a ∉ P`,
  there exists `n ≥ 1` such that `b ^ n ∈ P`. -/
theorem isPrimary_concept_formulation {I : Ideal R} :
    I.IsPrimary ↔ I ≠ ⊤ ∧ ∀ {a b : R}, a * b ∈ I → a ∉ I → ∃ n : ℕ, 0 < n ∧ b ^ n ∈ I := by
  rw [Ideal.isPrimary_iff]
  refine and_congr_right fun _hne ↦ ⟨fun h a b hab ha ↦ ?_, fun h x y hxy ↦ ?_⟩
  · rcases h hab with (hx | hy)
    · exact absurd hx ha
    · rcases hy with ⟨n, hn⟩
      by_cases hn0 : n = 0
      · subst hn0; simp at hn
        have htop : I = ⊤ := ((Ideal.eq_top_iff_one (I := I)).mpr hn)
        exact absurd htop _hne
      · refine ⟨n, Nat.pos_of_ne_zero hn0, hn⟩
  · by_cases hxin : x ∈ I
    · exact Or.inl hxin
    · rcases h hxy hxin with ⟨n, hnpos, hn⟩
      exact Or.inr (Ideal.mem_radical_iff.mpr ⟨n, hn⟩)

end primary_ideal_basics

/-! ### Every prime ideal is primary -/

section prime_implies_primary

variable {R : Type*} [CommSemiring R]

/-- Every prime ideal is a primary ideal (from Mathlib). -/
example {I : Ideal R} (hI : I.IsPrime) : I.IsPrimary :=
  hI.isPrimary

/-- The radical of a primary ideal is prime (from Mathlib). -/
example {I : Ideal R} (hI : I.IsPrimary) : Ideal.IsPrime (I.radical) :=
  Ideal.isPrime_radical hI

end prime_implies_primary

/-! ### Primary ideal under ring homomorphisms -/

section comap_primary

variable {R S : Type*} [CommSemiring R] [CommSemiring S] (f : R →+* S)

/-- The contraction (comap) of a primary ideal is primary. -/
example {I : Ideal S} (hI : I.IsPrimary) : (I.comap f).IsPrimary :=
  hI.comap f

end comap_primary

/-! ### Maximal radical implies primary -/

section maximal_radical

variable {R : Type*} [CommRing R]

/-- If the radical of an ideal is maximal, then the ideal is primary. -/
example {I : Ideal R} (h : Ideal.IsMaximal (I.radical)) : I.IsPrimary :=
  Ideal.isPrimary_of_isMaximal_radical h

end maximal_radical

/-! ### Intersection of primary ideals -/

section inf_primary

variable {R : Type*} [CommSemiring R]

/-- Intersection of two primary ideals with equal radical is primary. -/
example {I J : Ideal R} (hI : I.IsPrimary) (hJ : J.IsPrimary)
    (hrad : I.radical = J.radical) : (I ⊓ J).IsPrimary :=
  hI.inf hJ hrad

end inf_primary
