---
role: proof
locale: en
of_concept: formal-group-inverse
source_book: gtm059
source_chapter: "8"
source_section: "1. Lubin-Tate Groups"
---

The existence of $\iota(X)$ is proved by induction on the degree. Write $\iota(X) = -X + \sum_{n \ge 2} c_n X^n$. Suppose we have determined the coefficients up to degree $r$ such that $F(X, \iota(X)) \equiv 0 \pmod{\deg r+1}$. We wish to find $c_{r+1}$ such that the congruence holds modulo degree $r+2$.

Write $F(X,Y) = X + Y + \sum_{i,j \ge 1} a_{ij} X^i Y^j$. Then
$$
F(X, \iota(X)) = X + \iota(X) + \sum_{i,j \ge 1} a_{ij} X^i (\iota(X))^j.
$$
Substituting the expansion of $\iota(X)$ and collecting terms of degree $r+1$, the coefficient of $X^{r+1}$ is $c_{r+1} + P(a_{ij}, c_2, \dots, c_r)$ where $P$ is a polynomial expression in the previously determined coefficients. Setting this equal to $0$ uniquely determines $c_{r+1}$. This recursive construction yields the unique power series $\iota(X)$ with the required properties.
