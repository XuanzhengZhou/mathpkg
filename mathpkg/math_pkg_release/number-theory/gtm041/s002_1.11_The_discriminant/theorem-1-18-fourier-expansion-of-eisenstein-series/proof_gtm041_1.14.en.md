---
role: proof
locale: en
of_concept: theorem-1-18-fourier-expansion-of-eisenstein-series
source_book: gtm041
source_chapter: "1"
source_section: "1.14"
---

We write

$$g_2(\tau) = 60 \sum_{m,n=-\infty}^{+\infty} \frac{1}{(m+n\tau)^4}$$

$$= 60 \left\{ \sum_{m=-\infty}^{+\infty} \frac{1}{m^4} + \sum_{n=1}^{\infty} \sum_{m=-\infty}^{+\infty} \left( \frac{1}{(m+n\tau)^4} + \frac{1}{(m-n\tau)^4} \right) \right\}$$

$$= 60 \left\{ 2\zeta(4) + 2 \sum_{n=1}^{\infty} \sum_{m=-\infty}^{+\infty} \frac{1}{(m+n\tau)^4} \right\}$$

$$= 60 \left\{ \frac{2\pi^4}{90} + \frac{16\pi^4}{3} \sum_{n=1}^{\infty} \sum_{r=1}^{\infty} r^3x^{nr} \right\}$$

where $x = e^{2\pi i\tau}$. In the last double sum we collect together those terms for which $nr$ is constant and we obtain the expansion for $g_2(\tau)$. The formula for $g_3(\tau)$ is similarly proved. $\square$
