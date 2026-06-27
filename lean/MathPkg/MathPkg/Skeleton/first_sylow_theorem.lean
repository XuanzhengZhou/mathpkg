import Mathlib

/- First Sylow Theorem: If p is a prime and p^k divides the order of a finite group G,
   then G has a subgroup of order p^k. -/
theorem first_sylow_theorem {G : Type*} [Group G] [Finite G] {p k : ℕ} [Fact p.Prime]
    (h : p ^ k ∣ Nat.card G) : ∃ (H : Subgroup G), Nat.card H = p ^ k := by
  sorry
