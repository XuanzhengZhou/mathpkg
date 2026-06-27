import Mathlib

/-!
# Inner Automorphism and Center Theorem

For a group `G`:
(i) For each `g ∈ G`, conjugation by `g` induces an automorphism of `G`.
(ii) There is a homomorphism `G → MulAut G` whose kernel is `C(G) = {g ∈ G | gx = xg for all x ∈ G}`.

In Mathlib4:
- `MulAut.conj (G := G) : G →* MulAut G` is the conjugation homomorphism.
- `Subgroup.center G` is the center of `G` as a subgroup.
- `MonoidHom.ker (MulAut.conj (G := G))` is the kernel.

## Main definitions

* `MulAut.conj` — the homomorphism `G →* MulAut G` sending `g` to conjugation by `g`.
* `innerAutomorphism` — `MulAut.conj g`, the inner automorphism induced by `g`.
* `innerAutomorphism_ker_center` — the kernel of `MulAut.conj` equals the center of `G`.
-/

open Subgroup

variable {G : Type*} [Group G]

/--
  For a fixed element `g : G`, the conjugation-by-`g` map `x ↦ gxg⁻¹` is an automorphism of `G`.
  In Mathlib4, this is exactly `MulAut.conj g : MulAut G`.
-/
def innerAutomorphism (g : G) : MulAut G :=
  MulAut.conj g

/--
  `MulAut.conj` is a group homomorphism from `G` to `MulAut G`.
  That is, `MulAut.conj (g * h) = MulAut.conj g * MulAut.conj h` and `MulAut.conj 1 = 1`.
-/
example (g h : G) : MulAut.conj (g * h) = MulAut.conj g * MulAut.conj h :=
  map_mul (MulAut.conj (G := G)) g h

example : MulAut.conj (1 : G) = 1 :=
  map_one (MulAut.conj (G := G))

/--
  (ii) The kernel of the conjugation homomorphism `G → MulAut G` equals the center of `G`.

  That is, `g` is in the kernel of `MulAut.conj` if and only if `g ∈ Subgroup.center G`.
  Equivalently, conjugation by `g` is the identity automorphism iff `g` commutes with all elements.
-/
theorem innerAutomorphism_ker_center :
    MonoidHom.ker (MulAut.conj (G := G)) = Subgroup.center G := by
  ext g
  constructor
  · intro hg
    -- g ∈ ker(MulAut.conj), so MulAut.conj g = 1
    rw [MonoidHom.mem_ker] at hg
    -- Show g commutes with every x ∈ G
    rw [Subgroup.mem_center_iff]
    intro x
    -- From MulAut.conj g = 1, we have (conj g) x = x, i.e., g * x * g⁻¹ = x
    have h_conj : (MulAut.conj (G := G) g) x = x := by
      rw [hg]
      simp
    rw [MulAut.conj_apply] at h_conj
    -- g * x * g⁻¹ = x → x * g = g * x
    have h' : g * x = x * g := by
      calc
        g * x = (g * x * g⁻¹) * g := by group
        _ = x * g := by rw [h_conj]
    exact h'.symm
  · intro hg
    -- g ∈ center G, so g commutes with everything
    rw [Subgroup.mem_center_iff] at hg
    rw [MonoidHom.mem_ker]
    -- Show MulAut.conj g = 1, i.e., conjugation by g is the identity
    ext x
    rw [MulAut.conj_apply, ← hg x]
    simp

/--
  An element `g` is in the center of `G` if and only if conjugation by `g` is the identity
  automorphism. This is a corollary of `innerAutomorphism_ker_center`.
-/
theorem mem_center_iff_conj_eq_one (g : G) :
    g ∈ Subgroup.center G ↔ MulAut.conj (G := G) g = 1 := by
  rw [← innerAutomorphism_ker_center, MonoidHom.mem_ker]

/--
  Conjugation by `g` is the identity if and only if `g` commutes with every element of `G`.
  This is the key equivalence underlying the theorem.
-/
theorem conj_eq_one_iff_forall_commute (g : G) :
    MulAut.conj (G := G) g = 1 ↔ ∀ x : G, g * x = x * g := by
  constructor
  · intro h x
    have hmem := (mem_center_iff_conj_eq_one g).mpr h
    rw [Subgroup.mem_center_iff] at hmem
    exact (hmem x).symm
  · intro h
    have hmem : g ∈ Subgroup.center G := by
      rw [Subgroup.mem_center_iff]
      intro g₁
      exact (h g₁).symm
    exact (mem_center_iff_conj_eq_one g).mp hmem

/--
  Example: for `g, h : G`, the element `MulAut.conj g h` equals `g * h * g⁻¹`.
-/
example (g h : G) : (MulAut.conj g) h = g * h * g⁻¹ :=
  MulAut.conj_apply g h

/--
  Example: if `g` is in the center, then conjugation by `g` is the identity,
  so `g * h * g⁻¹ = h` for all `h`.
-/
example (g : G) (hg : g ∈ Subgroup.center G) (h : G) : g * h * g⁻¹ = h := by
  have := (mem_center_iff_conj_eq_one g).mp hg
  rw [← MulAut.conj_apply]
  simp [this]

/--
  Example: the inverse direction — if conjugation by `g` is the identity,
  then `g` is in the center.
-/
example (g : G) (h_conj : ∀ h : G, g * h * g⁻¹ = h) : g ∈ Subgroup.center G := by
  rw [mem_center_iff_conj_eq_one]
  ext x
  simp [MulAut.conj_apply, h_conj x]
