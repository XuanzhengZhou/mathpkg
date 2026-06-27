---
role: proof
locale: en
of_concept: cauchy-bunyakovskii-inequality
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of the Cauchy–Bunyakovskii Inequality for Expectations

**The Cauchy–Bunyakovskii Inequality.** Let $\xi$ and $\eta$ satisfy $E\xi^2 < \infty$, $E\eta^2 < \infty$. Then $E|\xi\eta| < \infty$ and

$$(E|\xi\eta|)^2 \leq E\xi^2 \cdot E\eta^2. \tag{24}$$

*Proof.* Suppose that $E\xi^2 > 0$, $E\eta^2 > 0$. Then, with

$$\tilde{\xi} = \frac{\xi}{\sqrt{E\xi^2}}, \quad \tilde{\eta} = \frac{\eta}{\sqrt{E\eta^2}},$$

we find, since $2|\tilde{\xi}\tilde{\eta}| \leq \tilde{\xi}^2 + \tilde{\eta}^2$ (by the elementary inequality $2ab \leq a^2 + b^2$), that

$$2E|\tilde{\xi}\tilde{\eta}| \leq E\tilde{\xi}^2 + E\tilde{\eta}^2 = 2,$$

i.e., $E|\tilde{\xi}\tilde{\eta}| \leq 1$, which establishes (24).

On the other hand, if, say, $E\xi^2 = 0$, then by Property H (zero expectation of a nonnegative random variable), $\xi = 0$ (a.s.), and then $E|\xi\eta| = 0$ by Property F, i.e., (24) is still satisfied (both sides are zero). $\square$
