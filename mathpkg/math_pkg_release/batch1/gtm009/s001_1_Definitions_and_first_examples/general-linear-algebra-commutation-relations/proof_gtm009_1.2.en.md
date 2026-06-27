---
role: proof
locale: en
of_concept: general-linear-algebra-commutation-relations
source_book: gtm009
source_chapter: "I. Basic Concepts"
source_section: "1. Definitions and first examples"
---

For the standard basis matrices $e_{ij}$ (with 1 in position $(i,j)$ and 0 elsewhere), the associative product satisfies $e_{ij}e_{kl} = \delta_{jk}e_{il}$. This follows from matrix multiplication: the $(p,q)$-entry of $e_{ij}e_{kl}$ is $\sum_r (e_{ij})_{pr}(e_{kl})_{rq} = \delta_{pi}\delta_{rj} \cdot \delta_{rk}\delta_{lq} = \delta_{pi}\delta_{jk}\delta_{lq}$, which is 1 exactly when $p=i$, $j=k$, and $q=l$.

Therefore:
$$[e_{ij}, e_{kl}] = e_{ij}e_{kl} - e_{kl}e_{ij} = \delta_{jk}e_{il} - \delta_{li}e_{kj}.$$

All coefficients are indeed $0$ or $\pm 1$, so they belong to the prime field.
