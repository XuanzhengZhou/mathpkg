---
role: proof
locale: en
of_concept: continuous-function-space-incomplete-under-l1-metric
source_book: gtm002
source_chapter: "10"
source_section: "10"
---

Consider $C[0,1]$ with the $L^1$ metric. Define $f_n$ to be the continuous piecewise linear function that equals $1$ on $[0, 1/2 - 1/2n]$, equals $0$ on $[1/2 + 1/2n, 1]$, and is linear in between. From the graph it is clear that

$$\sigma(f_n, f_m) = \frac{1}{4}\left|\frac{1}{n} - \frac{1}{m}\right|.$$

Hence $\{f_n\}$ is a Cauchy sequence. Suppose $\sigma(f_n, f) \to 0$ as $n \to \infty$ for some $f \in C[0,1]$. Then

$$\sigma(f_n, f) \geq \int_0^{1/2-1/2n} |1 - f(x)| \, dx + \int_{1/2+1/2n}^1 |f(x)| \, dx.$$

Letting $n \to \infty$, it follows that

$$\int_0^{1/2} |1 - f(x)| \, dx = \int_{1/2}^1 |f(x)| \, dx = 0.$$

Since $f$ is continuous, we must have $f(x) = 1$ on $[0, 1/2]$ and $f(x) = 0$ on $[1/2, 1]$, which is impossible. Hence no limit exists in $C[0,1]$.
