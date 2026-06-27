---
role: proof
locale: en
of_concept: decomposition-into-stable-planes
source_book: gtm023
source_chapter: "8"
source_section: "8.20"
---

Denote by $E_1$ and $E_2$ the eigenspaces corresponding to eigenvalues $\lambda = +1$ and $\lambda = -1$ respectively. For $x_1 \in E_1$ and $x_2 \in E_2$, we have $\varphi x_1 = x_1$ and $\varphi x_2 = -x_2$, so $(x_1, x_2) = -(\varphi x_1, \varphi x_2) = -(x_1, x_2)$, forcing $(x_1, x_2) = 0$. Thus $E_1 \perp E_2$.

Let $F = (E_1 \oplus E_2)^\perp$. Since any rotation preserves orthogonality of stable subspaces, $F$ is stable under $\varphi$. For any $e \in F$, $e \neq 0$, the vectors $e$ and $\varphi e$ are linearly independent (otherwise $\varphi$ would have an eigenvector in $F$). Equation (8.38): $\varphi^2 e = \lambda \varphi e - e$ follows from considering the selfadjoint part $\varphi + \varphi^{-1}$ restricted to $F$.

The vectors $e$ and $\varphi e$ span a stable plane $F_1$, and the induced mapping is a proper rotation (if it were improper, there would be an eigenvector). Taking $F_1^\perp$ in $F$ and iterating, we obtain an orthogonal decomposition of $F$ into mutually orthogonal stable planes.

Selecting orthonormal bases in $E_1$, $E_2$, and each stable plane yields the canonical matrix form with $\varepsilon_v = \pm 1$ and $2 \times 2$ rotation blocks.
