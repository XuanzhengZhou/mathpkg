---
role: proof
locale: en
of_concept: product-as-limit-of-discrete-diagram
source_book: gtm026
source_chapter: "1"
source_section: "1.20"
---

Let $\Delta$ be the diagram scheme with $N(\Delta) = I$ and $\Delta(i, j) = \emptyset$ for all $i, j \in I$. A diagram $(\Delta, D)$ consists of an object $D_i$ for each $i \in I$ with no assigned morphisms (since there are no edges).

A lower bound $(L, \psi)$ of $(\Delta, D)$ assigns to each node $i \in I$ a morphism $\psi_i: L \to D_i$. There are no commutativity conditions because there are no edges. This is exactly the data of a cone over the family $\{D_i\}$.

The universal property of a limit requires that for any other lower bound $(L', \psi')$, there exists a unique $f: L' \to L$ such that $f \circ \psi_i = \psi'_i$ for all $i$. This is precisely the universal property defining the product $\prod_{i \in I} D_i$ with projection maps $\psi_i$. Hence limits of discrete diagrams are products.
