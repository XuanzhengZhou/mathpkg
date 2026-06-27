---
role: proof
locale: en
of_concept: gcd-linear-combination-in-meromorphic-polynomial-ring
source_book: gtm038
source_chapter: "III"
source_section: "6"
---

**Proof of Theorem 6.6.**

Let $G \subset \mathbb{C}^n$ be a domain, $A = A(G)$ the ring of holomorphic functions on $G$, and $Q = Q(A)$ the field of meromorphic functions on $G$. The polynomial ring $Q[u]$ is a Euclidean ring with respect to the degree function.

Let $\omega_1, \omega_2 \in Q[u]$. Consider all linear combinations
$$\omega = p_1 \omega_1 + p_2 \omega_2$$
with $p_1, p_2 \in Q[u]$ and $\omega \neq 0$. Among these, choose $\omega$ of minimal degree. By the properties of Euclidean rings, this $\omega$ is a greatest common divisor of $\omega_1$ and $\omega_2$.

Now let $h \in A$ be the product of the denominators of $p_1$ and $p_2$ (when expressed as quotients of holomorphic functions). The polynomials $h \cdot p_i$ lie in $A[u]$, and we have
$$(h \cdot p_1) \omega_1 + (h \cdot p_2) \omega_2 = h \cdot \omega.$$
Since $h$ is a unit in $Q[u]$, multiplying by $h^{-1}$ yields that $\omega$ is a linear combination of $\omega_1$ and $\omega_2$ with coefficients in $A[u]$.
