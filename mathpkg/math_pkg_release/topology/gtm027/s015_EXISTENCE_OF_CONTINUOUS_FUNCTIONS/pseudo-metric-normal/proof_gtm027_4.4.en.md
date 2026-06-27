---
role: proof
locale: en
of_concept: pseudo-metric-normal
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Every Pseudo-Metric Space is Normal

**Theorem 10.** Each pseudo-metric space is normal.

*Proof.* Let $A$ and $B$ be disjoint closed subsets of a pseudo-metric space $X$, and let $D(A,x)$ and $D(B,x)$ be the distance from $x$ to $A$ and $B$ respectively. By Theorem 8, both functions are continuous. Define

$$U = \{x: D(A,x) - D(B,x) < 0\}, \quad V = \{x: D(A,x) - D(B,x) > 0\}.$$

The function $D(A,x) - D(B,x)$ is continuous in $x$ and therefore $U$ and $V$ are open. Clearly $U$ is disjoint from $V$. If $x \in A$, then $D(A,x) = 0$, and since $A$ and $B$ are disjoint closed sets and $B$ is closed, $x \notin B$ implies (by Theorem 9) $D(B,x) > 0$, so $D(A,x) - D(B,x) < 0$ and $x \in U$. Hence $A \subset U$. Similarly $B \subset V$. Thus $U$ and $V$ are disjoint open sets separating $A$ and $B$, proving normality.

