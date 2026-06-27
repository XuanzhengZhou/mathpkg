import Mathlib

/-!
# R-Algebra Homomorphism

Let `R` be a commutative semiring, and let `A` and `B` be `R`-algebras
(that is, semirings equipped with algebra maps `algebraMap R A : R → A`
and `algebraMap R B : R → B`).

An **R-algebra homomorphism** `ϕ : A →ₐ[R] B` is a ring homomorphism
`ϕ : A →+* B` such that `ϕ (algebraMap R A r) = algebraMap R B r` for all `r : R`.
In other words, `ϕ ∘ (algebraMap R A) = algebraMap R B`.

Mathlib4 provides `AlgHom R A B` (notation `A →ₐ[R] B`) in
`Mathlib/Algebra/Algebra/Hom.lean` for exactly this purpose.
We define `RAlgHom` as a type alias to make the terminology explicit.
-/

/-- An R-algebra homomorphism between `R`-algebras `A` and `B` is a ring homomorphism
`A →+* B` that commutes with the algebra maps. This is exactly `AlgHom R A B`
from Mathlib4. -/
abbrev RAlgHom (R A B : Type*) [CommSemiring R] [Semiring A] [Semiring B]
    [Algebra R A] [Algebra R B] : Type _ := by
  sorry
