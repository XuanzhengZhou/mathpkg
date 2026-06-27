---
role: proof
locale: en
of_concept: first-countable-accumulation-point
source_book: gtm027
source_chapter: "2"
source_section: "Sequences and Subsequences"
---

# Proof of Accumulation Points via Sequences in First Countable Spaces

**Theorem 8(a).** Let $X$ be a topological space satisfying the first axiom of countability. Then a point $s$ is an accumulation point of a subset $A$ of $X$ if and only if there is a sequence in $A \sim \{s\}$ converging to $s$.

*Proof.* Suppose that $s$ is an accumulation point of a subset $A$ of $X$, and that $U_0, U_1, \cdots, U_n, \cdots$ is a sequence which is a base for the neighborhood system of $s$. Let $V_n = \bigcap \{U_i: i = 0, 1, \cdots, n\}$. Then the sequence $V_0, V_1, \cdots, V_n, \cdots$ is also a base for the neighborhood system of $s$ and, moreover, $V_{n+1} \subset V_n$ for each $n$. For each $n$ select a point $S_n$ from $V_n \cap (A \sim \{s\})$, thus obtaining a sequence $\{S_n, n \in \omega\}$ which evidently converges to $s$. This establishes the forward direction.

The converse is obvious: if there is a sequence in $A \sim \{s\}$ converging to $s$, then every neighborhood of $s$ contains infinitely many points of $A$ distinct from $s$, so $s$ is an accumulation point of $A$. $\square$
