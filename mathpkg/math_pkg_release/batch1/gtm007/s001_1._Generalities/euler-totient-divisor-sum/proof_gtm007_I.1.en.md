---
role: proof
locale: en
of_concept: euler-totient-divisor-sum
source_book: gtm007
source_chapter: "I. Finite Fields"
source_section: "1. Generalities"
---

Consider the cyclic group $\mathbb{Z}/n\mathbb{Z}$. For each divisor $d$ of $n$, let $C_d$ be the unique subgroup of order $d$ (namely $C_d = \{\overline{0}, \overline{n/d}, \overline{2n/d}, \ldots, \overline{(d-1)n/d}\}$). The elements of $C_d$ are precisely those $\overline{x} \in \mathbb{Z}/n\mathbb{Z}$ for which $d \cdot \overline{x} = \overline{0}$, i.e., $n \mid dx$, or equivalently $(n/d) \mid x$.

Each element $\overline{x} \in \mathbb{Z}/n\mathbb{Z}$ belongs to exactly one such subgroup, namely the one with $d = n/\gcd(x,n)$. Moreover, an element generates $C_d$ if and only if its order is exactly $d$. The number of generators of a cyclic group of order $d$ is $\phi(d)$. Partitioning $\mathbb{Z}/n\mathbb{Z}$ by the order of its elements yields
$$n = |\mathbb{Z}/n\mathbb{Z}| = \sum_{d \mid n} (\text{number of elements of order } d) = \sum_{d \mid n} \phi(d).$$
