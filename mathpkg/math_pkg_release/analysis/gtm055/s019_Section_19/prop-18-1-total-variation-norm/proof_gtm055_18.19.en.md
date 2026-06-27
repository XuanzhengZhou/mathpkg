---
role: proof
locale: en
of_concept: prop-18-1-total-variation-norm
source_book: gtm055
source_chapter: "18"
source_section: "19"
---

It is clear that $\|\xi\| = 0$ if and only if $\xi$ is the zero measure, and that, if $\xi$ is any complex Borel measure on $X$ and $\alpha$ is any complex number, then $\|\alpha\xi\| = |\alpha|\|\xi\|$. Moreover, if $\xi$ and $\zeta$ are two elements of $\mathcal{M}(X)$, and if $\{E_1, \ldots, E_p\}$ is any partition of $X$ into Borel sets, then

$$\sum_{i=1}^{p} |\xi(E_i) + \zeta(E_i)| \leq \sum_{i=1}^{p} |\xi(E_i)| + \sum_{i=1}^{p} |\zeta(E_i)| \leq \|\xi\| + \|\zeta\|,$$

and therefore $\|\xi + \zeta\| \leq \|\xi\| + \|\zeta\|$. Thus $\|\xi\|$ is a norm on $\mathcal{M}(X)$. All that remains is to show that $\mathcal{M}(X)$ is complete in this norm.

Let $\{\xi_n\}$ be a sequence of complex Borel measures that is Cauchy in the total variation norm. Then for any one Borel set $E$ we have $|\xi_m(E) - \xi_n(E)| \leq \|\xi_m - \xi_n\|$, so $\{\xi_n\}$ converges setwise to a set function $\xi$ on the $\sigma$-ring $\mathcal{B}$ of Borel subsets of $X$, and it is obvious that $\xi$ is finitely additive. Hence, to prove that $\xi$ is a complex Borel measure, it suffices to show that $\xi$ is semicontinuous. Let $\{E_n\}$ be an increasing sequence of Borel sets in $X$ with union $E$, and let $\varepsilon > 0$. Choose $N$ such that $\|\xi_m - \xi_n\| < \varepsilon/3$ for $m, n \geq N$, and then choose $K$ such that $|\xi_N(E_k) - \xi_N(E)| < \varepsilon/3$ for all $k \geq K$. Then for any Borel set $F$ one has $\lim_{n \to \infty} |\xi_N(F) - \xi_n(F)| = |\xi_N(F) - \xi(F)| \leq \varepsilon/3$. Consequently $|\xi(E_k) - \xi(E)| \leq |\xi(E_k) - \xi_N(E_k)| + |\xi_N(E_k) - \xi_N(E)| + |\xi_N(E) - \xi(E)| < \varepsilon$ for all $k \geq K$, establishing semicontinuity. Thus $\mathcal{M}(X)$ is complete in the total variation norm.
