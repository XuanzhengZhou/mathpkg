---
role: proof
locale: en
of_concept: extension-of-derivations-to-finitely-generated-fields
source_book: gtm028
source_chapter: "IV"
source_section: "Examples of Derivations"
---

We first prove formula (7). By the Leibniz rule (2) for derivations, (7) holds when $g$ is a monomial $a X_1^{q_1} \cdots X_n^{q_n}$ with $a \in K$, since for a monomial:
$$D'(a x_1^{q_1} \cdots x_n^{q_n}) = D(a) x_1^{q_1} \cdots x_n^{q_n} + \sum_{i=1}^n a q_i x_1^{q_1} \cdots x_i^{q_i-1} \cdots x_n^{q_n} D'(x_i).$$
The first term is exactly the coefficientwise derivative, and the sum is $\sum_i D'(x_i)(D_i g)(x_1, \ldots, x_n)$. By linearity, (7) extends to all polynomials $g$.

Since $D'(0) = 0$, applying (7) to any relation $f_j(x_1, \ldots, x_n) = 0$ yields $D'(0) = f_j^D(x_1, \ldots, x_n) + \sum_i D'(x_i)(D_i f_j)(x_1, \ldots, x_n) = 0$, which is condition (5). This shows necessity and uniqueness (the values $D'(x_i)$ are forced).

For sufficiency when $\{f_j\}$ forms a basis of the ideal of algebraic relations: any polynomial $f$ vanishing at $(x_1, \ldots, x_n)$ can be written as $f = \sum_j g_j f_j$ with $g_j \in K[X_1, \ldots, X_n]$. By the product rule,
$$(D_i f)(x_1, \ldots, x_n) = \sum_j g_j(x_1, \ldots, x_n) (D_i f_j)(x_1, \ldots, x_n).$$
Multiplying each relation (6) by $g_j(x_1, \ldots, x_n)$ and summing over $j$ yields (5) for all relations, which guarantees consistency of the definition
$$D'(g(x_1, \ldots, x_n)) = g^D(x_1, \ldots, x_n) + \sum_i u_i (D_i g)(x_1, \ldots, x_n)$$
on $K[x_1, \ldots, x_n]$. One verifies that this defines a derivation, which then extends uniquely to the quotient field $F = K(x_1, \ldots, x_n)$.
