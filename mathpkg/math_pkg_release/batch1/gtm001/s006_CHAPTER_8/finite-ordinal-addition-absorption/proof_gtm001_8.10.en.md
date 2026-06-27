---
role: proof
locale: en
of_concept: finite-ordinal-addition-absorption
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (By induction). First note that $\gamma < \omega \rightarrow n + \gamma < \omega$. Hence $\bigcup_{\gamma < \omega} (n + \gamma) \leq \omega$. On the other hand, by Proposition 8.8, $(\forall \beta < \omega)(\exists \gamma \in \omega)[\beta \leq n + \gamma]$. Then $\omega = \bigcup_{\beta \in \omega} \beta \leq \bigcup_{\gamma < \omega} (n + \gamma)$ by Proposition 8.6. Thus $n + \omega = \omega$.

By Definition 8.1 and the induction hypothesis: $n + (\alpha + 1) = (n + \alpha) + 1 = \alpha + 1$. Finally, if $\alpha \in K_{\mathrm{II}}$ then from the induction hypothesis

$$n + \alpha = \bigcup_{\beta < \alpha} (n + \beta) = \bigcup_{\beta < \alpha} \beta = \alpha.$$
