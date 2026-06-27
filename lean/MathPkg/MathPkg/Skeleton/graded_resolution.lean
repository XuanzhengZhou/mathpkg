import Mathlib

open CategoryTheory
open HomologicalComplex

/-!
# Graded Resolution

A **graded resolution** of a graded `R`-module `M` is a chain complex of graded free
`R`-modules `... → F₂ → F₁ → F₀ → M → 0` where each differential `d_i : F_i → F_{i-1}`
is a **graded homomorphism of degree zero**.

In Mathlib4, a graded `R`-module is modeled as `GradedObject σ (ModuleCat R)`, i.e.,
a family of `R`-modules indexed by `σ`. A morphism in this category is automatically a
graded homomorphism of degree zero — it maps the `i`-th component to the `i`-th component.

## Main definitions

* `GradedModule` : A family of `R`-modules indexed by `σ` (abbreviation).
* `GradedHom` : A graded homomorphism of degree `d : σ` between graded `R`-modules
  `X` and `Y` — a family of `R`-linear maps `X i →ₗ[R] Y (i + d)`.
* `IsGradedFree` : A graded `R`-module `X` is graded free if each homogeneous component
  `X i` is a free `R`-module.
* `GradedResolution` : A graded resolution of a graded `R`-module `M` consists of
  a chain complex of graded free `R`-modules `F n` (indexed by `n : ℕ`) together with
  an augmentation map `F₀ → M` which is a graded epimorphism (surjective on each component).

## References

* `Mathlib/Algebra/Homology/HomologicalComplex.lean`
* `Mathlib/CategoryTheory/GradedObject.lean`
-/

universe u

section graded_hom

/-! ### Graded homomorphisms -/

variable (σ : Type*) [AddCommMonoid σ] (R : Type u) [CommRing R]

/--
A **graded `R`-module** with grading group `σ` is a family of `R`-modules indexed by `σ`.

This is a convenience abbreviation for `GradedObject σ (ModuleCat R)`.
-/
abbrev GradedModule : Type _ := GradedObject σ (ModuleCat.{u} R)

/--
A **graded homomorphism of degree `d : σ`** between two graded `R`-modules
`X` and `Y` is a family of `R`-linear maps `f i : X i →ₗ[R] Y (i + d)` for each `i : σ`.

When `d = 0`, this coincides with a morphism in the category `GradedObject σ (ModuleCat R)`:
the morphism at index `i` maps the `i`-th component to the `i`-th component.
-/
def GradedHom (d : σ) (X Y : GradedModule σ R) : Type _ := by
  sorry
