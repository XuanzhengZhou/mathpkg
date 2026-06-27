---
role: proof
locale: en
of_concept: intrinsic-derivative-via-normal-space
source_book: gtm014
source_chapter: "III"
source_section: "3"
---

The intrinsic derivative was defined in terms of a trivialization, so it suffices to prove the assertion for trivial bundles. Let $E = X \times \mathbf{R}^k$ and $F = X \times \mathbf{R}^l$ be product bundles. Then $\operatorname{Hom}(E, F) = X \times \operatorname{Hom}(\mathbf{R}^k, \mathbf{R}^l)$, and the map $\rho$ is given by a smooth family of matrices $A(x) \in \operatorname{Hom}(\mathbf{R}^k, \mathbf{R}^l)$.

The differential $(d\rho)_x$ maps $T_x X$ to $T_{A(x)} \operatorname{Hom}(\mathbf{R}^k, \mathbf{R}^l) = \operatorname{Hom}(\mathbf{R}^k, \mathbf{R}^l)$. For $\sigma = A(x) \in L^r(\mathbf{R}^k, \mathbf{R}^l)$, the tangent space $T_\sigma L^r(\mathbf{R}^k, \mathbf{R}^l)$ consists of those linear maps $B$ such that $B(K_\sigma) \subseteq \operatorname{Im} \sigma$. The normal space $N_\sigma$ is therefore naturally identified with $\operatorname{Hom}(K_\sigma, L_\sigma)$, since a linear map in $\operatorname{Hom}(\mathbf{R}^k, \mathbf{R}^l)$ is determined modulo $T_\sigma L^r$ by its restriction to $K_\sigma$ followed by projection to $L_\sigma = \mathbf{R}^l / \operatorname{Im} \sigma$.

The composite map $T_x X \to \operatorname{Hom}(\mathbf{R}^k, \mathbf{R}^l) \to \operatorname{Hom}(K_\sigma, L_\sigma)$ is precisely the intrinsic derivative as defined in the local (pedestrian) construction: the first map is $(d\rho)_x$, and the second map is restriction to $K_\sigma$ followed by projection to $L_\sigma$. Thus the composite coincides with $(D\rho)_x$.

For general (non-trivial) bundles, choose local trivializations and apply the above argument; the well-definedness of both constructions under changes of trivialization ensures the global equality.
