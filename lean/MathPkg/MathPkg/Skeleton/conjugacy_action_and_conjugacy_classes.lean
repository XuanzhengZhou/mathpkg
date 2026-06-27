import Mathlib

open scoped Classical

/-!
# Conjugacy Action and Conjugacy Classes

Let `G` be a group. The **conjugacy action** (action by inner automorphisms) of `G` on
itself is given by `g · x = g * x * g⁻¹` for all `g, x ∈ G`. The orbits under this
action are called **conjugacy classes**; two elements `a, b ∈ G` are **conjugate**
(denoted `a ∼ b`) if there exists `g ∈ G` such that `g * a * g⁻¹ = b`, i.e., if they
lie in the same orbit of the conjugacy action.

## Mathlib4 Locations

- `ConjAct G` — type alias for `G` equipped with the conjugation action (`GroupTheory/GroupAction/ConjAct.lean`)
- `IsConj a b` — the conjugacy relation (`Algebra/Group/Conj.lean`)
- `ConjClasses G` — the quotient type of conjugacy classes (`Algebra/Group/Conj.lean`)
- `MulAction.orbit (ConjAct G) g` — the conjugacy class of `g` as a set
- `mem_orbit_conjAct` — theorem: `g ∈ orbit (ConjAct G) h ↔ IsConj g h`
- `orbitRel_conjAct` — theorem: the orbit relation of `ConjAct G` equals `IsConj`

## Dependencies

- [Group](/concept/group) — underlying group structure
- [Inner automorphism](/concept/inner_automorphism) — conjugation by a fixed element
- [Group action definition](/concept/group_action) — the notion of a group action
-/

section conjugacy_action_and_conjugacy_classes

variable (G : Type*) [Group G]

/--
The **conjugation action** of a group `G` on itself, defined by `g · x = g * x * g⁻¹`.

In Mathlib4 this is realized via `ConjAct G`, a type alias for `G` equipped with
`MulDistribMulAction (ConjAct G) G`. The action formula is:
```lean
ConjAct.smul_def (g : ConjAct G) (h : G) : g • h = ConjAct.ofConjAct g * h * (ConjAct.ofConjAct g)⁻¹
```

Equivalently, using `toConjAct` to convert from `G`:
```lean
ConjAct.toConjAct_smul (g h : G) : ConjAct.toConjAct g • h = g * h * g⁻¹
```
-/
abbrev conjugationAction (G : Type*) [Group G] : SMul (ConjAct G) G := by
  sorry
