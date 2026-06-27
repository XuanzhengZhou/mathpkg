---
role: proof
locale: en
of_concept: completeness-of-l1
source_book: gtm018
source_chapter: "V"
source_section: "26"
---
**Proof.** By Theorem A, for each $n$ there is an integrable simple function $g_n$ with $\rho(f_n, g_n) < 1/n$. Then $\{g_n\}$ is mean fundamental; let $f$ be a measurable (hence integrable) function such that $\{g_n\}$ converges in measure to $f$. Since
$$0 \leq |\int f_n d\mu - \int f d\mu| \leq \int |f_n - f| d\mu = \rho(f_n, f) \leq \rho(f_n, g_n) + \rho(g_n, f),$$
the result follows from Theorem A.
