import Mathlib

/- Hall's residual finiteness for finitely generated abelian-by-nilpotent groups -/

theorem halls_residual_finiteness_for_finitely_generated_abelian_by_
    {G : Type*} [Group G] [Group.FG G]
    (A : Subgroup G) [A.Normal] [CommGroup (↥A)]
    [Group.IsNilpotent (G ⧸ A)] :
    Group.ResiduallyFinite G := by
  sorry
