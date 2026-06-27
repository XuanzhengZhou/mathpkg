import Mathlib

open Subring

/-!
# Intersection of Integrally Closed Subrings

Let T be a commutative ring with identity and {S_i}, {R_i} families of subrings such that
T is an extension ring of S_i and S_i is an extension ring of R_i for every i.
If each R_i is integrally closed in S_i, then ∩ R_i is integrally closed in ∩ S_i.

## Proof

Take x ∈ ∩ S_i integral over ∩ R_i. Since ∩ R_i ⊆ R_i, x is integral over each R_i.
Since each R_i is integrally closed in S_i and x ∈ S_i, we have x ∈ R_i for all i.
Hence x ∈ ∩ R_i.
-/

section intersection_of_integrally_closed_subrings

variable {ι : Type*} {T : Type*} [CommRing T]
  (R S : ι → Subring T)
  (hRS : ∀ i, R i ≤ S i)

/-- The intersection of all R_i -/
def interR : Subring T := ⨅ k, R k

/-- The intersection of all S_i -/
def interS : Subring T := ⨅ k, S k

theorem intersection_of_integrally_closed_subrings
    [∀ i, Algebra (R i) (S i)]
    (h_int_closed : ∀ i, IsIntegrallyClosedIn (R i) (S i)) :
    IsIntegrallyClosedIn (interR R) (interS S) := by
  -- Provide Algebra instance for interR → interS
  letI : Algebra (interR R) (interS S) :=
    (Subring.inclusion (by
      -- interR R ⊆ interS S because each R_i ⊆ S_i
      intro x hx
      rw [Subring.mem_iInf] at hx ⊢
      intro i
      exact hRS i (hx i)
    )).toAlgebra
  -- Algebra instances for interR → each R i
  have hAlg_interR_Ri (i : ι) : Algebra (interR R) (R i) :=
    (Subring.inclusion (iInf_le (fun k => R k) i)).toAlgebra
  -- Using the general isIntegrallyClosedIn_iff
  rw [isIntegrallyClosedIn_iff]
  refine ⟨?_, ?_⟩
  · -- algebraMap interR interS is injective (it's the inclusion)
    intro a b h
    apply Subtype.ext
    exact congrArg Subtype.val h
  · intro x hx_int
    -- x : interS S, hx_int : IsIntegral (interR R) x
    -- Goal: ∃ y : interR R, algebraMap (interR R) (interS S) y = x
    -- Plan: show x (as element of T) is in each R i, hence in interR R
    have hx_T_in_Ri : ∀ i : ι, (x : T) ∈ R i := by
      intro i
      -- (1) Using tower_top, lift integrality from interR R to R i (in T)
      haveI : Algebra (interR R) (R i) := hAlg_interR_Ri i
      haveI : IsScalarTower (interR R) (R i) T := by
        apply IsScalarTower.of_algebraMap_eq'
        ext z
        simp [hAlg_interR_Ri i]
      have hx_int_Ri_T : IsIntegral (R i) (x : T) :=
        IsIntegral.tower_top (A := R i) hx_int
      -- (2) x is in S i (since x is in the intersection interS S)
      have hx_T_in_Si : (x : T) ∈ S i := by
        have hx_T_in_SI : (x : T) ∈ interS S := x.property
        rw [Subring.mem_iInf] at hx_T_in_SI
        exact hx_T_in_SI i
      -- (3) Convert IsIntegral over R i of (x : T) to IsIntegral over R i of (x : S i)
      have hx_Si_int : IsIntegral (R i) (⟨(x : T), hx_T_in_Si⟩ : S i) := by
        have hinj : Function.Injective (algebraMap (S i) T) := Subring.injective _
        rw [← isIntegral_algebraMap_iff hinj]
        simpa using hx_int_Ri_T
      -- (4) Apply the hypothesis that R i is integrally closed in S i
      rw [Subring.isIntegrallyClosedIn_iff] at h_int_closed
      have h_mem := (h_int_closed i) hx_Si_int
      -- h_mem : ⟨(x : T), hx_T_in_Si⟩ ∈ R i
      simpa using h_mem
    -- Now we know (x : T) ∈ R i for all i, so (x : T) ∈ interR R
    have hx_T_in_interR : (x : T) ∈ interR R := by
      rw [Subring.mem_iInf]
      exact hx_T_in_Ri
    -- Construct the desired y : interR R
    refine ⟨⟨(x : T), hx_T_in_interR⟩, ?_⟩
    ext
    rfl

end intersection_of_integrally_closed_subrings
