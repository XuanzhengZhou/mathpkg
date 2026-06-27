---
role: proof
locale: en
of_concept: cross-ratio-reality-and-concyclicity
source_book: gtm011
source_chapter: "3"
source_section: "3.10"
---

Let $S(z) = (z, z_2, z_3, z_4)$ be the unique Mobius transformation sending $z_2 \mapsto 1$, $z_3 \mapsto 0$, $z_4 \mapsto \infty$. Then $(z_1, z_2, z_3, z_4)$ is real if and only if $S(z_1) \in \mathbb{R}_\infty$. The set of points $z$ such that $(z, z_2, z_3, z_4) \in \mathbb{R}$ is precisely $S^{-1}(\mathbb{R}_\infty)$. It therefore suffices to show that the image of $\mathbb{R}_\infty$ under any Mobius transformation is a generalized circle.

Let $T(z) = \frac{az+b}{cz+d}$ be a Mobius transformation, and let $z = x \in \mathbb{R}$ with $\omega = T(x) \neq \infty$. Then $T(x) = \overline{T(x)}$, i.e.,

$$\frac{a\omega + b}{c\omega + d} = \overline{\left(\frac{a\omega + b}{c\omega + d}\right)} = \frac{\bar{a}\bar{\omega} + \bar{b}}{\bar{c}\bar{\omega} + d}.$$

Cross-multiplying and setting $\omega = u + iv$ yields:

$$(a\bar{c} - \bar{a}c)|\omega|^2 + (a\bar{d} - \bar{b}c)\omega + (b\bar{c} - d\bar{a})\bar{\omega} + (b\bar{d} - \bar{b}d) = 0.$$

This is the general equation of a circle or a straight line in $\mathbb{C}$. Specifically:
- If $a\bar{c}$ is real (so that $a\bar{c} - \bar{a}c = 0$), the equation is linear in $\omega$ and $\bar{\omega}$, representing a straight line.
- Otherwise, completing the square shows the equation represents a circle.

Thus $T(\mathbb{R}_\infty)$ is a generalized circle. Applying this to $T = S^{-1}$, we see that $S^{-1}(\mathbb{R}_\infty)$ is a generalized circle, which is exactly the set of points $z$ with real cross-ratio. But $S^{-1}(\mathbb{R}_\infty)$ is the unique generalized circle passing through $z_2, z_3, z_4$ (since $S(z_2) = 1 \in \mathbb{R}$, $S(z_3) = 0 \in \mathbb{R}$, $S(z_4) = \infty \in \mathbb{R}_\infty$). Hence $(z_1, z_2, z_3, z_4) \in \mathbb{R}$ if and only if $z_1$ lies on the same generalized circle as $z_2, z_3, z_4$.
