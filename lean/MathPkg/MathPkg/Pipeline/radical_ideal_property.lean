import Mathlib

open scoped Classical
open scoped BigOperators

/-!
# Radical Ideal Property

For every ideal `I` in a commutative ring `R`, the radical `√I` is an ideal
containing `I`.

In Mathlib4, `I.radical` already has type `Ideal R`, so the fact that `√I` is
an ideal is automatic.  The non‑trivial statement is the containment `I ≤ I.radical`.
-/

section radical_ideal_property

open Ideal

/-- The radical of an ideal is an ideal containing the original ideal:
`I ≤ √I`.  The fact that `√I` is an ideal is guaranteed by the type
`I.radical : Ideal R`. -/
theorem radical_ideal_property {R : Type*} [CommSemiring R] (I : Ideal R) : I ≤ I.radical := by
  sorry

end radical_ideal_property
