import Mathlib

/-!
# Generalized Associative Law

If an element of a group is constructed from a sequence `x₁, x₂, …, xₙ` in order by repeatedly
inserting brackets and applying the operation, the element must equal
`(…((x₁ ∘ x₂) ∘ x₃)…) ∘ xₙ`, independently of the bracketing.

We model "arbitrary bracketings" as the inductive predicate `BracketedProduct`,
and prove that any such bracketed product equals the right-associated (left-fold) product.
-/

variable {G : Type*} [Group G]

/-! ### Right-associated product -/

/-- Right-associated product of a nonempty list (the `Πʳ` from the gapfill proof).
`Πʳ(a₁) = a₁`, `Πʳ(a₁,…,aₘ) = Πʳ(a₁,…,aₘ₋₁) * aₘ` for `m ≥ 2`.
This is implemented as a left fold: `foldl (· * ·) a [b, c, …]`. -/
def rightProd : List G → G
  | a :: as => List.foldl (· * ·) a as
  | [] => 1

@[simp]
theorem rightProd_singleton (a : G) : rightProd [a] = a := rfl

@[simp]
theorem rightProd_cons (a b : G) (bs : List G) :
    rightProd (a :: b :: bs) = rightProd ((a * b) :: bs) := rfl

theorem rightProd_pair (a b : G) : rightProd [a, b] = a * b := rfl

/-! ### Auxiliary lemmas about `rightProd` and `foldl` -/

theorem foldl_mul_cons (x y : G) (ys : List G) :
    List.foldl (· * ·) x (y :: ys) = x * List.foldl (· * ·) y ys := by
  sorry
