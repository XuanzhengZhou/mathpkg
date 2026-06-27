---
role: proof
locale: en
of_concept: properties-of-lambda-E
source_book: gtm040
source_chapter: "9"
source_section: "2"
---

The first two assertions follow from the facts that $P^n B^E \geq 0$ for every $n$ (since $P$ and $B^E$ are non-negative matrices) and that $(P^n B^E)_{ij} = 0$ if $j \in E$ (since $B^E_{kj} = 0$ for $j \in E$, and the $j$-th column of $B^E$ is zero on $E$). Hence the limit $\lambda^E$, if it exists, inherits these properties.

For the third assertion,
$$(\lambda^E 1) 1 = (1 \lambda^E) 1 = (\lim_n P^n B^E) 1 \leq \lim_n (P^n B^E 1) = 1,$$
since $B^E 1 \leq 1$ (the probability of ever hitting $E$ is at most 1), hence $\lambda^E 1 \leq 1$.
