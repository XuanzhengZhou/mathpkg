import Mathlib

/-!
# Linear independence of distinct values

Any set of elements of `R` with distinct `ρ` values is linearly independent over `F`.
This is a fundamental property of order domains (Cox–Little–O'Shea, Chapter 10).
-/

universe u v w

variable {F : Type u} [Field F]
variable {R : Type v} [CommRing R] [Algebra F R]
variable {Γ : Type w} [LinearOrderedAddCommMonoid Γ]

/-- If `ρ` is an order function on an `F`-algebra `R`, then any finite family of elements
of `R` whose `ρ`-values are pairwise distinct is linearly independent over `F`. -/
lemma linear_independence_of_distinct_values
    (ρ : R → WithBot Γ)
    {n : ℕ} (f : Fin n → R)
    (h_distinct : ∀ i j : Fin n, i ≠ j → ρ (f i) ≠ ρ (f j)) :
    LinearIndependent F f := by
  sorry
