---
role: proof
locale: en
of_concept: structure-of-orthogonal-complement-fperp-case-ii
source_book: gtm023
source_chapter: "Chapter 13: Minkowski Space"
source_section: "II. The minimum polynomial is completely reducible"
---

Since $F$ has index $1$ and the ambient Minkowski space $E$ has overall index $1$ (signature $(3,1)$ in dimension $4$), the orthogonal complement $F^\perp$ must have index $0$, i.e., the inner product restricted to $F^\perp$ is positive definite. Thus $F^\perp$ is a Euclidean plane.

The transformation $\varphi$ preserves the Minkowski inner product, hence it maps $F^\perp$ into itself (since $\varphi$ preserves $F$ and the inner product). The restriction $\varphi|_{F^\perp}$ is therefore an orthogonal transformation of a $2$-dimensional Euclidean space, i.e., a rotation (possibly with reflection). Its matrix in an orthonormal basis has the form

$$\begin{bmatrix} \cos \omega & -\sin \omega \\ \sin \omega & \cos \omega \end{bmatrix} \quad \text{or} \quad \begin{bmatrix} \cos \omega & \sin \omega \\ \sin \omega & -\cos \omega \end{bmatrix}.$$

The corresponding eigenvalues are $e^{\pm i\omega}$ (rotation) or $\pm 1$ (reflection). If $\omega \neq 0, \pi$, the eigenvalues are non-real complex numbers $e^{\pm i\omega}$, and the minimum polynomial of $\varphi|_{F^\perp}$ would contain the irreducible quadratic factor $t^2 - 2t\cos\omega + 1$. This factor would also appear in the minimum polynomial of $\varphi$ on $E$, contradicting the hypothesis that the minimum polynomial of $\varphi$ is completely reducible (splits into linear factors). Therefore $\omega = 0$ or $\omega = \pi$, corresponding to $\varphi|_{F^\perp} = \pm \iota$.
