---
role: proof
locale: en
of_concept: regular-matrix-generates-basis
source_book: gtm023
source_chapter: "I"
source_section: "3.12"
---

To show that the vectors $\bar{x}_v$ are linearly independent, assume that

$$\sum_{v} \lambda^v \bar{x}_v = 0.$$

Substituting $\bar{x}_v = \sum_{\mu} \alpha_v^\mu x_\mu$, we obtain

$$\sum_{v, \mu} \lambda^v \alpha_v^\mu x_\mu = 0.$$

In view of the linear independence of the vectors $x_\mu$, it follows that

$$\sum_{v} \lambda^v \alpha_v^\mu = 0 \quad (\mu = 1 \ldots n).$$

Multiplying with the inverse matrix $(\check{\alpha}_\kappa^\mu)$, which exists because $(\alpha_v^\mu)$ is regular, yields

$$\sum_{v, \mu} \lambda^v \alpha_v^\mu \check{\alpha}_\kappa^\mu = \sum_{v} \lambda^v \delta_\kappa^v = \lambda^\kappa = 0 \quad (\kappa = 1 \ldots n).$$

Thus all coefficients $\lambda^v$ vanish, proving that the vectors $\bar{x}_v$ are linearly independent. Since they number $n = \dim E$, they form a basis of $E$.
