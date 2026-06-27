---
role: proof
locale: en
of_concept: hom-symmetric-submanifold
source_book: gtm014
source_chapter: "VI"
source_section: "4. The $S_{r,s}$ Singularities"
---

The manifold structure on $\text{Hom}(V \circ V, W)_s$ is defined by requiring the map (4.5) to be a diffeomorphism. The proof that $\text{Hom}(V \circ V, W)_s$ is a submanifold of $\text{Hom}(V \circ V, W)$ uses Proposition 4.6 below.

For the dimension: the dimension of $\text{Hom}(V \circ V, W)_s$ equals the dimension of $\text{Hom}(Q \circ Q, W)_0$, where $Q$ is a quotient of $V$ of dimension $k - s$. The fiber dimension of $Q$ is $k - s$, so the fiber dimension of $\text{Hom}(Q \circ Q, W)_0$ is

$$\frac{(k-s)(k-s+1)l}{2}.$$

The dimension of the base space $G(s, V)$ (the Grassmannian of $s$-planes in $V$) is $s(k-s)$. Therefore the total dimension is

$$\frac{(k-s)(k-s+1)l}{2} + s(k-s),$$

and the codimension is as asserted.

Proposition 4.3 is valid for vector bundles as well: given vector bundles $E \to X$ and $F \to X$, the fiber bundle $\text{Hom}(E \circ E, F)_s$ (whose fiber at $p \in X$ is $\text{Hom}(E_p \circ E_p, F_p)_s$) is a fiber subbundle of $\text{Hom}(E \circ E, F)$, and its codimension is given by the same formula (4.4).
