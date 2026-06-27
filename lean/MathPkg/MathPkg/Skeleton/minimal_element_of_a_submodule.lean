/-
Copyright (c) 2024 MathPkg contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib

/-! # Minimal Element of a Submodule

Let `M` be a nonzero submodule of `k[x]²` (a rank-2 free module over the polynomial ring).
A **minimal element** of `M` with respect to a monomial order `>` is an element
`g ∈ M \ {0}` such that `LT(g)` is minimal among all nonzero leading terms of elements of `M`.

Here `LT(g)` denotes the leading term of `g` with respect to the monomial order `>`,
i.e., the unique monomial term of `g` whose exponent vector is maximal under `>`.
The monomial order is formalized via `MonomialOrder σ` (from `Mathlib/Data/Finsupp/MonomialOrder`),
which provides a well-ordering on exponent vectors `σ →₀ ℕ` compatible with addition.

This definition is fundamental in Gröbner basis theory for polynomial modules,
where one repeatedly picks minimal elements to construct Gröbner bases.

## Mathlib4 usage

Mathlib4 already defines:
* `MonomialOrder.degree f` -- the maximal exponent vector of `f` with respect to the order
* `MonomialOrder.leadingTerm f` -- the monomial term with that maximal exponent
* `MonomialOrder.leadingCoeff f` -- the coefficient of that term

The comparison `LT(g) ≼ LT(h)` between leading terms is equivalent to `m.degree g ≼[m] m.degree h`.

## Main definitions

* `IsMinimalElement m M g` -- `g` is a minimal element of the submodule `M` of `MvPolynomial σ k`
  with respect to monomial order `m`.  This means `g ∈ M`, `g ≠ 0`, and for every nonzero `h ∈ M`,
  `m.degree g ≼[m] m.degree h`.

## References

* [Cox, Little and O'Shea, *Ideals, varieties, and algorithms*][coxlittleoshea1997]
* [Becker and Weispfenning, *Gröbner bases*][Becker-Weispfenning1993]
-/

open scoped MonomialOrder

open MvPolynomial MonomialOrder

variable {σ R : Type*} [CommSemiring R] (m : MonomialOrder σ)

/-- A nonzero element `g` of a submodule `M` of `MvPolynomial σ R` is a **minimal element**
with respect to a monomial order `m` if its leading term is minimal among all nonzero elements.

Formally, `g ∈ M`, `g ≠ 0`, and for every nonzero `h ∈ M`,
`m.degree g ≼[m] m.degree h`.  Since `≼[m]` compares exponent vectors,
this means the leading term (which is determined by the degree vector) of `g`
is minimal with respect to `m`.

In the context of Gröbner bases, minimal elements are the irreducible residues
after the division algorithm — they cannot be further reduced by any other element. -/
def IsMinimalElement (M : Submodule R (MvPolynomial σ R)) (g : MvPolynomial σ R) : Prop := by
  sorry
