---
role: proof
locale: en
of_concept: canonical-form-of-real-skew-symmetric-matrices
source_book: gtm031
source_chapter: "VI"
source_section: "5"
---

If $A$ is a skew symmetric linear transformation and $y \neq 0$ is a vector whose order is an irreducible polynomial $\pi(\lambda)$, then consider the two possibilities for $\pi(\lambda)$.

If $\pi(\lambda)$ is linear, then $yA = \rho y$. Hence $\rho(y, y) = (yA, y) = -(y, yA) = -\rho(y, y)$, and this implies that $\rho = 0$. Thus $yA = 0$ on such a subspace.

If $\pi(\lambda)$ is quadratic, we choose a Cartesian basis in $\{y\}$. We then obtain a skew symmetric matrix
$$\begin{bmatrix}
0 & \delta \\
-\delta & 0
\end{bmatrix}.$$
The polynomial $\pi(\lambda)$ is the characteristic polynomial of this matrix. Hence $\pi(\lambda) = \lambda^2 + \delta^2$ where $\delta \neq 0$.

Applying the method used for symmetric mappings, we can decompose the space as a direct sum of mutually orthogonal spaces $\mathfrak{S}_i$, $i = 1, 2, \cdots, h$, such that each $\mathfrak{S}_i = \{y_i\}$, and the minimum polynomial $\pi_i(\lambda)$ of $y_i$ is either $\lambda$ or it is of the form $\lambda^2 + \delta_i^2$, $\delta_i \neq 0$. We can arrange the $\mathfrak{S}_i$ so that $\pi_i(\lambda) = \lambda^2 + \delta_i^2$ for $i = 1, 2, \cdots, k$ and $\pi_i(\lambda) = \lambda$ for $i > k$.

If we choose Cartesian bases in the $\mathfrak{S}_i$, we obtain a Cartesian basis for $\mathfrak{R}$ by stringing these bases together. The matrix of $A$ relative to this basis is the block diagonal matrix displayed in the theorem statement.

The canonical form is completely determined by the characteristic polynomial
$$\lambda^{n-2k} \prod_{i=1}^{k} (\lambda^2 + \delta_i^2), \quad \delta_i \neq 0$$
of $(\alpha)$. The characteristic roots are pure imaginaries.
