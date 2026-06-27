import Mathlib

open scoped Classical

/-!
# Dedekind Domain

A **Dedekind domain** is an integral domain that is:
- Noetherian,
- integrally closed in its field of fractions, and
- has Krull dimension at most one (every nonzero prime ideal is maximal).

This is the typeclass `IsDedekindDomain` from Mathlib.
-/

/-! ### Basic properties from Mathlib -/

section dedekind_domain

variable (R : Type*) [CommRing R] [IsDedekindDomain R]

/-- Every principal ideal domain that is an integral domain is a Dedekind domain. -/
example : IsDedekindDomain ℤ := by
  sorry
