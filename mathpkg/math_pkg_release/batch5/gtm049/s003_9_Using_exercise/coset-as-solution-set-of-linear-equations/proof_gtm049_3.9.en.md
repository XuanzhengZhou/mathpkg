---
role: proof
locale: en
of_concept: coset-as-solution-set-of-linear-equations
source_book: gtm049
source_chapter: "3"
source_section: "9"
---

By the reduction already given of Theorem 3 to Theorem 4 we need only prove the proposition when the given coset is actually a subspace $M$ of $F^n$.

Define $M^\perp$ to be the set of all $(y_1, \ldots, y_n)$ in $F^n$ satisfying

$$\sum_{i=1}^{n} x_i y_i = 0$$

for all $(x_1, \ldots, x_n)$ in $M$. If we interpret $M$ as a coefficient space we see that $M^\perp$ is a subspace of $F^n$ of dimension $n - \dim M$.

The subspace $M^{\perp\perp}$ consisting of all $(z_1, \ldots, z_n)$ in $F^n$ satisfying

$$\sum_{i=1}^{n} y_i z_i = 0$$

for all $(y_1, \ldots, y_n)$ in $M^\perp$ clearly contains $M$. But $M^{\perp\perp}$ has dimension $n - (n - \dim M) = \dim M$ and so $M^{\perp\perp} = M$ (by Theorem 2(1) of Chapter I, p. 11).

If the rows $(a_{i1}, \ldots, a_{in})$, $i = 1, \ldots, m$, span $M^\perp$ then $M$ is the solution space of the equations $\sum_{j=1}^{n} a_{ij} X_j = 0$.
