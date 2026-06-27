import Mathlib
import Mathlib.GroupTheory.Nilpotent
import Mathlib.GroupTheory.Abelianization.Defs
import Mathlib.GroupTheory.GroupExtension.Defs

open Subgroup

universe u

/-!
# Nilpotent Extension Property

Let `P` be a property of groups that is closed under forming extensions and under taking quotients.
If `G` is a nilpotent group and its abelianization `G_ab` satisfies `P`, then `G` itself
satisfies `P`.

This is a fundamental result in the theory of group extensions and nilpotent groups,
closely related to the concept of a *saturated formation* in finite group theory.

## References
- P. Hall, "A Contribution to the Theory of Groups of Prime-Power Order", 1934
- H. Heineken, L. Kurdachenko, J. Otal, I. Subbotin,
  "Groups with Prescribed Quotient Groups and Associated Module Theory"

## Main definitions
* `IsExtensionClosed P` : a property `P` is closed under forming group extensions
* `IsQuotientClosed P` : a property `P` is closed under taking quotients

## Main theorem
* `nilpotent_extension_property` : For an extension-closed and quotient-closed property `P`,
  if `G` is nilpotent and `G_ab` satisfies `P`, then `G` satisfies `P`.

## Mathlib4 References
- `GroupExtension` : `Mathlib/GroupTheory/GroupExtension/Defs.lean`
- `Abelianization` : `Mathlib/GroupTheory/Abelianization/Defs.lean`
- `lowerCentralSeries` : `Mathlib/GroupTheory/Nilpotent.lean`
- `IsNilpotent` : `Mathlib/GroupTheory/Nilpotent.lean`
-/


/-- A property `P` of groups is closed under forming extensions if for any group extension
`1 → N → E → Q → 1` (a short exact sequence of groups), whenever both `N` and `Q` have `P`,
then `E` also has `P`. -/
def IsExtensionClosed (P : ∀ (G : Type u) [Group G], Prop) : Prop := by
  sorry
