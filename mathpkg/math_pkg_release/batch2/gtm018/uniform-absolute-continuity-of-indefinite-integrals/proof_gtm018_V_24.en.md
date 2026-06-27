---
role: proof
locale: en
of_concept: uniform-absolute-continuity-of-indefinite-integrals
source_book: gtm018
source_chapter: "V"
source_section: "24"
---
**Proof.** Given $\epsilon > 0$, choose $n_0$ such that $\int |f_n - f_m| d\mu < \epsilon/2$ for $n,m \geq n_0$. Choose $\delta > 0$ such that $\int_E |f_n| d\mu < \epsilon/2$ for $n = 1,\dots,n_0$ whenever $\mu(E) < \delta$ (by 23.H). If $E$ has $\mu(E) < \delta$ and $n \leq n_0$, then $|\nu_n(E)| \leq \int_E |f_n| d\mu < \epsilon$. If $n > n_0$, then
$$|\nu_n(E)| \leq \int |f_n - f_{n_0}| d\mu + \int_E |f_{n_0}| d\mu < \epsilon.$$
