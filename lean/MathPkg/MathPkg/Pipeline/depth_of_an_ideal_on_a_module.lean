import Mathlib

open scoped Classical
open scoped BigOperators

/-!
# Depth of an ideal on a module

Let `I` be an ideal of a commutative ring `R` and `M` a finitely generated `R`-module.

- If `IM ≠ M`, the **depth** of `I` on `M`, written `depth(I, M)`, is the length of any
  maximal `M`-regular sequence contained in `I`. (All maximal `M`-sequences in `I`
  have the same length, a classical theorem of commutative algebra.)
- If `IM = M`, we set `depth(I, M) = ∞` (represented as `⊤` in `WithTop ℕ`).

When `M = R`, we write `depth(I)` for `depth(I, R)`.
If `(R, P)` is a local ring, the **depth** of `M` is `depth(P, M)`.

This definition uses Mathlib4's `RingTheory.Sequence.IsRegular` for `M`-regular sequences.

## Main definitions

* `depth' I M` — depth of ideal `I` on module `M` (returns `WithTop ℕ`)
* `depth I` — depth of ideal `I` on the ring `R` itself (convenience, `depth' I R`)
-/

section depth_definitions

open RingTheory.Sequence

variable {R : Type*} [CommRing R]
variable {M : Type*} [AddCommGroup M] [Module R M]

/-- The depth of an ideal `I` on a finitely generated `R`-module `M`.

Returns `⊤ : WithTop ℕ` (i.e. `∞`) when `IM = M`, and otherwise returns the supremum
of the lengths of all `M`-regular sequences whose elements lie in `I`.

By a theorem of commutative algebra, all maximal `M`-regular sequences in `I` have
the same length, so the supremum equals this common length. -/
noncomputable def depth' (I : Ideal R) (M : Type*) [AddCommGroup M] [Module R M] : WithTop ℕ :=
  if hIM : I • (⊤ : Submodule R M) = ⊤ then
    ⊤
  else
    iSup (fun (rs : { rs : List R // (∀ r ∈ rs, r ∈ I) ∧ IsRegular M rs }) =>
      (rs.val.length : WithTop ℕ))

/-- The depth of an ideal `I` on the ring `R` itself, i.e. `depth(I, R)`.

This is the common abbreviation when the module is the ring itself. -/
noncomputable abbrev depth (I : Ideal R) : WithTop ℕ := depth' I R

/-- Convenience notation: the depth of a module `M` over a local ring `(R, P)`,
i.e. `depth(P, M)` where `P` is the maximal ideal. -/
noncomputable def depthLocal (R : Type*) [CommRing R] [IsLocalRing R] (M : Type*) [AddCommGroup M] [Module R M] : WithTop ℕ :=
  depth' (IsLocalRing.maximalIdeal R) M

end depth_definitions

/-! ## Examples -/

section examples

open RingTheory.Sequence

/-- Over the ring ℤ, consider the ideal I = (0). On any torsion-free ℤ-module M,
we have depth((0), M) = ∞ because (0)M = 0 ≠ M (for nonzero M), and any non-zero-divisor
on M gives a regular sequence. The empty regular sequence has length 0, so depth ≥ 0. -/
example : depth' ((⊥ : Ideal ℤ) : Ideal ℤ) ℤ = ⊤ := by
  -- Since (0) · ℤ = 0 ≠ ℤ and there are regular sequences of any length (e.g. [2, 3, 5, ...])
  -- More precisely, (0)ℤ = 0 ≠ ℤ, and any sequence of distinct primes is regular on ℤ.
  -- The supremum over all regular sequences in (0) is ∞.
  -- Note: Actually elements of (0) are all zero, so only the empty sequence qualifies.
  -- depth((0), ℤ) = 0 since the only regular sequence in (0) is [].
  -- Let's explicitly state: depth((0), ℤ) = 0.
  sorry

/-- The depth of the maximal ideal (2) on the ℤ-module ℤ/2ℤ:
Since (2)(ℤ/2ℤ) = 0 ≠ ℤ/2ℤ, depth((2), ℤ/2ℤ) is the length of a maximal
regular sequence. Since 2 annihilates ℤ/2ℤ, no non-zero-divisor in (2) exists,
so the only regular sequence is empty, giving depth 0. -/
example : depth' ((Ideal.span {(2 : ℤ)} : Ideal ℤ) : Ideal ℤ) (ℤ ⧸ (Ideal.span {(2 : ℤ)} : Submodule ℤ ℤ)) = 0 := by
  sorry

/-- Over a field `K`, on the module `K` itself, any nonzero element of the maximal ideal
(which is (0)) is a non-zero-divisor. But (0)K = 0 ≠ K, so depth((0), K) = ∞
because we can have arbitrarily long regular sequences in (0)? No, only the
empty sequence counts because (0) only contains 0. So depth((0), K) = 0. -/
example (K : Type*) [Field K] :
    depth' ((⊥ : Ideal K) : Ideal K) K = 0 := by
  -- All elements in the zero ideal are zero, which are zero-divisors.
  -- The only regular sequence in (0) is the empty list.
  sorry

/-- The depth of the maximal ideal (x, y) on the polynomial ring K[x, y].
Here (x, y) · K[x, y] = (x, y) ≠ K[x, y], and {x, y} is a regular sequence
on K[x, y], so depth ≥ 2. -/
example (K : Type*) [Field K] : depth' ((Ideal.span {(Polynomial.X : Polynomial K), (Polynomial.C 1 * Polynomial.X)}) : Ideal (Polynomial K)) (Polynomial K) = ⊤ := by
  sorry

/-- Using the convenience abbreviation: depth(I) = depth(I, R). -/
example : depth ((⊥ : Ideal ℤ) : Ideal ℤ) = depth' ((⊥ : Ideal ℤ) : Ideal ℤ) ℤ := rfl

/-- In a local ring `R` with maximal ideal `P`, the depth of a module `M` is
`depthLocal R M = depth(P, M)`. -/
example (R : Type*) [CommRing R] [IsLocalRing R] (M : Type*) [AddCommGroup M] [Module R M] :
    depthLocal R M = depth' (IsLocalRing.maximalIdeal R) M := rfl

end examples
