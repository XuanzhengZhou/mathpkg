---
role: proof
locale: en
of_concept: lemma-3-2-density-on-halfspaces
source_book: gtm033
source_chapter: "2"
source_section: "3. Approximations on ∂-Manifolds and Manifold Pairs"
---

# Proof of Lemma 3.2: Density of Smooth Maps on Halfspaces

**Lemma 3.2.** Let $E \subset \mathbb{R}^m$, $F \subset \mathbb{R}^n$ be halfspaces and $U \subset E$, $V \subset F$ open sets. Then $C^\infty(U,V)$ is dense in $C_S^r(U,V)$, and $C^\infty(U,\partial U; V,\partial V)$ is dense in $C_S^r(U,\partial U; V,\partial V)$, $r < \infty$.

*Proof.* We use a variation of the convolution of Section 2.1. Let $\theta: \mathbb{R}^m \to \mathbb{R}$ be a $C^\infty$ convolution kernel of the special form

$$\theta(x,y) = \alpha(x)\beta(y)$$

where $\alpha: \partial E \to \mathbb{R}$, $\beta: \mathbb{R} \to \mathbb{R}$ are $C^\infty$ convolution kernels.

Suppose $\alpha$, $\beta$ and $\theta$ have support radius less than $\delta > 0$. Let $U' = \{(x,y) \in U \mid (x,z) \in U \text{ if } y \leqslant z < y + \delta\}$. Define

$$h: U' \to \mathbb{R}^n,$$

$$h(x,y) = \int_{t \geqslant 0} \int_{s \in \partial E} f(x - s, y + t)\,\alpha(s)\beta(t)\,ds\,dt.$$

Then $h$ is $C^\infty$ and $\|h - f\|_{r,U'} \to 0$ as $\delta \to 0$. Moreover $h(U') \subset F$ because $\alpha$ and $\beta$ are nonnegative. If $f(\partial U) \subset \partial F$ then $f(x,y) \geqslant f(x,0)$, which implies $h(x,y) \geqslant h(x,0)$. Now define $g(x,y) = h(x,y) - h(x,0)$. Then $g(U') \subset F$ and $g(\partial U') \subset \partial F$. If $\delta$ is small enough, the map $g: U' \to F$ satisfies the lemma.

Thus $C^\infty$ maps are dense in the strong $C^r$ topology for both the absolute and relative (manifold pair) cases.

QED
