---
role: proof
locale: en
of_concept: product-metrizability
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "14. The space (s)"
---

# Proof of Product Metrizability

**Lemma (14.5).** The product of a sequence of metrizable topological spaces is metrizable. Explicitly, suppose $(X_n, d_n)$ ($n = 1, 2, 3, \ldots$) is a sequence of metric spaces and $X = \prod_{n=1}^{\infty} X_n$ is the Cartesian product of the sets $X_n$. For $x = (x_n)$, $y = (y_n)$ in $X$, define

$$d(x, y) = \sum_{n=1}^{\infty} 2^{-n} \frac{d_n(x_n, y_n)}{1 + d_n(x_n, y_n)}.$$

Then $d$ is a metric on $X$ and the $d$-topology coincides with the product topology.

*Proof.* Let $D_n(x_n, y_n) = \frac{d_n(x_n, y_n)}{1 + d_n(x_n, y_n)}$. By (14.4), each $D_n$ is a metric on $X_n$ bounded by $1$ and equivalent to $d_n$. The series $d(x, y) = \sum_{n=1}^{\infty} 2^{-n} D_n(x_n, y_n)$ converges since each term is bounded by $2^{-n}$.

**$d$ is a metric:** Nonnegativity and symmetry are clear. If $x = y$ then each $D_n(x_n, y_n) = 0$, so $d(x, y) = 0$. Conversely, if $d(x, y) = 0$ then each $D_n(x_n, y_n) = 0$, hence $x_n = y_n$ for all $n$, so $x = y$. The triangle inequality follows from the triangle inequality for each $D_n$:

$$d(x, z) = \sum 2^{-n} D_n(x_n, z_n) \leq \sum 2^{-n}(D_n(x_n, y_n) + D_n(y_n, z_n)) = d(x, y) + d(y, z).$$

**Topology equivalence:** Let $\tau$ be the product topology and $\tau_d$ the $d$-topology. Write $U_\varepsilon(a) = \{x : d(x, a) < \varepsilon\}$.

To show $\tau_d \subset \tau$: Given $\varepsilon > 0$, choose $N$ such that $\sum_{n=N+1}^{\infty} 2^{-n} < \varepsilon/2$. Define

$$U = \{x : \sum_{n=1}^{N} 2^{-n} D_n(x_n, a_n) < \varepsilon/2\}.$$

Then $U$ is $\tau$-open (it restricts only finitely many coordinates) and $U \subset U_\varepsilon(a)$, since for $x \in U$,

$$d(x, a) < \varepsilon/2 + \sum_{n=N+1}^{\infty} 2^{-n} < \varepsilon.$$

To show $\tau \subset \tau_d$: A basic $\tau$-neighborhood restricts only finitely many coordinates. By the equivalence of $D_n$ and $d_n$, any such restriction can be captured by requiring $d(x, a)$ small enough, using that $d(x, a) \geq 2^{-n} D_n(x_n, a_n)$ for each $n$, so convergence in $d$ implies coordinatewise convergence. Conversely, if a sequence converges coordinatewise, a standard $\varepsilon/2$-argument using the tail bound $\sum_{n > N} 2^{-n} < \varepsilon/2$ shows $d$-convergence.

The same reasoning with Cauchy sequences holds: a sequence is $d$-Cauchy iff it is coordinatewise Cauchy. $\square$
