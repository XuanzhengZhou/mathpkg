---
role: proof
locale: en
of_concept: theorem-4-3-class-number-regulator
source_book: gtm059
source_chapter: "13"
source_section: "The Mellin Transform and p-adic L-function"
---

From Theorem 4.1 and the computation of the group index, we have
$$
h^+ = (\mathcal{E} : \mathcal{C}),
$$
where $(\mathcal{E}:\mathcal{C})$ is the index of the cyclotomic units in the full unit group, established in Theorem 5.1 of the preceding chapter. Then by Theorem 3.6 and the definition of the $p$-adic regulator:
$$
\pm h^+ \cdot R_p(\mathcal{E}) = \pm R_p(\mathcal{C}) = \prod_{\chi \neq 1} \sum_{a} \chi^{-1}(a) \log_p(1 - \zeta^a).
$$
Applying Theorem 3.6 to identify each factor with $L_p(1,\chi)$ and accounting for the factor $\frac{1}{2}$ arising because the Galois group involves $\mathbb{Z}/m^2\mathbb{Z}^\times$ (or more precisely $\pm 1$), we obtain:
$$
h^+ = \frac{1}{2^r} \cdot \frac{\prod_{\chi \neq 1} L_p(1,\chi)}{R_p(K)},
$$
which is the desired $p$-adic class number formula.
