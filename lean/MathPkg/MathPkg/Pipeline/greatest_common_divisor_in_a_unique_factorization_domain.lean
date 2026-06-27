import Mathlib

open scoped Classical

/-!
# Greatest Common Divisor in a Unique Factorization Domain

Let `a₁, …, aₙ` be nonzero elements of a unique factorization domain.
Write each `aᵢ = uᵢ · p₁^{m_{1i}} · p₂^{m_{2i}} · … · p_t^{m_{ti}}`
with a unit `uᵢ` and distinct prime elements `pⱼ`.
Then `c = p₁^{k₁} · p₂^{k₂} · … · p_t^{k_t}`, where `kⱼ = minᵢ m_{ⱼi}`,
is a greatest common divisor of `a₁, …, aₙ`.

Mathlib4 provides a `GCDMonoid` structure on any `UniqueFactorizationMonoid` via
`UniqueFactorizationMonoid.toGCDMonoid`. This file formalizes the connection between
the prime factorization view (via `normalizedFactors`) and the `gcd` operation.
-/

section greatest_common_divisor_in_a_unique_factorization_domain

open UniqueFactorizationMonoid

variable {α : Type*} [CommMonoidWithZero α] [UniqueFactorizationMonoid α] [NormalizationMonoid α]

-- Create a local GCDMonoid instance for the UFD so that `gcd`, `gcd_dvd_left`, etc. are available.
attribute [local instance] UniqueFactorizationMonoid.toGCDMonoid

/-! ### The GCD on a UFD via Mathlib4

Mathlib4 provides `UniqueFactorizationMonoid.toGCDMonoid α` which endows any UFD with
a `GCDMonoid` structure. The `gcd` and `lcm` are defined through the lattice structure
on `Associates α`. -/

/-- In a UFD, `gcd a b` divides `a`. This is `gcd_dvd_left`. -/
example (a b : α) : gcd a b ∣ a := gcd_dvd_left a b

/-- In a UFD, `gcd a b` divides `b`. This is `gcd_dvd_right`. -/
example (a b : α) : gcd a b ∣ b := gcd_dvd_right a b

/-- Any common divisor of `a` and `b` divides `gcd a b`. This is `dvd_gcd`. -/
example {a b c : α} (hac : c ∣ a) (hcb : c ∣ b) : c ∣ gcd a b := dvd_gcd hac hcb

/-! ### Connection to `normalizedFactors`

The fundamental bridge between divisibility and the multiset of normalized factors is
`dvd_iff_normalizedFactors_le_normalizedFactors`, which states that for nonzero `x, y`,
`x ∣ y ↔ normalizedFactors x ≤ normalizedFactors y`. Using `.mp`, we translate
divisibility into multiset inequalities. -/

/-- The `normalizedFactors` of `gcd a b` are bounded above by those of `a`. -/
theorem normalizedFactors_gcd_le_normalizedFactors_left (a b : α) (ha : a ≠ 0) (_hb : b ≠ 0) :
    normalizedFactors (gcd a b) ≤ normalizedFactors a := by
  have hgcd_ne_zero : gcd a b ≠ 0 := by
    intro hzero
    have hgcd_dvd := gcd_dvd_left a b
    rw [hzero] at hgcd_dvd
    exact ha (eq_zero_of_zero_dvd hgcd_dvd)
  exact ((dvd_iff_normalizedFactors_le_normalizedFactors hgcd_ne_zero ha).mp (gcd_dvd_left a b))

/-- The `normalizedFactors` of `gcd a b` are bounded above by those of `b`. -/
theorem normalizedFactors_gcd_le_normalizedFactors_right (a b : α) (_ha : a ≠ 0) (hb : b ≠ 0) :
    normalizedFactors (gcd a b) ≤ normalizedFactors b := by
  have hgcd_ne_zero : gcd a b ≠ 0 := by
    intro hzero
    have hgcd_dvd := gcd_dvd_right a b
    rw [hzero] at hgcd_dvd
    exact hb (eq_zero_of_zero_dvd hgcd_dvd)
  exact ((dvd_iff_normalizedFactors_le_normalizedFactors hgcd_ne_zero hb).mp (gcd_dvd_right a b))

/-- Any common divisor `c` of `a` and `b` has `normalizedFactors` bounded by those of
`gcd a b` (the "greatest" property in the multiset order). -/
theorem normalizedFactors_le_gcd_of_dvd_both (a b c : α) (ha : a ≠ 0) (_hb : b ≠ 0) (hc : c ≠ 0)
    (hca : c ∣ a) (hcb : c ∣ b) : normalizedFactors c ≤ normalizedFactors (gcd a b) := by
  have hgcd_ne_zero : gcd a b ≠ 0 := by
    intro hzero
    have hgcd_dvd := gcd_dvd_left a b
    rw [hzero] at hgcd_dvd
    exact ha (eq_zero_of_zero_dvd hgcd_dvd)
  have hc_dvd_gcd : c ∣ gcd a b := dvd_gcd hca hcb
  exact ((dvd_iff_normalizedFactors_le_normalizedFactors hc hgcd_ne_zero).mp hc_dvd_gcd)

/-- **Main characterization**: `normalizedFactors (gcd a b)` is simultaneously
bounded above by both `normalizedFactors a` and `normalizedFactors b`, and for any
common divisor `c`, its normalized factors are bounded above by those of the gcd.

In the multiset order `m ≤ n` means `count p m ≤ count p n` for all `p`.
So for each prime pⱼ, the count of pⱼ in `normalizedFactors (gcd a b)` is exactly
`min (count in a, count in b)` — the exponent kⱼ = minᵢ m_{ⱼi}. -/
theorem normalizedFactors_gcd_is_greatest_lower_bound (a b : α) (ha : a ≠ 0) (hb : b ≠ 0) :
    normalizedFactors (gcd a b) ≤ normalizedFactors a ∧
    normalizedFactors (gcd a b) ≤ normalizedFactors b ∧
    (∀ c : α, c ≠ 0 → c ∣ a → c ∣ b →
      normalizedFactors c ≤ normalizedFactors (gcd a b)) :=
  ⟨normalizedFactors_gcd_le_normalizedFactors_left a b ha hb,
   normalizedFactors_gcd_le_normalizedFactors_right a b ha hb,
   fun c hc hca hcb =>
    normalizedFactors_le_gcd_of_dvd_both a b c ha hb hc hca hcb⟩

/-- **Prime exponent formulation**: for each prime `p` and nonzero `a, b`,
the count of `p` in `normalizedFactors (gcd a b)` is bounded above by the minimum
of the counts in `a` and `b`. This mirrors the definition: for each prime pⱼ,
the exponent kⱼ = minᵢ m_{ⱼi} is at most each individual exponent. -/
theorem count_normalizedFactors_gcd_le_min_count (a b p : α) (ha : a ≠ 0) (hb : b ≠ 0) :
    (normalizedFactors (gcd a b)).count p ≤
    min ((normalizedFactors a).count p) ((normalizedFactors b).count p) := by
  have hle_a : (normalizedFactors (gcd a b)).count p ≤ (normalizedFactors a).count p := by
    have h := normalizedFactors_gcd_le_normalizedFactors_left a b ha hb
    rw [Multiset.le_iff_count] at h
    exact h p
  have hle_b : (normalizedFactors (gcd a b)).count p ≤ (normalizedFactors b).count p := by
    have h := normalizedFactors_gcd_le_normalizedFactors_right a b ha hb
    rw [Multiset.le_iff_count] at h
    exact h p
  exact le_min hle_a hle_b

/-! ### Explicit examples in ℕ

`ℕ` is a UFD (in fact, a Euclidean domain with computable gcd). We use the computable
`Nat.gcd` for concrete calculations. -/

/-- Example: `gcd(12, 18) = 6` in ℕ. Factorizations: `12 = 2²·3`, `18 = 2·3²`,
min exponents give `2¹·3¹ = 6`. -/
example : Nat.gcd 12 18 = 6 := by
  native_decide

/-- Example: `gcd(30, 42) = 6` in ℕ. Factorizations: `30 = 2·3·5`, `42 = 2·3·7`,
min exponents give `2·3 = 6`. -/
example : Nat.gcd 30 42 = 6 := by
  native_decide

/-- Using `Nat.factorization` (the computable prime factorization in ℕ), we can see
the "minimum exponent" rule: `Nat.factorization 12` gives `2 ↦ 2, 3 ↦ 1`,
`Nat.factorization 18` gives `2 ↦ 1, 3 ↦ 2`, so `Nat.factorization 6` gives `2 ↦ 1, 3 ↦ 1`. -/
example : (Nat.factorization 12) 2 = 2 := by
  native_decide

/-- The exponent of prime 2 in `Nat.factorization 18` is 1. -/
example : (Nat.factorization 18) 2 = 1 := by
  native_decide

/-- The exponent of prime 2 in `Nat.factorization 6` is 1, matching `min(2, 1) = 1`. -/
example : (Nat.factorization 6) 2 = 1 := by
  native_decide

end greatest_common_divisor_in_a_unique_factorization_domain
