---
role: proof
locale: en
of_concept: ga-orthogonality-formula
source_book: gtm007
source_chapter: "VI"
source_section: "4"
---

By definition, $f_\chi(s) = \sum_{p \nmid m} \chi(p)/p^s$. Multiply by $\chi(a)^{-1}$ and sum over all $\chi$:
$$\sum_\chi \chi(a)^{-1} f_\chi(s) = \sum_{p \nmid m} \left(\sum_\chi \chi(a^{-1}p)\right) / p^s.$$

By the orthogonality of characters (Corollary to Proposition 4 applied to $G(m)$):
$$\sum_\chi \chi(a^{-1}p) = \begin{cases} \phi(m) & \text{if } a^{-1}p \equiv 1 \pmod{m} \\ 0 & \text{otherwise.} \end{cases}$$

The condition $a^{-1}p \equiv 1 \pmod{m}$ is equivalent to $p \equiv a \pmod{m}$. Hence the sum equals $\phi(m) g_a(s)$, and dividing by $\phi(m)$ gives the stated formula.

