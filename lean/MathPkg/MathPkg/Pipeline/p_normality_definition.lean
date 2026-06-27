import Mathlib

open scoped Classical
open scoped Pointwise

/-!
# p-Normality

If P is a Sylow p-subgroup of G and if the center of P is weakly closed in P,
then G is said to be p-normal.

Among p-normal groups are groups with abelian Sylow p-subgroups and groups in which
distinct Sylow p-subgroups have trivial intersection.

## Main definitions

* `WeaklyClosed` : A subgroup H of G is weakly closed in a containing subgroup P with respect to G.
  This means: for all g ∈ G, if `gHg⁻¹ ≤ P` then `gHg⁻¹ = H`.
* `IsPNormal` : G is p-normal if there exists a Sylow p-subgroup P such that
  the center of P is weakly closed in P with respect to G.

## References

* Grün, O. "Beiträge zur Gruppentheorie. I." Journal für die reine und angewandte Mathematik
  174 (1936): 1-14.
-/

section p_normality

open Subgroup

variable (G : Type*) [Group G] (p : ℕ)

/-- A subgroup `H` of G is **weakly closed** in a containing subgroup `P` with respect to G
if `H ≤ P`, and for every `g : G`, `gHg⁻¹ ≤ P` implies `gHg⁻¹ = H`. -/
def WeaklyClosed (H P : Subgroup G) : Prop :=
  H ≤ P ∧ ∀ g : G, Subgroup.map (MulAut.conj g : G →* G) H ≤ P →
    Subgroup.map (MulAut.conj g : G →* G) H = H

/-- The center of a Sylow p-subgroup `P`, viewed as a subgroup of `G`.

We take the center of `P` as a group (i.e. `Subgroup.center (P : Subgroup G)`)
and then map it into `G` via the inclusion `P.subtype`. -/
def sylowCenter (P : Sylow p G) : Subgroup G :=
  (Subgroup.center (P : Subgroup G)).map (P : Subgroup G).subtype

/-- The center of a Sylow p-subgroup (viewed as a subgroup of G) is contained in the Sylow
subgroup. -/
theorem sylowCenter_le (P : Sylow p G) : sylowCenter G p P ≤ (P : Subgroup G) := by
  intro x hx
  obtain ⟨y, hy, rfl⟩ := Subgroup.mem_map.mp hx
  exact y.2

/-- `G` is **p-normal** if there exists a Sylow p-subgroup `P` of `G` such that
the center of `P` is weakly closed in `P` with respect to `G`. -/
def IsPNormal [Fact p.Prime] : Prop :=
  ∃ P : Sylow p G, WeaklyClosed G (sylowCenter G p P) (P : Subgroup G)

end p_normality
