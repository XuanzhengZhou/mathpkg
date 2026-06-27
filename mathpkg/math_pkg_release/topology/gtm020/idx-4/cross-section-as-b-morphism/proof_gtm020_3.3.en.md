---
role: proof
locale: en
of_concept: cross-section-as-b-morphism
source_book: gtm020
source_chapter: "3"
source_section: "3.3"
---

Let $s: B \to E$ be a cross section of $(E, p, B)$. This means $s$ is a continuous map such that $p \circ s = 1_B$. Consider the trivial identity bundle $(B, 1_B, B)$ where the total space and base space are both $B$ and the projection is the identity $1_B$. Define the bundle morphism $(s, 1_B): (B, 1_B, B) \to (E, p, B)$. We need to verify that $p \circ s = 1_B \circ 1_B$, which holds because $p \circ s(b) = b = 1_B(1_B(b))$ for all $b \in B$. Thus $(s, 1_B)$ is a $B$-morphism. Conversely, if $(u, 1_B): (B, 1_B, B) \to (E, p, B)$ is a $B$-morphism, then $p \circ u = 1_B \circ 1_B = 1_B$, so $u$ is a cross section of $(E, p, B)$. Therefore the cross sections correspond bijectively to $B$-morphisms from $(B, 1_B, B)$ to $(E, p, B)$.
