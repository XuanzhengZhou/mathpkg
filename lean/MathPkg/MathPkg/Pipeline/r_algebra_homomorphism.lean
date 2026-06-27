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
    [Algebra R A] [Algebra R B] :=
  A →ₐ[R] B

namespace RAlgHom

variable {R A B : Type*} [CommSemiring R] [Semiring A] [Semiring B]
  [Algebra R A] [Algebra R B]

/-- An R-algebra homomorphism preserves the algebra structure:
`ϕ (algebraMap R A r) = algebraMap R B r`. -/
theorem commutes (f : RAlgHom R A B) (r : R) : f (algebraMap R A r) = algebraMap R B r :=
  f.commutes' r

end RAlgHom

/-! ## Examples -/

/-- Example: the identity map is an R-algebra homomorphism
from any R-algebra `A` to itself. -/
example (R A : Type*) [CommSemiring R] [Semiring A] [Algebra R A] : RAlgHom R A A :=
  AlgHom.id R A

/-- Example: for any R-algebra `A`, the algebra map `algebraMap R A : R → A`
is an R-algebra homomorphism from `R` to `A`. -/
example (R A : Type*) [CommSemiring R] [Semiring A] [Algebra R A] : RAlgHom R R A :=
  Algebra.ofId R A
