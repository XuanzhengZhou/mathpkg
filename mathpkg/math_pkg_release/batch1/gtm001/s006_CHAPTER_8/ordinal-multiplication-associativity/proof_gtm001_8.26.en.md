---
role: proof
locale: en
of_concept: ordinal-multiplication-associativity
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (By induction on $\gamma$). For $\gamma = 0$: $(\alpha \cdot \beta) \cdot 0 = 0 = \alpha \cdot 0 = \alpha \cdot (\beta \cdot 0)$. If $(\alpha \cdot \beta) \cdot \gamma = \alpha \cdot (\beta \cdot \gamma)$, then

$$(\alpha \cdot \beta) \cdot (\gamma + 1) = (\alpha \cdot \beta) \cdot \gamma + \alpha \cdot \beta = \alpha \cdot (\beta \cdot \gamma) + \alpha \cdot \beta = \alpha \cdot (\beta \cdot \gamma + \beta) = \alpha \cdot (\beta \cdot (\gamma + 1)).$$

If $\gamma \in K_{\mathrm{II}}$ and $\alpha \cdot \beta = 0$, then $\alpha = 0$ or $\beta = 0$, and $(\alpha \cdot \beta) \cdot \gamma = 0 = \alpha \cdot (\beta \cdot \gamma)$. If $\alpha \cdot \beta \neq 0$, then $\beta \cdot \gamma \in K_{\mathrm{II}}$ (by Proposition 8.24) and

$$(\alpha \cdot \beta) \cdot \gamma = \bigcup_{\delta < \gamma} (\alpha \cdot \beta) \cdot \delta,$$
$$\alpha \cdot (\beta \cdot \gamma) = \bigcup_{\eta < \beta \cdot \gamma} \alpha \cdot \eta.$$

But $\delta < \gamma \leftrightarrow \beta \cdot \delta < \beta \cdot \gamma$ (by Proposition 8.19, since $\beta \neq 0$). By the induction hypothesis, $(\alpha \cdot \beta) \cdot \delta = \alpha \cdot (\beta \cdot \delta)$. Therefore the two suprema are equal.
