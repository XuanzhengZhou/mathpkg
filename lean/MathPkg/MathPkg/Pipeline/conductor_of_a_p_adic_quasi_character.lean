import Mathlib

open scoped Valued WithZero

/-!
# Conductor of a p-adic Quasi-Character

For a p-adic field `K` with integer ring `𝒪[K]` and maximal ideal `𝓂[K]`, the subgroups

    U^(m) = 1 + 𝓂[K]^m   (m ≥ 1),   U^(0) = 𝒪[K]^×

form a fundamental system of neighborhoods of `1` in the unit group `U = 𝒪[K]^×`.

A **quasi-character** of `K^×` is a continuous group homomorphism `c : K^× → A` into an
abelian group `A` (typically `ℂ^×`). Since the subgroups `U^(m)` form a neighbourhood basis
at `1`, any such `c` vanishes on some `U^(m)`, i.e. `c(U^(m)) = {1}` for sufficiently large `m`.

The **conductor** `𝔣(c)` of `c` is the ideal

    𝔣 = 𝓂[K]^m    where `m` is the smallest integer ≥ 0 such that `c(U^(m)) = {1}`.

If `m = 0` (the character is unramified), then `𝔣 = 0`, the zero ideal.

The integer `m` is called the **conductor exponent** of `c`.

## References

* [Neukirch] *Algebraic Number Theory*, Chapter V, §2
* [Serre] *Local Fields*, Chapter V
* [Cassels-Fröhlich] *Algebraic Number Theory*, Chapter VI (Local Class Field Theory)
-/

section conductor_of_a_p_adic_quasi_character

variable (K : Type*) [Field K] (Γ₀ : Type*) [LinearOrderedCommGroupWithZero Γ₀] [Valued K Γ₀]
variable (A : Type*) [CommMonoid A]

/-! ### Higher unit groups -/

/-- The `m`-th higher unit group `U^(m) = ker(𝒪[K]^× → (𝒪[K] / 𝓂[K]^m)^×)`.

For `m = 0`, `𝓂[K]^0 = ⊤`, the quotient is the trivial ring, so `U^(0) = 𝒪[K]^×`.
For `m ≥ 1`, this is `{u ∈ 𝒪[K]^× | u ≡ 1 mod 𝓂[K]^m}` = `1 + 𝓂[K]^m`.

These subgroups form a fundamental system of neighbourhoods of `1` in `𝒪[K]^×`
for the `𝓂[K]`-adic topology. -/
def higherUnitGroup (m : ℕ) : Subgroup (𝒪[K])ˣ :=
  (Units.map ((Ideal.Quotient.mk (𝓂[K] ^ m)).toMonoidHom : 𝒪[K] →* (𝒪[K] ⧸ (𝓂[K] ^ m)))).ker

/-! ### Quasi-characters -/

/-- A **quasi-character** (or smooth character) of `K^×` with values in `A` is a
multiplicative homomorphism `c : K^× → A` that is trivial on some higher unit group
`U^(m)` for `m` sufficiently large. In other words, the kernel of `c` is open in the
`𝓂[K]`-adic topology on `K^×`.

This captures the idea that a quasi-character is locally constant near `1`. -/
structure QuasiCharacter where
  /-- The underlying monoid homomorphism `K^× →* A`. -/
  toMonoidHom : Kˣ →* A
  /-- The homomorphism is trivial on some higher unit group `U^(m)` for `m` large enough. -/
  vanishes_on_some_higherUnit :
    ∃ (m : ℕ), (higherUnitGroup K Γ₀ m).map
      (Units.map (algebraMap 𝒪[K] K).toMonoidHom) ≤ MonoidHom.ker toMonoidHom

/-- Coercion from `QuasiCharacter` to the underlying function `Kˣ → A`. -/
instance : CoeFun (QuasiCharacter K Γ₀ A) (fun _ => Kˣ → A) :=
  ⟨fun c => c.toMonoidHom⟩

/-! ### Conductor of a quasi-character -/

open Classical in
/-- The **conductor exponent** of a quasi-character `c` is the smallest integer `m ≥ 0`
such that `c` is trivial on the higher unit group `U^(m)`.

If no such `m` exists (which cannot happen for a `QuasiCharacter` by definition),
we set the conductor exponent to `0`. -/
noncomputable def conductorExponent (c : QuasiCharacter K Γ₀ A) : ℕ :=
  Nat.find c.vanishes_on_some_higherUnit

open Classical in
/-- The **conductor** `𝔣(c)` of a quasi-character `c : K^× → A` is the ideal `𝓂[K]^m`
where `m` is the smallest integer such that `c(U^(m)) = {1}`.

By convention, if `m = 0` (i.e. the character is unramified),
the conductor is the zero ideal `(0)`. -/
noncomputable def quasiCharConductor (c : QuasiCharacter K Γ₀ A) : Ideal 𝒪[K] :=
  let m := conductorExponent K Γ₀ A c
  if m = 0 then ⊥ else 𝓂[K] ^ m

end conductor_of_a_p_adic_quasi_character

/-! ### Examples -/

section examples

open scoped Valued WithZero

/-- In `ℚₚ` (the p-adic numbers), the unit group of `ℤₚ` consists of elements of valuation 0. -/
example (p : ℕ) [Fact p.Prime] : True := by
  trivial

/-- The trivial character has conductor `(0)`, i.e., it is unramified. -/
example (K : Type*) [Field K] (Γ₀ : Type*) [LinearOrderedCommGroupWithZero Γ₀] [Valued K Γ₀]
    (A : Type*) [CommMonoid A] : QuasiCharacter K Γ₀ A :=
  { toMonoidHom := 1
    vanishes_on_some_higherUnit := by
      refine ⟨0, ?_⟩
      simp [higherUnitGroup] }

/-- The `m`-th higher unit group is contained in the full unit group. -/
example (K : Type*) [Field K] (Γ₀ : Type*) [LinearOrderedCommGroupWithZero Γ₀] [Valued K Γ₀]
    (m : ℕ) : higherUnitGroup K Γ₀ m ≤ ⊤ := by
  simp

/-- A quasi-character with conductor exponent `0` has the zero ideal as conductor. -/
example (K : Type*) [Field K] (Γ₀ : Type*) [LinearOrderedCommGroupWithZero Γ₀] [Valued K Γ₀]
    (A : Type*) [CommMonoid A] (c : QuasiCharacter K Γ₀ A) (h : conductorExponent K Γ₀ A c = 0) :
    quasiCharConductor K Γ₀ A c = ⊥ := by
  dsimp [quasiCharConductor]
  rw [h]
  rfl

end examples
