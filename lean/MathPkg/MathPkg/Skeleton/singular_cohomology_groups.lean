import Mathlib

/-!
# Singular Cohomology Groups

For a topological space `X` and an abelian group `G`, the **n-th singular cohomology group**
`Hⁿ(X; G)` is the quotient `ker(δⁿ) / im(δⁿ⁻¹)`, where `δ` is the coboundary operator
on the singular cochain complex `Cⁿ(X; G) = Hom(Cₙ(X; ℤ), G)`.

* Elements of `ker(δⁿ)` are called **cocycles**.
* Elements of `im(δⁿ⁻¹)` are called **coboundaries**.

## Mathlib4 context

* `Algebra/Homology` — homological algebra framework, including `HomologicalComplex` and
  `K.homology i` for the homology of a complex at degree `i`.
-/

open CategoryTheory

/- singular_cohomology_groups -/

universe u

/-- The **n-th singular cohomology group** of a topological space `X` with coefficients
    in an abelian group `G`.

    `Hⁿ(X; G) := ker(δⁿ) / im(δⁿ⁻¹)` where `δ` is the coboundary operator on the
    singular cochain complex `Cⁿ(X; G) = Hom(Cₙ(X; ℤ), G)`. -/
def singularCohomologyGroup (X : Type u) [TopologicalSpace X] (G : Type u) [AddCommGroup G]
    (n : ℕ) : Type u := by
  sorry
