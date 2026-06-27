---
role: proof
locale: en
of_concept: adjointness-of-d-and-e
source_book: gtm042
source_chapter: "15"
source_section: "15.4"
---

We can assume that $x = [\overline{X}]$, where $X$ is a projective $A[G]$-module, and that $y = [K \otimes_A Y]$, where $Y$ is an $A[G]$-module which is $A$-free. The $A$-module $\operatorname{Hom}^G(X, Y)$ is then free; let $r$ be its rank.

Then we have canonical isomorphisms:

$$K \otimes_A \operatorname{Hom}^G(X, Y) \cong \operatorname{Hom}^G(K \otimes_A X, K \otimes_A Y)$$

and

$$k \otimes_A \operatorname{Hom}^G(X, Y) \cong \operatorname{Hom}^G(k \otimes_A X, k \otimes_A Y).$$

Now, by definition of the bilinear forms in 14.5, we have:

$$\langle e(x), y \rangle_K = \langle [K \otimes_A X], [K \otimes_A Y] \rangle_K = \dim_K \operatorname{Hom}^G(K \otimes_A X, K \otimes_A Y).$$

By the first isomorphism above, this equals $\dim_K (K \otimes_A \operatorname{Hom}^G(X, Y)) = r$, since $\operatorname{Hom}^G(X, Y)$ is free of rank $r$ over $A$.

Similarly,

$$\langle x, d(y) \rangle_k = \langle [\overline{X}], [k \otimes_K (K \otimes_A Y)] \rangle_k = \langle [k \otimes_A X], [k \otimes_A Y] \rangle_k = \dim_k \operatorname{Hom}^G(k \otimes_A X, k \otimes_A Y).$$

By the second isomorphism, this equals $\dim_k (k \otimes_A \operatorname{Hom}^G(X, Y)) = r$.

Therefore $\langle e(x), y \rangle_K = r = \langle x, d(y) \rangle_k$, proving the adjointness relation.
