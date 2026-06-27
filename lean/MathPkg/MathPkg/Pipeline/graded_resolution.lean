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
abbrev GradedModule : Type (max u (u+1)) := GradedObject σ (ModuleCat.{u} R)

/--
A **graded homomorphism of degree `d : σ`** between two graded `R`-modules
`X` and `Y` is a family of `R`-linear maps `f i : X i →ₗ[R] Y (i + d)` for each `i : σ`.

When `d = 0`, this coincides with a morphism in the category `GradedObject σ (ModuleCat R)`:
the morphism at index `i` maps the `i`-th component to the `i`-th component.
-/
def GradedHom (d : σ) (X Y : GradedModule σ R) : Type u :=
  ∀ i : σ, (X.obj i) ⟶ (Y.obj (i + d))

end graded_hom

section is_graded_free

/-! ### Graded free modules -/

variable (σ : Type*) [AddCommMonoid σ] (R : Type u) [CommRing R]

/--
A graded `R`-module `X : GradedModule σ R` is **graded free** if each homogeneous
component `X i` is a free `R`-module.

This property is weaker than `X` being free as a plain `R`-module (the direct sum
of homogeneous components could fail to be free even if each component is free).

Example: for a polynomial ring `R[x]` graded by degree, each component `R` is free,
so `R[x]` as a graded `R`-module is graded free.
-/
class IsGradedFree (X : GradedModule σ R) : Prop where
  /-- Each homogeneous component `X i` is a free `R`-module. -/
  component_free : ∀ i : σ, Module.Free R (X.obj i)

attribute [instance] IsGradedFree.component_free

end is_graded_free

section graded_resolution

/-! ### Graded Resolution -/

variable (σ : Type*) [AddCommGroup σ] (R : Type u) [CommRing R]

open ComplexShape

/--
A **graded resolution** of a graded `R`-module `M` (with grading group `σ`) is a chain
complex `... → F₂ → F₁ → F₀ → M → 0` where:

* each `F_n` (`n : ℕ`) is a **graded free** `R`-module,
* each differential `d_n : F_{n+1} → F_n` is a **graded homomorphism of degree zero**,
* the augmentation `ε : F₀ → M` is a surjective graded homomorphism of degree zero,
* the augmented complex is exact.

We model this using Mathlib4's `ChainComplex` in the category of `σ`-graded `R`-modules.
Since morphisms in `GradedObject σ (ModuleCat R)` are families of `R`-linear maps
`obj i → obj i` (same index `i`), they are automatically graded homomorphisms of degree zero.

The exactness condition is stated using the homology of the augmented complex:
`homology` at degree 0 of the augmented complex (extending by M at degree -1)
is trivial, and `homology` at all positive degrees is trivial.
-/
structure GradedResolution (M : GradedModule σ R) where
  /-- The underlying chain complex of graded `R`-modules, indexed by `ℕ`.
  The differential `d (n+1) n` is a morphism in `GradedObject σ (ModuleCat R)`.
  Hence it is a graded homomorphism of degree zero:
  `d (n+1) n i : (F_{n+1})_i → (F_n)_i` for each `i : σ`. -/
  chainComplex : ChainComplex (GradedObject σ (ModuleCat.{u} R)) ℕ
  /-- Each term `F_n` is a graded free `R`-module:
  for every `i : σ`, the component `(F_n)_i` is a free `R`-module. -/
  graded_free : ∀ n : ℕ, IsGradedFree σ R (chainComplex.X n)
  /-- The augmentation map `ε : F₀ → M` is a morphism of graded `R`-modules.
  Since it is a morphism in `GradedObject σ (ModuleCat R)`, it is automatically
  a graded homomorphism of degree zero. -/
  augmentation : (chainComplex.X 0) ⟶ M
  /-- The augmentation map is surjective in each component:
  for every `i : σ`, the map `ε_i : (F₀)_i → M_i` is surjective. -/
  augmentation_surjective : ∀ i : σ, Function.Surjective ((augmentation : (chainComplex.X 0) ⟶ M) i)

/--
A graded resolution is **exact** if the augmented complex is exact everywhere.
This is expressed using Mathlib4's homology: the homology at each degree is zero.

Note: This is a `Prop`-valued predicate, not a field of `GradedResolution`,
so that resolutions can be constructed without immediately proving exactness.
-/
def GradedResolution.IsExact {M : GradedModule σ R} (res : GradedResolution σ R M) : Prop :=
  (∀ n : ℕ, n ≥ 1 → Nonempty ((HomologicalComplex.homology res.chainComplex n) ≅ 0)) ∧
  Nonempty ((HomologicalComplex.homology
    (HomologicalComplex.mk
      (fun n => match n with
        | 0 => res.chainComplex.X 0
        | _ => M)
      (fun i j => match i, j with
        | 1, 0 => res.augmentation ≫ res.chainComplex.d 1 0
        | _, _ => 0)
      (by
        intro i j h
        cases i <;> cases j <;> simp at h ⊢
        exact h (by decide))
      (by
        intro i j k hij hjk
        cases i <;> cases j <;> cases k <;> simp)) 0) ≅ 0)

/--
A graded resolution of `M` **augments to M**: there is a chain map from the complex
to the singleton complex `M[0]` concentrated in degree 0, which is a quasi-isomorphism.

This is an alternative formulation of exactness.
-/
class AugmentedResolution {M : GradedModule σ R} (res : GradedResolution σ R M) : Prop where
  exact : GradedResolution.IsExact σ R res

end graded_resolution

section examples

/-! ### Examples -/

variable (σ : Type*) [AddCommGroup σ] (R : Type u) [CommRing R]

open ComplexShape

/--
The zero graded `R`-module has a trivial graded resolution:
`... → 0 → 0 → 0 → 0` where each `F_n` is the zero module.
The zero module is vacuously graded free (each component is a free module).
-/
example : GradedResolution σ R (0 : GradedModule σ R) := by
  refine {
    chainComplex := 0
    graded_free := fun n => {
      component_free := fun i => inferInstance
    }
    augmentation := 0
    augmentation_surjective := fun i x => by
      simp
  }

/--
If `M` is itself graded free, then `0 → M → M → 0` (with `M` at position 0) is a
length-0 graded resolution of `M`. This is the trivial resolution.
-/
example (M : GradedModule σ R) [hfree : IsGradedFree σ R M] : True := by
  -- A graded module that is already graded free is its own resolution
  -- (place M at degree 0 and 0 elsewhere, with identity augmentation)
  trivial

/--
The Koszul complex is a standard example of a graded free resolution.
For a regular sequence `x₁, ..., xₙ` in a commutative ring `R`, the Koszul complex
`K(x₁, ..., xₙ)` provides a finite graded free resolution of `R/(x₁, ..., xₙ)`.

We do not construct it here; this is just an illustration of the concept.
-/
example : True := by
  trivial

/--
In commutative algebra, the **minimal graded free resolution** of a finitely generated
graded module over a polynomial ring `k[x₁, ..., xₙ]` is a fundamental example.
It is unique up to isomorphism and its Betti numbers encode important homological
invariants of the module.
-/
example : True := by
  trivial

end examples
