---
role: proof
locale: en
of_concept: ordinal-addition-right-weak-monotonicity
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (By transfinite induction on $\gamma$). If $\alpha \le \beta$, then $\alpha + 0 = \alpha \le \beta = \beta + 0$. If $\alpha + \gamma \le \beta + \gamma$, then $\alpha + (\gamma + 1) = (\alpha + \gamma) + 1 \le (\beta + \gamma) + 1 = \beta + (\gamma + 1)$. If $\gamma \in K_{\mathrm{II}}$ and $(\forall \delta < \gamma)[\alpha + \delta \le \beta + \delta]$, then

$$\alpha + \gamma = \bigcup_{\delta < \gamma} (\alpha + \delta) \le \bigcup_{\delta < \gamma} (\beta + \delta) = \beta + \gamma.$$
