---
role: proof
locale: en
of_concept: sum-of-direct-limit-systems
source_book: gtm001
source_chapter: "17"
source_section: "17.2"
---

We need to define $i < j$ and $\pi_{ij}$ when $i \in I_1$ and $j \in I_2$. Define:

$$i < j \iff \xi_i \leq \eta_j \wedge \alpha_i \leq \beta_j \wedge \rho_{i\infty}^* P_i \subseteq \mathcal{W}(\theta_{j\infty}) \wedge$$
$$\sup \{ \rho_{i\infty}(v) + 1 \mid v < \xi_i \} \in \mathcal{W}(\theta_{j\infty}).$$

Observe that $\mathcal{W}(\rho_{i\infty}) = \rho_{i\infty}^* \xi_i = \rho_{i\infty}^* M^{\xi_i}(\alpha_i \cup P_i) \subseteq \mathcal{W}(\theta_{j\infty})$. Hence $\theta_{j\infty}^{-1} \circ \rho_{i\infty}$ is a medium $M$-map by Proposition 16.18, and we set $\pi_{ij} = \theta_{j\infty}^{-1} \circ \rho_{i\infty}$.
