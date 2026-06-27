---
role: proof
locale: en
of_concept: ordinal-exponentiation-base-strict-monotonicity-successor
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** If $\gamma \in K_{\mathrm{I}}$ and $\gamma \neq 0$, then $\gamma = \delta + 1$ for some $\delta$. Then from Proposition 8.35, $\alpha^\delta \le \beta^\delta$. Hence

$$\alpha^\gamma = \alpha^{\delta+1} = \alpha^\delta \cdot \alpha \le \beta^\delta \cdot \alpha.$$

Since $\alpha < \beta$ and $\beta^\delta > 0$ (if $\beta^\delta = 0$, then $\beta = 0$, contradicting $\alpha < \beta$), by Proposition 8.19 we have $\beta^\delta \cdot \alpha < \beta^\delta \cdot \beta = \beta^{\delta+1} = \beta^\gamma$. Thus $\alpha^\gamma < \beta^\gamma$.
