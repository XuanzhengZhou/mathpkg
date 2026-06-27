---
role: proof
locale: en
of_concept: orthogonal-vectors-linear-independence
source_book: gtm023
source_chapter: "7"
source_section: "7.3"
---

Consider the relation $\sum_v \lambda^v x_v = 0$. Taking the inner product with $x_\mu$ for a fixed index $\mu$ yields

$$\left(\sum_v \lambda^v x_v, x_\mu\right) = 0.$$

By bilinearity of the inner product,

$$\sum_v \lambda^v (x_v, x_\mu) = 0.$$

Since the vectors are pairwise orthogonal, $(x_v, x_\mu) = 0$ for $v \neq \mu$. Hence all terms in the sum vanish except the term with $v = \mu$, giving

$$\lambda^\mu (x_\mu, x_\mu) = 0 \quad (\mu = 1, \ldots, p).$$

By definiteness of the inner product, $(x_\mu, x_\mu) > 0$ since $x_\mu \neq 0$. Therefore $\lambda^\mu = 0$ for all $\mu = 1, \ldots, p$, proving linear independence.
