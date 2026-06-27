---
role: proof
locale: en
of_concept: proposition-8-39-
source_book: gtm001
source_chapter: "8"
source_section: ""
---

** (1) If $\alpha > 1$, then $\alpha^{\beta} \geq 1$ and hence $\alpha^{\beta} \neq 0$. Therefore $\alpha^{\beta} \in K_{\mathrm{II}}$ or $(\exists \delta)[\delta + 1 = \alpha^{\beta}].$ Since $\beta \in K_{\mathrm{II}}$ and $\alpha \neq 0$
$$\alpha^{\beta} = \bigcup_{\gamma < \beta} \alpha^{\gamma}.$$
But $\delta \in \delta + 1 = \alpha^{\beta}$. Consequently $(\exists \gamma < \beta)[\delta < \alpha^{\gamma}].$ Since $1 < \alpha$, and $\delta < \alpha^{\gamma}$ it follows that $\delta + 1 \leq \alpha^{\gamma} < \alpha^{\gamma+1}$. But $\gamma + 1 < \beta$ and so $\delta + 1 \in \alpha^{\beta} = \delta + 1$. From this contradiction we conclude that
$$\alpha^{\beta} \in K_{\mathrm{II}}.$$
(2) If $\beta \in K_{\mathrm{II}}$ then $\alpha^{\beta} \in K_{\mathrm{II}}$ by (1) above. If $\beta \in K_{\mathrm{I}}$ then since $\beta \neq 0$, $(\exists \delta)[\beta = \delta

Thus $\alpha^{\beta} \cdot \alpha^{\gamma} \leq \alpha^{\beta+ \gamma}$. Furthermore if $\eta < \beta + \gamma$ then $\eta \leq \beta$ or $(\exists \tau)[\eta = \beta + \tau]$ Suppose that $\eta \leq \beta$. Then

$$\alpha^{\eta} \leq \alpha^{\beta} \cdot 1 \wedge 1 < \alpha^{\gamma}.$$

On the other hand if $\eta = \beta + \tau$, then $\tau < \gamma$. Hence $\alpha^{\beta+\tau} = \alpha^{\beta} \cdot \alpha^{\tau}$ and

$$\alpha^{\eta} = \alpha^{\beta+\tau} = \alpha^{\beta} \cdot \alpha^{\tau} \wedge \alpha^{\tau} < \alpha^{\gamma}.$$

Thus $\alpha^{\beta} \cdot \alpha^{\gamma} = \alpha^{\beta+ \gamma}$.
