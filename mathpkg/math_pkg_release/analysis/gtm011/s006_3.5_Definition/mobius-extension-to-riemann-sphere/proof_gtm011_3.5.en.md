---
role: proof
locale: en
of_concept: mobius-extension-to-riemann-sphere
source_book: gtm011
source_chapter: "3"
source_section: "3.5"
---

If $c = 0$, then $ad - bc = ad \neq 0$, so $a \neq 0$ and $d \neq 0$. In this case $S(z) = \frac{a}{d}z + \frac{b}{d}$ is an affine map, and we define $S(\infty) = \infty$, consistent with the limit $\lim_{|z| \to \infty} S(z) = \infty$.

If $c \neq 0$, then $\lim_{z \to \infty} S(z) = \lim_{z \to \infty} \frac{a + b/z}{c + d/z} = \frac{a}{c}$, so we define $S(\infty) = a/c$. Also, $\lim_{z \to -d/c} |S(z)| = \infty$, so we define $S(-d/c) = \infty$.

With these conventions, $S: \mathbb{C}_\infty \to \mathbb{C}_\infty$ is a bijection. The inverse $S^{-1}(z) = \frac{dz-b}{-cz+a}$ also satisfies these extension rules, confirming that the extension is consistent with the group structure.
