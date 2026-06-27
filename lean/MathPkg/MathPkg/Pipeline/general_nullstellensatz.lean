import Mathlib

/-!
# General Nullstellensatz (Jacobson Ring Property)

Let R be a Jacobson ring. If S is a finitely generated R-algebra, then S is a Jacobson ring.
Moreover, if n ⊂ S is a maximal ideal, then m = n ∩ R is a maximal ideal of R,
and S/n is a finite extension field of R/m.
-/

theorem general_nullstellensatz (R S : Type*) [CommRing R] [CommRing S] [Algebra R S]
    [IsJacobsonRing R] [Algebra.FiniteType R S] : IsJacobsonRing S ∧
    ∀ (n : Ideal S), n.IsMaximal →
      (n.comap (algebraMap R S)).IsMaximal ∧
      FiniteDimensional (R ⧸ n.comap (algebraMap R S)) (S ⧸ n) := by
  sorry
