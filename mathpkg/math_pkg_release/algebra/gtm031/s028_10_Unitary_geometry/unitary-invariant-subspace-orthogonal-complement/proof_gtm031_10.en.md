---
role: proof
locale: en
of_concept: unitary-invariant-subspace-orthogonal-complement
source_book: gtm031
source_chapter: "10"
source_section: "10. Unitary geometry"
---
Let $A$ be unitary and let $\mathfrak{S}$ be an $A$-invariant subspace. Since $A$ is invertible (as $A'A = AA' = 1$), the restriction of $A$ to $\mathfrak{S}$ is a bijection on $\mathfrak{S}$. For any $x \in \mathfrak{S}^{\perp}$ and any $y \in \mathfrak{S}$, we have $(xA, y) = (x, yA') = (x, yA^{-1})$. Since $\mathfrak{S}$ is $A$-invariant and $A$ is invertible, $A^{-1}$ also leaves $\mathfrak{S}$ invariant, so $yA^{-1} \in \mathfrak{S}$. Because $x \in \mathfrak{S}^{\perp}$, we have $(x, yA^{-1}) = 0$, hence $(xA, y) = 0$. Thus $xA \in \mathfrak{S}^{\perp}$, proving that $\mathfrak{S}^{\perp}$ is $A$-invariant.
