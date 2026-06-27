import Mathlib

open Set
open scoped Manifold

/- Cover characterization of manifold with boundary -/

lemma cover_characterization_of_manifold_with_boundary {n : ℕ} [NeZero n] {M : Type*} [TopologicalSpace M]
    [T2Space M] [SecondCountableTopology M] :
    (Nonempty (ChartedSpace (EuclideanHalfSpace n) M)) ↔
    (∃ (ι : Type) (U : ι → Set M),
      (∀ i, IsOpen (U i)) ∧ (⋃ i, U i) = Set.univ ∧
      ∀ i, (Nonempty ((Subtype (· ∈ U i)) ≃ₜ EuclideanSpace ℝ (Fin n))) ∨
           (Nonempty ((Subtype (· ∈ U i)) ≃ₜ EuclideanHalfSpace n))) := by
  sorry
