---
role: proof
locale: en
of_concept: proposition-7-8
source_book: gtm040
source_chapter: "7"
source_section: "8"
---

**Proof:** The random variables $x_{n+1}^{(k)} - x_n^{(k)}$ are independent and identically distributed and have mean 0 and variance

$$\sigma^2 = \frac{1}{2} \left(\frac{1}{2^k}\right)^2 + \frac{1}{2} \left(-\frac{1}{2^k}\right)^2 = \frac{1}{4^k}.$$

Let $m = 4k t$ be an integer. Since

$$x_m^{(k)} = \sum_{n=1}^{m} [x_n^{(k)} - x_{n-1}^{(k)}],$$

$x_m^{(k)}$ has mean 0 and variance $m/4^k = t$. Hence, by the Central Limit Theorem,
