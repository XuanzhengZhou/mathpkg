---
role: proof
locale: en
of_concept: intersection-of-compact-connected-sets
source_book: gtm027
source_chapter: "Problems"
source_section: "F"
---

# Proof of Intersection of Compact Connected Sets

**Theorem.** Let $X$ be a Hausdorff space and let $\alpha$ be a family of compact subsets of $X$ such that every finite intersection of members of $\alpha$ is connected. Then $\bigcap \{A : A \in \alpha\}$ is connected.

**Proof.** Suppose, for contradiction, that $C = \bigcap \{A : A \in \alpha\}$ is not connected. Then there exist disjoint relatively open subsets $V$ and $W$ of $C$ such that $C = V \cup W$, with $V \neq \varnothing$ and $W \neq \varnothing$.

Since $X$ is Hausdorff and each $A \in \alpha$ is compact (hence closed), the sets in $\alpha$ are closed in $X$. The sets $V$ and $W$ are closed in the subspace $C$; since $C$ is an intersection of closed sets, $C$ is closed, so $V$ and $W$ are closed in $X$. Moreover, compact subsets of a Hausdorff space are closed, so each $A \in \alpha$ is closed.

Being closed subsets of the compact sets $A$, the sets $V$ and $W$ are themselves compact. In a Hausdorff space, disjoint compact sets can be separated by disjoint open sets: there exist open sets $U_V, U_W \subset X$ such that $V \subset U_V$, $W \subset U_W$, and $U_V \cap U_W = \varnothing$.

Let $U = U_V \cup U_W$. Then $C \subset U$, and $U$ is open. By the finite subfamily intersection lemma (Problem F(a)), there exists a finite subfamily $F = \{A_1, \ldots, A_n\} \subset \alpha$ such that
\[
\bigcap_{i=1}^n A_i \subset U.
\]

By hypothesis, $K = \bigcap_{i=1}^n A_i$ is connected. However, $K \subset U = U_V \cup U_W$, and both $U_V \cap K$ and $U_W \cap K$ are nonempty (since $V \subset K \cap U_V$ and $W \subset K \cap U_W$), with $U_V \cap U_W = \varnothing$. This gives a separation of $K$, contradicting the connectedness of $K$.

Therefore $C$ must be connected.
