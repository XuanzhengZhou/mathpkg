---
role: proof
locale: en
of_concept: tychonoff-theorem
source_book: gtm027
source_chapter: "5"
source_section: "Products of Compact Spaces"
---

# Proof of Tychonoff Theorem

Let $Q = \prod \{X_a : a \in A\}$ where each $X_a$ is a compact topological space and $Q$ has the product topology. Let $\mathcal{S}$ be the subbase for the product topology consisting of all sets of the form $P_a^{-1}[U]$, where $P_a$ is the projection into the $a$-th coordinate space and $U$ is open in $X_a$. In view of Theorem 5.6 (Alexander subbase theorem), the space $Q$ is compact provided each subfamily $\mathcal{A}$ of $\mathcal{S}$, such that no finite subfamily of $\mathcal{A}$ covers $Q$, fails to cover $Q$.

For each index $a$, let $\mathcal{A}_a$ be the family of all open sets $U$ in $X_a$ such that $P_a^{-1}[U] \in \mathcal{A}$. Then no finite subfamily of $\mathcal{A}_a$ covers $X_a$ (otherwise the corresponding pre-images would form a finite subcover of $\mathcal{A}$). By compactness of $X_a$, there exists a point $x_a \in X_a \setminus \bigcup \mathcal{A}_a$, that is, $x_a \in X_a \sim U$ for each $U \in \mathcal{A}_a$.

Let $x$ be the point whose $a$-th coordinate is $x_a$ for each $a \in A$. For any member $P_a^{-1}[U]$ of $\mathcal{A}$, we have $U \in \mathcal{A}_a$, so $x_a \notin U$, and consequently $x \notin P_a^{-1}[U]$. Thus $x$ does not belong to any member of $\mathcal{A}$. Therefore $\mathcal{A}$ does not cover $Q$.

We have shown that every subfamily of $\mathcal{S}$ with no finite subcover fails to cover $Q$. By the Alexander subbase theorem, $Q$ is compact. $\square$
