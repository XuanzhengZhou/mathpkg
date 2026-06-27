---
role: proof
locale: en
of_concept: orthogonality-properties-of-root-spaces
source_book: gtm009
source_chapter: "8"
source_section: "8.3 Orthogonality properties"
---

**(a)** If $\alpha + \beta \neq 0$, then by Proposition 8.1, $\kappa(L_\alpha, L_\beta) = 0$. So the only possible nonzero pairing is when $\beta = -\alpha$.

**(b)** Since $\kappa$ is nondegenerate on $L$, and by (a) $L_\alpha$ is orthogonal to all root spaces except possibly $L_{-\alpha}$, the restriction $\kappa: L_\alpha \times L_{-\alpha} \to F$ must be nondegenerate. (Otherwise some $x \in L_\alpha$ would satisfy $\kappa(x, L) = 0$, forcing $x = 0$.)

**(c)** For any $x \in L_\alpha$, $y \in L_{-\alpha}$, $h \in H$, associativity gives:
$$\kappa([x y], h) = \kappa(x, [y h]) = -\kappa(x, [h y]) = \alpha(h) \kappa(x, y) = \kappa(\kappa(x, y) t_\alpha, h).$$
Thus $[x y] - \kappa(x, y) t_\alpha$ is orthogonal to $H$. Since $[L_\alpha L_{-\alpha}] \subset H$ (by Proposition 8.1, as $[L_\alpha L_{-\alpha}] \subset L_0 = H$) and $\kappa$ is nondegenerate on $H$ (Corollary 8.2), we get $[x y] = \kappa(x, y) t_\alpha$. This proves (e).

Since $L_\alpha \neq 0$, pick nonzero $x \in L_\alpha$. By (b), there exists $y \in L_{-\alpha}$ with $\kappa(x, y) \neq 0$. Then $[x y] = \kappa(x, y) t_\alpha$ is a nonzero multiple of $t_\alpha$, showing $[L_\alpha L_{-\alpha}]$ is one-dimensional and spanned by $t_\alpha$.

**(d)** Suppose $\kappa(t_\alpha, t_\alpha) = 0$, i.e., $\alpha(t_\alpha) = 0$. Then $[t_\alpha x] = 0 = [t_\alpha y]$ for all $x \in L_\alpha$, $y \in L_{-\alpha}$. Choose $x \in L_\alpha$, $y \in L_{-\alpha}$ with $\kappa(x, y) \neq 0$ (by (b)), and scale so $\kappa(x, y) = 1$. Then $[x y] = t_\alpha$ by (c). The subspace $S$ spanned by $x, y, t_\alpha$ is a three-dimensional solvable Lie algebra. By Lie's Theorem, $\mathrm{ad}_L S$ consists of upper triangular matrices in some basis, so $\mathrm{ad}_L t_\alpha = \mathrm{ad}_L [x y]$ is nilpotent. But $t_\alpha \in H$ is semisimple, so $\mathrm{ad}_L t_\alpha$ is both semisimple and nilpotent, forcing $\mathrm{ad}_L t_\alpha = 0$. Thus $t_\alpha \in Z(L) = 0$, a contradiction since $t_\alpha \neq 0$ (as $\alpha \neq 0$, there exists $h$ with $\alpha(h) \neq 0$, and $\kappa(t_\alpha, h) = \alpha(h) \neq 0$).

**(f)** By definition $h_\alpha = 2t_\alpha / \kappa(t_\alpha, t_\alpha)$. Then $\alpha(h_\alpha) = 2\alpha(t_\alpha)/\kappa(t_\alpha, t_\alpha) = 2\kappa(t_\alpha, t_\alpha)/\kappa(t_\alpha, t_\alpha) = 2$.

**(g)** Since $\kappa(t_{-\alpha}, h) = (-\alpha)(h) = -\alpha(h) = \kappa(-t_\alpha, h)$, and $\kappa$ is nondegenerate on $H$, we have $t_{-\alpha} = -t_\alpha$. Also $\kappa(t_{-\alpha}, t_{-\alpha}) = \kappa(t_\alpha, t_\alpha)$, so $h_{-\alpha} = -h_\alpha$.
