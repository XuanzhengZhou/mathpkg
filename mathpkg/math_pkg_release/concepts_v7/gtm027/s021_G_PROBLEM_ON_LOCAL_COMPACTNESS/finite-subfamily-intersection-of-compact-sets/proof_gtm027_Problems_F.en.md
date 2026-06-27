---
role: proof
locale: en
of_concept: finite-subfamily-intersection-of-compact-sets
source_book: gtm027
source_chapter: "Problems"
source_section: "F"
---

# Proof of Finite Subfamily Intersection Lemma for Closed Compact Sets

**Lemma.** Let $\alpha$ be a family of closed compact sets in a topological space $X$ such that $\bigcap \{A : A \in \alpha\}$ is a subset of an open set $U$. Then there exists a finite subfamily $F \subset \alpha$ such that $\bigcap \{A : A \in F\} \subset U$.

**Proof.**

Let $C = \bigcap \{A : A \in \alpha\}$. By hypothesis, $C \subset U$ where $U$ is open. Fix any $A_0 \in \alpha$. Consider the family $\{A_0 \setminus U\} \cup \{A_0 \cap A : A \in \alpha\}$.

Since each $A \in \alpha$ is closed, each $A_0 \cap A$ is closed in the subspace $A_0$. We claim that
\[
\bigcap_{A \in \alpha} (A_0 \cap A) \cap (A_0 \setminus U) = (A_0 \cap C) \setminus U = \varnothing,
\]
because $C \subset U$. Thus the family of closed subsets $\{A_0 \setminus U\} \cup \{A_0 \cap A : A \in \alpha\}$ of the compact space $A_0$ has empty intersection.

By the finite intersection property characterization of compactness, there exists a finite subfamily with empty intersection. Hence there exist $A_1, \ldots, A_n \in \alpha$ such that
\[
(A_0 \setminus U) \cap \bigcap_{i=1}^n (A_0 \cap A_i) = \varnothing.
\]

This is equivalent to
\[
A_0 \cap \bigcap_{i=1}^n A_i \subset U.
\]

Now set $F = \{A_0, A_1, \ldots, A_n\}$. Since $\bigcap \{A : A \in F\} \subset A_0 \cap \bigcap_{i=1}^n A_i \subset U$, the conclusion follows.
