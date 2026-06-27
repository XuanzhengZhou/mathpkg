---
role: proof
locale: en
of_concept: bounded-formula-absoluteness
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

Take $B'$ to be the two-element Boolean algebra $2$ in Theorem 13.18. Since any complete Boolean algebra $B$ contains $2 = \{0, 1\}$ as a complete subalgebra, we can apply Theorem 13.18 with $2$ as the subalgebra and $B$ as the larger algebra (or vice versa, which simply gives the equality of truth values).

Specifically, by Theorem 13.18 with the complete subalgebra $2 \subseteq B$:
$$[\![\phi(\check{u}_1, \ldots, \check{u}_n)]\!]^{(2)} = [\![\phi(\check{u}_1, \ldots, \check{u}_n)]\!]^{(B)}.$$

Now $V^{(2)}$ is essentially isomorphic to $V$ via the mapping $v \mapsto \check{v}$ (by Theorem 13.17 part 3). For a bounded formula $\phi$, the truth value in $V^{(2)}$ is either $0$ or $1$, and:
$$[\![\phi(\check{u}_1, \ldots, \check{u}_n)]\!]^{(2)} = 1 \iff \phi(u_1, \ldots, u_n) \text{ holds in } V.$$

Therefore:
$$\phi(u_1, \ldots, u_n) \leftrightarrow [\![\phi(\check{u}_1, \ldots, \check{u}_n)]\!]^{(B)} = 1.$$
