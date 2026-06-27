import Mathlib

/-!
# Adjacent Polytopes in a Complex

Two `n`-dimensional polytopes `P`, `Q` in a polyhedral complex `Δ` in `ℝⁿ` are said to be
**adjacent** if they are distinct and their intersection lies in an affine hyperplane.
In a pure `n`-dimensional complex this means `P` and `Q` share an `(n−1)`-dimensional common face.

Formally, a nonzero linear functional `f` and a scalar `b` witness that the intersection
`P ∩ Q` is contained in the affine hyperplane `{x | f x = b}`.

## Main definition

* `AreAdjacent P Q Δ` : `Prop` asserting that `P` and `Q` are adjacent `n`-dimensional
  polytopes in the complex `Δ`.

## References

* [Cox–Little–O'Shea, *Ideals, Varieties, and Algorithms*][cox2015]
-/

open Set

variable {n : ℕ}

/--
Two `n`-dimensional polytopes `P`, `Q` in a polyhedral complex `Δ` are **adjacent** if:

* `P ∈ Δ` and `Q ∈ Δ` — both are cells of the complex,
* `P ≠ Q` — they are distinct,
* `(P ∩ Q).Nonempty` — their intersection is nonempty,
* ∃ `f : (Fin n → ℝ) →ₗ[ℝ] ℝ`, `b : ℝ` with `f ≠ 0` such that `P ∩ Q ⊆ {x | f x = b}` —
  the intersection lies in an affine hyperplane of `ℝⁿ`.

In a pure `n`-dimensional polyhedral complex this means `P` and `Q` share a face
of dimension `n−1` (a common facet of each).
-/
def AreAdjacent (P Q : Set (Fin n → ℝ)) (Δ : Set (Set (Fin n → ℝ))) : Prop :=
  P ∈ Δ ∧ Q ∈ Δ ∧ P ≠ Q ∧ (P ∩ Q).Nonempty ∧
  ∃ (f : LinearMap ℝ (Fin n → ℝ) ℝ) (b : ℝ), f ≠ 0 ∧ P ∩ Q ⊆ {x | f x = b}

/-! ## Example -/

/--
In `ℝ¹`, the two unit intervals `[0, 1]` and `[1, 2]` are adjacent polytopes in the
complex `Δ` consisting of just these two intervals (the closed unit simplexes in `ℝ¹`).
They share the single point `{1}`, which is contained in the affine hyperplane
`{x | x = 1}` (a `0`-dimensional hyperplane in `ℝ¹`). The linear functional is
the projection onto the zeroth coordinate.
-/
example : AreAdjacent
    {x : Fin 1 → ℝ | 0 ≤ x 0 ∧ x 0 ≤ 1}
    {x : Fin 1 → ℝ | 1 ≤ x 0 ∧ x 0 ≤ 2}
    {{x : Fin 1 → ℝ | 0 ≤ x 0 ∧ x 0 ≤ 1}, {x : Fin 1 → ℝ | 1 ≤ x 0 ∧ x 0 ≤ 2}} := by
  unfold AreAdjacent
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · -- P ∈ Δ
    simp
  · -- Q ∈ Δ
    simp
  · -- P ≠ Q: the point x₀ = 1/2 is in P but not in Q
    intro h
    have hhalf : (fun (_ : Fin 1) => (1/2 : ℝ)) ∈
      {x : Fin 1 → ℝ | 0 ≤ x 0 ∧ x 0 ≤ 1} := by
      refine ⟨by norm_num, by norm_num⟩
    rw [h] at hhalf
    rcases hhalf with ⟨h0, h1⟩
    linarith
  · -- (P ∩ Q).Nonempty: the point x₀ = 1 is in both
    refine ⟨fun (_ : Fin 1) => (1 : ℝ), ?_, ?_⟩
    · exact ⟨by norm_num, by norm_num⟩
    · exact ⟨by norm_num, by norm_num⟩
  · -- ∃ f b, f ≠ 0 ∧ P ∩ Q ⊆ {x | f x = 1}
    refine ⟨LinearMap.proj 0, 1, ?_, ?_⟩
    · -- f ≠ 0: the projection onto the first coordinate sends (1, …) to 1 ≠ 0
      intro hzero
      have htest := congrArg (fun φ => φ (fun (_ : Fin 1) => (1 : ℝ))) hzero
      simpa [LinearMap.proj_apply] using htest
    · -- P ∩ Q ⊆ {x | x₀ = 1}
      rintro x ⟨⟨hP0, hP1⟩, ⟨hQ0, hQ1⟩⟩
      have hx0 : x 0 = 1 := by
        linarith
      simp [LinearMap.proj_apply, hx0]
