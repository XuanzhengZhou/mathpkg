role: proof
locale: en
of_concept: continuity-of-matrix-operations
source_book: gtm031
source_chapter: "VI"
source_section: "11"
---
We observe that the $(i, j)$ element of the sum $(\alpha) + (\beta)$ is $\alpha_{ij} + \beta_{ij}$, which is a continuous function of the $2n^2$ coordinates $\alpha_{ij}, \beta_{ij}$. Similarly, the $(i, j)$ element of the product $(\alpha)(\beta)$ is $\sum_{k=1}^{n} \alpha_{ik} \beta_{kj}$, which is also a continuous function (a polynomial) of the $2n^2$ coordinates. Since limits commute with continuous functions, the convergence of the sequences $(\alpha^{(k)})$ and $(\beta^{(k)})$ implies the convergence of the sum and product sequences to the respective limits.

For the similarity transformation, the map $(\alpha) \mapsto (\mu)(\alpha)(\mu)^{-1}$ is a composition of two multiplications (by $(\mu)$ on the left and by $(\mu)^{-1}$ on the right), each of which is continuous by the product continuity established above. Hence the similarity transformation preserves convergence.
