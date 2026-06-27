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
    Function.Injective g ∧ g.IsIntegral := by
  sorry
