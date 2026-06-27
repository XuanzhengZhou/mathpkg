---
role: proof
locale: en
of_concept: nowhere-dense-to-nullset-homeomorphism
source_book: gtm002
source_chapter: "13"
source_section: "13. Transforming Linear Sets into Nullsets"
---

Let $G = I - F$. Since $F$ is closed and nowhere dense, $G$ is a dense open subset of $I$. Define $h(x) = m([0, x] \cap G) / m(G)$. Since $G$ is open, $x \mapsto m([0, x] \cap G)$ is strictly increasing and continuous. Since $G$ is dense, $m(G) = m(I) = 1$. Thus $h: I \to I$ is a strictly increasing continuous bijection, hence a homeomorphism of $I$ onto itself.

The set $G$ is a countable union of disjoint open intervals. Under $h$, each component interval $(a,b)$ of $G$ is mapped onto the interval $(h(a), h(b))$ of length $m((a,b))/m(G) = (b-a)/1 = b-a$. The sum of lengths of these image intervals equals $m(G) = 1$. Hence $h(F) = I - h(G)$ is a closed set whose complement has full measure, so $h(F)$ is a nullset.
