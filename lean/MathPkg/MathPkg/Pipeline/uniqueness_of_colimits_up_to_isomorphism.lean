import Mathlib

open CategoryTheory
open CategoryTheory.Limits

/-!
# Uniqueness of colimits up to isomorphism

If a colimit of a diagram `F : J ⥤ C` exists, it is unique up to a unique isomorphism
compatible with the cocone maps. This is a fundamental result in category theory:
colimits are determined by their universal property.

## Main statement

Given two colimit cocones `c₁`, `c₂` for the same diagram `F`, there exists a unique
isomorphism `φ : c₁.pt ≅ c₂.pt` between their vertices such that for all objects `j` in
the index category `J`, the triangle

```
    c₁.pt ----φ----> c₂.pt
      ∧               ∧
c₁.ι_j \             / c₂.ι_j
        \           /
         F(j) = F(j)
```

commutes, i.e. `c₁.ι.app j ≫ φ.hom = c₂.ι.app j`.

## References

* [Mac Lane, *Categories for the Working Mathematician*][MacLane1971]
* Mathlib4: `CategoryTheory.Limits.IsColimit.uniqueUpToIso`
-/

section uniqueness_of_colimits_up_to_isomorphism

variable {J C : Type u} [Category.{v} J] [Category.{v} C] (F : J ⥤ C)

/-- **Uniqueness of colimits up to isomorphism**: if `c₁` and `c₂` are two colimit cocones
for a diagram `F : J ⥤ C`, then there exists a unique isomorphism `φ : c₁.pt ≅ c₂.pt`
between their vertices such that for all `j : J`, the cocone injection maps commute:
`c₁.ι.app j ≫ φ.hom = c₂.ι.app j`.

In Mathlib4, this is available as `IsColimit.uniqueUpToIso hc₁ hc₂`. We restate it here
as a theorem with an explicit `∃!` quantifier to emphasize the existence and uniqueness
of the isomorphism. -/
theorem uniqueness_of_colimits_up_to_isomorphism (c₁ c₂ : Cocone F) (hc₁ : IsColimit c₁) (hc₂ : IsColimit c₂) :
    ∃! (φ : c₁.pt ≅ c₂.pt), ∀ (j : J), c₁.ι.app j ≫ φ.hom = c₂.ι.app j := by
  sorry

end uniqueness_of_colimits_up_to_isomorphism

/-
## Examples

The Mathlib4 library already provides the canonical isomorphism between any two colimits
via `IsColimit.uniqueUpToIso`:

```
example : IsColimit.uniqueUpToIso hc₁ hc₂ : c₁.pt ≅ c₂.pt
```

Our theorem above expresses the full `∃!` statement which is equivalent to this definition.
-/
