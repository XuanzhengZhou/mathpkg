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
example : (1 : R[G]) = MonoidAlgebra.single (1 : G) (1 : R) := by
  sorry
