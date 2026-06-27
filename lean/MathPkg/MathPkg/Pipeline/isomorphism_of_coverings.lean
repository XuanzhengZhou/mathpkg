import Mathlib

/-!
# Isomorphism of Coverings

An isomorphism between covering maps `p : Y → X` and `p' : Y' → X` is a homeomorphism
`φ : Y → Y'` such that `p' ∘ φ = p`. This means the diagram

```
       Y --φ--→ Y'
        \       /
        p \     / p'
           ↘   ↙
            X
```

commutes.

## Main Definition

* `IsomorphismOfCoverings p p'`: the structure bundling a homeomorphism `φ : Y ≃ₜ Y'` and the
  commutativity condition `p' ∘ φ = p`.
-/

open Function

variable {X Y Y' : Type*} [TopologicalSpace X] [TopologicalSpace Y] [TopologicalSpace Y']

/-- An isomorphism between two covering maps `p : Y → X` and `p' : Y' → X` is a homeomorphism
`φ : Y ≃ₜ Y'` such that `p' ∘ φ = p`.

Both `p` and `p'` are assumed to be covering maps; the definition itself only requires the
commutativity of the diagram with a homeomorphism. -/
structure IsomorphismOfCoverings (p : Y → X) (p' : Y' → X) where
  /-- The homeomorphism between the total spaces. -/
  φ : Y ≃ₜ Y'
  /-- The commutativity condition: the diagram commutes. -/
  commutes : p' ∘ φ = p

namespace IsomorphismOfCoverings

variable {p : Y → X} {p' : Y' → X}

/-- The inverse of an isomorphism of coverings is also an isomorphism of coverings. -/
def symm (iso : IsomorphismOfCoverings p p') : IsomorphismOfCoverings p' p where
  φ := iso.φ.symm
  commutes := by
    ext y'
    calc
      p (iso.φ.symm y') = (p' ∘ iso.φ) (iso.φ.symm y') := by rw [iso.commutes]
      _ = p' (iso.φ (iso.φ.symm y')) := rfl
      _ = p' y' := by simp

/-- The identity isomorphism from a covering map to itself. -/
def id (p : Y → X) : IsomorphismOfCoverings p p where
  φ := .refl _
  commutes := rfl

/-- Composition of two isomorphisms of coverings. -/
def trans (iso₁ : IsomorphismOfCoverings p p') (iso₂ : IsomorphismOfCoverings p' p'')
    : IsomorphismOfCoverings p p'' where
  φ := iso₁.φ.trans iso₂.φ
  commutes := by
    ext y
    calc
      p'' (iso₂.φ (iso₁.φ y)) = p' (iso₁.φ y) := by rw [← iso₂.commutes, Function.comp_apply]
      _ = p y := by rw [← iso₁.commutes, Function.comp_apply]

/-- The inverse morphism as a homeomorphism applied to a point in the target space. -/
lemma symm_apply (iso : IsomorphismOfCoverings p p') (y' : Y') : p (iso.φ.symm y') = p' y' :=
  congrFun (iso.symm.commutes) y'

/-- The forward morphism as a homeomorphism applied to a point in the source space. -/
lemma apply_eq (iso : IsomorphismOfCoverings p p') (y : Y) : p' (iso.φ y) = p y :=
  congr_fun iso.commutes y

end IsomorphismOfCoverings

/-! ## Example

A trivial example: if `Y = Y'` and `p = p'` are the same covering map, then the identity
homeomorphism gives an isomorphism of coverings. -/

example {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y] (p : Y → X)
    (hp : IsCoveringMap p) : IsomorphismOfCoverings p p :=
  IsomorphismOfCoverings.id p
