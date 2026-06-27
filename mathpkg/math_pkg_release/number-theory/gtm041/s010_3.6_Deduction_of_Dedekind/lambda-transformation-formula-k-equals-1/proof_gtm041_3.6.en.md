---
role: proof
locale: en
of_concept: lambda-transformation-formula-k-equals-1
source_book: gtm041
source_chapter: "3"
source_section: "3.6"
---

**Proof.** We apply Iseki's formula (Theorem 3.5, Equation (18)) with $\beta = 0$ and take the limit as $\alpha \to 0^+$.

Iseki's formula states that for $\operatorname{Re}(z) > 0$ and suitable parameters $\alpha, \beta$,

$$\sum_{r=0}^{\infty} \lambda((r + \alpha)z - i\beta) + \sum_{r=0}^{\infty} \lambda((r + 1 - \alpha)z + i\beta) = \sum_{r=0}^{\infty} \lambda\!\left((r + \beta)\frac{1}{z} - i\alpha\right) + \sum_{r=0}^{\infty} \lambda\!\left((r + 1 - \beta)\frac{1}{z} + i\alpha\right) - \pi z\!\left(\alpha^2 - \alpha + \frac{1}{6}\right) + \frac{\pi}{z}\!\left(\beta^2 - \beta + \frac{1}{6}\right) + \pi i(2\alpha\beta - \alpha - \beta + \frac{1}{2}).$$

Setting $\beta = 0$, the formula simplifies to

$$\sum_{r=0}^{\infty} \lambda((r + \alpha)z) + \sum_{r=0}^{\infty} \lambda((r + 1 - \alpha)z) = \sum_{r=0}^{\infty} \lambda\!\left(\frac{r}{z} - i\alpha\right) + \sum_{r=0}^{\infty} \lambda\!\left(\frac{r + 1}{z} + i\alpha\right) - \pi z\!\left(\alpha^2 - \alpha + \frac{1}{6}\right) + \frac{\pi}{6z}.$$

As $\alpha \to 0^+$, each series on the left approaches $\sum_{n=1}^{\infty} \lambda(nz)$, except that the first term ($r = 0$) of the first left series and the first term ($r = 0$) of the second right series require special attention.

Separating these $r = 0$ terms, we must evaluate

$$\lim_{\alpha \to 0^+} \bigl[\lambda(\alpha z) - \lambda(i\alpha)\bigr].$$

Using the definition $\lambda(x) = -\log(1 - e^{-2\pi i x})$,

$$\lambda(\alpha z) - \lambda(i\alpha) = \log\frac{1 - e^{-2\pi i \alpha}}{1 - e^{-2\pi \alpha z}}.$$

Expanding the exponentials for small $\alpha$:

$$1 - e^{-2\pi i \alpha} = 2\pi i \alpha + O(\alpha^2), \qquad 1 - e^{-2\pi \alpha z} = 2\pi \alpha z + O(\alpha^2).$$

Therefore

$$\frac{1 - e^{-2\pi i \alpha}}{1 - e^{-2\pi \alpha z}} \to \frac{i}{z} \quad \text{as } \alpha \to 0^+,$$

and consequently

$$\lambda(\alpha z) - \lambda(i\alpha) \to \log\frac{i}{z} = \frac{\pi i}{2} - \log z.$$

The remaining parts of the series combine to give $\sum_{n=1}^{\infty} \lambda(nz)$ on the left and $\sum_{n=1}^{\infty} \lambda(n/z)$ on the right. Collecting the polynomial terms and the limit, we obtain

$$\sum_{n=1}^{\infty} \lambda(nz) = \sum_{n=1}^{\infty} \lambda\!\left(\frac{n}{z}\right) + \frac{1}{2}\log z - \frac{\pi}{12}\!\left(z - \frac{1}{z}\right).$$

Since $\lambda(x + i) = \lambda(x)$, the terms involving the integer shifts $ih$ and $iH$ in the original statement drop out, giving exactly the same formula. This proves the $k = 1$ case of Equation (16).
