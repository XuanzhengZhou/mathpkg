---
role: proof
locale: en
of_concept: exterior-powers-integral-invariant
source_book: gtm060
source_chapter: "8"
source_section: "38"
---

Since the symplectic form $\omega^2$ is an integral invariant of the Hamiltonian phase flow $g^t$, we have $(g^t)^* \omega^2 = \omega^2$. The pullback commutes with the wedge product:
$$
(g^t)^*(\omega^2 \wedge \omega^2) = (g^t)^*\omega^2 \wedge (g^t)^*\omega^2 = \omega^2 \wedge \omega^2 = (\omega^2)^2.
$$
By induction, $(g^t)^*(\omega^2)^k = (\omega^2)^k$ for all $k \geq 1$. Therefore each $(\omega^2)^k$ is an integral invariant of $g^t$.

The vanishing $(\omega^2)^k = 0$ for $k > n$ follows from the fact that $\omega^2$ is a $2$-form on a $2n$-dimensional manifold; any exterior power of degree higher than $2n$ (i.e., $k > n$ since $\deg((\omega^2)^k) = 2k$) exceeds the dimension of the manifold and must vanish.

The top-degree form $(\omega^2)^n$ is nondegenerate, hence defines a volume element. Its invariance under $g^t$ yields volume preservation, recovering Liouville's theorem as a special case.
