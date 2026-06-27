---
role: proof
locale: en
of_concept: rank-nullity
source_book: gtm028
source_chapter: "I"
source_section: "21"
---

The fact that $K$ is finite-dimensional is included in the following lemma: every subspace of a finite-dimensional vector space is finite-dimensional (see subspace-dimension-bound).

Let $\{x_1, \ldots, x_p\}$ be a basis of $K$ and extend it to a basis $\{x_1, \ldots, x_p, x_{p+1}, \ldots, x_q\}$ of $V$ (possible by Theorem 21). We assert that $\{x_{p+1}T, \ldots, x_qT\}$ is a basis of $VT$.

First, every element of $VT$ may be written in the form
$$\left( \sum_{i=1}^{q} a_i x_i \right) T = \sum_{i=1}^{q} a_i (x_i T) = \sum_{j=p+1}^{q} a_j (x_j T),$$
since $x_i T = 0$ for $i = 1, \ldots, p$. Thus $\{x_{p+1}T, \ldots, x_qT\}$ is a system of generators of $VT$.

On the other hand, this system is free in $VT$, since a relation $\sum_{j=p+1}^{q} a_j (x_j T) = 0$ implies $\sum_{j=p+1}^{q} a_j x_j \in K$, that is, $\sum_{j=p+1}^{q} a_j x_j = \sum_{i=1}^{p} a_i x_i$ for suitable elements $a_i$ of $F$. The linear independence of the vectors $x_i, x_j$ implies that $a_j = 0$ for $j = p + 1, \ldots, q$.

This proves that $[VT:F] = q - p$. Since $[V:F] = q$ and $[K:F] = p$, we have
$$[V:F] = [K:F] + [VT:F].$$
