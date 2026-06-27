---
role: proof
locale: en
of_concept: dcc-ring-is-direct-sum-of-noetherian-primary-rings
source_book: gtm028
source_chapter: "IV"
source_section: "§2. Rings with descending chain condition"
---

By Theorem 2, $(0)$ is a power product $\mathfrak{P}_1^{k(1)} \cdots \mathfrak{P}_n^{k(n)}$ of maximal ideals $\mathfrak{P}_i$ which may be assumed distinct. For $i \neq j$, the ideals $\mathfrak{P}_i^{k(i)}$ and $\mathfrak{P}_j^{k(j)}$ are comaximal (their sum is $R$) by Theorem 31 of III, §13, and this theorem also shows that
$$(0) = \mathfrak{P}_1^{k(1)} \cap \mathfrak{P}_2^{k(2)} \cap \cdots \cap \mathfrak{P}_n^{k(n)}.$$

Define $R_i = \bigcap_{j \neq i} \mathfrak{P}_j^{k(j)}$. By Theorem 32 of III, §13, $R$ is the direct sum of the ideals $R_i$ ($1 \leq i \leq n$).

Any prime ideal $\mathfrak{P}$ in $R$ contains $(0) = \bigcap \mathfrak{P}_i^{k(i)}$, hence contains some $\mathfrak{P}_i$, so $\mathfrak{P} = \mathfrak{P}_i$. Thus $R$ has only finitely many prime ideals.

This last fact is also immediate from the d.c.c.: if $\{\mathfrak{B}_i\}$ were an infinite sequence of distinct prime ideals, the products $\mathfrak{A}_i = \mathfrak{B}_1 \cdots \mathfrak{B}_i$ would form a strictly decreasing sequence. Its stabilization at some $n$ would give $\mathfrak{B}_1 \cdots \mathfrak{B}_n = \mathfrak{B}_1 \cdots \mathfrak{B}_n \mathfrak{B}_{n+1}$, implying $\mathfrak{B}_{n+1}$ contains some $\mathfrak{B}_i$ with $i \leq n$, contradicting that all prime ideals are maximal.
