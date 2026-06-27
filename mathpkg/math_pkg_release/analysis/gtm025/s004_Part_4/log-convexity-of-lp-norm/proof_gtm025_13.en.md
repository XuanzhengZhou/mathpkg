---
role: proof
locale: en
of_concept: log-convexity-of-lp-norm
source_book: gtm025
source_chapter: "4"
source_section: "13"
---

Apply Holder's inequality with exponents $1/\alpha$ and $1/(1-\alpha)$: $\int |f|^r d\mu = \int |f|^{\alpha p} |f|^{(1-\alpha)q} d\mu \leq (\int |f|^p d\mu)^{\alpha} (\int |f|^q d\mu)^{1-\alpha}$. Taking logarithms yields convexity of $\varphi$.
