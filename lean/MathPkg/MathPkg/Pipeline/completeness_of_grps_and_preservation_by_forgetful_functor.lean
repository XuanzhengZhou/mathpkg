import Mathlib

open CategoryTheory
open CategoryTheory.Limits

/-!
# Completeness of Grps and preservation by the forgetful functor

The category `GroupCat` of groups is complete: every (small) diagram in `GroupCat`
admits a limit. Moreover, the forgetful functor `forget GroupCat : GroupCat ⥤ Type`
preserves all limits — the underlying set of a limit of groups is the limit of the
underlying sets, endowed with the pointwise group structure.
-/

section completeness_of_grps_and_preservation_by_forgetful_functor

/-- **Completeness of Grps and preservation by the forgetful functor.**
The category of groups is complete (has all small limits), and the forgetful
functor from groups to sets preserves those limits. -/
theorem completeness_of_grps_and_preservation_by_forgetful_functor :
    HasLimits GroupCat.{u} ∧ PreservesLimits (forget GroupCat.{u}) := by
  sorry

end completeness_of_grps_and_preservation_by_forgetful_functor
