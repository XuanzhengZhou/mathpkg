---
role: proof
locale: en
of_concept: gauss-curvature-invariant-formula
source_book: gtm051
source_chapter: "5"
source_section: "5.1"
---

The above definitions involve tangent vectors, curves, and the Riemannian metric, all of which may be expressed in terms of a local coordinate system $(U, g)$. What needs to be verified is that these definitions are independent of choice of coordinate system.

1. Suppose $\phi: (V, \tilde{g}) \to (U, g)$ is an isometry. This means that
   $$\tilde{g}_{ij}(v) = \sum_{k,l} \frac{\partial u^k}{\partial v^i} \frac{\partial u^l}{\partial v^j} g_{kl}(\phi(v)).$$
   From this it is clear that length and energy are invariant under change of coordinates.

2. To show that the expression (4.1.2(*)) for the covariant derivative is coordinate invariant, it suffices to verify the transformation law (4.1.3) for the Christoffel symbols. This may be done by direct calculation. Alternatively, one can use the following argument: express $\tilde{g}_{pq}$ and $\tilde{\Gamma}_{pq}^r$ in terms of $g_{ik}$ and $\Gamma_{ik}^l$. Consider the transformation law (4.1.3) as an identity in which the $\Gamma_{ij}^k$ appear linearly, with coefficients of the form $\partial u^i/\partial v^p$, $\partial^2 u^i/\partial v^p \partial v^q$ and their products.

   Given $u_0 \in U$, there exists a surface $f: U \to \mathbb{R}^3$ such that the $g_{ij}(u_0)$ and $\Gamma_{ij}^k(u_0)$, defined by $f$, agree with those given by the Riemannian metric on $U$ at $u_0$. Since the identity (4.1.3) has already been verified for surfaces $f: U \to \mathbb{R}^3$, it then follows in the Riemannian case.

The invariance of the Gauss curvature $K = R_{1212}/\det(g_{ij})$ follows from the coordinate invariance of all quantities entering its definition.
