---
role: proof
locale: en
of_concept: continuity-of-linear-transformations
source_book: gtm055
source_chapter: "12"
source_section: "Bounded linear transformations"
---

Since it is clear that (i) implies (ii), it will suffice to show that (ii) implies (iii) and that (iii) implies (i). To see that (ii) implies (iii), choose $\delta > 0$ such that $\|x\| = \|x - 0\| \leq \delta$ implies $\|Tx\| = \|Tx - T0\| \leq 1$. Then $Tx$ belongs to the ball $\mathcal{F}_{1/\delta}$ whenever $x$ belongs to the unit ball $\mathcal{E}_1$, and from this it follows at once that $T$ is bounded. Finally, to see that (iii) implies (i), let $x_0$ be a vector in $\mathcal{E}$ and let $\varepsilon$ be positive. Then for $\delta = \varepsilon/(\|T\| + 1)$ and $\|x - x_0\| < \delta$, we have

$$\|Tx - Tx_0\| \leq \|T\| \|x - x_0\| < \varepsilon.$$

Thus $T$ is continuous at $x_0$. The inequality

$$\|Tx_1 - Tx_2\| \leq \|T\| \|x_1 - x_2\|$$

is valid for an arbitrary pair of vectors $x_1, x_2$ in $\mathcal{E}$, showing that a continuous (hence bounded) linear transformation between two normed spaces is automatically Lipschitzian, and in particular, uniformly continuous.
