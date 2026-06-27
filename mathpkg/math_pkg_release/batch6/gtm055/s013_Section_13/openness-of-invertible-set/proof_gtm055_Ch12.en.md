---
role: proof
locale: en
of_concept: openness-of-invertible-set
source_book: gtm055
source_chapter: "12"
source_section: "Bounded linear transformations"
---

To verify the first part of the proposition it suffices to show that if $R$ is a left inverse of $T$ with $\| R \| = d$, and if $\| S - T \| < 1/d$, then $S$ is left invertible. But in these circumstances we have

$$\| 1_{\mathcal{E}} - RS \| = \| R(T - S) \| \leq \| R \| \| S - T \| < 1,$$

so that $RS$ is invertible by Lemma 12.8. Thus $(RS)^{-1}(RS) = 1$, and $(RS)^{-1}R$ is a left inverse of $S$.

To prove continuity of inversion, let $0 < \varepsilon < \frac{1}{2}$ and suppose that $T \in \mathcal{U}$ and that $\| S - T \| < \varepsilon/\| T^{-1} \|$. Then as above, $T^{-1}S$ is invertible, and a similar argument yields the continuity estimate.
