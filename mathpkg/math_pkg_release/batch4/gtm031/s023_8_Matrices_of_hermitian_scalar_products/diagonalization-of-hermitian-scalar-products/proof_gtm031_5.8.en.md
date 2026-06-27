---
role: proof
locale: en
of_concept: diagonalization-of-hermitian-scalar-products
source_book: gtm031
source_chapter: "5"
source_section: "8"
---

The result is trivial if $g = 0$; then any basis serves as a set of $z$'s (with $r = 0$).

If $g \neq 0$, by the Lemma there exists a vector $u_1$ such that $g(u_1, u_1) = \beta_1 \neq 0$.

Now suppose we have already determined linearly independent vectors $(u_1, u_2, \cdots, u_k)$ such that $g(u_i, u_i) = \beta_i \neq 0$ and $g(u_i, u_j) = 0$ for $i \neq j$. Introduce the linear mapping $E_k$ defined by

$$x \mapsto x - \sum_{i=1}^{k} g(x, u_i) \beta_i^{-1} u_i.$$

Let $\Re F_k$ denote the image of $\Re$ under $E_k$, i.e., the orthogonal complement of $\mathfrak{S}_k = [u_1, u_2, \cdots, u_k]$ relative to $g$. The mapping $E_k$ is a projection onto $\Re F_k$, and one verifies that $u_j E_k = 0$ for $j \leq k$, so $E_k$ annihilates $\mathfrak{S}_k$.

If $g$ restricted to $\Re F_k$ is identically zero, then we may extend $(u_1, \cdots, u_k)$ to a basis for $\Re$ by adjoining any basis $(z_1, \cdots, z_{n-k})$ of $\Re F_k$. Since the $z$'s are orthogonal to the $u$'s and to each other (because $g = 0$ on $\Re F_k$), this yields a basis of the required type.

If $g \neq 0$ on $\Re F_k$, then by the Lemma applied to $\Re F_k$, there exists a vector $u_{k+1} \in \Re F_k$ such that $g(u_{k+1}, u_{k+1}) = \beta_{k+1} \neq 0$. The set $(u_1, u_2, \cdots, u_{k+1})$ is then linearly independent and, since $u_{k+1}$ is orthogonal to all $u_i$ ($i \leq k$), the enlarged set satisfies the same conditions. Repeating this process yields the desired basis after $r$ steps, where $r$ is the rank of $g$.

This method, due essentially to Lagrange, also shows that $\beta_1$ may be chosen as any element represented by the scalar product, and any $u_i$ may be replaced by $\gamma_i u_i$ ($\gamma_i \neq 0$), which transforms $\beta_i$ into $\beta_i' = \gamma_i \beta_i \bar{\gamma}_i$. In practice, a basis for $\Re F_k$ is obtained by supplementing $(u_1, \cdots, u_k)$ to a basis $(u_1, \cdots, u_k, v_1, \cdots, v_{n-k})$ of $\Re$, after which the $v_i E_k$ form a basis for $\Re F_k$.
