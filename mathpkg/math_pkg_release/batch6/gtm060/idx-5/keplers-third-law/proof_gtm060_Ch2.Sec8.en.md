---
role: proof
locale: en
of_concept: keplers-third-law
source_book: gtm060
source_chapter: "2"
source_section: "8"
---

**Proof.** Let $T$ be the period of revolution and $S$ the area swept out by the radius vector in time $T$. Since $M/2$ is the sectorial velocity (the areal velocity), we have $2S = MT$. The area of the ellipse is $S = \pi ab$, hence $T = 2\pi ab / M$.

From the geometry of the ellipse, the major semi-axis is
$$a = \frac{p}{1 - e^2} = \frac{M^2/k}{2|E| M^2/k^2} = \frac{k}{2|E|},$$
where $k$ is the gravitational constant (coefficient in $U = -k/r$) and $E$ is the total energy. The minor semi-axis is
$$b = \frac{M^2}{k} \cdot \frac{1}{\sqrt{2|E| M/k}} = \frac{M}{\sqrt{2|E|}}.$$

Substituting these into $T = 2\pi ab/M$:
$$T = 2\pi \frac{k}{2|E|} \cdot \frac{M}{\sqrt{2|E|}} \cdot \frac{1}{M} = 2\pi \frac{k}{(2|E|)^{3/2}}.$$

Since $2|E| = k/a$, we obtain $T = 2\pi a^{3/2} k^{-1/2}$. Therefore $T^2 \propto a^3$, which is Kepler's Third Law.
