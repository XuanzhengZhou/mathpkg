---
role: proof
locale: en
of_concept: kummer-cyclotomic-factorization-criterion
source_book: gtm050
source_chapter: "4"
source_section: "4.4"
---

**Proof (sketch, following Kummer).** Let $p \equiv 1 \pmod{\lambda}$ be a rational prime and let $\alpha$ be a primitive $\lambda$-th root of unity. In the cyclotomic integer ring $\mathbb{Z}[\alpha]$, the prime $p$ splits into $\lambda-1$ distinct prime factors. This follows from the factorization of the cyclotomic polynomial $\Phi_\lambda(X) = X^{\lambda-1} + X^{\lambda-2} + \cdots + X + 1$ modulo $p$.

Let $h$ be a primitive root modulo $p$. Since the multiplicative group $(\mathbb{Z}/p\mathbb{Z})^\times$ is cyclic of order $p-1$, and $\lambda \mid p-1$, the element $k \equiv h^{(p-1)/\lambda} \pmod{p}$ has multiplicative order $\lambda$ modulo $p$. The polynomial $X^\lambda - 1$ factors as $(X - 1)\prod_{j=1}^{\lambda-1}(X - k^j)$ modulo $p$. Since $\Phi_\lambda(X) \mid (X^\lambda - 1)/(X - 1)$, the residues $k, k^2, \ldots, k^{\lambda-1}$ are precisely the roots of $\Phi_\lambda(X)$ modulo $p$.

Reducing the ring $\mathbb{Z}[\alpha]$ modulo $p$ yields the isomorphism

$$
\mathbb{Z}[\alpha] / p\mathbb{Z}[\alpha] \cong \mathbb{F}_p[X] / \Phi_\lambda(X) \cong \prod_{j=1}^{\lambda-1} \mathbb{F}_p[X] / (X - k^j) \cong \prod_{j=1}^{\lambda-1} \mathbb{F}_p,
$$

where the Chinese Remainder Theorem splits $\Phi_\lambda(X)$ into linear factors over $\mathbb{F}_p$. Under this isomorphism, the image of $\alpha$ in the $j$-th component is $k^j$, so a cyclotomic integer $g(\alpha)$ maps to $(g(k), g(k^2), \ldots, g(k^{\lambda-1}))$ in the product $\prod_{j=1}^{\lambda-1} \mathbb{F}_p$.

Therefore, $g(\alpha)$ lies in the prime ideal corresponding to the $j$-th factor (i.e., $g(\alpha) \equiv 0$ modulo that prime divisor of $p$) if and only if its $j$-th coordinate vanishes, which means $g(k^j) \equiv 0 \pmod{p}$.

**Computational application.** To find explicit prime factors of $p$, one seeks a cyclotomic integer $g(\alpha)$ with small coefficients such that $g(k^j) \equiv 0 \pmod{p}$ for some $j$. If additionally $N(g(\alpha)) = p$, then $g(\alpha)$ is itself a prime factor. For example, when $\lambda = 7$, $p = 29$, take $h = 2$ (a primitive root mod 29) and $k \equiv 2^{28/7} \equiv 2^4 \equiv 16 \equiv -13 \pmod{29}$. Then $g(\alpha) = \alpha^2 - \alpha^4 + 1$ satisfies $g(-13) \equiv (-13)^2 - (-13)^4 + 1 \equiv 169 - 28561 + 1 \equiv 0 \pmod{29}$, and a computation shows $N(g(\alpha)) = 29$, confirming that $g(\alpha)$ is a prime factor of 29.
