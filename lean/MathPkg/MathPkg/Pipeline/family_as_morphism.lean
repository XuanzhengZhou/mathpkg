import Mathlib

/-!
# Family as Morphism

In algebraic geometry, a **family of varieties (or schemes)** parametrized by a base `B`
is given by a morphism `φ : X → B`. The members of the family are the **fibers**
`φ⁻¹(b)` for points `b ∈ B`, which "vary" as `b` moves in the base.

This perspective is already captured in Mathlib4 by two complementary mechanisms:

1. **`AlgebraicGeometry.Scheme.Over B`** — the typeclass that equips a scheme `X` with
   a structure morphism `X ↘ B : X ⟶ B`. This is the "family over B" perspective.
2. **`AlgebraicGeometry.Scheme.Hom.fiber`** — given a morphism `f : X ⟶ Y` and a point
   `y : Y`, the scheme-theoretic fiber `f.fiber y` is the pullback
   `X ×_Y Spec κ(y)`. This recovers the individual member of the family.

More generally, for any category `C`, the **over-category** `Over B` (from
`CategoryTheory.Comma.Over`) formalizes the idea that any arrow `X → B` can be
viewed as a family of objects parametrized by `B`.

## Main Definitions
* `Family B` — a scheme `X` equipped with a morphism `π : X → B` to the base `B`
  (essentially `Scheme.Over B` with a geometric name).
* `Family.fiber` — given a family `F : Family B` and a point `b : B`, the
  scheme-theoretic fiber `F.fiber b` is the member of the family over `b`.

## Mathlib4 Cross-References
* `AlgebraicGeometry.Scheme.Over` — scheme equipped with a structure morphism to a base
* `AlgebraicGeometry.Scheme.Hom.fiber` — scheme-theoretic fiber of a morphism
* `CategoryTheory.Over` — the over-category (comma category `C ↓ B`)
* `CategoryTheory.Limits.pullback` — the pullback construction used to define fibers
-/

open AlgebraicGeometry
open CategoryTheory

noncomputable section

universe u

/-- A **family of schemes parametrized by `B`** is a scheme `X` together with
a morphism `π : X → B` called the **structure morphism**.

This is a thin wrapper around `Scheme.Over B`; the name `Family` emphasizes
the geometric perspective: the preimages `π⁻¹(b)` (scheme-theoretic fibers)
are the individual members of the family, which vary as `b` moves in `B`.

For example:
- The projection `A¹ × B → B` is the trivial family with fiber `A¹`.
- A blow-up `Bl_Z(X) → X` is a family whose generic fiber is a point and
  whose special fiber over `Z` is a projective space.
- A smooth proper morphism is a family of smooth proper varieties. -/
abbrev Family (B : Scheme.{u}) : Type (u+1) := Scheme.Over B

namespace Family

variable {B : Scheme.{u}} (F : Family B)

/-- The total space of the family. -/
abbrev totalSpace : Scheme.{u} := F.left

/-- The structure morphism (projection to the base) of the family. -/
abbrev π : F.totalSpace ⟶ B := F.hom

/-- The scheme-theoretic fiber of the family over a point `b : B`.
This is the member of the family sitting over `b`. -/
abbrev fiber (b : B) : Scheme.{u} := π.fiber b

/-- The inclusion of the fiber into the total space. -/
abbrev fiberι (b : B) : F.fiber b ⟶ F.totalSpace := (π.fiberι b)

end Family

/-! ## Examples -/

section Examples

open AlgebraicGeometry

/-- **Example 1: The trivial family.**
The projection `X × B → B` is a family with constant fiber `X`.
This is the "constant" or "trivial" family. -/
example (X B : Scheme.{u}) [HasProducts.{u} (Scheme.{u})] : Family B where
  hom := Limits.prod.snd

/-- **Example 2: The identity family.**
The identity `B → B` is a family whose fibers are single reduced points
(`Spec κ(b)` for each `b ∈ B`). This is sometimes called the "tautological family"
over the base. -/
example (B : Scheme.{u}) : Family B where
  hom := 𝟙 B

/-- **Example 3: The diagonal as a family.**
The diagonal embedding `Δ : X → X × X` can be viewed as a family over the second factor,
whose fiber over a point `x` is `Spec κ(x)` sitting inside `X`. -/
example (X : Scheme.{u}) [HasProducts.{u} (Scheme.{u})] : Family (X ⨯ X) where
  hom := Limits.prod.lift (𝟙 X) (𝟙 X)

/-- **Example 4: Accessing fibers.**
If `F` is a family over `B` and `b` is a point of `B`, then `F.fiber b` gives the
member of the family over `b`. -/
example (B : Scheme.{u}) (F : Family B) (b : B) : Scheme.{u} := F.fiber b

/-- **Example 5: Base change produces a new family.**
Given a family `F : Family B` and a morphism `g : B' → B`, the pullback
`F.totalSpace ×_B B' → B'` is a family over `B'`. This is called the
**base change** of the family. -/
example (B B' : Scheme.{u}) (F : Family B) (g : B' ⟶ B) [HasPullbacks.{u} (Scheme.{u})] :
    Family B' where
  hom := Limits.pullback.snd (fst := F.π) (snd := g)

end Examples
