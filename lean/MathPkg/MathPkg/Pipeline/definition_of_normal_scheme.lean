import Mathlib

open AlgebraicGeometry

/-!
# Definition of Normal Scheme

A scheme `X` is **normal** if all its local rings (stalks) are integrally closed domains.
Equivalently, for every point `x : X`, the local ring `𝒪_{X, x}` is a normal domain:
it is an integral domain and is integrally closed in its field of fractions.

## Main Definition
* `AlgebraicGeometry.IsNormal` -- the predicate that a scheme is normal

## Mathlib4 Cross-References
* `IsIntegrallyClosed` in `RingTheory/IntegralClosure/IntegrallyClosed.lean`
  -- integrally closed ring (defined via `IsIntegralClosure R R (FractionRing R)`)
* `IsDomain` in `Algebra/Domain/Defs.lean` -- integral domain typeclass
* `AlgebraicGeometry.IsReduced` in `AlgebraicGeometry/Properties.lean`
  -- reduced scheme (similar stalk-based pattern)
* `AlgebraicGeometry.IsIntegral` in `AlgebraicGeometry/Properties.lean`
  -- integral scheme (all nonempty open sections are integral domains)
* `FractionRing` in `RingTheory/Localization/FractionRing.lean`
  -- total ring of fractions of a commutative ring

## References
* [Stacks: normal scheme](https://stacks.math.columbia.edu/tag/033H)
* [Stacks: normal domain](https://stacks.math.columbia.edu/tag/037B#0309)
-/

/-- A scheme `X` is **normal** if all its local rings are integrally closed domains.

For every point `x : X`, the stalk `X.presheaf.stalk x` must be an integral domain
(`IsDomain`) and integrally closed in its field of fractions (`IsIntegrallyClosed`).

This is equivalent to the condition that for every `x`, the local ring `𝒪_{X, x}` is
a normal domain. -/
class AlgebraicGeometry.IsNormal (X : Scheme) : Prop where
  /-- Every stalk is an integral domain. -/
  stalk_isDomain : ∀ x : X, IsDomain (X.presheaf.stalk x)
  /-- Every stalk is integrally closed in its fraction field. -/
  stalk_isIntegrallyClosed : ∀ x : X, IsIntegrallyClosed (X.presheaf.stalk x)

section examples

open AlgebraicGeometry

/-- The affine line over a field `K` is normal when `K` is algebraically closed.
  The scheme `Spec K[t]` has stalks that are localizations of the polynomial ring,
  which are normal domains. -/
example (K : Type*) [Field K] : AlgebraicGeometry.IsNormal (Spec (CommRingCat.of (Polynomial K))) := by
  refine {
    stalk_isDomain := ?_,
    stalk_isIntegrallyClosed := ?_
  }
  · -- Each stalk is a localization of a polynomial ring over a field, hence a domain
    intro x
    -- `X.presheaf.stalk x ≅ Localization.AtPrime (PrimeSpectrum.asIdeal x)`
    -- For Spec of a polynomial ring over a field, these localizations are domains.
    -- Proof omitted as this is a definition file.
    sorry
  · -- Each stalk is integrally closed (polynomial rings over fields are normal)
    intro x
    sorry

/-- The spectrum of the integers `Spec ℤ` is a normal scheme.
  Its stalks are `ℤ_{(p)}` (or `ℚ` at the generic point), which are normal domains. -/
example : AlgebraicGeometry.IsNormal (Spec (CommRingCat.of ℤ)) := by
  refine {
    stalk_isDomain := ?_,
    stalk_isIntegrallyClosed := ?_
  }
  · intro x
    -- Stalk of Spec ℤ at any point is a localization of ℤ, hence a domain.
    sorry
  · intro x
    -- ℤ is integrally closed, and this is preserved under localization.
    sorry

/-- Using the definition: extract that a stalk of a normal scheme is integrally closed. -/
example (X : Scheme) [AlgebraicGeometry.IsNormal X] (x : X) :
    IsIntegrallyClosed (X.presheaf.stalk x) :=
  AlgebraicGeometry.IsNormal.stalk_isIntegrallyClosed x

/-- Using the definition: extract that a stalk of a normal scheme is a domain. -/
example (X : Scheme) [AlgebraicGeometry.IsNormal X] (x : X) :
    IsDomain (X.presheaf.stalk x) :=
  AlgebraicGeometry.IsNormal.stalk_isDomain x

end examples
