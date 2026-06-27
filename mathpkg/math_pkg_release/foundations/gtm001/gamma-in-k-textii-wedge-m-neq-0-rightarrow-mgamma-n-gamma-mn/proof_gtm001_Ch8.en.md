---
role: proof
locale: en
of_concept: gamma-in-k-textii-wedge-m-neq-0-rightarrow-mgamma-n-gamma-mn
source_book: gtm001
source_chapter: "8"
source_section: ""
---

(By induction on $\gamma + n$). If $\gamma + n = \omega$ we have $m\omega = \bigcup_{n < \omega} mn$. Since $mn < \omega$ we have

$$\bigcup_{n < \omega} mn \leq \omega.$$

Furthermore $p < \omega \rightarrow (\exists q)(\exists r)[p = mq + r \wedge r < m]$. But $p = mq + r \leq mq + m = m(q + 1)$. Therefore $p \in \bigcup_{n < \omega} mn$; hence

$$\bigcup_{n < \omega} mn = \omega.$$

If $m(\gamma + n) = \gamma + mn$ then $m(\gamma + n + 1) = m(\gamma + n) + m = (\gamma + mn) + m = \gamma + m(n + 1)$. If $\gamma + n \in K_{\text{II}}$, then $n = 0$ and

$$m\gamma = \bigcup_{\delta < \gamma} m\delta.$$

If $\delta < \gamma$ then $\delta < \omega \vee \omega \leq \delta$. If $\delta < \omega$ then $m\delta < \varphi < \gamma$.

If $\omega \leq \delta$ then $(\exists \beta)(\exists n)[\beta \in K_{\text{II}} \wedge \delta = \beta + n]$. Then from the induction hypothesis $m\delta = \beta + mn$. But $\beta \leq \delta < \gamma$ and $\gamma \in K

We do not have a right-hand cancellation law:

$$1 \cdot \omega = 2 \cdot \omega \quad \text{but} \quad 1 \neq 2.$$

Having defined multiplication as repeated addition we next define exponentiation as repeated multiplication.
