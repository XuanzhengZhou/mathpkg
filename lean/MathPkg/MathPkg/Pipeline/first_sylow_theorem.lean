import Mathlib

/- First Sylow Theorem: If p is a prime and p^k divides the order of a finite group G,
   then G has a subgroup of order p^k. -/
theorem first_sylow_theorem {G : Type*} [Group G] [Fintype G] {p k : ℕ} (hp : Nat.Prime p)
    (h : p ^ k ∣ Fintype.card G) : ∃ (H : Subgroup G), Fintype.card H = p ^ k := by
  sorry
