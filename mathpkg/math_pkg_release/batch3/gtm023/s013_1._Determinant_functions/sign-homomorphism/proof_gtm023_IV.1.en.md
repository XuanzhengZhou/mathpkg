---
role: proof
locale: en
of_concept: sign-homomorphism
source_book: gtm023
source_chapter: "IV"
source_section: "§1. Determinant functions"
---

Define $\Phi: \mathbb{Z}^p \to \mathbb{Z}$ by
$$\Phi(x_1, \ldots, x_p) = \prod_{i < j} (x_i - x_j), \quad x_i \in \mathbb{Z}.$$
For each $\sigma \in S_p$, the permuted map $(\sigma\Phi)(x_1,\ldots,x_p) = \Phi(x_{\sigma(1)},\ldots,x_{\sigma(p)})$ simply reorders the differences $x_i - x_j$. Since each transposition changes the sign of $\Phi$, in general $\sigma\Phi = \varepsilon_\sigma \cdot \Phi$ with $\varepsilon_\sigma = \pm 1$. The identities
$$\tau(\sigma\Phi) = (\tau\sigma)\Phi \quad \text{and} \quad \iota\Phi = \Phi$$
(equations 4.1 and 4.2) imply
$$\varepsilon_{\tau\sigma} \cdot \Phi = (\tau\sigma)\Phi = \tau(\sigma\Phi) = \tau(\varepsilon_\sigma \Phi) = \varepsilon_\sigma (\tau\Phi) = \varepsilon_\sigma \varepsilon_\tau \cdot \Phi,$$
hence $\varepsilon_{\tau\sigma} = \varepsilon_\tau \cdot \varepsilon_\sigma$. Similarly, $\iota\Phi = \Phi$ gives $\varepsilon_\iota = 1$. Thus $\varepsilon$ is a homomorphism from $S_p$ to $\{-1, +1\}$.
