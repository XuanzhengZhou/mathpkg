---
role: proof
locale: en
of_concept: cantor-normal-form-times-power
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** From Proposition 8.43 (which bounds a Cantor Normal Form sum between consecutive powers),

$$\alpha^{\beta_n} \le \alpha^{\beta_n} \cdot \gamma_n + \cdots + \alpha^{\beta_0} \cdot \gamma_0 < \alpha^{\beta_n+1}.$$

Therefore, letting $S = \alpha^{\beta_n} \cdot \gamma_n + \cdots + \alpha^{\beta_0} \cdot \gamma_0$,

$$\alpha^{\beta_n} \cdot \alpha^\delta \le S \cdot \alpha^\delta < \alpha^{\beta_n+1} \cdot \alpha^\delta.$$

That is, $\alpha^{\beta_n + \delta} \le S \cdot \alpha^\delta < \alpha^{\beta_n + 1 + \delta}$. Since $\delta \ge \omega$, we have $\beta_n + 1 + \delta = \beta_n + \delta$ (finite ordinals are absorbed by infinite $\delta$). Thus $S \cdot \alpha^\delta$ lies between $\alpha^{\beta_n+\delta}$ and $\alpha^{\beta_n+\delta}$ exclusively on the upper bound, forcing $S \cdot \alpha^\delta = \alpha^{\beta_n+\delta}$.
