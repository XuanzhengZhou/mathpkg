---
role: exercise
locale: en
chapter: "1"
section: "1.12"
exercise_number: 6
---

(M. Barr, personal communication.) Let $U: \mathcal{C} \rightarrow \mathbf{Set}$ in $\text{Struct}(\mathbf{Set})$ construct finite limits and have the property that for all admissible $f: (X, s) \rightarrow (Y, t)$ the image $Xf$ is an optimal subset of $(Y, t)$. Many algebraic categories in mathematics are over such a base category. This exercise (the crux of the construction of 1.13; also, see the next exercise) provides insight as to how to interpret $\xi$ as in 1.2 as the coequalizer of a congruence.

Specializing the definition of the text, an optimal congruence on $(X, s)$ is an optimal subset $R$ of $(X, s) \times (X, s)$ which is an equivalence relation.

(a) Given optimal subsets $R, S$ on $(X, s)$ show that $R^{-1} = \{(y, x): (x, y) \in R\}$ and $RS = \{(x, z): \text{for some } y, (x, y) \in R \text{ and } (y, z) \in S\}$ are optimal subsets.

(b) Given $f, g: (X, s) \to (Y, t)$ with image $(S, \bar{s})$ of $f$ optimal, let $R$ be the intersection of all optimal congruences on $(X, s)$ containing $\{(af, ag): a \in X\}$. Prove that $R$ is an optimal congruence. (Hint: using the fact that $R$ is a subset of $RR^{-1}$, observe that $af = (afd)f$, $ag = (agd)f$, $(afd)g = (agd)g$.)
