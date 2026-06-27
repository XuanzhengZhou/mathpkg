---
role: proof
locale: en
of_concept: corollary-compact-positive-distance
source_book: gtm027
source_chapter: "5"
source_section: "Lebesgue's Covering Lemma"
---

# Proof of Positive Distance from a Compact Set to the Complement of a Neighborhood

**Corollary (to Theorem 26).** If $A$ is a compact subset of a pseudo-metric space $(X, d)$ and $U$ is a neighborhood of $A$, then there is a positive number $r$ such that $U$ contains the open $r$-sphere about every point of $A$; that is, the distance from $A$ to $X \setminus U$ is positive.

*Proof.* Let $V$ be an open set such that $A \subset V \subset U$ (such $V$ exists since $U$ is a neighborhood of $A$; one may take $V = U^\circ$ or use that $A$ is covered by open subsets of $U$). The singleton family $\{V\}$ is an open cover of $A$. Applying Theorem 26 to this cover, there exists $r > 0$ such that for each $x \in A$, the open $r$-sphere about $x$ is contained in $V$, and hence in $U$.

Equivalently, $d(x, X \setminus U) \geq d(x, X \setminus V) \geq r$ for all $x \in A$, so $\operatorname{dist}(A, X \setminus U) = \inf\{d(x, y) : x \in A, y \in X \setminus U\} \geq r > 0$. $\square$
