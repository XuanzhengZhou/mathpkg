---
role: proof
locale: en
of_concept: sum-of-orthogonal-projections
source_book: gtm023
source_chapter: "VIII"
source_section: "8.12"
---

Assume first that $E_1 \perp E_2$. Set $\pi = \pi_1 + \pi_2$. Then
$$\pi^2 = (\pi_1 + \pi_2)^2 = \pi_1^2 + \pi_1\pi_2 + \pi_2\pi_1 + \pi_2^2.$$
Since $E_1 \perp E_2$, we have $\pi_2 \circ \pi_1 = 0$ and by taking adjoints, $\pi_1 \circ \pi_2 = 0$ as well. Thus $\pi^2 = \pi_1 + \pi_2 = \pi$. Moreover, $\pi$ is selfadjoint as a sum of selfadjoint operators. Hence $\pi$ is an orthogonal projection, and $\operatorname{Im} \pi = E_1 \oplus E_2$.

Conversely, if $\pi = \pi_1 + \pi_2$ is a projection, then $\pi^2 = \pi$ implies $(\pi_1 + \pi_2)^2 = \pi_1 + \pi_2$, which yields $\pi_1\pi_2 + \pi_2\pi_1 = 0$. Applying $\pi_2$ on the left gives $\pi_2\pi_1\pi_2 + \pi_2\pi_1 = 0$, which forces $\pi_2\pi_1 = 0$, hence $E_1 \perp E_2$.
