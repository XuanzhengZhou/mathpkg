---
role: proof
locale: en
of_concept: smooth-diagonalization-of-parameter-dependent-quadratic-forms
source_book: gtm014
source_chapter: "II"
source_section: "5"
---

Solve for the eigenvalues of the matrix
$$
A = \begin{pmatrix}
a & b \\
b & c
\end{pmatrix}
$$
representing the quadratic form $a x_1^2 + 2b x_1 x_2 + c x_2^2$. Since $A$ is close to
$$
\begin{pmatrix}
1 & 0 \\
0 & -1
\end{pmatrix}
$$
for $z$ small, the eigenvalues are distinct and are close to $1$ and $-1$. Moreover, they depend smoothly on $z$ (by the implicit function theorem applied to the characteristic polynomial, using that the eigenvalues are distinct).

For the eigenvalue close to $1$, we can find an eigenvector $(1, \tau)^{\mathsf{T}}$ with $\tau$ a smooth function of $z$ and $\tau(0) = 0$. Since $A$ is symmetric, the other eigenvector (for the eigenvalue near $-1$) will be orthogonal, i.e., $(-\tau, 1)^{\mathsf{T}}$.

Let $S$ be the rotation matrix obtained by normalizing these eigenvectors:
$$
S = \frac{1}{\sqrt{1 + \tau^2}}
\begin{pmatrix}
1 & \tau \\
-\tau & 1
\end{pmatrix}.
$$
Its coefficients are smooth functions of $z$, and $S(0)$ is the identity (since $\tau(0) = 0$). In the rotated coordinates $(\bar{x}_1, \bar{x}_2)^{\mathsf{T}} = S (x_1, x_2)^{\mathsf{T}}$, the quadratic form becomes diagonal: $\bar{a} \bar{x}_1^2 + \bar{b} \bar{x}_2^2$, where $\bar{a}$ and $\bar{b}$ are the eigenvalues of $A$. Hence $\bar{a}(0) = 1$ and $\bar{b}(0) = -1$. $\square$
