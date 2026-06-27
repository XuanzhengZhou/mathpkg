---
role: proof
locale: en
of_concept: max-flow-min-cut-doubly-capacitated
source_book: gtm054
source_chapter: "IV"
source_section: "G"
---

The proof of Theorem G3 adapts the proof of the singly-capacitated Max-Flow Min-Cut Theorem (C6) with the following changes:

1. Replace the single capacity function $k$ by the upper capacity $k_2$ throughout.

2. Alter the third condition in the definition of an "unsaturated path." In the singly-capacitated case, a path $x_0, e_1, x_1, \ldots, e_m, x_m$ is unsaturated with respect to a flow $h$ if:
   - $e_i = (x_{i-1}, x_i) \Rightarrow h(e_i) < k_2(e_i)$,
   - $e_i = (x_i, x_{i-1}) \Rightarrow h(e_i) > 0$.

   For the doubly-capacitated case, the second condition is replaced by:
   - $e_i = (x_i, x_{i-1}) \Rightarrow h(e_i) > k_1(e_i)$.

   This ensures that the flow can be decreased along reverse edges only down to the lower capacity bound, not down to zero.

3. The existence of a feasible flow guarantees that the initial flow used in the augmenting-path algorithm respects both bounds. Starting from any feasible flow, one repeatedly augments along unsaturated paths (which respect both $k_1$ and $k_2$) until no such path exists.

Once no unsaturated path from the source $x_0^1$ to the sink $x_0^2$ exists, the set $S$ of vertices reachable via unsaturated paths defines a cut $C = \sum_{x \in S} f^*(x)$ through $e_0$. For this cut, every forward edge from $S$ to its complement is saturated ($h(e) = k_2(e)$), and every reverse edge from the complement to $S$ is at the lower bound ($h(e) = k_1(e)$). The equality $h(e_0) = k_2(C; e_0)$ then follows by the same accounting as in C6, and by Proposition G2 no feasible flow can exceed this value. Hence $h$ is a maximum flow.
