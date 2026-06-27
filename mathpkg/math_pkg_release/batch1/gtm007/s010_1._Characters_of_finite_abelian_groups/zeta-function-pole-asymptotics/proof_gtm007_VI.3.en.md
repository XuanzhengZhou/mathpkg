---
role: proof
locale: en
of_concept: zeta-function-pole-asymptotics
source_book: gtm007
source_chapter: "VI"
source_section: "3"
---

Taking the logarithm of the Euler product $\zeta(s) = \prod_p (1 - p^{-s})^{-1}$ for $s > 1$, we obtain
$$\log \zeta(s) = \sum_p \sum_{m=1}^{\infty} \frac{1}{m p^{ms}} = \sum_p p^{-s} + \sum_p \sum_{m=2}^{\infty} \frac{1}{m p^{ms}}.$$

The double sum remains bounded as $s \to 1^+$, while $\log \zeta(s) \sim \log 1/(s-1)$ since $\zeta(s) \sim 1/(s-1)$. Hence $\sum_p p^{-s} \sim \log 1/(s-1)$.

