---
role: proof
locale: en
of_concept: countable-closure-preserves-ordinal-sequences
source_book: gtm008
source_chapter: "12"
source_section: "12. The Independence of the AC"
---

Let $M \models D_{M[G]}(t)$ be an $\omega$-sequence of ordinals in $M[G]$. By Theorem 10.9, it suffices to show that the set
$$\{p \in P \mid p \models V(t)\}$$
is dense below any given condition, i.e.,
$$(orall p \in P)(\exists q \leq p)\,[q \models V(t)].$$

Given $p \in P$, we construct a descending sequence $\{p_n\}_{n \in \omega}$ by recursion. Since $t$ is a term for an $\omega$-sequence, for each $n$ there exists a dense set $D_n \in M$ of conditions that decide the $n$-th value of $t$. Using the countable closure property (every countable compatible subset has a lower bound), we can find, working in $M$, a decreasing sequence $p = p_0 \geq p_1 \geq p_2 \geq \cdots$ such that each $p_n$ decides the first $n$ values of $t$.

The set $\{p_n\}_{n \in \omega}$ is countable and compatible (since it is a descending chain), so by hypothesis there exists $q \in P$ with $q \leq p_n$ for all $n$. Then $q$ decides all values of $t$, so $q \models V(t)$, establishing the density claim.

By genericity, $G$ meets this dense set, so there exists $q \in G$ with $q \models V(t)$. The $\omega$-sequence determined by $q$ is then definable in $M$, so the sequence lies in $M$.
