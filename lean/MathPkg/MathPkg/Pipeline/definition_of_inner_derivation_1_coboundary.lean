import Mathlib
import Mathlib.RepresentationTheory.Homological.GroupCohomology.LowDegree

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

open RepresentationTheory.Homological.GroupCohomology

variable {k G : Type*} [CommRing k] [Group G] (A : Rep k G)

/--
For `a ∈ A`, the **inner derivation** `δ(a) : G → A` is the map `g ↦ g·a - a`.
This is a 1-coboundary, i.e., `IsCoboundary₁ (δ(a))`.
-/
noncomputable def innerDerivation (a : A) : G → A :=
  (d₀₁ A).hom a

/-- The inner derivation `δ(a)` is indeed a 1-coboundary. -/
example (a : A) : IsCoboundary₁ (innerDerivation A a) := by
  refine ⟨a, fun g => ?_⟩
  dsimp [innerDerivation]
  simp [d₀₁_hom_apply]

/-- The map `a ↦ δ(a)` is precisely the coboundary map `d₀₁`. -/
example (a : A) : innerDerivation A a = (d₀₁ A).hom a := rfl

/-- The set of 1-coboundaries `B¹(G, A)` is the submodule of all inner derivations. -/
example (f : G → A) : f ∈ coboundaries₁ A ↔ IsCoboundary₁ f := by
  constructor
  · intro hf
    obtain ⟨a, ha⟩ := Submodule.mem_range.mp hf
    refine ⟨a, fun g => ?_⟩
    have := congrArg (fun φ => φ g) ha
    simpa [d₀₁_hom_apply] using this
  · intro hf
    obtain ⟨a, ha⟩ := hf
    refine Submodule.mem_range.mpr ⟨a, ?_⟩
    ext g
    simp [d₀₁_hom_apply, ha g]
