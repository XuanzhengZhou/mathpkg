---
role: proof
locale: en
of_concept: max-flow-min-cut-doubly-capacitated
source_book: gtm054
source_chapter: "IV"
source_section: "IVG"
---

The proof of Theorem C6 may be adapted to prove this result with the following modest changes. First, replace $k$ by $k_2$ throughout. Second, alter the third condition in the definition of "unsaturated path" to read:

$$e_i = (x_i, x_{i-1}) \Rightarrow h(e_i) > k_1(e_i).$$

This modification ensures that flow can be decreased along backward edges only down to the lower capacity bound $k_1(e_i)$, rather than down to $0$ as in the standard case. The existence of a feasible flow guarantees that the iterative augmentation process is well-founded, and the argument proceeds as in the classical max-flow min-cut theorem to establish both the existence of a maximum flow and the equality with the minimum cut capacity.
