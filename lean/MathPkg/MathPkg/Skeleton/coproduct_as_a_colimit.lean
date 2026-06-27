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
abbrev CofanAsColimit (f : β → C) : Type _ := by
  sorry
