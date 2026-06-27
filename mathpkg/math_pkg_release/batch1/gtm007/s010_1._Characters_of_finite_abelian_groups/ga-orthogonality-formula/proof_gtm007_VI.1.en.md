---
role: proof
locale: en
of_concept: ga-orthogonality-formula
source_book: gtm007
source_chapter: "VI"
source_section: "§1. Characters of finite abelian groups"
---

Expand the right side:
$$
\frac{1}{\phi(m)} \sum_\chi \chi(a)^{-1} f_\chi(s) = \frac{1}{\phi(m)} \sum_{p \nmid m} \left(\sum_\chi \chi(a^{-1}p)\right) \frac{1}{p^s}.
$$
By the orthogonality corollary,
$$
\sum_\chi \chi(a^{-1}p) = \begin{cases} \phi(m) & \text{if } a^{-1}p \equiv 1 \pmod{m} \\ 0 & \text{otherwise} \end{cases}
$$
which is $\phi(m)$ exactly when $p \equiv a \pmod{m}$. Thus the sum reduces to $\sum_{p \equiv a (m)} 1/p^s = g_a(s)$.
