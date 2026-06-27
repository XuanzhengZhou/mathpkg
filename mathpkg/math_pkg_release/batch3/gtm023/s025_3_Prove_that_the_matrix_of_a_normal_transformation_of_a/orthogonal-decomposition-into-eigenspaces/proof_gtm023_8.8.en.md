---
role: proof
locale: en
of_concept: orthogonal-decomposition-into-eigenspaces
source_book: gtm023
source_chapter: "VIII"
source_section: "8.8"
---

Denote by $\lambda_v$ ($v = 1, \ldots, r$) the distinct eigenvalues of $\varphi$. For $i \neq j$, the eigenspaces $E(\lambda_i)$ and $E(\lambda_j)$ are orthogonal by the orthogonality of distinct eigenspaces. Since every vector $x \in E$ can be written as a linear combination of eigenvectors (by the spectral theorem), it follows that the direct sum of the spaces $E(\lambda_i)$ is $E$. Thus we obtain the orthogonal decomposition
$$E = E(\lambda_1) \oplus E(\lambda_2) \oplus \cdots \oplus E(\lambda_r).$$

Choosing an orthonormal basis within each eigenspace and taking their union yields an orthonormal basis of $E$ in which the matrix of $\varphi$ is diagonal with each $\lambda_v$ appearing $k_v = \dim E(\lambda_v)$ times. Consequently, the characteristic polynomial is
$$\det(\varphi - \lambda \iota) = (\lambda_1 - \lambda)^{k_1} \cdots (\lambda_r - \lambda)^{k_r}.$$
