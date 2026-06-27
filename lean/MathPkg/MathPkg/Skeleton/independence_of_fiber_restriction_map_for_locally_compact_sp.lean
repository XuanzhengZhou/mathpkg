import Mathlib

/-!
# Independence of the Fiber Restriction Map

Let `X` be a locally compact Hausdorff space and `T` a compact connected
Hausdorff space. For an abstract compactly supported cohomology theory `Hc`
with pullback homomorphism, the fiber restriction map is independent of the
choice of `t ∈ T`.

## References

* Bredon, *Sheaf Theory*, Section II.14
* Iversen, *Cohomology of Sheaves*, Section III.8
-/

universe u v w

theorem independence_of_fiber_restriction_map_for_locally_compact_sp
    {X T : Type u} [TopologicalSpace X] [TopologicalSpace T]
    [LocallyCompactSpace X] [T2Space X]
    [CompactSpace T] [ConnectedSpace T] [T2Space T]
    (Hc : (Y : Type u) → [TopologicalSpace Y] → (A : Type v) → [AddCommGroup A] → ℕ → Type w)
    (pullback : ∀ {Y Z : Type u} [TopologicalSpace Y] [TopologicalSpace Z]
      (f : C(Y, Z)) (A : Type v) [AddCommGroup A] (n : ℕ), Hc Z A n → Hc Y A n)
    (fiberInclusion : T → C(X, X × T))
    (A : Type v) [AddCommGroup A] (t₁ t₂ : T) (n : ℕ) :
    pullback (fiberInclusion t₁) A n = pullback (fiberInclusion t₂) A n := by
  sorry
