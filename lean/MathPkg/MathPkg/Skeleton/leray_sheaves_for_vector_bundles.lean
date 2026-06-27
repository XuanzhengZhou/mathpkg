import Mathlib

open TopologicalSpace

/-!
# Leray Sheaves for Vector Bundles

Let ξ be an n-plane bundle over a space Y with total space U.
Identify Y with the zero section, set U₀ = U - Y, and let π: U → Y, π₀ = π|U₀.
Then the Leray sheaf J^q(π; L) is the constant sheaf with stalks L for q = 0
and 0 otherwise; J^q(π, π₀; L) is the locally constant sheaf with stalks
H^q(ℝ^n, ℝ^n - {0}; L).

The Leray sheaf J^q(f; A) for a continuous map f: X → Y and a sheaf A on X
is the sheafification of the presheaf V ↦ H^q(f⁻¹(V); A|_{f⁻¹(V)}), i.e.,
the q-th higher direct image sheaf R^q f_* A.

When f is a locally trivial fibration with contractible fiber (as for a vector
bundle), the higher direct images simplify drastically by homotopy invariance.
-/

noncomputable section

variable {Y U : Type u} [TopologicalSpace Y] [TopologicalSpace U]

/-- The **Leray sheaf** (or **q-th higher direct image sheaf**) `R^q f_* A` on `Y`
associated to a continuous map `f : U → Y` and an abelian sheaf `A` on `U`.

This is the sheafification of the presheaf `V ↦ H^q(f⁻¹(V); A|_{f⁻¹(V)})`,
where `H^q` denotes sheaf cohomology on the subspace `f⁻¹(V)`.

In the language of derived functors, `LeraySheaf q f A` is the `q`-th right
derived functor of the pushforward `f_* : Sheaf U → Sheaf Y` evaluated at `A`.

For the site-theoretic definition, we work on the spatial site `Opens Y` and
the site `Opens U` with the natural map induced by `f`. The pushforward functor
`TopCat.Sheaf.pushforward` gives the direct image, and its right derived
functors give the higher direct images. -/
def LeraySheaf (q : ℕ) (f : U → Y) (hf : Continuous f) (A : TopCat.Sheaf AddCommGrpCat.{u} (TopCat.of U)) :
    TopCat.Sheaf AddCommGrpCat.{u} (TopCat.of Y) := by
  sorry
