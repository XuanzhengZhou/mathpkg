import Mathlib

open scoped Classical

/-!
# Bilinear Form Definition

Let `R` be a commutative ring and `M` an `R`-module. A **bilinear form** on `M` is a
function `⟨·,·⟩ : M × M → R` that is `R`-linear in both arguments:

1. `⟨r₁m₁ + r₂m₂, m⟩ = r₁⟨m₁,m⟩ + r₂⟨m₂,m⟩`  (linear in the first argument)
2. `⟨m, r₁m₁ + r₂m₂⟩ = r₁⟨m,m₁⟩ + r₂⟨m,m₂⟩`  (linear in the second argument)

for all `r₁, r₂ ∈ R` and `m₁, m₂, m ∈ M`.

## Mathlib4 Formalization

Mathlib4 defines `BilinForm R M` in `LinearAlgebra/BilinearMap.lean` as:

```lean
protected abbrev BilinMap : Type _ := M →ₗ[R] M →ₗ[R] Nₗ
protected abbrev BilinForm : Type _ := LinearMap.BilinMap R M R
```

That is, a bilinear form is a bilinear map `M →ₗ[R] M →ₗ[R] R`, i.e., a
curried representation of a function `M × M → R` that is `R`-linear in each slot.

The basic properties (additivity and scalar multiplication in each argument) are
proved in `LinearAlgebra/BilinearForm/Basic.lean`:

```lean
theorem add_left (x y z : M) : B (x + y) z = B x z + B y z
theorem smul_left (a : R) (x y : M) : B (a • x) y = a * B x y
theorem add_right (x y z : M) : B x (y + z) = B x y + B x z
theorem smul_right (a : R) (x y : M) : B x (a • y) = a * B x y
```

## Dependencies

- [Commutative ring](/concept/commutative_ring) — the scalar ring `R`
- [Module](/concept/module) — `M` is an `R`-module
- [Bilinear map](/concept/bilinear_map) — underlying notion of a bilinear map
-/

section bilinear_form_definition

variable (R : Type u) [CommRing R]
variable (M : Type v) [AddCommGroup M] [Module R M]

/--
A **bilinear form** on an `R`-module `M` is an `R`-bilinear map `B : M → M → R`.

In Mathlib4, `BilinForm R M` is defined as `M →ₗ[R] M →ₗ[R] R`, meaning a
linear map from `M` to the linear dual `M →ₗ[R] R`. This curried representation
is equivalent to the usual `M × M → R` presentation.

Formally:
```
BilinForm R M := M →ₗ[R] M →ₗ[R] R
```
-/
def BilinearForm' := BilinForm R M

/-- The standard dot product on `Rⁿ` as a bilinear form.

Given two vectors `v, w : (Fin n) → R`, the bilinear form returns
`∑ᵢ vᵢ * wᵢ`. This is the usual Euclidean inner product over the ring `R`. -/
example (n : ℕ) : BilinForm R ((Fin n) → R) := by
  -- Use Mathlib4's `Matrix.toBilin'` or construct directly via `LinearMap.mk₂`
  refine LinearMap.mk₂ R
    (fun v w => ∑ i : Fin n, v i * w i)
    (by
      intro v₁ v₂ w
      simp only [Pi.add_apply, add_mul, Finset.sum_add_distrib])
    (by
      intro c v w
      simp only [Pi.smul_apply, smul_eq_mul, mul_assoc, Finset.mul_sum])
    (by
      intro v w₁ w₂
      simp only [Pi.add_apply, mul_add, Finset.sum_add_distrib])
    (by
      intro c v w
      simp only [Pi.smul_apply, smul_eq_mul, mul_assoc, Finset.mul_sum, mul_comm, mul_left_comm])

/-- For a free `R`-module `M` of finite rank with basis `(e₁, …, eₙ)`, the
**standard bilinear form** is defined by `⟨eᵢ, eⱼ⟩ = δᵢⱼ` (Kronecker delta)
and extended bilinearly.

On a finite-dimensional vector space over a field, this yields the usual
notion of an inner product when `R = ℝ`. -/
example (n : ℕ) (v w : (Fin n) → ℝ) : BilinForm ℝ ((Fin n) → ℝ) :=
  -- The matrix `1` gives the standard dot product; use `Matrix.toBilin'` to
  -- obtain the corresponding bilinear form.
  Matrix.toBilin' (1 : Matrix (Fin n) (Fin n) ℝ)

end bilinear_form_definition
