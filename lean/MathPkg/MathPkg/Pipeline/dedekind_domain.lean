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
  infer_instance

/-- A Dedekind domain is Noetherian. -/
example : IsNoetherian R R := by
  infer_instance

/-- In a Dedekind domain, nonzero prime ideals are maximal. -/
example (p : Ideal R) (hp : p ≠ ⊥) (hp' : p.IsPrime) : p.IsMaximal :=
  hp'.isMaximal hp

/-- Equivalent characterization: Noetherian + dimension ≤ 1 + integrally closed. -/
example : IsDedekindDomain ℤ ↔
    (IsDomain ℤ ∧ IsNoetherianRing ℤ ∧ Ring.DimensionLEOne ℤ ∧
      ∀ {x : ℚ}, IsIntegral ℤ x → ∃ y : ℤ, algebraMap ℤ ℚ y = x) :=
  isDedekindDomain_iff (K := ℚ) (A := ℤ)

end dedekind_domain
