---
role: proof
locale: en
of_concept: diagonalization-of-symmetric-bilinear-function
source_book: gtm023
source_chapter: "VIII"
source_section: "8.10"
---

Since $\Phi$ is symmetric, the corresponding transformation $\varphi$ defined by $\Phi(x, y) = (\varphi x, y)$ is selfadjoint. By the spectral theorem, there exists an orthonormal system of $n$ eigenvectors $e_v$ with $\varphi e_v = \lambda_v e_v$ ($v = 1, \ldots, n$). Then
$$\Phi(e_v, e_\mu) = (\varphi e_v, e_\mu) = \lambda_v (e_v, e_\mu) = \lambda_v \delta_{v\mu}.$$
Thus the matrix of $\Phi$ in the basis $e_v$ is $\operatorname{diag}(\lambda_1, \ldots, \lambda_n)$.
