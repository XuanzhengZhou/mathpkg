---
role: proof
locale: en
of_concept: product-of-orthogonal-projections-vanishes-iff-subspaces-orthogonal
source_book: gtm023
source_chapter: "VIII"
source_section: "8.11"
---

Assume first that $E_1 \perp E_2$. Then for any $x \in E$, $\pi_1 x \in E_1$, and since $E_1 \subset E_2^\perp$, we have $\pi_1 x \in E_2^\perp$. Hence $\pi_2(\pi_1 x) = 0$, so $\pi_2 \circ \pi_1 = 0$.

Conversely, assume $\pi_2 \circ \pi_1 = 0$. Then for every $x \in E$, $\pi_2(\pi_1 x) = 0$, which means $\pi_1 x \in \ker \pi_2 = E_2^\perp$. In particular, for any $y \in E_1$, $y = \pi_1 y \in E_2^\perp$, so $E_1 \subset E_2^\perp$, i.e., $E_1 \perp E_2$.
