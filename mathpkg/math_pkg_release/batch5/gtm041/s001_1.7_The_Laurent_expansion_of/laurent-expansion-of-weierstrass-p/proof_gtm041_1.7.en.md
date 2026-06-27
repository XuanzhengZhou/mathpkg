---
role: proof
locale: en
of_concept: laurent-expansion-of-weierstrass-p
source_book: gtm041
source_chapter: "1"
source_section: "1.7"
---

If $0 < |z| < r$ then $|z/\omega| < 1$ for all nonzero $\omega \in \Omega$, and we have

$$\frac{1}{(z - \omega)^2} = \frac{1}{\omega^2 \left(1 - \frac{z}{\omega}\right)^2} = \frac{1}{\omega^2} \left(1 + \sum_{n=1}^{\infty} (n + 1) \left(\frac{z}{\omega}\right)^n\right),$$

hence

$$\frac{1}{(z - \omega)^2} - \frac{1}{\omega^2} = \sum_{n=1}^{\infty} \frac{n + 1}{\omega^{n+2}} z^n.$$

Summing over all nonzero $\omega$ and using the absolute convergence of the double series for $|z| < r$, we obtain

$$\wp(z) = \frac{1}{z^2} + \sum_{\omega \neq 0} \left(\frac{1}{(z - \omega)^2} - \frac{1}{\omega^2}\right) = \frac{1}{z^2} + \sum_{n=1}^{\infty} (n + 1) \left(\sum_{\omega \neq 0} \frac{1}{\omega^{n+2}}\right) z^n.$$

Since the lattice $\Omega$ is symmetric ($\omega \in \Omega$ implies $-\omega \in \Omega$), the sum $G_{n+2} = \sum_{\omega \neq 0} \omega^{-(n+2)}$ vanishes when $n$ is odd. Therefore only even powers survive. Replacing $n$ by $2n$, the coefficient becomes $(2n + 1) G_{2n+2}$, giving

$$\wp(z) = \frac{1}{z^2} + \sum_{n=1}^{\infty} (2n + 1) G_{2n+2} z^{2n}.$$
