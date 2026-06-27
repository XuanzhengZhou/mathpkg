---
role: proof
locale: en
of_concept: cluster-point-closure-characterization
source_book: gtm027
source_chapter: "2"
source_section: "Sequences and Subsequences"
---

# Proof of Cluster Point Characterization via Closure of Tail Sets

**Theorem 7.** Let $\{S_n, n \in D\}$ be a net in a topological space and for each $n$ in $D$ let $A_n$ be the set of all points $S_m$ for $m > n$. Then $s$ is a cluster point of $\{S_n, n \in D\}$ if and only if $s$ belongs to the closure of $A_n$ for each $n$ in $D$.

*Proof.* If $s$ is a cluster point of $\{S_n, n \in D\}$, then for each $n$, $A_n$ intersects each neighborhood of $s$ because $\{S_n, n \in D\}$ is frequently in each neighborhood. Therefore $s$ is in the closure of each $A_n$.

Conversely, if $s$ is not a cluster point of $\{S_n, n \in D\}$ there is a neighborhood $U$ of $s$ such that $\{S_n, n \in D\}$ is not frequently in $U$. Hence for some $n$ in $D$, if $m \geq n$, then $S_m \notin U$, so that $U$ and $A_n$ are disjoint. Consequently $s$ is not in the closure of $A_n$.

Thus $s$ is a cluster point if and only if $s \in \overline{A_n}$ for every $n \in D$. $\square$
