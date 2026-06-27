import Mathlib

/-!
# Fundamental Discriminant

An integer `D` is called a **fundamental discriminant** if `D` is the discriminant
of a quadratic field `ℚ(√D)`. Equivalently, `D ≠ 1` and either:

1. `D ≡ 1 mod 4` and `D` is squarefree; or
2. `D ≡ 0 mod 4`, `D/4` is squarefree, and `D/4 ≡ 2 or 3 mod 4`.

These conditions ensure that the quadratic field `ℚ(√D)` has its ring of integers
exactly `ℤ[(D+√D)/2]` when `D ≡ 1 mod 4`, and `ℤ[√D]` when `D ≡ 0 mod 4`.

## Examples

- `-4`, `-3`, `5`, `8`, `12` are fundamental discriminants.
- `1`, `-1`, `4`, `9`, `20` are NOT fundamental discriminants.

## References

- Cohen, *A Course in Computational Algebraic Number Theory*, Section 5.2
- Borevich–Shafarevich, *Number Theory*, Chapter 2
-/

/--
An integer `D` is a **fundamental discriminant** if `D ≠ 1` and either:
- `D ≡ 1 (mod 4)` and `D` is squarefree, or
- `D ≡ 0 (mod 4)`, `D/4` is squarefree, and `D/4 ≡ 2 or 3 (mod 4)`.

This characterizes discriminants of quadratic fields.
-/
def isFundamentalDiscriminant (D : ℤ) : Prop :=
  D ≠ 1 ∧ (
    (D % 4 = 1 ∧ Squarefree D) ∨
    (D % 4 = 0 ∧ Squarefree (D / 4) ∧ ((D / 4) % 4 = 2 ∨ (D / 4) % 4 = 3))
  )

-- Example: Using `isFundamentalDiscriminant` as a hypothesis
example (D : ℤ) (h : isFundamentalDiscriminant D) : D ≠ 1 :=
  h.1

-- Example: `D ≡ 1 mod 4` case — extract squarefree condition
example (D : ℤ) (h : isFundamentalDiscriminant D) (hmod : D % 4 = 1) : Squarefree D := by
  rcases h with ⟨_, h_or⟩
  rcases h_or with (⟨hmod1, hsqfree⟩ | ⟨hmod0, _, _⟩)
  · -- hmod1: D % 4 = 1 — matches hmod
    exact hsqfree
  · -- hmod0: D % 4 = 0 — contradicts hmod
    rw [hmod0] at hmod
    norm_num at hmod

-- Example: `D ≡ 0 mod 4` case — extract D/4 squarefree and its residue mod 4
example (D : ℤ) (h : isFundamentalDiscriminant D) (hmod : D % 4 = 0) :
    Squarefree (D / 4) ∧ ((D / 4) % 4 = 2 ∨ (D / 4) % 4 = 3) := by
  rcases h with ⟨_, h_or⟩
  rcases h_or with (⟨hmod1, _⟩ | ⟨hmod0, hsq, hres⟩)
  · -- hmod1: D % 4 = 1 — contradicts hmod
    rw [hmod1] at hmod
    norm_num at hmod
  · -- hmod0: D % 4 = 0 — matches
    exact ⟨hsq, hres⟩

-- Example: `1` is NOT a fundamental discriminant
example : ¬ isFundamentalDiscriminant (1 : ℤ) := by
  simp [isFundamentalDiscriminant]

-- Example: If `D` is a fundamental discriminant, then `D` can be used to construct
-- the quadratic field `ℚ(√D)` and study its ring of integers.
example (D : ℤ) (h : isFundamentalDiscriminant D) : True := by
  have hne_one : D ≠ 1 := h.1
  trivial
