---
role: proof
locale: en
of_concept: antiderivation-squared-is-derivation
source_book: gtm023
source_chapter: "5"
source_section: "§1. Basic properties"
---

Let $\Omega_1, \Omega_2$ be two antiderivations with respect to the same involution $\omega$ such that $\omega \Omega_i = -\Omega_i \omega$ for $i = 1, 2$. Then

$$
\Omega_1\Omega_2(xy) = \Omega_1(\Omega_2 x \cdot y + \omega x \cdot \Omega_2 y)
$$
$$
= \Omega_1\Omega_2 x \cdot y + \omega\Omega_2 x \cdot \Omega_1 y + \Omega_1\omega x \cdot \Omega_2 y + \omega x \cdot \Omega_1\Omega_2 y.
$$

Since $\omega\Omega_i = -\Omega_i\omega$, we have $\omega\Omega_2 = -\Omega_2\omega$ and $\Omega_1\omega = -\omega\Omega_1$. Substituting,

$$
\Omega_1\Omega_2(xy) = \Omega_1\Omega_2 x \cdot y - \Omega_2\omega x \cdot \Omega_1 y - \omega\Omega_1 x \cdot \Omega_2 y + \omega x \cdot \Omega_1\Omega_2 y.
$$

Similarly,

$$
\Omega_2\Omega_1(xy) = \Omega_2\Omega_1 x \cdot y - \Omega_1\omega x \cdot \Omega_2 y - \omega\Omega_2 x \cdot \Omega_1 y + \omega x \cdot \Omega_2\Omega_1 y.
$$

Adding these two equations, the cross terms cancel, yielding

$$
(\Omega_1\Omega_2 + \Omega_2\Omega_1)(xy) = (\Omega_1\Omega_2 + \Omega_2\Omega_1)x \cdot y + \omega x \cdot (\Omega_1\Omega_2 + \Omega_2\Omega_1)y.
$$

But $\omega x = x$ when acting through the derivation property (as $\Omega_i$ satisfy the condition), giving the derivation property for $\Omega_1\Omega_2 + \Omega_2\Omega_1$. Taking $\Omega_1 = \Omega_2 = \Omega$ yields that $\Omega^2$ is a derivation.
