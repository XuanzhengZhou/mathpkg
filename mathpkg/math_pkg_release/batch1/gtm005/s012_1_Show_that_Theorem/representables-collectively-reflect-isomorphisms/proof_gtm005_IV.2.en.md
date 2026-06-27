---
role: proof
locale: en
of_concept: representables-collectively-reflect-isomorphisms
source_book: gtm005
source_chapter: "IV"
source_section: "2"
---

In any category $C$, $f: a \to b$ is an isomorphism iff $C(x, f): C(x, a) \to C(x, b)$ is bijective for all $x \in C$.

($\Rightarrow$) If $f$ has inverse $f^{-1}$, then $g \mapsto f^{-1} \circ g$ is inverse to $g \mapsto f \circ g$, so $C(x, f)$ is bijective.

($\Leftarrow$) Take $x = b$. Since $C(b, f): C(b, a) \to C(b, b)$ is surjective, there exists $g: b \to a$ with $f \circ g = 1_b$. Now take $x = a$: $C(a, f)(g \circ f) = f \circ g \circ f = f = C(a, f)(1_a)$. Since $C(a, f)$ is injective, $g \circ f = 1_a$. Hence $g = f^{-1}$.

This is a corollary of the Yoneda Lemma: the Yoneda embedding is fully faithful and reflects isomorphisms.
