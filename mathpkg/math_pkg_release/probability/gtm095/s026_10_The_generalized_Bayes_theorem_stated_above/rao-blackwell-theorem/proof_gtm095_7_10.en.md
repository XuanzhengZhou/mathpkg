---
role: proof
locale: en
of_concept: rao-blackwell-theorem
source_book: gtm095
source_chapter: "7"
source_section: "10"
---

# Proof of the Rao-Blackwell Theorem

*Proof.* (a) The unbiasedness of $T = E_{\theta}(\hat{\theta} \mid \mathcal{G})$ follows directly from the tower property of conditional expectation:

$$E_{\theta} T = E_{\theta} \big[ E_{\theta}(\hat{\theta} \mid \mathcal{G}) \big] = E_{\theta} \hat{\theta} = \theta,$$

since $\hat{\theta}$ is unbiased by hypothesis. Thus $T$ is also an unbiased estimator for all $\theta \in \Theta$.

(b) For the mean-squared-error comparison, apply Jensen's inequality for conditional expectations (see Problem 5 in Section 12) with the convex function $g(x) = (x - \theta)^2$:

$$\big( E_{\theta}(\hat{\theta} \mid \mathcal{G}) - \theta \big)^2 = \big( E_{\theta}(\hat{\theta} - \theta \mid \mathcal{G}) \big)^2 \leq E_{\theta}\big[ (\hat{\theta} - \theta)^2 \mid \mathcal{G} \big] \quad (P_{\theta}\text{-a.s.}).$$

Now take the expectation $E_{\theta}(\cdot)$ on both sides. The left side becomes $E_{\theta}(T - \theta)^2$, while the right side becomes

$$E_{\theta}\Big[ E_{\theta}\big[ (\hat{\theta} - \theta)^2 \mid \mathcal{G} \big] \Big] = E_{\theta}(\hat{\theta} - \theta)^2,$$

again by the tower property. Hence

$$E_{\theta}(T - \theta)^2 \leq E_{\theta}(\hat{\theta} - \theta)^2, \quad \theta \in \Theta.$$

$\square$

**Remark.** The inequality is strict unless $\hat{\theta}$ is already $\mathcal{G}$-measurable (in which case $T = \hat{\theta}$ a.s.), or unless the convex function $g(x) = (x-\theta)^2$ is affine on the support of the conditional distribution. The theorem implies that any UMVUE, if one exists, must be a function of a sufficient statistic.
