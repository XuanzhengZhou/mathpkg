---
role: proof
locale: en
of_concept: alexandroff-compactification-theorem
source_book: gtm027
source_chapter: "5"
source_section: "Compactification"
---

# Proof of Alexandroff One-Point Compactification Theorem

**Theorem 21 (Alexandroff).** The one point compactification $X^*$ of a topological space $X$ is compact and $X$ is a subspace. The space $X^*$ is Hausdorff if and only if $X$ is locally compact and Hausdorff.

*Proof.* Recall that $X^* = X \cup \{\infty\}$ with the topology whose members are the open subsets of $X$ and all subsets $U$ of $X^*$ such that $X^* \setminus U$ is a closed compact subset of $X$. Equivalently, a set $U$ is open in $X^*$ iff (a) $U \cap X$ is open in $X$ and (b) whenever $\infty \in U$, then $X \setminus U$ is compact.

*Step 1: $X^*$ is a topological space and $X$ is a subspace.* Finite intersections and arbitrary unions of sets open in $X^*$ intersect $X$ in open sets. If $\infty$ is a member of the intersection of two open subsets of $X^*$, then the complement of the intersection is the union of two closed compact subsets of $X$ and is therefore closed and compact. If $\infty$ belongs to the union of the members of a family of open subsets of $X^*$, then $\infty$ belongs to some member $U$ of the family, and the complement of the union is a closed subset of the compact set $X \setminus U$ and is therefore closed and compact. Consequently $X^*$ is a topological space and $X$ is a subspace.

*Step 2: $X^*$ is compact.* Let $\mathcal{U}$ be an open cover of $X^*$. Then $\infty$ is a member of some $U \in \mathcal{U}$. The complement $X^* \setminus U = X \setminus U$ is compact by definition. Since $\mathcal{U}$ covers $X \setminus U$ as well, there is a finite subfamily of $\mathcal{U}$ covering $X \setminus U$. Together with $U$, this gives a finite subcover of $\mathcal{U}$. Therefore $X^*$ is compact.

*Step 3: If $X^*$ is Hausdorff, then $X$ is locally compact and Hausdorff.* If $X^*$ is a Hausdorff space, then its open subspace $X$ is also Hausdorff. Moreover, for each $x \in X$, there exist disjoint open neighborhoods $V$ of $x$ and $W$ of $\infty$ in $X^*$. Since $\infty \in W$, the complement $X^* \setminus W$ is a closed compact subset of $X$. Then $V \subset X^* \setminus W$, so the closure of $V$ in $X$ is contained in the compact set $X^* \setminus W$, hence $V$ has compact closure. Thus $X$ is locally compact.

*Step 4: If $X$ is locally compact and Hausdorff, then $X^*$ is Hausdorff.* Let $x$ and $y$ be distinct points of $X^*$. If both are in $X$, they can be separated by disjoint open subsets of $X$, which are also open in $X^*$. If one of them, say $y = \infty$, then since $X$ is locally compact and Hausdorff, $x$ has an open neighborhood $V$ in $X$ whose closure $\overline{V}^X$ is compact. Let $U = X^* \setminus \overline{V}^X$. Then $\infty \in U$ and $U$ is open in $X^*$ (since $X \setminus U = \overline{V}^X$ is compact), and $V \cap U = \emptyset$. Hence $X^*$ is Hausdorff. $\square$
