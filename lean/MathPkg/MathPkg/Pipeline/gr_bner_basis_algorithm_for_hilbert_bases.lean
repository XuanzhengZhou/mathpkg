import Mathlib

open scoped MonomialOrder

/-!
# Gröbner Basis Algorithm for Hilbert Bases

Let `G` be a Gröbner basis for the ideal `I` with respect to any elimination
order `>` for which all `z_i, t > v_j` and all `v_j > w_k`.  Let `S` be the
subset of `G` consisting of binomials `v^α - w^α` for `α ∈ ℤ_{≥0}^N`.
Then `H = {α : v^α - w^α ∈ S}` is the Hilbert basis for `K`.

This is Theorem 1.11 from Sturmfels' "Gröbner Bases and Convex Polytopes",
which establishes that the exponent vectors of the binomials in a Gröbner basis
of a toric ideal form a Hilbert basis for the corresponding rational cone.

## Dependencies

* `initialSubmodule` — initial ideal / leading term ideal
* `IsHilbertBasis` — Hilbert basis of a subsemigroup (defined below)

## References

* [Stu1] Sturmfels, B. *Gröbner Bases and Convex Polytopes*, Theorem 1.11
-/

open MvPolynomial

section HilbertBasisDefinition

variable {N : Type*} [Fintype N]

/-- A **Hilbert basis** of a subsemigroup `C` of `ℕⁿ` is a finite set `H ⊆ C`
such that every element of `C` can be written as an `ℕ`-linear combination
of elements of `H`.  By Gordan's Lemma, every finitely generated rational
cone admits a finite Hilbert basis. -/
structure IsHilbertBasis (C : Set (N →₀ ℕ)) (H : Finset (N →₀ ℕ)) : Prop where
  subset : (H : Set (N →₀ ℕ)) ⊆ C
  spanning : ∀ a ∈ C, ∃ (cs : N →₀ ℕ → ℕ),
    (∀ i, cs i ≠ 0 → i ∈ (H : Set (N →₀ ℕ))) ∧ a = ∑ i in H, cs i • i

end HilbertBasisDefinition

section GroebnerBasisAlgorithm

variable {Z V : Type*} [Fintype Z] [Fintype V]
  {K : Type*} [Field K]

/-- Embed a `V`-exponent vector into the `V`-block of the combined
variable set `(Z ⊕ V) ⊕ V` (where the second copy of `V` plays the role of `W`).
This sends each generator indexed by `v` to the generator in the `V`-block. -/
def embedV (α : V →₀ ℕ) : (Z ⊕ V) ⊕ V →₀ ℕ :=
  Finsupp.mapDomain (Sum.inl ∘ Sum.inr) α

/-- Embed a `V`-exponent vector into the `W`-block of the combined
variable set `(Z ⊕ V) ⊕ V`.  This sends each generator indexed by `v`
to the generator in the `W`-block (the second copy of `V`). -/
def embedW (α : V →₀ ℕ) : (Z ⊕ V) ⊕ V →₀ ℕ :=
  Finsupp.mapDomain Sum.inr α

/-- **Gröbner Basis Algorithm for Hilbert Bases** (Sturmfels).

Given an ideal `I` in the polynomial ring `K[Z, V, W]` (with `W` a second copy
of `V`), a monomial order `m` that is an elimination order (with the variable
blocks ordered `Z > V > W`), and a finite Gröbner basis `G` for `I` with
respect to `m`, the exponent vectors `α` of those binomials in `G` of the form
`v^α - w^α` constitute a Hilbert basis for the cone `C`. -/
theorem groebner_basis_algorithm_for_hilbert_bases
    (I : Ideal (MvPolynomial ((Z ⊕ V) ⊕ V) K))
    (m : MonomialOrder ((Z ⊕ V) ⊕ V))
    (G : Finset (MvPolynomial ((Z ⊕ V) ⊕ V) K))
    (hGroebner : initialSubmodule (m := m) (I := I) = Ideal.span
      {m.leadingTerm g | (g : MvPolynomial ((Z ⊕ V) ⊕ V) K) (_ : g ∈ G)})
    (hG_sub_I : (G : Set (MvPolynomial ((Z ⊕ V) ⊕ V) K)) ⊆ (I : Set _))
    (h_elim : ∀ (z : Z) (v₁ v₂ : V),
      (Finsupp.single (Sum.inl (Sum.inl z)) 1 : ((Z ⊕ V) ⊕ V) →₀ ℕ) ≻[m]
      (Finsupp.single (Sum.inl (Sum.inr v₁)) 1 : ((Z ⊕ V) ⊕ V) →₀ ℕ) ∧
      (Finsupp.single (Sum.inl (Sum.inr v₁)) 1 : ((Z ⊕ V) ⊕ V) →₀ ℕ) ≻[m]
      (Finsupp.single (Sum.inr v₂) 1 : ((Z ⊕ V) ⊕ V) →₀ ℕ))
    (C : Set (V →₀ ℕ))
    (H : Finset (V →₀ ℕ))
    (hH : H = {α : V →₀ ℕ |
      (monomial (embedV α) (1 : K) - monomial (embedW α) (1 : K)) ∈ (G : Set _)})
    : IsHilbertBasis C H := by
  sorry

end GroebnerBasisAlgorithm
