---
role: proof
locale: en
of_concept: chromatic-number-euler-characteristic-bound
source_book: gtm054
source_chapter: "VII"
source_section: "D"
---

The right-hand inequality follows from D3 and C6.

For the left-hand inequality, by A2, $\Gamma$ has a component $\Theta$ such that $\chi_0(\Theta) = \chi_0(\Gamma)$. If $\Theta$ is planar, then
$$\chi_0(\Gamma) = \chi_0(\Theta) \leq 5 < 6 \leq H(3, 2 - \varepsilon(\Gamma)),$$
since $\varepsilon(\Gamma) \leq 1$.

If $\Theta$ is nonplanar, then by C13, C6, D3, and the fact that $\varepsilon(\Theta) \geq \varepsilon(\Gamma)$, we have
$$\chi_0(\Gamma) = \chi_0(\Theta) \leq H(3, \iota(\Theta)) \leq H(3, 2 - \varepsilon(\Gamma)).$$
This proves the left-hand inequality.
