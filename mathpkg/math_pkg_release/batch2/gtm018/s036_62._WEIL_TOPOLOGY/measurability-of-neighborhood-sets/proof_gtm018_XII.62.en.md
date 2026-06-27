---
role: proof
locale: en
of_concept: measurability-of-neighborhood-sets
source_book: gtm018
source_chapter: "XII"
source_section: "62"
---

Since $N = \{x : \mu(xE \cap E) > \mu(E) - \epsilon/2\}$, the measurability of $N$ follows from 59.F. To prove that $\mu(N) > 0$, we apply Theorem A. If $G$ is a measurable set of positive measure such that $GG^{-1} \subset N$, then, in particular, $Gy^{-1} \subset N$ for any $y$ in $G$. Since $\mu(G) > 0$, this implies $\mu(N) > 0$.

The last assertion of the theorem follows from the relations

$$\left(\mu(E) - \frac{\epsilon}{2}\right) \mu(N) \leq \int_N \mu(xE \cap E) \, d\mu(x) \leq \int_X \mu(xE \cap E) \, d\mu(x) = \mu(E) \mu(E^{-1}).$$

If $\mu(E^{-1}) < \infty$, then $\mu(N) \leq \frac{\mu(E)\mu(E^{-1})}{\mu(E) - \epsilon/2} < \infty$.
