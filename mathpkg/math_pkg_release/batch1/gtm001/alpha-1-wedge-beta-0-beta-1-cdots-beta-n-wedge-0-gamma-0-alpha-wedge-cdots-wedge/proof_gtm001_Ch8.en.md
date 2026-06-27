---
role: proof
locale: en
of_concept: alpha-1-wedge-beta-0-beta-1-cdots-beta-n-wedge-0-gamma-0-alpha-wedge-cdots-wedge
source_book: gtm001
source_chapter: "8"
source_section: ""
---

From Proposition 8.43.

$$\alpha^{\beta_n} \leq \alpha^{\beta_n}\gamma_n + \cdots + \alpha^{\beta_0}\gamma_0 < \alpha^{\beta_n+1}.$$

Therefore

$$\alpha^{\beta_n+ \delta} = \alpha^{\beta_n}\alpha^{\

(By transfinite induction on $\gamma$). If $\gamma = 1$, then $(\alpha^\beta m)^1 = \alpha^{\beta \cdot 1} m$. If $(\alpha^\beta m)^\gamma = \alpha^{\beta \gamma} m$ then $(\alpha^\beta m)^{\gamma+1} = (\alpha^\beta m)^\gamma \alpha^\beta m = \alpha^{\beta \gamma} m \alpha^\beta m = \alpha^{\beta (\gamma+1)} m$. If $(\alpha^\beta m)^\gamma = \alpha^{\beta \gamma} m$ then $(\alpha^\beta m)^{\gamma+1} = (\alpha^\beta m)^\gamma \alpha^\beta m = \alpha^{\beta \gamma} \alpha^\beta m = \alpha^{\beta (\gamma+1)} m$. If $\gamma \in K_{\text{II}}$ then

$$(\alpha^\beta)^\gamma \leq (\alpha^\beta m)^\gamma = \bigcup_{\delta < \gamma} (\alpha^\beta m)^\delta \leq \bigcup_{\delta < \gamma} \alpha^{\beta \delta} m \leq \bigcup_{\delta < \gamma} \alpha^{\beta (\delta+1)} = \alpha^{\beta \gamma}.$$
