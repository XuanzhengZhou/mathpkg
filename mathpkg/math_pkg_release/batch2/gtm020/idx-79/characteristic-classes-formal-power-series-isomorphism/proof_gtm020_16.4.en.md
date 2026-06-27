---
role: proof
locale: en
of_concept: characteristic-classes-formal-power-series-isomorphism
source_book: gtm020
source_chapter: "16"
source_section: "4"
---

We construct $a$ as follows: Let $a(\phi)(t) \in R[[t]]$ be such that $a(\phi)(c_1(\gamma)) = \phi(CP^n)\gamma$ in $H^{\text{ev}}(CP^n, R) = R[x] \bmod x^{n+1}$. This yields an inductive definition of the first $n$ coefficients of $a(\phi)(t)$ and displays the uniqueness of $a$.

If $\lambda$ is a line bundle over $X$, there is a map $f: X \rightarrow CP^n$ such that $f^*(\gamma)$ and $\lambda$ are $X$-isomorphic. Then we have $\phi(X)(\lambda) = f^*(\phi(CP^n)\gamma) = f^*[a(\phi)(c_1(\gamma))] = a(\phi)[f^*(c_1(\gamma))] = a(\phi)(c_1(\lambda))$. Similarly, $m$ is constructed in this unique way.

Next, for two characteristic classes $\phi$ and $\phi'$ we have $a(\phi + \phi')(c_1(\gamma)) = (\phi + \phi')(CP^n)\gamma = \phi(CP^n)\gamma + \phi'(CP^n)\gamma$ in $H^{\text{ev}}(CP^n, R) = R[x] \bmod x^{n+1}$. Consequently, $a(\phi + \phi')(t) \equiv a(\phi)(t) + a(\phi')(t) \bmod t^{n+1}$ for each $n$ and $a(\phi + \phi') = a(\phi) + a(\phi')$. Similarly, $m(\psi\psi') = m(\psi)m(\psi')$.

To prove that $a$ is injective, suppose that $a(\phi_1) = a(\phi_2)$. Then for a line bundle $\lambda$ over $X$ we have $\phi_1(X)\lambda = a(\phi_1)(c_1(\lambda)) = a(\phi_2)(c_1(\lambda)) = \phi_2(X)\lambda$. For a bundle $\xi$ over $X$, by the splitting principle, there exists a splitting map and the equality follows for all vector bundles.
