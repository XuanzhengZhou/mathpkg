---
role: proof
locale: en
of_concept: matrix-form-case-ii-lorentz
source_book: gtm023
source_chapter: "Chapter 13: Minkowski Space"
source_section: "II. The minimum polynomial is completely reducible"
---

Select an orthonormal basis $\{u_1, u_2\}$ of the pseudo-Euclidean plane $F$ adapted to the light-vector basis. Since $F$ has index $1$, we can choose $u_1, u_2$ such that the inner product matrix on $F$ is $\operatorname{diag}(1, -1)$ (or similar). The restriction $\varphi|_F$ acts as a hyperbolic rotation (Lorentz boost) on this plane. In the orthonormal basis, the matrix of a hyperbolic rotation with rapidity $\theta$ is

$$\begin{bmatrix} \cosh \theta & \sinh \theta \\ \sinh \theta & \cosh \theta \end{bmatrix}.$$

The condition $\theta \neq 0$ follows from the hypothesis that not all eigenvalues equal $1$ (otherwise $\varphi|_F = \iota$, contradicting $\lambda \neq 1$).

For $F^\perp$, we select an orthonormal basis. Since $\varphi|_{F^\perp}$ is a Euclidean rotation with angle $0$ or $\pi$, its matrix is $\varepsilon I_2$ with $\varepsilon = 1$ (angle $0$) or $\varepsilon = -1$ (angle $\pi$).

Taking the union of these bases gives an orthonormal basis of $E = F \oplus F^\perp$, and the matrix of $\varphi$ in this basis is the block diagonal matrix

$$\begin{bmatrix} \cosh \theta & \sinh \theta & 0 & 0 \\ \sinh \theta & \cosh \theta & 0 & 0 \\ 0 & 0 & \varepsilon & 0 \\ 0 & 0 & 0 & \varepsilon \end{bmatrix}.$$
