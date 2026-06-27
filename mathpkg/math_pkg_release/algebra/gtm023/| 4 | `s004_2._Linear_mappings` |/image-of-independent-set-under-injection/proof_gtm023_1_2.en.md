---
role: proof
locale: en
of_concept: image-of-independent-set-under-injection
source_book: gtm023
source_chapter: "1"
source_section: "2"
---

Consider a linear relation among the images:
$$
\sum_i \lambda^i \varphi x_i = 0, \quad x_i \in S.
$$
By linearity, $\sum_i \lambda^i \varphi x_i = \varphi\left(\sum_i \lambda^i x_i\right)$, so
$$
\varphi\left(\sum_i \lambda^i x_i\right) = 0.
$$
Since $\varphi$ is injective, $\sum_i \lambda^i x_i = 0$. Because the vectors $x_i \in S$ are linearly independent, it follows that $\lambda^i = 0$ for all $i$. Hence $\varphi(S)$ is a linearly independent set.
