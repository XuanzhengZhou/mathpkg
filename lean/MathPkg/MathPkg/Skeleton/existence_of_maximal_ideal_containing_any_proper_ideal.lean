import Mathlib

open scoped Classical

/-!
# Existence of Maximal Ideal Containing Any Proper Ideal

In a ring `R` with identity, every proper ideal is contained in a maximal ideal.
This is Krull's theorem, a standard application of Zorn's Lemma.
-/

open Ideal

theorem existence_of_maximal_ideal_containing_any_proper_ideal {R : Type*} [CommRing R]
    (I : Ideal R) (hI : I ≠ ⊤) : ∃ M : Ideal R, I ≤ M ∧ M.IsMaximal := by
  sorry
