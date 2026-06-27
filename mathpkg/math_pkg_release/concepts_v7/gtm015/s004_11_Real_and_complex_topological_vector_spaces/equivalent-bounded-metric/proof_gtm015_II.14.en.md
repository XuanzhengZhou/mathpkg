---
role: proof
locale: en
of_concept: equivalent-bounded-metric
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "14. The space (s)"
---

# Proof of Equivalent Bounded Metric

**Lemma (14.4).** If $(X, d)$ is a metric space, the formula

$$D(x, y) = \frac{d(x, y)}{1 + d(x, y)}$$

defines an equivalent metric $D$ on $X$. In particular, a sequence in $X$ is convergent for $d$ iff it is convergent for $D$. Moreover, a sequence in $X$ is Cauchy for $d$ iff it is Cauchy for $D$; thus $X$ is complete for $d$ iff it is complete for $D$.

*Proof.* The triangle inequality for $D$ follows from Lemma (14.3): given $x, y, z \in X$, we have $d(x, z) \leq d(x, y) + d(y, z)$, so by (14.3),

$$D(x, z) = \frac{d(x,z)}{1+d(x,z)} \leq \frac{d(x,y)}{1+d(x,y)} + \frac{d(y,z)}{1+d(y,z)} = D(x, y) + D(y, z).$$

Symmetry $D(x, y) = D(y, x)$ is clear from $d(x, y) = d(y, x)$, and $D(x, y) = 0$ iff $d(x, y) = 0$ iff $x = y$. Thus $D$ is a metric.

Since $D(x, y) \leq d(x, y)$ (because $1 + d(x, y) \geq 1$), convergence in $d$ implies convergence in $D$. Conversely, if $D(x_n, x) \to 0$, then

$$d(x_n, x) = \frac{D(x_n, x)}{1 - D(x_n, x)} \to 0$$

since the denominator approaches $1$. Thus the two metrics are equivalent. The same reasoning with Cauchy sequences shows $d$-Cauchy $\iff$ $D$-Cauchy, and hence completeness is preserved. $\square$
