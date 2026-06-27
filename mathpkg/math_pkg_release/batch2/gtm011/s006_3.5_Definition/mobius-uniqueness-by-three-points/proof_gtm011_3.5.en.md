---
role: proof
locale: en
of_concept: mobius-uniqueness-by-three-points
source_book: gtm011
source_chapter: "3"
source_section: "3.5"
---

Let $S$ be a Mobius transformation and let $a, b, c$ be distinct points in $\mathbb{C}_\infty$ with $\alpha = S(a)$, $\beta = S(b)$, $\gamma = S(c)$. Suppose $T$ is another Mobius transformation with $T(a) = \alpha$, $T(b) = \beta$, $T(c) = \gamma$. Then $T^{-1} \circ S$ is a Mobius transformation (as composition of Mobius maps) satisfying

$$(T^{-1} \circ S)(a) = T^{-1}(\alpha) = a, \quad (T^{-1} \circ S)(b) = b, \quad (T^{-1} \circ S)(c) = c.$$

Thus $T^{-1} \circ S$ has three distinct fixed points $a, b, c$. By the theorem on fixed points, a non-identity Mobius transformation has at most two fixed points, so $T^{-1} \circ S$ must be the identity transformation $I$. Hence $T^{-1} \circ S = I$, which implies $S = T$.

For existence, one constructs $S$ explicitly using the cross-ratio formula (see cross-ratio mapping).
