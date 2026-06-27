---
role: proof
locale: en
of_concept: radical-dimension-formula
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "1. Bilinear forms"
---

By definition, the left radical $\mathfrak{N}_L$ is the null space of the linear transformation $L: \mathfrak{R} \to (\mathfrak{R}')^*$. By the rank-nullity theorem for linear transformations,

$$\dim \operatorname{im} L + \dim \ker L = \dim \mathfrak{R}.$$

Since $\ker L = \mathfrak{N}_L$, this gives $\dim \operatorname{im} L + \dim \mathfrak{N}_L = \dim \mathfrak{R}$. Similarly, $\mathfrak{N}_R = \ker R$, so

$$\dim \operatorname{im} R + \dim \mathfrak{N}_R = \dim \mathfrak{R}'.$$

From the canonical form theorem (Theorem 1), the rank $r$ of the bilinear form equals the rank of its matrix, which is also the dimension of the image of $L$ and of $R$. Indeed, for the bases that put $g$ in canonical form, the matrix of $L$ has rank $r$, as does the matrix of $R$. Therefore $\dim \operatorname{im} L = r = \dim \operatorname{im} R$, yielding the stated formulas.
