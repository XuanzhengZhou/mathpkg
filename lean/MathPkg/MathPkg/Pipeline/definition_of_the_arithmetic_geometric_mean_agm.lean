import Mathlib

/-!
# Definition of the Arithmetic-Geometric Mean (AGM)

Let `a` and `b` be two positive real numbers. The **Arithmetic-Geometric mean** of `a` and `b`,
denoted by `AGM(a, b)`, is defined as the common limit of the sequences `a_n` and `b_n`
defined by:

* `a₀ = a`, `b₀ = b`
* `a_{n+1} = (a_n + b_n) / 2`  (arithmetic mean)
* `b_{n+1} = √(a_n · b_n)`  (geometric mean)

Starting with two nonnegative real numbers and repeatedly replacing them with their
arithmetic and geometric means, the two monotone sequences converge to the same limit:
the arithmetic-geometric mean (AGM).

Mathlib4 already provides `NNReal.agm` for nonnegative reals.
We define `Real.agm` as a wrapper for positive real numbers, which is the classical setting.
-/

open Real

/-- The arithmetic-geometric mean of two nonnegative real numbers `a` and `b`.

This is the common limit of the sequences defined by iteratively replacing
`(a, b)` with `((a + b) / 2, √(a · b))`.

Uses Mathlib4's `NNReal.agm` by converting to `ℝ≥0` and back. -/
noncomputable def agm (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) : ℝ :=
  NNReal.agm ⟨a, ha⟩ ⟨b, hb⟩

namespace agm

/-- `agm a b ha hb` is the common limit of the arithmetic and geometric mean sequences. -/

/-- Commutativity: `agm a b ha hb = agm b a hb ha`. -/
theorem comm (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) : agm a b ha hb = agm b a hb ha := by
  simp [agm, NNReal.agm_comm]

/-- For equal arguments: `agm a a ha ha = a`. -/
@[simp]
theorem self (a : ℝ) (ha : 0 ≤ a) : agm a a ha ha = a := by
  simp [agm, NNReal.agm_self]

/-- If both arguments are positive, the AGM is also positive. -/
theorem pos (a b : ℝ) (ha : 0 < a) (hb : 0 < b) (hpa : 0 ≤ a := ha.le) (hpb : 0 ≤ b := hb.le) :
    0 < agm a b hpa hpb :=
  NNReal.agm_pos ha hb

/-- The AGM is at most the maximum of the two arguments. -/
theorem le_max (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) : agm a b ha hb ≤ max a b :=
  NNReal.agm_le_max

/-- The minimum of the two arguments is at most the AGM. -/
theorem min_le (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) : min a b ≤ agm a b ha hb :=
  NNReal.min_le_agm

/-- Zero AGM: `agm 0 b (by norm_num) hb = 0`. -/
@[simp]
theorem zero_left (b : ℝ) (hb : 0 ≤ b) : agm 0 b (by norm_num) hb = 0 := by
  simp [agm]

/-- Zero AGM: `agm a 0 ha (by norm_num) = 0`. -/
@[simp]
theorem zero_right (a : ℝ) (ha : 0 ≤ a) : agm a 0 ha (by norm_num) = 0 := by
  simp [agm]

/-- The AGM distributes over multiplication by a nonnegative scalar. -/
theorem mul_distrib (k a b : ℝ) (hk : 0 ≤ k) (ha : 0 ≤ a) (hb : 0 ≤ b) :
    agm (k * a) (k * b) (mul_nonneg hk ha) (mul_nonneg hk hb) = k * agm a b ha hb := by
  simpa [agm, NNReal.coe_mul, Subtype.ext_iff, mul_comm k] using
    NNReal.agm_mul_distrib (k := ⟨k, hk⟩) (x := ⟨a, ha⟩) (y := ⟨b, hb⟩)

/-- Strict AM-GM inequality: if `a ≠ b`, then `√(ab) < agm a b ha hb < (a + b) / 2`. -/
theorem lt_of_ne (a b : ℝ) (ha : 0 < a) (hb : 0 < b) (hne : a ≠ b) :
    Real.sqrt (a * b) < agm a b ha.le hb.le := by
  have h := NNReal.min_lt_agm_of_pos_of_ne ha hb hne
  simpa [agm] using h

end agm

/-! ## Examples -/

/-- Example: The AGM of 1 and 4 lies between 1 and 4, and is approximately 2. -/
example : agm 1 4 (by norm_num) (by norm_num) = agm 4 1 (by norm_num) (by norm_num) :=
  agm.comm 1 4 (by norm_num) (by norm_num)

/-- The AGM of a number with itself equals that number. -/
example : agm 3 3 (by norm_num) (by norm_num) = 3 :=
  agm.self 3 (by norm_num)

/-- The AGM is commutative. -/
example : agm 2 8 (by norm_num) (by norm_num) = agm 8 2 (by norm_num) (by norm_num) :=
  agm.comm 2 8 (by norm_num) (by norm_num)

/-- The AGM of 1 and 9 is at most 9. -/
example : agm 1 9 (by norm_num) (by norm_num) ≤ 9 := by
  calc
    agm 1 9 (by norm_num) (by norm_num) ≤ max 1 9 := agm.le_max 1 9 (by norm_num) (by norm_num)
    _ = 9 := by norm_num

/-- The minimum of 1 and 9 is at most the AGM. -/
example : 1 ≤ agm 1 9 (by norm_num) (by norm_num) := by
  calc
    1 = min 1 9 := by norm_num
    _ ≤ agm 1 9 (by norm_num) (by norm_num) := agm.min_le 1 9 (by norm_num) (by norm_num)

/-- Distributivity: AGM of (k·a, k·b) equals k · AGM(a, b). -/
example : agm (2 * 1) (2 * 4) (by norm_num) (by norm_num) = 2 * agm 1 4 (by norm_num) (by norm_num) :=
  agm.mul_distrib 2 1 4 (by norm_num) (by norm_num) (by norm_num)

/-- Zero case: AGM(0, b) = 0. -/
example : agm 0 5 (by norm_num) (by norm_num) = 0 :=
  agm.zero_left 5 (by norm_num)
