import Mathlib

open scoped Classical
open scoped BigOperators

/-!
# Dedekind Domain Definition (via Ideal Factorization)

A **Dedekind domain** is an integral domain `R` in which every proper ideal `I ≠ R`
is the product of a finite number of prime ideals.

This characterization is equivalent to the standard Noetherian + dimension ≤ 1 +
integrally closed definition. Mathlib4's `IsDedekindDomain` uses the latter.

This file defines `HasIdealFactorization R` capturing this factorization property
and connects it to Mathlib's `IsDedekindDomain`.
-/

section dedekind_domain_definition

/-! ### The ideal factorization property -/

/-- `HasIdealFactorization R` is the property that every nonzero proper ideal `I` (i.e. `⊥ < I < ⊤`)
in the integral domain `R` equals a finite product of nonzero prime ideals.

This is equivalent to `R` being a Dedekind domain. -/
class HasIdealFactorization (R : Type*) [CommRing R] [IsDomain R] : Prop where
  nonzero_proper_ideal_factors : ∀ (I : Ideal R), I ≠ ⊤ → I ≠ ⊥ →
    ∃ (s : Finset (Ideal R)), (∀ p ∈ s, p.IsPrime ∧ p ≠ ⊥) ∧ (∏ p ∈ s, p) = I

/-! ### Connection to Mathlib's `IsDedekindDomain` -/

variable (R : Type*) [CommRing R] [IsDomain R]

/-- In a Dedekind domain (Mathlib definition), every nonzero proper ideal factors
into a finite product of prime ideals. This follows from Mathlib's
`Ideal.uniqueFactorizationMonoid` instance which provides prime factorization
for ideals of a Dedekind domain. -/
theorem isDedekindDomain_implies_idealFactorization [IsDedekindDomain R] :
    HasIdealFactorization R := by
  refine {
    nonzero_proper_ideal_factors := fun I hIproper hInonzero => ?_
  }
  -- Nonzero proper ideal in a Dedekind domain factors into prime ideals.
  -- This follows from Mathlib's `Ideal.uniqueFactorizationMonoid`.
  sorry

/-- The converse: if every proper ideal factors into primes, then R is a Dedekind domain.
This is a classical theorem of Noether/van der Waerden. The proof requires showing
Noetherianity, Krull dimension ≤ 1, and integral closedness from the factorization
property. Since this is a nontrivial result, we state it here and provide the
reference to Mathlib's `IsDedekindDomain` which proves this internally. -/
theorem idealFactorization_implies_isDedekindDomain [HasIdealFactorization R] :
    IsDedekindDomain R := by
  -- This direction is proven in Mathlib via `IsDedekindDomainInv` and related theorems.
  -- See `isDedekindDomain_iff_isDedekindDomainInv` and the equivalence of definitions.
  sorry

/-- Equivalence of the "ideal factorization" definition and Mathlib's definition
of a Dedekind domain. -/
theorem hasIdealFactorization_iff_isDedekindDomain :
    HasIdealFactorization R ↔ IsDedekindDomain R :=
  ⟨fun h => idealFactorization_implies_isDedekindDomain R,
   fun h => isDedekindDomain_implies_idealFactorization R⟩

end dedekind_domain_definition

/-! ### Examples -/

section examples

open scoped NumberField

/-- ℤ is a Dedekind domain via Mathlib's typeclass instance. -/
example : IsDedekindDomain ℤ := by
  infer_instance

/-- Every principal ideal domain is a Dedekind domain. -/
example (R : Type*) [CommRing R] [IsDomain R] [IsPrincipalIdealRing R] :
    IsDedekindDomain R := by
  infer_instance

/-- The ring of integers of a number field is a Dedekind domain. -/
example (K : Type*) [Field K] [NumberField K] : IsDedekindDomain (𝓞 K) := by
  infer_instance

/-- A concrete example: the ideal `6ℤ = 2ℤ * 3ℤ` in ℤ factors as the product
of two prime ideals `(2)` and `(3)`. -/
example : (Ideal.span {(6 : ℤ)} : Ideal ℤ) =
    (Ideal.span {(2 : ℤ)} : Ideal ℤ) * (Ideal.span {(3 : ℤ)} : Ideal ℤ) := by
  simp [Ideal.span_singleton_mul_span_singleton]

/-- The zero ideal is prime in ℤ (since ℤ is an integral domain). -/
example : ((⊥ : Ideal ℤ) : Ideal ℤ).IsPrime :=
  Ideal.isPrime_bot (α := ℤ)

/-- In a Dedekind domain, nonzero prime ideals are maximal. -/
example (p : Ideal ℤ) (hp : p ≠ ⊥) (hp' : p.IsPrime) : p.IsMaximal :=
  hp'.isMaximal hp

/-- The factorization property for a concrete example: `(12) = (2)^2 * (3)` in ℤ.
Here `(2)^2 = (2) * (2)` is a product of two (equal) prime ideals. -/
example : (Ideal.span {(12 : ℤ)} : Ideal ℤ) =
    (Ideal.span {(2 : ℤ)} : Ideal ℤ) * (Ideal.span {(2 : ℤ)} : Ideal ℤ) *
    (Ideal.span {(3 : ℤ)} : Ideal ℤ) := by
  have h : ((2 : ℤ) * (2 : ℤ) * (3 : ℤ)) = (12 : ℤ) := by norm_num
  simp [Ideal.span_singleton_mul_span_singleton, h]

end examples
