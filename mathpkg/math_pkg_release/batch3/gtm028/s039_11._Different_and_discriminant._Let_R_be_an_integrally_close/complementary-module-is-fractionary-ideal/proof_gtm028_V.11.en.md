---
role: proof
locale: en
of_concept: complementary-module-is-fractionary-ideal
source_book: gtm028
source_chapter: "V"
source_section: "§11. Different and discriminant"
---

Since $R'$ has $K'$ as quotient field, there exists a $K$-basis $\{e_1, \dots, e_n\}$ of $K'$ all of whose elements are in $R'$. Take any $z \in \mathcal{C}$ and write $z = \sum_i a_i e_i$ with $a_i \in K$. For each $i$, we have $T(z e_i) = \sum_j a_j T(e_j e_i) \in R$.

Since $K'$ is separable over $K$, the determinant $d = \det(T(e_i e_j))$ is non-zero. The system of linear equations $\sum_j a_j T(e_j e_i) = r_i \in R$ can be solved for the $a_i$ by Cramer's rule, giving $a_i \in d^{-1} R$.

Thus $z \in d^{-1} \sum_i R e_i$, showing that $\mathcal{C}$ is contained in the finite $R$-module $d^{-1} \sum_i R e_i$. By definition, $\mathcal{C}$ is an $R'$-module. Since it is contained in a finite $R$-module, it is a fractionary ideal of $R'$.
