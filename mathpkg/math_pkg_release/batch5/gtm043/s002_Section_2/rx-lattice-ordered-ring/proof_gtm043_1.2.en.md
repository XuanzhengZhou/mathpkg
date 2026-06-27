---
role: proof
locale: en
of_concept: rx-lattice-ordered-ring
source_book: gtm043
source_chapter: "1"
source_section: "1.2"
---

For any $f, g \in \mathbf{R}^X$, define $k(x) = f(x) \vee g(x)$. Then for each $x$, $k(x) \geq f(x)$ and $k(x) \geq g(x)$, so $k \geq f$ and $k \geq g$. If $h \geq f$ and $h \geq g$, then $h(x) \geq f(x)$ and $h(x) \geq g(x)$ for all $x$, hence $h(x) \geq f(x) \vee g(x) = k(x)$, so $h \geq k$. Therefore $f \vee g = k$ exists. Dually, $(f \wedge g)(x) = f(x) \wedge g(x)$ gives the meet. Thus $\mathbf{R}^X$ is a lattice.

Defining $|f| = f \vee (-f)$, we have $|f|(x) = f(x) \vee (-f(x)) = |f(x)|$, the ordinary absolute value in $\mathbf{R}$. The ring $\mathbf{R}$ is totally ordered, but if $X$ has at least two distinct points $x_1, x_2$, then functions $f$ and $g$ with $f(x_1) > g(x_1)$ and $f(x_2) < g(x_2)$ are incomparable, so $\mathbf{R}^X$ is not totally ordered.
