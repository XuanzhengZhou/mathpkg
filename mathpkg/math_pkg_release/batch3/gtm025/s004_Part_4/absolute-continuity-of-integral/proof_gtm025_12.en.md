---
role: proof
locale: en
of_concept: absolute-continuity-of-integral
source_book: gtm025
source_chapter: "3"
source_section: "12"
---

For $n = 1,2,\ldots$, let $\psi_n(x) = |f(x)|$ if $|f(x)| \leq n$, and $\psi_n(x) = n$ otherwise. Then $(\psi_n)$ is nondecreasing and $\lim \psi_n = |f|$. By (12.22), $\lim \int_X \psi_n d\mu = \int_X |f| d\mu$. Choose $n$ so that $\int_X (|f| - \psi_n) d\mu < \varepsilon/2$. Set $\delta = \varepsilon/(2n)$. For any $E$ with $\mu(E) < \delta$, $\int_E \psi_n d\mu \leq n\mu(E) < \varepsilon/2$. Thus $\int_E |f| d\mu \leq \int_E (|f| - \psi_n) d\mu + \int_E \psi_n d\mu < \varepsilon$.
