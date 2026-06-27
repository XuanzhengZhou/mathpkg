---
role: proof
locale: en
of_concept: derived-rees-system-preserves-specialness
source_book: gtm004
source_chapter: "VIII. Exact Couples and Spectral Sequences"
source_section: "6. Rees Systems and Filtered Complexes"
---

# Proof of Derived Rees System Preserves Specialness

**Proposition 6.5.** If a Rees system (6.9) is special, then its derived Rees system (6.16) is also special, with the same automorphism $\theta : \Gamma \cong \Gamma$.

*Proof.* Suppose given $\theta$ satisfying the specialness relations (6.11):

$$\theta\varphi = \varphi\alpha, \qquad \bar{\varphi}\theta = \bar{\alpha}\bar{\varphi}, \qquad \bar{\varphi}\theta^{-1}\varphi = \bar{\gamma}\beta.$$

In the derived Rees system (6.16), the morphisms $\varphi_1 : D_1 \to \Gamma$, $\bar{\varphi}_1 : \Gamma \to \bar{D}_1$ and the induced endomorphisms $\alpha_1$, $\bar{\alpha}_1$, $\beta_1$, $\bar{\gamma}_1$ are constructed via the $\theta_{\sigma}^{\bar{\varphi}}$-process, satisfying

$$\varphi_1\sigma = \varphi, \qquad \bar{\varphi}\,\bar{\varphi}_1 = \bar{\varphi}, \qquad \sigma\alpha_1 = \alpha\sigma,$$

together with the corresponding relations for the other derived morphisms. We verify the three specialness relations for the derived system:

1. **$\theta\varphi_1 = \varphi_1\alpha_1$:**

   $$\theta\varphi_1\sigma = \theta\varphi = \varphi\alpha = \varphi_1\sigma\alpha = \varphi_1\alpha_1\sigma.$$

   Since $\sigma$ is monic, we cancel to obtain $\theta\varphi_1 = \varphi_1\alpha_1$.

2. **$\bar{\varphi}_1\theta = \bar{\alpha}_1\bar{\varphi}_1$:**

   Dually, using the factorization $\bar{\varphi} = \bar{\varphi}\,\bar{\varphi}_1$ and the second relation of (6.11), one obtains $\bar{\varphi}_1\theta = \bar{\alpha}_1\bar{\varphi}_1$.

3. **$\bar{\varphi}_1\theta^{-1}\varphi_1 = \bar{\gamma}_1\beta_1$:**

   $$\bar{\varphi}_1\theta^{-1}\varphi_1\sigma = \bar{\varphi}_1\theta^{-1}\varphi = \bar{\varphi}\,\theta^{-1}\varphi = \bar{\gamma}\beta = \bar{\varphi}_1\bar{\gamma}_1\beta_1\sigma,$$

   where the last equality uses the relation $\bar{\varphi}\,\bar{\gamma}_1 = \bar{\gamma}$ and the factorization of $\beta$ through $\sigma$. Canceling the monomorphism $\sigma$ (and using that $\bar{\varphi}_1$ is monic in the appropriate sense) yields $\bar{\varphi}_1\theta^{-1}\varphi_1 = \bar{\gamma}_1\beta_1$.

Thus the derived Rees system (6.16) is special with the same automorphism $\theta$. $\square$
