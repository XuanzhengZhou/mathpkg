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
def symm (iso : IsomorphismOfCoverings p p') : IsomorphismOfCoverings p' p := by
  sorry
