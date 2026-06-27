---
role: proof
locale: en
of_concept: decomposition-into-irreducible-subspaces
source_book: gtm023
source_chapter: "XIII"
source_section: "3"
---

Let
$$E = \sum_{j=1}^{s} F_j \quad \dim F_j > 0$$
be a decomposition of $E$ into stable subspaces such that $s$ is maximized (this is clearly possible, since for all decompositions we have $s \leq \dim E$). Then the spaces $F_i$ are irreducible. In fact, assume that for some $i$,
$$F_i = F_i' \oplus F_i'' \quad \dim F_i' > 0, \dim F_i'' > 0$$
is a decomposition of $F_i$ into stable subspaces. Then
$$E = \sum_{j \neq i} F_j \oplus F_i' \oplus F_i''$$
is a decomposition of $E$ into $(s+1)$ stable subspaces, which contradicts the maximality of $s$.
