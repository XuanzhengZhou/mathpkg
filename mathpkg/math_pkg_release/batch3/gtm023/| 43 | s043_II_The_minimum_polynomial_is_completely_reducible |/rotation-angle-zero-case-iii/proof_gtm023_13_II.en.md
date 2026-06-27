---
role: proof
locale: en
of_concept: rotation-angle-zero-case-iii
source_book: gtm023
source_chapter: "Chapter 13: Minkowski Space"
source_section: "II. The minimum polynomial is completely reducible"
---

Let $\varphi_1 = \varphi|_{E_1}$. Computing the characteristic polynomial directly from the matrix

$$\begin{bmatrix}
\cos\omega & -\sin\omega & \alpha_1 \\
\sin\omega & \cos\omega & \alpha_2 \\
0 & 0 & 1
\end{bmatrix}$$

with respect to the basis $\{e_1, e_2, e\}$, we obtain

$$\chi_1(t) = \det(t I - \varphi_1) = \det\begin{bmatrix}
t - \cos\omega & \sin\omega & -\alpha_1 \\
-\sin\omega & t - \cos\omega & -\alpha_2 \\
0 & 0 & t-1
\end{bmatrix}.$$

Expanding along the third row, the determinant factors as

$$\chi_1(t) = (t-1) \cdot \det\begin{bmatrix} t - \cos\omega & \sin\omega \\ -\sin\omega & t - \cos\omega \end{bmatrix} = (t-1)((t-\cos\omega)^2 + \sin^2\omega) = (t-1)(t^2 - 2t\cos\omega + 1).$$

On the other hand, since the minimum polynomial of $\varphi$ on $E$ is $\mu = (t-1)^k$ and the characteristic polynomial of $\varphi$ has degree $4$ and is divisible by $\mu$, with all eigenvalues equal to $1$, the characteristic polynomial of $\varphi$ must be $(t-1)^4$. The characteristic polynomial of $\varphi_1$ on the $3$-dimensional invariant subspace $E_1$ divides that of $\varphi$, so $\chi_1(t) = (t-1)^3 = (1-t)^3$.

Equating the two expressions:

$$(t-1)(t^2 - 2t\cos\omega + 1) = (t-1)^3 = (t-1)(t^2 - 2t + 1).$$

Canceling the common factor $(t-1)$, we get

$$t^2 - 2t\cos\omega + 1 = t^2 - 2t + 1,$$

which implies $\cos\omega = 1$, so $\omega = 0$ (mod $2\pi$). Substituting $\omega = 0$ into the mapping equations gives the simplified form:

$$\varphi e_1 = e_1 + \alpha_1 e, \quad \varphi e_2 = e_2 + \alpha_2 e, \quad \varphi e = e.$$
