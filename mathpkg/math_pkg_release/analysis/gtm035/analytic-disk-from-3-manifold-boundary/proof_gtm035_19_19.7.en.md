---
role: proof
locale: en
of_concept: analytic-disk-from-3-manifold-boundary
source_book: gtm035
source_chapter: "Chapter 19"
source_section: "19.7"
---

# Proof of Existence of Analytic Disks from 3-Manifold Boundary

**Proof.** We regard $K$ as defined on $\mathbb{C}^2 \times \mathbb{C}^2 \setminus \{z = \zeta\}$. Here

$$K(\zeta, z) = \left( \frac{\bar{\zeta}_1 - \bar{z}_1}{|\zeta - z|^4} d\bar{\zeta}_2 - \frac{\bar{\zeta}_2 - \bar{z}_2}{|\zeta - z|^4} d\bar{\zeta}_1 \right) \wedge d\zeta_1 \wedge d\zeta_2.$$

So $\bar{\partial}_z K(\zeta, z)$ is a form on $\mathbb{C}^2 \times \mathbb{C}^2 \setminus \{z = \zeta\}$ of type $(2, 1)$ in $\zeta$ and type $(0, 1)$ in $z$. We define a form $K_1$ on $\mathbb{C}^2 \times \mathbb{C}^2 \setminus \{z = \zeta\}$ by

$$K_1(\zeta, z) = \bar{\partial}_z K(\zeta, z).$$

A direct computation shows that $K_1$ is, up to a constant factor, the Bochner-Martinelli kernel in $\mathbb{C}^3$ pulled back to a suitable submanifold. The maximally complex hypothesis on $M$ then implies that the integral of $\psi(\zeta, \eta) \pi^*(K_1(\zeta, z))$ over $M$ vanishes, which yields $\bar{\partial} F(z) = 0$. Hence $F$ is analytic on $U$.

*Note: The section text is truncated at this point; the complete proof requires a detailed computation of $K_1$ and application of the maximal complexity condition. See the original text [HarL2] for the full argument.* $\square$
