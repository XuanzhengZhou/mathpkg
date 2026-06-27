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
def innerAutomorphism (g : G) : MulAut G := by
  sorry
