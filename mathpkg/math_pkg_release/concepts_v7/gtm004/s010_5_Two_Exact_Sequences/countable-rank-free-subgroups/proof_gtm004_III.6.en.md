---
role: proof
locale: en
of_concept: countable-rank-free-subgroups
source_book: gtm004
source_chapter: "III"
source_section: "6"
---

# Proof of Lemma 6.2

Let $A$ be an abelian group of countable rank. If every subgroup of $A$ of finite rank is free, then $A$ is free.

**Proof.** By hypothesis there is a maximal countable linearly independent set $T = (a_1, a_2, \ldots, a_n, \ldots)$ of elements of $A$. Let $A_n$ be the subgroup of $A$ consisting of all elements $a \in A$ linearly dependent on $(a_1, a_2, \ldots, a_n)$, i.e., such that $(a_1, a_2, \ldots, a_n, a)$ is linearly dependent. Since $A$ is torsionfree (a subgroup of finite rank being free implies $A$ is torsionfree), $A_0 = 0$.

Plainly $A_{n-1} \subseteq A_n$, and since $T$ is maximal, $A = \bigcup_n A_n$. Since $A_n$ has finite rank $n$, it is free of rank $n$ by hypothesis. Moreover, the inclusion $A_{n-1} \hookrightarrow A_n$ exhibits $A_{n-1}$ as a direct summand of $A_n$ (since finitely generated free abelian groups have the property that pure subgroups are direct summands, and $A_{n-1}$ is pure in $A_n$ in this case).

Thus we may write $A_n = A_{n-1} \oplus F_n$ where $F_n$ is free of rank 1. Iterating, we obtain

$$
A = \bigcup_n A_n = \bigoplus_{n=1}^{\infty} F_n,
$$

which is a free abelian group of countable rank.
