---
role: proof
locale: en
of_concept: zeta-function-simple-pole
source_book: gtm007
source_chapter: "VI"
source_section: "3"
---

Write $\zeta(s) = \frac{1}{s-1} + \sum_{n=1}^{\infty} \phi_n(s)$ where
$$\phi_n(s) = \int_{n}^{n+1} (n^{-s} - t^{-s})\, dt.$$

Each $\phi_n(s)$ is holomorphic for $\Re(s) > 0$. The estimate $|\phi_n(s)| \leq |s|/n^{\Re(s)+1}$ shows the series $\sum \phi_n$ converges normally on every compact subset of $\Re(s) > 0$, hence defines a holomorphic function there. Thus $\zeta(s) - 1/(s-1)$ extends holomorphically to $\Re(s) > 0$, so $s = 1$ is a simple pole.

