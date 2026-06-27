import Mathlib

open scoped Classical

/-!
# Finite and Infinite Field Extensions

For a field extension `K/F`, if the degree `[K : F]` is finite, then `K` is a **finite extension**
of `F`; otherwise `K` is an **infinite extension** of `F`.

Mathlib4 already encodes this via the typeclass `FiniteDimensional F K` (or equivalently
`Module.Finite F K`), which asserts that `K` is finite-dimensional as an `F`-vector space.
The degree `[K : F]` is given by `Module.finrank F K`.

## Main definitions

* `FiniteExtension F K` -- alias for `FiniteDimensional F K`; `K/F` is a finite extension.
* `InfiniteExtension F K` -- alias for `¬ FiniteDimensional F K`; `K/F` is an infinite extension.
* `extensionDegree F K` -- alias for `Module.finrank F K`; the degree `[K : F]`.

In practice, use the Mathlib4 typeclasses directly: `[FiniteDimensional F K]` or
`[Module.Finite F K]`.
-/

section finite_and_infinite_extensions

variable (F K : Type*) [Field F] [Field K] [Algebra F K]

/-! ### Core abbreviations -/

/-- `FiniteExtension F K` means `K` is a finite-dimensional `F`-vector space,
i.e., the field extension `K/F` is **finite**. This is simply an alias for
Mathlib4's `FiniteDimensional F K`. -/
abbrev FiniteExtension (F K : Type*) [Field F] [Field K] [Algebra F K] : Prop :=
  FiniteDimensional F K

/-- `InfiniteExtension F K` means `K` is not a finite-dimensional `F`-vector space,
i.e., the field extension `K/F` is **infinite**. This is the logical negation of
`FiniteDimensional F K`. -/
abbrev InfiniteExtension (F K : Type*) [Field F] [Field K] [Algebra F K] : Prop :=
  ¬ FiniteDimensional F K

/-- `extensionDegree F K` is the degree `[K : F]` of the field extension, defined as
the `F`-dimension of `K` as an `F`-vector space: `Module.finrank F K`. -/
abbrev extensionDegree (F K : Type*) [Field F] [Field K] [Algebra F K] : ℕ :=
  Module.finrank F K

/-- The fundamental relationship: `K/F` is a finite extension if and only if the degree
`[K : F]` is finite (i.e., less than `ℵ₀`).
This is `FiniteDimensional.finrank_lt_aleph0` from Mathlib4. -/
example [FiniteDimensional F K] : Module.finrank F K < ℵ₀ :=
  FiniteDimensional.finrank_lt_aleph0 F K

end finite_and_infinite_extensions

/-! ### Examples -/

section examples

open scoped Cardinal

variable (F K : Type*) [Field F] [Field K] [Algebra F K]

/-- Example 1: ℚ ⊆ ℚ(√2) is a finite extension. The degree [ℚ(√2) : ℚ] = 2. -/
example : FiniteExtension ℚ (AdjoinRoot (X ^ 2 - 2 : Polynomial ℚ)) := by
  have : FiniteDimensional ℚ (AdjoinRoot (X ^ 2 - 2 : Polynomial ℚ)) :=
    Module.finite_of_finrank_pos (by
      have : (AdjoinRoot.powerBasis' (Polynomial.monic_X_pow_sub_C 2 (by norm_num))).finrank = 2 :=
        AdjoinRoot.powerBasis' (Polynomial.monic_X_pow_sub_C 2 (by norm_num)) |>.finrank
      -- finrank > 0
      positivity)
  exact this

/-- Example 2: The extension degree of ℚ(∛2) over ℚ is 3. -/
example : extensionDegree ℚ (AdjoinRoot (X ^ 3 - 2 : Polynomial ℚ)) = 3 := by
  dsimp [extensionDegree]
  have h : PowerBasis ℚ (AdjoinRoot (X ^ 3 - 2 : Polynomial ℚ)) :=
    AdjoinRoot.powerBasis' (monic_X_pow_sub_C 3 (by norm_num : (2 : ℚ) ≠ 0))
  rw [PowerBasis.finrank h, h.dim]
  rfl

/-- Example 3: ℂ is a finite extension of ℝ (degree 2). -/
example : FiniteExtension ℝ ℂ := by
  dsimp [FiniteExtension]
  infer_instance

/-- Example 4: [ℂ : ℝ] = 2. -/
example : extensionDegree ℝ ℂ = 2 := by
  dsimp [extensionDegree]
  rw [Complex.finrank_real_complex]

/-- Example 5: ℚ ⊆ ℚ(x) (the rational function field) is an infinite extension. -/
example : InfiniteExtension ℚ (RatFunc ℚ) := by
  dsimp [InfiniteExtension, FiniteExtension]
  -- The rational function field ℚ(x) is infinite-dimensional as a ℚ-vector space
  intro h
  have : FiniteDimensional ℚ (RatFunc ℚ) := h
  -- The set {x^n | n ∈ ℕ} is linearly independent and infinite, contradiction
  have : Finite ℚ (RatFunc ℚ) := Module.finite_of_finite ℚ
  have hcard : ℵ₀ ≤ Module.rank ℚ (RatFunc ℚ) := by
    -- There are infinitely many linearly independent elements 1, x, x^2, ...
    refine aleph0_le_rank.mpr ?_
    -- but we can give a simpler argument using the fact that a finite-dimensional
    -- vector space over a field cannot have an infinite linearly independent set
    have h_ind : LinearIndependent ℚ (fun (n : ℕ) ↦ (RatFunc.X : RatFunc ℚ) ^ n) := by
      refine linearIndependent_pow (RatFunc.X : RatFunc ℚ)
    have : Infinite ℕ := by infer_instance
    exact h_ind.aleph0_le_rank
  have : Module.rank ℚ (RatFunc ℚ) < ℵ₀ :=
    FiniteDimensional.rank_lt_aleph0 ℚ (RatFunc ℚ)
  exact not_lt.mpr hcard this

/-- Example 6: If K/F is a finite extension, then [K : F] is a natural number. -/
example [FiniteDimensional F K] : extensionDegree F K < ℵ₀ := by
  dsimp [extensionDegree]
  exact FiniteDimensional.finrank_lt_aleph0 F K

/-- Example 7: For any field F, F/F is a finite extension of degree 1. -/
example (F : Type*) [Field F] : FiniteExtension F F ∧ extensionDegree F F = 1 := by
  dsimp [FiniteExtension, extensionDegree]
  refine ⟨inferInstance, ?_⟩
  simp [finrank_self]

/-- Example 8: A tower of finite extensions: if K/F and L/K are finite, then L/F is finite.
This is the tower law for finite extensions (Mathlib4: `FiniteDimensional.trans`). -/
example (L : Type*) [Field L] [Algebra F L] [Algebra K L] [IsScalarTower F K L]
    [FiniteDimensional F K] [FiniteDimensional K L] : FiniteDimensional F L := by
  infer_instance

/-- Example 9: The tower degree formula: [L : F] = [L : K] · [K : F] (when both are finite).
This is `Module.finrank_mul_finrank` from Mathlib4. -/
example (L : Type*) [Field L] [Algebra F L] [Algebra K L] [IsScalarTower F K L]
    [FiniteDimensional F K] [FiniteDimensional K L] :
    finrank F L = finrank K L * finrank F K := by
  rw [finrank_mul_finrank F K L]

/-- Example 10: A finite extension has a finite basis.
In particular, a simple algebraic extension ℚ(α) where α has degree n has basis {1, α, …, α^{n-1}}. -/
example [FiniteDimensional F K] : ∃ (n : ℕ), Nonempty (Basis (Fin n) F K) := by
  have h := FiniteDimensional.exists_isBasis_finset F K
  rcases h with ⟨B, hB⟩
  refine ⟨B.card, ?_⟩
  have : Fintype B := FinsetCoe.fintype B
  exact ⟨Basis.mk hB.linearIndependent (by
    rw [Finset.coe_sort_coe, Basis.coe_mk, hB.span_eq])⟩

end examples
