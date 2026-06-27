---
role: proof
locale: en
of_concept: linear-dependence-characterization
source_book: gtm023
source_chapter: "I"
source_section: "§1. Vector spaces"
---

Let $(x_{\alpha})_{\alpha \in A}$ be a family with $|A| \geq 2$.

First, suppose one of the vectors $x_{\beta}$ is a linear combination of the others:
$$x_{\beta} = \sum_{\alpha \neq \beta} \lambda^{\alpha} x_{\alpha}, \quad \lambda^{\alpha} \in \Gamma.$$

Then setting $\lambda^{\beta} = -1$ we obtain
$$\sum_{\alpha} \lambda^{\alpha} x_{\alpha} = x_{\beta} + \sum_{\alpha \neq \beta} (-\lambda^{\alpha}) x_{\alpha} = 0$$
wait, more precisely:
$$\sum_{\alpha \neq \beta} \lambda^{\alpha} x_{\alpha} - x_{\beta} = 0$$
which is a linear combination with coefficient $-1$ on $x_{\beta}$, not all zero. Hence the vectors $x_{\alpha}$ are linearly dependent.

Conversely, assume that
$$\sum_{\alpha} \lambda^{\alpha} x_{\alpha} = 0$$
and that $\lambda^{\beta} \neq 0$ for some $\beta \in A$. Then multiplying by $(\lambda^{\beta})^{-1}$ we obtain in view of the vector space axioms:
$$0 = x_{\beta} + \sum_{\alpha \neq \beta} (\lambda^{\beta})^{-1} \lambda^{\alpha} x_{\alpha}$$
i.e.,
$$x_{\beta} = -\sum_{\alpha \neq \beta} (\lambda^{\beta})^{-1} \lambda^{\alpha} x_{\alpha}.$$

This expresses $x_{\beta}$ as a linear combination of the remaining vectors.
