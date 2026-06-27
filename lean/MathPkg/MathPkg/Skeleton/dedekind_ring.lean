import Mathlib

open scoped Classical

/-!
# Dedekind Ring

A **Dedekind ring** (Dedekind domain) is an integral domain in which every nonzero
ideal can be written uniquely as a product of prime ideals.

Mathlib4 formalizes this via `IsDedekindDomain R`, defined using the equivalent
characterization: Noetherian, integrally closed in its fraction field, and Krull
dimension at most one. The equivalence to unique factorization of ideals is proved
via `Ideal.uniqueFactorizationMonoid` in
`Mathlib/RingTheory/DedekindDomain/Ideal/Basic.lean`.

## Main definitions

* `IsDedekindRing R` — Mathlib4 typeclass: Noetherian, dim ≤ 1, integrally closed
  (no IsDomain hypothesis required).
* `IsDedekindDomain R` — extends `IsDedekindRing R` + `IsDomain R`. This is the
  standard definition of a Dedekind ring as an integral domain.
* `DedekindRing R` — abbreviation for `IsDedekindDomain R`, matching the
  knowledge-graph formulation (integral domain with unique ideal factorization).

## References

* [D. Marcus, *Number Fields*][marcus1977number]
* [J. Neukirch, *Algebraic Number Theory*][Neukirch1992]
-/

section dedekind_ring_definition

/-- `DedekindRing R` is the property that `R` is a Dedekind domain, i.e. an integral
domain in which every nonzero proper ideal factors uniquely as a product of prime ideals.

This is an abbreviation for Mathlib4's `IsDedekindDomain R`, which uses the equivalent
Noetherian + integrally closed + Krull dimension ≤ 1 characterization and proves the
ideal-factorization equivalence via `Ideal.uniqueFactorizationMonoid`. -/
abbrev DedekindRing (R : Type*) [CommRing R] [IsDomain R] : Prop := IsDedekindDomain R

end dedekind_ring_definition

/-! ### Examples -/

section examples

open scoped NumberField

/-- `ℤ` is a Dedekind ring. Mathlib4 provides the instance via
`IsPrincipalIdealRing.isDedekindDomain`. -/
example : DedekindRing ℤ := by
  sorry
