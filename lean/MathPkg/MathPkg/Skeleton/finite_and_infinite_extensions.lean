import Mathlib

open scoped Classical

/-!
# Finite and Infinite Field Extensions

For a field extension `K/F`, if the degree `[K : F]` is finite, then `K` is a **finite extension**
of `F`; otherwise `K` is an **infinite extension** of `F`.

Mathlib4 already encodes this via the typeclass `FiniteDimensional F K` (or equivalently
`Module.Finite F K`), which asserts that `K` is finite-dimensional as an `F`-vector space.
The degree `[K : F]` is given by `Module.finrank F K`.

## Main definitions

* `FiniteExtension F K` -- alias for `FiniteDimensional F K`; `K/F` is a finite extension.
* `InfiniteExtension F K` -- alias for `¬ FiniteDimensional F K`; `K/F` is an infinite extension.
* `extensionDegree F K` -- alias for `Module.finrank F K`; the degree `[K : F]`.

In practice, use the Mathlib4 typeclasses directly: `[FiniteDimensional F K]` or
`[Module.Finite F K]`.
-/

section finite_and_infinite_extensions

variable (F K : Type*) [Field F] [Field K] [Algebra F K]

/-! ### Core abbreviations -/

/-- `FiniteExtension F K` means `K` is a finite-dimensional `F`-vector space,
i.e., the field extension `K/F` is **finite**. This is simply an alias for
Mathlib4's `FiniteDimensional F K`. -/
abbrev FiniteExtension (F K : Type*) [Field F] [Field K] [Algebra F K] : Prop := by
  sorry
