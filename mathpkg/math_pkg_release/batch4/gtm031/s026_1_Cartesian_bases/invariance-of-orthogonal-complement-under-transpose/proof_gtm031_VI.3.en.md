---
role: proof
locale: en
of_concept: invariance-of-orthogonal-complement-under-transpose
source_book: gtm031
source_chapter: "VI"
source_section: "3"
---

Let $x \in \mathfrak{S}$ and $y \in \mathfrak{S}^\perp$. For any $A \in \Omega$, since $\mathfrak{S}$ is invariant under $\Omega$, we have $xA \in \mathfrak{S}$. By definition of the orthogonal complement, $(xA, y) = 0$.

Using the defining property of the adjoint, $(xA, y) = (x, yA')$. Thus $(x, yA') = 0$ for all $x \in \mathfrak{S}$. This means $yA' \in \mathfrak{S}^\perp$ for every $y \in \mathfrak{S}^\perp$ and every $A' \in \Omega'$.

Since $y$ was arbitrary in $\mathfrak{S}^\perp$, we conclude that $\mathfrak{S}^\perp$ is invariant under $\Omega'$.
