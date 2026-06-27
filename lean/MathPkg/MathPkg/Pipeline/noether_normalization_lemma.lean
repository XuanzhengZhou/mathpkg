import Mathlib

/-!
# Noether Normalization Lemma

Let `A` be a finitely generated algebra over a field `k`.
Then there exist algebraically independent elements `y₁,…,y_d ∈ A` such that
`A` is a finitely generated module over the polynomial subring `k[y₁,…,y_d]`.

Mathlib4 provides a full proof in `Mathlib.RingTheory.NoetherNormalization`.
The main theorem is `exists_integral_inj_algHom_of_fg` and the finite-module
version `exists_finite_inj_algHom_of_fg`.

Reference: <https://stacks.math.columbia.edu/tag/00OW>
-/

open MvPolynomial

variable (k R : Type*) [Field k] [CommRing R] [Nontrivial R] [Algebra k R]
  [Algebra.FiniteType k R]

/--
**Noether Normalization Lemma**

For a finitely generated algebra `R` over a field `k`, there exists a natural number `s`
and an injective `k`-algebra homomorphism `g : k[X₀,…,X_{s-1}] → R` such that
`R` is integral (hence a finitely generated module) over `k[X₀,…,X_{s-1}]`.

This is the integral version from `Mathlib.RingTheory.NoetherNormalization`.
-/
theorem noether_normalization_lemma_integral : ∃ s : ℕ,
    ∃ g : MvPolynomial (Fin s) k →ₐ[k] R,
    Function.Injective g ∧ g.IsIntegral :=
  exists_integral_inj_algHom_of_fg k R

/--
**Noether Normalization Lemma (finite module version)**

For a finitely generated algebra `R` over a field `k`, there exists a natural number `s`
and an injective `k`-algebra homomorphism `g : k[X₀,…,X_{s-1}] → R` such that
`R` is a finitely generated module over `k[X₀,…,X_{s-1}]`.
-/
theorem noether_normalization_lemma_finite : ∃ s : ℕ,
    ∃ g : MvPolynomial (Fin s) k →ₐ[k] R,
    Function.Injective g ∧ g.Finite :=
  exists_finite_inj_algHom_of_fg k R

/--
Example: If `R = k[X₀, X₁]` is the polynomial ring in 2 variables, we can take `s = 2`
and the identity map, which is trivially injective and integral.
-/
example : ∃ s : ℕ,
    ∃ g : MvPolynomial (Fin s) ℚ →ₐ[ℚ] MvPolynomial (Fin 2) ℚ,
    Function.Injective g ∧ g.IsIntegral := by
  refine ⟨2, AlgHom.id _ _, ?_, ?_⟩
  · exact Function.injective_id
  · let f : MvPolynomial (Fin 2) ℚ →+* MvPolynomial (Fin 2) ℚ :=
      (AlgHom.id ℚ (MvPolynomial (Fin 2) ℚ)).toRingHom
    have hsurj : Function.Surjective f := fun x => ⟨x, rfl⟩
    exact RingHom.isIntegral_of_surjective f hsurj

/--
Example: For a finitely generated ℚ-algebra `R := ℚ[X,Y,Z]/(X^3 - Y^2)`,
the Noether normalization lemma guarantees the existence of algebraically
independent elements over which `R` is finite.
-/
example (R : Type*) [CommRing R] [Nontrivial R] [Algebra ℚ R] [Algebra.FiniteType ℚ R] :
    ∃ s : ℕ,
    ∃ g : MvPolynomial (Fin s) ℚ →ₐ[ℚ] R,
    Function.Injective g ∧ g.IsIntegral :=
  noether_normalization_lemma_integral ℚ R
