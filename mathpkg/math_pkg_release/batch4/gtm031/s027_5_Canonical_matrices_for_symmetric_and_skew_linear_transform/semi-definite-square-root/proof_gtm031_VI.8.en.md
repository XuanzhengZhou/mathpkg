---
role: proof
locale: en
of_concept: semi-definite-square-root
source_book: gtm031
source_chapter: "VI"
source_section: "8"
---

Since $B$ is symmetric, by Theorem 4 there exists a Cartesian basis $(y_1, \ldots, y_n)$ such that $y_i B = \rho_i y_i$ with $\rho_i \geq 0$ (by Theorem 10, since $B$ is semi-definite). Group the $y_i$ so that the first $n_1$ are those with root $\rho_1$, the next $n_2$ go with $\rho_2 \neq \rho_1$, etc. Introduce the subspaces
$$\mathfrak{R}_1 = [y_1, \ldots, y_{n_1}], \quad \mathfrak{R}_2 = [y_{n_1+1}, \ldots, y_{n_1+n_2}], \ldots$$
so that $\mathfrak{R} = \mathfrak{R}_1 \oplus \mathfrak{R}_2 \oplus \cdots \oplus \mathfrak{R}_h$ where $h$ is the number of distinct characteristic roots.

For $u_i \in \mathfrak{R}_i$, clearly $u_i B = \rho_i u_i$. Moreover, the space $\mathfrak{R}_i$ is exactly the characteristic subspace of $\mathfrak{R}$ corresponding to the root $\rho_i$ of $B$. Since characteristic subspaces are invariant under any linear transformation that commutes with $B$, any semi-definite $P$ with $P^2 = B$ must satisfy $BP = PB$, hence $\mathfrak{R}_i P \subseteq \mathfrak{R}_i$.

Thus $P$ induces a semi-definite transformation on each $\mathfrak{R}_i$ satisfying $P^2 = \rho_i 1$. Define $P$ on $\mathfrak{R}_i$ as scalar multiplication by $\sqrt{\rho_i}$ (the non-negative square root). This $P$ is semi-definite, commutes with $B$, and satisfies $P^2 = B$.

For positive definite $B$, all $\rho_i > 0$ and the construction yields a unique positive definite square root.
