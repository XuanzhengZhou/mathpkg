import Mathlib

/-!
# R-linear Derivation

If `S` is an `R`-algebra, a derivation `d : S → M` is **R-linear** if it is a map of
`R`-modules.  The set of all R-linear derivations from `S` to `M` is denoted
`Der_R(S, M)`.

Mathlib4 already encodes R-linearity in the `Derivation` structure:
`Derivation R S M` extends `S →ₗ[R] M`.  Therefore every `Derivation R S M`
is automatically R-linear.  We provide a convenient type alias `Der_R`
that makes the notation explicit.

-/

open Algebra

/-- `Der_R R S M` is an alias for `Derivation R S M`, the type of
R-linear derivations from the `R`-algebra `S` into the `R`-module `M`.

A `Derivation R S M` satisfies
1. `R`-linearity: it is an `R`-module map `S → M`,
2. Leibniz rule: `d (a * b) = a • d b + b • d a`,
3. `d 1 = 0`. -/
abbrev Der_R (R S M : Type*)
    [CommSemiring R] [CommSemiring S] [AddCommMonoid M]
    [Algebra R S] [Module S M] [Module R M] :=
  Derivation R S M

namespace Der_R

/-- An example: the zero derivation is R-linear. -/
example (R S M : Type*)
    [CommSemiring R] [CommSemiring S] [AddCommMonoid M]
    [Algebra R S] [Module S M] [Module R M] : Der_R R S M :=
  0

/-- An example: any `Derivation R S M` (as defined in Mathlib) is a `Der_R R S M`. -/
example (R S M : Type*) [CommSemiring R] [CommSemiring S] [AddCommMonoid M]
    [Algebra R S] [Module S M] [Module R M] (d : Derivation R S M) : Der_R R S M :=
  d

/-- An example showing R-linearity: the derivation is an R-linear map. -/
example (R S M : Type*) [CommSemiring R] [CommSemiring S] [AddCommMonoid M]
    [Algebra R S] [Module S M] [Module R M] (d : Der_R R S M) (r : R) (x y : S) :
    d (r • x + y) = r • d x + d y := by
  simp

end Der_R
