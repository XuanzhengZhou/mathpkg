---
role: proof
locale: en
of_concept: frechet-space-cauchy-criterion
source_book: gtm055
source_chapter: "14"
source_section: "15"
---
The quasinorm $\|\cdot\|$ defined by $\|x\| = \sum_{n=1}^{\infty} \frac{1}{2^n} \frac{\sigma_n(x)}{1 + \sigma_n(x)}$ induces the same topology as $\{\sigma_n\}$. A sequence converges with respect to $\|\cdot\|$ iff it converges with respect to each $\sigma_n$. If $\{x_p\}$ is Cauchy with respect to $\|\cdot\|$, it is Cauchy with respect to every $\sigma_n$. Conversely, suppose $\{x_p\}$ is Cauchy with respect to each $\sigma_n$. Given $\varepsilon > 0$, choose $K$ such that $\sum_{n=K+1}^{\infty} 1/2^n < \varepsilon/2$. Then there exists $P$ such that $\sigma_n(x_p - x_q) < \varepsilon/2$ for all $p, q \geq P$ and $n = 1, \ldots, K$, whence $\|x_p - x_q\| < \varepsilon$ for all $p, q \geq P$.
