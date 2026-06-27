---
role: proof
locale: en
of_concept: automorphism-group-hyperplane-invariant
source_book: gtm049
source_chapter: "3"
source_section: "3.6"
---

The mapping $\rho: \pi \mapsto \alpha$ where $\alpha = \pi|_A$ is precisely the restriction map from Proposition 3. By Proposition 3, every $\pi \in (\operatorname{Aut} \mathcal{P}(V))_H$ restricts to an affine isomorphism $\alpha \in \operatorname{Aut} \mathcal{A}$, and conversely every $\alpha$ extends uniquely to a $\pi$ with $H\pi = H$. This gives a bijection.

To see that $\rho$ is a homomorphism, note that if $\pi_1, \pi_2 \in (\operatorname{Aut} \mathcal{P}(V))_H$, then $(\pi_1\pi_2)|_A = \pi_1|_A \circ \pi_2|_A = \alpha_1\alpha_2$, since both $\pi_1$ and $\pi_2$ map $A$ to itself (as they preserve $H$). Thus $(\pi_1\pi_2)\rho = (\pi_1\rho)(\pi_2\rho)$.

The restriction to $(\operatorname{Pr} \mathcal{P}(V))_H$ gives an isomorphism onto $\operatorname{Af} \mathcal{A}$ by the second part of Proposition 3 (a projective isomorphism restricts to an affinity if and only if it is a projectivity).
