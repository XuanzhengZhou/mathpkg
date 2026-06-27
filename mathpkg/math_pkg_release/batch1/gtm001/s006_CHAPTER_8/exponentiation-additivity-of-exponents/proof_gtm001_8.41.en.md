---
role: proof
locale: en
of_concept: exponentiation-additivity-of-exponents
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (By transfinite induction on $\gamma$). For $\gamma = 0$: $\alpha^{\beta+0} = \alpha^\beta = \alpha^\beta \cdot 1 = \alpha^\beta \cdot \alpha^0$.

If $\alpha^{\beta+\gamma} = \alpha^\beta \cdot \alpha^\gamma$, then

$$\alpha^{\beta+(\gamma+1)} = \alpha^{(\beta+\gamma)+1} = \alpha^{\beta+\gamma} \cdot \alpha = (\alpha^\beta \cdot \alpha^\gamma) \cdot \alpha = \alpha^\beta \cdot (\alpha^\gamma \cdot \alpha) = \alpha^\beta \cdot \alpha^{\gamma+1}.$$

If $\gamma \in K_{\mathrm{II}}$ and the equality holds for $\delta < \gamma$, then

$$\alpha^{\beta+\gamma} = \bigcup_{\eta < \beta+\gamma} \alpha^\eta,$$
$$\alpha^\beta \cdot \alpha^\gamma = \alpha^\beta \cdot \bigcup_{\delta < \gamma} \alpha^\delta = \bigcup_{\delta < \gamma} (\alpha^\beta \cdot \alpha^\delta) = \bigcup_{\delta < \gamma} \alpha^{\beta+\delta}.$$

For any $\eta < \beta+\gamma$, either $\eta \le \beta$ or $\eta = \beta + \delta$ for some $\delta < \gamma$. If $\eta \le \beta$, then $\alpha^\eta \le \alpha^\beta \cdot 1 \le \alpha^\beta \cdot \alpha^\gamma$. If $\eta = \beta + \delta$ with $\delta < \gamma$, then $\alpha^\eta = \alpha^{\beta+\delta} = \alpha^\beta \cdot \alpha^\delta \le \alpha^\beta \cdot \alpha^\gamma$. Conversely, each $\alpha^{\beta+\delta}$ (for $\delta < \gamma$) appears in the union defining $\alpha^{\beta+\gamma}$ (since $\beta+\delta < \beta+\gamma$). Thus both sides are equal.
