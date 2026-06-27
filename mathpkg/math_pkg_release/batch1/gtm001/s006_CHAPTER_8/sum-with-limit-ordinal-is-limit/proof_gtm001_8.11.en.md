---
role: proof
locale: en
of_concept: sum-with-limit-ordinal-is-limit
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** If $\beta \in K_{\mathrm{II}}$, then $\alpha + \beta \neq 0$ since $\beta \neq 0$. Suppose $\alpha + \beta = \delta + 1$ for some $\delta$. Since $\beta \in K_{\mathrm{II}}$, $\alpha + \beta = \bigcup_{\gamma < \beta} (\alpha + \gamma)$. Then $\delta \in \delta + 1 = \alpha + \beta$, so $(\exists \gamma < \beta)[\delta \in \alpha + \gamma]$. That is, $\delta < \alpha + \gamma$. Then $\delta + 1 \leq \alpha + \gamma$. Since $\beta \in K_{\mathrm{II}}$ and $\gamma < \beta$, we have $\gamma + 1 < \beta$. Therefore

$$\delta + 1 \in \bigcup_{\gamma < \beta} (\alpha + \gamma) = \alpha + \beta = \delta + 1,$$

which is a contradiction. Hence $\alpha + \beta$ is not a successor, so $\alpha + \beta \in K_{\mathrm{II}}$.
