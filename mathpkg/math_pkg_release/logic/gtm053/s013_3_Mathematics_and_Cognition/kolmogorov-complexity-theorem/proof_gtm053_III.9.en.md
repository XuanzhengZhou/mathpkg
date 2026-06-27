---
role: proof
locale: en
of_concept: kolmogorov-complexity-theorem
source_book: gtm053
source_chapter: "III"
source_section: "9"
---

We first choose a recursive embedding $\theta : \mathbf{Z}^+ \times \mathbf{Z}^+ \rightarrow \mathbf{Z}^+$ that has a recursive inverse function and satisfies the linear growth condition

$$\theta(k, j) \leqslant k \cdot \phi(j), \quad \text{for all } k, j \in \mathbf{Z}^+ \text{ and some suitable } \phi : \mathbf{Z}^+ \rightarrow \mathbf{Z}^+.$$

For example, $\theta(k, j) = (2k - 1)2^j$ with $\phi(j) = 2^{j+1}$ satisfies this condition.

Now let $U$ be any versal family of $(m+1)$-functions. We define a family $u$ of $m$-functions by setting

$$u(x_1, \ldots, x_m, k) = U(x_1, \ldots, x_m, \theta^{-1}(k)).$$

We show that the family $u$ is optimal, with the bound $c_{u,v} \leqslant \phi(C_U(v))$ for the constants. Let $f$ be a recursive $m$-function occurring in the family $v$:

$$f(x_1, \ldots, x_m) = v(x_1, \ldots, x_m; C_v(f)) = U(x_1, \ldots, x_m; C_U(v), C_v(f)).$$

Then $f = u_{\theta(C_v(f), C_U(v))}$, hence

$$C_u(f) \leqslant \theta(C_v(f), C_U(v)) \leqslant C_v(f) \cdot \phi(C_U(v)).$$

Setting $c_{u,v} = \phi(C_U(v))$ gives the required inequality, proving (a).

For (b), if $u$ and $v$ are both optimal, then by definition there exist constants $c_{u,v}$ and $c_{v,u}$ such that $C_u(f) \leqslant c_{u,v}C_v(f)$ and $C_v(f) \leqslant c_{v,u}C_u(f)$ for all $f$. Combining these yields $c_{v,u}^{-1} \leqslant C_u(f)/C_v(f) \leqslant c_{u,v}$.
