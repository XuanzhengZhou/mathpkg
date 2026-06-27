---
role: proof
locale: en
of_concept: convergence-property-vs-uniform-convexity
source_book: gtm036
source_chapter: "5"
source_section: "17"
---

This is stated as Problem C(d) in the text, with reference to Banach [1] Ch. IX, §3, p. 140. The key observation is that $\ell^1$ has the Schur property: every weakly convergent sequence in $\ell^1$ is norm convergent. Therefore, if $x_n \to x_0$ weakly and $\|x_n\| \to \|x_0\|$, then automatically $\|x_n - x_0\| \to 0$, so the convergence property holds. However, $\ell^1$ is not uniformly convex: for $x = e_1$, $y = e_2$ (standard basis vectors), one has $\|x\| = \|y\| = 1$ but $\|x + y\| = 2$, so the midpoint $\frac{x+y}{2}$ has norm $1$, violating the condition that $\|\frac{x+y}{2}\| < 1 - \delta$ for some $\delta > 0$ whenever $\|x\| = \|y\| = 1$ and $\|x - y\| \geq \varepsilon$.
