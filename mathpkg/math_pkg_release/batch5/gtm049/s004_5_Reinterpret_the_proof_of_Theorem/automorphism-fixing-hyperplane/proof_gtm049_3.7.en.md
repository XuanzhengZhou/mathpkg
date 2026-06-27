---
role: proof
locale: en
of_concept: automorphism-fixing-hyperplane
source_book: gtm049
source_chapter: "3"
source_section: "3.7"
---

Let $\{a_1, \ldots, a_k\}$ be a basis of $M$ (if $M = \{0\}$, this is vacuous). Extend this to a basis $\{a_1, \ldots, a_k, p, b_{k+2}, \ldots, b_n\}$ of $V$. Since $q \notin M$, the set $\{a_1, \ldots, a_k, q, b_{k+2}, \ldots, b_n\}$ is also a basis of $V$ (otherwise $q$ would be in the span of $M$ and $\{b_{k+2}, \ldots, b_n\}$, contradicting $q \notin M$).

Define $f$ on the first basis by:
$$a_i f = a_i \quad (i = 1, \ldots, k), \quad pf = q, \quad b_j f = b_j \quad (j = k+2, \ldots, n)$$
and extend linearly. This defines a linear automorphism of $V$.

Now let $H$ be the hyperplane spanned by $\{a_1, \ldots, a_k, p+q, b_{k+2}, \ldots, b_n\}$ (if $p+q = 0$, choose $p-q$ or another suitable combination). One verifies that $M \subset H$ and $f$ restricts to the identity on $H$, since $f$ fixes each basis vector of $H$. The induced projective transformation $\mathcal{P}(f)$ is then a central collineation with axis $\mathcal{P}(H)$.
