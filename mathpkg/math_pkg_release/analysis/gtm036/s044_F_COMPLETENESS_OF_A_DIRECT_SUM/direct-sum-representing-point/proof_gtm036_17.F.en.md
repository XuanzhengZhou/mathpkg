---
role: proof
locale: en
of_concept: direct-sum-representing-point
source_book: gtm036
source_chapter: "17"
source_section: "F"
---

For each $t \in B$, the composition $\phi \circ I_t$ is a linear functional on $E_t^*$. By hypothesis, $\phi$ is weak* continuous on every equicontinuous subset of $E^*$. Since $I_t$ maps $E_t^*$ into $E^*$ and preserves equicontinuity, each $\phi \circ I_t$ is weak* continuous on $E_t^*$.

Each $E_t$ is complete by assumption. Applying Grothendieck's completeness theorem (17.7) to $E_t$, the weak* continuity of $\phi \circ I_t$ on $E_t^*$ implies that there exists a point $x_t \in E_t$ such that
$$(\phi \circ I_t)(f_t) = f_t(x_t)$$
for all $f_t \in E_t^*$.

Define $x = \sum_{t \in B} x_t$, which belongs to the finite direct sum $\sum \{E_t : t \in B\} \subseteq E$. For any $f \in E^*$, by Lemma (b):
$$\phi(f) = \sum_{t \in B} (\phi \circ I_t)(f_t) = \sum_{t \in B} f_t(x_t) = f(x).$$

Thus $\phi$ is the evaluation functional at $x \in E$.
