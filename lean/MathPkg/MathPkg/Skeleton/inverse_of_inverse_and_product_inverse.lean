import Mathlib

/-!
# Inverse of Inverse and Product Inverse (Proposition 2.2)

In a multiplicative group G:

(i) `(x⁻¹)⁻¹ = x` — the inverse of the inverse is the original element.

(ii) `(x₁ x₂ ⋯ xₙ)⁻¹ = xₙ⁻¹ ⋯ x₂⁻¹ x₁⁻¹` — the inverse of a product
is the product of the inverses in reverse order.

For (ii), we express this via `List G`. Reversing the list and then taking
the inverse of each element produces the reversed product of inverses.
-/

section inverse_of_inverse_and_product_inverse

/-- **Proposition 2.2**: In a multiplicative group G:

(i) The inverse of the inverse of an element is the original element.
(ii) The inverse of a finite product is the product of the inverses taken
in reverse order (expressed here for any list of group elements).

Both statements are of fundamental importance in group theory. -/
theorem inverse_of_inverse_and_product_inverse {G : Type*} [Group G] :
    (∀ x : G, x⁻¹⁻¹ = x) ∧ (∀ (L : List G), L.prod⁻¹ = (L.reverse.map (·⁻¹)).prod) := by
  sorry
