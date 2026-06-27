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
example (I : Ideal R) : I.IsPrimary ↔ I ≠ ⊤ ∧ ∀ {x y : R}, x * y ∈ I → x ∈ I ∨ y ∈ I.radical := by
  sorry
