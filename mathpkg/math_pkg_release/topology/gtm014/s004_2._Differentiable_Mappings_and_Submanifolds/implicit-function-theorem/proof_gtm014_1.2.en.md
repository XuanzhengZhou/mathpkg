---
role: proof
locale: en
of_concept: implicit-function-theorem
source_book: gtm014
source_chapter: "I"
source_section: "2"
---

**Note:** The proof text in the source appears to be partially corrupted by OCR; the content below reconstructs what is present.

Since $(d\phi)_{x_0}$ has rank $n$, there is an $n \times n$ minor which is non-singular. Let $\phi_1, \ldots, \phi_m$ be the coordinate functions defined by $\phi$. Then

$$
(d\phi)_{x_0} = \begin{pmatrix}
\frac{\partial \phi_1}{\partial x_1} & \frac{\partial \phi_1}{\partial x_2} & \ldots & \frac{\partial \phi_1}{\partial x_m} \\
\vdots & \vdots & & \vdots \\
\frac{\partial \phi_m}{\partial x_1} & \frac{\partial \phi_m}{\partial x_2} & \ldots & \frac{\partial \phi_m}{\partial x_m}
\end{pmatrix}
$$

The appropriate minor is determined by $n$ columns $i_1, \ldots, i_n$.

Let $\tau_1$ be a linear isomorphism of $\mathbf{R}^m$ which maps $\varepsilon_{i_j} \mapsto \varepsilon_j$ ($1 \leq j \leq n$) where $\varepsilon_j$ is the unit vector along the $j$th coordinate. Then $\tau_1 \circ \phi$ has the property that $(d\tau_1 \circ \phi)_{x_0}$ has rank $n$ and the appropriate $n \times n$ minor which is nonsingular is given by the first $n$-columns. By including $\tau_1$ in the definition of $\tau$ we assume that $\phi$ has this property.

Write $\mathbf{R}^m = \mathbf{R}^n \times \mathbf{R}^l$ where $l = m - n$ and $\mathbf{R}^n$ is given by the first $n$-coordinates $x_1, \ldots, x_n$ and $\mathbf{R}^l$ by the last $l$-coordinates $y_1, \ldots, y_l$. $\phi: U \to \mathbf{R}^n \times \mathbf{R}^l$ is given by $\phi = \phi_1 + \phi_2$ where $\phi_1: U \to \mathbf{R}^n$, $\phi_2: U \to \mathbf{R}^l$.

Define $\tilde{\phi}(x, y) = (\phi_1(x, y), y)$. Then

$$
d\tilde{\phi} = \begin{pmatrix}
\frac{\partial \phi_1}{\partial x} & \frac{\partial \phi_1}{\partial y} \\
0 & I
\end{pmatrix}
$$

which has rank $n$. By the inverse function theorem $\tilde{\phi}$ is locally a diffeomorphism. Let $\sigma = \tilde{\phi}$ and $\lambda: \mathbf{R}^m \times \mathbf{R}^l \to \mathbf{R}^m$ be given by $\lambda(x, y) = x$. Then $\lambda \circ \tilde{\phi}(x, y) = \lambda(\phi_1(x,y), y) = \phi_1(x,y)$.
