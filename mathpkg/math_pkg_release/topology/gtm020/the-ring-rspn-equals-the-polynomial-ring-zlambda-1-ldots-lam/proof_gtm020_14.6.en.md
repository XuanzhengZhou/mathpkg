---
locale: en
of_concept: the-ring-rspn-equals-the-polynomial-ring-zlambda-1-ldots-lam
role: proof
source_book: gtm020
source_chapter: 14. Representation Rings of Classical Groups
source_section: '6'
---

As a $T(e_1, \ldots, e_n)$-module, $C^{2n} = H^n$ is a direct sum of $2n$ one-dimensional modules corresponding to $\alpha_1, \alpha_1^{-1}, \ldots, \alpha_n, \alpha_n^{-1}$, and the representation of $\lambda_k$ as the elementary symmetric function in $\alpha_1, \alpha_1^{-1}, \ldots, \alpha_n, \alpha_n^{-1}$ follows from Proposition 13(4.6). Since the Weyl group $W$ consists of all permutations of $\{1, \ldots, n\}$ composed with substitutions $\alpha_i \mapsto \alpha_i^{\pm 1}$, we have by (5.2) the inclusions $Z[\lambda_1, \ldots, \lambda_n] \subset RSp(n) \subset Z[\sigma_1, \ldots, \sigma_n] = Z[\alpha_1, \alpha_1^{-1}, \ldots, \alpha_n, \alpha_n^{-1}]^W$, where $\sigma_k$ is the $k$th elementary symmetric function in the

is $r$, where $n = 2r$ or $2r + 1$. The Weyl group $W$ of $SO(2r + 1)$ consists of the $2^r r!$ permutations of the indexes of $(\theta_1, \ldots, \theta_r)$ composed with substitutions $(\theta_1, \ldots, \theta_r) \mapsto (\pm \theta_1, \ldots, \pm \theta_r)$, and Weyl group $W$ of $SO(2r)$ consists of the $2^{r-1} r!$ permutations of the indexes of $(\theta_1, \ldots, \theta_r)$ composed with substitutions $(\theta_1, \ldots, \theta_r) \mapsto (\varepsilon_1 \theta_1, \ldots, \varepsilon_r \theta_r)$ with $\varepsilon_i = \pm 1$ and $\varepsilon_1 \cdots \varepsilon_r = 1$.

Proof. Clearly, $T(e_1, \ldots, e_n)$ is an $r$-dimensional torus $n = 2r$ or $2r + 1$. Since $wT(e_1, \ldots, e_n)w^{-1} = T(w(e_1), \ldots, w(e_n))$, we have only to show that each $u \in SO(n)$ is a member of some $T(x_1, \ldots, x_n)$ to prove the first two statements. For this, we let $c = a + ib$ be a complex eigenvalue of $u$ with eigenvector $x_1 + ix_2$. Then we have $u(x_1 + ix_2) = (a + ib)(x_1 + ix_2) = (ax_1 - bx_2) + i(bx_1 + ax_2)$. Since $|a + ib| = 1$, we can represent $u|(\mathbf{R}x_1 + \mathbf{R}x_2)$ by $D(\theta_1)$ for some $\theta_1$. If all eigenvalues are real, then $\theta_1 = 0$ or $1/2$ for $c = 1$ or $-

We have the following diagram where $T' = \omega(T(r))$.

Then ker $\omega$ consists of $(\theta_1, \ldots, \theta_r)$ with $\theta_i = 0$ or $1/2$ (mod 1) and $\theta_1 + \cdots + \theta_r = 0$ (mod 1), and there are $2^{r-1}$ elements in ker $\omega$. Then ker $\phi$ consists of two elements, 1 and $-1$. Note that we have $1 = \omega(\theta_1, \ldots, \theta_r)$ for $\theta_i = 0$ or $1/2$ (mod 1) and $\theta_1 + \cdots + \theta_r = 0$ (mod 1) and $-1 = \omega(\theta_1, \ldots, \theta_r)$ for $\theta_i = 0$ or $1/2$ (mod 1) and $\theta_1 + \cdots + \phi_r = 1/2$ (mod 1). Finally, we have $\phi \omega(\theta_1, \ldots, \theta_r) = (2\theta_1, \ldots, 2\theta_r)$ in $T(e_1, \ldots, e_n)$.
