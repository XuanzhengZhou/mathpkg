import Mathlib

/-!
# Rabinowitch's Trick (Jacobson Criterion)

For a ring `R`, the following are equivalent:
(a) `R` is a Jacobson ring.
(b) If `P` is a prime ideal of `R` and `S = R/P` contains a nonzero element `b`
    such that `S[b⁻¹]` is a field, then `S` is a field.

This is a key characterization: every Goldman ideal in a Jacobson ring is maximal.
-/

lemma rabinowitchs_trick (R : Type u) [CommRing R] :
    IsJacobsonRing R ↔
    ∀ (P : Ideal R) [hP : Ideal.IsPrime P],
    ∀ (b : R ⧸ P), b ≠ 0 → IsField (Localization.Away b) → IsField (R ⧸ P) := by
  sorry
