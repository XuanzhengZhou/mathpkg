---
role: proof
locale: en
of_concept: smooth-diagonalization-of-parameter-dependent-quadratic-forms
source_book: gtm014
source_chapter: "VII"
source_section: "5. Umbilics"
---

Let $A = \begin{pmatrix} a & b \\ b & c \end{pmatrix}$ be the symmetric matrix representing the quadratic form. Since $A$ is close to $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ for $z$ small, the eigenvalues are distinct and are close to $1$ and $-1$. Moreover, the eigenvalues depend smoothly on $z$ (as roots of the characteristic polynomial with distinct roots).

For the eigenvalue close to $1$, we can find an eigenvector $(1, \tau)$ with $\tau$ a smooth function of $z$ and $\tau(0) = 0$. Since $A$ is symmetric, the other eigenvector will be $(-\tau, 1)$. Let $S$ be the rotation matrix
$$\frac{1}{\sqrt{1 + \tau^2}} \begin{pmatrix} 1 & \tau \\ -\tau & 1 \end{pmatrix}.$$
Then $S(0)$ is the identity matrix, and $S$ diagonalizes the quadratic form. The diagonal entries $\bar{a}$ and $\bar{b}$ are precisely the eigenvalues of $A$, which satisfy $\bar{a}(0) = 1$ and $\bar{b}(0) = -1$.
