---
role: proof
locale: en
of_concept: prop-linear-dependence-characterization
source_book: gtm023
source_chapter: "I"
source_section: "1.4"
---

Suppose the family $(x_\alpha)$ is linearly dependent. Then there exist scalars $\lambda^\alpha$, not all zero, with $\sum_\alpha \lambda^\alpha x_\alpha = 0$. Choose $\beta$ such that $\lambda^\beta \neq 0$. Then
$$\lambda^\beta x_\beta = -\sum_{\alpha \neq \beta} \lambda^\alpha x_\alpha.$$
Multiplying by $(\lambda^\beta)^{-1}$ gives
$$x_\beta = -\sum_{\alpha \neq \beta} (\lambda^\beta)^{-1}\lambda^\alpha x_\alpha,$$
expressing $x_\beta$ as a linear combination of the remaining vectors.

Conversely, if $x_\beta = \sum_{\alpha \neq \beta} \mu^\alpha x_\alpha$, then setting $\lambda^\beta = -1$ gives
$$\sum_\alpha \lambda^\alpha x_\alpha = 0$$
with $\lambda^\beta \neq 0$, so the family is linearly dependent.
