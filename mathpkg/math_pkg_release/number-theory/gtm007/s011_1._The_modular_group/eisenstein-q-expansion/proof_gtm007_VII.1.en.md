---
role: proof
locale: en
of_concept: eisenstein-q-expansion
source_book: gtm007
source_chapter: "VII"
source_section: "§1. The modular group"
---

The proof uses the identity (for $\operatorname{Im}(z) > 0$):
$$
\sum_{m \in \mathbf{Z}} \frac{1}{(mz+n)^k} = \frac{(-2\pi i)^k}{(k-1)!} \sum_{r=1}^\infty r^{k-1} e^{2\pi i r n z},
$$
valid for $k \geq 2$. Summing over $n \neq 0$ gives the $q$-expansion. The constant term $2\zeta(k)$ comes from the $n = 0$, $m \neq 0$ terms. The Poisson summation formula provides the analytic justification.
