---
role: proof
locale: en
of_concept: basis-transformation-inverse-matrices
source_book: gtm023
source_chapter: "I"
source_section: "3.12"
---

Combining the two defining relations (3.22) and (3.23):

$$\bar{x}_v = \sum_{\mu} \alpha_v^\mu x_\mu, \qquad x_\mu = \sum_{\lambda} \check{\alpha}_\mu^\lambda \bar{x}_\lambda,$$

we obtain

$$\bar{x}_v = \sum_{\mu, \lambda} \alpha_v^\mu \check{\alpha}_\mu^\lambda \bar{x}_\lambda.$$

This is equivalent to

$$\sum_{\lambda} \left( \sum_{\mu} \alpha_v^\mu \check{\alpha}_\mu^\lambda - \delta_v^\lambda \right) \bar{x}_\lambda = 0.$$

Since the vectors $\bar{x}_\lambda$ are linearly independent, it follows that

$$\sum_{\mu} \alpha_v^\mu \check{\alpha}_\mu^\lambda = \delta_v^\lambda.$$

In a similar way, combining the relations in reverse order yields

$$\sum_{\mu} \check{\alpha}_v^\mu \alpha_\mu^\lambda = \delta_v^\lambda.$$

Thus the two matrices are inverse to each other.
