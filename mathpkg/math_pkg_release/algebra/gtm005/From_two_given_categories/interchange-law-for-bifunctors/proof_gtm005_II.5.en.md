---
role: proof
locale: en
of_concept: interchange-law-for-bifunctors
source_book: gtm005
source_chapter: "II"
source_section: "5"
---

For a bifunctor $S: A \times B \to C$ and arrows $f: a \to a'$, $f': a' \to a''$ in $A$, $g: b \to b'$, $g': b' \to b''$ in $B$:
$$S(f' \circ f, g' \circ g) = S(f', g') \circ S(f, g).$$

Proof: $S(f', g') \circ S(f, g) = S(f', 1) \circ S(1, g') \circ S(f, 1) \circ S(1, g)$. By bifunctoriality, $S(1, g') \circ S(f, 1) = S(f, 1) \circ S(1, g')$ (they are equal to $S(f, g')$). Hence
$$S(f', 1) \circ S(f, 1) \circ S(1, g') \circ S(1, g) = S(f' \circ f, 1) \circ S(1, g' \circ g) = S(f' \circ f, g' \circ g).$$
The key step $S(1, g') \circ S(f, 1) = S(f, 1) \circ S(1, g')$ follows because both decompose $S(f, g')$: $S(f, g') = S(f \circ 1, 1 \circ g') = S(f, 1) \circ S(1, g') = S(1 \circ f, g' \circ 1) = S(1, g') \circ S(f, 1)$.
