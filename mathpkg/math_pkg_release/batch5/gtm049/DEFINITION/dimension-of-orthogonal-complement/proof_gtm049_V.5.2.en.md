---
role: proof
locale: en
of_concept: dimension-of-orthogonal-complement
source_book: gtm049
source_chapter: "V"
source_section: "5.2"
---

Let $r = \dim(M \cap V^{\top})$ and extend a basis $(a_1, \ldots, a_r)$ of $M \cap V^{\top}$ to a basis $(a_1, \ldots, a_r, a_{r+1}, \ldots, a_m)$ of $M$. A vector $b = \sum y_j a_j$ lies in $M^{\perp}$ if and only if $\sigma(a_i, b) = 0$ for $i = 1, \ldots, m$, which gives a system of $m$ linear equations in $n$ unknowns $y_1, \ldots, y_n$. Since $a_1, \ldots, a_r \in V^{\top}$, the first $r$ equations are identically zero, leaving $m - r$ independent equations. By Theorem 4 of Chapter III (p. 50), the solution space has dimension $n - (m - r) = \dim V - (\dim M - \dim(M \cap V^{\top}))$, establishing the first formula. The second is proved symmetrically.

Alternatively, using Lemma 1: $M^{\perp} = (M\varrho)^{\circ}$ where $\varrho: V \to V^*$ is the linear map induced by $\sigma$, and the dimension formula for annihilators yields the same result.
