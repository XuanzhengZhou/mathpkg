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
noncomputable def depth' (I : Ideal R) (M : Type*) [AddCommGroup M] [Module R M] : WithTop ℕ := by
  sorry
