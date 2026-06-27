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
  induction ys generalizing x y with
  | nil => simp
  | cons z zs ih =>
    calc
      List.foldl (· * ·) x (y :: z :: zs) = List.foldl (· * ·) (x * y) (z :: zs) := rfl
      _ = (x * y) * List.foldl (· * ·) z zs := by rw [ih (x * y) z]
      _ = x * (y * List.foldl (· * ·) z zs) := by group
      _ = x * List.foldl (· * ·) y (z :: zs) := by rw [ih y z]

theorem rightProd_append (l₁ l₂ : List G) (h₁ : l₁ ≠ []) (h₂ : l₂ ≠ []) :
    rightProd (l₁ ++ l₂) = rightProd l₁ * rightProd l₂ := by
  cases l₁ with
  | nil => exact (h₁ rfl).elim
  | cons a as =>
    cases l₂ with
    | nil => exact (h₂ rfl).elim
    | cons b bs =>
      calc
        rightProd ((a :: as) ++ (b :: bs))
            = rightProd (a :: (as ++ (b :: bs))) := rfl
        _ = List.foldl (· * ·) a (as ++ (b :: bs)) := rfl
        _ = List.foldl (· * ·) (List.foldl (· * ·) a as) (b :: bs) := by rw [List.foldl_append]
        _ = (List.foldl (· * ·) a as) * List.foldl (· * ·) b bs := by rw [foldl_mul_cons]
        _ = rightProd (a :: as) * rightProd (b :: bs) := rfl

/-! ### Bracketed products

A `BracketedProduct l u` means that `u` can be obtained from the sequence given by `l`
by repeatedly inserting brackets and applying the binary operation.
-/

inductive BracketedProduct : List G → G → Prop
  | single (a : G) : BracketedProduct [a] a
  | mul {l₁ l₂ : List G} {v w : G} (hp₁ : BracketedProduct l₁ v) (hp₂ : BracketedProduct l₂ w) :
      BracketedProduct (l₁ ++ l₂) (v * w)

lemma BracketedProduct.ne_nil {l : List G} {u : G} (hp : BracketedProduct l u) : l ≠ [] := by
  induction hp with
  | single a => simp
  | mul hp₁ hp₂ ih₁ ih₂ =>
    intro hnil
    exact ih₁ ((List.append_eq_nil_iff.mp hnil).1)

/-! ### Generalized Associative Law -/

/-- **Generalized Associative Law**: Any bracketed product of a sequence of group elements
equals the right-associated (left-fold) product, independent of the bracketing.

Proof by induction on the bracketing tree (structural induction on `BracketedProduct`):
- Base case (single element): trivial.
- Inductive step: if `u = v * w` where `v` is from prefix `l₁` and `w` from suffix `l₂`,
  then by IH `v = rightProd l₁` and `w = rightProd l₂`, and the `rightProd_append` lemma
  gives `rightProd l₁ * rightProd l₂ = rightProd (l₁ ++ l₂)`. -/
theorem generalized_associative_law {l : List G} {u : G} (hp : BracketedProduct l u) :
    u = rightProd l := by
  induction hp
  case single a =>
    simp
  case mul l₁ l₂ v w hp₁ hp₂ ih₁ ih₂ =>
    rw [ih₁, ih₂, rightProd_append l₁ l₂ (hp₁.ne_nil) (hp₂.ne_nil)]

/-! ### Alternative formulation using `FreeMagma`

We also provide a formulation using `FreeMagma G` (binary trees with leaves in `G`)
as the representation of arbitrary bracketings. -/

open FreeMagma

/-- Evaluate a `FreeMagma G` tree in `G`. -/
def FreeMagma.eval : FreeMagma G → G
  | of a => a
  | t₁ * t₂ => t₁.eval * t₂.eval

/-- Extract the leaves of a `FreeMagma G` tree in left-to-right order. -/
def FreeMagma.leaves : FreeMagma G → List G
  | of a => [a]
  | t₁ * t₂ => t₁.leaves ++ t₂.leaves

/-- Any `FreeMagma` tree evaluates to a bracketed product of its leaves. -/
theorem FreeMagma.eval_is_bracketed (t : FreeMagma G) : BracketedProduct t.leaves t.eval := by
  induction t with
  | ih1 a => exact BracketedProduct.single a
  | ih2 t₁ t₂ ih₁ ih₂ =>
      simp [FreeMagma.eval, FreeMagma.leaves]
      exact BracketedProduct.mul ih₁ ih₂

/-- **Generalized Associative Law** (FreeMagma version):
Any evaluation of a `FreeMagma G` tree equals the right-associated product of its leaves. -/
theorem generalized_associative_law_freeMagma (t : FreeMagma G) :
    t.eval = rightProd t.leaves :=
  generalized_associative_law t.eval_is_bracketed

/-! ### Examples -/

/-- Example: `(a*b)*c` produces the same result via `BracketedProduct`. -/
example (a b c : G) : (a * b) * c = rightProd [a, b, c] := by
  have hp : BracketedProduct [a, b, c] ((a * b) * c) :=
    BracketedProduct.mul
      (BracketedProduct.mul (BracketedProduct.single a) (BracketedProduct.single b))
      (BracketedProduct.single c)
  rw [generalized_associative_law hp]

/-- Example: an arbitrary bracketing `(a*(b*(c*d)))` equals `rightProd [a,b,c,d]`. -/
example (a b c d : G) : a * (b * (c * d)) = rightProd [a, b, c, d] := by
  have hp : BracketedProduct [a, b, c, d] (a * (b * (c * d))) :=
    BracketedProduct.mul
      (BracketedProduct.single a)
      (BracketedProduct.mul
        (BracketedProduct.single b)
        (BracketedProduct.mul (BracketedProduct.single c) (BracketedProduct.single d)))
  rw [generalized_associative_law hp]

/-- Example: `rightProd` for 2 elements matches direct multiplication. -/
example (a b : G) : rightProd [a, b] = a * b := by
  simp
