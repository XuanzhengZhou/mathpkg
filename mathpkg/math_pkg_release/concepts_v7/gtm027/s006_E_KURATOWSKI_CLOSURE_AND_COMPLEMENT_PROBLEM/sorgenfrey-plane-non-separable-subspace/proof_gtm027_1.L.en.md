---
role: proof
locale: en
of_concept: sorgenfrey-plane-non-separable-subspace
source_book: gtm027
source_chapter: "1"
source_section: "L"
---

# Proof that the Sorgenfrey Plane Contains a Non-Separable Subspace

**Proposition.** The space $(Y, \mathfrak{U})$ (the Sorgenfrey plane) contains a subspace which is not separable.

*Proof.* Consider the anti-diagonal subspace:
$$Z = \{(x,y) \in \mathbb{R}^2 : x + y = 1\},$$
with the subspace topology inherited from the Sorgenfrey plane.

For each $x \in \mathbb{R}$, the point $(x, 1-x)$ belongs to $Z$. These points are distinct for distinct $x$.

Consider the open sets $U_x = [x, x+1) \times [1-x, 2-x)$ in the Sorgenfrey plane. The intersection $U_x \cap Z$ contains exactly the point $(x, 1-x)$: if $(t, 1-t) \in U_x \cap Z$, then $x \leq t < x+1$ and $1-x \leq 1-t < 2-x$. From the second inequality, $-x \leq -t < 1-x$, so $x-1 < t \leq x$. Combined with $x \leq t < x+1$, we get $t = x$.

Thus each point $(x, 1-x)$ of $Z$ has an open neighborhood in $Y$ whose intersection with $Z$ is a singleton. This means $Z$ is discrete in the subspace topology.

An uncountable discrete space cannot be separable (any dense subset must intersect every singleton open set, hence must contain every point). Since $Z$ has the cardinality of $\mathbb{R}$ (uncountable), $Z$ is not separable. $\square$
