---
role: proof
locale: en
of_concept: outer-measure-properties
source_book: gtm040
source_chapter: "1"
source_section: "2"
---
We see that $\mu$ is non-negative because $\mu$ is the limit of non-negative quantities. If $A \subset B$, then $\mu(A) \leq \mu(B)$ because every covering of $B$ is a covering of $A$. Let $C$ be in $\mathcal{F}$. Then $\{C\}$ is a covering of $C$ and $\mu(C) \leq \nu(C)$. And for any covering $\{C_n\}$,
$$\nu(C) \leq \sum_n \nu(C_n)$$
by Proposition 1-18. Therefore,
$$\nu(C) \leq \inf \sum_n \nu(C_n) = \mu(C).$$
Hence $\mu(C) = \nu(C)$.
