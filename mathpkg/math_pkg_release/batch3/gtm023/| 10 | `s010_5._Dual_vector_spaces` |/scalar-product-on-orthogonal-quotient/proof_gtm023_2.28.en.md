---
role: proof
locale: en
of_concept: scalar-product-on-orthogonal-quotient
source_book: gtm023
source_chapter: "II"
source_section: "2.28"
---

The bilinear function is well-defined because if $\bar{x}_1 = \bar{x}_2$ in $E/E_1$, then $x_1 - x_2 \in E_1$, and since $x^* \in E_1^\perp$, we have $\langle x^*, x_1 - x_2 \rangle = 0$, so $\langle x^*, x_1 \rangle = \langle x^*, x_2 \rangle$.

To show non-degeneracy: if $x^* \in E_1^\perp$ satisfies $\langle x^*, \bar{x} \rangle = 0$ for all $\bar{x} \in E/E_1$, then $\langle x^*, x \rangle = 0$ for all $x \in E$, so $x^* = 0$. Conversely, if $\bar{x} \in E/E_1$ satisfies $\langle x^*, \bar{x} \rangle = 0$ for all $x^* \in E_1^\perp$, then $x \in (E_1^\perp)^\perp = E_1^{\perp\perp} = E_1$ by Proposition IV, so $\bar{x} = 0$.
