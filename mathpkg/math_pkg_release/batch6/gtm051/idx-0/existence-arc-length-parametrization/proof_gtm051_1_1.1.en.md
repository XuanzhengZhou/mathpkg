---
role: proof
locale: en
of_concept: existence-arc-length-parametrization
source_book: gtm051
source_chapter: "1"
source_section: "1.1"
---

Define the arc length function $s: I \to \mathbb{R}$ by
$$s(t) = \int_{t_0}^t |\dot{c}(t')| dt', \quad t_0 \in I.$$
Since $c$ is regular, $|\dot{c}(t)| > 0$ for all $t \in I$, hence $s'(t) = |\dot{c}(t)| > 0$.

Thus $s$ is strictly increasing and differentiable, with a differentiable inverse $\phi := s^{-1}: J \to I$, where $J = s(I)$ is an interval.

Now consider $\tilde{c} := c \circ \phi: J \to \mathbb{R}^n$. By the chain rule,
$$|\tilde{c}'(s)| = |\dot{c}(\phi(s))| \cdot |\phi'(s)| = |\dot{c}(\phi(s))| \cdot \frac{1}{|\dot{c}(\phi(s))|} = 1.$$
Hence $\tilde{c}$ is parameterized by arc length.
