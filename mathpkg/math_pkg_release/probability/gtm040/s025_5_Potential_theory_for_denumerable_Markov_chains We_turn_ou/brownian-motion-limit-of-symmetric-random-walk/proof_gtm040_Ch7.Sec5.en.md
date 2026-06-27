---
role: proof
locale: en
of_concept: brownian-motion-limit-of-symmetric-random-walk
source_book: gtm040
source_chapter: "7"
source_section: "5"
---

The random variables $x_{n+1}^{(k)} - x_n^{(k)}$ are independent and identically distributed and have mean $0$ and variance

$$\sigma^2 = \frac{1}{2}\left(\frac{1}{2^k}\right)^2 + \frac{1}{2}\left(-\frac{1}{2^k}\right)^2 = \frac{1}{4^k}.$$

Let $m = 4^k t$ be an integer. Since

$$x_m^{(k)} = \sum_{n=1}^{m} \bigl[x_n^{(k)} - x_{n-1}^{(k)}\bigr],$$

$x_m^{(k)}$ has mean $0$ and variance $m / 4^k = t$. Hence, by the Central Limit Theorem (Theorem 1-68),

$$\lim_{k \to \infty} \Pr_0\!\left[\frac{\alpha}{\sqrt{t}} < \frac{x_m^{(k)}}{\sqrt{t}} < \frac{\beta}{\sqrt{t}}\right] = \Phi\!\left(\frac{\beta}{\sqrt{t}}\right) - \Phi\!\left(\frac{\alpha}{\sqrt{t}}\right) = \Pr_0[x_t \in (\alpha, \beta)].$$

This completes the proof.
