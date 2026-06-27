---
role: proof
locale: en
of_concept: decomposition-of-collineation-group
source_book: gtm006
source_chapter: "VIII"
source_section: "3"
---

**Proof.** Let $\pi$ be any collineation in $\Pi$ and suppose $(m)^\pi = (0)$ and $(a, b)^\pi = (0, 0)$. Since $\mathcal{P}(D)$ is a translation plane there is a translation $\alpha$ with $(a, b)^\alpha = (0, 0)$ while the $([\infty], [0])$-transitivity of $\mathcal{P}(D)$ implies the existence of a $([\infty], [0])$-elation $\beta$ with $(m)^\beta = (0)$. The collineation $\alpha\beta$ is in $\Sigma$ and $(\alpha\beta)^{-1}\pi$ is in $\Lambda$, so that $\Pi = \Sigma \cdot \Lambda$.

Suppose $\gamma$ is in $\Sigma \cap \Lambda$. Then there exists a translation $\lambda$ and a shear $\mu$ such that $\gamma = \lambda\mu$. But $(0)^\gamma = (0)$, since $(0)$ is on the axis of $\lambda$, so that $(0) = (0)^\gamma = (0)^\lambda$. Thus, since the identity is the only shear fixing $(0)$, $\mu = 1$ and $\gamma = \lambda$ is a translation. But as $\gamma \in \Lambda$ fixes $(\infty)$ and $(0,0)$, and a non-identity translation cannot fix $(0,0)$, we must have $\gamma = 1$. Hence $\Sigma \cap \Lambda = 1$. $\square$
