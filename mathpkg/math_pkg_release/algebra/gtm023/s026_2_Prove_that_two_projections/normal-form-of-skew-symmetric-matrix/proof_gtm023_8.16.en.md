---
role: proof
locale: en
of_concept: normal-form-of-skew-symmetric-matrix
source_book: gtm023
source_chapter: "8"
source_section: "8.16"
---

Consider the mapping $\varphi = \psi^2$. Then $\tilde{\varphi} = \varphi$, so $\varphi$ is selfadjoint. By the spectral theorem for selfadjoint transformations (sec. 8.7), there exists an orthonormal basis $e_v$ ($v = 1 \dots n$) in which $\varphi$ has the form $\varphi e_v = \lambda_v e_v$.

All eigenvalues $\lambda_v$ are negative or zero. Indeed, if $\varphi e = \lambda e$ with $|e| = 1$, then $\lambda = (e, \varphi e) = (e, \psi^2 e) = -(\psi e, \psi e) \leq 0$.

Since the rank of $\psi$ is even and $\psi^2$ has the same rank as $\psi$, the rank of $\varphi$ must be even. Consequently, the number of negative eigenvalues is even and we can enumerate the vectors such that $\lambda_v < 0$ for $v = 1 \dots 2p$ and $\lambda_v = 0$ for $v = 2p+1 \dots n$.

Define the orthonormal basis $a_v$ ($v = 1 \dots n$) by
$$a_{2v-1} = e_v, \quad a_{2v} = \frac{1}{\kappa_v} \psi e_v \quad \text{where } \kappa_v = \sqrt{-\lambda_v} \quad (v = 1 \dots p)$$
and $a_v = e_v$ for $v = 2p+1 \dots n$. In this basis, the matrix of $\psi$ takes the block-diagonal form (8.35) with $2 \times 2$ blocks $\begin{bmatrix} 0 & \kappa_i \\ -\kappa_i & 0 \end{bmatrix}$.
