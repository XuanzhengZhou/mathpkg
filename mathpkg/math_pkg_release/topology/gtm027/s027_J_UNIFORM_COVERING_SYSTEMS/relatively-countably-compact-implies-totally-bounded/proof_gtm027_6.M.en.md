---
role: proof
locale: en
of_concept: relatively-countably-compact-implies-totally-bounded
source_book: gtm027
source_chapter: "6"
source_section: "M"
---

# Proof that Relatively Countably Compact Implies Totally Bounded

Let $(X, \mathfrak{J})$ be a completely regular space and let $A \subset X$ be relatively countably compact (each sequence in $A$ has a cluster point in $X$).

Let $\mathfrak{U}_{\max}$ be the largest uniformity whose topology is $\mathfrak{J}$. Suppose, for contradiction, that $A$ is not totally bounded relative to $\mathfrak{U}_{\max}$.

By part (a), there exists $U \in \mathfrak{U}_{\max}$ and an infinite subset $B = \{x_n : n \in \omega\} \subset A$ such that $U[x_n] \cap U[x_m] = \emptyset$ for $n \neq m$. Since $A$ is relatively countably compact, the sequence $\{x_n\}$ has a cluster point $x \in X$.

Since $U[x]$ is a neighborhood of $x$, it must contain infinitely many terms of the sequence. Thus there exist $n \neq m$ with $x_n, x_m \in U[x]$. But then $x \in U[x_n] \cap U[x_m]$, contradicting that these neighborhoods are disjoint.

Therefore, $A$ is totally bounded relative to $\mathfrak{U}_{\max}$.
