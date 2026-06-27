---
role: proof
locale: en
of_concept: cramers-rule
source_book: gtm023
source_chapter: "4"
source_section: "4"
---

From the cofactor expansion formula (4.36) in the text, we have the relation

$$\xi^i \cdot \det A = \sum_j \beta_j^i \eta^j,$$

where $\beta_j^i = (-1)^{i+j} \det S_i^j = \operatorname{cof}(\alpha_i^j)$. Since $\det A \neq 0$, we can divide to obtain

$$\xi^i = \frac{1}{\det A} \sum_j \beta_j^i \eta^j = \frac{1}{\det A} \sum_j \operatorname{cof}(\alpha_i^j) \eta^j.$$

This formula follows from the identity $\sum_j \alpha_i^j \beta_j^k = \delta_i^k \det A$, which expresses the fact that the matrix $(\beta_j^i / \det A)$ is the inverse of $(\alpha_i^j)$.
