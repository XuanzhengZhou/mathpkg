import Mathlib

open scoped MonomialOrder

/-!
# Artinian property of monomial orders

Let `S` be a Noetherian ring and `F` a free `S`-module with a finite basis.
Then any monomial order on `F` is **Artinian** — every nonempty subset of monomials
has a least element with respect to the order.  Equivalently, there are no infinite
strictly descending chains of monomials under the monomial order.

This is a fundamental lemma in Gröbner basis theory: the Artinian (well-founded)
property guarantees that algorithms such as Buchberger's algorithm terminate.

## Dependencies

* `MonomialOrder σ` — monomial order on exponent vectors `σ →₀ ℕ`
* `IsNoetherianRing S` — the Noetherian property of the base ring `S`

## Main statement

* `artinian_property_of_monomial_orders` : the strict order `≺[m]` is well-founded,
  i.e., `WellFounded (· ≺[m] ·)`.
-/

/-- Any monomial order on a free module with a finite basis over a Noetherian ring
is Artinian (well-founded): the strict order `≺[m]` admits no infinite strictly
descending chains. -/
lemma artinian_property_of_monomial_orders {S : Type*} [CommRing S] [IsNoetherianRing S]
    {σ : Type*} [Fintype σ] (m : MonomialOrder σ) :
    WellFounded (fun (a b : σ →₀ ℕ) => a ≺[m] b) := by
  sorry
