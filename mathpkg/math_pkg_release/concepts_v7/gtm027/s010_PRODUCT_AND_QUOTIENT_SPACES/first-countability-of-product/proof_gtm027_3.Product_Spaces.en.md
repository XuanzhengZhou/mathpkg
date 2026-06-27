---
role: proof
locale: en
of_concept: first-countability-of-product
source_book: gtm027
source_chapter: "3"
source_section: "Product Spaces"
---

# Proof of First Countability of Product Spaces

**Theorem.** The product space $\bigwedge\{X_a : a \in A\}$ satisfies the first axiom of countability if and only if each coordinate space $X_a$ satisfies the first axiom of countability and all but countably many of the coordinate spaces are indiscrete.

*Proof.* ($\Leftarrow$) Suppose that $B$ is a countable subset of $A$, that $X_a$ is indiscrete for $a \in A \sim B$, and that each $X_a$ satisfies the first axiom of countability. Let $x$ be a point in the product space. For each $a \in B$ choose a countable base $\mathcal{U}_a$ for the neighborhood system of $x_a$ in $X_a$. For $a \in A \sim B$, the only neighborhood of $x_a$ is $X_a$ itself (the space is indiscrete), so set $\mathcal{U}_a = \{X_a\}$.

Consider the family of all finite intersections of sets of the form $P_a^{-1}[U]$ for $a \in A$ and $U \in \mathcal{U}_a$. This family is countable because for $a \in A \sim B$, $P_a^{-1}[X_a] = \bigwedge\{X_b : b \in A\}$ (the whole product space), which contributes nothing beyond the empty intersection. The remaining generating sets come from the countable family of pairs $(a, U)$ with $a \in B$ and $U \in \mathcal{U}_a$ (a countable set). The finite intersections of a countable family form a countable family. This family is a base for the neighborhood system of $x$, and consequently the product space satisfies the first axiom of countability.

($\Rightarrow$) To prove the converse, suppose that $B$ is an uncountable subset of $A$ such that for each $a \in B$ there is a neighborhood of $x_a$ in $X_a$ which is a proper subset of $X_a$ (i.e., the coordinate space is not indiscrete at $x_a$). Assume, for contradiction, that there is a countable local base $\mathcal{U}$ for the neighborhood system of $x$.

Each member $U$ of $\mathcal{U}$ contains a member of the defining base for the product topology, and consequently, except for a finite number of members $a$ of $A$, $P_a[U] = X_a$. Since $B$ is uncountable and each $U \in \mathcal{U}$ fails to project onto the full $X_a$ for only finitely many coordinates, the countable union over $\mathcal{U}$ of these finite exceptional sets is still countable. Thus there exists a member $a \in B$ such that $P_a[U] = X_a$ for every $U \in \mathcal{U}$.

But by hypothesis, for this $a$ there is an open neighborhood $V$ of $x_a$ which is a proper subset of $X_a$. Clearly no member of $\mathcal{U}$ is a subset of $P_a^{-1}[V]$, since each member of $\mathcal{U}$ projects onto the entirety of $X_a$. This contradicts the assumption that $\mathcal{U}$ is a local base at $x$. Therefore, at most countably many coordinate spaces can fail to be indiscrete.

Each individual coordinate space inherits first countability from the product (one may embed $X_a$ as a slice in the product, and the first axiom of countability is hereditary for subspaces). $\square$
