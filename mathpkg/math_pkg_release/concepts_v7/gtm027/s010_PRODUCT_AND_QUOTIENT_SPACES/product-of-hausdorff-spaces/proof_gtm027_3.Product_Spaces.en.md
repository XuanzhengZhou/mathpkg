---
role: proof
locale: en
of_concept: product-of-hausdorff-spaces
source_book: gtm027
source_chapter: "3"
source_section: "Product Spaces"
---

# Proof of Product of Hausdorff Spaces

**Theorem.** The product of Hausdorff spaces is a Hausdorff space.

*Proof.* If $x$ and $y$ are distinct members of the product $\bigwedge\{X_a : a \in A\}$, then $x_a \neq y_a$ for some $a$ in $A$. Since each coordinate space $X_a$ is Hausdorff, there are disjoint open neighborhoods $U$ and $V$ of $x_a$ and $y_a$ respectively in $X_a$.

The preimages $P_a^{-1}[U]$ and $P_a^{-1}[V]$ are open in the product topology (they belong to the defining subbase) and contain $x$ and $y$ respectively. Moreover, they are disjoint because $U$ and $V$ are disjoint and the projection $P_a$ is a function. Thus $P_a^{-1}[U]$ and $P_a^{-1}[V]$ are disjoint open neighborhoods of $x$ and $y$ in the product space. Hence the product is Hausdorff. $\square$
