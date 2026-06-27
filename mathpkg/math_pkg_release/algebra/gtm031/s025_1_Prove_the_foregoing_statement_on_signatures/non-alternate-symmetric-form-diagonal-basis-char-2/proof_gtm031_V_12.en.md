---
role: proof
locale: en
of_concept: non-alternate-symmetric-form-diagonal-basis-char-2
source_book: gtm031
source_chapter: "V"
source_section: "12"
---

We suppose that $g(x,y)$ is a skew-symmetric scalar product that is not alternate. Then $\Phi$ has characteristic two and $g(x,y)$ may also be regarded as symmetric. Moreover, we have seen that if $(e_1, e_2, \ldots, e_n)$ is a basis for $\mathfrak{R}$, then $g(e_i, e_i) \neq 0$ for some $i$. We shall now show that it is possible to choose a basis $(u_1, u_2, \ldots, u_r, z_1, z_2, \ldots, z_{n-r})$ for $\mathfrak{R}$ such that the matrix determined by this basis is

$$\{\beta_1, \beta_2, \ldots, \beta_r, 0, 0, \ldots, 0\},$$

with $\beta_i \neq 0$. Evidently $u_1$ can be chosen so that $g(u_1, u_1) \neq 0$, and we set $\beta_1 = g(u_1, u_1)$. Assume that we have found $u_1, u_2, \ldots, u_k$, $k \geq 1$, such that $g(u_i, u_j) = 0$ for $i \neq j$ and $g(u_i, u_i) = \beta_i \neq 0$. Let $\mathfrak{U}$ be the subspace spanned by $u_1, u_2, \ldots, u_k$, and let $\mathfrak{U}^{\perp}$ be the orthogonal complement of $\mathfrak{U}$ relative to $g$. If $\mathfrak{U}^{\perp}$ contains a vector $v$ with $g(v, v) = 0$, then since $g$ is non-alternate on the whole space, there exists a $w$ in the full space with $g(w, w) \neq 0$. By considering the projection, we can find $v \in \mathfrak{U}^{\perp}$ and $w \notin \mathfrak{U}^{\perp}$ such that $g(v, w) = 1$ and the restriction of $g$ to $[v, w]$ is non-degenerate.

We now set $u = u_k$, $\beta = \beta_k$ and we consider the scalar product in the three-dimensional space $[u, v, w]$. Using these vectors as basis we obtain the matrix

$$\begin{bmatrix}
\beta & 0 & 0 \\
0 & 0 & 1 \\
0 & 1 & 0
\end{bmatrix}.$$

Thus if $y = \xi u + \eta v + \zeta w$ and $y' = \xi' u + \eta' v + \zeta' w$, then $g(y, y') = \beta \xi \xi' + \eta \zeta' + \eta' \zeta$. Hence the following vectors

$$y_1 = u + v, \quad y_2 = u + \beta w, \quad y_3 = u + v + \beta w$$

are orthogonal in pairs and satisfy $g(y_i, y_i) = \beta$. It follows that, if we replace the original $u_k$ by $y_1$ and call this vector $u_k$ again, then $u_1, u_2, \ldots, u_k, u_{k+1} = y_2, u_{k+2} = y_3$ satisfy $g(u_i, u_j) = \delta_{ij} \beta_i$, $\beta_i \neq 0$.

This process can be continued until the orthogonal complement of the subspace spanned by the $u_i$ contains only vectors $z$ with $g(z, z) = 0$. Since $g$ is non-alternate, such vectors must satisfy $g(z, z') = 0$ for all $z, z'$ in this complement, completing the construction of the diagonal basis. $\square$
