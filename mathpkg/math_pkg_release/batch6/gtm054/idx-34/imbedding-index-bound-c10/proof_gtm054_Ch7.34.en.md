---
role: proof
locale: en
of_concept: imbedding-index-bound-c10
source_book: gtm054
source_chapter: "Chapter VII"
source_section: "Section 34"
---

Starting from C8:
$$\iota - 2 \geq \frac{\gamma - 2}{\gamma} \nu_1 - \nu_0.$$

Using C9 ($\rho\nu_0 = 2\nu_1$) to eliminate $\nu_1 = \rho\nu_0/2$:

$$\iota - 2 \geq \frac{\gamma - 2}{\gamma} \cdot \frac{\rho\nu_0}{2} - \nu_0.$$

Factor $\nu_0$ on the right:

$$\iota - 2 \geq \nu_0\left(\frac{(\gamma - 2)\rho}{2\gamma} - 1\right).$$

Rearrange:

$$\frac{\iota - 2}{\nu_0} + 1 \geq \frac{(\gamma - 2)\rho}{2\gamma}.$$

Solving for $\rho$:

$$\rho \leq \frac{2\gamma}{\gamma - 2}\left(1 + \frac{\iota - 2}{\nu_0}\right) = G(\gamma)\left(1 + \frac{\iota - 2}{\nu_0}\right).$$

This is exactly C10.
