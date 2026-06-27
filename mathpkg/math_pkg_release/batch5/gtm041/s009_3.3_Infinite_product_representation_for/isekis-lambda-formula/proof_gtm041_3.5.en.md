---
role: proof
locale: en
of_concept: isekis-lambda-formula
source_book: gtm041
source_chapter: "3"
source_section: "3.5"
---

First assume $0 < \alpha < 1$ and $0 < \beta < 1$. Begin with the first sum in the definition of $\Lambda$ and use $\lambda(z) = \sum_{m=1}^{\infty} \frac{e^{2\pi i m z}}{m}$ to write

$$\sum_{r=0}^{\infty} \lambda((r + \alpha)z - i\beta) = \sum_{r=0}^{\infty} \sum_{m=1}^{\infty} \frac{e^{2\pi im\beta}}{m} e^{-2\pi m(r + \alpha)z}.$$

Now apply Mellin's integral for $e^{-x}$:

$$e^{-x} = \frac{1}{2\pi i} \int_{c-i\infty}^{c+i\infty} \Gamma(s) x^{-s} ds, \quad c > 0,\; \operatorname{Re}(x) > 0.$$

Summing the geometric series in $r$ introduces the Hurwitz zeta function $\zeta(s,\alpha) = \sum_{r=0}^{\infty} \frac{1}{(r+\alpha)^s}$ and the periodic zeta function $F(x,s) = \sum_{m=1}^{\infty} \frac{e^{2\pi imx}}{m^s}$ (both valid for $\operatorname{Re}(s) > 1$). Similarly treating the second sum gives

$$\Lambda(\alpha, \beta, z) = \frac{1}{2\pi i} \int_{(3/2)} z^{-s} \Phi(\alpha, \beta, s)\, ds,$$

where

$$\Phi(\alpha, \beta, s) = \frac{\Gamma(s)}{(2\pi)^s} \Bigl\{ \zeta(s, \alpha) F(\beta, 1+s) + \zeta(s, 1-\alpha) F(1-\beta, 1+s) \Bigr\}.$$

Now shift the line of integration from $c = 3/2$ to $c = -3/2$ by applying Cauchy's theorem to a rectangular contour (with horizontal segments tending to $0$ as $T \to \infty$, established in Exercise 8). We obtain

$$\int_{(3/2)} = \int_{(-3/2)} + R,$$

where $R$ is the sum of residues at the poles encoun-tered. Making the change of variable $u = -s$ in the integral over $(-3/2)$ gives

$$\Lambda(\alpha, \beta, z) = \frac{1}{2\pi i} \int_{(3/2)} z^u \Phi(\alpha, \beta, -u)\, du + R.$$

The function $\Phi$ satisfies the functional equation

$$\Phi(\alpha, \beta, -s) = \Phi(1 - \beta, \alpha, s),$$

a consequence of Hurwitz's formula for $\zeta(s,\alpha)$ (see Exercise 7). Substituting this yields

$$\Lambda(\alpha, \beta, z) = \Lambda(1 - \beta, \alpha, z^{-1}) + R.$$

It remains to compute the residue sum $R$. The function $\Phi(\alpha,\beta,s)$ has first-order poles at $s = 1, 0, -1$. Denoting residues by $R(1), R(0), R(-1)$:

$$R(1) = \frac{\Gamma(1)}{2\pi z} \bigl\{ F(\beta, 2) + F(1-\beta, 2) \bigr\} = \frac{1}{2\pi z} \sum_{n=-\infty}^{+\infty} \frac{e^{2\pi i n\beta}}{n^2} = \frac{1}{2\pi z} \frac{-(2\pi i)^2}{2!} B_2(\beta) = \frac{\pi}{z} B_2(\beta).$$

By symmetry, $R(-1) = -\pi z B_2(\alpha)$. For the residue at $s = 0$, explicit computation using the expansions of $\Gamma(s)$, $\zeta(s,\alpha)$, and $F(\beta,1+s)$ near $s=0$ gives

$$R(0) = 2\pi i \Bigl(\alpha - \tfrac{1}{2}\Bigr)\Bigl(\beta - \tfrac{1}{2}\Bigr).$$

Summing the three residues:

$$R = R(-1) + R(0) + R(1) = -\pi z \sum_{n=0}^{2} \binom{2}{n} (iz)^{-n} B_{2-n}(\alpha) B_n(\beta).$$

This proves Iseki's formula under the restriction $0 < \alpha < 1$, $0 < \beta < 1$. The extension to the boundary cases ($\alpha = 0,1$ or $\beta = 0,1$, with appropriate strictness) follows by a limiting argument: for example, when $\alpha = 0$, the series $\sum_{r=0}^{\infty} \lambda(rz - i\beta)$ converges uniformly in any compact set away from the poles, and the limit as $\alpha \to 0^+$ can be taken inside the formula. The same reasoning applies to the other boundary values.
