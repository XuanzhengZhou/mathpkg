import Mathlib

/- 有限群作用保持上同调局部连通性 -/

/-- A topological space `X` is n-clc_L (cohomologically locally connected of degree `n`
over a field `L`) if for every point `x : X` and every neighborhood `U` of `x`,
there exists a smaller neighborhood `V ⊆ U` such that the restriction map in
degree `n` Čech cohomology `Hⁿ(U; L) → Hⁿ(V; L)` is zero. -/
def IsNClc (L : Type*) [Field L] (n : ℕ) (X : Type*) [TopologicalSpace X] : Prop :=
  sorry

/-- If `X` is a Hausdorff space and n-clc_L with `char(L)` relatively prime to `|G|`,
then the orbit space `X/G` is also n-clc_L. -/
theorem finite_group_action_preserves_cohomological_local_connectedness
    {X G L : Type*} [TopologicalSpace X] [T2Space X]
    [TopologicalSpace G] [Group G] [Fintype G]
    [MulAction G X] [ContinuousSMul G X]
    [Field L] (n : ℕ)
    (hNclc : IsNClc L n X)
    (hCoprime : ¬ ringChar L ∣ Fintype.card G) :
    IsNClc L n (Quotient (MulAction.orbitRel G X)) := by
  sorry
