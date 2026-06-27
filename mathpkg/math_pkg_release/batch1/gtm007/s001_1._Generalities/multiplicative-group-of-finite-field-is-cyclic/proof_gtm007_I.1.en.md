---
role: proof
locale: en
of_concept: multiplicative-group-of-finite-field-is-cyclic
source_book: gtm007
source_chapter: "I. Finite Fields"
source_section: "1. Generalities"
---

Let $n = q-1 = |\mathbf{F}_q^*|$. For each divisor $d$ of $n$, consider the equation $x^d = 1$ in $\mathbf{F}_q$. This polynomial equation has at most $d$ roots in the field $\mathbf{F}_q$. Let $m_d$ denote the number of elements of order exactly $d$ in $\mathbf{F}_q^*$. If $m_d > 0$, let $a$ be an element of order $d$. Then the $d$ distinct powers $1, a, a^2, \ldots, a^{d-1}$ all satisfy $x^d = 1$, and by the bound on roots, these are precisely all solutions. Among these $d$ elements, exactly $\phi(d)$ have order $d$ (the generators of the cyclic subgroup $\langle a \rangle$), so $m_d = \phi(d)$ whenever $m_d > 0$.

Since every element of $\mathbf{F}_q^*$ has some order dividing $n$, we have
$$\sum_{d \mid n} m_d = n.$$

By Lemma 1, $\sum_{d \mid n} \phi(d) = n$. Since $0 \leq m_d \leq \phi(d)$ for each $d$ (with equality when $m_d > 0$), these two sums force $m_d = \phi(d)$ for every $d \mid n$. In particular, $m_n = \phi(n) > 0$, so there exists an element of order $n$. Therefore $\mathbf{F}_q^*$ is cyclic of order $q-1$.
