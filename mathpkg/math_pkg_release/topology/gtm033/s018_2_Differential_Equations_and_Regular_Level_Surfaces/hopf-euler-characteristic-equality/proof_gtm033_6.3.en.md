---
role: proof
locale: en
of_concept: hopf-euler-characteristic-equality
source_book: gtm033
source_chapter: "6"
source_section: "6.3"
---

# Proof of Hopf's Theorem: Equality of Euler Characteristics

The Euler characteristic of $M$ can be computed from any vector field $X$ on $M$ having finitely many zeros. We choose $X = \operatorname{grad} f$, where $f: M \to \mathbb{R}$ is a Morse function, and the gradient is taken with respect to a Riemannian metric on $M$ which, near each critical point, is induced from the standard Euclidean metric on $\mathbb{R}^n$ by Morse coordinates.

Let $p$ be a critical point of $f$ of index $k$. Let $(x_1, \ldots, x_n)$ be Morse coordinates at $p = (0, \ldots, 0)$. In these coordinates,

$$f(x) = -x_1^2 - \cdots - x_k^2 + x_{k+1}^2 + \cdots + x_n^2 + f(p),$$

and the gradient field is

$$X(x) = \operatorname{grad} f(x) = (-2x_1, \ldots, -2x_k, 2x_{k+1}, \ldots, 2x_n).$$

Scaling by $1/2$, we consider the vector field

$$\tilde{X}(x) = (-x_1, \ldots, -x_k, x_{k+1}, \ldots, x_n).$$

Thus $\tilde{X}$ is the Cartesian product of the vector fields $Y$ on $\mathbb{R}^k$ and $Z$ on $\mathbb{R}^{n-k}$ defined by

$$Y(y) = -y \quad (y \in \mathbb{R}^k),$$
$$Z(z) = z \quad (z \in \mathbb{R}^{n-k}).$$

The index of a product of vector fields is the product of their indices:

$$\operatorname{Ind}_0 \tilde{X} = (\operatorname{Ind}_0 Y)(\operatorname{Ind}_0 Z).$$

For the radial vector field $Y(y) = -y$ on $\mathbb{R}^k$, the map $y \mapsto -y/|y|$ on $S^{k-1}$ has degree $(-1)^k$, so

$$\operatorname{Ind}_0 Y = (-1)^k.$$

For $Z(z) = z$ on $\mathbb{R}^{n-k}$, the map $z \mapsto z/|z|$ on $S^{n-k-1}$ has degree $1$, so

$$\operatorname{Ind}_0 Z = 1.$$

Therefore

$$\operatorname{Ind}_p X = \operatorname{Ind}_0 \tilde{X} = (-1)^k.$$

Summing over all critical points of $f$, the Euler characteristic of $M$ (computed as the sum of indices of $X = \operatorname{grad} f$) is

$$\chi(M) = \sum_{p \text{ critical}} \operatorname{Ind}_p X = \sum_{k=0}^{n} (-1)^k v_k$$

where $v_k$ is the number of critical points of index $k$, i.e., the $k$-th type number of the Morse function $f$.

By Theorem 3.5 (the Morse inequalities with empty lower boundary, part (b)), the alternating sum of type numbers equals the homological Euler characteristic:

$$\sum_{k=0}^{n} (-1)^k v_k = \sum_{k=0}^{n} (-1)^k \dim_F H_k(M; F) = \chi'(M).$$

Equating the two expressions yields $\chi(M) = \chi'(M)$. Thus the Euler characteristic (defined via vector field indices) equals the homological Euler characteristic (defined via alternating sums of Betti numbers).
