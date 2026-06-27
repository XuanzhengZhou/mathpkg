import Mathlib

open scoped Classical

/-!
# Definition of Contraction and Lies Over

If `S` is an extension ring of `R` and `I` is an ideal of `S`, then `I ∩ R` is an ideal of `R`
called the **contraction** of `I` to `R`, and `I` is said to **lie over** `J = I ∩ R`.
If `Q` is a prime ideal in `S`, then `Q ∩ R` is a prime ideal of `R`.

In Mathlib4, this is formalized in `Mathlib/RingTheory/Ideal/Over.lean`:
- **Contraction**: `Ideal.under A P := Ideal.comap (algebraMap A B) P`
- **Lies Over**: `Ideal.LiesOver` is a typeclass with field `over : p = P.under A`
- **Prime contraction**: The instance `IsPrime.under` proves that `P.under A` is prime.
- **primesOver**: The set of all prime ideals lying over a given ideal.

## Sub-concepts

- **Going-up / Going-down**: Properties of ring extensions concerning chains of prime ideals
  lying over each other.
- **Incomparability**: Two prime ideals lying over the same prime ideal are incomparable.
-/

noncomputable section

/-! ### 1. Contraction of an ideal to a subring -/

section contraction

variable (R S : Type*) [CommSemiring R] [Semiring S] [Algebra R S]

/-- The contraction of an ideal `I` of `S` to `R` is `I ∩ R`, realized as `Ideal.under R I`. -/
example (I : Ideal S) : I.under R = Ideal.comap (algebraMap R S) I :=
  rfl

/-- An element `x : R` is in the contraction of `I` iff `algebraMap R S x` is in `I`. -/
example (I : Ideal S) (x : R) : x ∈ I.under R ↔ algebraMap R S x ∈ I :=
  Ideal.mem_under (A := R) (P := I) (x := x)

/-- Contraction respects the algebra map: `algebraMap` sends the contraction into the ideal. -/
example (I : Ideal S) : algebraMap R S '' (I.under R : Set R) ⊆ (I : Set S) := by
  rintro y ⟨x, hx, rfl⟩
  simpa using hx

/-- The contraction of `⊤` is `⊤`. -/
example : (⊤ : Ideal S).under R = ⊤ :=
  Ideal.under_top R S

/-- The contraction of `⊥` is `⊥` when the algebra map is injective
  (e.g. for domains as extensions). -/
example (A B : Type*) [CommRing A] [IsDomain A] [Ring B] [Nontrivial B]
    [Algebra A B] [Module.IsTorsionFree A B] : (⊥ : Ideal B).under A = ⊥ :=
  Ideal.under_bot A B

/-- Contraction is contravariant: if `I ≤ J` then `I.under R ≤ J.under R`. -/
example (I J : Ideal S) (h : I ≤ J) : I.under R ≤ J.under R :=
  Ideal.comap_mono h

/-- The contraction of the contraction from a tower `R → A → B` is the contraction from `R`. -/
example (A : Type*) [CommSemiring A] [Algebra R A] [Algebra A S]
    [IsScalarTower R A S] (I : Ideal S) : (I.under A).under R = I.under R :=
  Ideal.under_under I

end contraction

/-! ### 2. Lies Over -/

section lies_over

variable (R S : Type*) [CommSemiring R] [Semiring S] [Algebra R S]

/-- `P` lies over `p` if `p = P.under R`, i.e. `P ∩ R = p`.
  This is the `Ideal.LiesOver` typeclass. -/
example (p : Ideal R) (P : Ideal S) [P.LiesOver p] : p = P.under R :=
  Ideal.over_def P p

/-- If `P` lies over `p`, then `x ∈ p ↔ algebraMap R S x ∈ P`. -/
example (p : Ideal R) (P : Ideal S) [P.LiesOver p] (x : R) :
    x ∈ p ↔ algebraMap R S x ∈ P :=
  Ideal.mem_of_liesOver P p x

/-- Every ideal lies over its own contraction. -/
example (P : Ideal S) : P.LiesOver (P.under R) :=
  inferInstance

/-- The top ideal lies over the top ideal. -/
example : (⊤ : Ideal S).LiesOver (⊤ : Ideal R) :=
  inferInstance

/-- The bottom ideal lies over the bottom ideal (for torsion-free domains). -/
example (A B : Type*) [CommRing A] [IsDomain A] [Ring B] [Nontrivial B]
    [Algebra A B] [Module.IsTorsionFree A B] : (⊥ : Ideal B).LiesOver (⊥ : Ideal A) :=
  inferInstance

/-- If `P` lies over `p` and `P.IsPrime`, then `p.IsPrime`. -/
example (p : Ideal R) (P : Ideal S) [P.IsPrime] [P.LiesOver p] : p.IsPrime :=
  Ideal.isPrime_of_liesOver P p

/-- LiesOver is transitive in a tower of ring extensions. -/
example (A : Type*) [CommSemiring A] [Algebra R A] [Algebra A S]
    [IsScalarTower R A S] (𝔓 : Ideal S) (P : Ideal A) (p : Ideal R)
    [𝔓.LiesOver P] [P.LiesOver p] : 𝔓.LiesOver p :=
  Ideal.LiesOver.trans 𝔓 P p

/-- If `P.LiesOver p` and `P ≠ ⊤`, then `p ≠ ⊤`. -/
example (p : Ideal R) (P : Ideal S) [P.LiesOver p] (h : P ≠ ⊤) : p ≠ ⊤ :=
  ((Ideal.ne_top_iff_of_liesOver P p).mp h)

/-- If `P.LiesOver p` and `p ≠ ⊤`, then `P ≠ ⊤`. -/
example (p : Ideal R) (P : Ideal S) [P.LiesOver p] (h : p ≠ ⊤) : P ≠ ⊤ :=
  ((Ideal.ne_top_iff_of_liesOver P p).mpr h)

/-- For a field extension `K → A`, every prime ideal `P` of `A` lies over `⊥` of `K`. -/
example (K A : Type*) [Field K] [Semiring A] [Algebra K A] (P : Ideal A) [P.IsPrime] :
    P.LiesOver (⊥ : Ideal K) :=
  inferInstance

end lies_over

/-! ### 3. Prime contraction: If Q is prime in S, then Q ∩ R is prime in R -/

section prime_contraction

variable (R S : Type*) [CommSemiring R] [Semiring S] [Algebra R S]

/-- **Prime Contraction Theorem**: If `Q` is a prime ideal of `S`,
  then its contraction `Q ∩ R` is a prime ideal of `R`.
  This is the instance `Ideal.IsPrime.under`. -/
theorem contraction_of_prime_is_prime (Q : Ideal S) [Q.IsPrime] :
    (Q.under R).IsPrime :=
  inferInstance

/-- The proof of prime contraction uses `Ideal.IsPrime.comap`. -/
example (Q : Ideal S) [hQ : Q.IsPrime] : (Q.under R).IsPrime :=
  hQ.comap (algebraMap R S)

/-- Full explicit statement with proof: If `Q` is prime in `S`, then `Q ∩ R` is prime in `R`. -/
theorem intersection_of_prime_with_subring_is_prime (Q : Ideal S) [Q.IsPrime] :
    (Ideal.comap (algebraMap R S) Q).IsPrime :=
  Ideal.IsPrime.comap (algebraMap R S)

/-- The condition for the contraction being prime: `x * y ∈ Q.under R` implies `x` or `y` lies in
  the contraction. -/
example (Q : Ideal S) [hQ : Q.IsPrime] (x y : R) (h : x * y ∈ Q.under R) :
    x ∈ Q.under R ∨ y ∈ Q.under R := by
  have h' : algebraMap R S (x * y) ∈ Q := by
    simpa using h
  rw [map_mul] at h'
  rcases hQ.mem_or_mem h' with (hx | hy)
  · left; simpa using hx
  · right; simpa using hy

end prime_contraction

/-! ### 4. The set of all prime ideals lying over a given ideal (`primesOver`) -/

section primes_over

variable (R S : Type*) [CommSemiring R] [Semiring S] [Algebra R S]

/-- `Ideal.primesOver p S` is the set of all prime ideals of `S` that lie over `p`. -/
example (p : Ideal R) : Set (Ideal S) :=
  p.primesOver S

/-- A member of `primesOver` is a prime ideal lying over `p`. -/
example (p : Ideal R) (Q : p.primesOver S) : Q.1.IsPrime ∧ Q.1.LiesOver p :=
  ⟨Q.2.1, Q.2.2⟩

/-- Construct an element of `primesOver` from a prime ideal `P` lying over `p`. -/
def primesOver.mk' (p : Ideal R) (P : Ideal S) [hPp : P.IsPrime] [hp : P.LiesOver p] :
    p.primesOver S :=
  ⟨P, ⟨hPp, hp⟩⟩

end primes_over

/-! ### 5. Concrete examples -/

section examples

/-- Example: In ℤ ⊂ ℚ, the contraction of any proper ideal of ℚ (namely `⊥`) to ℤ is `⊥`. -/
example : ((⊥ : Ideal ℚ).under ℤ : Set ℤ) = ({0} : Set ℤ) := by
  ext x; simp

/-- Example: The contraction of `⊤` of ℚ to ℤ is `⊤` (since 1 ∈ ℚ is in ℤ). -/
example : ((⊤ : Ideal ℚ).under ℤ : Set ℤ) = Set.univ := by
  ext x; simp

/-- Example: In ℤ ⊂ ℚ, the zero ideal `⟨0⟩` of ℚ is prime, so its contraction `⟨0⟩` of ℤ is prime. -/
example : ((⊥ : Ideal ℚ).under ℤ).IsPrime :=
  contraction_of_prime_is_prime ℤ ℚ ⊥

/-- Example: In ℝ ⊂ ℂ, the zero ideal `⟨0⟩` is prime in both; contraction preserves primality. -/
example : ((⊥ : Ideal ℂ).under ℝ).IsPrime :=
  contraction_of_prime_is_prime ℝ ℂ ⊥

/-- Example: In ℤ ⊂ ℚ, the prime ideals in ℚ are only `⟨0⟩` and `ℚ`.
  `⟨0⟩` contracts to `⟨0⟩` in ℤ, `ℚ` contracts to `ℤ`. Both are prime in ℤ. -/
example : ((⊥ : Ideal ℚ).under ℤ).IsPrime := by
  have hprime : (⊥ : Ideal ℚ).IsPrime := Ideal.isPrime_bot
  exact hprime.comap (algebraMap ℤ ℚ)

/-- Example: In ℤ ⊂ ℚ, the total ideal `ℚ` contracts to `ℤ`, which is NOT prime.
  However the contraction is always an ideal (but not necessarily prime). -/
example : ((⊤ : Ideal ℚ).under ℤ) = ⊤ :=
  Ideal.under_top ℤ ℚ

/-- Example: For any ring extension `R → S`, the contraction of any ideal `J` is contained in `J`. -/
example (R S : Type*) [CommSemiring R] [Semiring S] [Algebra R S] (J : Ideal S) : algebraMap R S '' (J.under R : Set R) ⊆ (J : Set S) := by
  rintro y ⟨x, hx, rfl⟩
  simpa using hx

end examples

/-! ### 6. Extension of ideals (dual to contraction) -/

section extension

/-- The **extension** of an ideal `I` of `R` to `S` is `I · S`, the ideal generated by the image
  of `I` under `algebraMap R S`. This is `Ideal.map (algebraMap R S) I`. -/
example (R S : Type*) [CommSemiring R] [Semiring S] [Algebra R S] (I : Ideal R) : Ideal S :=
  Ideal.map (algebraMap R S) I

/-- The extension of `I` is the smallest ideal of `S` containing the image of `I`. -/
example (R S : Type*) [CommSemiring R] [Semiring S] [Algebra R S] (I : Ideal R) (x : R)
    (hx : x ∈ I) : algebraMap R S x ∈ Ideal.map (algebraMap R S) I :=
  Ideal.mem_map_of_mem _ hx

/-- Contraction-extension relation: `I ≤ (I · S) ∩ R`. -/
example (R S : Type*) [CommSemiring R] [Semiring S] [Algebra R S] (I : Ideal R) :
    I ≤ (Ideal.map (algebraMap R S) I).under R := by
  intro x hx
  rw [Ideal.mem_under (A := R)]
  exact Ideal.mem_map_of_mem _ hx

/-- Extension-contraction relation: `(J ∩ R) · S ≤ J`. -/
example (R S : Type*) [CommSemiring R] [Semiring S] [Algebra R S] (J : Ideal S) :
    Ideal.map (algebraMap R S) (J.under R) ≤ J := by
  simp [Ideal.under, Ideal.map_comap_le]

end extension
