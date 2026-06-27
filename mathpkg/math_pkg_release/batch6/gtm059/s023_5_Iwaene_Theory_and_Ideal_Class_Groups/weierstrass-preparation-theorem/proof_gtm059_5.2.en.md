---
role: proof
locale: en
of_concept: weierstrass-preparation-theorem
source_book: gtm059
source_chapter: "5"
source_section: "5. Iwasawa Theory and Ideal Class Groups"
---

Let $\tau: A[[X]] \to A[[X]]$ be the projection onto the tail (terms of degree $\geq n$) and let $z$ be the projection onto the head (terms of degree $< n$). We need to find $q, r$ such that $g = qf + r$ with $\deg r < n$. This is equivalent to $\tau(g) = \tau(qf)$. Writing $f = z(f) + X^n \tau(f)$ and noting that $z(f)$ is invertible modulo $\mathfrak{m}$, one constructs $q$ by a successive approximation argument using the completeness of $A$. The uniqueness follows from the invertibility of the head coefficient.
