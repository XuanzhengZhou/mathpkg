---
role: proof
locale: en
of_concept: inverse-system-homeomorphism
source_book: gtm008
source_chapter: "22"
source_section: "The Completion of a Boolean Algebra"
---

The first assertion is verified by checking the definition of an o.c.o. (open continuous onto) inverse system: each $p_{\alpha\beta}$ is a projection, hence open, continuous, and onto, and the compatibility condition $p_{\alpha\beta} \circ p_{\beta\gamma} = p_{\alpha\gamma}$ holds by definition.

For the second assertion, the condition $\operatorname{cf}(\kappa) \geq \lambda$ ensures that every element of the $\lambda$-product $X$ is determined by its projections to the finite partial products $X^{\alpha}$. The map $f \mapsto (p_{\alpha}(f))_{\alpha < \kappa}$ gives a homeomorphism between $X$ and the inverse limit $\lim_{\alpha \to \kappa} X^{\alpha}$, where continuity and openness follow from the definition of the $\lambda$-product topology and the inverse limit topology.
