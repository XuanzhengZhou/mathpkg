import Mathlib

open scoped Classical

/-!
# Module as a Complex

An R-module M may be considered as a (chain) complex with only one nonzero term
(all other terms zero). Concretely, for an `R`-module `M` and a degree `j : ι`,
we place `M` in degree `j` and the zero object in all other degrees, with all
differentials equal to zero.

Mathlib4 provides `HomologicalComplex.single V c j` — a functor from `V` to
`HomologicalComplex V c` that constructs a complex supported in a single degree `j`.

We define convenient abbreviations:
- `ModuleAsChainComplex R M n` — the chain complex with `M` concentrated in degree `n`
- `ModuleAsCochainComplex R M n` — the cochain complex with `M` concentrated in degree `n`
-/

open CategoryTheory

section module_as_complex

variable (R : Type*) [Ring R] (M : Type*) [AddCommGroup M] [Module R M]

/-- View an `R`-module `M` as a chain complex (downward ℕ-indexed) concentrated in degree `n`.
All other degrees are zero, and all differentials are zero. -/
noncomputable abbrev ModuleAsChainComplex (n : ℕ) : ChainComplex (ModuleCat R) ℕ :=
  (HomologicalComplex.single (ModuleCat R) (ComplexShape.down ℕ) n).obj (ModuleCat.of R M)

/-- View an `R`-module `M` as a cochain complex (upward ℕ-indexed) concentrated in degree `n`.
All other degrees are zero, and all differentials are zero. -/
noncomputable abbrev ModuleAsCochainComplex (n : ℕ) : CochainComplex (ModuleCat R) ℕ :=
  (HomologicalComplex.single (ModuleCat R) (ComplexShape.up ℕ) n).obj (ModuleCat.of R M)

end module_as_complex

section examples

variable (R : Type*) [Ring R]

/-- Example: The ℤ-module ℤ viewed as a chain complex concentrated in degree 0.
The resulting chain complex has ℤ at index 0, and 0 at all other indices. -/
example : ChainComplex (ModuleCat ℤ) ℕ :=
  ModuleAsChainComplex ℤ ℤ 0

/-- Example: The ℤ-module ℤ viewed as a cochain complex concentrated in degree 0. -/
example : CochainComplex (ModuleCat ℤ) ℕ :=
  ModuleAsCochainComplex ℤ ℤ 0

/-- In the chain complex `ModuleAsChainComplex R M n`, the object at degree `n` is `M`. -/
example (M : Type*) [AddCommGroup M] [Module R M] (n : ℕ) :
    ((ModuleAsChainComplex R M n).X n) = ModuleCat.of R M := rfl

/-- In the chain complex `ModuleAsChainComplex R M n`, the object at any other degree is 0. -/
example (M : Type*) [AddCommGroup M] [Module R M] (n m : ℕ) (h : m ≠ n) :
    IsZero ((ModuleAsChainComplex R M n).X m) :=
  HomologicalComplex.isZero_single_obj_X (ModuleCat R) (ComplexShape.down ℕ) n
    (ModuleCat.of R M) m h

/-- All differentials of `ModuleAsChainComplex R M n` are zero. -/
example (M : Type*) [AddCommGroup M] [Module R M] (n i j : ℕ) :
    ((ModuleAsChainComplex R M n).d i j) = 0 := rfl

/-- Using the `single₀` abbreviation from Mathlib: chain complex supported in degree 0. -/
example (M : Type*) [AddCommGroup M] [Module R M] :
    ChainComplex (ModuleCat R) ℕ :=
  (ChainComplex.single₀ (ModuleCat R)).obj (ModuleCat.of R M)

end examples
