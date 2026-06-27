import Mathlib

open Function Order Set

/-!
# Direct Limit of a Direct System of Groups

Given a direct system of groups `{G_λ, α_λ^μ}` indexed by a directed preorder `ι`,
we construct the direct limit group `D` as the quotient of the disjoint union
`Σ λ, G_λ` by the equivalence relation:
  `g_λ ∼ g_μ` iff `α_λ^ν(g_λ) = α_μ^ν(g_μ)` for some `ν ≥ λ, μ`.

Multiplication on equivalence classes is defined by:
  `[g_λ][g_μ] = [α_λ^ν(g_λ) α_μ^ν(g_μ)]` for any `ν ≥ λ, μ`.

## Mathlib4 References
- `DirectedSystem` in `Mathlib/Order/DirectedInverseSystem.lean`
- `DirectLimit` := `Quotient (setoid f)` -- the underlying set
- `exists_ge_ge` in `Mathlib/Order/Directed.lean`
-/

/-- A direct system of groups over a directed preorder `ι` consists of:
- a family of groups `G i` for each `i : ι`
- transition homomorphisms `α i j` for `i ≤ j`
- satisfying the directed system axioms (identity and composition). -/
structure DirectSystemOfGroups (ι : Type u) [Preorder ι] where
  /-- The family of groups. -/
  G : ι → Type v
  /-- Each component is a group. -/
  [group : ∀ i, Group (G i)]
  /-- The transition homomorphisms `α_λ^μ : G_λ → G_μ` for `λ ≤ μ`. -/
  α : ∀ {i j : ι}, i ≤ j → G i →* G j
  /-- `α_λ^λ = id` -/
  map_self : ∀ {i} (x : G i), α (le_refl i) x = x
  /-- `α_μ^ν ∘ α_λ^μ = α_λ^ν` for `λ ≤ μ ≤ ν` -/
  map_map : ∀ {i j k} (hij : i ≤ j) (hjk : j ≤ k) (x : G i), α hjk (α hij x) = α (hij.trans hjk) x

namespace DirectSystemOfGroups

variable {ι : Type u} [Preorder ι] [IsDirectedOrder ι] (D : DirectSystemOfGroups ι)

/-- Local instance: each component G i is a group. -/
instance instGroup (i : ι) : Group (D.G i) := D.group i

/-- A helper lemma: `α hjk (α hij x) = α (hij.trans hjk) x`. -/
theorem map_map' {i j k : ι} (hij : i ≤ j) (hjk : j ≤ k) (x : D.G i) :
    D.α hjk (D.α hij x) = D.α (hij.trans hjk) x := by
  sorry
