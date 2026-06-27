---
role: proof
locale: en
of_concept: jump-across-boundary-arc-lemma
source_book: gtm035
source_chapter: "Chapter 19"
source_section: "19.2"
---

# Proof of Jump Formula Across Smooth Boundary Arc

**Proof.** We note that the hypothesis, that $\alpha$ is positively oriented for $U_j$, is equivalent to the identity $n_j = n_i + 1$ for the winding numbers. We represent $\gamma$ by the equation:

$$\eta = f(\zeta), \quad \zeta \in \pi(\gamma).$$

Fix $w$ with $|w| > R$. For $z \in U_i$ we have

$$\Phi(z, w) = \frac{1}{2\pi i} \int_{\gamma} \frac{\log(w - \eta)}{\zeta - z} d\zeta = \frac{1}{2\pi i} \int_{\pi(\gamma)} \frac{\log(w - f(\zeta))}{\zeta - z} d\zeta.$$

$\pi(\gamma)$ is the union of $\alpha$ and a complementary curve $\beta$. So

$$\Phi(z, w) = \frac{1}{2\pi i} \int_{\alpha} \frac{\log(w - f(\zeta))}{\zeta - z} d\zeta + \frac{1}{2\pi i} \int_{\beta} \frac{\log(w - f(\zeta))}{\zeta - z} d\zeta.$$

The integral over $\beta$ is analytic in $z$ across $\alpha$. Applying Plemelj's Theorem to the Cauchy-type integral over $\alpha$, we obtain that $\Phi$ has continuous extensions from $U_i$ and from $U_j$ to $\alpha$, and on $\alpha$ the jump is given by

$$\Phi_j(a, w) - \Phi_i(a, w) = \log(w - f(a)), \quad a \in \alpha, \; |w| > R.$$

Since $F(z, w) = e^{\Phi(z, w)}$, the corresponding extensions of $F_i$ and $F_j$ to $\alpha$ satisfy

$$F_j(a, w) = e^{\Phi_j(a, w)} = e^{\Phi_i(a, w) + \log(w - f(a))} = (w - f(a)) \cdot e^{\Phi_i(a, w)} = (w - f(a)) F_i(a, w).$$

This establishes both the continuity of the extensions and the jump relation. $\square$
