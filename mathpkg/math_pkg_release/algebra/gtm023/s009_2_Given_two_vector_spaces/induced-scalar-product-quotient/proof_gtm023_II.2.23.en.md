---
role: proof
locale: en
of_concept: induced-scalar-product-quotient
source_book: gtm023
source_chapter: "II"
source_section: "2.23"
---

Let $\Phi$ be the restriction of the scalar product $\langle \, , \, \rangle$ to $E^* \times F$. Then the nullspaces of $\Phi$ are given by
$$N_{E^*} = F^\perp \quad \text{and} \quad N_F = 0.$$
Indeed, $x^* \in N_{E^*}$ means $\langle x^*, y \rangle = 0$ for all $y \in F$, which is exactly $x^* \in F^\perp$. And $y \in N_F$ means $\langle x^*, y \rangle = 0$ for all $x^* \in E^*$, which by non-degeneracy of the scalar product implies $y = 0$.

The result now follows immediately from the construction of the non-degenerate bilinear function on the quotient by nullspaces (sec. 2.21/2.22): factoring out $N_{E^*} = F^\perp$ yields a non-degenerate bilinear pairing between $E^*/F^\perp$ and $F$, defining a scalar product via
$$\langle \bar{x}^*, y \rangle = \langle x^*, y \rangle$$
for any representative $x^*$ of $\bar{x}^*$.
