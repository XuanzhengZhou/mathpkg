import Mathlib

open scoped LSeries.notation

/-!
# Dirichlet L-Function (Dirichlet L-Series)

Given a Dirichlet character `χ` modulo `N` (with `χ : DirichletCharacter ℂ N`)
and a complex variable `s` with `re s > 1`, the **Dirichlet L-function** is defined as

$$L(s, χ) = \sum_{n=1}^\infty \frac{\chi(n)}{n^s} = \prod_{p \text{ prime}} \left(1 - \frac{\chi(p)}{p^s}\right)^{-1}.$$

This is the **Dirichlet series** (or **L-series**) associated to the Dirichlet character `χ`.

Mathlib4 provides this via `LSeries` (with notation `L` scoped to `LSeries.notation`),
and the coercion `↗χ` which interprets a Dirichlet character as a function `ℕ → ℂ`.
Thus `L ↗χ s` denotes the Dirichlet L-function of `χ` at `s`.

## Mathlib4 Definition

The L-series `L f s` of a sequence `f : ℕ → ℂ` is defined in
`Mathlib/NumberTheory/LSeries/Basic.lean` as the sum over `LSeries.term f s n`
(where `term f s n = f n / n ^ s` for `n > 0` and `0` for `n = 0`),
converging absolutely when the series is summable.

## Key References

* `Mathlib/NumberTheory/LSeries/Basic.lean` — general L-series definitions and notation `L`, `↗`
* `Mathlib/NumberTheory/LSeries/Dirichlet.lean` — Dirichlet L-series properties
* `Mathlib/NumberTheory/EulerProduct/DirichletLSeries.lean` — Euler product formula for Dirichlet L-series
-/

section dirichlet_l_function

open Complex

/-! ### The Dirichlet L-function via the LSeries notation -/

/--
The Dirichlet L-function `L(s, χ)` for a Dirichlet character `χ` modulo `N` and `s ∈ ℂ` with
`re s > 1`.

The notation `L ↗χ s` is what Mathlib4 uses for the Dirichlet L-series:
`L` is `LSeries` (sum over `LSeries.term`), and `↗χ` coerces `χ : DirichletCharacter ℂ N` to
`ℕ → ℂ` via `fun n : ℕ ↦ (χ n : ℂ)`.

For `re s > 1`, this series converges absolutely and satisfies the Euler product:
$$L(s, χ) = \prod_{p \text{ prime}} \left(1 - \frac{\chi(p)}{p^s}\right)^{-1}.$$
-/
example {N : ℕ} (χ : DirichletCharacter ℂ N) (s : ℂ) : ℂ := by
  sorry
