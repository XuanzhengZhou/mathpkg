import Mathlib

/-!
# Indecomposable Group

A group G is indecomposable when G ≠ 1 and G = A ⊕ B implies A = 1 or B = 1.

We formalize this for additive commutative groups, using `IsCompl` to capture the internal
direct sum decomposition: `IsCompl A B` means `Disjoint A B` and `Codisjoint A B`.

## Main definition

* `IsIndecomposable G` : An additive commutative group `G` is indecomposable if it is nontrivial
  and whenever it is the internal direct sum of two subgroups, one of them must be trivial.
-/

open AddSubgroup

variable {G : Type*} [AddCommGroup G]

/-- An additive commutative group `G` is indecomposable if it is nontrivial and
cannot be written as the internal direct sum of two nontrivial subgroups.

Formally: whenever `A, B` are additive subgroups of `G` with `IsCompl A B`
(i.e., `Disjoint A B` and `Codisjoint A B`), then one of `A` or `B` must be `⊥`. -/
def IsIndecomposable (G : Type*) [AddCommGroup G] : Prop :=
  Nontrivial G ∧ ∀ (A B : AddSubgroup G), IsCompl A B → A = ⊥ ∨ B = ⊥

namespace IsIndecomposable

/-- The trivial group is not indecomposable. -/
theorem not_indec_of_subsingleton [Subsingleton G] : ¬ IsIndecomposable G := by
  rintro ⟨h, _⟩
  exact not_nontrivial G h

/-- In a domain where no two nontrivial subgroups are disjoint (e.g. ℤ),
the group is automatically indecomposable. -/
theorem indecomposable_of_no_nontriv_disjoint
    (h_nontriv : Nontrivial G)
    (h_no_disj : ∀ (A B : AddSubgroup G), A ≠ ⊥ → B ≠ ⊥ → ¬ Disjoint A B) :
    IsIndecomposable G := by
  refine ⟨h_nontriv, ?_⟩
  intro A B h_compl
  rcases h_compl with ⟨h_disj, _⟩
  by_cases hA : A = ⊥
  · left; exact hA
  · by_cases hB : B = ⊥
    · right; exact hB
    · exfalso; exact h_no_disj A B hA hB h_disj

/-- Helper lemma: if an additive subgroup is not ⊥, it contains a nonzero element. -/
theorem exists_ne_zero_of_ne_bot {H : AddSubgroup G} (hH : H ≠ ⊥) : ∃ a ∈ H, a ≠ 0 := by
  by_contra! h
  apply hH
  apply eq_bot_iff.mpr
  intro x hx
  rw [mem_bot]
  by_contra! hx0
  exact hx0 (h x hx)

/-- ℤ is indecomposable because any two nonzero subgroups of ℤ have nonzero intersection.
In ℤ, subgroups are of the form nℤ, and (mℤ) ⊓ (nℤ) = lcm(m,n)ℤ ≠ ⊥ for m, n ≠ 0. -/
theorem indecomposable_int : IsIndecomposable ℤ := by
  apply indecomposable_of_no_nontriv_disjoint (by infer_instance)
  intro A B hA hB
  rcases exists_ne_zero_of_ne_bot hA with ⟨a, ha, ha0⟩
  rcases exists_ne_zero_of_ne_bot hB with ⟨b, hb, hb0⟩
  -- a ∈ A, a ≠ 0 and b ∈ B, b ≠ 0
  -- Use zsmul: (b : ℤ) • a ∈ A and (a : ℤ) • b ∈ B
  have ha_smul : (b : ℤ) • a ∈ A := AddSubgroup.zsmul_mem A ha (b : ℤ)
  have hb_smul : (a : ℤ) • b ∈ B := AddSubgroup.zsmul_mem B hb (a : ℤ)
  have h_eq : (b : ℤ) • a = (a : ℤ) • b := by
    simp [mul_comm]
  have h_mem_inf : (b : ℤ) • a ∈ A ⊓ B := by
    apply AddSubgroup.mem_inf.mpr
    exact ⟨ha_smul, h_eq ▸ hb_smul⟩
  have h_ne_zero : (b : ℤ) • a ≠ 0 := by
    rw [zsmul_eq_mul]
    exact mul_ne_zero hb0 ha0
  intro h_disj
  -- h_disj : Disjoint A B
  -- Use Disjoint.le_bot: A ⊓ B ≤ ⊥
  have h_mem_bot : (b : ℤ) • a ∈ (⊥ : AddSubgroup ℤ) := h_disj.le_bot h_mem_inf
  rw [AddSubgroup.mem_bot] at h_mem_bot
  exact h_ne_zero h_mem_bot

/-- ℤ/4ℤ is indecomposable.
The subgroups of ℤ/4ℤ are: ⊥, the subgroup {0, 2}, and ⊤.
No two nontrivial proper subgroups are disjoint, because the only nontrivial proper subgroup
is {0, 2}, and it is not disjoint from itself. -/
theorem indecomposable_ZMod4 : IsIndecomposable (ZMod 4) := by
  have hnontriv : Nontrivial (ZMod 4) := by
    refine ⟨⟨0, 1, ?_⟩⟩
    decide
  apply indecomposable_of_no_nontriv_disjoint hnontriv
  intro A B hA hB
  rcases exists_ne_zero_of_ne_bot hA with ⟨a, ha, ha0⟩
  rcases exists_ne_zero_of_ne_bot hB with ⟨b, hb, hb0⟩

  -- In ZMod 4, any nonzero element is 1, 2, or 3.
  -- 1+1=2, 2+2=0, 3+3=2. So any subgroup containing a nonzero element also contains 2.
  have h2a : (2 : ZMod 4) ∈ A := by
    have h_cases : a = 1 ∨ a = 2 ∨ a = 3 := by
      have h_all : ∀ x : ZMod 4, x = 0 ∨ x = 1 ∨ x = 2 ∨ x = 3 := by decide
      rcases h_all a with (rfl|rfl|rfl|rfl)
      · exfalso; exact ha0 rfl
      · exact Or.inl rfl
      · exact Or.inr (Or.inl rfl)
      · exact Or.inr (Or.inr rfl)
    rcases h_cases with (rfl|rfl|rfl)
    · -- a = 1, then 1+1 = 2 ∈ A
      have hsum : (1 : ZMod 4) + (1 : ZMod 4) = (2 : ZMod 4) := by decide
      rw [← hsum]
      exact AddSubgroup.add_mem A ha ha
    · -- a = 2, trivial
      exact ha
    · -- a = 3, then 3+3 = 2 ∈ A
      have hsum : (3 : ZMod 4) + (3 : ZMod 4) = (2 : ZMod 4) := by decide
      rw [← hsum]
      exact AddSubgroup.add_mem A ha ha

  have h2b : (2 : ZMod 4) ∈ B := by
    have h_cases : b = 1 ∨ b = 2 ∨ b = 3 := by
      have h_all : ∀ x : ZMod 4, x = 0 ∨ x = 1 ∨ x = 2 ∨ x = 3 := by decide
      rcases h_all b with (rfl|rfl|rfl|rfl)
      · exfalso; exact hb0 rfl
      · exact Or.inl rfl
      · exact Or.inr (Or.inl rfl)
      · exact Or.inr (Or.inr rfl)
    rcases h_cases with (rfl|rfl|rfl)
    · have hsum : (1 : ZMod 4) + (1 : ZMod 4) = (2 : ZMod 4) := by decide
      rw [← hsum]
      exact AddSubgroup.add_mem B hb hb
    · exact hb
    · have hsum : (3 : ZMod 4) + (3 : ZMod 4) = (2 : ZMod 4) := by decide
      rw [← hsum]
      exact AddSubgroup.add_mem B hb hb

  -- Both A and B contain 2, so A ⊓ B contains 2 ≠ 0, hence A and B are not disjoint
  intro h_disj
  have h_mem_inf : (2 : ZMod 4) ∈ A ⊓ B :=
    AddSubgroup.mem_inf.mpr ⟨h2a, h2b⟩
  have h_mem_bot : (2 : ZMod 4) ∈ (⊥ : AddSubgroup (ZMod 4)) := h_disj.le_bot h_mem_inf
  rw [AddSubgroup.mem_bot] at h_mem_bot
  have h2_ne_zero : (2 : ZMod 4) ≠ 0 := by
    decide
  exact h2_ne_zero h_mem_bot

/-- If G ≃+ H and G is indecomposable, then H is indecomposable. -/
theorem of_addEquiv {G H : Type*} [AddCommGroup G] [AddCommGroup H] (e : G ≃+ H)
    (hG : IsIndecomposable G) : IsIndecomposable H := by
  rcases hG with ⟨h_nontriv, h_indec⟩
  have h_nontriv' : Nontrivial H := by
    rcases exists_pair_ne G with ⟨x, y, hxy⟩
    refine ⟨⟨e x, e y, ?_⟩⟩
    intro h
    apply hxy
    exact e.injective h
  refine ⟨h_nontriv', ?_⟩
  intro A B h_compl
  rcases h_compl with ⟨h_disj, h_codisj⟩
  let f : H →+ G := e.symm
  have hf_inj : Function.Injective f := e.symm.injective
  have hf_surj : Function.Surjective f := e.symm.surjective
  let A' : AddSubgroup G := AddSubgroup.map f A
  let B' : AddSubgroup G := AddSubgroup.map f B

  -- IsCompl is preserved under map along a bijective homomorphism
  have h_compl' : IsCompl A' B' := by
    have h_disj' : Disjoint A' B' := by
      rw [disjoint_iff_inf_le]
      calc
        A' ⊓ B' = (AddSubgroup.map f A) ⊓ (AddSubgroup.map f B) := rfl
        _ = AddSubgroup.map f (A ⊓ B) := by
          rw [← AddSubgroup.map_inf_eq A B f hf_inj]
        _ ≤ AddSubgroup.map f (⊥ : AddSubgroup H) :=
          AddSubgroup.map_mono (disjoint_iff_inf_le.mp h_disj)
        _ = ⊥ := AddSubgroup.map_bot f
    have h_codisj' : Codisjoint A' B' := by
      rw [codisjoint_iff_le_sup]
      calc
        ⊤ = AddSubgroup.map f (⊤ : AddSubgroup H) := by
          rw [AddSubgroup.map_top_of_surjective f hf_surj]
        _ ≤ AddSubgroup.map f (A ⊔ B) :=
          AddSubgroup.map_mono (codisjoint_iff_le_sup.mp h_codisj)
        _ = AddSubgroup.map f A ⊔ AddSubgroup.map f B := by rw [AddSubgroup.map_sup A B f]
        _ = A' ⊔ B' := rfl
    exact ⟨h_disj', h_codisj'⟩

  rcases h_indec A' B' h_compl' with (hA' | hB')
  · -- A' = ⊥ implies A = ⊥ (since f = e.symm is injective)
    left
    have hA_le_bot : A ≤ ⊥ := by
      intro x hx
      have hfx : f x ∈ A' := AddSubgroup.mem_map.mpr ⟨x, hx, rfl⟩
      rw [hA'] at hfx
      have hfx_zero : f x = 0 := by simpa [AddSubgroup.mem_bot] using hfx
      have hx_zero : x = 0 := hf_inj (by simpa using hfx_zero)
      rw [hx_zero]
      exact AddSubgroup.zero_mem _
    exact le_antisymm hA_le_bot bot_le
  · -- B' = ⊥ implies B = ⊥
    right
    have hB_le_bot : B ≤ ⊥ := by
      intro x hx
      have hfx : f x ∈ B' := AddSubgroup.mem_map.mpr ⟨x, hx, rfl⟩
      rw [hB'] at hfx
      have hfx_zero : f x = 0 := by simpa [AddSubgroup.mem_bot] using hfx
      have hx_zero : x = 0 := hf_inj (by simpa using hfx_zero)
      rw [hx_zero]
      exact AddSubgroup.zero_mem _
    exact le_antisymm hB_le_bot bot_le

end IsIndecomposable
