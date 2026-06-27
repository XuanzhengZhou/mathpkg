---
role: proof
locale: en
of_concept: colimit-iff-left-kan-extension
source_book: gtm005
source_chapter: "X"
source_section: "7"
---

A functor $S: \mathbf{1} \to A$ is just an object $a \in A$, and a natural transformation $\alpha: T \to SK_1$, for $K_1: M \to \mathbf{1}$, is just a cone with base $T$ and vertex $a$. Since the left Kan extension $L = \operatorname{Lan}_{K_1} T$ is constructed to provide the universal natural transformation $\eta: T \to LK_1$, it also provides the universal cone with base $T$, and hence the colimit of $T$.

The dual statement for limits follows by applying the same argument to the opposite categories.
