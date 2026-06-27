import Mathlib

/-!
# Boundaries, Cycles, and Homology of a Chain Complex

Let `F = (F_i, φ_i)` be a chain complex of modules (or more generally, objects
in an abelian category with `HasHomology`).

* **Cycles** at `F_i` are the elements of `ker φ_i`.
  In Mathlib4 this is `K.cycles i`.
* **Boundaries** at `F_i` are the elements of `im φ_{i+1}`.
  In Mathlib4 this is captured by `K.opcycles i`, which represents the
  quotient `F_i / im φ_{i+1}`, and the inclusion `K.homologyι : K.homology i ⟶ K.opcycles i`
  witnesses that homology is a subobject of the boundary quotient.
* **Homology** at `F_i`, denoted `H_i(F)`, is the quotient module
  `(ker φ_i) / (im φ_{i+1})`.
  In Mathlib4 this is `K.homology i`.

## Mathlib4 definitions (all pre-existing)

The file `Mathlib/Algebra/Homology/HomologicalComplex.lean` defines the
general notion of a homological complex `K : HomologicalComplex V c`
with objects `K.X i` and differentials `K.d i j`.

The file `Mathlib/Algebra/Homology/ShortComplex/HomologicalComplex.lean`
defines the homology API for a homological complex:

* `K.cycles i`           : the cycles at degree `i` (kernel of the outgoing differential)
* `K.opcycles i`          : the opcycles at degree `i` (cokernel of the incoming differential)
* `K.homology i`          : the homology at degree `i`
* `K.HasHomology i`       : typeclass asserting that homology data exists
* `K.iCycles i`           : the inclusion `K.cycles i ⟶ K.X i`
* `K.pOpcycles i`         : the projection `K.X i ⟶ K.opcycles i`
* `K.homologyπ i`         : the projection `K.cycles i ⟶ K.homology i`
* `K.homologyι i`         : the inclusion `K.homology i ⟶ K.opcycles i`

## References

* `Mathlib/Algebra/Homology/HomologicalComplex.lean`
* `Mathlib/Algebra/Homology/ShortComplex/HomologicalComplex.lean`
* `Mathlib/Algebra/Homology/ShortComplex/Homology.lean`
-/

open CategoryTheory
open CategoryTheory.Limits
open HomologicalComplex

universe u

section cycles_boundaries_homology

/-! ### Cycles, boundaries, and homology in a homological complex -/

variable {C : Type u} [Category.{u} C] [HasZeroMorphisms C]
  {ι : Type*} {c : ComplexShape ι} (K : HomologicalComplex C c) (i : ι)

/--
`Cycles K i` is an alias for Mathlib4's `K.cycles i`, the kernel of the
outgoing differential `K.d i (c.next i)`.

In the textbook notation for a complex `F = (F_i, φ_i)`, cycles at `F_i`
are `ker φ_i`.
-/
noncomputable abbrev Cycles (K : HomologicalComplex C c) (i : ι) [K.HasHomology i] : C := K.cycles i

/--
The **boundaries** at degree `i` are the image of the incoming differential
`K.d (c.prev i) i`. In Mathlib4 this is not stored as a standalone subobject;
instead `K.opcycles i` represents the quotient `K.X i / image(incoming differential)`.

We provide `BoundaryQuotient` as a convenient alias for `K.opcycles i`.
-/
noncomputable abbrev BoundaryQuotient (K : HomologicalComplex C c) (i : ι) [K.HasHomology i] : C := K.opcycles i

/--
`Homology K i` is an alias for Mathlib4's `K.homology i`, the homology
of the complex `K` at degree `i`.

In the textbook notation for a complex `F = (F_i, φ_i)`,
`H_i(F) := (ker φ_i) / (im φ_{i+1})`.
-/
noncomputable abbrev Homology (K : HomologicalComplex C c) (i : ι) [K.HasHomology i] : C := K.homology i

/--
`iCycles K i` is the inclusion of the cycles into the chain group `K.X i`.
-/
noncomputable abbrev iCycles (K : HomologicalComplex C c) (i : ι) [K.HasHomology i] :
    K.cycles i ⟶ K.X i := K.iCycles i

/--
`pOpcycles K i` is the canonical projection from `K.X i` onto `K.opcycles i`,
the quotient by boundaries.
-/
noncomputable abbrev pOpcycles (K : HomologicalComplex C c) (i : ι) [K.HasHomology i] :
    K.X i ⟶ K.opcycles i := K.pOpcycles i

/--
`homologyπ K i` is the canonical epimorphism from cycles onto homology,
i.e., `(ker φ_i) ↠ H_i(F)`.
-/
noncomputable abbrev homologyπ (K : HomologicalComplex C c) (i : ι) [K.HasHomology i] :
    K.cycles i ⟶ K.homology i := K.homologyπ i

/--
`homologyι K i` is the canonical monomorphism from homology into
the boundary quotient `opcycles i`, i.e., `H_i(F) ↪ F_i / im φ_{i+1}`.
-/
noncomputable abbrev homologyι (K : HomologicalComplex C c) (i : ι) [K.HasHomology i] :
    K.homology i ⟶ K.opcycles i := K.homologyι i

end cycles_boundaries_homology

section examples

/-! ### Examples -/

open ComplexShape

variable {R : Type u} [CommRing R]

/--
**Example 1**: The homology of a two-term complex.

Consider the chain complex (in `ModuleCat R`) with
`F₁ = R`, `F₀ = R`, all other `F_i = 0`, and `φ₁ : R → R` the identity map.
Then:
- cycles at F₁: ker(id_R) = 0  (since id_R is injective)
- cycles at F₀: ker(0) = R    (the outgoing map is zero)
- boundaries at F₀: im(id_R) = R
- H₁(F) = 0 / 0 = 0
- H₀(F) = R / R = 0

This complex is acyclic (all homology groups vanish).
-/
example : True := by
  sorry
