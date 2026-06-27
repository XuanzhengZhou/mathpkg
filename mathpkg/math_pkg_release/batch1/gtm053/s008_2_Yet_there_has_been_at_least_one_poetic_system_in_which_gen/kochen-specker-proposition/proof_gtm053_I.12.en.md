---
role: proof
locale: en
of_concept: kochen-specker-proposition
source_book: gtm053
source_chapter: "I"
source_section: "12"
---

The proof is given in Sections 12.12–12.15 of the book (not fully reproduced in the section text). The proof proceeds by explicitly constructing a finite set $\Gamma \subset S^2$ of 117 points and showing that no mapping $k: \Gamma \to \{0,1\}$ can satisfy the condition that on every orthogonal frame (triple of mutually perpendicular directions in $\Gamma$), $k$ takes the value $1$ on exactly two directions and $0$ on exactly one.

The construction of $\Gamma$ and the combinatorial verification involve the following ideas:

1. **Geometric realization on $S^2$:** The points of $\Gamma$ are chosen as specific directions on the sphere corresponding to vertices of certain regular polytopes or as intersection points of certain great circles.

2. **Coloring argument:** Suppose a coloring $k: \Gamma \to \{0,1\}$ existed satisfying the frame condition. By exploring the logical constraints imposed by overlapping frames (triples of orthogonal directions sharing one or two points), one derives contradictions.

3. **Finite combinatorics:** The set of 117 points and the set of orthogonal triples among them form a hypergraph. The condition that each triple has exactly one 0 means the 0-valued points form a "hitting set" with a specific structure. One shows that no such hitting set exists by exhaustive analysis of the hypergraph.

The key implication: adopting both the quantum-mechanical assertions about spin measurements (Section 12.2) and the hidden-variable hypotheses (Section 12.3) would allow one to define such a mapping

$$S^2 \to \{0,1\}: \alpha \mapsto |s|(\alpha, t; \omega)$$

for fixed $t$ and $\omega$, which would satisfy conditions (a) and (b). Since the Kochen–Specker proposition proves such a mapping cannot exist, the hidden-variable interpretation is impossible. See Kochen and Specker, J. Math. Mech. 17 (1967), 59–87 for the complete construction and proof.
