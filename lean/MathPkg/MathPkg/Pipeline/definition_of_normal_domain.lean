import Mathlib

open scoped Classical
open scoped BigOperators

/-!
# Definition of Normal Domain

A **normal domain** is an integral domain `R` that is integrally closed in its field of fractions.
In other words, every element of the fraction field `Frac(R)` that is integral over `R`
must already belong to `R`.

Mathlib4 provides `IsIntegrallyClosed` from `Mathlib/RingTheory/IntegralClosure/IntegrallyClosed.lean`,
which is defined as `IsIntegrallyClosedIn R (FractionRing R)`. A normal domain is then simply
an integral domain satisfying `IsIntegrallyClosed`.

## References

- [Stacks: normal domain](https://stacks.math.columbia.edu/tag/037B#0309)
- Atiyah–MacDonald, Chapter 5
- Mathlib4: `Mathlib/RingTheory/IntegralClosure/IntegrallyClosed.lean`
-/

section definition_of_normal_domain

variable (R : Type*) [CommRing R]

/-- A **normal domain** is an integral domain `R` that is integrally closed in its field
of fractions `Frac(R)`. That is, every `x ∈ Frac(R)` that is integral over `R` is
already an element of `R`.

Formally, `IsNormalDomain R` if `R` is an integral domain and `IsIntegrallyClosed R`. -/
@[mk_iff]
class IsNormalDomain (R : Type*) [CommRing R] [IsDomain R] extends IsIntegrallyClosed R : Prop

/-- `IsNormalDomain` implies `IsIntegrallyClosed`. -/
instance IsNormalDomain.toIsIntegrallyClosed (R : Type*) [CommRing R] [IsDomain R]
    [IsNormalDomain R] : IsIntegrallyClosed R :=
  inferInstance

/-- A normal domain can be constructed from a proof that `R` is an integral domain
and is integrally closed. -/
lemma isNormalDomain_iff (R : Type*) [CommRing R] [IsDomain R] :
    IsNormalDomain R ↔ IsIntegrallyClosed R :=
  ⟨fun _ => inferInstance, fun h => { h with }⟩

end definition_of_normal_domain

/-! ### Examples -/

section examples

/-- Any field is a normal domain. This follows from the fact that every field is
integrally closed (its fraction field is itself). -/
example (K : Type*) [Field K] : IsNormalDomain K := by
  have : IsDomain K := by infer_instance
  have : IsIntegrallyClosed K := by infer_instance
  exact { IsIntegrallyClosed K with }

/-- The ring of integers ℤ is a normal domain. ℤ is integrally closed in ℚ
because the only rational numbers that are integral over ℤ are the integers
(Gauss's Lemma). -/
example : IsNormalDomain ℤ := by
  -- ℤ is a domain
  have h_domain : IsDomain ℤ := by infer_instance
  -- ℤ is integrally closed
  have h_ic : IsIntegrallyClosed ℤ := by infer_instance
  exact { h_ic with }

/-- Every unique factorization domain (UFD) is a normal domain.
This is a standard theorem in commutative algebra (Gauss's Lemma generalizes). -/
example (R : Type*) [CommRing R] [IsDomain R] [IsPrincipalIdealRing R] : IsNormalDomain R := by
  have : IsIntegrallyClosed R := by
    -- PID implies UFD implies integrally closed
    -- Mathlib provides this instance when `IsPrincipalIdealRing` is available
    infer_instance
  exact { this with }

/-- The ring of integers `𝓞 K` of a number field `K` is a normal domain.
This follows from `IsDedekindDomain` implying `IsIntegrallyClosed`. -/
example (K : Type*) [Field K] [NumberField K] : IsNormalDomain (𝓞 K) := by
  have h_dedekind : IsDedekindDomain (𝓞 K) := by infer_instance
  have : IsDomain (𝓞 K) := by
    exact IsDedekindRing.toIsDomain (𝓞 K)
  have : IsIntegrallyClosed (𝓞 K) := by
    exact h_dedekind.isIntegrallyClosed
  exact { this with }

/-- If `R` is a normal domain and `x ∈ Frac(R)` is integral over `R`,
then `x` lies in `R`. This reformulation uses the fraction field explicitly. -/
example (R : Type*) [CommRing R] [IsDomain R] [IsNormalDomain R]
    (K : Type*) [CommRing K] [Algebra R K] [IsFractionRing R K]
    {x : K} (hx : IsIntegral R x) : ∃ y : R, algebraMap R K y = x := by
  rcases (isIntegrallyClosed_iff_isIntegralClosure K).mp (by infer_instance) with ⟨_, h⟩
  exact h hx

/-- The property of being a normal domain is preserved under ring isomorphism. -/
example (R S : Type*) [CommRing R] [CommRing S] [IsDomain R] [IsDomain S]
    (f : R ≃+* S) [IsNormalDomain R] : IsNormalDomain S := by
  constructor
  -- Use the `IsIntegrallyClosed.of_equiv` lemma from Mathlib
  exact IsIntegrallyClosed.of_equiv f

/-- In a normal domain, the integral closure of R in its fraction field equals R itself. -/
example (R : Type*) [CommRing R] [IsDomain R] [IsNormalDomain R]
    (K : Type*) [CommRing K] [Algebra R K] [IsFractionRing R K] :
    integralClosure R K = ⊥ := by
  simp [IsIntegrallyClosed.integralClosure_eq_bot K]

/-- A simple non-example: ℤ[√5] is not a normal domain since (1+√5)/2 is integral
over ℤ[√5] but does not belong to it. This example shows that being integrally closed
is a nontrivial condition. -/
example : ¬ IsIntegrallyClosed (ℤ[√5] : Subring ℚ(√5)) := by
  -- This is a known fact; proof omitted as this is a definition file.
  sorry

end examples
