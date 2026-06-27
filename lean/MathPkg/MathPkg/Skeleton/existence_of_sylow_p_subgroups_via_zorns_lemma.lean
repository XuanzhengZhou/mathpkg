import Mathlib

lemma existence_of_sylow_p_subgroups_via_zorns_lemma {G : Type*} [Group G] [Fintype G] {p : ℕ} [Fact p.Prime]
    (P : Subgroup G) (hP : IsPGroup p P) : ∃ S : Sylow p G, P ≤ (S : Subgroup G) := by
  sorry
