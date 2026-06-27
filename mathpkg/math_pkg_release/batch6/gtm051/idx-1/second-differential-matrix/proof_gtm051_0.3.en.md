---
role: proof
locale: en
of_concept: second-differential-matrix-representation
source_book: gtm051
source_chapter: "0"
source_section: "0.3"
---

The differential $dF: U \to L(\mathbb{R}^n, \mathbb{R}^m)$ is a mapping from an open subset of $\mathbb{R}^n$ into the vector space $L(\mathbb{R}^n, \mathbb{R}^m) \cong \mathbb{R}^{n \cdot m}$.

By definition, $dF$ is determined by the $n \cdot m$ real-valued coordinate functions

$$\frac{\partial F^i}{\partial x^j}, \qquad 1 \leq i \leq m, \; 1 \leq j \leq n.$$

These are the components of $dF$ with respect to the standard basis of $L(\mathbb{R}^n, \mathbb{R}^m)$ (matrices with a single 1 in position $(i, j)$ and zeros elsewhere).

Now $d^2F_{x_0} = d(dF)_{x_0}$. Applying the Jacobian matrix representation of the first differential to the map $dF$ itself, the matrix of $d^2F_{x_0}$ has entries given by the partial derivatives of the coordinate functions of $dF$, namely

$$\frac{\partial}{\partial x^k} \left( \frac{\partial F^i}{\partial x^j} \right)\bigg|_{x_0} = \frac{\partial^2 F^i}{\partial x^j \partial x^k}\bigg|_{x_0}.$$

The row index is $i$ (corresponding to the $m$ coordinate functions of $F$), while the column index runs over all $n \cdot m$ pairs $(j, k)$ where $j$ selects which component of $dF$ and $k$ selects the direction of differentiation. With the pairs $(i, j)$ ordered lexicographically, this yields an $m \times (n \cdot m)$ matrix.
