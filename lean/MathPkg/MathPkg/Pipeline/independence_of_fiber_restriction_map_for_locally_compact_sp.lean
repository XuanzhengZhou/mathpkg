import Mathlib

open Set
open scoped Topology

/-!
# Independence of the Fiber Restriction Map

Let `X` be a locally compact Hausdorff space and `T` a compact connected
Hausdorff space. For a coefficient (sheaf) system `F` on `X`, consider the
pullback to `X × T`. The fiber inclusion map `i_t : X → X × T` given by
`x ↦ (x, t)` induces a pullback homomorphism

`i_t^* : H_c^n(X × T; F × T) → H_c^n(X; F)`

on compactly supported cohomology. The theorem states that this induced
map is **independent** of the choice of `t ∈ T`: for any `t₁, t₂ ∈ T`,
the maps `i_{t₁}^*` and `i_{t₂}^*` coincide.

## References

* Bredon, *Sheaf Theory*, Section II.14
* Iversen, *Cohomology of Sheaves*, Section III.8
-/

noncomputable section

variable {X T : Type*} [TopologicalSpace X] [TopologicalSpace T]
  [LocallyCompactSpace X] [T2Space X]
  [CompactSpace T] [ConnectedSpace T] [T2Space T]

/-- The inclusion map `i_t : X → X × T` sending `x ↦ (x, t)`. -/
def fiberInclusion (t : T) : C(X, X × T) where
  toFun x := (x, t)
  continuous_toFun := Continuous.prod_mk continuous_id continuous_const

section CohomologyAxioms

/-! ### Abstract compactly supported cohomology

We work with an abstract cohomology theory `Hc` that assigns to each
topological space `Y` and coefficient abelian group `A` a graded family
of abelian groups `Hc^n(Y; A)`, along with pullback homomorphisms
`f^* : Hc^n(Z; A) → Hc^n(Y; A)` for each continuous map `f : Y → Z`.

In a full formalisation this would be instantiated with the derived
functor `RΓ_c` of the compactly supported sections functor.
-/

/-- The compactly supported cohomology groups, depending on the space,
coefficient group, and degree. -/
variable (Hc : (Y : Type*) → [TopologicalSpace Y] → (A : Type*) → [AddCommGroup A] → ℕ → Type*)

/-- Each `Hc^n(Y; A)` is an abelian group. -/
variable [∀ (Y : Type*) [TopologicalSpace Y] (A : Type*) [AddCommGroup A] (n : ℕ),
  AddCommGroup (Hc Y A n)]

/-- Pullback homomorphism `f^* : Hc^n(Z; A) → Hc^n(Y; A)` for `f : C(Y, Z)`. -/
variable (pullback : ∀ {Y Z : Type*} [TopologicalSpace Y] [TopologicalSpace Z]
  (f : C(Y, Z)) (A : Type*) [AddCommGroup A] (n : ℕ), Hc Z A n →+ Hc Y A n)

end CohomologyAxioms

/-- **Independence of the fiber restriction map.**
For any coefficient group `A` and degree `n`, the pullback along `i_t`
does not depend on `t ∈ T`. -/
theorem independence_of_fiber_restriction_map_for_locally_compact_sp
    (A : Type*) [AddCommGroup A] (t₁ t₂ : T) (n : ℕ) :
    pullback Hc (fiberInclusion t₁) A n = pullback Hc (fiberInclusion t₂) A n := by
  sorry
