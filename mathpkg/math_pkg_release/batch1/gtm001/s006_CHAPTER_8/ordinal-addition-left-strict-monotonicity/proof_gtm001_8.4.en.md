---
role: proof
locale: en
of_concept: ordinal-addition-left-strict-monotonicity
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof** (By transfinite induction on $\beta$). For $\beta = \alpha + 1$ we have $\gamma + \alpha < (\gamma + \alpha) + 1 = \gamma + (\alpha + 1)$. If $\alpha < \beta \rightarrow \gamma + \alpha < \gamma + \beta$ and if $\alpha < \beta + 1$, then either $\alpha < \beta$ or $\alpha = \beta$. If $\alpha < \beta$, then by the induction hypothesis $\gamma + \alpha < \gamma + \beta < (\gamma + \beta) + 1 = \gamma + (\beta + 1)$. If $\alpha = \beta$, then $\gamma + \alpha = \gamma + \beta < (\gamma + \beta) + 1 = \gamma + (\beta + 1)$. If $\beta \in K_{\mathrm{II}}$ and $\alpha < \beta$, then $\alpha + 1 < \beta$ and by the induction hypothesis $\gamma + \alpha < \gamma + (\alpha + 1)$. Hence $\gamma + \alpha \in \gamma + (\alpha + 1) \subseteq \bigcup_{\delta < \beta} (\gamma + \delta) = \gamma + \beta$.
