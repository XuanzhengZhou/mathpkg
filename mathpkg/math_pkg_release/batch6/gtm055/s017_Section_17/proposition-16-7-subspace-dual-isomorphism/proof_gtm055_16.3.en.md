---
role: proof
locale: en
of_concept: proposition-16-7-subspace-dual-isomorphism
source_book: gtm055
source_chapter: "16"
source_section: "16.3"
---

The mapping $\hat{\beta}(f + \mathcal{M}^a) = f|_{\mathcal{M}}$ is well-defined because if $f_1 + \mathcal{M}^a = f_2 + \mathcal{M}^a$, then $f_1 - f_2 \in \mathcal{M}^a$, so $(f_1 - f_2)|_{\mathcal{M}} = 0$, hence $f_1|_{\mathcal{M}} = f_2|_{\mathcal{M}}$. Linearity is clear.

In the Banach space case, $\|\hat{\beta}(f + \mathcal{M}^a)\| = \|f|_{\mathcal{M}}\| \leq \|f\|$, and taking the infimum over representatives gives $\|\hat{\beta}(f + \mathcal{M}^a)\| \leq \|f + \mathcal{M}^a\|$, so $\|\hat{\beta}\| \leq 1$. Conversely, for any $g \in \mathcal{M}^*$, the Hahn–Banach theorem yields an extension $f_0 \in \mathcal{E}^*$ with $\|f_0\| = \|g\|$ and $f_0|_{\mathcal{M}} = g$. Then $\hat{\beta}(f_0 + \mathcal{M}^a) = g$ and
$$\|g\| = \|f_0\| \geq \|f_0 + \mathcal{M}^a\| \geq \|\hat{\beta}(f_0 + \mathcal{M}^a)\| = \|g\|,$$
where the last inequality uses $\|\hat{\beta}\| \leq 1$. Hence $\|\hat{\beta}(f_0 + \mathcal{M}^a)\| = \|f_0 + \mathcal{M}^a\| = \|g\|$, showing $\hat{\beta}$ is an isometry.
