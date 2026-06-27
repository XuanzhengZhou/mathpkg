import Mathlib

/-!
# Supporting Hyperplane of a Polytope

A supporting hyperplane H of a convex polytope P ⊂ ℝⁿ is a hyperplane such that
P is entirely contained in one of the closed half-spaces determined by H and
H ∩ P is non-empty.

We represent a hyperplane as `{x | l x = a}` where `l` is a nonzero continuous linear
functional (`StrongDual ℝ E`) and `a` is a real number. The closed half-space
containing the polytope is `{x | l x ≥ a}` (or equivalently `{x | a ≤ l x}`).

## Main definition

* `IsSupportingHyperplane l a P` -- asserts that the hyperplane `H = {x | l x = a}`
  supports the set `P`. Formally, every point `x ∈ P` lies in the closed half-space
  `{x | a ≤ l x}`, and the hyperplane touches `P`, i.e., `H ∩ P ≠ ∅`.

This definition generalizes the classical notion of a supporting hyperplane of a
convex polytope in ℝⁿ and can be instantiated for any set in a real normed vector space.

## References

* [Barry Simon, *Convexity*][simon2011], Chapter 8
-/

open Set

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/--
A supporting hyperplane of a set `P` in a real normed vector space `E`,
represented by a continuous linear functional `l : StrongDual ℝ E` and a threshold `a : ℝ`.

The hyperplane is `H = {x : E | l x = a}`. The definition states:

1. `P` is contained in the closed half-space determined by `H`: `∀ x ∈ P, a ≤ l x`.
   (Equivalently, all points of `P` lie on the same side of `H`.)
2. The hyperplane touches `P`: `∃ x ∈ P, l x = a`. (i.e., `H ∩ P ≠ ∅`.)

This matches the classical geometric intuition: the hyperplane `H` bounds `P` from
"below" and makes contact with `P` at least at one point. Negating `l` gives the
upper-supporting variant `∀ x ∈ P, l x ≤ a`.
-/
def IsSupportingHyperplane (l : StrongDual ℝ E) (a : ℝ) (P : Set E) : Prop :=
  (∀ x ∈ P, a ≤ l x) ∧ (∃ x ∈ P, l x = a)

/-! ## Examples -/

/-- In ℝ, the point `0` provides a supporting hyperplane for the unit interval `[0,1]`.
The functional is the identity `ContinuousLinearMap.id`, the threshold is `a = 0`,
and `P = [0,1]`. Indeed, every `x ∈ [0,1]` satisfies `0 ≤ x`, and `0 ∈ [0,1]` gives
the touching point. -/
example : IsSupportingHyperplane (ContinuousLinearMap.id ℝ ℝ) 0 (Set.Icc (0 : ℝ) 1) := by
  refine ⟨?_, ?_⟩
  · rintro x ⟨hx0, hx1⟩
    exact hx0
  · refine ⟨0, ⟨by norm_num, by norm_num⟩, ?_⟩
    simp

/-- In ℝ², the x-axis (y = 0) is a supporting hyperplane of the unit square `[0,1]×[0,1]`.
The functional is the projection onto the y-coordinate
`ContinuousLinearMap.snd ℝ ℝ ℝ`, the threshold is `a = 0`,
and the touching point is `(0,0)`. -/
example : IsSupportingHyperplane (ContinuousLinearMap.snd ℝ ℝ ℝ) 0
    (Set.Icc (0, 0) (1, 1) : Set (ℝ × ℝ)) := by
  refine ⟨?_, ?_⟩
  · rintro ⟨x, y⟩ ⟨⟨hx0, hy0⟩, ⟨hx1, hy1⟩⟩
    exact hy0
  · refine ⟨(0, 0), ?_, ?_⟩
    · refine ⟨?_, ?_⟩
      · constructor <;> norm_num
      · constructor <;> norm_num
    · simp

/-- In ℝ², the line `y = 1` supports the unit square from above.
Using the negated functional `-snd`, the condition becomes `1 ≤ -y` (equivalently `y ≤ -1`),
which is not what we want for the upper face. Instead, we use `l = snd` with `a = 1`
and the reversed inequality `∀ x ∈ P, l x ≤ a`. This variant is obtained by
negating the functional: `IsSupportingHyperplane (-l) (-a) P`. -/
example : IsSupportingHyperplane (-ContinuousLinearMap.snd ℝ ℝ ℝ) (-1)
    (Set.Icc (0, 0) (1, 1) : Set (ℝ × ℝ)) := by
  refine ⟨?_, ?_⟩
  · rintro ⟨x, y⟩ ⟨⟨hx0, hy0⟩, ⟨hx1, hy1⟩⟩
    -- Need to show: -1 ≤ -y  ⇔  y ≤ 1
    linarith
  · refine ⟨(0, 1), ?_, ?_⟩
    · refine ⟨?_, ?_⟩
      · constructor <;> norm_num
      · constructor <;> norm_num
    · simp
