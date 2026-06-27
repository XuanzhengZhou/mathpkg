---
role: proof
locale: en
of_concept: alpha-beta-rightarrow-alphagamma-leq-betagamma
source_book: gtm001
source_chapter: "8"
source_section: ""
---

** (By transfinite induction on $\gamma$). For $\gamma = 0$ we have $\alpha^{0} = 1 = \beta^{0}$. Suppose that $\alpha < \beta$ and $\alpha^{\gamma} \leq \beta^{\gamma}$. Then $\alpha^{\gamma+1} = \alpha^{\gamma} \cdot \alpha \leq \beta^{\gamma} \cdot \alpha < \beta^{\gamma} \cdot \beta = \beta^{\gamma+1}$. If $\gamma \in K_{\text{II}}, \alpha < \beta$, and if $\alpha^{\delta} \leq \beta^{\delta}$ for $\delta < \gamma$ then

$$\alpha^{\gamma} = \bigcup_{\delta < \gamma} \alpha^{\delta} \leq \bigcup_{\delta < \gamma} \beta^{\delta} = \beta^{\gamma}.$$
