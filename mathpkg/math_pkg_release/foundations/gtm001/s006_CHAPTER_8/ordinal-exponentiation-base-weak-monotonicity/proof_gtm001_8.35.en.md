---
role: proof
locale: en
of_concept: ordinal-exponentiation-base-weak-monotonicity
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (By transfinite induction on $\gamma$). For $\gamma = 0$: $\alpha^0 = 1 = \beta^0$. Suppose $\alpha < \beta$ and $\alpha^\gamma \le \beta^\gamma$. Then

$$\alpha^{\gamma+1} = \alpha^\gamma \cdot \alpha \le \beta^\gamma \cdot \alpha < \beta^\gamma \cdot \beta = \beta^{\gamma+1},$$

where the strict inequality uses Proposition 8.19 (left strict monotonicity of multiplication) since $\beta^\gamma > 0$ (if $\beta^\gamma = 0$ then $\beta = 0$, contradicting $\alpha < \beta$). If $\gamma \in K_{\mathrm{II}}$, $\alpha < \beta$, and $\alpha^\delta \le \beta^\delta$ for $\delta < \gamma$, then

$$\alpha^\gamma = \bigcup_{\delta < \gamma} \alpha^\delta \le \bigcup_{\delta < \gamma} \beta^\delta = \beta^\gamma.$$
