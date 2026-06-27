---
role: proof
locale: en
of_concept: alphabetagamma-alphabetagamma
source_book: gtm001
source_chapter: "8"
source_section: ""
---

(By transfinite induction on $\gamma$). For $\gamma = 0$ we have $(\alpha^{\beta})^{0} = 1 = \alpha^{\beta \cdot 0}.$ If $(\alpha^{\beta})^{\gamma} = \alpha^{\beta\gamma}$ then $(\alpha^{\beta})^{\gamma+1} = (\alpha^{\beta})^{\gamma\alpha^{\beta}} = \alpha^{\beta\gamma}\alpha^{\beta} = \alpha^{\beta\gamma+\beta} = \alpha^{\beta(\gamma+1)}.$ If $\gamma \in K_{\text{II}}$ then $\beta = 0$ or $\beta\gamma \in K_{\text{II}}.$ If $\beta = 0$ then $(\alpha^{\beta})^{\gamma} = 1^{\gamma} = 1 = \alpha^{\beta\gamma}.$ If $\beta\gamma \in K_{\text{II}}$ then $\alpha = 0$ or $\alpha \neq 0.$ If $\alpha = 0$ then $\alpha^{\beta} = 0$ and hence $(\alpha^{\beta})^{\gamma} = 0 = \alpha^{\beta\gamma}.$ If $\alpha \neq 0$ then

(By transfinite induction on $\beta$). By Proposition 8.38, there exists a $\delta$ such that

(1) $\alpha^{\delta} < \beta < \alpha^{\delta+1}$.

By Proposition 8.27 there exists a $\tau$ and $\nu$ such that

(2) $\beta = \alpha^{\delta}\tau + \nu$

and $\nu < \alpha^{\delta}$. From (1) it follows that $0 < \tau < \alpha$. So if $\nu = 0$ we are through. If $\nu > 0$, then by the induction hypothesis, it follows that there exist ordinals $\beta_0, \ldots, \beta_n, \gamma_0, \ldots, \gamma_n$ as prescribed, such that

$$\nu = \alpha^{\beta_n}\gamma_n + \cdots + \alpha^{\beta_0}\gamma_0.$$

Substituting this in (2) we have

$$\beta = \alpha^{\delta}\tau + \alpha^{\beta_n}\gamma_n + \cdots + \alpha^{\beta_0}\gamma_0$$

and the ordinals $\delta, \beta_n, \ldots, \beta_0; \tau, \gamma_n, \ldots, \gamma_0$ are as required. $\square$

The proof of uniqueness we leave to the reader.
