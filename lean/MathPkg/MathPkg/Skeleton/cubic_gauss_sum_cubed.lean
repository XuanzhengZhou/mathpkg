import Mathlib

open AddChar MulChar

/- Cubic Gauss sum cubed relation: If χ is a cubic character on a finite field F
   and ψ is a primitive additive character, then g(χ)³ = |F| · J(χ,χ). -/
theorem cubic_gauss_sum_cubed {F R' : Type*} [Field F] [Fintype F] [CommRing R'] [IsDomain R']
    (χ : MulChar F R') (hχ_cubic : χ ^ 3 = 1) (hχ_nontriv : χ ≠ 1)
    (ψ : AddChar F R') (hψ : ψ.IsPrimitive) :
    (gaussSum χ ψ) ^ 3 = (Fintype.card F : R') * jacobiSum χ χ := by
  sorry
