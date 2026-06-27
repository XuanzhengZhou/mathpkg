---
role: proof
locale: en
of_concept: set-system-distinguishes-vertices-d5-d5
source_book: gtm054
source_chapter: "5"
source_section: "IVE"
---

Let $h_0 = h$, and let $h_i$ be the feasible flow obtained in the $i$th iteration of Step 3 of the Flow Algorithm. By the definition of $h_i$, $h_i(e_0) = h_{i-1}(e_0) + 1$ for $i \geq 1$. Thus $h_i(e_0) = h(e_0) + i$. Since $h_i$ is feasible, $k(e_0) \geq h_i(e_0)$ for all $i$, and so the maximum number of iterations possible is $k(e_0) - h(e_0)$.

Evidently the efficiency of the Flow Algorithm depends upon the efficiency of the search technique used in implementing Step 2. There is a search technique implicit in the proof of the Max-Flow–Min-Cut Theorem; it is the one most often associated with the Flow Algorithm in the literature. This section concludes with a description of this search technique.

Let $(V, k)$ be an integral network, $e_0 = (y_0, x_0) \in W$, and $h$ an integral

x₀y₀-path (with respect to h, henceforth being understood) or to show that such a path cannot exist. For i = 0, 1, 2, ..., let
