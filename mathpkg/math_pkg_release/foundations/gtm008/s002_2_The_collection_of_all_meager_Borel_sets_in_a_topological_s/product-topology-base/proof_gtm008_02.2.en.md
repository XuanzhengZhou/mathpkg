---
role: proof
locale: en
of_concept: product-topology-base
source_book: gtm008
source_chapter: "Chapter 2: Topological Spaces"
source_section: "2. The Collection of All Meager Borel Sets in a Topological Space"
---

If $A \neq 0$, then there exists $b \in A$. If $f \in \prod_{a \in A} X_a$, then $f(b) \in X_b$, so there exists a neighborhood $N(f(b)) \in T_b$. Then
$$f \in \left\{ g \in \prod_{a \in A} X_a \mid g(b) \in N(f(b)) \right\} \in T'.$$
Thus every point of the product is covered by an element of $T'$.

If $B_1, B_2 \in T'$, then $B_1 \cap B_2 \in T'$: the finite set of restricted coordinates for the intersection is the union of the finite sets of restricted coordinates for $B_1$ and $B_2$, and on each coordinate the intersection of two open sets is open.

Therefore by Theorem 1.18, $T'$ is a base for a topology on $\prod_{a \in A} X_a$.
