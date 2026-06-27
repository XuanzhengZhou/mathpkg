---
role: proof
locale: en
of_concept: neyman-fisher-factorization-theorem
source_book: gtm095
source_chapter: "7"
source_section: "10"
---

# Proof of the Neyman-Fisher Factorization Theorem

*Proof.* Let $\mathcal{P} = \{P_{\theta}, \theta \in \Theta\}$ be a dominated family with $P_{\theta} \ll \lambda$ for all $\theta$, where $\lambda$ is a $\sigma$-finite measure. We establish both directions of the equivalence.

**Sufficiency $\Rightarrow$ factorization.** Suppose $\mathcal{G}$ is sufficient for $\mathcal{P}$. Introduce the measure $\tilde{\lambda} = \sum_{k=1}^{\infty} c_k P_{\theta_k}$ with $c_k > 0$, $\sum c_k = 1$, chosen so that $\tilde{\lambda}$ is a probability measure equivalent to the family $\mathcal{P}$ (i.e., $P_{\theta} \ll \tilde{\lambda}$ and $\tilde{\lambda} \ll \sum P_{\theta}$; this is possible because the family is dominated). Then by the formula for recalculating conditional expectations (see (44) in the text), for any $\mathcal{F}$-measurable bounded random variable $X = X(\omega)$,

$$E_{\theta}(X \mid \mathcal{G}) = \frac{E_{\tilde{\lambda}}\!\left( X \frac{dP_{\theta}}{d\tilde{\lambda}} \mid \mathcal{G} \right)}{E_{\tilde{\lambda}}\!\left( \frac{dP_{\theta}}{d\tilde{\lambda}} \mid \mathcal{G} \right)} \quad (P_{\theta}\text{-a.s.}).$$

By the chain rule for Radon-Nikodym derivatives,

$$g_{\theta}^{(\tilde{\lambda})} = \frac{dP_{\theta}}{d\tilde{\lambda}} = \frac{dP_{\theta}}{d\lambda} \cdot \frac{d\lambda}{d\tilde{\lambda}} = g_{\theta}^{(\lambda)} \frac{d\lambda}{d\tilde{\lambda}}.$$

If we assume the factorization representation

$$g_{\theta}^{(\lambda)}(\omega) = \hat{g}_{\theta}^{(\lambda)}(\omega) \, h(\omega)$$

with $\hat{g}_{\theta}^{(\lambda)}$ being $\mathcal{G}$-measurable, then

$$g_{\theta}^{(\tilde{\lambda})} = \hat{g}_{\theta}^{(\lambda)} \, h \, \frac{d\lambda}{d\tilde{\lambda}}.$$

Substituting into the formula for $E_{\theta}(X \mid \mathcal{G})$ and noting that the $\mathcal{G}$-measurable factor $\hat{g}_{\theta}^{(\lambda)}$ cancels from numerator and denominator, we obtain

$$E_{\theta}(X \mid \mathcal{G}) = \frac{E_{\tilde{\lambda}}\!\left( X \, h \, \frac{d\lambda}{d\tilde{\lambda}} \mid \mathcal{G} \right)}{E_{\tilde{\lambda}}\!\left( h \, \frac{d\lambda}{d\tilde{\lambda}} \mid \mathcal{G} \right)} \quad (P_{\theta}\text{-a.s.}).$$

The right-hand side does not depend on $\theta$, which means that $\mathcal{G}$ is sufficient. Moreover, if we take $\lambda = P_{\theta_0}$, then sufficiency of $\mathcal{G}$ directly yields the factorization with $\hat{g}_{\theta}^{(\theta_0)} = g_{\theta}^{(\theta_0)}$ and $h \equiv 1$.

**Factorization $\Rightarrow$ sufficiency.** Conversely, suppose the densities factorize as

$$\frac{dP_{\theta}}{d\lambda}(\omega) = \hat{g}_{\theta}^{(\lambda)}(\omega) \, h(\omega),$$

where $\hat{g}_{\theta}^{(\lambda)}$ is $\mathcal{G}$-measurable and $h$ is independent of $\theta$. Consider the measure $\tilde{\lambda}$ as above and write

$$g_{\theta}^{(\tilde{\lambda})} = \frac{dP_{\theta}}{d\tilde{\lambda}}.$$

For any $\mathcal{F}$-measurable bounded $X$, the formula for $E_{\theta}(X \mid \mathcal{G})$ again involves the ratio

$$\frac{E_{\tilde{\lambda}}\!\left( X \frac{dP_{\theta}}{d\tilde{\lambda}} \mid \mathcal{G} \right)}{E_{\tilde{\lambda}}\!\left( \frac{dP_{\theta}}{d\tilde{\lambda}} \mid \mathcal{G} \right)}.$$

Writing $\frac{dP_{\theta}}{d\tilde{\lambda}} = \frac{dP_{\theta}}{d\lambda} \cdot \frac{d\lambda}{d\tilde{\lambda}} = \hat{g}_{\theta}^{(\lambda)} \, h \, \frac{d\lambda}{d\tilde{\lambda}}$ and canceling the $\mathcal{G}$-measurable factor $\hat{g}_{\theta}^{(\lambda)}$ yields an expression independent of $\theta$. Hence $\mathcal{G}$ is sufficient.

In particular, when $\lambda = P_{\theta_0}$ for some $\theta_0 \in \Theta$, we have the simpler factorization

$$\frac{dP_{\theta}}{dP_{\theta_0}} = \hat{g}_{\theta}^{(\theta_0)} \quad \text{and} \quad h = \frac{dP_{\theta_0}}{d\lambda},$$

recovering the general form (48) from the text.

$\square$
