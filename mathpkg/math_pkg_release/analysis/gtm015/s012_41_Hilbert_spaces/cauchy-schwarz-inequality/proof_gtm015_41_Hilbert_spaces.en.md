---
role: proof
locale: en
of_concept: cauchy-schwarz-inequality
source_book: gtm015
source_chapter: "41"
source_section: "Hilbert spaces"
---

# Proof of Cauchy–Schwarz inequality (in pre-Hilbert spaces)

In either case the inequality is obvious if $x = \theta$ or $y = \theta$.  Assuming $x$ and $y$ are nonzero, homogeneity permits us to suppose $\|x\| = \|y\| = 1$; the problem then reduces to proving $|(x, y)| \leq 1$ (real case) or $|(x|y)| \leq 1$ (complex case).

**Real case.**  From the defining formula (1) and the parallelogram law,

$$
\begin{aligned}
4(x, y) &= \|x + y\|^2 - \|x - y\|^2, \\[4pt]
4|(x, y)| &\leq \|x + y\|^2 + \|x - y\|^2 \qquad \text{(triangle inequality in } \mathbb{R}\text{)}\\
&= 2\|x\|^2 + 2\|y\|^2 \qquad\qquad\;\; \text{(parallelogram law)}\\
&= 4.
\end{aligned}
$$

Thus $|(x, y)| \leq 1$, as required.

**Complex case.**  Write $|(x|y)| = \mu (x|y)$ with $\mu \in \mathbb{C}$, $|\mu| = 1$ (if $(x|y) = 0$ the inequality is trivial; otherwise take $\mu = |(x|y)|/(x|y)$).  Then $(\mu x|y) = \mu(x|y) = |(x|y)|$ is real.  In the notation of the proof of Theorem 41.6 (formula (2′)),

$$(\mu x|y) = (\mu x, y) + i(\mu x, iy)$$

where $(\cdot,\cdot)$ is the real inner product.  Since $(\mu x|y)$ is real, the imaginary part vanishes, yielding $(\mu x|y) = (\mu x, y)$.  Now $\|\mu x\| = \|y\| = 1$ (absolute homogeneity), so applying the real case just proved,

$$|(x|y)| = |(\mu x|y)| = |(\mu x, y)| \leq 1.$$

This completes the proof.  $\square$
