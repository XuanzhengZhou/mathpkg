---
role: proof
locale: en
of_concept: diagonal-rank-computation
source_book: gtm038
source_chapter: "V"
source_section: "V.3 Examples of Complex Manifolds"
---

In local coordinates $(z_1, \ldots, z_n)$ on $X$ near $x$, the coordinate functions on $X \times X$ can be written as $(z_1, \ldots, z_n, w_1, \ldots, w_n)$, where $z_i$ and $w_i$ correspond to the first and second factor respectively. Consider the holomorphic mapping
$$F: X \times X \to \mathbb{C}^n, \quad F(x, y) = (z_1(x) - w_1(y), \ldots, z_n(x) - w_n(y)).$$
The diagonal $D$ is precisely $F^{-1}(0)$.

At a point $(x, x) \in D$, we compute the rank of the Jacobian matrix of $F$ in local coordinates. With respect to the $2n$ variables $(z_1, \ldots, z_n, w_1, \ldots, w_n)$, the Jacobian matrix of $F$ at $(x, x)$ is the $n \times 2n$ matrix:
$$\operatorname{rk}_{(x, x)}(z_1 - w_1, \ldots, z_n - w_n) = \operatorname{rk}\big((D_v(z_i - w_i))_{\tilde{\varphi}}(x, x)\big)_{\substack{i=1,\ldots,n \\ v=1,\ldots,2n}} = \operatorname{rk}\begin{pmatrix} 1 & 0 & & -1 & 0 & \\ 0 & 1 & & 0 & -1 & \\ & & \ddots & & & \ddots \end{pmatrix} = n.$$

The block structure shows that the first $n$ columns (derivatives with respect to $z_i$) form an identity matrix, and the last $n$ columns (derivatives with respect to $w_i$) form a negative identity matrix. Thus the rank is $n$, confirming that the diagonal $D$ is a regular analytic subset of $X \times X$ of codimension $n$, which is exactly $\dim(X \times X) - \dim X = 2n - n = n$.
