---
role: proof
locale: en
of_concept: completeness-of-mean-convergence
source_book: gtm018
source_chapter: "IX"
source_section: "§26. Sequences of Integrable Functions"
---

By Theorem A, for each positive integer $n$ there is an integrable simple function $g_n$ such that $\rho(f_n, g_n) < \frac{1}{n}$. It follows that $\{g_n\}$ is a mean fundamental sequence of integrable simple functions; let $f$ be a measurable (and therefore integrable) function such that $\{g_n\}$ converges in measure to $f$. Since

$$0 \leq \left|\int f_n \, d\mu - \int f \, d\mu\right| \leq \int |f_n - f| \, d\mu = \rho(f_n, f) \leq \rho(f_n, g_n) + \rho(g_n, f),$$

the desired result follows from Theorem A.
