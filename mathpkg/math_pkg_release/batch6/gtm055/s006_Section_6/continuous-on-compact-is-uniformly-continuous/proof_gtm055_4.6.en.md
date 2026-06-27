---
role: proof
locale: en
of_concept: continuous-on-compact-is-uniformly-continuous
source_book: gtm055
source_chapter: "4"
source_section: "6"
---

Let $\varepsilon$ be a positive number. For each point $x$ of $X$ there exists a $\delta_x > 0$ such that $\rho'(f(x'), f(x)) < \varepsilon/2$ whenever $x'$ is a point of $X$ such that $\rho(x', x) < \delta_x$. The open balls $D_{\delta_x/2}(x)$ cover $X$, so there exists a finite set of points $x_1, \ldots, x_n$ in $X$ such that the balls

$$D_i = D_{\delta_{x_i}/2}(x_i), \quad i = 1, \ldots, n,$$

cover $X$. Let $\delta_i = \delta_{x_i}$, $i = 1, \ldots, n$, set $\delta = \delta_1 \wedge \cdots \wedge \delta_n$, and suppose $\rho(x', x'') < \delta/2$. Then $x'$ belongs to some $D_i$, and it follows that $x'$ and $x''$ both belong to $D_{\delta_i}(x_i)$. But then $\rho'(f(x'), f(x_i)) < \varepsilon/2$ and $\rho'(f(x''), f(x_i)) < \varepsilon/2$, so that $\rho'(f(x'), f(x'')) < \varepsilon$.
