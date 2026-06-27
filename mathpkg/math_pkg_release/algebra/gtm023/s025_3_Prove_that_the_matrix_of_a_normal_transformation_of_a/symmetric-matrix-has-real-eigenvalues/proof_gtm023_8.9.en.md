---
role: proof
locale: en
of_concept: symmetric-matrix-has-real-eigenvalues
source_book: gtm023
source_chapter: "VIII"
source_section: "8.9"
---

Consider the transformation $\varphi$ defined on an orthonormal basis $x_v$ ($v = 1, \ldots, n$) by
$$\varphi x_v = \sum_\mu \alpha_v^\mu x_\mu.$$
The matrix of $\varphi$ relative to this orthonormal basis is $A = (\alpha_v^\mu)$, which is symmetric. Hence $\varphi$ is selfadjoint. By the spectral theorem, the characteristic polynomial of $\varphi$ factors as
$$\det(\varphi - \lambda \iota) = (\lambda_1 - \lambda)^{k_1} \cdots (\lambda_r - \lambda)^{k_r}$$
with real $\lambda_v$. But $\det(\varphi - \lambda \iota) = \det(A - \lambda I)$, so
$$\det(A - \lambda I) = (\lambda_1 - \lambda)^{k_1} \cdots (\lambda_r - \lambda)^{k_r}.$$
Thus $A$ has $n$ real eigenvalues (counted with multiplicity).
