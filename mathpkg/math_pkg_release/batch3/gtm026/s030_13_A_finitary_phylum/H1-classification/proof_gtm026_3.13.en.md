---
role: proof
locale: en
of_concept: H1-classification
source_book: gtm026
source_chapter: "3"
source_section: "13"
---

**(a)** A $1$-cocycle is an element $a \in [XT^2, Y]$ satisfying $d^2(a) = 0$, i.e.,

$$\xi T^2 \cdot a - XT\mu \cdot a + X\mu T \cdot a = 0.$$

Given such a cocycle, define a $\mathbf{T}$-algebra structure $\gamma$ on $Y \times X$ by constructing its structure map $\gamma: (Y \times X)T \rightarrow Y \times X$ using the universal property of products and the given structures $\theta$ on $Y$ and $\xi$ on $X$, twisted by the cocycle $a$. The conditions (i) and (ii) correspond exactly to the cocycle condition.

Conversely, given a $\mathbf{T}$-algebra structure $\gamma$ on $Y \times X$ satisfying (i) and (ii), one extracts a $1$-cocycle by comparing $\gamma$ with the product structure $\theta \times \xi$. The bijection is established by verifying that these constructions are inverse to each other.

**(b)** Two cocycles $a, a'$ are cohomologous (differ by a coboundary $d^1(t)$) precisely when there exists $q: Y \times X \rightarrow Y$ such that the indicated map is a $\mathbf{T}$-homomorphism between the corresponding twisted structures $\gamma$ and $\gamma'$. The existence of such $q$ provides the equivalence relation, and the quotient by coboundaries yields $H^1(X, \xi)$.

The detailed verification involves checking that the diagrammatic conditions on $\gamma$ translate exactly to the algebraic conditions defining cocycles and coboundaries in the triple cochain complex.
