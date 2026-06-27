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
noncomputable abbrev ModuleAsChainComplex (n : ℕ) : ChainComplex (ModuleCat R) ℕ := by
  sorry
