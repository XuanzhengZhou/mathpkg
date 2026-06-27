---
role: proof
locale: en
of_concept: congruence-under-automorphism
source_book: gtm049
source_chapter: "V"
source_section: "5.1"
---

Given two ordered bases $(a_1, \ldots, a_n)$ and $(b_1, \ldots, b_n)$ of $V$, there is a unique automorphism $f$ of $V$ such that $b_i = a_i f$ for $i = 1, \ldots, n$.

By the definition of $\sigma^f$, we have $(\sigma^f; (a_i)) = (\sigma; (b_i))$. Indeed, the $(i,j)$-entry of $(\sigma^f; (a_i))$ is $\sigma^f(a_i, a_j) = \sigma(a_i f, a_j f) = \sigma(b_i, b_j)$, which is the $(i,j)$-entry of $(\sigma; (b_i))$.

The matrices $(\sigma^f; (a_i))$ and $(\sigma; (a_i))$ are congruent (this is the content of Proposition 2). Thus the matrices of $\sigma$ with respect to all ordered bases lie in a single congruence class.

To prove that the whole class is obtained, take any matrix $T$ congruent to $(\sigma; (a_i))$. By Proposition 1, $T = (\tau; (a_i))$ for some bilinear form $\tau$, and then $\tau = \sigma^f$ for some automorphism $f$ of $V$. Hence $T = (\sigma; (b_i))$ where $b_i = a_i f$ for $i = 1, \ldots, n$.
