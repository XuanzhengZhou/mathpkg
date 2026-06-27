---
role: proof
locale: en
of_concept: j-conjugate-symmetry
source_book: gtm041
source_chapter: "2"
source_section: "2.7"
---

Write $\tau = u + iv$ with $u, v \in \mathbb{R}$ and $v > 0$. Then

$$x = e^{2\pi i \tau} = e^{2\pi i(u + iv)} = e^{-2\pi v} e^{2\pi i u}$$

and

$$\bar{x} = e^{-2\pi i \bar{\tau}} = e^{-2\pi i(u - iv)} = e^{-2\pi v} e^{-2\pi i u}.$$

Now, $-\bar{\tau} = -u + iv$, so the corresponding Fourier variable for $-\bar{\tau}$ is

$$x' = e^{2\pi i (-\bar{\tau})} = e^{2\pi i(-u + iv)} = e^{-2\pi v} e^{-2\pi i u} = \bar{x}.$$

Since the Fourier expansion of $J(\tau)$ has real coefficients, we have $J(\tau) = \overline{J(\tau)}$ expressed in terms of $x$ and $\bar{x}$, and the equality $x' = \bar{x}$ implies $J(\tau) = J(-\bar{\tau})$ because the Fourier series

$$12^3 J(\tau) = \frac{1}{x} + \sum_{n=0}^{\infty} c(n) x^n \quad (x = e^{2\pi i \tau})$$

has real coefficients $c(n)$. Substituting $\bar{x}$ for $x$ yields the conjugate Fourier series evaluated at $-\bar{\tau}$, giving the same value.
