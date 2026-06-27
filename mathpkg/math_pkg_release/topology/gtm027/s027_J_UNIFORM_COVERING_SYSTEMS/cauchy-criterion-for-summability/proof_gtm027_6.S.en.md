---
role: proof
locale: en
of_concept: cauchy-criterion-for-summability
source_book: gtm027
source_chapter: "6"
source_section: "S"
---

# Proof of the Cauchy Criterion for Summability

Let $f: A \to G$ be a function into a complete abelian Hausdorff topological group $G$. Let $\alpha$ be the family of finite subsets of $A$, directed by $\supset$ (reverse inclusion). Define $S_F = \sum_{a \in F} f(a)$ for $F \in \alpha$. The net $\{S_F, F \in \alpha, \supset\}$ is the net of partial sums.

$f$ is *summable* over $A$ iff this net converges.

Since $G$ is complete, the net converges iff it is Cauchy. The Cauchy condition for this net reads: for each neighborhood $U$ of $0$, there exists a finite $B \subset A$ such that for all finite $F_1, F_2 \supset B$ (i.e., $F_1, F_2 \subset B$), we have $S_{F_1} - S_{F_2} \in U$.

Equivalently: for each $U$, there exists finite $B \subset A$ such that for every finite $C \subset A \setminus B$, $\sum_{c \in C} f(c) \in U$. (Take $F_1 = B \cup C$, $F_2 = B$.)

This is precisely the Cauchy criterion stated.

**Consequence:** If $f$ is summable over $A$, then for any subset $A' \subset A$, the restriction $f|_{A'}$ is summable over $A'$. This follows because the Cauchy condition for $A$ implies the same condition for any subset.
