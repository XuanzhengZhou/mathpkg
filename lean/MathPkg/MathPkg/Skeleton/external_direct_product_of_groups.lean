import Mathlib

/-!
# External Direct Product of Groups

The **external direct product** (also called the *restricted direct product* or *weak direct
product*) of a family of groups `(G_λ)_{λ∈Λ}` is the subset of the full cartesian product
`Π_λ G_λ` consisting of all `(g_λ)` such that `g_λ = 1_λ` for almost all `λ` (i.e., all but
finitely many).

When the index set `Λ` is finite, the external direct product coincides with the full cartesian
product, denoted `G_{λ₁} × ··· × G_{λ_n}`.

## Mathlib4 References
- `Pi.group` in `Algebra/Group/Pi/Basic.lean` — the group instance on the full cartesian product
- `Subgroup` in `Algebra/Group/Subgroup/Defs.lean` — subgroup construction
- `Set.Finite` in `Data/Set/Finite/Basic.lean` — finiteness of sets
- `Pi.mulSingle` in `Algebra/Group/Pi/Lemmas.lean` — element supported at a single index
-/

open Set

universe u v

variable {ι : Type u} {G : ι → Type v} [∀ i, Group (G i)]

/-- The external direct product (restricted direct product) of a family of groups.

For a family of groups `G i` indexed by `ι`, the external direct product `ExternalDirectProduct G`
consists of all functions `f : Π i, G i` such that `f i = 1` for all but finitely many `i`.
This is a subgroup of the full cartesian product `Π i, G i`.

When `ι` is finite, this coincides with the full product (see `ExternalDirectProduct.eq_top`).

**Notation**: In the literature, this is often written as `Dr_{λ∈Λ} G_λ` or `∏ᵈ G_λ`. -/
def ExternalDirectProduct (G : ι → Type v) [∀ i, Group (G i)] : Subgroup (∀ i, G i) := by
  sorry
