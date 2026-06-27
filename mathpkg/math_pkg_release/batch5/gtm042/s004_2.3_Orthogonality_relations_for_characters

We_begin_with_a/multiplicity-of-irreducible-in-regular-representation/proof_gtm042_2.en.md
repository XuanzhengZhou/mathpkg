---
role: proof
locale: en
of_concept: multiplicity-of-irreducible-in-regular-representation
source_book: gtm042
source_chapter: "2"
source_section: "2.4"
---

By Theorem 4, the multiplicity of an irreducible representation $W_i$ in the regular representation is $\langle r_G, \chi_i \rangle$. Using the formula for $r_G$ from Proposition 5,

$$\langle r_G, \chi_i \rangle = \frac{1}{g} \sum_{s \in G} r_G(s^{-1})\chi_i(s) = \frac{1}{g} \cdot r_G(1) \cdot \chi_i(1) = \frac{1}{g} \cdot g \cdot \chi_i(1) = \chi_i(1) = n_i,$$

since $r_G(s^{-1}) = 0$ for all $s \neq 1$, and $r_G(1) = g$. $\square$
