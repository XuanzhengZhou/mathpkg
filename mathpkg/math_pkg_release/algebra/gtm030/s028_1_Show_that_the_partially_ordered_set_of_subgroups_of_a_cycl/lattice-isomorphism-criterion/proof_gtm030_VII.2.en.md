---
role: proof
locale: en
of_concept: lattice-isomorphism-criterion
source_book: gtm030
source_chapter: "Chapter VII"
source_section: "2. Lattices"
---

A mapping $a \rightarrow a'$ of a lattice $L$ into a lattice $L'$ is called order preserving if $a \geq b$ implies that $a' \geq b'$.

First, suppose $a \rightarrow a'$ is an isomorphism and $a \geq b$. Then $a \cup b = a$, so by the homomorphism property:
$$a' \cup b' = (a \cup b)' = a'.$$
Thus $a' \geq b'$, showing the isomorphism is order preserving. Evidently the inverse mapping $a' \rightarrow a$ is also order preserving (being an isomorphism itself).

Conversely, suppose $a \rightarrow a'$ is a 1-1 mapping of $L$ onto $L'$ which is order preserving and whose inverse is also order preserving. We must show $(a \cup b)' = a' \cup b'$ and $(a \cap b)' = a' \cap b'$.

Let $d = a \cup b$. Then $d \geq a, b$, so by order preservation $d' \geq a', b'$. Thus $d'$ is an upper bound of $\{a', b'\}$.

Now let $e'$ be any element of $L'$ such that $e' \geq a', b'$, and let $e$ be the (unique) element of $L$ whose image is $e'$ (the map is onto and 1-1). Since the inverse map is order preserving, $e \geq a, b$. Hence $e \geq a \cup b = d$, and by order preservation again $e' \geq d'$.

Thus $d' = a' \cup b'$, i.e., $(a \cup b)' = a' \cup b'$. The dual argument yields $(a \cap b)' = a' \cap b'$. Therefore the mapping is a lattice isomorphism.
