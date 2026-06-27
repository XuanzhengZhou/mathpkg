---
role: proof
locale: en
of_concept: incompleteness-of-continuous-functions-under-integral-metric
source_book: gtm002
source_chapter: "10"
source_section: "10"
---

Consider the sequence $\{f_n\}$ of functions on $[0,1]$ defined by

$$f_n(x) = \begin{cases} 0 & \text{for } 0 \leq x \leq 1/2 - 1/2n, \\ \text{linear} & \text{for } 1/2 - 1/2n \leq x \leq 1/2 + 1/2n, \\ 1 & \text{for } 1/2 + 1/2n \leq x \leq 1. \end{cases}$$

From the graph of this function it is clear that

$$\sigma(f_n, f_m) = (1/4)|1/n - 1/m|.$$

Hence $\{f_n\}$ is a Cauchy sequence. Suppose $\sigma(f_n, f) \to 0$ as $n \to \infty$ for some $f$ in $C$. Then

$$\sigma(f_n, f) \geq \int_0^{1/2-1/2n}|1-f(x)| \, dx + \int_{1/2+1/2n}^{1}|f(x)| \, dx.$$

Letting $n \to \infty$ it follows that

$$\int_0^{1/2}|1-f(x)| \, dx = \int_{1/2}^{1}|f(x)| \, dx = 0.$$

Since $f$ is continuous, we must have $f(x) = 1$ on $[0, 1/2]$ and $f(x) = 0$ on $[1/2, 1]$, which is impossible. Therefore no continuous limit exists, and $(C, \sigma)$ is not complete.
