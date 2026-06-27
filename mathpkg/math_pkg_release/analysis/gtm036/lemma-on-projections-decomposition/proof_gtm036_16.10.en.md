---
role: proof
locale: en
of_concept: lemma-on-projections-decomposition
source_book: gtm036
source_chapter: "16"
source_section: "16.10"
---

To prove (i), observe that if $f \in \times \{B_t^\circ: t \in A\}$ and $x$ belongs to $B_t$, then $| \langle x, f \rangle | = | \langle x(t), f(t) \rangle |$, which is at most one because $f(t) \in B_t^\circ$. On the other hand, if $f$ belongs to the polar of the union of the sets $B_t$, then for each $t$ and each $x$ in $B_t$, $| \langle x(t), f(t) \rangle | = | \langle x, f \rangle | \leq 1$; hence, $f(t) \in B_t^\circ$.

To prove (ii), note that if $x \in (C_t)_0$, then $| \langle x, f \rangle | = | \langle x(t), f(t) \rangle | \leq 1$ for each $f$ in the product $\times \{C_t: t \in A\}$; hence $x$ belongs to the polar. The inclusion in $aB$ for $a > 1$ follows from the bipolar theorem.
