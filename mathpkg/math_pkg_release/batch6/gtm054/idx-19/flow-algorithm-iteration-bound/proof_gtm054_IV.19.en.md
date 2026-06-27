---
role: proof
locale: en
of_concept: flow-algorithm-iteration-bound
source_book: gtm054
source_chapter: "IV"
source_section: "19"
---

Let $h_0 = h$, and let $h_i$ be the feasible flow obtained in the $i$-th iteration of Step 3 of the Flow Algorithm. By the definition of $h_i$, we have $h_i(e_0) = h_{i-1}(e_0) + 1$ for $i \geq 1$. Thus $h_i(e_0) = h(e_0) + i$. Since $h_i$ is feasible, the capacity constraint $k(e_0) \geq h_i(e_0)$ holds for all $i$. Therefore the maximum number of iterations possible is $k(e_0) - h(e_0)$.
