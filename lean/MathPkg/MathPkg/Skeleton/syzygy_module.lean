import Mathlib

open scoped Classical

/-!
# Syzygy Module

For a set of polynomials (or more generally, elements) f₁, ..., f_t in a commutative ring R,
the **syzygy module** Syz(f₁, ..., f_t) is the set of all (h₁, ..., h_t) ∈ R^t such that
h₁f₁ + ... + h_t f_t = 0.

In more abstract terms: given a commutative ring `R` and a family `f : ι → R`, the syzygy
module is the kernel of the `R`-linear map `(ι →₀ R) →ₗ[R] R` that sends a finitely supported
function `h : ι →₀ R` to `∑ᵢ hᵢ • fᵢ`. This is exactly `LinearMap.ker (Finsupp.linearCombination R f)`.

## Mathlib4 correspondence

Mathlib4 already provides all the ingredients:
- `Finsupp.linearCombination R f` is the `R`-linear map `(ι →₀ R) →ₗ[R] R` sending a
  finitely-supported function to the linear combination of the `f i`.
- `LinearMap.ker` gives the submodule of relations (syzygies).
- The syzygy module is a submodule of the free `R`-module `(ι →₀ R)`.

This file:
1. Defines `Syz R f` as a `Submodule R (ι →₀ R)`.
2. Proves the membership condition: `h ∈ Syz R f ↔ (Finsupp.linearCombination R f) h = 0`.
3. Provides examples.
-/

section syzygy_module

variable {ι R : Type*} [CommRing R] (f : ι → R)

/-- The **syzygy module** of a family `f : ι → R` of elements in a commutative ring `R`.
It is the submodule of `(ι →₀ R)` consisting of all finitely-supported functions
`h : ι →₀ R` such that `∑ᵢ hᵢ • fᵢ = 0`. -/
noncomputable def Syz (f : ι → R) : Submodule R (ι →₀ R) := by
  sorry
