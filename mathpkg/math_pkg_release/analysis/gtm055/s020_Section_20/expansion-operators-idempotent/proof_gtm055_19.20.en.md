---
role: proof
locale: en
of_concept: expansion-operators-idempotent
source_book: gtm055
source_chapter: "19"
source_section: "20"
---

These assertions are immediate consequences of the biorthogonality relations. For any $x \in \mathcal{E}$, $E_N x = \sum_{n=0}^{N} \alpha_n(x) x_n$. Then for $M \leq N$,
$$E_M(E_N x) = \sum_{m=0}^{M} \alpha_m\left(\sum_{n=0}^{N} \alpha_n(x) x_n\right) x_m = \sum_{m=0}^{M} \alpha_m(x) x_m = E_M x,$$
since $\alpha_m(x_n) = \delta_{mn}$. Similarly $E_N(E_M x) = E_M x$. Thus $E_M E_N = E_N E_M = E_{M \wedge N}$. Setting $M = N$ gives $E_N^2 = E_N$, so each $E_N$ is idempotent.
