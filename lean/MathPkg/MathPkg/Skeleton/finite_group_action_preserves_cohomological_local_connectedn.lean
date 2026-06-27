import Mathlib

/- 有限群作用保持上同调局部连通性 -/

/-- A topological space `X` is n-clc_L (cohomologically locally connected of degree `n`
over a field `L`) if for every point `x : X` and every neighborhood `U` of `x`,
there exists a smaller neighborhood `V ⊆ U` such that the restriction map in
degree `n` Čech cohomology `Hⁿ(U; L) → Hⁿ(V; L)` is zero. -/
def IsNClc (L : Type*) [Field L] (n : ℕ) (X : Type*) [TopologicalSpace X] : Prop := by
  sorry
