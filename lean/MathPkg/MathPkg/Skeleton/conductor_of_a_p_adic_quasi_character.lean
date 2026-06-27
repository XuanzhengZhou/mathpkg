import Mathlib

open scoped Valued WithZero

/-!
# Conductor of a p-adic Quasi-Character

For a p-adic field `K` with integer ring `𝒪[K]` and maximal ideal `𝓂[K]`, the subgroups

    U^(m) = 1 + 𝓂[K]^m   (m ≥ 1),   U^(0) = 𝒪[K]^×

form a fundamental system of neighborhoods of `1` in the unit group `U = 𝒪[K]^×`.

A **quasi-character** of `K^×` is a continuous group homomorphism `c : K^× → A` into an
abelian group `A` (typically `ℂ^×`). Since the subgroups `U^(m)` form a neighbourhood basis
at `1`, any such `c` vanishes on some `U^(m)`, i.e. `c(U^(m)) = {1}` for sufficiently large `m`.

The **conductor** `𝔣(c)` of `c` is the ideal

    𝔣 = 𝓂[K]^m    where `m` is the smallest integer ≥ 0 such that `c(U^(m)) = {1}`.

If `m = 0` (the character is unramified), then `𝔣 = 0`, the zero ideal.

The integer `m` is called the **conductor exponent** of `c`.

## References

* [Neukirch] *Algebraic Number Theory*, Chapter V, §2
* [Serre] *Local Fields*, Chapter V
* [Cassels-Fröhlich] *Algebraic Number Theory*, Chapter VI (Local Class Field Theory)
-/

section conductor_of_a_p_adic_quasi_character

variable (K : Type*) [Field K] (Γ₀ : Type*) [LinearOrderedCommGroupWithZero Γ₀] [Valued K Γ₀]
variable (A : Type*) [CommMonoid A]

/-! ### Higher unit groups -/

/-- The `m`-th higher unit group `U^(m) = ker(𝒪[K]^× → (𝒪[K] / 𝓂[K]^m)^×)`.

For `m = 0`, `𝓂[K]^0 = ⊤`, the quotient is the trivial ring, so `U^(0) = 𝒪[K]^×`.
For `m ≥ 1`, this is `{u ∈ 𝒪[K]^× | u ≡ 1 mod 𝓂[K]^m}` = `1 + 𝓂[K]^m`.

These subgroups form a fundamental system of neighbourhoods of `1` in `𝒪[K]^×`
for the `𝓂[K]`-adic topology. -/
def higherUnitGroup (m : ℕ) : Subgroup (𝒪[K])ˣ := by
  sorry
