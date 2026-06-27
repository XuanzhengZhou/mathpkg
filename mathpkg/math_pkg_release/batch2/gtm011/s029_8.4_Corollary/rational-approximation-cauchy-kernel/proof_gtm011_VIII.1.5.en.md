---
role: proof
locale: en
of_concept: rational-approximation-cauchy-kernel
source_book: gtm011
source_chapter: "VIII"
source_section: "1.5"
---

Since $K$ and $\{\gamma\}$ are disjoint, there exists a number $r$ with $0 < r < d(K, \{\gamma\})$. If $\gamma$ is defined on $[0, 1]$, then for $0 \leq s, t \leq 1$ and $z$ in $K$:

$$\left| \frac{f(\gamma(t))}{\gamma(t)-z} - \frac{f(\gamma(s))}{\gamma(s)-z} \right| \leq \frac{1}{r^2} \Big| f(\gamma(t))\gamma(s) - f(\gamma(s))\gamma(t) - z[f(\gamma(t)) - f(\gamma(s))] \Big|$$

$$\leq \frac{1}{r^2} |f(\gamma(t))| \, |\gamma(s) - \gamma(t)| + \frac{1}{r^2} |\gamma(t)| \, |f(\gamma(s)) - f(\gamma(t))| + \frac{|z|}{r^2} |f(\gamma(s)) - f(\gamma(t))|.$$

There is a constant $c > 0$ such that $|z| \leq c$ for all $z$ in $K$, $|\gamma(t)| \leq c$, and $|f(\gamma(t))| \leq c$ for all $t$ in $[0, 1]$. This yields a uniform Lipschitz estimate for the integrand. Choose a partition $0 = t_0 < t_1 < \cdots < t_n = 1$ of $[0, 1]$ sufficiently fine so that the oscillation of the integrand on each subinterval is small. Define the rational function

$$R(z) = \sum_{k=1}^{n} \frac{f(\gamma(t_k))}{\gamma(t_k) - z} (\gamma(t_k) - \gamma(t_{k-1})),$$

which is a Riemann sum approximation of the integral and whose poles are exactly the points $\gamma(t_k) \in \{\gamma\}$. The uniform continuity estimate ensures that $| \int_\gamma f(w)/(w-z) dw - R(z) | < \varepsilon$ for all $z \in K$.
