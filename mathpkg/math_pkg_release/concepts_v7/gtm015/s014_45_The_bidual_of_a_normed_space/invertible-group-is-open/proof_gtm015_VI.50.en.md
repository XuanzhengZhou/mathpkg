---
role: proof
locale: en
of_concept: invertible-group-is-open
source_book: gtm015
source_chapter: "VI"
source_section: "50"
---

# Proof that the Group of Invertible Elements is Open

Let $A$ be a Banach algebra with unity $1$, and let $U$ be the set of invertible elements. We must show: if $x \in U$, then there exists $\varepsilon > 0$ such that $\{y : \|y - x\| < \varepsilon\} \subset U$. Specifically, we claim $\varepsilon = \|x^{-1}\|^{-1}$ works.

Let $y \in A$ satisfy $\|y - x\| < \|x^{-1}\|^{-1}$. Then
$$\|1 - yx^{-1}\| = \|(x - y)x^{-1}\| \leq \|x - y\|\|x^{-1}\| < \|x^{-1}\|^{-1} \cdot \|x^{-1}\| = 1.$$

By Corollary 50.3 (elements within distance $1$ of unity are invertible), the element $yx^{-1}$ belongs to $U$, i.e., there exists $v \in A$ such that $(yx^{-1})v = v(yx^{-1}) = 1$. It follows that
$$y = (yx^{-1})x \in U \cdot U \subset U,$$
since the product of two invertible elements is invertible: $(yx^{-1})x$ has inverse $x^{-1}(yx^{-1})^{-1}$.

Thus $\{y : \|y - x\| < \|x^{-1}\|^{-1}\} \subset U$, proving $U$ is open in $A$. $\square$
