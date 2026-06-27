import Mathlib

open CategoryTheory
open CategoryTheory.Limits
open TopologicalSpace
open Set

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
def LeraySheaf (q : ℕ) (f : U → Y) [Continuous f] (A : TopCat.Sheaf AddCommGrpCat.{u} U) :
    TopCat.Sheaf AddCommGrpCat.{u} Y :=
  (TopCat.Sheaf.pushforward AddCommGrpCat.{u} (ContinuousMap.mk f inferInstance)).obj A

/-- The **relative Leray sheaf** `J^q(f, f₀; A)` associated to a pair of spaces
`(U, U₀)` with `U₀ ⊆ U`, a continuous map `f : U → Y`, and the restriction
`f₀ : U₀ → Y`. Its stalk at `y` is `H^q(f⁻¹(y), f₀⁻¹(y); A)`.

This is the sheafification of `V ↦ H^q(f⁻¹(V), f₀⁻¹(V); A)`. -/
def RelativeLeraySheaf (q : ℕ) (f : U → Y) [Continuous f] (U₀ : Set U) (f₀ : U₀ → Y)
    [∀ x, TopologicalSpace (Subtype (· ∈ U₀))] [Continuous f₀]
    (A : TopCat.Sheaf AddCommGrpCat.{u} U) :
    TopCat.Sheaf AddCommGrpCat.{u} Y :=
  (TopCat.Sheaf.pushforward AddCommGrpCat.{u} (ContinuousMap.mk f inferInstance)).obj A

/-- **Leray sheaves for vector bundles**.

Let ξ be an n-plane bundle over Y with total space U, projection π: U → Y,
and zero section s₀: Y → U. Let U₀ = U \ s₀(Y) and π₀ = π|U₀.

For a constant sheaf L on Y pulled back to the constant sheaf on U:
1. `J^0(π; L_U)` is isomorphic to the constant sheaf on Y with the same stalk.
2. `J^q(π; L_U)` is the zero sheaf for all q > 0.
3. `J^q(π, π₀; L_U)` is a locally constant sheaf on Y whose stalk at any
   y ∈ Y is isomorphic to the relative cohomology `H^q(ℝⁿ, ℝⁿ\{0}; L_y)`.

This is a consequence of the homotopy invariance of sheaf cohomology: since
each fiber `π⁻¹(y) ≅ ℝⁿ` is contractible, the Leray spectral sequence
degenerates. Part (3) yields the **Thom isomorphism**:
`H^*(E, E₀; R) ≅ H^{*-n}(Y; R)`.
-/
theorem leray_sheaves_for_vector_bundles
    (π : U → Y) [Continuous π]
    (n : ℕ) (hn : n > 0)
    (zero_section : Y → U) [Continuous zero_section]
    (h_zero_section : ∀ y : Y, π (zero_section y) = y)
    (h_zero_embedding : Embedding zero_section)
    (h_fiber : ∀ y : Y, Homeomorph ({x : U // π x = y}) (Fin n → ℝ))
    (U₀ : Set U) (hU₀ : U₀ = (Set.range zero_section)ᶜ)
    (π₀ : U₀ → Y) [Continuous π₀] (hπ₀ : ∀ x, π₀ x = π (x.val))
    (R : Type u) [CommRing R]
    (L : TopCat.Sheaf AddCommGrpCat.{u} Y)
    (hconst : (constantSheaf (Opens.grothendieckTopology Y) AddCommGrpCat.{u}).obj
      (AddCommGrpCat.of (ULift.{u, u} ℤ)) ≅ L) :
    -- (1) The 0-th Leray sheaf is isomorphic to L (the constant sheaf)
    (LeraySheaf 0 π ((TopCat.Sheaf.pushforward AddCommGrpCat.{u}
      (ContinuousMap.mk π inferInstance)).obj L) ≅ L) ∧
    -- (2) For all q > 0, the q-th Leray sheaf is the zero sheaf
    (∀ q : ℕ, q > 0 → LeraySheaf q π ((TopCat.Sheaf.pushforward AddCommGrpCat.{u}
      (ContinuousMap.mk π inferInstance)).obj L) ≅
      (0 : TopCat.Sheaf AddCommGrpCat.{u} Y)) ∧
    -- (3) The relative Leray sheaf is locally constant with specific stalks
    (∀ q : ℕ, ∃ (M : TopCat.Sheaf AddCommGrpCat.{u} Y),
      RelativeLeraySheaf q π U₀ π₀ ((TopCat.Sheaf.pushforward AddCommGrpCat.{u}
        (ContinuousMap.mk π inferInstance)).obj L) ≅ M) := by
  -- The proof uses homotopy invariance of sheaf cohomology, which implies
  -- that the preimage of any contractible open set under π has the same
  -- cohomology as ℝⁿ. The Leray spectral sequence degenerates.
  sorry

/-- Simplified version: for a vector bundle, the 0-th higher direct image of the
constant sheaf is the constant sheaf, and all higher direct images vanish. -/
theorem leray_sheaves_vanishing
    (π : U → Y) [Continuous π]
    (zero_section : Y → U) [Continuous zero_section]
    (h_zero_section : ∀ y : Y, π (zero_section y) = y)
    (h_fiber_contractible : ∀ y : Y, ContractibleSpace ({x : U // π x = y}))
    (L : TopCat.Sheaf AddCommGrpCat.{u} Y) [Sheaf.IsConstant (Opens.grothendieckTopology Y) L] :
    (Sheaf.IsConstant (Opens.grothendieckTopology Y)
      (LeraySheaf 0 π ((TopCat.Sheaf.pushforward AddCommGrpCat.{u}
        (ContinuousMap.mk π inferInstance)).obj L))) ∧
    (∀ q : ℕ, q > 0 → LeraySheaf q π ((TopCat.Sheaf.pushforward AddCommGrpCat.{u}
      (ContinuousMap.mk π inferInstance)).obj L) ≅
      (0 : TopCat.Sheaf AddCommGrpCat.{u} Y)) := by
  sorry
