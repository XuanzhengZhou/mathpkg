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
  sorry
