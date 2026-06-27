---
role: proof
locale: en
of_concept: alpha-le-beta-rightarrow-exists-gammaalpha-gamma-beta
source_book: gtm001
source_chapter: "8"
source_section: ""
---

Since $\alpha \geq 0$ it follows from Propositions 8.7 and 8.3 that $\alpha + \beta

By Proposition 8.9, $\gamma < \omega \rightarrow n + \gamma < \omega$. Hence

$$\bigcup_{\gamma < \omega} (n + \gamma) \leq \omega.$$

On the other hand, by Proposition 8.8, $(\forall \beta < \omega)(\exists \gamma \in \omega)[\beta \leq n + \gamma]$. Then

$$\omega = \bigcup_{\beta \in \omega} \beta \leq \bigcup_{\gamma < \omega} (n + \gamma)$$

by Proposition 8.6. Thus $n + \omega = \omega$. By Definition 8.1 and the induction hypothesis

$$n + (\alpha + 1) = (n + \alpha) + 1 = \alpha + 1.$$

Finally, if $\alpha \in K_{\text{II}}$ then from the induction hypothesis

$$n + \alpha = \bigcup_{\beta < \alpha} (n + \beta) = \bigcup_{\beta < \alpha} \beta = \alpha.$$

Remark. From Proposition 8.10 we see that ordinal addition is not commutative:

$$1 + \omega = \omega \neq \omega + 1.$$

Furthermore $1 + \omega = 2 + \omega$ but $1 \neq 2$. Thus we do not have a right-hand cancellation law. From Corollary 8.5 we see that we do however have a left-hand cancellation law.
