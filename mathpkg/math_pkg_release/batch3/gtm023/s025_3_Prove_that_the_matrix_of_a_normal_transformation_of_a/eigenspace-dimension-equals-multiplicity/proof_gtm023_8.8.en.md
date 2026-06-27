---
role: proof
locale: en
of_concept: eigenspace-dimension-equals-multiplicity
source_book: gtm023
source_chapter: "VIII"
source_section: "8.8"
---

From the orthogonal decomposition $E = \bigoplus_{v=1}^r E(\lambda_v)$, choose an orthonormal basis within each eigenspace. In the union of these bases, the matrix of $\varphi$ is diagonal with $\lambda_v$ appearing $\dim E(\lambda_v)$ times on the diagonal. The characteristic polynomial is therefore
$$\det(\varphi - \lambda \iota) = \prod_{v=1}^r (\lambda_v - \lambda)^{\dim E(\lambda_v)}.$$
Comparing with the factorization $(\lambda_1 - \lambda)^{k_1} \cdots (\lambda_r - \lambda)^{k_r}$ from the spectral theorem, we obtain $k_v = \dim E(\lambda_v)$. Thus the dimension of each eigenspace equals the algebraic multiplicity of the corresponding eigenvalue.
