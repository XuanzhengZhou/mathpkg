---
role: proof
locale: en
of_concept: norm-distance-is-metric
source_book: gtm023
source_chapter: "VII"
source_section: "5 (7.19)"
---

From $N_1$ we have $\|x-y\| \geq 0$ and $\|x-y\| = 0$ only if $x-y = 0$, i.e., $x = y$. Hence $\varrho(x,y) > 0$ if $x \neq y$.

From $N_2$ we obtain
$$\varrho(x,y) = \|x-y\| = \|(x-z) + (z-y)\| \leq \|x-z\| + \|z-y\| = \varrho(x,z) + \varrho(z,y).$$

From $N_3$ with $\lambda = -1$ we have $\|-(x-y)\| = \|x-y\|$, so
$$\varrho(y,x) = \|y-x\| = \|-(x-y)\| = \|x-y\| = \varrho(x,y).$$

Thus $\varrho$ is a metric. Continuity of addition follows from $N_2$ and continuity of scalar multiplication from $N_3$, making $E$ a topological vector space.
