import Mathlib

open scoped MonoidAlgebra

/-!
# Group Ring (Group Algebra)

For a group `G` and a ring `R` with identity, the **group ring** `R[G]` is the set of all
formal finite sums `∑_{x ∈ G} r_x·x` with coefficients `r_x ∈ R` and only finitely many
`r_x ≠ 0`. Addition is pointwise and multiplication is the convolution product:
`(∑ r_x·x)(∑ s_y·y) = ∑_{x,y} (r_x·s_y)·(x·y)`.

In Mathlib4, this is implemented as `MonoidAlgebra R G` (notation `R[G]` in the
`MonoidAlgebra` namespace), which is defined as `G →₀ R` (finitely supported functions
from `G` to `R`) with the convolution product.

## Main definitions
* `MonoidAlgebra R G` : the group ring type, notation `R[G]`
* `MonoidAlgebra.single g r` : the basis element representing `r·g`
* `MonoidAlgebra.of R G` : the canonical embedding `G →* R[G]` sending `g ↦ single g 1`
* `singleOneRingHom` : the canonical embedding `R →+* R[G]` sending `r ↦ single 1 r`

## References
* Dummit & Foote, §7.1 (Group Rings)
* Mathlib: `Mathlib/Algebra/MonoidAlgebra/Defs.lean`
-/

open MonoidAlgebra

noncomputable section

/-! ### Core definition (from Mathlib) -/

section group_ring_definition

variable (R G : Type*) [Ring R] [Group G]

/--
The group ring `R[G]` is Mathlib's `MonoidAlgebra R G`, defined as `G →₀ R`
(finitely supported functions from the group `G` to the coefficient ring `R`).
This captures the notion of "formal finite sums `∑ r_x·x`" from the textbook definition.
-/
example : Type _ := R[G]

/-- The basis element `single g r` represents the formal term `r·g` in the group ring. -/
example (g : G) (r : R) : R[G] := MonoidAlgebra.single g r

/-- The canonical embedding `G → R[G]` sending each group element `g` to `1·g`. -/
example (g : G) : R[G] := MonoidAlgebra.of R G g

/-- The canonical embedding `R → R[G]` sending each ring element `r` to `r·1_G`. -/
example (r : R) : R[G] := singleOneRingHom r

/-- The identity element of the group ring is `1_R·1_G`, represented as `single 1 1`.
This is true by definition of the `One` instance on `MonoidAlgebra`. -/
example : (1 : R[G]) = MonoidAlgebra.single (1 : G) (1 : R) :=
  rfl

/-- The zero element is the formal sum with all coefficients zero. -/
example : (0 : R[G]) = (0 : G →₀ R) := rfl

end group_ring_definition

/-! ### Ring structure -/

section ring_structure

variable (R G : Type*) [Ring R] [Group G]

/-- The group ring `R[G]` forms a ring.
Mathlib4 provides this instance when `R` is a `Ring` and `G` is a `Monoid` (hence also a `Group`). -/
example : Ring R[G] := by
  infer_instance

/-- `R[G]` is an `AddCommGroup` (the underlying additive structure). -/
example : AddCommGroup R[G] := by
  infer_instance

end ring_structure

/-! ### Multiplication (convolution product) -/

section multiplication

variable {R G : Type*} [Ring R] [Group G]

/-- The product of two basis elements obeys the convolution rule:
`(r₁·g₁) * (r₂·g₂) = (r₁·r₂)·(g₁·g₂)`.
This is the fundamental multiplication rule for the group ring. -/
example (g₁ g₂ : G) (r₁ r₂ : R) :
    MonoidAlgebra.single g₁ r₁ * MonoidAlgebra.single g₂ r₂ =
    MonoidAlgebra.single (g₁ * g₂) (r₁ * r₂) := by
  simp

/-- The product of the group embedding elements: `of g₁ * of g₂ = of (g₁ * g₂)`. -/
example (g₁ g₂ : G) :
    MonoidAlgebra.of R G g₁ * MonoidAlgebra.of R G g₂ = MonoidAlgebra.of R G (g₁ * g₂) := by
  simp

/-- Multiplication by the identity element: `1·x = x`. -/
example (x : R[G]) : (1 : R[G]) * x = x := by
  simp

/-- Multiplication by the identity element: `x·1 = x`. -/
example (x : R[G]) : x * (1 : R[G]) = x := by
  simp

/-- The zero element is absorbing: `0·x = 0`. -/
example (x : R[G]) : (0 : R[G]) * x = (0 : R[G]) := by
  simp

/-- The zero element is absorbing: `x·0 = 0`. -/
example (x : R[G]) : x * (0 : R[G]) = (0 : R[G]) := by
  simp

/-- Multiplication is associative. -/
example (x y z : R[G]) : (x * y) * z = x * (y * z) := by
  simp [mul_assoc]

/-- Multiplication distributes over addition on the left. -/
example (x y z : R[G]) : x * (y + z) = x * y + x * z := by
  simp [mul_add]

/-- Multiplication distributes over addition on the right. -/
example (x y z : R[G]) : (x + y) * z = x * z + y * z := by
  simp [add_mul]

end multiplication

/-! ### The group inverse -/

section group_inverse

variable {R G : Type*} [Ring R] [Group G]

/-- The canonical embedding `G → R[G]` maps inverses: `of (g⁻¹) * of g = 1`. -/
example (g : G) :
    MonoidAlgebra.of R G (g⁻¹) * MonoidAlgebra.of R G g = (1 : R[G]) := by
    simp

/-- Similarly, `of g * of (g⁻¹) = 1`. -/
example (g : G) :
    MonoidAlgebra.of R G g * MonoidAlgebra.of R G (g⁻¹) = (1 : R[G]) := by
    simp

end group_inverse

/-! ### Example: group ring over ℤ (the integral group ring `ℤ[G]`) -/

section examples_Z

variable {G : Type*} [Group G]

/-- `ℤ[G]` is the integral group ring. -/
example : Type _ := ℤ[G]

/-- `ℤ[G]` is a ring. -/
example : Ring (ℤ[G]) := by
  infer_instance

/-- Sum of two group ring elements:
`(3·a + 2·b) + (1·a + 4·b) = 4·a + 6·b`. -/
example (a b : G) :
    (MonoidAlgebra.single a (3 : ℤ) + MonoidAlgebra.single b (2 : ℤ)) +
    (MonoidAlgebra.single a (1 : ℤ) + MonoidAlgebra.single b (4 : ℤ)) =
    (MonoidAlgebra.single a (4 : ℤ) + MonoidAlgebra.single b (6 : ℤ)) := by
  calc
    (MonoidAlgebra.single a (3 : ℤ) + MonoidAlgebra.single b (2 : ℤ)) +
    (MonoidAlgebra.single a (1 : ℤ) + MonoidAlgebra.single b (4 : ℤ)) =
      ((MonoidAlgebra.single a (3 : ℤ) + MonoidAlgebra.single a (1 : ℤ)) +
       (MonoidAlgebra.single b (2 : ℤ) + MonoidAlgebra.single b (4 : ℤ))) := by abel
    _ = (MonoidAlgebra.single a ((3 : ℤ) + (1 : ℤ)) +
         MonoidAlgebra.single b ((2 : ℤ) + (4 : ℤ))) := by
      simp [← MonoidAlgebra.single_add]
    _ = MonoidAlgebra.single a (4 : ℤ) + MonoidAlgebra.single b (6 : ℤ) := by norm_num

/-- Product: `(3·a) * (2·b) = 6·(a*b)`. -/
example (a b : G) :
    MonoidAlgebra.single a (3 : ℤ) * MonoidAlgebra.single b (2 : ℤ) =
    MonoidAlgebra.single (a * b) (6 : ℤ) := by
  simp

/-- Product expansion when group elements commute:
if `a` and `b` commute, then `(a + b) * (a - b) = a^2 - b^2` in `ℤ[G]`. -/
example (a b : G) (h_comm : a * b = b * a) :
    (MonoidAlgebra.of ℤ G a + MonoidAlgebra.of ℤ G b) *
    (MonoidAlgebra.of ℤ G a - MonoidAlgebra.of ℤ G b) =
    MonoidAlgebra.of ℤ G (a ^ 2) - MonoidAlgebra.of ℤ G (b ^ 2) := by
  calc
    (MonoidAlgebra.of ℤ G a + MonoidAlgebra.of ℤ G b) *
    (MonoidAlgebra.of ℤ G a - MonoidAlgebra.of ℤ G b) =
      (MonoidAlgebra.of ℤ G a) * (MonoidAlgebra.of ℤ G a)
      - (MonoidAlgebra.of ℤ G a) * (MonoidAlgebra.of ℤ G b)
      + (MonoidAlgebra.of ℤ G b) * (MonoidAlgebra.of ℤ G a)
      - (MonoidAlgebra.of ℤ G b) * (MonoidAlgebra.of ℤ G b) := by
        rw [mul_sub, add_mul, add_mul]; abel
    _ = MonoidAlgebra.of ℤ G (a * a) - MonoidAlgebra.of ℤ G (a * b)
      + MonoidAlgebra.of ℤ G (b * a) - MonoidAlgebra.of ℤ G (b * b) := by
        simp
    _ = MonoidAlgebra.of ℤ G (a ^ 2) - MonoidAlgebra.of ℤ G (a * b)
      + MonoidAlgebra.of ℤ G (a * b) - MonoidAlgebra.of ℤ G (b ^ 2) := by
        simp [h_comm, pow_two]
    _ = MonoidAlgebra.of ℤ G (a ^ 2) - MonoidAlgebra.of ℤ G (b ^ 2) := by
      abel

end examples_Z

/-! ### Example: group ring over a field (the group algebra `k[G]`) -/

section examples_field

variable (k G : Type*) [Field k] [Group G]

/-- `k[G]` is the group algebra over a field — a `k`-algebra. -/
example : Algebra k k[G] := by
  infer_instance

/-- `k[G]` is a `k`-vector space. -/
example : Module k k[G] := by
  infer_instance

/-- The group algebra contains the group `G` via the embedding `of k G`. -/
example (g : G) : k[G] := MonoidAlgebra.of k G g

/-- Scalar multiplication: `r • of g = single g r`. -/
example (r : k) (g : G) : r • MonoidAlgebra.of k G g = MonoidAlgebra.single g r := by
  simp

end examples_field

/-! ### Example: finite group ring and the augmentation map -/

section examples_finite_group

variable (R G : Type*) [Ring R] [Group G] [Fintype G] [DecidableEq G]

open scoped BigOperators

/-- The sum of the group basis elements `∑_{g ∈ G} single g 1` is a well-defined
element of the group ring (since the sum is finite). -/
example : R[G] := ∑ g : G, MonoidAlgebra.single g (1 : R)

/-- The group ring of a finite group is a finite-dimensional module over its coefficient ring. -/
example : Module.Finite R R[G] := by
  exact inferInstance

/-- The augmentation map `ε : R[G] → R` sending `∑ r_g·g` to `∑ r_g`.
This is a ring homomorphism (the "augmentation homomorphism").
We use `Finsupp.sum` to sum all coefficients of a finitely supported function. -/
noncomputable def augmentation : R[G] →+* R where
  toFun x := Finsupp.sum x fun _ r => r
  map_one' := by simp [Finsupp.sum_single_index]
  map_mul' x y := by
    classical
    simp [MonoidAlgebra.mul_def, Finsupp.sum_sum_index, Finsupp.sum_add_index,
      Finsupp.sum_mul, Finsupp.mul_sum, mul_comm, add_comm]
  map_zero' := by simp
  map_add' x y := by simp [Finsupp.sum_add_index]

/-- The augmentation map evaluates the sum of all coefficients for a single basis element. -/
example (g : G) (r : R) : augmentation R G (MonoidAlgebra.single g r) = r := by
  simp [augmentation]

/-- The augmentation of a group element (via `of`) is 1. -/
example (g : G) : augmentation R G (MonoidAlgebra.of R G g) = 1 := by
  simp [augmentation]

end examples_finite_group

/-! ### Connections: group ring and tensor product -/

section tensor_connection

variable (R G : Type*) [CommRing R] [Group G]

/-- The group ring `R[G]` is isomorphic to the tensor product `R ⊗_ℤ ℤ[G]`
where `ℤ[G]` is the integral group ring. This reflects the fact that every
group ring over a commutative ring is the base change of the integral group ring. -/
example : R[G] ≃ₐ[R] R ⊗[ℤ] ℤ[G] :=
  MonoidAlgebra.ringEquivTensorProduct R G

end tensor_connection

end noncomputable section
