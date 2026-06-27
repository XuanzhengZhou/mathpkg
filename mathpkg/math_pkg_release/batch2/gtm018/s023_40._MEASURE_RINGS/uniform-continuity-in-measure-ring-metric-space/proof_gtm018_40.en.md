---
role: proof
locale: en
of_concept: uniform-continuity-in-measure-ring-metric-space
source_book: gtm018
source_chapter: "X"
source_section: "40. Measure Rings"
---

The desired results are immediate consequences of the relations

$$\mu((E_1 \cup F_1) \Delta (E_2 \cup F_2)) + \mu((E_2 \cup F_2) \Delta (E_1 \cup F_1)) \leq$$

$$\mu((E_1 \cap F_1) \Delta (E_2 \cap F_2)) + \mu((E_2 \cap F_2) \Delta (E_1 \cap F_1)) \leq$$

In more detail, to prove uniform continuity of the union $f(E,F) = E \cup F$, observe that

$$(E_1 \cup F_1) \Delta (E_2 \cup F_2) \subset (E_1 \Delta E_2) \cup (F_1 \Delta F_2).$$

Consequently,

$$\rho(E_1 \cup F_1, E_2 \cup F_2) = \mu((E_1 \cup F_1) \Delta (E_2 \cup F_2)) \leq \mu(E_1 \Delta E_2) + \mu(F_1 \Delta F_2) = \rho(E_1, E_2) + \rho(F_1, F_2).$$

Thus if $(E_1, F_1)$ and $(E_2, F_2)$ are close in the product metric, their unions are close, establishing uniform continuity of $f$. A similar argument applies to $g(E,F) = E \cap F$, using the same symmetric difference estimates.

For the measure $\mu$, we have

$$|\mu(E) - \mu(F)| \leq \mu(E \Delta F) = \rho(E, F),$$

which shows that $\mu$ is Lipschitz and hence uniformly continuous.
