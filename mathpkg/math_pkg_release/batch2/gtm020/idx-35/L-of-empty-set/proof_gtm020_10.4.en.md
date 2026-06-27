---
role: proof
locale: en
of_concept: L-of-empty-set
source_book: gtm020
source_chapter: "10. Relative K-Theory"
source_section: "4"
---

When $A = \emptyset$, every vector bundle morphism restricts to an isomorphism over $A$ (vacuously), so $S(X,\emptyset)$ consists of all morphisms $\alpha: \xi_0 \to \xi_1$ without restriction conditions. The isomorphism classes in $S(X,\emptyset)$ are determined solely by the isomorphism classes of the domain and codomain bundles, giving $S(X,\emptyset) = \text{Vect}_F(X) \times \text{Vect}_F(X)$.

Two pairs $(\xi_0, \xi_1)$ and $(\eta_0, \eta_1)$ determine the same element in $L(X,\emptyset)$ if there exist bundles $\zeta_1, \zeta_2$ with $\xi_i \oplus \zeta_1 \cong \eta_i \oplus \zeta_2$ for $i = 0, 1$. This means $\xi_0 \oplus \eta_1 \oplus (\zeta_1 \oplus \zeta_2) \cong \xi_1 \oplus \eta_0 \oplus (\zeta_1 \oplus \zeta_2)$, which is precisely the $s$-equivalence relation used in the Grothendieck construction of $K(X)$.
