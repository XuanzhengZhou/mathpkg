---
role: proof
locale: en
of_concept: linear-combination-of-antiderivations
source_book: gtm023
source_chapter: "5"
source_section: "§1. Basic properties"
---

Let $\Omega_1, \Omega_2$ be antiderivations with respect to $\omega$ and let $\alpha, \beta$ be scalars. Then for $\Omega = \alpha \Omega_1 + \beta \Omega_2$,

$$
\Omega(xy) = \alpha \Omega_1(xy) + \beta \Omega_2(xy)
= \alpha(\Omega_1 x \cdot y + \omega x \cdot \Omega_1 y) + \beta(\Omega_2 x \cdot y + \omega x \cdot \Omega_2 y)
$$
$$
= (\alpha \Omega_1 x + \beta \Omega_2 x) \cdot y + \omega x \cdot (\alpha \Omega_1 y + \beta \Omega_2 y)
= \Omega x \cdot y + \omega x \cdot \Omega y.
$$

Thus $\Omega$ is an antiderivation with respect to $\omega$.
