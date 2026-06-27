---
role: proof
locale: en
of_concept: alpha-betagamma-alphabeta-gamma
source_book: gtm001
source_chapter: "8"
source_section: ""
---

(By induction on $\gamma$). For $\gamma = 0$ we have $(\alpha \beta)\cdot 0 = 0 = \alpha \cdot 0 = \alpha(\beta \cdot 0)$. If $(\alpha \beta)\gamma = \alpha(\beta \gamma)$ then $(\alpha \beta)(\gamma + 1) = (\alpha \beta)\gamma + \alpha \beta = \alpha(\beta \gamma) + \alpha \beta = \alpha(\beta \gamma + \beta) = \alpha(\beta(\gamma + 1))$. If $\gamma \in K_{\text{II}}$ and $\alpha \beta = 0$ then $\alpha = 0$ or $\beta = 0$ and $(\alpha \beta)\gamma = 0 = \alpha(\beta \gamma)$. If $\alpha \beta \neq 0$ then $\beta \gamma \in K_{\text{II}}$ and hence
$$(\alpha \beta)\gamma = \bigcup_{\delta < \gamma}(\alpha \beta)\delta,$$
$$\alpha(\beta \gamma) = \bigcup_{\eta < \beta \gamma}\alpha \eta.$$
But $\delta < \gamma \leftrightarrow \beta \delta < \beta \gamma$. Therefore $(\alpha \

By Proposition 8.27 $(\exists! \gamma)(\exists! \delta)[m = n\gamma + \delta \wedge \delta < n]$. But $n\gamma + \delta \in \omega$ implies $n\gamma \in \omega$ and $\delta \in \omega$. Furthermore if $1 \leq n$, then $\gamma \leq n\gamma$. Therefore $\gamma \in \omega$.
