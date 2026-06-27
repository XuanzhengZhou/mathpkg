import Mathlib

/-!
# Conjugacy Classes and Centralizers

The conjugation action `g ↦ (x ↦ g⁻¹xg)` partitions a group `G` into orbits called
**conjugacy classes**. The stabilizer of `x` under this action is the **centralizer**
`C_G(x) = {g ∈ G | gx = xg}`. By the orbit-stabilizer theorem, the size of the
conjugacy class of `x` equals the index `|G : C_G(x)|`.

## Mathlib4 Locations

* `ConjClasses G` — the quotient type of conjugacy classes (`Algebra/Group/Conj.lean`)
* `IsConj a b` — the conjugacy relation
* `ConjAct G` — conjugation action of `G` on itself (`GroupTheory/GroupAction/ConjAct.lean`)
* `Subgroup.centralizer s` — centralizer of a subset (`GroupTheory/Subgroup/Centralizer.lean`)
* `Set.centralizer s` — centralizer as a set (`Algebra/Group/Center.lean`)
* `MulAction.orbit` / `MulAction.stabilizer` — orbit and stabilizer of a group action
* `MulAction.card_orbit_mul_card_stabilizer_eq_card_group` — orbit-stabilizer theorem for finite groups
-/

open scoped BigOperators

/--
The **conjugacy class** of an element `g : G` is the set of all elements conjugate to `g`:
`{h * g * h⁻¹ | h ∈ G}`.

In Mathlib4 this is expressed as either `ConjClasses.mk g` (as a quotient type) or
as `orbit (ConjAct G) g` (as a set via the conjugation action).
-/
def conjugacyClass (G : Type*) [Group G] (g : G) : ConjClasses G :=
  ConjClasses.mk g

/--
An element `h` is **conjugate** to `g` if there exists `k : G` such that `k * g * k⁻¹ = h`.

Mathlib4 uses `IsConj g h` for this relation (defined in `Algebra/Group/Conj.lean`).
-/
def isConjugate (G : Type*) [Group G] (g h : G) : Prop :=
  IsConj g h

/--
The **centralizer** of an element `g` in a group `G` is the subgroup of elements
that commute with `g`:
`C_G(g) = {h ∈ G | h * g = g * h}`.

Mathlib4 defines this as `Subgroup.centralizer {g}`.
-/
def centralizerOf (G : Type*) [Group G] (g : G) : Subgroup G :=
  Subgroup.centralizer {g}

/--
The **centralizer** of a subset `S ⊆ G` is the subgroup of elements commuting with
every element of `S`:
`C_G(S) = {h ∈ G | ∀ s ∈ S, h * s = s * h}`.

This is `Subgroup.centralizer S` in Mathlib4.
-/
abbrev centralizerSubset (G : Type*) [Group G] (S : Set G) : Subgroup G :=
  Subgroup.centralizer S

/--
The conjugation action of `G` on itself: `g • x = g * x * g⁻¹`.

Mathlib4 provides `ConjAct G`, a type alias for `G`, with a `MulDistribMulAction`
on `G` by conjugation. The orbit of `x` under this action is the conjugacy class of `x`,
and the stabilizer is the centralizer `C_G(x)`.
-/
def conjActionOrbit (G : Type*) [Group G] (g : G) : Set G :=
  orbit (ConjAct G) g

/--
An **example** showing the conjugacy class of the identity element `1` in any group:
the identity is only conjugate to itself, so its conjugacy class is `{1}`.
-/
example (G : Type*) [Group G] : ConjClasses.mk (1 : G) = ConjClasses.mk (1 : G) := rfl

/--
An **example** in `ZMod 7` (an abelian group): every conjugacy class is a singleton,
since `g + h - g = h` in additive notation.
-/
example (x y : Additive (ZMod 7)) : IsConj x y ↔ x = y := by
  simp

/--
An **example** showing that in the symmetric group `S₃`, the 3-cycles `(1 2 3)` and
`(1 3 2)` are conjugate.
-/
example : IsConj
    (Equiv.swap 0 1 * Equiv.swap 1 2 : Equiv.Perm (Fin 3))
    (Equiv.swap 0 1 * Equiv.swap 0 2 : Equiv.Perm (Fin 3)) := by
  -- (1 3)(1 2 3)(1 3) = (1 3 2), so they are conjugate by the transposition (1 3)
  refine ⟨Equiv.swap 0 2, ?_⟩
  ext i
  fin_cases i <;> decide

/--
An **example** of the centralizer: in an abelian group `G`, the centralizer of any
element is the whole group.
-/
example (G : Type*) [CommGroup G] (g : G) : centralizerOf G g = ⊤ := by
  dsimp [centralizerOf]
  rw [Subgroup.centralizer_eq_top_iff_subset]
  intro x hx
  simp at hx
  subst hx
  exact CommGroup.mem_center_commGroup g

/--
An **example** illustrating the orbit-stabilizer size formula: for a finite group `G`
and an element `g : G`, the product of the size of the conjugacy class and the size
of the centralizer equals the order of the group.
This is a direct consequence of `MulAction.card_orbit_mul_card_stabilizer_eq_card_group`.
-/
example (G : Type*) [Group G] [Fintype G] (g : G) :
    Fintype.card (orbit (ConjAct G) g) * Fintype.card (MulAction.stabilizer (ConjAct G) g) =
    Fintype.card G := by
  rw [MulAction.card_orbit_mul_card_stabilizer_eq_card_group (ConjAct G) g]

/--
An **example** showing the stabilizer under conjugation equals the centralizer
(as a subgroup of `G`, composed with `toConjAct`).
-/
example (G : Type*) [Group G] (g : G) :
    MulAction.stabilizer (ConjAct G) g = (Subgroup.centralizer {g}).comap ConjAct.toConjAct.toMonoidHom := by
  ext k
  simp [ConjAct.stabilizer_eq_centralizer g]

/--
An **example** in the dihedral group `D₄` (order 8). The rotation `r` has a
non-trivial centralizer (containing at least all rotations `{1, r, r², r³}`),
while a reflection `s` has a smaller centralizer.
-/
example : Fintype.card (Subgroup.centralizer {(DihedralGroup.r 1 : DihedralGroup 4)} : Set (DihedralGroup 4)) = 4 := by
  native_decide

/--
An **example**: the size formula for the conjugacy class of a specific element.
In `S₃`, the conjugacy class of a 2-cycle has size 3, the centralizer has size 2,
and the group order is 6 = 3 * 2.
-/
example : Fintype.card (orbit (ConjAct (Equiv.Perm (Fin 3))) (Equiv.swap 0 1 : Equiv.Perm (Fin 3))) = 3 := by
  native_decide
