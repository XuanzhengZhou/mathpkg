---
role: proof
locale: en
of_concept: power-of-power-property-for-ordinals
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (By transfinite induction on $\gamma$). For $\gamma = 0$: $(\alpha^\beta)^0 = 1 = \alpha^{\beta \cdot 0}$.

If $(\alpha^\beta)^\gamma = \alpha^{\beta \cdot \gamma}$, then

$$(\alpha^\beta)^{\gamma+1} = (\alpha^\beta)^\gamma \cdot \alpha^\beta = \alpha^{\beta \cdot \gamma} \cdot \alpha^\beta = \alpha^{\beta \cdot \gamma + \beta} = \alpha^{\beta \cdot (\gamma + 1)}.$$

If $\gamma \in K_{\mathrm{II}}$, then consider cases:
- If $\beta = 0$, then $(\alpha^0)^\gamma = 1^\gamma = 1 = \alpha^0 = \alpha^{0 \cdot \gamma} = \alpha^{\beta \cdot \gamma}$.
- If $\beta \neq 0$ and $\alpha = 0$, then $\alpha^\beta = 0$ so $(\alpha^\beta)^\gamma = 0^\gamma$. If $\gamma = 0$, this is $1$; if $\gamma > 0$, since $\gamma \in K_{\mathrm{II}}$, $0^\gamma = 0$. Meanwhile $\alpha^{\beta \cdot \gamma} = 0^{\beta \cdot \gamma}$. Since $\beta \neq 0$, $\beta \cdot \gamma$ is a limit ordinal (or $0$ if $\gamma = 0$). In all cases the equality holds.
- If $\alpha \neq 0$ and $\beta \neq 0$, then $\beta \cdot \gamma \in K_{\mathrm{II}}$ (by Proposition 8.24). Then

$$(\alpha^\beta)^\gamma = \bigcup_{\delta < \gamma} (\alpha^\beta)^\delta,$$
$$\alpha^{\beta \cdot \gamma} = \bigcup_{\eta < \beta \cdot \gamma} \alpha^\eta.$$

By Proposition 8.23, if $\eta < \beta \cdot \gamma$, there exists $\delta < \gamma$ such that $\eta < \beta \cdot \delta$. Then $\alpha^\eta \le \alpha^{\beta \cdot \delta} = (\alpha^\beta)^\delta$. Conversely, for $\delta < \gamma$, $\beta \cdot \delta < \beta \cdot \gamma$, so $(\alpha^\beta)^\delta = \alpha^{\beta \cdot \delta}$ appears in the union. Thus the two suprema are equal.
