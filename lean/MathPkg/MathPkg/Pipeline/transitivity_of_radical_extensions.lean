/-
  Translation of: Transitivity of Radical Extensions
  Source concept ID: transitivity_of_radical_extensions

  If K/F is a radical extension and L/K is a radical extension,
  then L/F is a radical extension.

  Dependencies: radical extension
-/

import Mathlib

/--
  Transitivity of radical extensions: if K/F and L/K are radical
  field extensions, then L/F is also a radical extension.

  Here `F`, `K`, `L` are fields with algebra structures making them
  field extensions: `F ⊆ K ⊆ L`.  The predicate `IsRadicalExtension`
  asserts that the larger field is obtained from the smaller one
  by repeatedly adjoining radicals (n-th roots of elements).
-/
theorem transitivity_of_radical_extensions {F K L : Type*} [Field F] [Field K] [Field L]
    [Algebra F K] [Algebra K L] [IsScalarTower F K L]
    [IsRadicalExtension F K] [IsRadicalExtension K L] :
    IsRadicalExtension F L := by
  sorry
