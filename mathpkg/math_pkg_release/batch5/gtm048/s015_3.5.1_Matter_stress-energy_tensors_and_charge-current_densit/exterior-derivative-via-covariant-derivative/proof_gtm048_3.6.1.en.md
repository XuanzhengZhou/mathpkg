---
role: proof
locale: en
of_concept: exterior-derivative-via-covariant-derivative
source_book: gtm048
source_chapter: "3"
source_section: "3.6.1"
---

We first show that the right-hand side $\omega^i \wedge D_{X_i} \eta$ is independent of the choice of basis $\{X_i\}$. Given any two bases, their transformation is linear with smooth coefficients, and a direct algebraic computation using the properties of the wedge product and the covariant derivative shows that the expression is invariant under change of basis. Hence it is globally defined on $M$.

Since both sides are tensor fields on $M$, it suffices to prove equality at each $x \in M$. We may thus assume that $\{X_i\}$ is a basis of coordinate vector fields $\{\partial_i\}$ that is normal at $x$ (i.e., $D\partial_i(x) = 0$ and $[\partial_i, \partial_j](x) = 0$). In this coordinate neighborhood, writing $\eta = \eta_{j_1 \dots j_p} dx^{j_1} \wedge \dots \wedge dx^{j_p}$, we have at $x$:

$$D_{\partial_i} \eta = (\partial_i \eta_{j_1 \dots j_p}) dx^{j_1} \wedge \dots \wedge dx^{j_p},$$

since the connection coefficients vanish at $x$. Contracting with $dx^i$ via the wedge product yields

$$\omega^i \wedge D_{X_i} \eta = dx^i \wedge (\partial_i \eta_{j_1 \dots j_p}) dx^{j_1} \wedge \dots \wedge dx^{j_p} = (\partial_i \eta_{j_1 \dots j_p}) dx^i \wedge dx^{j_1} \wedge \dots \wedge dx^{j_p}$$

at the point $x$, which is precisely the coordinate expression for $d\eta$ at $x$.
