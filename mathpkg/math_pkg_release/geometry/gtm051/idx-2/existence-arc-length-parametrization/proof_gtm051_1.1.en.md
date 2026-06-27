---
role: proof
locale: en
of_concept: existence-arc-length-parametrization
source_book: gtm051
source_chapter: "1"
source_section: "1.1"
---

The desired equation for $\phi$ is $|dc/ds| = |dc/dt| \cdot |d\phi/ds| = 1$. Define the arc length function $s(t) = \int_{t_0}^t |\dot{c}(t')| dt'$ for $t_0 \in I$, and let $s(t) = \phi^{-1}(t)$. Since $c$ is regular, $|\dot{c}(t)| > 0$ for all $t \in I$, so $s(t)$ is strictly increasing and thus invertible with differentiable inverse $\phi = s^{-1}$. By the chain rule, $|(c \circ \phi)'(s)| = |\dot{c}(\phi(s))| \cdot |\phi'(s)| = |\dot{c}(\phi(s))| \cdot (1/|\dot{c}(\phi(s))|) = 1$. Therefore $c \circ \phi$ is parametrized by arc length.
