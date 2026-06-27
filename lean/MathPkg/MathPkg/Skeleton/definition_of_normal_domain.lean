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
    [IsNormalDomain R] : IsIntegrallyClosed R := by
  sorry
