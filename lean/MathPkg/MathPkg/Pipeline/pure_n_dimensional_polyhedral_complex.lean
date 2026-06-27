import Mathlib

/-!
# Pure n-dimensional Polyhedral Complex

A polyhedral complex `Δ` in `ℝⁿ` is said to be **pure n‑dimensional** if every maximal
element of `Δ` (with respect to inclusion) is an `n`‑dimensional polyhedron.

Geometrically, in a pure `n`‑dimensional polyhedral complex all maximal (co‑dimension‑0)
faces have dimension `n`, i.e. nonempty interior in `ℝⁿ`.  Lower‑dimensional faces only
appear as proper subsets of these maximal faces.

## Main definitions

* `IsPolyhedralComplex n Δ` — `Δ` is a finite collection of convex polytopes in `ℝⁿ`
  closed under binary intersections (a simplified “polyhedral complex” axiom).
* `IsMaximalIn P Δ` — `P` is a ⊆‑maximal element of the collection `Δ`.
* `IsPureNDimensional n Δ` — `Δ` is a pure `n`‑dimensional polyhedral complex:
  it is a polyhedral complex and every maximal element has nonempty interior.

## References

* [Cox–Little–O'Shea, *Ideals, Varieties, and Algorithms*][cox2015]
-/

open Set

variable {n : ℕ}

/--
A **polyhedral complex** `Δ` in `ℝⁿ` is a finite collection of convex subsets such that
the intersection of any two members also belongs to the collection.

In a full polyhedral complex one also requires closure under taking faces; here
we keep a simplified model that captures the essential structure needed to define
purity.
-/
def IsPolyhedralComplex (n : ℕ) (Δ : Set (Set (Fin n → ℝ))) : Prop :=
  (∀ P ∈ Δ, Convex ℝ P) ∧
  (∀ P ∈ Δ, ∀ Q ∈ Δ, P ∩ Q ∈ Δ) ∧
  Δ.Finite

/--
`P` is a **maximal element** of the collection `Δ` (with respect to the subset order `⊆`):
`P ∈ Δ` and no element `Q ∈ Δ` strictly contains `P`.
-/
def IsMaximalIn (P : Set (Fin n → ℝ)) (Δ : Set (Set (Fin n → ℝ))) : Prop :=
  P ∈ Δ ∧ ∀ Q ∈ Δ, P ⊆ Q → P = Q

/--
A polyhedral complex `Δ` in `ℝⁿ` is **pure n‑dimensional** if every maximal element
of `Δ` has nonempty interior in `ℝⁿ`.  Having nonempty interior characterises an
`n`‑dimensional polyhedron inside `ℝⁿ`.
-/
def IsPureNDimensional (n : ℕ) (Δ : Set (Set (Fin n → ℝ))) : Prop :=
  IsPolyhedralComplex n Δ ∧ ∀ P ∈ Δ, IsMaximalIn P Δ → (interior P).Nonempty

/-! ## Examples -/

/--
Example of `IsPolyhedralComplex`: the complex consisting of a single closed
unit interval `[0,1]` in `ℝ¹` is a polyhedral complex.
-/
example : IsPolyhedralComplex 1 {{x : Fin 1 → ℝ | 0 ≤ x 0 ∧ x 0 ≤ 1}} := by
  unfold IsPolyhedralComplex
  refine ⟨?_, ?_, ?_⟩
  · -- convexity
    intro P hP
    rw [Set.mem_singleton_iff.mp hP]
    intro a ha b hb t ht0 ht1
    rcases ha with ⟨ha0, ha1⟩
    rcases hb with ⟨hb0, hb1⟩
    refine ⟨?_, ?_⟩
    · nlinarith
    · nlinarith
  · -- intersection closedness
    intro P hP Q hQ
    rw [Set.mem_singleton_iff.mp hP, Set.mem_singleton_iff.mp hQ]
    have : {x | 0 ≤ x 0 ∧ x 0 ≤ 1} ∩ {x | 0 ≤ x 0 ∧ x 0 ≤ 1} = {x | 0 ≤ x 0 ∧ x 0 ≤ 1} := by
      ext x; simp
    simp [this]
  · -- finite
    apply Set.finite_singleton

/--
Example of `IsMaximalIn`: the unit interval `[0,1]` is maximal in the singleton complex
`{[0,1]}` since it is the only element.
-/
example : IsMaximalIn {x : Fin 1 → ℝ | 0 ≤ x 0 ∧ x 0 ≤ 1}
    {{x : Fin 1 → ℝ | 0 ≤ x 0 ∧ x 0 ≤ 1}} := by
  unfold IsMaximalIn
  refine ⟨by simp, ?_⟩
  intro Q hQ hPQ
  rw [Set.mem_singleton_iff.mp hQ]
  -- now P ⊆ P, so P = P — trivial
  rfl

/--
Example of `IsPureNDimensional`: an open interval `(0,1)` as a singleton complex
in `ℝ¹` has nonempty interior (it is its own interior).
-/
example : IsPureNDimensional 1 {{x : Fin 1 → ℝ | (0 : ℝ) < x 0 ∧ x 0 < (1 : ℝ)}} := by
  unfold IsPureNDimensional
  refine ⟨?_, ?_⟩
  · -- IsPolyhedralComplex
    unfold IsPolyhedralComplex
    refine ⟨?_, ?_, ?_⟩
    · intro P hP
      rw [Set.mem_singleton_iff.mp hP]
      -- convexity of the open interval: if a, b ∈ (0,1) then ta+(1-t)b ∈ (0,1)
      intro a ha b hb t ht0 ht1
      rcases ha with ⟨ha0, ha1⟩
      rcases hb with ⟨hb0, hb1⟩
      refine ⟨?_, ?_⟩
      · nlinarith
      · nlinarith
    · intro P hP Q hQ
      rw [Set.mem_singleton_iff.mp hP, Set.mem_singleton_iff.mp hQ]
      have hself : {x | (0 : ℝ) < x 0 ∧ x 0 < (1 : ℝ)} ∩ {x | (0 : ℝ) < x 0 ∧ x 0 < (1 : ℝ)} =
          {x | (0 : ℝ) < x 0 ∧ x 0 < (1 : ℝ)} := by
        ext x; simp
      simp [hself]
    · apply Set.finite_singleton
  · -- every maximal element has nonempty interior
    intro P hP hmax
    rw [Set.mem_singleton_iff.mp hP]
    -- interior of (0,1) is (0,1) itself, which is nonempty (contains 1/2)
    have h_open : IsOpen {x : Fin 1 → ℝ | (0 : ℝ) < x 0 ∧ x 0 < (1 : ℝ)} := by
      -- product of open intervals is open
      refine isOpen_setOf ?_
      -- the conditions x 0 > 0 and x 0 < 1 define an open set
      exact (isOpen_lt (continuous_apply 0) continuous_const).inter (isOpen_lt continuous_const (continuous_apply 0))
    have hinterior : interior {x : Fin 1 → ℝ | (0 : ℝ) < x 0 ∧ x 0 < (1 : ℝ)} =
        {x : Fin 1 → ℝ | (0 : ℝ) < x 0 ∧ x 0 < (1 : ℝ)} :=
      interior_eq_iff_isOpen.mpr h_open
    rw [hinterior]
    refine ⟨fun (_ : Fin 1) => (1/2 : ℝ), ?_⟩
    refine ⟨by norm_num, by norm_num⟩
