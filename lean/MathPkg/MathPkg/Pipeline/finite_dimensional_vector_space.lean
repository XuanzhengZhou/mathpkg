import Mathlib

/-!
# Finite-Dimensional Vector Space

If `V` has a finite basis over a division ring `K`, then `V` is said to be a
**finite-dimensional** vector space over `K`.

Mathlib4 already provides `FiniteDimensional K V` as an abbreviation for
`Module.Finite K V` (see `Mathlib/LinearAlgebra/FiniteDimensional/Defs.lean`).
The connection to the existence of a finite basis is given by
`Module.Basis.finiteDimensional_of_finite`:
a vector space with a basis indexed by a finite type is finite-dimensional.

## Main definitions

* `FiniteDimensional K V` -- the typeclass asserting `V` is finite-dimensional over `K`.
* `Module.Basis.finiteDimensional_of_finite` -- a vector space with a finite basis
  is finite-dimensional.
* `finrank K V` -- the dimension of a finite-dimensional space as a natural number.
-/

open FiniteDimensional

variable (K V : Type*) [DivisionRing K] [AddCommGroup V] [Module K V]

/--
`FiniteDimensional K V` is Mathlib4's typeclass for a finite-dimensional vector space.
It is defined as `Module.Finite K V`, meaning `V` is finitely generated as a `K`-module.
Equivalently, `V` admits a finite basis.
-/
#check FiniteDimensional K V

-- The fundamental theorem linking finite bases to finite-dimensionality:
#check Module.Basis.finiteDimensional_of_finite

/-! ## Examples -/

/-- `Fin n → K` is finite-dimensional over `K` (dimension = n). -/
example (K : Type*) [DivisionRing K] (n : ℕ) : FiniteDimensional K (Fin n → K) := by
  infer_instance

/-- Any vector space with a finite basis is finite-dimensional.
This example constructs a basis for `K × K` over `K` and deduces finite-dimensionality. -/
example (K : Type*) [DivisionRing K] : FiniteDimensional K (K × K) :=
  have _ : Finite (Fin 2) := inferInstance
  (Module.Basis.finiteDimensional_of_finite (Pi.basisFun K (Fin 2)))

/-- The field `K` itself is finite-dimensional over `K` (dimension = 1). -/
example (K : Type*) [DivisionRing K] : FiniteDimensional K K := by
  infer_instance

/-- A subspace of a finite-dimensional vector space is also finite-dimensional. -/
example (K V : Type*) [DivisionRing K] [AddCommGroup V] [Module K V] [FiniteDimensional K V]
    (W : Submodule K V) : FiniteDimensional K W := by
  infer_instance

/-- If a finite-dimensional space has a basis indexed by `Fin n`, then `finrank K V = n`. -/
example (K V : Type*) [DivisionRing K] [AddCommGroup V] [Module K V] (n : ℕ)
    (h : Basis (Fin n) K V) : finrank K V = n :=
  Module.finrank_eq_card_basis h
