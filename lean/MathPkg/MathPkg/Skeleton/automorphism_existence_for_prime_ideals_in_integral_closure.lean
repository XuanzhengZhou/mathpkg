import Mathlib

open scoped Classical

/- Automorphism existence for prime ideals in the integral closure.

Let N be a field and K ⊆ N a subfield such that N is finite and normal over K.
Let R ⊆ K be a subring that is integrally closed in K, and let S ⊆ N be the
integral closure of R in N. Then for two prime ideals Q, Q̃ ∈ Spec(S) with
R ∩ Q = R ∩ Q̃, there exists σ ∈ G := Aut_K(N) with Q̃ = σ(Q). -/

lemma automorphism_existence_for_prime_ideals_in_integral_closure
    (K N : Type*) [Field K] [Field N] [Algebra K N]
    [FiniteDimensional K N] [IsGalois K N]
    (R : Subring K) [IsIntegrallyClosed R]
    (Q Q' : Ideal (integralClosure R N))
    (hQ : Q.IsPrime) (hQ' : Q'.IsPrime)
    (h_eq : Ideal.comap (algebraMap R (integralClosure R N)) Q =
            Ideal.comap (algebraMap R (integralClosure R N)) Q') :
    ∃ σ : N ≃ₐ[K] N,
      Ideal.map (algebraMap (integralClosure R N) N) Q' =
      Ideal.map ((σ : N →+* N).comp (algebraMap (integralClosure R N) N)) Q := by
  sorry
