---
role: proof
locale: en
of_concept: cantor-normal-form-existence
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (By transfinite induction on $\beta$). By Proposition 8.38 (with $\alpha = \omega$), there exists a unique $\delta$ such that $\omega^\delta \le \beta < \omega^{\delta+1}$. By Proposition 8.27 (the division algorithm), there exist unique $\tau$ and $\nu$ such that $\beta = \omega^\delta \cdot \tau + \nu$ with $\nu < \omega^\delta$. From $\beta < \omega^{\delta+1} = \omega^\delta \cdot \omega$, it follows that $\tau < \omega$, i.e., $0 < \tau < \omega$. If $\nu = 0$, we are done: $\beta = \omega^\delta \cdot \tau$ with $\tau \in \omega$, $\tau > 0$.

If $\nu > 0$, then by the induction hypothesis (since $\nu < \omega^\delta \le \beta$), there exist ordinals $\beta_0, \ldots, \beta_n$ and nonzero natural numbers $\gamma_0, \ldots, \gamma_n$ such that $\nu = \omega^{\beta_n} \cdot \gamma_n + \cdots + \omega^{\beta_0} \cdot \gamma_0$ with $\beta_n > \cdots > \beta_0$. Substituting, we obtain

$$\beta = \omega^\delta \cdot \tau + \omega^{\beta_n} \cdot \gamma_n + \cdots + \omega^{\beta_0} \cdot \gamma_0.$$

Since $\nu < \omega^\delta$, the leading exponent of $\nu$ must be less than $\delta$, i.e., $\beta_n < \delta$. Thus the exponents $\delta, \beta_n, \ldots, \beta_0$ are strictly decreasing and the coefficients $\tau, \gamma_n, \ldots, \gamma_0$ are all nonzero natural numbers. This proves existence.

The proof of uniqueness is left to the reader (it follows by induction using the uniqueness in the division algorithm and the logarithm proposition).
