---
role: proof
locale: en
of_concept: maximum-flow-vertex-edge-equivalence
source_book: gtm054
source_chapter: "IV"
source_section: "19"
---

As established in F3, the mapping $h \mapsto \bar{h}$ is a bijection from the set of feasible flows on $(V, D)$ onto the set of feasible flows on the edge-capacitated network $(X, k)$. By the definition of $\bar{h}$, for $e_0 = (x_0^2, x_0^1)$ we have

$$\bar{h}(x_0^2, x_0^1) = h(x_0)$$

directly from the third clause of the definition. Since the mapping is a bijection, the maximum value of $h(x_0)$ over all feasible flows $h$ in $(V, D)$ equals the maximum value of $\bar{h}(e_0)$ over all feasible flows $\bar{h}$ in $(X, k)$. Hence

$$\max\{h(x_0): h \text{ is a feasible flow in } (V, D)\} = \max\{\bar{h}(e_0): \bar{h} \text{ is a feasible flow in } (X, k)\}.$$

This equality completes the reduction of the vertex form of the Max-Flow–Min-Cut Theorem to the classical edge-capacitated form C6.
