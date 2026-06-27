---
role: proof
locale: en
of_concept: commutator-of-derivations-is-derivation
source_book: gtm023
source_chapter: "5"
source_section: "§1. Basic properties"
---

The product of two derivations $\theta_1, \theta_2$ satisfies

$$
(\theta_1 \theta_2)(xy) = \theta_1(\theta_2 x \cdot y + x \cdot \theta_2 y)
= \theta_1\theta_2 x \cdot y + \theta_2 x \cdot \theta_1 y + \theta_1 x \cdot \theta_2 y + x \cdot \theta_1\theta_2 y.
$$

Similarly,

$$
(\theta_2 \theta_1)(xy) = \theta_2\theta_1 x \cdot y + \theta_1 x \cdot \theta_2 y + \theta_2 x \cdot \theta_1 y + x \cdot \theta_2\theta_1 y.
$$

Subtracting, the cross terms cancel, yielding

$$
[\theta_1, \theta_2](xy) = [\theta_1, \theta_2]x \cdot y + x \cdot [\theta_1, \theta_2]y,
$$

which shows that $[\theta_1, \theta_2]$ is a derivation.
