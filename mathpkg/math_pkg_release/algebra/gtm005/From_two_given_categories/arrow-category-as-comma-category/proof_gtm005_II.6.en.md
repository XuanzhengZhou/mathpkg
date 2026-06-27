---
role: proof
locale: en
of_concept: arrow-category-as-comma-category
source_book: gtm005
source_chapter: "II"
source_section: "6"
---

The arrow category $C^{\mathbf{2}}$ is isomorphic to the comma category $(1_C \downarrow 1_C)$. Objects of $C^{\mathbf{2}}$ are arrows $f: a \to b$; objects of $(1_C \downarrow 1_C)$ are triples $(a, f, b)$ with $f: a \to b$. The bijection on objects is clear.

A morphism in $C^{\mathbf{2}}$ from $f: a \to b$ to $f': a' \to b'$ is a commutative square $(h, k)$ where $h: a \to a'$, $k: b \to b'$, and $k \circ f = f' \circ h$.

A morphism in $(1_C \downarrow 1_C)$ from $(a, f, b)$ to $(a', f', b')$ is a pair $(h, k)$ with $h: a \to a'$, $k: b \to b'$ such that $1_C(k) \circ f = f' \circ 1_C(h)$, i.e., $k \circ f = f' \circ h$ — exactly the same condition. Thus the isomorphism extends to morphisms.
