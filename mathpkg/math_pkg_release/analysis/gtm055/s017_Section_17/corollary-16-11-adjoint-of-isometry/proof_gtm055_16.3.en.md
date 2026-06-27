---
role: proof
locale: en
of_concept: corollary-16-11-adjoint-of-isometry
source_book: gtm055
source_chapter: "16"
source_section: "16.3"
---

Since $T$ is an isometric isomorphism we have $\|T\| = \|T^{-1}\| = 1$. By Proposition 16.9, $\|T^*\| = \|T\| = 1$, and by Corollary 16.10, $(T^*)^{-1} = (T^{-1})^*$, so $\|(T^*)^{-1}\| = \|(T^{-1})^*\| = \|T^{-1}\| = 1$.

Hence for every $f \in \mathcal{F}^*$,
$$\|f\| = \|(T^*)^{-1}(T^* f)\| \leq \|(T^*)^{-1}\| \|T^* f\| = \|T^* f\| \leq \|T^*\| \|f\| = \|f\|.$$

Thus $\|T^* f\| = \|f\|$ for all $f \in \mathcal{F}^*$, which shows that $T^*$ is an isometry and therefore an isometric isomorphism.
