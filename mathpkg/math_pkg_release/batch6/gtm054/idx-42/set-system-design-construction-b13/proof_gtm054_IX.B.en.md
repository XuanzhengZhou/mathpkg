---
role: proof
locale: en
of_concept: set-system-design-construction-b13
source_book: gtm054
source_chapter: "IX"
source_section: "B"
---
If $t_1, \ldots, t_p$ are consecutive, we refer to B12. Otherwise, the integers $t_1, \ldots, t_p$ can be represented as

$$t_1, t_2, t_2 + 1, \ldots, t_2 + (p - 2) = t_p, \text{ where } t_1 < t_2 - 1.$$

In this case one constructs a set system by a modification of the construction in B12, taking care to handle the gap between $t_1$ and $t_2$ appropriately. The construction ensures that the resulting system is a $(t;)$-design exactly for $t \in \{t_1, \ldots, t_p\}$.
