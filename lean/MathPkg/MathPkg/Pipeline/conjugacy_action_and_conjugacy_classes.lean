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
abbrev conjugationAction (G : Type*) [Group G] : SMul (ConjAct G) G :=
  inferInstance

/--
The **conjugacy relation**: `a` is conjugate to `b` if there exists `g : G` such that
`g * a * g⁻¹ = b`.

In Mathlib4 this is `IsConj a b` (defined in `Algebra/Group/Conj.lean`).
-/
abbrev isConjugate (G : Type*) [Group G] (a b : G) : Prop :=
  IsConj a b

/--
A **conjugacy class** is the set of all elements conjugate to a given `g : G`:
`{h * g * h⁻¹ | h ∈ G}`.

Mathlib4 provides two representations:
1. `ConjClasses.mk g` — the conjugacy class as a quotient type `ConjClasses G`
2. `MulAction.orbit (ConjAct G) g` — the conjugacy class as a set
-/
abbrev conjugacyClass (G : Type*) [Group G] (g : G) : ConjClasses G :=
  ConjClasses.mk g

end conjugacy_action_and_conjugacy_classes

section examples

variable (G : Type*) [Group G]

/--
**Example**: The conjugacy class of the identity `1 : G` is the singleton `{1}`,
since `g * 1 * g⁻¹ = 1` for all `g`.
-/
example : ConjClasses.mk (1 : G) = ConjClasses.mk (1 : G) := rfl

/--
**Example**: The identity element is only conjugate to itself.
-/
example (g : G) : IsConj g (1 : G) ↔ g = 1 := by
  simp

/--
**Example**: The conjugacy orbit as a set. The orbit of `x` under the conjugation
action `ConjAct G` is precisely the conjugacy class of `x` (as a subset of `G`).
-/
example (g : G) : orbit (ConjAct G) g = (ConjClasses.mk g).carrier := by
  exact ConjAct.orbit_eq_carrier_conjClasses g

/--
**Example**: Two elements are conjugate iff they lie in the same orbit
of the conjugation action. This is the fundamental connection between
the conjugacy action and conjugacy classes.
-/
example (g h : G) : g ∈ orbit (ConjAct G) h ↔ IsConj g h := by
  rw [ConjAct.mem_orbit_conjAct]

/--
**Example**: The orbit relation of `ConjAct G` equals the `IsConj` relation,
so the quotient by the conjugation action is exactly `ConjClasses G`.
-/
example (g h : G) : (orbitRel (ConjAct G) G).r g h ↔ IsConj g h := by
  rw [ConjAct.orbitRel_conjAct]

/--
**Example**: In the symmetric group `S₃`, the two 3-cycles `(0 1 2)` and `(0 2 1)`
are conjugate.
-/
example : IsConj
    (Equiv.swap 0 1 * Equiv.swap 1 2 : Equiv.Perm (Fin 3))
    (Equiv.swap 0 2 * Equiv.swap 0 1 : Equiv.Perm (Fin 3)) := by
  refine ⟨Equiv.swap 0 2, ?_⟩
  ext i
  fin_cases i <;> decide

/--
**Example**: In an abelian group, every conjugacy class is a singleton:
`IsConj a b ↔ a = b`.
-/
example (G : Type*) [CommGroup G] (a b : G) : IsConj a b ↔ a = b := by
  simp

/--
**Example**: The conjugacy class of `r` in the dihedral group `D₄` has size 2.
Indeed, `r` is conjugate to `r³` but not to the reflections.
-/
example : Fintype.card
    (orbit (ConjAct (DihedralGroup 4)) (DihedralGroup.r 1 : DihedralGroup 4)) = 2 := by
  native_decide

/--
**Example**: The centralizer of an element `g` equals the stabilizer of `g` under
the conjugation action (up to composing with `toConjAct`).
-/
example (g : G) :
    MulAction.stabilizer (ConjAct G) g =
    (Subgroup.centralizer {g}).comap ConjAct.toConjAct.toMonoidHom := by
  exact ConjAct.stabilizer_eq_centralizer g

/--
**Example**: The conjugacy relation is an equivalence relation: it is reflexive,
symmetric, and transitive. (In Mathlib4 this is encoded by `IsConj.setoid`.)
-/
example : IsConj.refl (1 : G) := IsConj.refl 1
example {a b : G} (h : IsConj a b) : IsConj b a := IsConj.symm h
example {a b c : G} (hab : IsConj a b) (hbc : IsConj b c) : IsConj a c :=
  IsConj.trans hab hbc

end examples
