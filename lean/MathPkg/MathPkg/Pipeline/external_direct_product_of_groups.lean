import Mathlib

/-!
# External Direct Product of Groups

The **external direct product** (also called the *restricted direct product* or *weak direct
product*) of a family of groups `(G_λ)_{λ∈Λ}` is the subset of the full cartesian product
`Π_λ G_λ` consisting of all `(g_λ)` such that `g_λ = 1_λ` for almost all `λ` (i.e., all but
finitely many).

When the index set `Λ` is finite, the external direct product coincides with the full cartesian
product, denoted `G_{λ₁} × ··· × G_{λ_n}`.

## Mathlib4 References
- `Pi.group` in `Algebra/Group/Pi/Basic.lean` — the group instance on the full cartesian product
- `Subgroup` in `Algebra/Group/Subgroup/Defs.lean` — subgroup construction
- `Set.Finite` in `Data/Set/Finite/Basic.lean` — finiteness of sets
- `Pi.mulSingle` in `Algebra/Group/Pi/Lemmas.lean` — element supported at a single index
-/

open Set

universe u v

variable {ι : Type u} {G : ι → Type v} [∀ i, Group (G i)]

/-- The external direct product (restricted direct product) of a family of groups.

For a family of groups `G i` indexed by `ι`, the external direct product `ExternalDirectProduct G`
consists of all functions `f : Π i, G i` such that `f i = 1` for all but finitely many `i`.
This is a subgroup of the full cartesian product `Π i, G i`.

When `ι` is finite, this coincides with the full product (see `ExternalDirectProduct.eq_top`).

**Notation**: In the literature, this is often written as `Dr_{λ∈Λ} G_λ` or `∏ᵈ G_λ`. -/
def ExternalDirectProduct (G : ι → Type v) [∀ i, Group (G i)] : Subgroup (∀ i, G i) where
  carrier := {f | {i | f i ≠ 1}.Finite}
  one_mem' := by
    simp
  mul_mem' {f g} hf hg := by
    have h_union : ({i | f i ≠ 1} ∪ {i | g i ≠ 1}).Finite := hf.union hg
    refine h_union.subset ?_
    intro i hi
    have hi' : f i * g i ≠ 1 := by
      simpa [Pi.mul_apply] using hi
    simp
    by_cases hf_i : f i = 1
    · right
      intro hg_i
      apply hi'
      simp [hf_i, hg_i]
    · left; exact hf_i
  inv_mem' {f} hf := by
    dsimp
    simpa using hf

/-- An element `f` is in the external direct product iff its support
`{i | f i ≠ 1}` is finite. -/
theorem ExternalDirectProduct.mem_iff (f : ∀ i, G i) :
    f ∈ ExternalDirectProduct G ↔ {i | f i ≠ 1}.Finite := by
  rfl

/-- When the index set is finite, the external direct product coincides with the full
cartesian product (as a subgroup). That is, `ExternalDirectProduct G = ⊤`. -/
@[simp]
theorem ExternalDirectProduct.eq_top [Fintype ι] : ExternalDirectProduct (G := G) = ⊤ := by
  ext f
  refine ⟨fun _ => Subgroup.mem_top _, fun _ => ?_⟩
  dsimp [ExternalDirectProduct]
  simpa using Set.toFinite ({i : ι | f i ≠ 1} : Set ι)

/-- The projection of an element of the external direct product onto a single component. -/
def ExternalDirectProduct.proj (i : ι) : ExternalDirectProduct G →* G i :=
  (Pi.evalMonoidHom (f := G) i).comp (Subgroup.subtype (ExternalDirectProduct G))

/-- The inclusion of a single component into the external direct product.
Given `g : G i`, this returns the element that is `g` at index `i` and `1` everywhere else. -/
def ExternalDirectProduct.single [DecidableEq ι] (i : ι) : G i →* ExternalDirectProduct G where
  toFun g :=
    ⟨Pi.mulSingle i g, by
      have h_supp : {j | Pi.mulSingle i g j ≠ 1} ⊆ {i} := by
        intro j hj
        by_cases hij : j = i
        · simp [hij]
        · have h_one : Pi.mulSingle i g j = 1 := Pi.mulSingle_eq_of_ne hij g
          exfalso; exact hj h_one
      exact (Set.finite_singleton i).subset h_supp⟩
  map_one' := by
    apply Subtype.ext
    simp [Pi.mulSingle]
  map_mul' x y := by
    apply Subtype.ext
    simp [Pi.mulSingle_mul]

/-- The single-element embedding has the expected projection property: projecting at index `i`
after embedding gives back the original element. -/
@[simp]
theorem ExternalDirectProduct.proj_single [DecidableEq ι] (i : ι) (g : G i) :
    (ExternalDirectProduct.proj i) ((ExternalDirectProduct.single i) g) = g := by
  simp [ExternalDirectProduct.proj, ExternalDirectProduct.single]

/-- Projecting at a different index `j ≠ i` gives the identity. -/
@[simp]
theorem ExternalDirectProduct.proj_single_ne [DecidableEq ι] (i j : ι) (hij : j ≠ i) (g : G i) :
    (ExternalDirectProduct.proj j) ((ExternalDirectProduct.single i) g) = 1 := by
  simp [ExternalDirectProduct.proj, ExternalDirectProduct.single, Pi.mulSingle_eq_of_ne hij]

-- Examples

section Examples

/-- Example 1: When the index set is finite (e.g. `Fin 2`), every function belongs to the
external direct product, which equals the full cartesian product. -/
example [Fintype ι] (f : ∀ i, G i) : f ∈ ExternalDirectProduct G := by
  simp [ExternalDirectProduct.eq_top]

/-- Example 2: The constant identity function belongs to the external direct product
regardless of the size of the index set. -/
example : (1 : ∀ i, G i) ∈ ExternalDirectProduct G := by
  dsimp [ExternalDirectProduct]
  simp

/-- Example 3: In an infinite index set `ℕ`, a function that equals `1` except at finitely many
places belongs to the external direct product. -/
example [DecidableEq ℕ] (G0 : Type*) [Group G0] (a : G0) :
    (fun (n : ℕ) => if n = 0 then a else if n = 5 then a⁻¹ else 1) ∈
    ExternalDirectProduct (fun _ : ℕ => G0) := by
  dsimp [ExternalDirectProduct]
  have h_subset : {n : ℕ | (fun (n : ℕ) => if n = 0 then a else if n = 5 then a⁻¹ else 1) n ≠ 1}
      ⊆ ({0, 5} : Set ℕ) := by
    intro n hn
    simp at hn ⊢
    by_cases h0 : n = 0; · tauto
    by_cases h5 : n = 5; · tauto
    simp [h0, h5] at hn
  exact (Set.toFinite _).subset h_subset

/-- Example 4: When `ℕ` is the index set, a constant non-identity function is NOT in the
external direct product, because its support is all of `ℕ` (infinite). -/
example [DecidableEq ℕ] (G0 : Type*) [Group G0] (a : G0) (ha : a ≠ 1) :
    (fun (_ : ℕ) => a) ∉ ExternalDirectProduct (fun _ : ℕ => G0) := by
  intro h
  have h_finite : {i : ℕ | (fun (_ : ℕ) => a) i ≠ 1}.Finite := h
  have h_eq : {i : ℕ | (fun (_ : ℕ) => a) i ≠ 1} = Set.univ := by
    ext i; simp [ha]
  rw [h_eq] at h_finite
  exact Set.infinite_univ.not_finite h_finite

/-- Example 5: The product of two elements of the external direct product is again in
the external direct product (this follows from the subgroup structure). -/
example (f g : ∀ i, G i) (hf : f ∈ ExternalDirectProduct G) (hg : g ∈ ExternalDirectProduct G) :
    f * g ∈ ExternalDirectProduct G := by
  simpa using Subgroup.mul_mem _ hf hg

/-- Example 6: Using `single` to embed a group element and project it back. -/
example [DecidableEq ι] (i : ι) (g : G i) :
    (ExternalDirectProduct.proj i) ((ExternalDirectProduct.single i) g) = g := by
  simp

end Examples
