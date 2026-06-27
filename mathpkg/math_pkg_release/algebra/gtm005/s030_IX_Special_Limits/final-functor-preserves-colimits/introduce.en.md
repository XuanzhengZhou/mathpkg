---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This theorem states that precomposition with a final functor does not change the colimit. In other words, if $L : J' \to J$ is final, then for any diagram $F : J \to X$, the colimit of $F$ can be computed equally well from the restriction $F \circ L$. The canonical comparison map $h : \varinjlim (F \circ L) \to \varinjlim F$ is always an isomorphism. The proof constructs the inverse by showing that the colimiting cone for $F \circ L$ extends uniquely to $F$, using the finality condition to verify that any cone over $F \circ L$ determines a cone over $F$. The converse also holds: if the canonical map is an isomorphism for all $F$, then $L$ must be final.
