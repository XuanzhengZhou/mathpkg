---
role: proof
locale: en
of_concept: ryser-incidence-matrix-commutation
source_book: gtm054
source_chapter: "IX"
source_section: "C"
---
Let us abbreviate $\lambda^*(2)$ by $\lambda^*$. By Exercise C15a,
$$M^*M = (k - \lambda^*)I + \lambda^*J.$$
Then
$$JM^* = JM^*MM^{-1} = J[(k - \lambda^*)I + \lambda^*J]M^{-1} = (k - \lambda^*)JM^{-1} + \lambda^*vJM^{-1} = \frac{k - \lambda^* + \lambda^*v}{k}J.$$
Taking the transpose gives $MJ = \frac{k - \lambda^* + \lambda^*v}{k}J$ (Equation C19).

Equation C19 implies that the matrix $M$ has constant row sums $(k - \lambda^* + \lambda^*v)/k$, and hence $\Lambda$ is a $(1; 1, 2)$-design. Since $b = v$, equation C7 gives $k = \frac{k - \lambda^* + \lambda^*v}{k}$, whence C19 becomes $MJ = kJ$ (Equation C20).

Hence by C17, C18, and C20,
$$MM^* = MM^*MM^{-1} = M[(k - \lambda^*)I + \lambda^*J]M^{-1} = (k - \lambda^*)I + \lambda^*J = M^*M.$$
