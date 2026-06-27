import Mathlib

/-!
# Definition of inner derivation (1-coboundary)

Let `G` be a group and `A` a G-module (equivalently, a representation of `G` over a commutative
ring `k`). For `a ∈ A`, the **inner derivation** (or **1-coboundary**) associated to `a` is the map

    δ(a) : G → A,   (δ(a))(g) = g · a - a.

Such a function `f : G → A` is called a 1-coboundary if there exists `a ∈ A` such that
`f(g) = g · a - a` for all `g ∈ G`. The set of all inner derivations is denoted
B¹(G, A) (or Inn(G, A)).

## Mathlib4 correspondence

Mathlib4 defines these concepts in
`RepresentationTheory.Homological.GroupCohomology.LowDegree` for a `k`-linear
representation `A : Rep k G`:

* `d₀₁ A` — the `k`-linear map `A → (G → A)` sending `a ↦ (g ↦ ρ_A(g)(a) - a)`.
  This is the coboundary map that sends an element of `A` to its associated inner derivation.
* `coboundaries₁ A` — the submodule `B¹(G, A)` of 1-coboundaries, defined as the image of `d₀₁`.
* `IsCoboundary₁ f` — the proposition that `f : G → A` is a 1-coboundary:
  `∃ x : A, ∀ g : G, g • x - x = f g`.
-/

variable {k G : Type*} [CommRing k] [Group G] (A : Rep k G)

/--
For `a ∈ A`, the **inner derivation** `δ(a) : G → A` is the map `g ↦ g·a - a`.
This is a 1-coboundary, i.e., `IsCoboundary₁ (δ(a))`.
-/
noncomputable def innerDerivation (a : A) : G → A := by
  sorry
