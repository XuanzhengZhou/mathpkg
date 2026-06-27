role: proof
locale: en
of_concept: unitary-as-exponential-of-hermitian
source_book: gtm031
source_chapter: "VI"
source_section: "11"
---
Since $U$ is unitary, it is normal, and therefore there exists a unitary basis relative to which the matrix of $U$ is diagonal:

$$\operatorname{diag}\{\rho_1, \rho_2, \cdots, \rho_n\}.$$

Because $U$ is unitary, its eigenvalues satisfy $|\rho_i| = 1$ for all $i$. Hence each $\rho_i$ can be written as $\rho_i = \exp(\sqrt{-1}\,\theta_i) = \exp(i\theta_i)$ for some real number $\theta_i$.

Define $H$ to be the linear transformation whose matrix relative to the same unitary basis is

$$\operatorname{diag}\{\theta_1, \theta_2, \cdots, \theta_n\}.$$

Since the $\theta_i$ are real, this matrix is hermitian, and therefore $H$ is a hermitian transformation.

Now consider $\exp(iH)$. By the result on power series of normal transformations, since $H$ has the diagonal matrix $\operatorname{diag}\{\theta_1, \cdots, \theta_n\}$, the transformation $\exp(iH)$ has the matrix

$$\operatorname{diag}\{\exp(i\theta_1), \exp(i\theta_2), \cdots, \exp(i\theta_n)\} = \operatorname{diag}\{\rho_1, \rho_2, \cdots, \rho_n\},$$

which is precisely the matrix of $U$ in this basis. Hence $U = \exp(iH)$.
