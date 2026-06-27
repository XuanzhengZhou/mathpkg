---
role: proof
locale: en
of_concept: ordinal-addition-associativity
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (By transfinite induction on $\gamma$). For $\gamma = 0$: $(\alpha + \beta) + 0 = \alpha + \beta = \alpha + (\beta + 0)$. If $(\alpha + \beta) + \gamma = \alpha + (\beta + \gamma)$, then

$$(\alpha + \beta) + (\gamma + 1) = ((\alpha + \beta) + \gamma) + 1 = (\alpha + (\beta + \gamma)) + 1 = \alpha + ((\beta + \gamma) + 1) = \alpha + (\beta + (\gamma + 1)).$$

If $\gamma \in K_{\mathrm{II}}$ and $(\alpha + \beta) + \delta = \alpha + (\beta + \delta)$ for $\delta < \gamma$, then

$$(\alpha + \beta) + \gamma = \bigcup_{\delta < \gamma} ((\alpha + \beta) + \delta) = \bigcup_{\delta < \gamma} (\alpha + (\beta + \delta)).$$

Furthermore, since $\gamma \in K_{\mathrm{II}}$, by Proposition 8.11 we have $\beta + \gamma \in K_{\mathrm{II}}$. Therefore

$$\alpha + (\beta + \gamma) = \bigcup_{\eta < \beta + \gamma} (\alpha + \eta).$$

If $\delta < \gamma$ and $\eta = \beta + \delta$, then $\eta < \beta + \gamma$ and $\alpha + (\beta + \delta) \leq \alpha + \eta$. Conversely, if $\eta < \beta + \gamma$, then $\eta < \beta$ or $(\exists \delta < \gamma)[\eta = \beta + \delta]$. In either case, $\alpha + \eta$ is bounded by terms in the union over $\delta < \gamma$. Thus both unions are equal.
