import Mathlib

open CategoryTheory
open AlgebraicTopology

/-!
# Singular Cochain Complex

Given a topological space `X`, the **singular cochain complex** `S^*(X; ℤ)` is the cochain
complex obtained by dualizing the singular chain complex `S_*(X)`:
`S^q(X) = Hom_ℤ(S_q(X), ℤ)`, with the coboundary operator `d : S^q(X) → S^{q+1}(X)`
defined by `(dω)(c) = ω(∂c)` for a (q+1)-chain `c`.

The graded group `S^*(X) = ⊕_q S^q(X)` becomes a differential complex; the homology
of this complex is the **singular cohomology** of `X` with integer coefficients,
denoted `H^*(X)`.

More generally, replacing ℤ with an abelian group `G` yields the singular cochain complex
with coefficients in `G`: `S^*(X; G) = Hom(S_*(X), G)`, whose homology is
**singular cohomology with coefficients in G**, denoted `H^*(X; G)`.

## Mathlib4 References

* `AlgebraicTopology/SingularHomology/Basic.lean` — `singularChainComplexFunctor`
* `Algebra/Homology/HomologicalComplex.lean` — `CochainComplex`
* `Algebra/Category/ModuleCat/Basic.lean` — `ModuleCat`

## Main definitions

* `singularCochainComplex` : The singular cochain complex with coefficients in ℤ
* `singularCohomology` : The singular cohomology functor with coefficients in ℤ
* `singularCochainComplexWithCoeffs` : The singular cochain complex with coefficients
  in an abelian group `G`
-/

noncomputable section

/--
The **singular cochain complex** of a topological space `X` with coefficients in ℤ.

This is the cochain complex `S^*(X) = Hom(S_*(X), ℤ)` obtained by dualizing the
singular chain complex `S_*(X)`. In degree `q`, the cochain group is
`S^q(X) = Hom_ℤ(S_q(X), ℤ)`, the ℤ-module of linear functionals on singular q-chains.

The coboundary `d_q : S^q(X) → S^{q+1}(X)` is defined by `(d_q ω)(c) = ω(∂_{q+1} c)`
for any (q+1)-chain `c`, where `∂ : S_{q+1}(X) → S_q(X)` is the boundary operator
of the singular chain complex.
-/
noncomputable def singularCochainComplex (X : TopCat.{u}) : CochainComplex (ModuleCat ℤ) ℕ := by
  sorry

/--
The **singular cohomology** of a topological space `X` in degree `n` with coefficients
in ℤ. This is the `n`-th homology of the singular cochain complex `S^*(X)`:
`H^n(X; ℤ) = ker(d_n) / im(d_{n-1})`.

Equivalently, `H^n(X; ℤ)` is the `n`-th cohomology group of the cochain complex
`Hom(S_*(X), ℤ)`.
-/
noncomputable def singularCohomology (X : TopCat.{u}) (n : ℕ) : ModuleCat ℤ := by
  sorry

/--
The **singular cochain complex** of a topological space `X` with coefficients in
an abelian group `G`. This generalises the integer-coefficient version: replace ℤ
with `G`, so that the cochain group in degree `q` is `S^q(X; G) = Hom_ℤ(S_q(X), G)`.

The homology of this complex is singular cohomology with coefficients in `G`,
denoted `H^*(X; G)`.
-/
noncomputable def singularCochainComplexWithCoeffs (G : ModuleCat ℤ) (X : TopCat.{u}) :
    CochainComplex (ModuleCat ℤ) ℕ := by
  sorry

/--
The **singular cohomology** of a topological space `X` in degree `n` with coefficients
in an abelian group `G`. This is `H^n(X; G)`, the `n`-th cohomology group of the
cochain complex `S^*(X; G) = Hom(S_*(X), G)`.
-/
noncomputable def singularCohomologyWithCoeffs (G : ModuleCat ℤ) (X : TopCat.{u}) (n : ℕ) :
    ModuleCat ℤ := by
  sorry

end
