---
role: proof
locale: en
of_concept: left-distributivity-of-ordinal-multiplication
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (By transfinite induction on $\gamma$). For $\gamma = 0$, $\alpha \cdot (\beta + 0) = \alpha \cdot \beta = \alpha \cdot \beta + 0 = \alpha \cdot \beta + \alpha \cdot 0$. If $\alpha \cdot (\beta + \gamma) = \alpha \cdot \beta + \alpha \cdot \gamma$, then

$$\alpha \cdot (\beta + (\gamma + 1)) = \alpha \cdot ((\beta + \gamma) + 1) = \alpha \cdot (\beta + \gamma) + \alpha = (\alpha \cdot \beta + \alpha \cdot \gamma) + \alpha = \alpha \cdot \beta + (\alpha \cdot \gamma + \alpha) = \alpha \cdot \beta + \alpha \cdot (\gamma + 1).$$

If $\gamma \in K_{\mathrm{II}}$ and the equality holds for $\delta < \gamma$, then

$$\alpha \cdot (\beta + \gamma) = \bigcup_{\eta < \beta + \gamma} \alpha \cdot \eta,$$
$$\alpha \cdot \beta + \alpha \cdot \gamma = \bigcup_{\delta < \gamma} (\alpha \cdot \beta + \alpha \cdot \delta) = \bigcup_{\delta < \gamma} \alpha \cdot (\beta + \delta).$$

If $\eta < \beta + \gamma$, then $\eta < \beta$ or $(\exists \delta < \gamma)[\eta = \beta + \delta]$. If $\eta < \beta$, then $\alpha \cdot \eta < \alpha \cdot \beta \le \alpha \cdot \beta + \alpha \cdot \gamma$. If $\eta = \beta + \delta$ with $\delta < \gamma$, then $\alpha \cdot \eta = \alpha \cdot (\beta + \delta)$ is in the union. Conversely, if $\delta < \gamma$ and we set $\eta = \beta + \delta$, then $\eta < \beta + \gamma$ and $\alpha \cdot (\beta + \delta) \le \alpha \cdot \eta$. Thus both unions are equal. Hence $\alpha \cdot (\beta + \gamma) = \alpha \cdot \beta + \alpha \cdot \gamma$.
