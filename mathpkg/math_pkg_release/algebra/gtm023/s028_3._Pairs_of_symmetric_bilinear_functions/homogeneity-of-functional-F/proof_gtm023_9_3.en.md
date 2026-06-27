---
role: proof
locale: en
of_concept: homogeneity-of-functional-F
source_book: gtm023
source_chapter: "9"
source_section: "3. Pairs of symmetric bilinear functions"
---

By path independence of $J$, we may choose any convenient path to compute the difference $F(\lambda x) - F(x)$. Consider the straight line segment
$$x(t) = (1-t)\lambda x + t x, \quad 0 \leq t \leq 1.$$
Along this path,
$$\dot{x}(t) = (1-\lambda)x.$$
The integrand of $J$ involves the expression $\Phi(x)\Psi(x,\dot{x}) - \Phi(x,\dot{x})\Psi(x)$. Using the symmetry of $\Phi$ and $\Psi$:
$$\Phi(x(t))\Psi(x(t),\dot{x}) - \Phi(x(t),\dot{x})\Psi(x(t)) = (1-\lambda)\bigl[\Phi(x(t))\Psi(x(t),x) - \Phi(x(t),x)\Psi(x(t))\bigr].$$
Since $x(t)$ is collinear with $x$, we have $\Phi(x(t),x) = \Phi(x(t))\cdot\text{const}$ and $\Psi(x(t),x) = \Psi(x(t))\cdot\text{const}$, and the bracket vanishes. Therefore the integrand is identically zero along this path, yielding
$$\int_{x}^{\lambda x} \frac{\Phi(x)\Psi(x,\dot{x}) - \Phi(x,\dot{x})\Psi(x)}{\Phi(x)^2 + \Psi(x)^2}\,dt = 0.$$
Hence $F(\lambda x) = F(x)$.
