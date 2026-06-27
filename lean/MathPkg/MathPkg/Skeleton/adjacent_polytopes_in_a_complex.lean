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
def AreAdjacent (P Q : Set (Fin n → ℝ)) (Δ : Set (Set (Fin n → ℝ))) : Prop := by
  sorry
