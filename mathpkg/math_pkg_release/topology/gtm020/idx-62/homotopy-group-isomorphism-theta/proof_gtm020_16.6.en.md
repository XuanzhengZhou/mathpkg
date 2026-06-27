---
role: proof
locale: en
of_concept: homotopy-group-isomorphism-theta
source_book: gtm020
source_chapter: "16"
source_section: "6"
---

Since $\operatorname{Map}_*(S^{n-1}, S^{n-1})$ is homeomorphic to the $H$-space $\Omega^{n-1}(S^{n-1})$, there are isomorphisms
$$\pi_k(H(n)) \cong \pi_k(M_n^1) \cong \pi_k(M_n^0) \cong \pi_k(\Omega^{n-1}(S^{n-1})) \cong \pi_{n+k-1}(S^{n-1})$$
for $1 \leq k \leq n-3$. The isomorphism $\theta$ is the composition.

Explicitly, for $[f] \in \pi_k(M_n^1)$, the map $f$ is the translation by the identity of $h': S^k \times S^{n-1} \to S^{n-1}$, where $h'(x, y) = *$ if either $x = *$ or $y = *$. Then $\theta([f])$ is the homotopy class of the adjoint map $S^{k+n-1} \cong S^k \wedge S^{n-1} \to S^{n-1}$.
