---
role: proof
locale: en
of_concept: uniform-limit-of-continuous-functions
source_book: gtm011
source_chapter: "II"
source_section: "6"
---

Fix $x_0$ in $X$ and $\epsilon > 0$; we wish to find a $\delta > 0$ such that $\rho(f(x_0), f(x)) < \epsilon$ when $d(x_0, x) < \delta$. Since $f = u - \lim f_n$, there is a function $f_n$ with $\rho(f(x), f_n(x)) < \epsilon/3$ for all $x$ in $X$. Since $f_n$ is continuous there is a $\delta > 0$ such that $\rho(f_n(x_0), f_n(x)) < \epsilon/3$ when $d(x_0, x) < \delta$. Therefore, if $d(x_0, x) < \delta$,
$$\rho(f(x_0), f(x)) \leq \rho(f(x_0), f_n(x_0)) + \rho(f_n(x_0), f_n(x)) + \rho(f_n(x), f(x)) < \epsilon.$$
