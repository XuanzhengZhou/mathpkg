---
role: proof
locale: en
of_concept: equality-of-uf-and-ug-for-equivalent-dirichlet-series
source_book: gtm041
source_chapter: "8"
source_section: "8.9"
---

Let $B = \{\beta(n)\}$ be a basis for the sequence $\Lambda$ of exponents. If $f(s) = \sum a(n)e^{-s\lambda(n)}$ and $g(s) = \sum b(n)e^{-s\lambda(n)}$ then there is a real sequence $\{y_k\}$ such that

$$b(n) = a(n) \exp \left\{ -i \sum_{k=1}^{q(n)} r_{n,k} y_k \right\}.$$

The Bohr series of $f$ and $g$ are given by

$$F(z_1, z_2, \ldots) = \sum_{n=1}^{\infty} a(n) \exp \left\{ -\sum_{k=1}^{q(n)} r_{n,k} z_k \right\}$$

and

$$G(z_1, z_2, \ldots) = \sum_{n=1}^{\infty} b(n) \exp \left\{ -\sum_{k=1}^{q(n)} r_{n,k} z_k \right\}.$$

Expressing the $b(n)$ in terms of the $a(n)$ we find

$$G(z_1, z_2, \ldots) = \sum_{n=1}^{\infty} a(n) \exp \left\{ -\sum_{k=1}^{q(n)} r_{n,k}(z_k + iy_k) \right\} = F(z_1 + iy_1, z_2 + iy_2, \ldots).$$

Now the set $U_f(\sigma_0)$ is the set of values taken by $F$ at points $z_k = \sigma_0 \beta(k)$ with the real parts fixed. Since $G$ is obtained from $F$ by translating each variable $z_k$ by the purely imaginary quantity $iy_k$, the sets of values taken by $F$ and $G$ on the corresponding domains coincide. Therefore $U_f(\sigma_0) = U_g(\sigma_0)$.
