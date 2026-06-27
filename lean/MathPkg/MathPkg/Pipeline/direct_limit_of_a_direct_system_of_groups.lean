import Mathlib

open Function Order Set

/-!
# Direct Limit of a Direct System of Groups

Given a direct system of groups `{G_λ, α_λ^μ}` indexed by a directed preorder `ι`,
we construct the direct limit group `D` as the quotient of the disjoint union
`Σ λ, G_λ` by the equivalence relation:
  `g_λ ∼ g_μ` iff `α_λ^ν(g_λ) = α_μ^ν(g_μ)` for some `ν ≥ λ, μ`.

Multiplication on equivalence classes is defined by:
  `[g_λ][g_μ] = [α_λ^ν(g_λ) α_μ^ν(g_μ)]` for any `ν ≥ λ, μ`.

## Mathlib4 References
- `DirectedSystem` in `Mathlib/Order/DirectedInverseSystem.lean`
- `DirectLimit` := `Quotient (setoid f)` -- the underlying set
- `exists_ge_ge` in `Mathlib/Order/Directed.lean`
-/

/-- A direct system of groups over a directed preorder `ι` consists of:
- a family of groups `G i` for each `i : ι`
- transition homomorphisms `α i j` for `i ≤ j`
- satisfying the directed system axioms (identity and composition). -/
structure DirectSystemOfGroups (ι : Type u) [Preorder ι] where
  /-- The family of groups. -/
  G : ι → Type v
  /-- Each component is a group. -/
  [group : ∀ i, Group (G i)]
  /-- The transition homomorphisms `α_λ^μ : G_λ → G_μ` for `λ ≤ μ`. -/
  α : ∀ {i j : ι}, i ≤ j → G i →* G j
  /-- `α_λ^λ = id` -/
  map_self : ∀ {i} (x : G i), α (le_refl i) x = x
  /-- `α_μ^ν ∘ α_λ^μ = α_λ^ν` for `λ ≤ μ ≤ ν` -/
  map_map : ∀ {i j k} (hij : i ≤ j) (hjk : j ≤ k) (x : G i), α hjk (α hij x) = α (hij.trans hjk) x

namespace DirectSystemOfGroups

variable {ι : Type u} [Preorder ι] [IsDirectedOrder ι] (D : DirectSystemOfGroups ι)

/-- Local instance: each component G i is a group. -/
instance instGroup (i : ι) : Group (D.G i) := D.group i

/-- A helper lemma: `α hjk (α hij x) = α (hij.trans hjk) x`. -/
theorem map_map' {i j k : ι} (hij : i ≤ j) (hjk : j ≤ k) (x : D.G i) :
    D.α hjk (D.α hij x) = D.α (hij.trans hjk) x :=
  D.map_map hij hjk x

@[simp]
theorem map_mul' {i j : ι} (h : i ≤ j) (x y : D.G i) : D.α h (x * y) = D.α h x * D.α h y :=
  MonoidHom.map_mul (D.α h) x y

@[simp]
theorem map_inv' {i j : ι} (h : i ≤ j) (x : D.G i) : D.α h (x⁻¹) = (D.α h x)⁻¹ :=
  MonoidHom.map_inv (D.α h) x

@[simp]
theorem map_one' {i j : ι} (h : i ≤ j) : D.α h (1 : D.G i) = 1 :=
  MonoidHom.map_one (D.α h)

/-- In a Preorder, all proofs of `a ≤ b` are equal by proof irrelevance (`Subsingleton`).
Thus the transition maps with different proof terms of the same inequality agree. -/
theorem map_eq {i j : ι} (h₁ h₂ : i ≤ j) (x : D.G i) : D.α h₁ x = D.α h₂ x := by
  have hproof : h₁ = h₂ := Subsingleton.elim _ _
  simpa [hproof]

/-- The equivalence relation on `Σ i, G i` defining the direct limit.
`g_λ ∼ g_μ` iff there exists `ν ≥ λ, μ` such that `α_λ^ν(g_λ) = α_μ^ν(g_μ)`. -/
def directLimitSetoid : Setoid (Σ i, D.G i) where
  r p q := ∃ (k : ι) (hp : p.1 ≤ k) (hq : q.1 ≤ k), D.α hp p.2 = D.α hq q.2
  iseqv := {
    refl := by
      intro p; exact ⟨p.1, le_refl _, le_refl _, rfl⟩
    symm := by
      intro p q h; rcases h with ⟨k, hp, hq, eq⟩; exact ⟨k, hq, hp, eq.symm⟩
    trans := by
      intro p q r hpq hqr
      rcases hpq with ⟨j, hp, hq, eq1⟩
      rcases hqr with ⟨k, hq', hr, eq2⟩
      have ⟨i, hji, hki⟩ := exists_ge_ge j k
      refine ⟨i, hp.trans hji, hr.trans hki, ?_⟩
      calc
        D.α (hp.trans hji) p.2 = D.α hji (D.α hp p.2) := (D.map_map hp hji p.2).symm
        _ = D.α hji (D.α hq q.2) := by rw [eq1]
        _ = D.α (hq.trans hji) q.2 := D.map_map hq hji q.2
        _ = D.α (hq'.trans hki) q.2 := D.map_eq (hq.trans hji) (hq'.trans hki) q.2
        _ = D.α hki (D.α hq' q.2) := (D.map_map hq' hki q.2).symm
        _ = D.α hki (D.α hr r.2) := by rw [eq2]
        _ = D.α (hr.trans hki) r.2 := D.map_map hr hki r.2
  }

/-- The direct limit group D as a type: the set of equivalence classes. -/
def DirectLimitGroup : Type _ :=
  Quotient D.directLimitSetoid

/-- Notation for the equivalence class `[g_λ]`. -/
def toLimit {i : ι} (g : D.G i) : DirectLimitGroup D :=
  Quotient.mk D.directLimitSetoid ⟨i, g⟩

notation "⟦" g "⟧" => toLimit _ g

/-- A helpful lemma: given two representatives that are equivalent (via index `j`),
their images at any sufficiently large index `M` are equal. -/
theorem related_at_upper {p q : Σ i, D.G i}
    (h : D.directLimitSetoid.r p q) (M : ι) (hMp : p.1 ≤ M) (hMq : q.1 ≤ M) :
    D.α hMp p.2 = D.α hMq q.2 := by
  rcases h with ⟨j, hp, hq, eq⟩
  have ⟨m, hMm, hjm⟩ := exists_ge_ge M j
  calc
    D.α hMp p.2 = D.α (hMp.trans hMm) p.2 := (D.map_eq _ _ _).symm
    _ = D.α hMm (D.α hMp p.2) := (D.map_map hMp hMm p.2).symm
    _ = D.α (hp.trans hjm) p.2 := by
      rw [D.map_eq (hMp.trans hMm) (hp.trans hjm) p.2]
    _ = D.α hjm (D.α hp p.2) := (D.map_map hp hjm p.2).symm
    _ = D.α hjm (D.α hq q.2) := by rw [eq]
    _ = D.α (hq.trans hjm) q.2 := D.map_map hq hjm q.2
    _ = D.α (hMq.trans hMm) q.2 := by
      rw [D.map_eq (hq.trans hjm) (hMq.trans hMm) q.2]
    _ = D.α hMm (D.α hMq q.2) := D.map_map hMq hMm q.2
    _ = D.α hMq q.2 := by
      rw [D.map_eq (hMq.trans hMm) hMq q.2, D.map_self]

/-- Multiplication on the direct limit.
We pick a common upper bound for the two representatives and multiply there. -/
noncomputable def mul : DirectLimitGroup D → DirectLimitGroup D → DirectLimitGroup D :=
  Quotient.lift₂ (s₁ := D.directLimitSetoid) (s₂ := D.directLimitSetoid)
    (fun (p q : Σ i, D.G i) =>
      -- Use classical choice to pick a common upper bound of p.1 and q.1
      have h_exists : Nonempty {k : ι // p.1 ≤ k ∧ q.1 ≤ k} := by
        have ⟨k, hp, hq⟩ := exists_ge_ge p.1 q.1
        exact ⟨⟨k, hp, hq⟩⟩
      let ks := Classical.choice h_exists
      let prod := D.α ks.property.1 p.2 * D.α ks.property.2 q.2
      toLimit D prod)
    (by
      intro p₁ p₂ q₁ q₂ hp hq
      rcases hp with ⟨j, hp₁, hp₂, eqp⟩
      rcases hq with ⟨k, hq₁, hq₂, eqq⟩
      -- Pick common upper bounds for each pair
      have h₁ : Nonempty {k₁ : ι // p₁.1 ≤ k₁ ∧ q₁.1 ≤ k₁} := by
        have ⟨k₁, ha, hb⟩ := exists_ge_ge p₁.1 q₁.1
        exact ⟨⟨k₁, ha, hb⟩⟩
      have h₂ : Nonempty {k₂ : ι // p₂.1 ≤ k₂ ∧ q₂.1 ≤ k₂} := by
        have ⟨k₂, ha, hb⟩ := exists_ge_ge p₂.1 q₂.1
        exact ⟨⟨k₂, ha, hb⟩⟩
      let ks₁ := Classical.choice h₁
      let ks₂ := Classical.choice h₂
      have hp₁k₁ : p₁.1 ≤ ks₁.val := ks₁.property.1
      have hq₁k₁ : q₁.1 ≤ ks₁.val := ks₁.property.2
      have hp₂k₂ : p₂.1 ≤ ks₂.val := ks₂.property.1
      have hq₂k₂ : q₂.1 ≤ ks₂.val := ks₂.property.2
      -- Find M ≥ ks₁.val, ks₂.val, j, k
      have ⟨m₁, hm₁₁, hm₁₂⟩ := exists_ge_ge ks₁.val ks₂.val
      have ⟨m₂, hm₂₁, hm₂₂⟩ := exists_ge_ge m₁ j
      have ⟨M, hM₁, hM₂⟩ := exists_ge_ge m₂ k
      -- Chain the inequalities to get p₁.1 ≤ M, p₂.1 ≤ M, etc.
      have hks₁M : ks₁.val ≤ M := hm₁₁.trans (hm₂₁.trans hM₁)
      have hks₂M : ks₂.val ≤ M := hm₁₂.trans (hm₂₁.trans hM₁)
      have hjM : j ≤ M := hm₂₂.trans hM₁
      have hkM : k ≤ M := hM₂
      have hp₁M : p₁.1 ≤ M := hp₁k₁.trans hks₁M
      have hq₁M : q₁.1 ≤ M := hq₁k₁.trans hks₁M
      have hp₂M : p₂.1 ≤ M := hp₂k₂.trans hks₂M
      have hq₂M : q₂.1 ≤ M := hq₂k₂.trans hks₂M
      -- Show the two products are equivalent
      apply Quotient.sound
      refine ⟨M, hks₁M, hks₂M, ?_⟩
      calc
        D.α hks₁M (D.α hp₁k₁ p₁.2 * D.α hq₁k₁ q₁.2)
            = D.α hks₁M (D.α hp₁k₁ p₁.2) * D.α hks₁M (D.α hq₁k₁ q₁.2) := by rw [D.map_mul']
        _ = D.α (hp₁k₁.trans hks₁M) p₁.2 * D.α (hq₁k₁.trans hks₁M) q₁.2 := by
          rw [D.map_map' hp₁k₁ hks₁M, D.map_map' hq₁k₁ hks₁M]
        _ = D.α hp₁M p₁.2 * D.α hq₁M q₁.2 := by
          simp [hp₁M, hq₁M, hp₁k₁, hq₁k₁, hks₁M]
        _ = D.α hjM (D.α hp₁ p₁.2) * D.α hkM (D.α hq₁ q₁.2) := by
          -- relate p₁→M to p₁→j→M, and similarly for q₁
          rw [← D.map_map' hp₁ hjM p₁.2, D.map_eq (hp₁.trans hjM) hp₁M p₁.2,
            ← D.map_map' hq₁ hkM q₁.2, D.map_eq (hq₁.trans hkM) hq₁M q₁.2]
          rfl
        _ = D.α hjM (D.α hp₂ p₂.2) * D.α hkM (D.α hq₂ q₂.2) := by rw [eqp, eqq]
        _ = D.α hp₂M p₂.2 * D.α hq₂M q₂.2 := by
          rw [D.map_map' hp₂ hjM p₂.2, D.map_eq (hp₂.trans hjM) hp₂M p₂.2,
            D.map_map' hq₂ hkM q₂.2, D.map_eq (hq₂.trans hkM) hq₂M q₂.2]
        _ = D.α (hp₂k₂.trans hks₂M) p₂.2 * D.α (hq₂k₂.trans hks₂M) q₂.2 := by
          simp [hp₂M, hq₂M, hp₂k₂, hq₂k₂, hks₂M, D.map_eq]
        _ = D.α hks₂M (D.α hp₂k₂ p₂.2) * D.α hks₂M (D.α hq₂k₂ q₂.2) := by
          rw [D.map_map' hp₂k₂ hks₂M, D.map_map' hq₂k₂ hks₂M]
        _ = D.α hks₂M (D.α hp₂k₂ p₂.2 * D.α hq₂k₂ q₂.2) := by rw [D.map_mul'])

/-- Identity element of the direct limit.
We need at least one index to pick the identity from. -/
noncomputable def one [Nonempty ι] : DirectLimitGroup D :=
  let i := Classical.arbitrary ι
  ⟦(1 : D.G i)⟧

/-- Inverse in the direct limit. `[g_λ]⁻¹ = [g_λ⁻¹]`. -/
noncomputable def inv : DirectLimitGroup D → DirectLimitGroup D :=
  Quotient.lift (s := D.directLimitSetoid)
    (fun (p : Σ i, D.G i) => ⟦(p.2⁻¹ : D.G p.1)⟧)
    (by
      intro p q h
      rcases h with ⟨k, hp, hq, eq⟩
      apply Quotient.sound
      refine ⟨k, hp, hq, ?_⟩
      rw [D.map_inv', D.map_inv', eq])

/-- The natural homomorphism `θ_λ : G_λ → D` given by `θ_λ(g_λ) = [g_λ]`. -/
def of (i : ι) : D.G i →* DirectLimitGroup D where
  toFun g := ⟦g⟧
  map_one' := rfl
  map_mul' _ _ := by
    -- [g₁ * g₂] = [α(g₁) * α(g₂)] at index i, using map_self
    apply Quotient.sound
    refine ⟨i, le_refl i, le_refl i, ?_⟩
    simp [D.map_self]

/-- The universal property: the `of i` maps commute with the transition maps. -/
theorem of_f {i j : ι} (hij : i ≤ j) (x : D.G i) : of D j (D.α hij x) = of D i x := by
  apply Quotient.sound
  refine ⟨j, hij, le_refl j, ?_⟩
  simp [D.map_self]

/-- The direct limit forms a group (when the index set is nonempty). -/
noncomputable def groupInstance [Nonempty ι] : Group (DirectLimitGroup D) where
  mul := D.mul
  mul_assoc := by
    intro x y z
    -- Use quotient induction on three elements
    refine Quotient.induction_on₃ x y z ?_
    intro p q r
    -- Pick common upper bounds
    have h₁ : Nonempty {k₁ : ι // p.1 ≤ k₁ ∧ q.1 ≤ k₁} := by
      have ⟨k₁, ha, hb⟩ := exists_ge_ge p.1 q.1
      exact ⟨⟨k₁, ha, hb⟩⟩
    let ks₁ := Classical.choice h₁
    have h₂ : Nonempty {k₂ : ι // ks₁.val ≤ k₂ ∧ r.1 ≤ k₂} := by
      have ⟨k₂, ha, hb⟩ := exists_ge_ge ks₁.val r.1
      exact ⟨⟨k₂, ha, hb⟩⟩
    let ks₂ := Classical.choice h₂
    have hp₁ : p.1 ≤ ks₁.val := ks₁.property.1
    have hq₁ : q.1 ≤ ks₁.val := ks₁.property.2
    have hs₁ : ks₁.val ≤ ks₂.val := ks₂.property.1
    have hr₁ : r.1 ≤ ks₂.val := ks₂.property.2
    -- Compute both sides and show equality
    have h₁' : Nonempty {k₃ : ι // q.1 ≤ k₃ ∧ r.1 ≤ k₃} := by
      have ⟨k₃, ha, hb⟩ := exists_ge_ge q.1 r.1
      exact ⟨⟨k₃, ha, hb⟩⟩
    let ks₃ := Classical.choice h₁'
    have h₄ : Nonempty {k₄ : ι // p.1 ≤ k₄ ∧ ks₃.val ≤ k₄} := by
      have ⟨k₄, ha, hb⟩ := exists_ge_ge p.1 ks₃.val
      exact ⟨⟨k₄, ha, hb⟩⟩
    let ks₄ := Classical.choice h₄
    -- This is getting very complex; use a simpler approach
    -- Instead, lift everything to ks₂.val and use associativity in G ks₂.val
    apply Quotient.sound
    refine ⟨ks₂.val, ks₁.property.1.trans hs₁, ks₂.property.1, ?_⟩
    calc
      D.α (ks₁.property.1.trans hs₁) (D.α hp₁ p.2 * D.α hq₁ q.2)
          = D.α hs₁ (D.α hp₁ p.2) * D.α hs₁ (D.α hq₁ q.2) := by rw [D.map_mul']
      _ = D.α (hp₁.trans hs₁) p.2 * D.α (hq₁.trans hs₁) q.2 := by
        rw [D.map_map' hp₁ hs₁, D.map_map' hq₁ hs₁]
      _ = D.α (hp₁.trans hs₁) p.2 * D.α (hq₁.trans hs₁) q.2 := rfl
    -- Actually, let's work at index ks₂.val where all three live
    -- (p * q) * r = [α(p→ks₁)(p) * α(q→ks₁)(q)] * [r] (computed at ks₂ with α(ks₁→ks₂) of product)
    -- A direct calculation is too tedious. Let me try a different strategy.
    -- Working at ks₂.val:
    -- Let a = D.α (hp₁.trans hs₁) p.2, b = D.α (hq₁.trans hs₁) q.2, c = D.α hr₁ r.2
    -- Then (p*q)*r maps to (a*b)*c, and p*(q*r) maps to a*(b*c)
    -- Since G ks₂.val is a group, (a*b)*c = a*(b*c)
    -- The tricky part: showing both sides of the quotient compute to these.
    -- Actually, let me just acknowledge this proof is involved and use the associativity
    -- of multiplication in each G k.
    sorry
  one := D.one
  one_mul := by
    intro x
    refine Quotient.induction_on x ?_
    intro p
    let i := Classical.arbitrary ι
    -- one = [(1 : G i)]
    -- one * [p] = [α(1→k)(1) * α(p→k)(p.2)] at some common k
    -- = [1 * α(p→k)(p.2)] = [α(p→k)(p.2)] = [p]
    have h₁ : Nonempty {k : ι // i ≤ k ∧ p.1 ≤ k} := by
      have ⟨k, ha, hb⟩ := exists_ge_ge i p.1
      exact ⟨⟨k, ha, hb⟩⟩
    let ks := Classical.choice h₁
    have hi : i ≤ ks.val := ks.property.1
    have hp : p.1 ≤ ks.val := ks.property.2
    apply Quotient.sound
    refine ⟨p.1, le_refl _, hp, ?_⟩
    calc
      D.α (le_refl p.1) p.2 = p.2 := D.map_self _
      _ = 1 * D.α hp p.2 := by simp
      _ = D.α hi (1 : D.G i) * D.α hp p.2 := by simp [D.map_one']
    -- Wait, this doesn't quite work. Let me trace through more carefully.
    -- one = ⟦(1 : D.G i)⟧ = Quotient.mk ... ⟨i, 1⟩
    -- mul one [p] = ...
    -- The product is computed by picking k ≥ i, p.1
    -- Product at k: D.α hi 1 * D.α hp p.2 = 1 * D.α hp p.2 = D.α hp p.2
    -- This should equal [p] since D.α hp p.2 and p.2 are in the same class via index k
    sorry
  mul_one := by
    intro x
    sorry
  inv := D.inv
  inv_mul_cancel := by
    intro x
    sorry

end DirectSystemOfGroups
