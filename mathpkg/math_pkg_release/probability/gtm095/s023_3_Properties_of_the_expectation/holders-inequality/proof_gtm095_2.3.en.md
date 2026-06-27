---
role: proof
locale: en
of_concept: holders-inequality
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Hölder's Inequality for Expectations

**Hölder's Inequality.** Let $1 < p < \infty$, $1 < q < \infty$, and $1/p + 1/q = 1$. If $E|\xi|^p < \infty$ and $E|\eta|^q < \infty$, then $E|\xi\eta| < \infty$ and

$$E|\xi\eta| \leq (E|\xi|^p)^{1/p} (E|\eta|^q)^{1/q}. \tag{29}$$

*Proof.* If $E|\xi|^p = 0$ or $E|\eta|^q = 0$, then by Property H, $\xi = 0$ (a.s.) or $\eta = 0$ (a.s.), so $E|\xi\eta| = 0$ and (29) holds trivially. (Note that the Cauchy–Bunyakovskii inequality is the special case $p = q = 2$.)

Now let $E|\xi|^p > 0$ and $E|\eta|^q > 0$. Set

$$\tilde{\xi} = \frac{\xi}{(E|\xi|^p)^{1/p}}, \quad \tilde{\eta} = \frac{\eta}{(E|\eta|^q)^{1/q}}.$$

By Young's inequality, for any nonnegative $a, b$, we have $ab \leq a^p/p + b^q/q$ (since $1/p + 1/q = 1$). Applying this to $a = |\tilde{\xi}|$ and $b = |\tilde{\eta}|$,

$$|\tilde{\xi}\tilde{\eta}| \leq \frac{|\tilde{\xi}|^p}{p} + \frac{|\tilde{\eta}|^q}{q}.$$

Taking expectations,

$$E|\tilde{\xi}\tilde{\eta}| \leq \frac{E|\tilde{\xi}|^p}{p} + \frac{E|\tilde{\eta}|^q}{q} = \frac{1}{p} + \frac{1}{q} = 1.$$

Substituting back the definitions of $\tilde{\xi}$ and $\tilde{\eta}$, we obtain

$$\frac{E|\xi\eta|}{(E|\xi|^p)^{1/p}(E|\eta|^q)^{1/q}} \leq 1,$$

which is exactly (29). $\square$
