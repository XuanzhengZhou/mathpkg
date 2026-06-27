---
role: proof
locale: en
of_concept: distance-function-continuity
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Distance to a Set is Continuous

**Theorem 8.** If $A$ is a fixed subset of a pseudo-metric space, then the distance from a point $x$ to $A$ is a continuous function of $x$ relative to the pseudo-metric topology.

*Proof.* Recall that $D(A,x) = \inf \{d(x,z) : z \in A\}$. Since $d(x,z) \leq d(x,y) + d(y,z)$ for all $y \in X$ and $z \in A$, it follows, taking infimum over $z \in A$, that $D(A,x) \leq d(x,y) + D(A,y)$. The same inequality holds with $x$ and $y$ interchanged (by symmetry of $d$), and hence $|D(A,x) - D(A,y)| \leq d(x,y)$. Consequently, if $y$ is in the open $r$-sphere about $x$, then $|D(A,x) - D(A,y)| < r$ and continuity follows.

