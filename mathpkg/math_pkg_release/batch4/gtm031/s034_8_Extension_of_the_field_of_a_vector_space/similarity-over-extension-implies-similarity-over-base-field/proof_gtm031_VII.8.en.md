---
role: proof
locale: en
of_concept: similarity-over-extension-implies-similarity-over-base-field
source_book: gtm031
source_chapter: "VII"
source_section: "8"
---

Let $\omega$ be the set of matrices determined by the extensions of the linear transformations in $\Omega$ relative to the basis $(\bar{e}_1, \dots, \bar{e}_n)$ with $\bar{e}_i = 1 \times e_i$, where $(e_1, \dots, e_n)$ is a basis of $\mathfrak{R}$ over $\Phi$. As shown, the matrices in $\omega$ all have elements in $\Phi$.

Let $(u_1, \dots, u_n)$ be any basis of $\mathfrak{R}_P$ over $P$ and write $u_i = \sum_{j=1}^n \mu_{ij} \bar{e}_j$ with $\mu_{ij} \in P$. Then the set of matrices of $\Omega$ relative to this basis is $(\mu)\omega(\mu)^{-1}$.

Assume that $(\mu)\omega(\mu)^{-1} \subseteq \Phi_n$, i.e., all these conjugated matrices have entries in $\Phi$. Then for every $(\alpha) \in \omega$,

$$(\mu)(\alpha) = (\beta)(\mu)$$

for some $(\beta) \in \Phi_n$, or equivalently $(\mu)(\alpha)(\mu)^{-1} = (\beta) \in \Phi_n$. This yields the equations

$$\sum_{k} \mu_{ik} \alpha_{kj} = \sum_{\ell} \beta_{i\ell} \mu_{\ell j}.$$

Rearranging gives linear equations in the $\mu_{ij}$ with coefficients in $\Phi$:

$$\sum_{i,j} \beta_{ij} \mu_{ij} = 0, \quad \beta_{ij} \in \Phi.$$

Regard the set $\{(\beta)\}$ as a subset of $\Phi_n$ and let $r$ be the rank of this set — the largest number of linearly independent (over $\Phi$) matrices in $\{(\beta)\}$. The equations $\sum \beta_{ij} \xi_{ij} = 0$ have $n^2 - r$ linearly independent solutions for $\xi_{ij}$ in $\Phi$, and every solution is a $\Phi$-linear combination of these. Let $(\gamma_{ij}^{(1)}), (\gamma_{ij}^{(2)}), \dots, (\gamma_{ij}^{(h)})$ with $h = n^2 - r$ be such a basic set of solutions.

A key observation: a set of matrices with coefficients in $\Phi$ that are linearly independent over $\Phi$ are also linearly independent over $P$. This follows because the space $P_n$ is precisely the extension space $\Phi_n^P$ (the Kronecker product $P \times \Phi_n$). Consequently, the rank $r$ of $\{(\beta)\}$ relative to $P$ is the same as over $\Phi$, and the maximum number of linearly independent solutions of $\sum \beta_{ij} \xi_{ij} = 0$ in $P$ is also $n^2 - r$. Hence the solutions $(\gamma_{ij}^{(1)}), \dots, (\gamma_{ij}^{(h)})$ we selected form a basic set for the solutions in $P$.

In particular, the $\mu_{ij}$ (which satisfy the equations by assumption) can be expressed as

$$\mu_{ij} = \nu_1 \gamma_{ij}^{(1)} + \nu_2 \gamma_{ij}^{(2)} + \cdots + \nu_h \gamma_{ij}^{(h)}$$

where the $\nu_k \in P$.

Now replace the $\nu_k$ by independent indeterminates $\lambda_k$ and consider the matrix $(\gamma(\lambda))$ with entries

$$\gamma_{ij}(\lambda) = \lambda_1 \gamma_{ij}^{(1)} + \lambda_2 \gamma_{ij}^{(2)} + \cdots + \lambda_h \gamma_{ij}^{(h)}.$$

The determinant $\det(\gamma(\lambda))$ is a polynomial in $\lambda_1, \dots, \lambda_h$ with coefficients in $\Phi$. Since $\det(\gamma(\nu)) = \det(\mu) \neq 0$ (as $(\mu)$ is a change-of-basis matrix, hence invertible), this polynomial is not identically zero over $P$, and therefore not identically zero over $\Phi$.

Because $\Phi$ is infinite, there exist values $\lambda_k = \gamma_k \in \Phi$ such that $\det(\gamma(\gamma)) \neq 0$. The matrix $(\gamma) = (\gamma(\gamma))$ has entries in $\Phi$ and is invertible. Moreover, since each column of $(\gamma(\lambda))$ satisfies the linear equations for all $\lambda$, the matrix $(\gamma)$ satisfies

$$(\gamma)(\alpha) = (\beta')(\gamma)$$

for suitable $(\beta') \in \Phi_n$ (depending on $\alpha$). Thus

$$(\gamma)(\alpha)(\gamma)^{-1} = (\mu)(\alpha)(\mu)^{-1}$$

for every $(\alpha) \in \omega$, completing the proof.
