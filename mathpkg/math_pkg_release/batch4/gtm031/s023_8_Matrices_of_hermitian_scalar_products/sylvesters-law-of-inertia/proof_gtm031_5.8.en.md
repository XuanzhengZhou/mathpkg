---
role: proof
locale: en
of_concept: sylvesters-law-of-inertia
source_book: gtm031
source_chapter: "5"
source_section: "8"
---

The given diagonal matrices may be taken to be matrices of the same symmetric scalar product $g$ in $\Re$ relative to two bases $(u_1, \cdots, u_n)$ and $(v_1, \cdots, v_n)$. By reordering, we may arrange the basis vectors so that

$$\beta_i > 0 \text{ for } i = 1, \cdots, p; \quad \beta_j < 0 \text{ for } j = p+1, \cdots, r; \quad \beta_k = 0 \text{ for } k = r+1, \cdots, n,$$

and similarly for the $\beta_i'$ with $p'$ positive entries.

Introduce the subspaces:
$$\mathfrak{R}_+ = [u_1, \cdots, u_p], \quad \mathfrak{S}_+ = [v_1, \cdots, v_{p'}],$$
$$\mathfrak{R}_- = [u_{p+1}, \cdots, u_r], \quad \mathfrak{S}_- = [v_{p'+1}, \cdots, v_r].$$

Let $\mathfrak{R}^\perp$ denote the radical of $g$, spanned by $u_{r+1}, \cdots, u_n$.

If $y \in \mathfrak{R}_+ + \mathfrak{R}^\perp$, then $y = \sum_{i=1}^{p} \eta_i u_i + \sum_{j=r+1}^{n} \eta_j u_j$, and

$$g(y, y) = \sum_{i=1}^{p} \eta_i^2 \beta_i.$$

Since $\beta_i > 0$ for $i \leq p$, we have $g(y, y) \geq 0$, and $g(y, y) = 0$ only if all $\eta_i = 0$ ($i \leq p$), i.e., only if $y \in \mathfrak{R}^\perp$. A similar result holds for $\mathfrak{S}_+ + \mathfrak{R}^\perp$.

On the other hand, if $y \in \mathfrak{R}_- + \mathfrak{R}^\perp$, then $g(y, y) \leq 0$ and $g(y, y) = 0$ only if $y \in \mathfrak{R}^\perp$, and similarly for $\mathfrak{S}_- + \mathfrak{R}^\perp$.

Now consider $y \in (\mathfrak{R}_+ + \mathfrak{R}^\perp) \cap (\mathfrak{S}_- + \mathfrak{R}^\perp)$. Then $g(y, y) \geq 0$ (since $y \in \mathfrak{R}_+ + \mathfrak{R}^\perp$) and $g(y, y) \leq 0$ (since $y \in \mathfrak{S}_- + \mathfrak{R}^\perp$), hence $g(y, y) = 0$. By the characterization above, this forces $y \in \mathfrak{R}^\perp$. Thus

$$(\mathfrak{R}_+ + \mathfrak{R}^\perp) \cap (\mathfrak{S}_- + \mathfrak{R}^\perp) = \mathfrak{R}^\perp.$$

By dimension count,

$$\dim(\mathfrak{R}_+ + \mathfrak{R}^\perp) = p + (n - r), \quad \dim(\mathfrak{S}_- + \mathfrak{R}^\perp) = (r - p') + (n - r) = n - p'.$$

Since the intersection has dimension $n - r$, we have

$$(p + n - r) + (n - p') - (n - r) \leq n,$$

which simplifies to $p \leq p'$. By symmetry (exchanging the roles of the two bases), $p' \leq p$, so $p = p'$.
