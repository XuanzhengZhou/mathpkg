---
role: proof
locale: en
of_concept: shrinking-lemma-for-point-finite-covers
source_book: gtm027
source_chapter: "5"
source_section: "V. Point Finite Covers and Metacompact Spaces"
---

# Proof of Shrinking Lemma for Point Finite Open Covers

Let $U$ be a point finite open cover of a normal space $X$. We construct a family of open sets $G(U)$ for each $U$ in $U$ such that $\overline{G(U)} \subset U$ and $\{G(U) : U \in U\}$ covers $X$.

Consider the class $\mathcal{F}$ of all functions $F$ satisfying:
1. The domain of $F$ is a subfamily of $U$.
2. For each $U$ in the domain of $F$, $F(U)$ is an open set with $\overline{F(U)} \subset U$.
3. $\bigcup \{F(U) : U \in \text{domain } F\} \cup \bigcup \{V : V \in U \text{ and } V \notin \text{domain } F\} = X$.

Partially order $\mathcal{F}$ by inclusion of functions (i.e., $F_1 \leq F_2$ if the domain of $F_1$ is contained in the domain of $F_2$ and $F_1(U) = F_2(U)$ for all $U$ in the domain of $F_1$). Every chain in $\mathcal{F}$ has an upper bound (the union of the functions in the chain), so by Zorn's Lemma there exists a maximal element $F^*$ in $\mathcal{F}$.

We claim the domain of $F^*$ is all of $U$. Suppose not; then there exists $U_0 \in U$ not in the domain of $F^*$. Let

$$T = X \setminus \left( \bigcup \{F^*(U) : U \in \text{domain } F^*\} \cup \bigcup \{V : V \in U \text{ and } V \notin \text{domain } F^*\} \setminus \{U_0\} \right).$$

Then $T$ is a closed subset of $U_0$ (by normality and point finiteness). Since $X$ is normal, there exists an open set $W$ with $T \subset W \subset \overline{W} \subset U_0$. Extending $F^*$ by setting $F^*(U_0) = W$ would contradict maximality. Hence the domain of $F^*$ is $U$, and the collection $\{G(U) = F^*(U) : U \in U\}$ satisfies the required properties.

The point finiteness of $U$ is essential: it ensures that each point $x \in X$ belongs to only finitely many members of $U$, which guarantees that the maximal function $F^*$ can be extended to all of $U$ using the normality of $X$.
