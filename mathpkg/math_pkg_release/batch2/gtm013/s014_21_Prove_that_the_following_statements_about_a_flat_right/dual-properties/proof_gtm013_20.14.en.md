---
role: proof
locale: en
of_concept: dual-properties
source_book: gtm013
source_chapter: "20"
source_section: "20.14"
---

First observe that $\sigma_{M^*}: M^* \to M^{***}$ and $\sigma_M^*: M^{***} \to M^*$.

For (1): If $\gamma \in M^*$, then for all $m \in M$:

$$\sigma_{M^*}(\sigma_M^*(\gamma))(m) = (\sigma_M^*(\gamma) \circ \sigma_M)(m) = [\sigma_M(m)](\gamma) = \gamma(m).$$

Thus $\sigma_{M^*} \circ \sigma_M^* = 1_{M^*}$.

For (2): From (1) it follows that $\sigma_{M^*}$ is a (split) monomorphism, which is precisely the definition of $M^*$ being $U$-torsionless.

For (3): Suppose $\sigma_M$ is an isomorphism. Then so is $\sigma_M^*$ (since $(-)^*$ is a functor and preserves isomorphisms). But then (1) forces $\sigma_{M^*}$ to also be an isomorphism (as a retraction of an isomorphism), proving that $M^*$ is $U$-reflexive.
