---
role: proof
locale: en
of_concept: l1-metric-space-not-complete
source_book: gtm002
source_chapter: "10"
source_section: "10. Examples of Metric Spaces"
---

Consider $C[0,1]$. Define $f_n(x)$ piecewise linearly so that $f_n(x) = 1$ for $0 \leq x \leq 1/2 - 1/2n$, $f_n(x) = 0$ for $1/2 + 1/2n \leq x \leq 1$, and $f_n$ is linear on $[1/2 - 1/2n, 1/2 + 1/2n]$. From the graph of this function it is clear that

$$\sigma(f_n, f_m) = (1/4)|1/n - 1/m|.$$

Hence $\{f_n\}$ is a Cauchy sequence. Suppose $\sigma(f_n, f) \to 0$ as $n \to \infty$ for some $f$ in $C$. Then

$$\sigma(f_n, f) \geq \int_0^{1/2-1/2n}|1-f(x)| \, dx + \int_{1/2+1/2n}^{1}|f(x)| \, dx.$$

Letting $n \to \infty$ it follows that

$$\int_0^{1/2}|1-f(x)| \, dx = \int_{1/2}^{1}|f(x)| \, dx = 0.$$

Since $f$ is continuous, we must have $f(x) = 1$ on $[0, 1/2]$ and $f(x) = 0$ on $[1/2, 1]$, which is impossible at $x = 1/2$. Thus no such $f \in C$ exists.
