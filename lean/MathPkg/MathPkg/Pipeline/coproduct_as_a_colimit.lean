import Mathlib

open scoped Classical
open CategoryTheory
open CategoryTheory.Limits

/-!
# Coproduct as a colimit

The **coproduct** of a family of objects `B_i` (for `i : β`) in a category `C`, denoted
`∐_i B_i`, is the colimit of the discrete diagram consisting of the objects `B_i`
together with only their identity morphisms.

Mathlib4 defines this natively:
- `HasCoproduct f` is an abbreviation for `HasColimit (Discrete.functor f)`
- `Cofan f` is an abbreviation for `Cocone (Discrete.functor f)`
- `coproductIsCoproduct f` proves that the cofan built from `Sigma.ι` is colimiting.

Thus in Mathlib4 the coproduct **is** the colimit of the discrete diagram — it is not
a separate construction but exactly the same concept.

## Main definitions

* `coproductAsColimit f` — the coproduct object `∐ f`, equal to `colimit (Discrete.functor f)`
* `HasCoproductAsColimit f` — typeclass asserting the colimit exists
* `CofanAsColimit` — a cofan = a cocone over the discrete diagram
-/

section coproduct_as_a_colimit

variable {C : Type u} [Category.{v} C]
variable {β : Type w} (f : β → C)

/-- A cofan over `f : β → C` is exactly a cocone over the discrete diagram `Discrete.functor f`.
This is the standard Mathlib4 definition. -/
abbrev CofanAsColimit (f : β → C) :=
  Cofan f

/-- The coproduct of `f : β → C` is the colimit of the discrete diagram `Discrete.functor f`.
Mathlib4 defines `HasCoproduct f` as `HasColimit (Discrete.functor f)`, so the coproduct
**is** literally the colimit. -/
abbrev HasCoproductAsColimit (f : β → C) :=
  HasCoproduct f

/-- The coproduct object `∐ f`, which is the colimit of the discrete diagram. -/
abbrev coproductAsColimit (f : β → C) [HasCoproduct f] : C :=
  ∐ f

/-- The injection `ι_b : f b ⟶ ∐ f` for `b : β`, coming from the colimit cocone. -/
abbrev coproductAsColimit.inj (f : β → C) [HasCoproduct f] (b : β) : f b ⟶ coproductAsColimit f :=
  Sigma.ι f b

/-- The cofan built from the coproduct inclusions is colimiting.
This is `coproductIsCoproduct` from Mathlib4, which proves that the coproduct
cofan is indeed a colimit of the discrete diagram. -/
example (f : β → C) [HasCoproduct f] : IsColimit (Cofan.mk (∐ f) (Sigma.ι f)) :=
  coproductIsCoproduct f

/-- The coproduct object `∐ f` is definitionally equal to `colimit (Discrete.functor f)`.
(Technically it depends on the `HasCoproduct` instance, which selects a particular colimit.) -/
example (f : β → C) [HasCoproduct f] : coproductAsColimit f = ∐ f :=
  rfl

/-- `HasCoproduct f` is literally `HasColimit (Discrete.functor f)` — the coproduct
is the colimit of the discrete diagram, not a separate concept. -/
example (f : β → C) : (HasCoproduct f : Prop) ↔ (HasColimit (Discrete.functor f) : Prop) := by
  rfl

end coproduct_as_a_colimit
