---
role: proof
locale: en
of_concept: product-with-limit-ordinal-is-limit
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** If $\alpha \neq 0$ and $\beta \in K_{\mathrm{II}}$, then $\alpha \cdot \beta \neq 0$ by Proposition 8.22. Therefore $\alpha \cdot \beta \in K_{\mathrm{II}}$ or $(\exists \gamma)[\gamma + 1 = \alpha \cdot \beta]$. If $\gamma + 1 = \alpha \cdot \beta$, then since $\beta \in K_{\mathrm{II}}$, $\alpha \cdot \beta = \bigcup_{\delta < \beta} \alpha \cdot \delta$. Hence $\gamma \in \bigcup_{\delta < \beta} \alpha \cdot \delta$, i.e., $(\exists \delta < \beta)[\gamma < \alpha \cdot \delta]$ (by Theorem 8.23). Then $\gamma + 1 \le \alpha \cdot \delta + 1 \le \alpha \cdot \delta + \alpha = \alpha \cdot (\delta + 1)$. But $\beta \in K_{\mathrm{II}}$ and $\delta < \beta$ implies $\delta + 1 < \beta$, so $\gamma + 1 \in \alpha \cdot (\delta + 1) \subseteq \bigcup_{\eta < \beta} \alpha \cdot \eta = \alpha \cdot \beta = \gamma + 1$, a contradiction. Thus $\alpha \cdot \beta \in K_{\mathrm{II}}$.
