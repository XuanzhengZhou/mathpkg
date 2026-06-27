---
role: proof
locale: en
of_concept: uniform-convergence-uniformity-properties
source_book: gtm027
source_chapter: "7"
source_section: "Uniform Convergence"
---

# Proof of Theorem 7.8 — Properties of the Uniformity of Uniform Convergence

Let $F$ be a family of functions on $X$ to a uniform space $(Y, \mathcal{U})$. The uniformity of uniform convergence (u.c. uniformity) $\mathfrak{U}$ has as a base all sets $W(V) = \{(f, g) : (f(x), g(x)) \in V \text{ for all } x \in X\}$ for $V \in \mathcal{U}$.

**(a)** Observe that the family of all sets $\{(y, z) : d(y, z) \leq r\}$, for $r > 0$ and $d$ a bounded member of the gage of $\mathcal{U}$, forms a base for $\mathcal{U}$. This holds because for each pseudo-metric $e$, the pseudo-metric $d = \min[1, e]$ is bounded and induces the same uniformity. Now

$$\{(f, g) : d^*(f, g) \leq r\} = \{(f, g) : d(f(x), g(x)) \leq r \text{ for all } x \in X\} = W(\{(y, z) : d(y, z) \leq r\}),$$

where $d^*(f, g) = \sup\{d(f(x), g(x)) : x \in X\}$. Hence $d^*$ belongs to the gage of $\mathfrak{U}$ and the pseudo-metrics of this form generate the gage of $\mathfrak{U}$.

**(b)** If a net $\{f_n, n \in D\}$ converges uniformly to $g$, then it is clearly Cauchy relative to $\mathfrak{U}$ and converges pointwise to $g$. Conversely, suppose $\{f_n\}$ is a Cauchy net relative to $\mathfrak{U}$ and converges pointwise to $g$. Let $V$ be a closed symmetric member of $\mathcal{U}$. Choose $m \in D$ such that $(f_n, f_p) \in W(V)$ for all $n, p \geq m$. For each $x \in X$, since $f_n(x) \to g(x)$, there exists $p \geq m$ (depending on $x$) with $(f_p(x), g(x)) \in V$. Then for $n \geq m$,

$$(f_n(x), g(x)) \in (f_n(x), f_p(x)) \circ (f_p(x), g(x)) \in V \circ V.$$

Since $V$ was an arbitrary closed symmetric member, $\{f_n\}$ converges uniformly to $g$.

**(c)** If $(Y, \mathcal{U})$ is complete, let $\{f_n\}$ be a Cauchy net in $(F, \mathfrak{U})$. For each $x \in X$, the net $\{f_n(x)\}$ is Cauchy in $Y$, hence converges to some $g(x) \in Y$. Define $g(x) = \lim f_n(x)$. By part (b), $f_n \to g$ uniformly, and $g \in F$ if $F$ is closed under uniform limits. Thus $(F, \mathfrak{U})$ is complete.
