---
role: proof
locale: en
of_concept: association-scheme-triple-product-symmetry
source_book: gtm054
source_chapter: "IX"
source_section: "E"
---

**Proof.** Let $x \in V$ be fixed. Consider the set of ordered triples $(x, y, z) \in V^3$ such that $\{x, y\} \in Q_i$, $\{y, z\} \in Q_j$, and $\{z, x\} \in Q_k$. We count the number of such triples in three different ways.

First, fix $x$ and count pairs $(y, z)$. There are $n_i$ choices for $y$ (the $i$th-associates of $x$). For each such $y$, the definition of $p_{jk}^i$ gives exactly $p_{jk}^i$ choices for $z$ such that $z$ is a $j$th-associate of $y$ and a $k$th-associate of $x$. Thus the first count yields $n_i p_{jk}^i$ triples.

Second, count by fixing $x$ and first choosing $z$. There are $n_k$ choices for $z$ (the $k$th-associates of $x$). For each such $z$, there are $p_{ij}^k$ choices for $y$ such that $y$ is an $i$th-associate of $x$ and a $j$th-associate of $z$. This gives $n_k p_{ij}^k$ triples.

Third, count by fixing $x$ and first choosing $y$ in a different order [or by symmetry in the roles of the three vertices], yielding $n_j p_{ki}^j$.

Since all three counting methods enumerate the same set of triples, we obtain

$$n_i p_{jk}^i = n_j p_{ki}^j = n_k p_{ij}^k.$$
