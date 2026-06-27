---
role: proof
locale: en
of_concept: covering-transformation-fixed-point-free
source_book: gtm051
source_chapter: "6"
source_section: "6.7"
---

**Proof.** On the universal covering surface $\tilde{M}$ of $M$, $\gamma$ operates as a fixed-point free isometry: For suppose $\gamma(\tilde{p}) = \tilde{p}$. Then, if $(u_\alpha, \tilde{M}_\alpha)$ is a coordinate chart containing $\tilde{p}$, $\gamma$ has the local expression

$$u_\alpha \circ \mu \circ \gamma \circ \mu^{-1} \circ u_\alpha^{-1}: U_\alpha \rightarrow U_\alpha.$$

But since $\mu \circ \gamma = \mu$ (because $\gamma$ is a covering transformation), this map is equal to the identity. This means that $\gamma = \text{identity near } p$. By the simple connectivity of $\tilde{M}$ and the fact that the set of points where two isometries agree is open and closed, $\gamma = \text{id on } \tilde{M}$, which means $\gamma = 1$ is the neutral element of $\Gamma$. This contradicts the assumption that $\gamma \neq 1$. Therefore, no nontrivial element of $\Gamma$ can have a fixed point on $\tilde{M}$.
