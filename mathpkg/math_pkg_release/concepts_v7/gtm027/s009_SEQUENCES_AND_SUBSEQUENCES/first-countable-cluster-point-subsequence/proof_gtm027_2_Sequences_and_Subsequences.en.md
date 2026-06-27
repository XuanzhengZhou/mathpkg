---
role: proof
locale: en
of_concept: first-countable-cluster-point-subsequence
source_book: gtm027
source_chapter: "2"
source_section: "Sequences and Subsequences"
---

# Proof of Cluster Points Yield Convergent Subsequences in First Countable Spaces

**Theorem 8(c).** Let $X$ be a topological space satisfying the first axiom of countability. If $s$ is a cluster point of a sequence $S$, then there is a subsequence of $S$ converging to $s$.

*Proof.* Suppose that $s$ is a cluster point of a sequence $S$ and that $V_0, V_1, \cdots$ is a sequence which is a base for the neighborhood system of $s$ such that $V_{n+1} \subset V_n$ for each $n$. (Such a nested base exists by the first countability axiom: take a countable base $U_0, U_1, \cdots$ and set $V_n = \bigcap \{U_i: i = 0, 1, \cdots, n\}$.)

For every non-negative integer $i$, choose $N_i$ such that $N_i \geq i$ and $S_{N_i}$ belongs to $V_i$. Such an $N_i$ exists because $s$ is a cluster point, so $S$ is frequently in each $V_i$. Then $\{S_{N_i}, i \in \omega\}$ is a subsequence of $S$ (since $N_i \geq i$, the indices are strictly increasing after passing to a suitable refinement). This subsequence converges to $s$ because for any neighborhood $U$ of $s$, there exists $k$ with $V_k \subset U$, and then $S_{N_i} \in V_i \subset V_k \subset U$ for all $i \geq k$. $\square$
