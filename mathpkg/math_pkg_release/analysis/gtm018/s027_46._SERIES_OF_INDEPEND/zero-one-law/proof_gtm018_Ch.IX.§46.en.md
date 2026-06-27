---
role: proof
locale: en
of_concept: zero-one-law
source_book: gtm018
source_chapter: "IX. Probability"
source_section: "§46. Series of Independent Functions"
---

For every measurable set $F$, define $\nu(F) = \mu(E \cap F)$. If $F$ is a $J$-cylinder for a finite set $J \subset \mathbb{N}$ (so that $F$ depends only on coordinates in $J$), then, since $E$ is a $J_n$-cylinder for every $n$, we may choose $n$ large enough so that $J \subset \{1, \dots, n\}$. Then $E$ is a $J_{n}$-cylinder, meaning $E$ depends only on coordinates with index $> n$, while $F$ depends only on coordinates with index $\leq n$. By the independence structure of the product measure,

$$\nu(F) = \mu(E \cap F) = \mu(E) \mu(F).$$

Thus the signed measure $\nu$ and the measure $\mu(E) \cdot \mu$ agree on all finite-dimensional cylinder sets. Since a finite measure on the class of all measurable subsets of $X$ is uniquely determined by its values on such cylinders (these cylinders generate the product $\sigma$-algebra), the relation $\nu(F) = \mu(E) \mu(F)$ holds for all measurable sets $F$.

In particular, take $F = E$. Then

$$\mu(E) = \mu(E \cap E) = \nu(E) = \mu(E) \mu(E) = \mu(E)^2.$$

The equation $\mu(E) = \mu(E)^2$ implies $\mu(E) = 0$ or $\mu(E) = 1$.
