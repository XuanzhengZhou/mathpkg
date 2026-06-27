---
role: proof
locale: en
of_concept: conditional-smoothing-countable-partition
source_book: gtm046
source_chapter: "VIII"
source_section: "28.2"
---
Let $\{B_j\}$ be a countable partition of $\Omega$ generating $\mathfrak{B}$. Then each $B_j$ is an atom of $\mathfrak{B}$. On each atom $B_j$, $E^{\mathfrak{B}} X$ is constant (by $\mathfrak{B}$-measurability) with value
$$E_{B_j} X = \frac{1}{P B_j} \int_{B_j} X \, dP$$
when $P B_j > 0$. For any $\omega \in \Omega$, $\omega$ belongs to exactly one $B_j$, so $(E^{\mathfrak{B}} X)(\omega) = E_{B_j} X$. Therefore,
$$E^{\mathfrak{B}} X = \sum_j (E_{B_j} X) I_{B_j} \text{ a.s.}$$
The right-hand side is almost surely defined since each $E_{B_j} X$ exists as an integral over a set of positive measure.
