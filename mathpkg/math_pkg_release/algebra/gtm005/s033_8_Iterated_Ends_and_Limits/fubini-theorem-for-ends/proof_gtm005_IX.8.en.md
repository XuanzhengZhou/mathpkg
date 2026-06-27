---
role: proof
locale: en
of_concept: fubini-theorem-for-ends
source_book: gtm005
source_chapter: "IX"
source_section: "8"
---

For $S: A^{\mathrm{op}} \times A \times B^{\mathrm{op}} \times B \to X$,
$$\int_a \int_b S(a, a, b, b) \cong \int_b \int_a S(a, a, b, b) \cong \int_{(a, b)} S(a, a, b, b),$$
provided the ends exist.

Proof: An end $\int_{(a,b)} S(a, a, b, b)$ is a universal wedge with components indexed by $(a, b)$. By the universal property of iterated limits/ends, first fixing $b$ and taking the end over $a$, then taking the end over $b$, yields the same universal object (and similarly for the other order).

Formally, universal wedges are in bijection:
$$\operatorname{Wedge}\left(x, \int_a S(a, a, -, -)\right) \cong \operatorname{Wedge}(x, S) \cong \operatorname{Wedge}\left(x, \int_b S(-, -, b, b)\right).$$
The Yoneda Lemma then gives the isomorphism of the ends.
