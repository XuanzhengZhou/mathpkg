---
role: proof
locale: en
of_concept: direct-sum-functional-decomposition
source_book: gtm036
source_chapter: "17"
source_section: "F"
---

Let $f \in E^*$. Define $g \in E^*$ by
$$g_t = \begin{cases} f_t & \text{if } t \in B, \\ 0 & \text{if } t \in A \setminus B. \end{cases}$$

Then $(f - g)_t = 0$ for $t \in B$, so $(\phi \circ I_t)((f - g)_t) = 0$ for all $t \in B$. By Lemma (a), $(\phi \circ I_t)((f - g)_t) = 0$ also for all $t \in A \setminus B$. Thus $(\phi \circ I_t)((f - g)_t) = 0$ for all $t \in A$.

Now consider the set of finite partial sums of components of $f - g$. This set is equicontinuous in $E^*$. Since $\phi$ is weak* continuous on equicontinuous sets and vanishes on each component, $\phi$ vanishes on every finite partial sum. By weak* continuity, $\phi(f - g) = 0$.

Therefore $\phi(f) = \phi(g) = \sum_{t \in B} (\phi \circ I_t)(g_t) = \sum_{t \in B} (\phi \circ I_t)(f_t)$, as desired.
