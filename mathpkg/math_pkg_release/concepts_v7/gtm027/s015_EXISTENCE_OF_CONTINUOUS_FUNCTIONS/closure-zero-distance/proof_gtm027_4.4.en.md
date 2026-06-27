---
role: proof
locale: en
of_concept: closure-zero-distance
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Closure Equals Zero-Distance Set in Pseudo-Metric Spaces

**Theorem 9.** The closure of a set $A$ in a pseudo-metric space is the set of all points which are zero distance from $A$.

*Proof.* Since $D(A,x)$ is continuous in $x$ (by Theorem 8), the set $\{x: D(A,x) = 0\}$ is closed and contains $A$, hence contains the closure $A^{-}$ of $A$. If $y \notin A^{-}$, then there is a neighborhood of $y$, which may be taken to be an open $r$-sphere, which does not intersect $A$. Consequently $D(A,y) \geq r$ and hence $\{x: D(A,x) = 0\} \subset A^{-}$. Therefore $A^{-} = \{x: D(A,x) = 0\}$.

