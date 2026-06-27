import Mathlib

open MonoidHom

/-!
# Consequences of Injectivity and Surjectivity for Homomorphisms

Corollary of the First Isomorphism Theorem. Let `φ : A →* B` be a group homomorphism.

- If `φ` is injective, then `A ≃* φ.range`.
- If `φ` is surjective, then `B ≃* A ⧸ (ker φ)`.
-/

/--
**Consequences of Injectivity and Surjectivity for Homomorphisms.**

Given a group homomorphism `φ : A →* B`:
1. If `φ` is injective, then `A` is isomorphic to the image of `φ`.
2. If `φ` is surjective, then `B` is isomorphic to the quotient `A ⧸ ker φ`.

These follow directly from the First Isomorphism Theorem
(`MonoidHom.quotientKerEquivRange`), which states `A ⧸ (ker φ) ≃* range φ`.
-/
def consequences_of_injectivity_and_surjectivity_for_homomorphis {A B : Type*} [Group A] [Group B] (φ : A →* B) :
    (Function.Injective φ → A ≃* φ.range) × (Function.Surjective φ → B ≃* A ⧸ (ker φ)) := by
  sorry
