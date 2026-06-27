---
role: proof
locale: en
of_concept: classification-of-maps-to-sphere
source_book: gtm033
source_chapter: "5"
source_section: "1. Degrees of Maps"
---

# Proof of Theorem 1.10 (Classification of Maps into the Sphere by Degree)

**Theorem statement.** Let $M$ be a compact connected $n$-manifold, $n \geqslant 1$. Let $f, g: M \to S^n$ be continuous maps.

(a) If $M$ is oriented and $\partial M = \varnothing$, then $f \simeq g$ (homotopic) if and only if $\deg f = \deg g$; and there exist maps of every integer degree.

(b) If $M$ is nonorientable and $\partial M = \varnothing$, then $f \simeq g$ if and only if $\deg_2 f = \deg_2 g$; and both mod 2 degrees are realized.

(c) If $\partial M \neq \varnothing$, then every map $M \to S^n$ is null-homotopic.

**Proof.** (a) First, suppose $f \simeq g$. By Theorem 1.6(a), $\deg f = \deg g$. Conversely, suppose $\deg f = \deg g$. Consider the map $F: \partial(M \times I) = M \times \{0\} \sqcup M \times \{1\} \to S^n$ defined by $F(x, 0) = f(x)$, $F(x, 1) = g(x)$. The oriented boundary of $M \times I$ is $\partial(M \times I) = M \times \{1\} \sqcup (-M) \times \{0\}$ (where $-M$ denotes $M$ with the opposite orientation). The degree of $F$ on this boundary is $\deg g - \deg f = 0$. By Theorem 1.8, $F$ extends to a map $H: M \times I \to S^n$, which is precisely a homotopy from $f$ to $g$.

To construct maps of every integer degree $m$, it suffices to produce a map $S^n \to S^n$ of degree $m$ and compose with a map $M \to S^n$ of degree $1$ (e.g., a constant map to a point, followed by the identity on $S^n$, appropriately modified). Maps $S^n \to S^n$ of arbitrary degree exist: for $m \geqslant 0$, take the suspension of a degree-$m$ map $S^{n-1} \to S^{n-1}$; for negative $m$, compose with the antipodal map if $n$ is odd, or with a reflection.

(b) The mod 2 case follows the same pattern using Theorem 1.9. If $\deg_2 f = \deg_2 g$, then the map on $\partial(M \times I)$ has mod 2 degree $0$ and extends to a homotopy by Theorem 1.9.

(c) If $\partial M \neq \varnothing$, regard $M$ as a subset of itself. The map $f$ extends to a map of the cone on $M$ (which is $M \times I / M \times \{1\}$) by sending the cone point to any point of $S^n$. Since $M \times I$ is a compact oriented $(n+1)$-manifold with boundary, and $f$ extends over it (modulo the cone construction), $f$ is null-homotopic. More directly, Theorem 1.8 (or 1.9) with $W = M$ (considered as a $\partial$-manifold) implies $f$ is homotopic to a constant map.
