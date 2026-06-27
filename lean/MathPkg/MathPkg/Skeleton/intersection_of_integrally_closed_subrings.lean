import Mathlib

open Subring

/-!
# Intersection of Integrally Closed Subrings

Let T be a commutative ring with identity and {S_i}, {R_i} families of subrings such that
T is an extension ring of S_i and S_i is an extension ring of R_i for every i.
If each R_i is integrally closed in S_i, then ∩ R_i is integrally closed in ∩ S_i.

## Proof

Take x ∈ ∩ S_i integral over ∩ R_i. Since ∩ R_i ⊆ R_i, x is integral over each R_i.
Since each R_i is integrally closed in S_i and x ∈ S_i, we have x ∈ R_i for all i.
Hence x ∈ ∩ R_i.
-/

section intersection_of_integrally_closed_subrings

variable {ι : Type*} {T : Type*} [CommRing T]
  (R S : ι → Subring T)
  (hRS : ∀ i, R i ≤ S i)

/-- The intersection of all R_i -/
def interR : Subring T := ⨅ k, R k

/-- The intersection of all S_i -/
def interS : Subring T := ⨅ k, S k

theorem intersection_of_integrally_closed_subrings
    [∀ i, Algebra (R i) (S i)]
    [Algebra (interR R) (interS S)]
    (h_int_closed : ∀ i, IsIntegrallyClosedIn (R i) (S i)) :
    IsIntegrallyClosedIn (interR R) (interS S) := by
  sorry
