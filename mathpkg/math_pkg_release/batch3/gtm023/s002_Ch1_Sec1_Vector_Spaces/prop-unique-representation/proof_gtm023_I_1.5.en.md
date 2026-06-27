---
role: proof
locale: en
of_concept: prop-unique-representation
source_book: gtm023
source_chapter: "I"
source_section: "1.5"
---

First suppose the scalars in (1.4) are uniquely determined by $x$. Setting $x = 0$ we have $\sum_\alpha 0 \cdot x_\alpha = 0$. By uniqueness, this is the only representation of $0$, so $\sum_\alpha \lambda^\alpha x_\alpha = 0$ forces $\lambda^\alpha = 0$ for all $\alpha$. Hence the $x_\alpha$ are linearly independent.

Conversely, suppose the $x_\alpha$ are linearly independent and consider two representations
$$x = \sum_\alpha \lambda^\alpha x_\alpha = \sum_\alpha \mu^\alpha x_\alpha.$$
Subtracting,
$$\sum_\alpha (\lambda^\alpha - \mu^\alpha)x_\alpha = 0.$$
By linear independence, $\lambda^\alpha - \mu^\alpha = 0$ for all $\alpha$, i.e., $\lambda^\alpha = \mu^\alpha$.
