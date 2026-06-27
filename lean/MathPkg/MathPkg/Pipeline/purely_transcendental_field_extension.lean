import Mathlib

/-! # Purely Transcendental Field Extension

A field extension `K/F` is purely transcendental if `K` is isomorphic (as an
`F`-algebra) to a field of rational functions over `F` in some number of
variables (equivalently: `K` is generated as a field over `F` by an
algebraically independent set).
-/

open IntermediateField

/-- `IsPurelyTranscendental F K` means that `K` is a purely transcendental extension
of `F`, i.e. there exists an algebraically independent family over `F` whose
images generate `K` as a field extension. -/
def IsPurelyTranscendental (F K : Type*) [Field F] [Field K] [Algebra F K] : Prop :=
  ∃ (ι : Type*) (t : ι → K),
    AlgebraicIndependent F t ∧ adjoin F (Set.range t) = ⊤
