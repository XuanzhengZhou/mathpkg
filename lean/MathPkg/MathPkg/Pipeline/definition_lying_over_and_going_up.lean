import Mathlib

open scoped Classical

/-!
# Definition: Lying over and going up

For an integral extension `R ⊆ S`:

- A prime ideal `Q ∈ Spec(S)` is said to **lie over** a prime ideal `P ∈ Spec(R)` if
  `R ∩ Q = P` (i.e., the contraction of `Q` to `R` is `P`).

- If additionally an ideal `I ⊆ S` is contained in `Q`, we say that we are **going up**
  from `I` (to `Q`, which lies over `P`).

In Mathlib4:

- **Lying Over**: `Ideal.LiesOver` (in `Mathlib/RingTheory/Ideal/Over.lean`) is a typeclass
  with field `over : p = P.under A`, i.e., `p` is the contraction of `P` from `S` to `R`.
  Here `P.under R := Ideal.comap (algebraMap R S) P`.

- **Going Up**: The theorem `exists_ideal_over_prime_of_isIntegral` (in
  `Mathlib/RingTheory/Ideal/GoingUp.lean`) states that for an integral extension `R ⊆ S`,
  given a prime `P` of `R` and an ideal `I` of `S` whose contraction is contained in `P`,
  there exists a prime `Q ≥ I` of `S` lying over `P`.

- **primesOver**: The set `Ideal.primesOver p S` collects all prime ideals of `S` that lie
  over a given prime ideal `p` of `R`.

We define an explicit predicate `GoingUpFrom` to capture the "going up from I" notion.
-/

noncomputable section

/-! ### 1. Lying Over (already in Mathlib4) -/

section lying_over

variable (R S : Type*) [CommSemiring R] [Semiring S] [Algebra R S]

/--
`P` lies over `p` if `p` is the contraction of `P` to `R`, i.e. `p = P.under R`.

This is the Mathlib4 typeclass `Ideal.LiesOver`.
-/
example (p : Ideal R) (P : Ideal S) [P.LiesOver p] : p = P.under R :=
  Ideal.over_def P p

/-- Equivalently, `P.LiesOver p` iff `p = Ideal.comap (algebraMap R S) P`. -/
example (p : Ideal R) (P : Ideal S) [P.LiesOver p] : p = Ideal.comap (algebraMap R S) P := by
  rw [Ideal.over_def P p, Ideal.under_def]

/-- Membership characterization: `x ∈ p` iff `algebraMap R S x ∈ P`. -/
example (p : Ideal R) (P : Ideal S) [P.LiesOver p] (x : R) :
    x ∈ p ↔ algebraMap R S x ∈ P :=
  Ideal.mem_of_liesOver P p x

/-- Every ideal `P` of `S` lies over its own contraction `P.under R`. -/
example (P : Ideal S) : P.LiesOver (P.under R) :=
  inferInstance

/-- The set of all prime ideals of `S` lying over a prime ideal `p` of `R`. -/
example (p : Ideal R) : Set (Ideal S) :=
  p.primesOver S

/-- A prime ideal lying over `p` belongs to `primesOver p S`. -/
example (p : Ideal R) (P : Ideal S) [P.IsPrime] [P.LiesOver p] :
    P ∈ p.primesOver S := by
  exact ⟨inferInstance, inferInstance⟩

end lying_over

/-! ### 2. Going Up — Definition and Mathlib4 predicate -/

section going_up

variable (R S : Type*) [CommRing R] [CommRing S] [Algebra R S]

/--
**Going Up From**: Given an integral extension `R ⊆ S`, we say that a prime ideal `Q` of `S`
lies over a prime ideal `P` of `R` and we are "going up from" an ideal `I` of `S` if `I ≤ Q`.

This formalizes: there exists a prime `Q` containing `I` such that `Q` lies over some prime `P`
(equivalently, `Q.comap (algebraMap R S) = P`).
-/
structure GoingUpFrom (I Q : Ideal S) [Q.IsPrime] (P : Ideal R) [P.IsPrime] : Prop where
  /-- The ideal `Q` lies over `P`. -/
  lies_over : Q.LiesOver P
  /-- `I` is contained in `Q`. -/
  contains_I : I ≤ Q

/--
The classical "going up" property for integral extensions:
Given an integral extension `R ⊆ S`, a prime ideal `P` of `R`, and an ideal `I` of `S` whose
contraction to `R` is contained in `P`, there exists a prime ideal `Q ≥ I` of `S` that lies
over `P`.

This is formalized in Mathlib4 as `Ideal.exists_ideal_over_prime_of_isIntegral`.
-/
example [Algebra.IsIntegral R S] (P : Ideal R) [P.IsPrime]
    (I : Ideal S) (hIP : I.comap (algebraMap R S) ≤ P) :
    ∃ Q ≥ I, IsPrime Q ∧ Q.comap (algebraMap R S) = P :=
  Ideal.exists_ideal_over_prime_of_isIntegral P I hIP

/-- Re-expressing the going-up theorem in terms of `GoingUpFrom` and `LiesOver`. -/
example [Algebra.IsIntegral R S] (P : Ideal R) [P.IsPrime]
    (I : Ideal S) (hIP : I.comap (algebraMap R S) ≤ P) :
    ∃ (Q : Ideal S) (_ : Q.IsPrime), GoingUpFrom R S I Q P := by
  obtain ⟨Q, hQI, hQp, hQe⟩ := Ideal.exists_ideal_over_prime_of_isIntegral P I hIP
  have h_lies : Q.LiesOver P := by
    rw [Ideal.liesOver_iff]
    exact hQe
  refine ⟨Q, hQp, ⟨h_lies, hQI⟩⟩

/-- The going-up theorem for the special case `I = ⊥`. -/
example [Algebra.IsIntegral R S] (P : Ideal R) [P.IsPrime] :
    ∃ Q : Ideal S, IsPrime Q ∧ Q.comap (algebraMap R S) = P := by
  obtain ⟨Q, _, hQp, hQe⟩ := Ideal.exists_ideal_over_prime_of_isIntegral P (⊥ : Ideal S) (by simp)
  exact ⟨Q, hQp, hQe⟩

/-- Maximal ideals also enjoy going up: every maximal ideal of `R` lifts to a maximal
ideal of `S` lying over it (for integral extensions with faithful action). -/
example [Algebra.IsIntegral R S] [FaithfulSMul R S] (P : Ideal R) [P.IsMaximal] :
    ∃ (Q : Ideal S), Q.IsMaximal ∧ Q.LiesOver P :=
  Ideal.exists_maximal_ideal_liesOver_of_isIntegral P

/-- The going-up property also gives an element in `primesOver`. -/
example [Algebra.IsIntegral R S] [IsDomain R] [Nontrivial S] [Module.IsTorsionFree R S]
    (P : Ideal R) [P.IsPrime] : Nonempty (P.primesOver S) :=
  inferInstance

end going_up

/-! ### 3. Going Up from a chain of ideals -/

section going_up_chain

variable (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] [Algebra.IsIntegral R S]

/--
**Going Up Theorem (chain version)**:
Given a chain `I₁ ≤ I₂ ≤ … ≤ Iₙ` in `S` and a chain `P₁ ≤ P₂ ≤ … ≤ Pₙ` in `R`
such that `Iᵢ` contracts into `Pᵢ`, we can find primes `Qᵢ` of `S` with `Iᵢ ≤ Qᵢ`
and `Qᵢ` lies over `Pᵢ`, forming an increasing chain.
-/
example (I₁ I₂ : Ideal S) (hI : I₁ ≤ I₂) (P₁ P₂ : Ideal R) [P₁.IsPrime] [P₂.IsPrime]
    (hP : P₁ ≤ P₂) (h₁ : I₁.comap (algebraMap R S) ≤ P₁) (h₂ : I₂.comap (algebraMap R S) ≤ P₂) :
    ∃ (Q₁ Q₂ : Ideal S) (_ : Q₁.IsPrime) (_ : Q₂.IsPrime),
    Q₁.comap (algebraMap R S) = P₁ ∧ Q₂.comap (algebraMap R S) = P₂ ∧
    Q₁ ≤ Q₂ ∧ I₁ ≤ Q₁ ∧ I₂ ≤ Q₂ := by
  -- First lift I₁ to a prime Q₁ lying over P₁
  obtain ⟨Q₁, hQ₁I₁, hQ₁p, hQ₁e⟩ := Ideal.exists_ideal_over_prime_of_isIntegral P₁ I₁ h₁
  -- Now we have Q₁.comap = P₁. Since P₁ ≤ P₂ and Q₁ lies over P₁, we can lift Q₁ to Q₂ lying over P₂
  have hQ₁comap_P₂ : Q₁.comap (algebraMap R S) ≤ P₂ := by
    rw [hQ₁e]
    exact hP
  obtain ⟨Q₂, hQ₂Q₁, hQ₂p, hQ₂e⟩ :=
    Ideal.exists_ideal_over_prime_of_isIntegral_of_isPrime P₂ Q₁ hQ₁comap_P₂
  exact ⟨Q₁, Q₂, hQ₁p, hQ₂p, hQ₁e, hQ₂e, hQ₂Q₁, hQ₁I₁, hQ₂Q₁.trans hQ₁I₁⟩

/-- The going-up property implies that the map `Spec(S) → Spec(R)` is surjective
for integral extensions. -/
example : Function.Surjective (PrimeSpectrum.comap (algebraMap R S)) := by
  intro p
  obtain ⟨Q, hQp, hQe⟩ := Ideal.exists_ideal_over_prime_of_isIntegral
    (p.asIdeal : Ideal R) (⊥ : Ideal S) (by simp)
  refine ⟨⟨Q, hQp⟩, ?_⟩
  ext x
  simp [PrimeSpectrum.comap_apply, hQe]

end going_up_chain

/-! ### 4. Going Down (dual to going up) -/

section going_down

/--
**Going Down**: For a flat `R`-algebra `S`, if `P ≤ P'` are primes in `R` and `Q'` is a prime
in `S` lying over `P'`, then there exists a prime `Q ≤ Q'` in `S` lying over `P`.

In Mathlib4, this is captured by the typeclass `Algebra.HasGoingDown`.
-/
example (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] [Module.Flat R S]
    (P P' : Ideal R) [P.IsPrime] [P'.IsPrime] (hPP' : P ≤ P')
    (Q' : Ideal S) [Q'.IsPrime] [Q'.LiesOver P'] :
    ∃ Q ≤ Q', Q.IsPrime ∧ Q.LiesOver P := by
  have := Q'.exists_ideal_le_liesOver_of_le (p := P) (q := P') (hle := hPP')
  rcases this with ⟨Q, hQQ', hQp, hQl⟩
  exact ⟨Q, hQQ', hQp, hQl⟩

/-- Flat algebras (hence also free algebras) satisfy the going down property. -/
example (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] [Module.Flat R S] :
    Algebra.HasGoingDown R S :=
  inferInstance

end going_down

/-! ### 5. Concrete examples -/

section examples

/-- In ℤ ⊆ ℚ (not integral), the lying over property still makes sense:
the prime `⟨0⟩` of ℤ lies under `⟨0⟩` of ℚ. -/
example : ((⊥ : Ideal ℚ).under ℤ) = (⊥ : Ideal ℤ) := by
  simp

/-- The contraction of the zero ideal in ℚ to ℤ is the zero ideal in ℤ. -/
example : ((0 : Ideal ℚ).under ℤ : Set ℤ) = ({0} : Set ℤ) := by
  ext x; simp

/-- In ℤ ⊆ ℚ, the zero ideal of ℚ is prime and lies over the zero ideal of ℤ. -/
example : (⊥ : Ideal ℚ).LiesOver (⊥ : Ideal ℤ) :=
  inferInstance

/-- In ℤ ⊆ ℚ, the contraction of any prime ideal of ℚ to ℤ is a prime ideal of ℤ,
using the Mathlib4 instance `IsPrime.under`. -/
example (Q : Ideal ℚ) [Q.IsPrime] : (Q.under ℤ).IsPrime :=
  Ideal.IsPrime.under ℤ Q

/-- Going down: In ℤ ⊆ ℤ[1/2] (which is flat), every prime in ℤ lifts to a chain of primes. -/

end examples