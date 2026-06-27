import Mathlib

open MulOpposite

/-!
# Natural Anti-isomorphism to Opposite Ring

The identity map on the underlying set, r ↦ r, is an anti-isomorphism from
a ring R to its opposite ring Rᵒᵖ.

In Mathlib4, the map is `MulOpposite.op` (and its inverse is `MulOpposite.unop`).
This map is:
- **Bijective**: `MulOpposite.opEquiv` gives the canonical bijection between R and Rᵐᵒᵖ
- **Additive**: `op (a + b) = op a + op b` (rfl)
- **Anti-multiplicative**: `op (a * b) = op b * op a` (rfl, this is the definition of multiplication in Rᵐᵒᵖ)

For commutative rings, this anti-isomorphism is actually an ordinary ring isomorphism
(`MulOpposite.opMulEquiv`). For non-commutative rings, it is a genuine anti-isomorphism.
-/

/-! ### 1. Definition of Ring Anti-isomorphism

We define a `RingAntiEquiv` as a bijective map between rings that preserves addition
and reverses multiplication. -/

/-- A `RingAntiEquiv R S` is a bijective map `R → S` that preserves addition
and reverses multiplication: `φ(a + b) = φ a + φ b` and `φ(a * b) = φ b * φ a`.

This is the appropriate notion of "anti-isomorphism" between (possibly non-commutative) rings.
-/
structure RingAntiEquiv (R S : Type*) [Add R] [Mul R] [Add S] [Mul S] extends R ≃ S where
  map_add' : ∀ x y, toEquiv (x + y) = toEquiv x + toEquiv y
  map_mul' : ∀ x y, toEquiv (x * y) = toEquiv y * toEquiv x

/-- Notation for `RingAntiEquiv`. -/
infixl:25 " ≃ₐ+* " => RingAntiEquiv

namespace RingAntiEquiv

variable {R S T : Type*} [Add R] [Mul R] [Add S] [Mul S] [Add T] [Mul T]

instance : CoeFun (R ≃ₐ+* S) fun _ => R → S :=
  ⟨fun φ => φ.toEquiv⟩

@[simp]
theorem apply_eq_iff_eq (φ : R ≃ₐ+* S) {x y : R} : φ x = φ y ↔ x = y :=
  φ.toEquiv.apply_eq_iff_eq

/-- The inverse of a ring anti-isomorphism is a ring anti-isomorphism. -/
def symm (φ : R ≃ₐ+* S) : S ≃ₐ+* R where
  toEquiv := φ.toEquiv.symm
  map_add' x y := by
    apply φ.toEquiv.injective
    calc
      φ (φ.toEquiv.symm (x + y)) = x + y := φ.toEquiv.apply_symm_apply _
      _ = φ (φ.toEquiv.symm x) + φ (φ.toEquiv.symm y) := by
        simp [φ.toEquiv.apply_symm_apply]
      _ = φ (φ.toEquiv.symm x + φ.toEquiv.symm y) := by rw [φ.map_add']
  map_mul' x y := by
    apply φ.toEquiv.injective
    calc
      φ (φ.toEquiv.symm (x * y)) = x * y := φ.toEquiv.apply_symm_apply _
      _ = φ (φ.toEquiv.symm x) * φ (φ.toEquiv.symm y) := by
        simp [φ.toEquiv.apply_symm_apply]
      _ = φ (φ.toEquiv.symm y * φ.toEquiv.symm x) := by rw [φ.map_mul']

end RingAntiEquiv

/-! ### 2. Main Theorem: `MulOpposite.op` is a Ring Anti-isomorphism

The core result: the map `r ↦ op r` (which is the identity on the underlying set,
wrapped in the `MulOpposite` constructor) is an anti-isomorphism from any ring `R` to `Rᵐᵒᵖ`.
-/

section main_theorem

variable (R : Type*) [NonUnitalNonAssocRing R]

/-- The canonical map `MulOpposite.op : R → Rᵐᵒᵖ` is a ring anti-isomorphism.
It is the identity on the underlying set, so `op r` is essentially `r`, but viewed
as an element of the opposite ring.

Proof summary:
1. Bijectivity: `MulOpposite.opEquiv` provides the canonical bijection.
2. Addition preservation: `op_add` (true by definition).
3. Multiplication reversal: `op_mul` — in `Rᵐᵒᵖ`, multiplication is defined by
   `op a * op b = op (b * a)`, so `op (a * b) = op b * op a`. -/
def naturalAntiIso (R : Type*) [NonUnitalNonAssocRing R] : R ≃ₐ+* Rᵐᵒᵖ where
  toEquiv := MulOpposite.opEquiv
  map_add' _ _ := MulOpposite.op_add _ _
  map_mul' _ _ := MulOpposite.op_mul _ _

/-- The canonical map `MulOpposite.op` from a ring to its opposite ring is a ring anti-isomorphism.
(This is the same as `naturalAntiIso` but stated with explicit type arguments.) -/
def op_is_ring_anti_equiv (R : Type*) [NonUnitalNonAssocRing R] : R ≃ₐ+* Rᵐᵒᵖ :=
  naturalAntiIso R

end main_theorem

/-! ### 3. Alternative Formulation: AddEquiv + Anti-multiplicative Property

Rather than defining a new `RingAntiEquiv` structure, one can state the theorem
using Mathlib4's existing typeclasses: `MulOpposite.op` is an `AddEquiv` that
reverses multiplication. -/

section alternative_formulation

variable (R : Type*) [NonUnitalNonAssocRing R]

/-- `MulOpposite.op` is an additive equivalence (already in Mathlib4 as `MulOpposite.opAddEquiv`). -/
example : R ≃+ Rᵐᵒᵖ := MulOpposite.opAddEquiv

/-- `MulOpposite.op` preserves zero: `op 0 = 0`. -/
example : MulOpposite.op (0 : R) = (0 : Rᵐᵒᵖ) := by
  simp

/-- `MulOpposite.op` preserves negation: `op (-a) = -op a`. -/
example (a : R) : MulOpposite.op (-a) = -MulOpposite.op a := by
  simp

/-- `MulOpposite.op` preserves addition: `op (a + b) = op a + op b`. -/
example (a b : R) : MulOpposite.op (a + b) = MulOpposite.op a + MulOpposite.op b := by
  simp

/-- `MulOpposite.op` reverses multiplication: `op (a * b) = op b * op a`.
This is the key property that makes it an *anti*-isomorphism rather than an isomorphism. -/
example (a b : R) : MulOpposite.op (a * b) = MulOpposite.op b * MulOpposite.op a := by
  simp

/-- `MulOpposite.op` is bijective, with inverse `MulOpposite.unop`. -/
example : Function.Bijective (MulOpposite.op : R → Rᵐᵒᵖ) :=
  MulOpposite.op_bijective

/-- The inverse `MulOpposite.unop` also reverses multiplication. -/
example (a b : Rᵐᵒᵖ) : MulOpposite.unop (a * b) = MulOpposite.unop b * MulOpposite.unop a := by
  simp

end alternative_formulation

/-! ### 4. Special Case: Commutative Rings

When `R` is commutative, the anti-isomorphism `R ≃ₐ+* Rᵐᵒᵖ` is actually an ordinary
ring isomorphism `R ≃+* Rᵐᵒᵖ`. Mathlib4 provides this as `MulOpposite.opMulEquiv`. -/

section commutative_case

variable (R : Type*) [CommSemiring R]

/-- For a commutative semiring, `MulOpposite.op` is a multiplicative equivalence
(already in Mathlib4 as `opMulEquiv`). -/
example : R ≃* Rᵐᵒᵖ := MulOpposite.opMulEquiv

/-- When R is commutative, `op (a * b) = op a * op b` holds as well
(since multiplication is commutative, the reversal has no effect). -/
example (a b : R) : MulOpposite.op (a * b) = MulOpposite.op a * MulOpposite.op b := by
  rw [MulOpposite.op_mul, mul_comm]

/-- Alternative proof using `calc`. -/
example (a b : R) : MulOpposite.op (a * b) = MulOpposite.op a * MulOpposite.op b := by
  calc
    MulOpposite.op (a * b) = MulOpposite.op b * MulOpposite.op a := by simp
    _ = MulOpposite.op a * MulOpposite.op b := mul_comm _ _

/-- For a commutative ring, the anti-isomorphism gives a `RingEquiv` via
the fact that `RingEquiv.op` sends `RingEquiv.refl R` to an isomorphism `Rᵐᵒᵖ ≃+* Rᵐᵒᵖ`. -/
example : RingEquiv (Rᵐᵒᵖ) (Rᵐᵒᵖ) := RingEquiv.refl _

/-- When R is commutative, the ring `R` and its opposite `Rᵐᵒᵖ` are isomorphic as rings
(via `MulOpposite.opMulEquiv` combined with the additive equivalence). -/
example : R ≃+* Rᵐᵒᵖ :=
  { MulOpposite.opMulEquiv with
    map_add' := MulOpposite.op_add }

end commutative_case

/-! ### 5. Concrete Examples -/

section examples

/-- Example: ℤ → ℤᵐᵒᵖ via op is an anti-isomorphism.
Since ℤ is commutative, this is also a regular isomorphism. -/
example : ℤ ≃ₐ+* ℤᵐᵒᵖ := naturalAntiIso ℤ

/-- Example: The ring of integers in the opposite ring — addition. -/
example : MulOpposite.op ((2 : ℤ) + (3 : ℤ)) = MulOpposite.op (2 : ℤ) + MulOpposite.op (3 : ℤ) := by
  norm_num

/-- Example: Multiplication reversal in ℤᵐᵒᵖ. -/
example : MulOpposite.op ((2 : ℤ) * (3 : ℤ)) = MulOpposite.op (3 : ℤ) * MulOpposite.op (2 : ℤ) := by
  norm_num

/-- Example: Matrix ring M₂(ℝ) → M₂(ℝ)ᵐᵒᵖ.
For non-commutative rings, this is genuinely an anti-isomorphism,
not a regular isomorphism. -/
abbrev M2 := Matrix (Fin 2) (Fin 2) ℝ

example : M2 ≃ₐ+* M2ᵐᵒᵖ := naturalAntiIso M2

/-- For M₂(ℝ), multiplication reversal is a non-trivial property:
`op (A * B) = op B * op A` in M₂(ℝ)ᵐᵒᵖ. -/
example (A B : M2) : MulOpposite.op (A * B) = MulOpposite.op B * MulOpposite.op A := by
  simp

/-- The inverse `unop` also gives an anti-isomorphism back: `Rᵐᵒᵖ → R`. -/
example (R : Type*) [Ring R] : Rᵐᵒᵖ ≃ₐ+* R :=
  (naturalAntiIso R).symm

/-- `op` followed by `unop` is the identity. -/
example (R : Type*) [Ring R] (r : R) : MulOpposite.unop (MulOpposite.op r) = r := by
  simp

/-- `unop` followed by `op` is the identity. -/
example (R : Type*) [Ring R] (x : Rᵐᵒᵖ) : MulOpposite.op (MulOpposite.unop x) = x := by
  simp

end examples

/-! ### 6. Verification Against the Gap-Fill Proof

The gap-fill proof has 14 steps. Here we verify each step in Lean:

**Steps 1-2**: Define θ(r) = r as map R → Rᵒᵖ; this is `MulOpposite.op`.
**Step 3**: θ is bijective — `MulOpposite.opEquiv` / `MulOpposite.op_bijective`
**Steps 4-6**: θ preserves addition — `MulOpposite.op_add`
**Steps 7-9**: θ reverses multiplication — `MulOpposite.op_mul`
**Steps 10-11**: θ is an anti-homomorphism — combination of op_add and op_mul
**Steps 12-13**: θ is an anti-isomorphism — bijective + anti-homomorphism
**Step 14**: Conclusion — `naturalAntiIso R` -/

section gapfill_verification

/-- Step 3: The map θ = op is bijective. -/
theorem step3_bijective (R : Type*) : Function.Bijective (MulOpposite.op : R → Rᵐᵒᵖ) :=
  MulOpposite.op_bijective

/-- Steps 4-6: The map θ preserves addition. -/
theorem step6_additive (R : Type*) [Add R] (a b : R) :
    MulOpposite.op (a + b) = MulOpposite.op a + MulOpposite.op b :=
  MulOpposite.op_add a b

/-- Steps 7-9: The map θ reverses multiplication. -/
theorem step9_antimultiplicative (R : Type*) [Mul R] (a b : R) :
    MulOpposite.op (a * b) = MulOpposite.op b * MulOpposite.op a :=
  MulOpposite.op_mul a b

/-- Steps 10-13: θ is an anti-isomorphism (bijective + additive + anti-multiplicative). -/
def step13_anti_isomorphism (R : Type*) [NonUnitalNonAssocRing R] : R ≃ₐ+* Rᵐᵒᵖ :=
  naturalAntiIso R

/-- Step 14: Conclusion (same as step 13). -/
def step14_conclusion (R : Type*) [NonUnitalNonAssocRing R] : R ≃ₐ+* Rᵐᵒᵖ :=
  naturalAntiIso R

end gapfill_verification
