import Mathlib

open Ideal

/-!
# Fundamental Equality for Complete Discrete Valuations

Let `E` be a finite extension of `K`, `v` a discrete nonarchimedean absolute value on `K`,
and `w` a discrete nonarchimedean absolute value on `E` extending `v`.
If `K` is complete with respect to `v`, then `e(w:v) · f(w:v) = [E:K]`.

In the language of Dedekind domains: given a Dedekind domain `R` with fraction field `K`,
and its integral closure `S` in a finite extension `L/K`, if `S` is a local ring
(i.e., a discrete valuation ring, which corresponds to `K` being complete), then
for any maximal ideal `p` of `R`,
`ramificationIdx p (maximalIdeal S) * inertiaDeg p (maximalIdeal S) = finrank K L`.
-/

theorem fundamental_equality_for_complete_discrete_valuations
    {R S : Type u} [CommRing R] [CommRing S] [Algebra R S]
    {K L : Type*} [Field K] [Field L] [Algebra K L]
    [IsDedekindDomain R] [IsDedekindDomain S]
    [Algebra R K] [IsFractionRing R K] [Algebra S L] [IsFractionRing S L]
    [Algebra R L] [IsScalarTower R S L] [IsScalarTower R K L]
    [Module.Finite R S] [IsLocalRing S] {p : Ideal R} [p.IsMaximal] (hp0 : p ≠ ⊥) :
    ramificationIdx p (IsLocalRing.maximalIdeal S) *
    inertiaDeg p (IsLocalRing.maximalIdeal S) = Module.finrank K L := by
  sorry
