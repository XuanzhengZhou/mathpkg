role: proof
locale: en
of_concept: power-series-of-normal-transformation
source_book: gtm031
source_chapter: "VI"
source_section: "11"
---
Since $A$ is a normal linear transformation, there exists a unitary basis for the vector space such that the matrix of $A$ is diagonal:

$$\operatorname{diag}\{ \rho_1, \rho_2, \cdots, \rho_n \}.$$

In this basis, the matrix of $A^k$ is simply $\operatorname{diag}\{ \rho_1^k, \rho_2^k, \cdots, \rho_n^k \}$. Therefore the partial sum $S_k(A) = \gamma_0 1 + \gamma_1 A + \cdots + \gamma_k A^k$ has the matrix

$$\operatorname{diag}\{ S_k(\rho_1), S_k(\rho_2), \cdots, S_k(\rho_n) \},$$

where $S_k(\lambda) = \gamma_0 + \gamma_1 \lambda + \cdots + \gamma_k \lambda^k$.

By hypothesis, $|\rho_i| < r$ for all $i = 1, 2, \cdots, n$, where $r$ is the radius of convergence of the power series $S(\lambda) = \sum_{j=0}^{\infty} \gamma_j \lambda^j$. Hence each scalar sequence $S_k(\rho_i)$ converges to $S(\rho_i)$ as $k \to \infty$. Therefore the matrix sequence $S_k(A)$ converges to the diagonal matrix

$$\operatorname{diag}\{S(\rho_1), S(\rho_2), \cdots, S(\rho_n)\}.$$

Since this limit matrix is diagonal with respect to a unitary basis, it is a normal transformation.
