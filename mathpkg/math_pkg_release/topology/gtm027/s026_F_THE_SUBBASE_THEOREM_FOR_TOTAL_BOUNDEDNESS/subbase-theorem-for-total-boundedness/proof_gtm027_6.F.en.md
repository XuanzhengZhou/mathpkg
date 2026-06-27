---
role: proof
locale: en
of_concept: subbase-theorem-for-total-boundedness
source_book: gtm027
source_chapter: "6"
source_section: "F"
---

# Proof of Subbase Theorem for Total Boundedness

Let $(X, \mathfrak{u})$ be a uniform space and let $\mathcal{S}$ be a subbase for $\mathfrak{u}$ such that for each $U \in \mathcal{S}$ there exists a finite cover $\{A_1, \dots, A_n\}$ of $X$ with $A_i \times A_i \subset U$ for each $i$.

Recall that a uniformity is *totally bounded* if for every entourage $V \in \mathfrak{u}$, there exists a finite cover $\{B_1, \dots, B_k\}$ of $X$ such that $B_j \times B_j \subset V$ for each $j$.

The family $\mathcal{B}$ of all finite intersections of members of $\mathcal{S}$ forms a base for $\mathfrak{u}$. It therefore suffices to verify the total boundedness condition for members of $\mathcal{B}$, since any $W \in \mathfrak{u}$ contains some $B \in \mathcal{B}$, and a cover satisfying $B_j \times B_j \subset B$ also satisfies $B_j \times B_j \subset W$.

Let $V = U_1 \cap U_2 \cap \cdots \cap U_m \in \mathcal{B}$ with each $U_k \in \mathcal{S}$. For each $k = 1, \dots, m$, by hypothesis there exists a finite cover $\mathcal{A}_k = \{A_{k,1}, \dots, A_{k,n_k}\}$ of $X$ such that $A_{k,i} \times A_{k,i} \subset U_k$ for all $i$.

Consider the family of all intersections of the form
$$
C_{(i_1, \dots, i_m)} = \bigcap_{k=1}^{m} A_{k, i_k}
$$
where $i_k$ ranges over $\{1, \dots, n_k\}$. This is a finite family (there are at most $n_1 n_2 \cdots n_m$ such sets), and it forms a cover of $X$ because each $x \in X$ belongs to some $A_{k, i_k}$ for each $k$.

For any such intersection $C = \bigcap_{k=1}^{m} A_{k, i_k}$, we have
$$
C \times C \subset \bigcap_{k=1}^{m} (A_{k, i_k} \times A_{k, i_k}) \subset \bigcap_{k=1}^{m} U_k = V.
$$

Thus we have produced a finite cover of $X$ by sets whose squares are contained in $V$. Therefore $(X, \mathfrak{u})$ is totally bounded. $\square$
