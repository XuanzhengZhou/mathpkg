---
role: proof
locale: en
of_concept: weil-neighborhood-measurable-positive-measure
source_book: gtm018
source_chapter: "62"
source_section: "Weil Topology"
---

**Theorem C.** Since $N = \{x : \mu(xE \cap E) > \mu(E) - \frac{\varepsilon}{2}\}$, the measurability of $N$ follows from 59.F, which establishes that the function $x \mapsto \mu(xE \cap E)$ is measurable. 

To prove that $\mu(N) > 0$, we apply Theorem A. If $G$ is a measurable set of positive measure such that $GG^{-1} \subset N$, then, in particular, $Gy^{-1} \subset N$ for any $y \in G$. Since $\mu(G) > 0$, it follows that $\mu(N) > 0$.

The last assertion of the theorem follows from the relations:

$$\left(\mu(E) - \frac{\varepsilon}{2}\right)\mu(N) \leq \int_N \mu(xE \cap E) d\mu(x) \leq \int_X \mu(xE \cap E) d\mu(x) = \mu(E)\mu(E^{-1}).$$

Thus if $\mu(E^{-1}) < \infty$, then $\mu(N) < \infty$. $\blacksquare$
